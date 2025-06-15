import requests
from config import TACHYON_BASE_URL, HEADERS, VECTOR_STORE_NAME

def upload_and_ingest(file_path):
    upload_url = f"{TACHYON_BASE_URL}/file-upload"
    ingest_url = f"{TACHYON_BASE_URL}/ingest"

    files = {"file": open(file_path, "rb")}
    upload_resp = requests.post(upload_url, headers=HEADERS, files=files)

    if not upload_resp.ok:
        raise Exception(f"Upload failed: {upload_resp.text}")

    file_id = upload_resp.json()["file_id"]
    ingest_resp = requests.post(ingest_url, headers=HEADERS, json={
        "file_id": file_id,
        "vector_store": VECTOR_STORE_NAME
    })

    if not ingest_resp.ok:
        raise Exception(f"Ingest failed: {ingest_resp.text}")
