"""Small, dependency-free GitHub connector round-trip test.

This file is intentionally public and contains no credentials.
Run: python tests/connector_roundtrip.py --name ChatGPT
"""
from __future__ import annotations

import argparse
import json


def make_result(name: str) -> dict[str, object]:
    """Return a deterministic, serializable result for connector testing."""
    return {
        "ok": True,
        "source": "katelkum/chatgptcodebase",
        "message": f"Ciao, {name}!",
        "roundtrip_version": 2,
        "checks": {"read": True, "write": True, "python": True},
    }


def main() -> None:
    parser = argparse.ArgumentParser(description="Test GitHub codebase round trip")
    parser.add_argument("--name", default="ChatGPT")
    args = parser.parse_args()
    print(json.dumps(make_result(args.name), ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()
