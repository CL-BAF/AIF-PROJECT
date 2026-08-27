# Learning Goal, Calendar and Plan

*(Portfolio item — supports E1, E2; evidence base for PA2 in both Progress Checks)*

## My Learning Goal

To design, build and safely operate **Kobald** (formerly Project JARVIS) — a governed
autonomous AI system for research and authorised security work — and, through building it,
learn how trustworthiness is *engineered* into a system that can take real actions:
approval gates, audit trails, sealed state, honest documentation of limits.

The design principle I chose, and measure everything against, is:

> **"Autonomous in thought, cautious in action."**

The system may research, form provisional conclusions and preserve contradictions on its
own — but every state-changing action pauses for my explicit approval.

## My Learning Output

A working, deployed, publicly documented system: the Kobald control plane running on a
second machine over an encrypted private network, a desktop client for Windows, and an
open-source repository (`github.com/CL-BAF/Kobald`) so my work can be examined.

## Calendar — milestones achieved (evidence: dated commits in the Kobald repo)

| Date | Milestone | Strategy link |
|------|-----------|---------------|
| 2026-07-08 | Project started: initial Kobald core foundation committed | Numbered-phase plan |
| 2026-07-13 | First security & data-integrity fix pass | Adversarial review |
| 2026-07-22 → 07-26 | Runtime concurrency hardening, WARDEN tests, scope lock, supervisor daemon | Test-pinning |
| 2026-07-26 | GUI redesigned to a modern dashboard; v0.12.0 released 07-27 | Secondary research (reference designs) |
| 2026-07-27 | `kobald chat` CLI + install guides (native Windows, WSL/Kali) | Documentation strategy |
| 2026-07-29 → 07-31 | `/api/v1` compatibility surface, policy layer (message bus, agent registry, WARDEN suspension) — 16 commits in one day | Small verified steps |
| 2026-08-01 → 08-03 | Multi-agent departments/specialists + privacy-aware model routing (Phases P-2a → 4), each closed by an adversarial-audit fix commit | Adversarial audit loop |
| 2026-08-11 → 08-18 (uncommitted work) | Work Mode persistent jobs, conversational chat fixes (Phase 12/13), OSINT collection subsystem, knowledge vault wired to live feeds | Live smoke testing |
| 2026-08-15 | Knowledge Vault grew 12 → 323 records via live authoritative feeds (CISA KEV, MITRE ATT&CK, NVD, GHSA) | Secondary research, automated |

## Calendar — deadlines I have set (per the teacher's advice: to-do list on a calendar)

| Deadline | Task | Why (acceptance criteria) |
|----------|------|---------------------------|
| Fri 28 Aug 2026 | Progress Check One draft submitted | Uses portfolio evidence; 500–750 words; PA2/PA3/A2 all answered |
| 28 Aug 2026 | Send expert-contact emails (see `expert-outreach.md`) | Handout: contact early, follow up after one week |
| 28 Aug 2026 | Commit the two weeks of finished-but-uncommitted code | Risk: uncommitted work is unproofed work |
| Sep 2026 (per teacher) | Progress Check Two | Must show *new* progress since Check One, not repeat evidence |
| End of term | External security review of the critical concurrency finding | The finding cannot be closed by me alone |

## Risks on the calendar (managed, not just listed)

- **Uncommitted work** — 112 paths with uncommitted changes (78 untracked, 34 modified); a disk failure would erase ~2 weeks
  of evidence. *Action:* commit in slices, each with a passing test run.
- **Expert response latency** — the handout warns people deprioritise student requests.
  *Action:* contact several at once this week; follow up after 7 days.
- **Word-limit discipline** — both checks are capped (Part 1 ≈700, combined ≤1500).
  *Action:* drafted to per-section word budgets and counted, not eyeballed.