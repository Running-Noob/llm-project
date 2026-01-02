from utils.chat_util import chat

# 确定模型
model = "Qwen/Qwen3-30B-A3B-Instruct-2507"


def reverse():
    prompt = "Take the letters in lollipop and reverse them"
    print(chat(model, prompt))


if __name__ == "__main__":
    reverse()
