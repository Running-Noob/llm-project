def extract_content(response: dict) -> str:
    """
    处理大模型API响应，提取响应内容
    
    Args:
        response: API响应的字典对象
        
    Returns:
        str: 提取的文本内容
    """
    try:
        return response['choices'][0]['message']['content']
    except (KeyError, IndexError):
        return "无法提取内容"