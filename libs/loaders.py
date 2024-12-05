import json

def load_asciiart(key:str) -> str:
    with open("data/asciiart.json", "r") as f:
        data = json.load(f)
        return data[key]