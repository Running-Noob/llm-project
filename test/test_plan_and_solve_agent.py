from agents.plan_and_solve_agent import PlanAndSolveAgent
from core.llm import HelloAgentsLLM

if __name__ == "__main__":
    # 模型配置
    model = "Qwen/Qwen3-30B-A3B-Instruct-2507"
    llm_client = HelloAgentsLLM(model=model)

    # plan-and-solve agent实例创建
    plan_and_solve_agent = PlanAndSolveAgent(llm_client)

    # 运行plan-and-solve agent
    question = "一个水果店周一卖出了15个苹果。周二卖出的苹果数量是周一的两倍。周三卖出的数量比周二少了5个。请问这三天总共卖出了多少个苹果？"
    res = plan_and_solve_agent.run(question=question)
    print(f"\n{res}")