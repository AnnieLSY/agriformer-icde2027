# Public method-evidence snapshot

This minimized snapshot retains only the method contract cited by
`CLAIMS_TO_ARTIFACTS.tsv` (`METHOD-03`). The complete internal evidence map is
preserved outside the public repository.

## Phenotype-routing contract

| Component | Public definition | Permitted phenotype use | Inference input |
|---|---|---|---|
| SBV | Scoped Background View: PLS scores fitted within the training partition | Target labels may be used only while fitting PLS on training rows | Genotype-derived scores |
| EMV | Effect-Ordered Marker View: top-K markers selected and ordered by training-partition BayesB absolute effects | Target labels may be used only while fitting BayesB on training rows | Selected genotype markers |
| TAS | Train-Only Auxiliary Supervision: a yield-centred multi-output training head | Auxiliary phenotypes are training outputs only | None |

AgriFormer receives genotype-derived inputs at inference. Auxiliary phenotype
heads are removed from the inference interface, and the runner returns only
the target-trait prediction.

The preparation scope is enforced by explicit training indices. Held-out rows
are rejected by the preparation code if they overlap the supplied training
partition.
