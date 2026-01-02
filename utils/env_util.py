import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()


def get_url():
    """
    获取大模型聊天api
    """
    url = os.environ["URL"]
    return url


def get_api_key():
    """
    获取api key
    """
    api_key = os.environ["LLM_API_KEY"]
    return api_key
