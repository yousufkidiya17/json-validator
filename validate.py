"""Validate + pretty-print JSON"""
import json
import sys
from pathlib import Path

def validate(path=None):
    text = Path(path).read_text() if path else sys.stdin.read()
    try:
        data = json.loads(text)
        print(json.dumps(data, indent=2))
        print("VALID")
    except json.JSONDecodeError as e:
        print(f"INVALID at line {e.lineno}, col {e.colno}: {e.msg}")
        sys.exit(1)

if __name__ == "__main__":
    validate(sys.argv[1] if len(sys.argv) > 1 else None)
