from autogen_ext.models.openai import OpenAIChatCompletionClient
from utils.env_util import get_api_key, get_url

def create_openai_model_client(model: str):
    """创建并配置 OpenAI 模型客户端"""
    return OpenAIChatCompletionClient(
        model=model,
        model_info={
            "vision": False,
            "function_calling": False,
            "json_output": False,
            "family": "qwen",  # 模型家族
            "structured_output": True,  # 支持结构化输出
        },
        api_key=get_api_key(),
        base_url=get_url()
    )