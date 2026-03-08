from langchain_core.messages import SystemMessage, AIMessage
from framework_demo.langgraph.services.llm_service import llm
from framework_demo.langgraph.services.tavily_service import tavily_client
from framework_demo.langgraph.state import SearchState

def understand_query_node(state: SearchState) -> dict:
    """步骤1：理解用户查询并生成搜索关键词"""
    user_message = state["messages"][-1].content

    understand_prompt = f"""分析用户的查询："{user_message}"
    请完成两个任务：
    1. 简洁总结用户想要了解什么
    2. 生成最适合搜索引擎的关键词（中英文均可，要精准）

    格式：
    理解：[用户需求总结]
    搜索词：[最佳搜索关键词]"""

    response = llm.invoke([SystemMessage(content=understand_prompt)])
    response_text = response.content

    # 解析LLM的输出，提取搜索关键词
    search_query = user_message  # 默认使用原始查询
    if "搜索词：" in response_text:
        search_query = response_text.split("搜索词：")[1].strip()
    elif "搜索词:" in response_text:
        search_query = response_text.split("搜索词:")[1].strip()

    return {
        "user_query": response_text,
        "search_query": search_query,
        "step": "understood",
        "messages": [AIMessage(content=f"我将为您搜索：{search_query}")]
    }

def tavily_search_node(state: SearchState) -> dict:
    """步骤2：使用Tavily API进行真实搜索"""
    search_query = state["search_query"]
    try:
        print(f"正在搜索: {search_query}")
        # 调用Tavily搜索API
        response = tavily_client.search(
            query=search_query,
            search_depth="basic",
            include_answer=True,
            include_raw_content=False,
            max_results=5
        )

        # 处理搜索结果
        search_results = ""

        # 优先使用Tavily的综合答案
        if response.get("answer"):
            search_results = f"综合答案：\n{response['answer']}\n\n"

        # 添加具体的搜索结果
        if response.get("results"):
            search_results += "相关信息：\n"
            for i, result in enumerate(response["results"][:3], 1):
                title = result.get("title", "")
                content = result.get("content", "")
                url = result.get("url", "")
                search_results += f"{i}. {title}\n{content}\n来源：{url}\n\n"

        if not search_results:
            search_results = "抱歉，没有找到相关信息。"

        return {
            "search_results": search_results,
            "step": "searched",
            "messages": [AIMessage(content=f"搜索完成！找到了相关信息，正在为您整理答案...")]
        }
    except Exception as e:
        error_msg = f"搜索时发生错误: {str(e)}"
        print(f"{error_msg}")

        return {
            "search_results": f"搜索失败：{error_msg}",
            "step": "search_failed",
            "messages": [AIMessage(content="搜索遇到问题，我将基于已有知识为您回答")]
        }


def generate_answer_node(state: SearchState) -> dict:
    """步骤3：基于搜索结果生成最终答案"""
    if state["step"] == "search_failed":
        # 如果搜索失败，执行回退策略，基于LLM自身知识回答
        fallback_prompt = f"""搜索API暂时不可用，请基于您的知识回答用户的问题：

        用户问题：{state['user_query']}

        请提供一个有用的回答，并说明这是基于已有知识的回答。"""
        response = llm.invoke([SystemMessage(content=fallback_prompt)])
    else:
        # 搜索成功，基于搜索结果生成答案
        answer_prompt = f"""基于以下搜索结果为用户提供完整、准确的答案：

        用户问题：{state['user_query']}

        搜索结果：
        {state['search_results']}

        请要求：
        1. 综合搜索结果，提供准确、有用的回答
        2. 如果是技术问题，提供具体的解决方案或代码
        3. 引用重要信息的来源
        4. 回答要结构清晰、易于理解
        5. 如果搜索结果不够完整，请说明并提供补充建议"""
        response = llm.invoke([SystemMessage(content=answer_prompt)])

    return {
        "final_answer": response.content,
        "step": "completed",
        "messages": [AIMessage(content=response.content)]
    }