import requests
import re
import json
from util.env_util import get_api_key, get_url
from util.response_util import extract_content

url = get_url()
api_key = get_api_key()
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}


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


def parse_json(response: str):
    """
    解析模型的json回答内容
    :param: response 模型的json回答内容
    :return: 解析后的json结果
    """
    try:
        # 使用正则表达式提取JSON部分
        json_match = re.search(r'```json\s*(.*?)\s*```', response, re.DOTALL)
        if json_match:
            json_str = json_match.group(1)
        else:
            # 如果没有```json标记，尝试直接解析
            json_str = response.strip()

        # 解析JSON
        result = json.loads(json_str)

        return result

    except Exception as e:
        print(f"解析失败: {e}")
        return None
