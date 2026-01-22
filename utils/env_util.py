import os
import sys
from dotenv import load_dotenv

from utils import get_project_root_path

project_root_path = get_project_root_path()
dotenv_path = os.path.join(project_root_path, ".env")

# 加载 .env 文件
if os.path.exists(dotenv_path):
    load_dotenv(dotenv_path)
else:
    # TODO: 加载.env文件失败日志记录
    print(".env文件不存在!")
    sys.exit(1)


def get_url():
    """获取大模型聊天api"""
    try:
        return os.environ["URL"]
    except Exception as e:
        # TODO: 异常日志记录
        raise e


def get_api_key():
    """获取api key"""
    try:
        return os.environ["LLM_API_KEY"]
    except Exception as e:
        # TODO: 异常日志记录
        raise e
