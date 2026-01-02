from utils.chat_util import chat

# 确定模型
model = "Qwen/Qwen3-30B-A3B-Instruct-2507"


def chat_in_text_transform():
    """
    一、文本翻译
    """

    # prompt = f"""
    # 将以下中文翻译成西班牙语: \
    # ```您好，我想订购一个搅拌机。```
    # """

    # prompt = f"""
    # 请将以下文本分别翻译成中文、英文、法语和西班牙语:
    # ```I want to order a basketball.```
    # """

    """
    二、文件格式转换
    """

    # data_json = {"restaurant employees": [
    #     {"name": "Shyam", "email": "shyamjaiswal@gmail.com"},
    #     {"name": "Bob", "email": "bob32@gmail.com"},
    #     {"name": "Jai", "email": "jai87@gmail.com"}
    # ]}
    # prompt = f"""
    # 将以下Python字典从JSON转换为HTML表格，保留表格标题和列名：{data_json}
    # """
    #

    """
    三、拼写及语法校正
    """
    text = [
        "The girl with the black and white puppies have a ball.",  # The girl has a ball.
        "Yolanda has her notebook.",  # ok
        "Its going to be a long day. Does the car need it’s oil changed?",  # Homonyms
        "Their goes my freedom. There going to bring they’re suitcases.",  # Homonyms
        "Your going to need you’re notebook.",  # Homonyms
        "That medicine effects my ability to sleep. Have you heard of the butterfly affect?",  # Homonyms
        "This phrase is to cherck chatGPT for spelling abilitty"  # spelling
    ]

    prompt = f"""请校对并更正以下文本，注意纠正文本保持原始语种，无需输出原始文本。
    如果您没有发现任何错误，请说“未发现错误”。

    例如：
    输入：I are happy.
    输出：I am happy.
    ```{text}```"""
    print(chat(model, prompt))


if __name__ == "__main__":
    chat_in_text_transform()
