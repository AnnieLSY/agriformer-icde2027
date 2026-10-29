#!/usr/bin/env python3
"""Run every release audit and fail on the first unmet promise."""

from pathlib import Path
from audit_splits import audit as audit_splits
from audit_preparation_records import audit as audit_preparation
from audit_aus_only_regressors import audit as audit_aus_only
from audit_claims_to_artifacts import audit as audit_claims
from audit_public_wording import audit as audit_wording
from audit_public_evidence_snapshot import audit as audit_snapshot


if __name__ == "__main__":
    root = Path(__file__).resolve().parents[1]
    print(audit_splits(root))
    print(audit_preparation(root))
    print(audit_aus_only(root))
    print(audit_claims(root))
    print(audit_snapshot(root))
    print(audit_wording(root))
    print("PASS: all manuscript release commitments are covered")
