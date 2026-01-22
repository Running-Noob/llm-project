import re
import json


def parse_json(response: str):
    """
    解析模型的json回答内容
    :param response: 模型的json回答内容
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
