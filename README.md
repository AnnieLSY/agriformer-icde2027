# AgriFormer

Reproduction package for **AgriFormer: Routing Phenotype Information for
Genotype-Only Prediction under Phenotype Scarcity**. The package provides the
frozen evidence used by the manuscript, train-confined preparation code,
unified model entry points, audit tools, and two reproduction modes.

## Reproduction modes

- **Quick mode** reconstructs Tables I--V and Figs. 3--5 from frozen,
  provenance-linked source data. It does not train a model.
- **Full mode** begins with acquisition and checksum verification of the
  source datasets, then fits all label-derived preparation inside each outer
  training partition, trains AgriFormer or a baseline through one command,
  and writes predictions, metrics, and preparation records.

## Included evidence

The manuscript coverage layer includes all seven dataset split
definitions, explicit train-confined PLS/BayesB preparation, scientific audit
tools, the 30 regressors evaluated only on AUS2015, and 85 outer-fold
preparation records. Locked table/figure source data and provenance are under
`results_reference/manuscript_v1_4/`. See `RELEASE_READINESS_V14.md` and
`CLAIMS_TO_ARTIFACTS.md` for the coverage audit.

## Data availability and acquisition

Third-party raw data are not distributed in this repository. They remain under
their upstream licenses, some sources require acceptance or manual retrieval,
and redistributing one mixed bundle would obscure source attribution and
version identity. Full reproduction therefore starts by downloading the exact
upstream records listed in `data/DOWNLOAD.md` and verifying them with:

```bash
python data/download_and_verify.py verify --data-root /path/to/data
```

All label-derived preparation receives an explicit training-index set.
`agriformer/preparation.py` rejects train/test overlap and silent BayesB
fallback. The deliberately leaky control is isolated under an unmistakable
`naive_out_of_scope_*` name and is never the default.

## Installation

```bash
python -m pip install -r environment/requirements-lock.txt
Rscript environment/restore_R_environment.R
```

The exact tested Python and R package versions are recorded under
`environment/`. Platform-specific accelerator selection is automatic; CPU is
always supported.

## Quick mode: rebuild every manuscript table and figure

```bash
python experiments/reproduce_artifacts.py \
  --reference-dir results_reference/manuscript_v1_4 \
  --out outputs/quick
```

The command writes five LaTeX tables, three figures in PDF and PNG, copied
source-data tables, and a SHA-256 manifest.

## Full mode: source data to predictions

1. Follow `data/DOWNLOAD.md` and place acquired files under a local data root.
2. Verify the exact files with the command above.
3. Run AgriFormer or a baseline through the same entry point:

```bash
python -m agriformer.runner \
  --model agriformer \
  --genotypes /path/to/X.csv \
  --phenotypes /path/to/Y.csv \
  --split-manifest splits/AUS2015/repeat_1_fold_1.csv \
  --target-index 0 --dataset AUS2015 \
  --genotype-mode training_mean \
  --out outputs/full/AUS2015/af_repeat1_fold1
```

Replace `agriformer` with `ridge`, `elasticnet`, `random-forest`, `svr-rbf`,
`lightgbm`, `gblup`, or `bayesb`. Every entry writes the same prediction and
metric schema. Label-derived PLS and BayesB state is fitted only from rows
marked `train` in the split manifest. See
`python -m agriformer.runner --help` for input formats and model options.

The full-mode interface has passed an end-to-end test on synthetic data,
including split loading, train-confined preparation, fitting, prediction and
metric output. The numerical results reported in the manuscript come from the
frozen, audited prediction files in `results_reference/`; they are not replaced
by the synthetic test.

## Table III reproduction map

Table III has 14 displayed model entries. The unified entry can refit eight of
them from source data. Six historical deep-learning controls are reproduced
exactly from their frozen audited predictions; their original method or
experimental code source is identified below.

| Table III entry | Reproduction route | Code source for the reported configuration |
|---|---|---|
| GBLUP | Unified entry, from scratch: `--model gblup` | `agriformer/run_r_baseline.R` |
| BayesB | Unified entry, from scratch: `--model bayesb` | `agriformer/run_r_baseline.R` |
| Ridge | Unified entry, from scratch: `--model ridge` | `agriformer/baselines.py` |
| ElasticNet | Unified entry, from scratch: `--model elasticnet` | `agriformer/baselines.py` |
| RF | Unified entry, from scratch: `--model random-forest` | `agriformer/baselines.py` |
| LightGBM | Unified entry, from scratch: `--model lightgbm` | `agriformer/baselines.py` |
| SVR-RBF | Unified entry, from scratch: `--model svr-rbf` | `agriformer/baselines.py` |
| MLP-Dual | Frozen predictions | Original project runner `fg2_mlp_d_corrected.py`, SHA-256 `828aaf61c0c47e2addf45275b86623600f84a756f8f785df8365f97a7aa9655d`; prediction provenance is in `table_iii_provenance.csv` |
| WheatGP | Frozen predictions | Original adapted runner `hf2_deep.py`, SHA-256 `e8f6d1b7c566f5e186ffd447f594bdb794a3b4eb252f1ee41299a4ecd7276422`, based on [Breed-AI/WheatGP](https://github.com/Breed-AI/WheatGP) commit `a061b8be1d231e21fc89ed7179ae58c2a3048819` |
| Cropformer | Frozen predictions | Original adapted runner `hf2_deep.py` (hash above), based on [jiekesen/Cropformer](https://github.com/jiekesen/Cropformer) commit `e0a77cf699b034d956b249f41b2e1f357f486f06` |
| VMGP | Frozen predictions | Original adapter `vmgp_v13l_cpu_first.py`, SHA-256 `a41613e5be999c7560a82020983e7adcb304a453a719c20226f669e2c132a05b`; authors' source endpoint is reported with DOI `10.1016/j.aiia.2025.06.007` |
| TabNet | Frozen predictions | Original adapter `v13n_c_unit.py`, SHA-256 `4dceff3142ca9f5aa60268c68b4dfff2188ae310153ab8dfaff57700de94d795`; `pytorch-tabnet` 4.1.0 from [dreamquark-ai/tabnet](https://github.com/dreamquark-ai/tabnet) |
| DeepGS | Frozen predictions | Original adapted runner `hf2_deep.py` (hash above), based on [cma2015/DeepGS](https://github.com/cma2015/DeepGS) commit `33ae2dc1ed7bda4e38b76460b18756649d4478a5` |
| AF | Unified entry, from scratch: `--model agriformer` | `agriformer/model.py`, `agriformer/learning.py`, and `agriformer/runner.py` |

For every frozen-only entry, `table_iii_source_data.csv`,
`table_iii_provenance.csv`, and the SHA-256 manifest retain the exact values,
configuration identity and frozen-file lineage used by the manuscript. The
named historical runners are retained in the authors' non-public experiment
archive; they are identified here by filename and SHA-256 rather than being
presented as release-integrated entry points.

## Verification

```bash
python -m unittest discover -s tests -v
python audits/run_all.py
python tools/check_environment_lock.py
```

## Dependencies, licenses, and citation

Project code is MIT licensed. Third-party packages and datasets retain their
own licenses. Dataset licenses and required citations are listed in
`THIRD_PARTY_DATA_LICENSES.md`. The manuscript title and author metadata are
recorded in `CITATION.cff`.

## Release approval

Release remains subject to the authors' final artifact review. The repository
should be published only after that review is complete.
