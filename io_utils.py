import pandas as pd
import json

def load_comments(file_path):
    if file_path.endswith(".csv"):
        return pd.read_csv(file_path)
    elif file_path.endswith(".xlsx"):
        return pd.read_excel(file_path)
    elif file_path.endswith(".json"):
        return pd.read_json(file_path)
    else:
        raise ValueError("Unsupported file format")

def write_output(data, path="data/output.json"):
    with open(path, "w") as f:
        json.dump(data, f, indent=2)
