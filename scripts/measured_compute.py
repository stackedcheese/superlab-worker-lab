"""Deterministic CPU-only cloud-runner workload; all data synthetic and public."""
from __future__ import annotations
import argparse, hashlib, json, time
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
ORACLE = ROOT / "fixtures" / "measured_oracle.json"
def compute(count: int, seed: int) -> dict[str, int | str]:
    if not 0 < count <= 2_000_000: raise ValueError("count out of bounded test range")
    state = seed & 0xFFFFFFFF
    positive_cents = negative_cents = positive_count = negative_count = zero_count = 0
    weighted_checksum64 = 0
    h = hashlib.sha256()
    for index in range(count):
        state = (1664525 * state + 1013904223) & 0xFFFFFFFF
        cents = state % 200001 - 100000
        h.update(state.to_bytes(4, "little"))
        if cents > 0:
            positive_cents += cents; positive_count += 1
        elif cents < 0:
            negative_cents += cents; negative_count += 1
        else:
            zero_count += 1
        weighted_checksum64 = (weighted_checksum64 + (index + 1) * (cents + 100000)) & 0xFFFFFFFFFFFFFFFF
    return {"count": count, "seed": seed, "positive_cents": positive_cents,
            "negative_cents": negative_cents, "net_cents": positive_cents + negative_cents,
            "gross_abs_cents": positive_cents - negative_cents, "positive_count": positive_count,
            "negative_count": negative_count, "zero_count": zero_count,
            "weighted_checksum64": weighted_checksum64, "sha256_states": h.hexdigest()}
def mismatches(actual: dict, expected: dict) -> dict[str, dict]:
    return {k: {"expected": v, "actual": actual.get(k)} for k,v in expected.items() if actual.get(k) != v}
def main() -> int:
    p = argparse.ArgumentParser()
    p.add_argument("--inject-one-cent-error", action="store_true")
    args = p.parse_args()
    expected = json.loads(ORACLE.read_text(encoding="utf-8"))
    start = time.perf_counter()
    observed = compute(expected["count"], expected["seed"])
    duration = time.perf_counter() - start
    if args.inject_one_cent_error:
        observed["net_cents"] += 1
    errors = mismatches(observed, expected)
    result = {"schema": "SUPERLAB_PUBLIC_GHA_MEASURED_CPU_V1",
              "mode": "intentional_one_cent_error" if args.inject_one_cent_error else "correct",
              "status": "FAIL" if errors else "PASS", "records_processed": observed["count"],
              "duration_ms": round(duration * 1000, 3),
              "records_per_second": round(observed["count"] / max(duration, 1e-9)),
              "observed": observed, "defects": errors,
              "note": "Public synthetic test only; not native V27 model-worker acceptance"}
    print("MEASURED_CLOUD_RESULT=" + json.dumps(result, sort_keys=True), flush=True)
    if errors:
        print("FAIL: exact oracle mismatch; refusing incorrect result", flush=True)
        return 2
    print("PASS: one million events match ALL fixed oracle fields", flush=True)
    return 0
if __name__ == "__main__":
    raise SystemExit(main())
