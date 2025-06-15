import requests
from config import TACHYON_BASE_URL, HEADERS, VECTOR_STORE_NAME

def get_embedding(text):
    url = f"{TACHYON_BASE_URL}/embedding"
    headers = HEADERS.copy()
    headers.update({
        "file-name": "placeholder.txt",
        "vector-store": VECTOR_STORE_NAME
    })

    response = requests.post(url, headers=headers, json={"text": text})
    if response.ok:
        return response.json()["embedding"]
    else:
        raise Exception(f"Embedding API Error: {response.status_code} - {response.text}")
