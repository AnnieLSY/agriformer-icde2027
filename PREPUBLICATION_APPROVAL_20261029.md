# Prepublication approval checkpoint

Date: 2026-10-29 JST

## Completed locally

- `CITATION.cff` uses the ICDE manuscript title.
- Release-facing provenance uses neutral wording and machine-local roots are
  represented only by descriptive placeholders.
- `README.md` documents quick and full reproduction, including why raw data
  are obtained from their upstream sources rather than redistributed here.
- `experiments/reproduce_artifacts.py` reconstructs Tables I--V and Figs. 3--5
  from the frozen manuscript source data without model training.
- `python -m agriformer.runner` exposes AgriFormer and the registered Python/R
  baselines through one input, split, prediction, metric, and metadata schema.
- Train-scoped PLS and BayesB preparation reject overlap and silent fallback;
  preparation outputs include fitting rows, PLS state, BayesB coefficients,
  and selected marker indices.
- Python and R environments are exactly recorded under `environment/`.
- Automated tests cover the model forward pass, one-epoch AF training, the
  unified AF/Python entry, both R backends when R is available, quick artifact
  reconstruction, split/preparation confinement, wording, and lock files.
- The public evidence snapshot is reduced to the four files referenced by the
  claims map and to five rows in each ledger. The complete ledgers are retained
  outside the public repository.
- Release-build-only freeze and sanitization scripts have been moved outside
  the public repository.
- Table III's 14 entries have an explicit reproduction route and original code
  source in `README.md`.
- Sensitive-content scanning reports zero usernames, local paths, CJK
  directory names and credential patterns.

## Publication actions deliberately not performed

- no remote created or changed;
- no upload or push;
- no release or public archive;
- no `v1.0-icde2027-submission` tag.

## Final author review requested

Before publication, confirm the author metadata in `CITATION.cff`, inspect the
quick-mode figures and tables, and approve the repository snapshot explicitly.
