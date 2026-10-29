# Audit report: ICDE manuscript commitments

Run date: 2026-10-29 JST  
State: author approval gate active; publication action not performed

## Coverage checks

| Check | Result |
|---|---|
| Seven-dataset cross-validation splits | PASS: 85 manifests; every repeat partitions the material universe exactly once |
| Three wheat fixed holdouts | PASS: 419/75, 315/56 and 266/48 train/test identities are disjoint and complete |
| Preparation identity | PASS: 85 records across seven datasets |
| BayesB effects and selected markers | PASS: exact binary vector hashes; Top-1000 absolute-effect order; readable CSV copies |
| PLS dimensions | PASS: every recorded value is in the declared 1--30 range |
| Fitting rows | PASS: exact match to the training rows of each split manifest |
| Genotype mode and policy | PASS: AUS2015 training-mean `-1` imputation; GABI/Ward original; EasyGeSe supplied preprocessed |
| AUS2015-only Table III supplement | PASS: 30 unique regressors, 75 materials, 46 hashed prediction files |
| Claims-to-artifacts map | PASS: 42 unique, covered material claims; every package-relative path exists |
| Public evidence minimization | PASS: four claim-linked files; five original and five post-October ledger rows |
| Unit tests | PASS: all 23 tests passed, including both R-backed baseline tests, using the locked R environment |
| Sensitive-content scan | PASS: zero usernames, local paths, CJK directory names and credential patterns |

## Commands

```bash
python -m unittest discover -s tests -v
python audits/run_all.py
python audits/scan_sensitive_content.py .
```

The exact machine-readable build counts are in `RELEASE_COVERAGE_BUILD.json`.
The scientific interpretation and approval gate are in
`RELEASE_READINESS_V14.md`.
