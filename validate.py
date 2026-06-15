"""Validate + pretty-print JSON"""
import json
import sys
from pathlib import Path

def validate(path):
    try:
        data = json.loads(Path(path).read_text())
        print(json.dumps(data, indent=2))
        print("VALID")
    except json.JSONDecodeError as e:
        print(f"INVALID: {e}")
        sys.exit(1)
