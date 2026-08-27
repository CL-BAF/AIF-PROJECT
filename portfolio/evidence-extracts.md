# Evidence Extracts

*(Portfolio item — raw extracts from the real project, so the claims in the Progress
Checks can be checked against primary evidence rather than taken on trust. All quotes
are verbatim from the Kobald working copy.)*

## 1. Commit log (process evidence)

From `git log --date=short --pretty='%ad %h %s'` — 106+ commits since 2026-07-08,
each phase closed with a fix commit:

```
2026-08-03 41fcbe5 Phase 4 audit fix [2/5]: cross-validation rejects dead/contradictory bindings
2026-08-03 7796784 Phase 4 audit fix [1/5]: close CRITICAL route() privacy/consent bypass
2026-08-03 8962217 Phase 4 Step 9 — runtime approved-fallback chain on provider errors
2026-08-03 4ba3fe9 Phase 4 Step 6: ModelRegistry + models.yaml + /api/v1/models + cross-validation
```

This is where PA2's "numbered phases of small, dated commits" claim comes from — any
date in either Progress Check can be traced to a commit like these.

## 2. Security review table (source of the audit finding counts)

The adversarial review is recorded in
`services/jarvis-core/CANONICAL-ARCHITECTURE-PLAN.md` as a requirement-by-requirement
table with a verdict per row. Verbatim rows:

```
| Bounded persistence ... | [~] | Continue-on-failure present (1855-1872), exact blocker set (1499-1771);
  no failure-classification taxonomy or programmatic temporary-retry-with-backoff |
| High-water rollback detection | [x] | state_seal.py:226-354; gen CAS agent_state.py:839-846;
  documented attacker-can-replace-highwater gap (state_seal.py:18-23) |
| Bounded retrieval + access controls + audited updates + high-impact review | [~] |
  Keyword-bounded; WARDEN + actor validation; no per-item count cap in code, no RBAC/ACL, no size cap |
| Detect unavailable/unhealthy models | [~] | Consecutive-provider-error count → FAIL (1532-1571);
  cloud check_availability gated by allow_metadata_requests default False → cloud always reports healthy:0 |
```

This is what the "[x]/[~]/[ ]" verdicts behind the *1 critical / 6 high / 16 medium /
21 low* finding counts look like in the source: every verdict carries a file and line
reference, and the "[~]" rows are the documented residuals that were deliberately not
all fixed at once (PA3, Progress Check One).

## 3. Runtime audit trail (live evidence of the approval gate)

`services/jarvis-core/<kobald-root>/audit/kobald-audit.jsonl` — 177 append-only events,
including every Knowledge Vault creation with its content hash and unreviewed status:

```
{"event_type":"vault.knowledge.created","created_at":"2026-08-11T03:36:06.037597+00:00",
 "data":{"record_id":"nist-ai-600-1-genai-profile","status":"unreviewed",
         "title":"NIST AI 600-1 Generative AI Profile Overview"}}
```

This is the structural trustworthiness judgement from PA3 in action: records enter as
*unreviewed* and the event is hashed and logged the moment they do.

## 4. Deployment record

`docs/kobald/DEPLOY.md` is headed *"Deployed state (jarmedia, 2026-07-25)"* — the date
the two-host deployment (control plane + isolated worker VM) went live, which fixes the
"running live since late July" claim in the reflection sheet.

## 5. Test suite

`services/jarvis-core/tests/` contains 118 test files (≈2,100 tests across the project,
122 files including integration tests) — the basis of the "every guarantee is pinned by
a test" strategy in `strategy-tracking.md`.
