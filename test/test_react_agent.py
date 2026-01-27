from agents.react_agent import ReActAgent
from core.llm import HelloAgentsLLM
from tools.executor import ToolExecutor
from tools.search_tool import search

if __name__ == "__main__":
    # 模型配置
    model = "Qwen/Qwen3-30B-A3B-Instruct-2507"
    llm_client = HelloAgentsLLM(model=model)

    # 工具配置
    tool_executor = ToolExecutor()
    search_description = "一个网页搜索引擎。当你需要回答关于时事、事实以及在你的知识库中找不到的信息时，应使用此工具。"
    tool_executor.register_tool("Search", search_description, search)

    # ReAct Agent实例创建
    react_agent = ReActAgent(llm_client=llm_client, tool_executor=tool_executor)

    # 运行ReAct Agent
    question = "英伟达最新的显卡型号是多少"
    answer = react_agent.run(question)
    if answer:
        print(f"\n\n模型的最终回答为: {answer}")