# SuperLab Worker Lab

This public repository is an isolated sandbox for local coding-tool setup and synthetic worker-contract checks. It is separate from the StackedCheese product and the authoritative V27 workspace. It contains no production data or credentials.

The original V27 Codex PM retains assignment, source-authority, coordination, and acceptance authority. This repository does not change the V27 tracker, assign or dispatch workers, or accept or integrate their work.

## Qwen Code

The local Qwen Code file-write smoke check succeeded using LM Studio and scoped `--approval-mode auto-edit`. Run Qwen Code from this repository root and keep each task inside the task card's read/write allowlists:

```sh
qwen --approval-mode auto-edit
```

The GitHub workflow here does not call Qwen Code or LM Studio. It validates only checked-in synthetic fixtures.

## Local checks

The workstation has Ruff 0.17.3, pre-commit 4.7.0, and Gitleaks 8.30.1 installed. Hooks call these local executables and do not download hook environments.

```sh
pre-commit install
pre-commit run --all-files
python scripts/validate_synthetic_receipt.py
```

A task card defines read/write allowlists, denies network, paid usage, and secret access, and lists acceptance checks and stop conditions. A receipt records changed paths and checks. Independent review is required; the original V27 PM records ACCEPT, REVISE, or REJECT in the existing tracker.

The fixture under `fixtures/` is synthetic and marked as a sample. Passing the GitHub check validates only this fixture; it is not worker dispatch, independent review, or project acceptance.

## GitHub check

`.github/workflows/synthetic-validation.yml` runs only by manual `workflow_dispatch`. It uses a standard GitHub-hosted Ubuntu runner with read-only repository permission and installs no dependencies. GitHub documents standard hosted runners as free in public repositories: https://docs.github.com/en/actions/how-tos/write-workflows/choose-where-workflows-run/choose-the-runner-for-a-job
