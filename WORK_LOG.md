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
- The synthetic task, manifest, and trigger/cleanup source are on branch worker/apps-script-synthetic-20261102; local JavaScript syntax and JSON parsing passed.
- An initial clasp invocation hit ECOMPROMISED from npm's shared-cache lock timeout. A dedicated temporary cache then ran clasp 3.4.1 without a global install.
- No clasp authorization was present. The clasp sign-in flow requested broad Drive and Google Cloud scopes beyond this trigger-only test, so it was stopped before approval.
- No Apps Script project was created, no Google scopes were granted, no quota check occurred, and no worker execution took place.
- Next step: get a least-scope Apps Script authorization path, then run the synthetic trigger and cleanup. Do not count Apps Script as tested yet.