import requests
from utils.env_util import get_api_key, get_url
from utils.response_util import extract_content
from utils.config_util import prompt_config

# 模型请求相关配置
url = get_url()
api_key = get_api_key()
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# 分隔符
delimiter = prompt_config.get("delimiter", "####")


def chat(model: str, prompt: str) -> any:
    """
    聊天函数
    :param: model 模型名称
    :param: prompt 用户输入
    :return: 模型回答
    """
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(url, json=payload, headers=headers)

    return extract_content(response.json())


def chat_with_system_prompt(model: str, system_prompt: str, prompt: str) -> any:
    """
    设定系统提示词的聊天
    :param model: 模型名称
    :param system_prompt: 系统提示词
    :param prompt: 用户输入
    :return: 模型回答
    """
    payload = {
        "model": model,
        "messages": [
            {
                "role": "system",
                "content": system_prompt
            },
            {
                "role": "user",
                "content": f"{delimiter}{prompt}{delimiter}"
            }
        ]
    }

    response = requests.post(url, json=payload, headers=headers)

    return extract_content(response.json())
