import unittest
from pathlib import Path
import numpy as np
import pandas as pd

from agriformer.splits import repeated_kfold


class SplitTests(unittest.TestCase):
    def test_repeated_kfold_is_deterministic_and_disjoint(self):
        left = list(repeated_kfold(31, repeats=2, folds=5))
        right = list(repeated_kfold(31, repeats=2, folds=5))
        self.assertEqual(len(left), 10)
        for (_, _, ltr, lte), (_, _, rtr, rte) in zip(left, right):
            np.testing.assert_array_equal(ltr, rtr)
            np.testing.assert_array_equal(lte, rte)
            self.assertEqual(np.intersect1d(ltr, lte).size, 0)

    def test_frozen_split_manifests_cover_each_dataset_once_per_repeat(self):
        root = Path(__file__).resolve().parents[1] / "splits"
        for dataset_dir in sorted(path for path in root.iterdir() if path.is_dir()):
            index = pd.read_csv(dataset_dir / "SPLIT_INDEX.csv")
            self.assertEqual(len(index), 15)
            for repeat, group in index.groupby("repeat"):
                self.assertEqual(len(group), 5)
                test_ids = []
                expected_ids = None
                for filename in group["manifest"]:
                    manifest = pd.read_csv(dataset_dir / filename, dtype=str)
                    current_ids = set(manifest["material_id"])
                    expected_ids = current_ids if expected_ids is None else expected_ids
                    self.assertEqual(current_ids, expected_ids)
                    test_ids.extend(manifest.loc[manifest["partition"] == "test", "material_id"])
                self.assertEqual(len(test_ids), len(set(test_ids)), msg=f"{dataset_dir.name} repeat {repeat}")
                self.assertEqual(set(test_ids), expected_ids)


if __name__ == "__main__":
    unittest.main()

