import os
from dotenv import load_dotenv

# 加载 .env 文件
load_dotenv()
    
"""
获取大模型聊天api
"""
def get_url():
    url =  os.environ["URL"]
    return url

"""
获取api key
"""
def get_api_key():
    api_key = os.environ["LLM_API_KEY"]
    return api_key