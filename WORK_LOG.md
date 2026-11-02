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

### Google Apps Script synthetic test — BLOCKED
- This is the next untested candidate in the ranked sequence.
- The temporary npx invocation for @google/clasp failed with npm ECOMPROMISED: Lock compromised.
- clasp is not installed and no clasp authorization file is present. No Apps Script project was created and no worker execution or quota check occurred.
- Do not count Apps Script as tested until the install/authentication blocker is resolved.