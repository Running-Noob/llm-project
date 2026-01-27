from openai import OpenAI
from typing import List, Dict

from utils.env_util import get_api_key, get_url


class HelloAgentsLLM:
    """
    "Hello Agents"定制的LLM客户端。
    它用于调用任何兼容OpenAI接口的服务，并支持流式响应。
    """

    def __init__(self, model: str = None, api_key: str = None, base_url: str = None, timeout: int = 60):
        """
        初始化客户端。优先使用传入参数，如果未提供，则从环境变量加载。
        """
        self.model = model
        self.api_key = api_key or get_api_key()
        self.base_url = base_url or get_url()

        if not all([self.model, self.api_key, self.base_url]):
            raise ValueError(f"模型ID、API密钥或服务地址缺失: \
                                model: {self.model}, api_key: {self.api_key}, base_url: {self.base_url}")

        self.client = OpenAI(api_key=self.api_key, base_url=self.base_url, timeout=timeout)

    def chat(self, messages: List[Dict[str, str]], **kwargs):
        """
        调用大语言模型进行回答，并返回其响应。
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                **kwargs
            )

            llm_output = response.choices[0].message.content

            return llm_output

        except Exception as e:
            print(f"调用LLM时发生错误: error:{e}")
            raise e

    def chat_streamly(self, messages: List[Dict[str, str]], **kwargs):
        """
        调用大语言模型进行回答，并流式返回其相应。
        """
        try:
            response = self.client.chat.completions.create(
                model=self.model,
                messages=messages,
                stream=True,
                **kwargs
            )

            for chunk in response:
                content = chunk.choices[0].delta.content
                if content:
                    yield content

        except Exception as e:
            print(f"调用LLM时发生错误: error:{e}")
            raise e


# --- 客户端使用示例 ---
if __name__ == '__main__':
    model = "Qwen/Qwen3-30B-A3B-Instruct-2507"
    try:
        llm_client = HelloAgentsLLM(model)

        example_messages = [
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": "你好, 介绍一下你自己"}
        ]

        response_text = llm_client.chat_streamly(example_messages, temperature=0.7, top_p=0.8)

        for content in response_text:
            print(content, end='')

    except Exception as e:
        print(e)