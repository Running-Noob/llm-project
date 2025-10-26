def extract_content(response: dict) -> str:
    """
    处理大模型API响应，提取响应内容
    :param: response API响应的字典对象
    :return: 提取后的响应内容
    """
    try:
        return response['choices'][0]['message']['content']
    except (KeyError, IndexError):
        return "无法提取内容"
