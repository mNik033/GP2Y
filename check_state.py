"""Offline regression check: execute the actual state handler with synthetic data."""
import ast
import asyncio
import json
from pathlib import Path
import sys
import time


def check(source):
    tree = ast.parse(Path(source).read_text(encoding="utf-8"))
    handler = next(n for n in tree.body if isinstance(n, ast.AsyncFunctionDef) and n.name == "get_state")
    handler.decorator_list = []
    fixture = {"accounts": [{"id": "fixture", "email": "fixture@example.invalid",
                             "password": "FIXTURE_PASSWORD", "recovery_email": "recovery@example.invalid",
                             "totp_secret": "FIXTURE_SECRET", "proxy": "FIXTURE_PROXY",
                             "unexpected_secret": "FUTURE_SECRET", "status": "pending"}]}
    ns = {"load_config": lambda: fixture, "get_totp": lambda _: "123456",
          "time": time, "ACTIVE_TASKS": {}, "LOGS": [], "BATCH_RUNNING": False}
    exec(compile(ast.Module(body=[handler], type_ignores=[]), str(source), "exec"), ns)
    result = asyncio.run(ns["get_state"]())
    item = result["accounts"][0]
    assert item["id"] == "fixture" and item["email"] == "fixture@example.invalid"
    assert item["is_running"] is False
    forbidden = {"password", "recovery_email", "totp_secret", "totp_now", "totp_rem", "proxy", "unexpected_secret"}
    exposed = sorted(forbidden.intersection(item))
    print(json.dumps({"exposed_account_fields": exposed, "has_totp": item.get("has_totp")}, sort_keys=True))
    if "--require-redacted" in sys.argv:
        assert not exposed and item["has_totp"] is True
    assert fixture["accounts"][0]["password"] == "FIXTURE_PASSWORD"


if __name__ == "__main__":
    check(sys.argv[1] if len(sys.argv) > 1 else Path(__file__).with_name("app.py"))
