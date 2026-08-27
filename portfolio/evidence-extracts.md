# Evidence Register and Dated Extracts

This is the evidence index for the portfolio. It follows the assessment advice that a live link alone is not evidence. Each entry states what has been captured, how reliable it is, and what still needs to be added.

## A. Project development — Git capture

| Date | Commit / record | What it evidences | Status |
|---|---|---|---|
| 8 Jul 2026 | `6ff5dbe` — initial core | Start of the Kobald development record | **Verified capture** |
| 13 Jul 2026 | `4edf511` — security/data-integrity fixes; 98 tests | Early response to security and data-integrity risks | **Verified capture** |
| 13 Jul 2026 | `1e4b14d` — research runtime boundary; 137 tests | A deliberate boundary between research and action | **Verified capture** |
| 13 Jul 2026 | `9bdf862` — v0.3 acceptance baseline; 198 pass / 1 skip | Testing became a tracked quality measure | **Verified capture** |
| 13 Jul 2026 | `b512b04` — v0.6 evaluation; 252 pass / 1 skip | Evaluation was added as the project grew | **Verified capture** |
| 13 Jul 2026 | `9e3956f` — v0.7 ingestion/cross-session; 273 pass / 1 skip | Real-data handling and continuity became a design concern | **Verified capture** |
| 14 Jul 2026 | `c1e7671` — review queue/offline Rotary demo; 295 pass / 1 skip | Human review and communication needs affected development | **Verified capture** |
| 18 Jul 2026 | `9e3161d` — v0.9 provider layer; 538 pass / 1 skip | The project expanded while keeping a dated test record | **Verified capture** |
| 26 Jul 2026 | `b0432ddd` — Mullvad kill-switch/Tailscale coexistence verified | I tested a networking constraint rather than assuming it would work | **Verified capture** |
| 26–27 Jul 2026 | `e983080`, `2b97f46`, `5aa0b35` | Concurrency hardening, a task-breaking error fix, and oversight/chat changes | **Verified capture** |

The linked Kobald repository and public showcase are useful navigation sources, but the dates and descriptions above are the portfolio capture. The public showcase describes an early-stage project and says it is not production-ready; I retain that limitation rather than presenting the work as a finished commercial system.

## B. Problem → decision → evidence

| Problem found | Decision made | What changed | Evidence status |
|---|---|---|---|
| File/path and audit-integrity risks in early development | Strengthened validation, atomic writes and audit logging | Safety work was prioritised before more features | **Verified capture** — 13 July security/data-integrity commit |
| An AI task needed a clearer boundary | Kept research runtime separate from state-changing action and required approval | The project principle became a technical constraint | **Verified capture** — 13 July runtime-boundary commit |
| Real feed data used unexpected formats | Fixed parsers for claim length and dotted ATT&CK identifiers rather than weakening validation | Preserved the guardrail and improved the parser | **Reported working-copy evidence** — add a redacted test/output capture |
| A fake test connection accepted an argument the real API rejects | Added a regression expectation that mocks match the real interface | A passing test suite was treated as a question, not a guarantee | **Reported working-copy evidence** — add the failing test and fix capture |
| A `build_context` error stopped tasks in a live run | Fixed the error and added a test path | Live testing exposed a gap ordinary tests missed | **Verified capture** — 26 July `2b97f46` |
| VPN kill-switch and private-network access conflicted | Tested and documented a safe coexistence setup | Networking was treated as a safety decision | **Verified capture** — 26 July `b0432ddd` |
| Concurrency could resume or double-fire work | Hardened locks, pause/cancel persistence and oversight restrictions | High-consequence actions received extra safeguards | **Verified capture** — 26 July `e983080` |

## C. Community, resources and communication

| Date | Evidence | What it demonstrates | Status |
|---|---|---|---|
| 9–29 Jun 2026 | Enquiries to council, businesses, community groups and technical contacts | I actively sought resources and viewpoints instead of assuming equipment would appear | **Verified capture** — email history |
| Mid June | A technical contact offered equipment and requested a project brief/parts list | I responded by making the project needs specific | **Verified capture** — email history |
| 25 Jun | Donor confirmed two PCs, monitors, basic networking equipment and cables; no UPS, NAS storage or GPU | Resource planning had to distinguish what was available from what was still needed | **Verified capture** — email history; exact second-PC model remains **to verify** |
| 21–29 Jun | Regional development advice pointed to future STEM grants, library options, alerts and documented budgets/goals | Funding feedback changed my plan from a one-off ask to staged resourcing | **Verified capture** — email history |
| 11 Aug | Rotary presentation and later support list | I adapted my explanation for a non-technical audience and identified concrete requests | **Verified capture** — invitation and follow-up history |
| 9 Aug | Feedback from Zoe Dalton about readability, plain-language AI explanation, a familiar hook and demo contingency | I was asked to make the project clearer for an audience, not simply more technical | **Verified capture** — feedback email |
| 24 Aug | Lions Club and GTE equipment enquiries sent | I continued outreach after earlier outcomes | **Verified capture** — sent email history; replies are **not yet received** |

## D. Evidence gaps — actions before final submission

| Needed capture | Why it matters | Planned action |
|---|---|---|
| Current test result and date | Prevents old test counts being presented as current | Run the suite; save a redacted terminal screenshot or exported log |
| Redacted approval-flow capture | Demonstrates the project principle in action | Record one harmless task reaching the approval gate |
| Exact hardware inventory | Resolves conflicting descriptions of the second donated PC | Check the device label/system information and take a photo/screenshot |
| External technical feedback | Adds a perspective not created by me | Send the draft outreach, follow up after one week, record the response and my action |
| Reconciled feed/vault count | Existing notes contain inconsistent totals | Export the count and record method/date before using it in assessed writing |

## Evidence-handling note

Emails are summarised rather than copied with personal contact information. Code evidence is described with commit identifiers and purpose. I will attach redacted screenshots or PDF captures to this portfolio folder if my teacher needs the original artefacts; I will not publish private details or credentials in a public repository.
