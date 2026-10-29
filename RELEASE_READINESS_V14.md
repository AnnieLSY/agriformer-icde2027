# Manuscript reproduction-coverage audit

Audit date: 2026-10-29 JST  
Manuscript: current ICDE submission manuscript  
Evidence state: minimized public claim-level snapshot  
Publication state: **author approval gate active**

## Result

All five commitments requested for this audit are represented by concrete
package artifacts:

1. **Seven-dataset splits:** 85 cross-validation manifests cover the seven
   datasets, and the three wheat fixed holdouts are included.
2. **Train-confined preparation code:** PLS, genotype handling and BayesB use
   explicit training indices; train/test overlap and silent BayesB fallback are
   rejected.
3. **Audit tools:** scientific identity audits cover splits, preparation
   records, the AUS-only 30-regressor supplement and claim-path completeness.
4. **Table III supplement:** 30 AUS2015-only regressors are listed, with 46
   copied prediction files and SHA-256 values.
5. **Preparation identity:** 85 outer-fold records retain genotype policy, PLS
   dimension, complete BayesB coefficients, selected marker indices/names and
   fitting rows.

The manuscript-wide claim map contains 42 material claims and points each one
to a package-relative file. Locked table/figure source data and provenance are
copied under `results_reference/manuscript_v1_4/`; minimized evidence and ledger
snapshots are under `evidence_snapshot/`.

The complete internal ledgers and release-build scripts are retained outside
the public repository. The public evidence directory contains only files
referenced by the claim map and only the ten claim-level ledger rows required
by those references.

## Interpretation of the RQ4 record promise

In the RQ4 sentence, *coefficients and marker indices* refer to the BayesB
effect vector and Top-1000 marker order used by EMV. Both are frozen for every
outer fold. PLS dimension and projected-score hashes are also frozen. The
public `TrainScopedPLS` implementation exports full PLS scaler, weight, loading
and rotation state when full mode is rerun; the historical caches did not
serialize a separate projection matrix. This boundary is stated explicitly
in `preparation_records/README.md` and is not hidden by the coverage label.

## Approval gate

No public remote has been created, and no upload, push or release tag has been
performed. Public release remains blocked until the user reviews this report,
the claim map, audit output and author metadata, then gives explicit approval.
