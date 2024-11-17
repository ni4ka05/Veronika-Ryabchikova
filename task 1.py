import json

INPUT_FILE = "input.json"


def task() -> float:
    with open(INPUT_FILE) as f:
        json_data = json.load(f)

    total = sum([item["score"] * item["weight"] for item in json_data])
    return round(total, 3)

print(task())
