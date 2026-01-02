import re
import json


def extract_content(response: dict) -> str:
    """
    处理大模型API响应，提取响应内容
    :param: response API响应的字典对象
    :return: 提取后的响应内容
    """
    try:
        return response['choices'][0]['message']['content']
    except (KeyError, IndexError) as e:
        return f"Fail to extract content, error: {str(e)}"


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
        print(f"Fail to parse json, error: {str(e)}")
        return None
