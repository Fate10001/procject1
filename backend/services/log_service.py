import json
import os
from datetime import datetime

class LogService:
    def __init__(self, log_dir="logs"):
        self.log_dir = log_dir
        os.makedirs(self.log_dir, exist_ok=True)

    def write(self, task_id: str, record: dict):
        path = os.path.join(self.log_dir, f"{task_id}.jsonl")
        record["created_at"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(path, "a", encoding="utf-8") as f:
            f.write(json.dumps(record, ensure_ascii=False) + "\n")
