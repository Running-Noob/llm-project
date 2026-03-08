import asyncio
from typing import List

from autogen_agentchat.teams import RoundRobinGroupChat
from autogen_agentchat.conditions import TextMentionTermination
from autogen_agentchat.ui import Console

from framework_demo.autogen.agent import (
    create_user_proxy,
    create_engineer,
    create_code_reviewer,
    create_product_manager
)

from framework_demo.autogen.model_client import create_openai_model_client

def build_default_agents(model_client):
    """
    构建软件开发团队Agent
    """
    return [
        create_product_manager(model_client),
        create_engineer(model_client),
        create_code_reviewer(model_client),
        create_user_proxy(),
    ]

def create_software_development_team(agents: List):
    """
    创建软件开发团队
    """
    return RoundRobinGroupChat(
        participants=agents,
        termination_condition=TextMentionTermination("TERMINATE"),
        max_turns=20,
    )

async def run_team(task: str, model: str):
    """
    运行软件开发团队
    """
    # 1 创建模型
    model_client = create_openai_model_client(model)
    # 2 创建 agents
    agents = build_default_agents(model_client)
    # 3 创建 team
    team = create_software_development_team(agents)
    # 4 执行任务
    return await Console(team.run_stream(task=task))

async def main():
    task = """我们需要开发一个比特币价格显示应用，具体要求如下：
            核心功能：
            - 实时显示比特币当前价格（USD）
            - 显示24小时价格变化趋势（涨跌幅和涨跌额）
            - 提供价格刷新功能

            技术要求：
            - 使用 Streamlit 框架创建 Web 应用
            - 界面简洁美观，用户友好
            - 添加适当的错误处理和加载状态

            请团队协作完成这个任务，从需求分析到最终实现。"""

    result = await run_team(
        task=task,
        model="Qwen/Qwen3-Coder-30B-A3B-Instruct"
    )

    print(result)


if __name__ == "__main__":
    asyncio.run(main())