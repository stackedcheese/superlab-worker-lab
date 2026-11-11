"""Independent exact-oracle and fault-injection checks. No extra dependencies."""
from __future__ import annotations
import importlib.util, json, unittest
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
spec = importlib.util.spec_from_file_location("measured_compute", ROOT/"scripts"/"measured_compute.py")
assert spec and spec.loader
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
ORACLE = json.loads((ROOT/"fixtures"/"measured_oracle.json").read_text("utf-8"))
class DeterministicCloudWorkerTests(unittest.TestCase):
    def test_one_million_records_equal_fixed_oracle(self):
        self.assertEqual(module.mismatches(module.compute(ORACLE["count"], ORACLE["seed"]), ORACLE), {})
    def test_balances_and_population_invariants(self):
        r = module.compute(1000, 20261110)
        self.assertEqual(r["count"], r["positive_count"]+r["negative_count"]+r["zero_count"])
        self.assertEqual(r["net_cents"], r["positive_cents"]+r["negative_cents"])
        self.assertEqual(r["gross_abs_cents"], r["positive_cents"]-r["negative_cents"])
    def test_one_cent_tamper_is_detected(self):
        self.assertIn("net_cents", module.mismatches(dict(ORACLE, net_cents=ORACLE["net_cents"]+1), ORACLE))
        self.assertEqual(module.mismatches(ORACLE, ORACLE), {})
    def test_wrong_sha256_is_detected(self):
        self.assertIn("sha256_states", module.mismatches(dict(ORACLE, sha256_states="0"*64), ORACLE))
    def test_invalid_count_rejected(self):
        with self.assertRaises(ValueError): module.compute(0, 1)
        with self.assertRaises(ValueError): module.compute(2_000_001, 1)
if __name__ == "__main__":
    unittest.main()
