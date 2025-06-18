# clients/llm_client.py

import requests
from config.settings import (
    TACHYON_API_KEY,
    TACHYON_CHAT_COMPLETION_URL,
    PREDEFINED_CATEGORIES
)

HEADERS = {
    "Authorization": f"Bearer {TACHYON_API_KEY}",
    "Content-Type": "application/json"
}

def classify_comment_with_llm(comment: str) -> dict:
    categories_list = ", ".join(PREDEFINED_CATEGORIES)
    
    prompt = (
        f"You are a customer feedback classifier.\n"
        f"Classify the following user comment into one of the predefined categories:\n"
        f"[{categories_list}].\n"
        f"Return the result in JSON format like this:\n"
        f'{{"category": "<category>", "confidence": <score between 0 and 1>}}.\n\n'
        f"Comment: \"{comment}\""
    )

    payload = {
        "messages": [
            {"role": "system", "content": "You classify customer comments into categories."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.3,
        "max_tokens": 100
    }

    response = requests.post(
        TACHYON_CHAT_COMPLETION_URL,
        headers=HEADERS,
        json=payload
    )

    if response.status_code != 200:
        print(f"LLM classification failed: {response.status_code} - {response.text}")
        return {"category": "", "confidence": 0.0}

    try:
        content = response.json()["choices"][0]["message"]["content"]
        result = eval(content)  # optionally replace with json.loads() if safer
        return {
            "category": result.get("category", ""),
            "confidence": result.get("confidence", 0.0)
        }
    except Exception as e:
        print(f"Failed to parse LLM output: {e}")
        return {"category": "", "confidence": 0.0}
