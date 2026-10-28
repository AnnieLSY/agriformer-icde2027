"""Train-confined preparation primitives with explicit leakage guards."""

from __future__ import annotations

from dataclasses import dataclass
import numpy as np
from sklearn.cross_decomposition import PLSRegression

from .splits import assert_disjoint


@dataclass(frozen=True)
class FoldScope:
    train_indices: np.ndarray
    test_indices: np.ndarray

    def __post_init__(self):
        assert_disjoint(self.train_indices, self.test_indices)


@dataclass
class MarkerMeanTransform:
    means: np.ndarray

    @classmethod
    def fit(cls, X: np.ndarray, scope: FoldScope):
        train = np.asarray(scope.train_indices, dtype=int)
        means = np.nanmean(np.asarray(X, dtype=float)[train], axis=0)
        means[~np.isfinite(means)] = 0.0
        return cls(means=means)

    def transform(self, X: np.ndarray, indices):
        values = np.asarray(X, dtype=float)[np.asarray(indices, dtype=int)]
        return np.where(np.isnan(values), self.means, values)


@dataclass
class PLSContextTransform:
    imputer: MarkerMeanTransform
    model: PLSRegression

    @classmethod
    def fit(cls, X: np.ndarray, y: np.ndarray, scope: FoldScope, n_components: int):
        train = np.asarray(scope.train_indices, dtype=int)
        imputer = MarkerMeanTransform.fit(X, scope)
        X_train = imputer.transform(X, train)
        y_train = np.asarray(y, dtype=float)[train]
        model = PLSRegression(n_components=int(n_components), scale=True)
        model.fit(X_train, y_train)
        return cls(imputer=imputer, model=model)

    def transform(self, X: np.ndarray, indices):
        values = self.imputer.transform(X, indices)
        return self.model.transform(values)


def naive_out_of_scope_fit_pls(X: np.ndarray, y: np.ndarray, n_components: int):
    """Intentionally leaky comparator; never use for normative evaluation."""
    values = np.asarray(X, dtype=float)
    means = np.nanmean(values, axis=0)
    means[~np.isfinite(means)] = 0.0
    filled = np.where(np.isnan(values), means, values)
    model = PLSRegression(n_components=int(n_components), scale=True)
    model.fit(filled, np.asarray(y, dtype=float))
    return model, means

