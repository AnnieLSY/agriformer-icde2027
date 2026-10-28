import unittest
import numpy as np

from agriformer.preparation import FoldScope, MarkerMeanTransform


class PreparationTests(unittest.TestCase):
    def test_overlap_is_rejected(self):
        with self.assertRaisesRegex(ValueError, "overlap"):
            FoldScope(np.array([0, 1]), np.array([1, 2]))

    def test_test_values_do_not_affect_training_means(self):
        X = np.array([[0.0, np.nan], [2.0, 4.0], [999.0, 999.0]])
        scope = FoldScope(np.array([0, 1]), np.array([2]))
        fitted = MarkerMeanTransform.fit(X, scope)
        np.testing.assert_allclose(fitted.means, [1.0, 4.0])


if __name__ == "__main__":
    unittest.main()

