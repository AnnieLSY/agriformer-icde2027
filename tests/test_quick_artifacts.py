from pathlib import Path
import tempfile
import unittest

from experiments.reproduce_artifacts import run


class QuickArtifactTests(unittest.TestCase):
    def test_all_five_tables_and_three_figures_are_rebuilt(self):
        root = Path(__file__).resolve().parents[1]
        with tempfile.TemporaryDirectory() as folder:
            out = Path(folder)
            run(root / "results_reference/manuscript_v1_4", out)
            for number in ("i", "ii", "iii", "iv", "v"):
                self.assertTrue((out / f"table_{number}.tex").exists())
            for number in (3, 4, 5):
                self.assertTrue((out / f"fig{number}.pdf").exists())
                self.assertTrue((out / f"fig{number}.png").exists())
            self.assertTrue((out / "MANIFEST.json").exists())


if __name__ == "__main__":
    unittest.main()
