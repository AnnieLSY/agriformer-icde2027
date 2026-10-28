import unittest
import numpy as np

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


if __name__ == "__main__":
    unittest.main()

