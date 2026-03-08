from agents.reflection_agent import ReflectionAgent
from core.llm import HelloAgentsLLM

if __name__ == "__main__":
    # 模型配置
    model = "Qwen/Qwen3-30B-A3B-Instruct-2507"
    llm_client = HelloAgentsLLM(model=model)

    # reflection agent实例创建
    reflection_agent = ReflectionAgent(llm_client)

    # 运行reflection agent
    task = "编写一个Python函数，找出1到n之间所有的素数 (prime numbers)。"
    reflection_agent.run(task=task)