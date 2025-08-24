import requests
from util.env_util import get_api_key, get_url
from util.response_util import extract_content

url = get_url()
api_key = get_api_key()
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

def chat(model: str, prompt: str) -> any:
    payload = {
        "model": model,
        "messages": [
            {
                "role": "user",
                "content": prompt
            }
        ]
    }

    response = requests.post(url, json=payload, headers=headers)

    return extract_content(response.json())