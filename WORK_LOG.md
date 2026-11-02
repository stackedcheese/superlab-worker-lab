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

### Google Apps Script synthetic test — BLOCKED BEFORE EXECUTION
- This is the next untested candidate in the ranked sequence.
- First npx invocation hit ECOMPROMISED from npm's shared-cache lock timeout.
- Retrying with a dedicated temporary cache succeeded; clasp 3.4.1 ran ephemerally without a global install.
- No clasp authorization file is present. No Apps Script project was created, no quota check occurred, and no worker execution took place.
- Next gate: authorize a synthetic Apps Script project run. Do not count Apps Script as tested yet.