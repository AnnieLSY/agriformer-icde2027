# Frozen reference results

These files support the artifact's quick mode. They are copied, not linked,
from the verified research workspace and contain no model checkpoints, caches,
runtime logs, or machine-specific paths.

Current initial import:

- `rq1_holdout/agriformer_external/`: five fixed-holdout AgriFormer predictions
  for each of GABI and Ward, including all trait outputs.
- `rq1_holdout/e6_standard/`: standard fixed-holdout classical controls for
  AUS2015, GABI, and Ward.
- `rq1_holdout/hf2_additional/`: normally tuned additional holdout controls for
  GABI and Ward.
- `rq1_holdout/aus_historical/`: the frozen seed-42 matrix from the final
  Genome Biology submission package. It is preserved for provenance and is
  not by itself a claim of state-of-the-art superiority.
- `summaries/`: frozen aggregate panels and paired-comparison summaries.

`REFERENCE_MANIFEST.tsv` records size and SHA-256 for every imported file. The
ICDE evidence map v5 will determine which of these rows enter final tables.

