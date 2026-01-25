from openai import OpenAI

from utils.env_util import get_api_key, get_url
from utils.config_util import prompt_config_dict

# 模型相关配置
url = get_url()
api_key = get_api_key()

client = OpenAI(
    base_url=url,
    api_key=api_key
)

# 分隔符
delimiter = prompt_config_dict.get("delimiter", "####")
# 默认的系统提示词
_system_prompt = prompt_config_dict.get("system_prompt", "")


def chat(model: str, prompt: str, system_prompt: str = _system_prompt):
    """
    聊天函数
    :param model: 模型名称
    :param prompt: 用户输入
    :param system_prompt: 系统提示词
    :return: 模型回答
    """
    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        raise e


def chat_streamly(model: str, prompt: str, system_prompt: str = _system_prompt):
    """
    聊天函数，流式输出
    :param model: 模型名称
    :param prompt: 用户输入
    :param system_prompt: 系统提示词
    :return: 模型回答
    """
    messages = [
        {
            "role": "system",
            "content": system_prompt
        },
        {
            "role": "user",
            "content": prompt
        }
    ]
    try:
        response = client.chat.completions.create(
            model=model,
            messages=messages,
            stream=True
        )
        for chunk in response:
            content = chunk.choices[0].delta.content
            if content:
                yield content
    except Exception as e:
        raise e
