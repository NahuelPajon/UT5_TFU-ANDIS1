import json
from pathlib import Path

DATA_DIR = Path(__file__).parent.parent / "data"

def read_json(filename: str) -> list:
    path = DATA_DIR / filename
    if not path.exists():
        return []
    with open(path, "r", encoding="utf-8") as f:
        return json.load(f)

def write_json(filename: str, data: list) -> None:
    path = DATA_DIR / filename
    with open(path, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)