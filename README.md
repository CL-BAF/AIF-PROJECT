# AIF-PROJECT

AIF AT2 coursework repository for **CL-BAF**.

## The project behind this work: Kobald

Kobald (formerly Project JARVIS) is a governed autonomous AI control plane for
research and authorised security work, built around one principle:

> *Autonomous in thought, cautious in action.*

- **Core:** Python-standard-library-only agent runtime (~54k lines, 102 modules,
  ~2,110 tests) with WARDEN default-deny approval gating, HMAC-sealed task
  state, redacting audit logging, a Knowledge Vault with a human review gate,
  and a multi-agent spine (supervisor, departments, specialists, monitoring).
- **Deployment:** two-host split — an always-on HTTP control plane over
  Tailscale, plus an isolated worker VM behind a kill-switch VPN for anything
  state-changing.
- **Clients:** a PySide6 desktop client and a separate Tauri/React
  "Kobald Command Centre" for Windows.
- **Source:** [github.com/CL-BAF/Kobald](https://github.com/CL-BAF/Kobald)

## Contents

| File | Purpose |
|------|---------|
| `Progress-Check-AT2-Response.docx` | The AT2 Progress Check submission (Word document, ~750 words) answering the PA2, PA3 and A2 prompts against the Kobald project |
| `progress-check-at2-response.md` | Markdown source of the same response |
| `make_docx.py` | Regenerates the `.docx` from the markdown (`python3 make_docx.py`, stdlib only) |

## Progress Check structure

The response follows the AIF AT2 Progress Check prompts:

- **PA2 — Managing time and resources** (being strategic, planning, managing
  risks, resource use)
- **PA3 — Making judgements and decisions** (discerning decisions, moving
  learning forward)
- **A2 — Appraising the impact of strategies, perspectives and/or feedback**
  (evaluating effectiveness, feedback, perspectives, impact on the learning
  goal)

Every claim in the response is grounded in the real Kobald build log — commit
history, audit findings, test counts, and live deployment behaviour.