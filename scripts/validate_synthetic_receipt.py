from __future__ import annotations

import json
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parents[1]


def load_json(path: str) -> dict[str, object]:
    value = json.loads((ROOT / path).read_text(encoding="utf-8"))
    if not isinstance(value, dict):
        raise SystemExit(f"FAIL: {path} must contain a JSON object")
    return value


def safe_paths(values: object, label: str) -> set[str]:
    if not isinstance(values, list) or any(not isinstance(value, str) for value in values):
        raise SystemExit(f"FAIL: {label} must be an array of path strings")
    paths: set[str] = set()
    for value in values:
        path = PurePosixPath(value)
        if path.is_absolute() or not path.parts or any(part in {".", ".."} for part in path.parts):
            raise SystemExit(f"FAIL: unsafe path in {label}: {value}")
        resolved = ROOT.joinpath(*path.parts).resolve()
        if not resolved.is_relative_to(ROOT) or not resolved.is_file():
            raise SystemExit(f"FAIL: missing or out-of-repository path in {label}: {value}")
        if value in paths:
            raise SystemExit(f"FAIL: duplicate path in {label}: {value}")
        paths.add(value)
    return paths


def main() -> None:
    task = load_json("fixtures/synthetic-task.json")
    receipt = load_json("fixtures/synthetic-receipt.json")
    task_id = task.get("task_id")
    if not isinstance(task_id, str) or not task_id.startswith("SYN-"):
        raise SystemExit("FAIL: task_id must identify a synthetic task")
    if receipt.get("task_id") != task_id or receipt.get("sample_only") is not True:
        raise SystemExit("FAIL: receipt must match the synthetic task and be sample_only")
    if receipt.get("status") != "complete" or receipt.get("review_status") != "pending":
        raise SystemExit("FAIL: sample status must be complete and review must remain pending")
    if any(task.get(key) != "deny" for key in ("external_access", "paid_usage", "secret_access")):
        raise SystemExit("FAIL: external access, paid usage, and secret access must be denied")

    allowed_reads = safe_paths(task.get("allowed_read_paths"), "allowed_read_paths")
    allowed_writes = safe_paths(task.get("allowed_write_paths"), "allowed_write_paths")
    if not safe_paths(receipt.get("files_read"), "files_read") <= allowed_reads:
        raise SystemExit("FAIL: receipt reports a read outside the task allowlist")
    if not safe_paths(receipt.get("files_changed"), "files_changed") <= allowed_writes:
        raise SystemExit("FAIL: receipt reports a change outside the task allowlist")

    checks = receipt.get("checks")
    if not isinstance(checks, list) or not checks or any(
        not isinstance(check, dict) or check.get("result") != "passed" for check in checks
    ):
        raise SystemExit("FAIL: all synthetic sample checks must pass")
    print("PASS: synthetic task and receipt satisfy path and deny-by-default checks.")
    print("Review remains pending; this result does not dispatch or accept worker work.")


if __name__ == "__main__":
    main()
