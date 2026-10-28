# AgriFormer ICDE 2027 reproduction package

This is a **local, private, work-in-progress artifact** for the ICDE 2027
submission. It has not been uploaded or released. The repository is being
built from a clean history so that experimental caches, obsolete runs,
machine-specific paths, and credentials are never inherited from the research
workspace.

## Reproduction modes

- **Quick mode** recomputes metrics, tables, and figures from the frozen
  per-sample predictions under `results_reference/`.
- **Full mode** starts from source datasets, fits all label-derived preparation
  inside the outer training partition, trains models, and evaluates once on
  held-out samples. Full-mode experiment entry points are being added in
  stages.

## Current status

The repository skeleton, metadata, data-license register, checksum manifest,
canonical metrics, split utilities, leakage guard, and initial tests are in
place. Reference predictions and the unified experiment entry points are being
integrated. See `../RELEASE_BUILD_REPORT.md` for the authoritative build state.

## Safety and scope

Third-party raw data are not committed by default. Download the exact upstream
versions described in `data/DOWNLOAD.md`, then verify them with:

```bash
python data/download_and_verify.py verify --data-root /path/to/downloads
```

All label-derived preparation must receive an explicit training-index set.
`agriformer/preparation.py` rejects train/test overlap and silent fallback.
The intentionally leaky comparison used by one controlled experiment is kept
under an unmistakable `naive_out_of_scope_*` name and is never the default.

## Quick verification

```bash
python -m pip install -r environment/requirements.txt
python -m unittest discover -s tests -v
python experiments/reproduce_tables.py --reference-dir results_reference --out outputs/quick
```

## Dependencies and licenses

This project code is MIT licensed. It calls, but does not redistribute, third-
party packages including NumPy, pandas, SciPy, scikit-learn, PyTorch, BGLR,
and rrBLUP; those packages retain their own licenses. Dataset licenses and
required citations are listed in `THIRD_PARTY_DATA_LICENSES.md`.

## Citation

The manuscript citation will be updated after publication. Author metadata in
`CITATION.cff` was extracted from the final submitted manuscript source and
must be confirmed before public release.

