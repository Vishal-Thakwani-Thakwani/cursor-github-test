from datetime import datetime


def get_timestamp() -> str:
    return datetime.now().isoformat()


def format_greeting(name: str, time: str) -> str:
    return f"[{time}] Welcome, {name}!"
