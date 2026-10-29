import json
from pathlib import Path
import unittest
import yaml

from audits.audit_public_wording import audit
from audits.audit_public_evidence_snapshot import audit as audit_snapshot


class ReleaseWordingAndLockTests(unittest.TestCase):
    def setUp(self):
        self.root = Path(__file__).resolve().parents[1]

    def test_public_wording_audit(self):
        self.assertTrue(audit(self.root).startswith("PASS"))

    def test_public_evidence_snapshot_is_minimal(self):
        finding = audit_snapshot(self.root)
        self.assertEqual(finding, {"files": 4, "original_rows": 5, "post_rows": 5})

    def test_readme_lists_all_table_iii_entries(self):
        text = (self.root / "README.md").read_text()
        expected = {
            "GBLUP", "BayesB", "Ridge", "ElasticNet", "RF", "LightGBM",
            "SVR-RBF", "MLP-Dual", "WheatGP", "Cropformer", "VMGP",
            "TabNet", "DeepGS", "AF",
        }
        rows = {
            line.split("|")[1].strip()
            for line in text.splitlines()
            if line.startswith("|") and line.count("|") >= 3
        }
        self.assertTrue(expected <= rows)

    def test_python_lock_uses_exact_versions(self):
        rows = [line for line in (self.root / "environment/requirements-lock.txt").read_text().splitlines() if line and not line.startswith("#")]
        self.assertTrue(rows)
        self.assertTrue(all("==" in line and ">=" not in line and "<" not in line for line in rows))

    def test_r_lock_has_runtime_and_required_packages(self):
        lock = json.loads((self.root / "environment/renv.lock").read_text())
        self.assertEqual(lock["R"]["Version"], "4.5.3")
        self.assertEqual(lock["Packages"]["BGLR"]["Version"], "1.1.4")
        self.assertEqual(lock["Packages"]["rrBLUP"]["Version"], "4.6.3")
        self.assertEqual(lock["Packages"]["truncnorm"]["Version"], "1.0.9")
        self.assertEqual(lock["Packages"]["MASS"]["Version"], "7.3.66")

    def test_citation_uses_icde_title(self):
        citation = yaml.safe_load((self.root / "CITATION.cff").read_text())
        self.assertEqual(citation["title"], "AgriFormer: Routing Phenotype Information for Genotype-Only Prediction under Phenotype Scarcity")
        self.assertEqual(citation["version"], "1.0.0")


if __name__ == "__main__":
    unittest.main()
