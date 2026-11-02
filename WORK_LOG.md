# Worker Lab Work Log

Record only actions completed in this public synthetic sandbox. This log does not alter V27 authority or count as worker admission or project acceptance.

## 2026-11-02

### Qwen Code local file-edit smoke — PASS (prior run)
- The repository README already records a successful local Qwen Code file-write smoke against LM Studio using scoped --approval-mode auto-edit.
- Qwen Code CLI 0.21.8 was confirmed installed during this turn.
- The current-turn LM Studio model inventory check was read-only; no model was switched or loaded.

### GitHub Actions synthetic validation — PASS
- Repository commit tested: 1c4a36b764f8c80fb543648e0ec9923bbdc5e0eb.
- Manual run: 41399634914 (workflow_dispatch), completed with conclusion success at 2026-11-02 06:23:59 UTC.
- The workflow validated checked-in synthetic fixtures only. It did not call Qwen Code or LM Studio, dispatch a V27 worker, or change production files.

### Google Apps Script synthetic trigger test — BLOCKED BEFORE EXECUTION
- This is the next untested candidate in the ranked sequence.
- Synthetic task, manifest, and trigger/cleanup source are staged on branch worker/apps-script-synthetic-20261102; local JavaScript syntax and JSON parsing passed.
- npm's shared-cache lock first returned ECOMPROMISED. A dedicated temporary cache then ran clasp 3.4.1 without a global install.
- The clasp OAuth flow requested broad Drive and Google Cloud scopes; it was stopped before approval.
- A later Opera navigation to script.google.com under the proposed Kobe account was rejected by automatic approval review because no explicit account selection was received. No Google page was opened or authorized.
- No Apps Script project was created, no Google scopes were granted, no quota check occurred, and no worker execution took place.
- Next step: select the Google account and use a narrower Apps Script authorization path. Do not count Apps Script as tested yet.