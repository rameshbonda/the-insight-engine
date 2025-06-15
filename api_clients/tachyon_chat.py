import requests
from config import TACHYON_BASE_URL, HEADERS, PREDEFINED_CATEGORIES

def classify_comment(comment):
    url = f"{TACHYON_BASE_URL}/chat-completion"
    prompt = f"""Classify the following client comment into one of these categories:
{', '.join(PREDEFINED_CATEGORIES)}. 
Comment: "{comment}"
Respond in format: Category: <category>"""

    response = requests.post(url, headers=HEADERS, json={
        "messages": [{"role": "user", "content": prompt}]
    })

    if response.ok:
        output = response.json()["choices"][0]["message"]["content"]
        category = output.replace("Category:", "").strip()
        return category
    else:
        raise Exception(f"LLM API Error: {response.status_code} - {response.text}")
