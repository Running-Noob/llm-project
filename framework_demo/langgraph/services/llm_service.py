from langchain_openai import ChatOpenAI
from utils.env_util import get_api_key, get_url

llm = ChatOpenAI(
    model="Qwen/Qwen3-Coder-30B-A3B-Instruct",
    api_key=get_api_key(),
    base_url=get_url(),
)