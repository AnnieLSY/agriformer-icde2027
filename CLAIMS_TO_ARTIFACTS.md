# Claims-to-artifacts map for the manuscript

This map was rebuilt against `ICDE_manuscript/v1.4/main.pdf` and the locked
claim--evidence state **v5.5**. The physical evidence-map filename remains
`ICDE_evidence_map_v5_20261028.md`; its header records the v5.5 update dated
2026-10-29, and `manuscript-profile.yml` identifies the companion frozen
manuscript state. Sanitized supporting snapshots are retained under
`evidence_snapshot/`.

The complete row-level map is `CLAIMS_TO_ARTIFACTS.tsv`. It contains 42
material manuscript claims. Each row names the PDF location, the claim, the
v5.5 evidence section, package-relative artifacts, the verification method and
coverage status. `audits/audit_claims_to_artifacts.py` rejects duplicate IDs,
missing paths and any status other than `covered`.

## Five publication commitments requested for this audit

| Commitment in v1.4 | Package coverage | Verification |
|---|---|---|
| Seven-dataset split definitions | `splits/` contains 85 cross-validation manifests (45 wheat, 40 EasyGeSe) and three wheat fixed holdouts | `audits/audit_splits.py`; `tests/test_split_identity.py` |
| Preparation fitted only inside training partitions | `agriformer/preparation.py` requires an explicit disjoint `FoldScope`; `run_bayesb_select.R` is a hard-failure BayesB entry point with no silent first-K fallback | `tests/test_train_confined_preparation.py` |
| Audit tools | Split identity, preparation-state identity, AUS-only result coverage, claim-path coverage and sensitive-content audits are under `audits/` | `audits/run_all.py` |
| Results for 30 regressors evaluated only on AUS2015 | `results_reference/table_iii/aus2015_only_30_regressors.csv` plus a hash manifest for 46 underlying prediction files | `audits/audit_aus_only_regressors.py` |
| Preparation settings and identity | 85 records contain genotype mode/policy, PLS dimension, complete BayesB coefficient vector, Top-1000 indices/names/effects and exact fitting rows | `preparation_records/README.md`; `audits/audit_preparation_records.py` |

## Claim groups

- **Literature and data profile:** `LIT-01`, `DATA-01`--`DATA-02`.
- **Prediction contract and method:** `CONTRACT-01`, `METHOD-01`--`METHOD-06`.
- **Evaluation protocol:** `PROTOCOL-01`--`PROTOCOL-02`.
- **RQ1:** `RQ1-01`--`RQ1-05`, including the Table III 30-regressor note.
- **RQ2:** `RQ2-01`--`RQ2-06`.
- **RQ3:** `RQ3-01`--`RQ3-04`.
- **RQ4:** `RQ4-01`--`RQ4-04`, including the preparation-identity promise.
- **RQ5:** `RQ5-01`--`RQ5-06`.
- **Explicit release promises:** `RELEASE-01`--`RELEASE-05`.

The package remains local. This map does not authorize publication, creation
of a public remote, upload, push or release tag.
