# Feedback and Perspectives

*(Portfolio item — the teacher's feedback/perspectives template, filled from real events.
Supports E3 and PA1; evidence base for A2 in both Progress Checks.)*

## Feedback received

### Entry 1 — Adversarial audit findings (the most consequential feedback so far)

| Field | Entry |
|---|---|
| **Learning Goal** | Build Kobald so that "autonomous in thought, cautious in action" is enforced, not claimed |
| **Person giving feedback & why I chose them** | Adversarial reviewer sessions (AI reviewers given a hostile mandate). I chose a *hostile* reviewer deliberately: a friendly reviewer confirms what I already believe |
| **Key takeaways from feedback** | My last full audit produced 1 critical, 6 high, 16 medium, 21 low findings. The critical one: in a narrow multi-process window, an approved state-changing action could fire twice. The high ones included sorting a knowledge-retrieval list by the wrong key (silently dropping the most relevant records) and a validator that rejected legitimate citations |
| **Action plan (steps to improve)** | 1. Rank findings by real-world impact, not by how embarrassing they are. 2. Fix the critical + high findings per phase, each with its own fix commit and tests. 3. Re-audit after fixing — a fix can introduce its own defects |
| **Apply & reflect (what changed?)** | Every phase since late July has closed with a "confirmed findings" fix commit (4 confirmed on 01 Aug, 6 on 02 Aug, a critical route-privacy bypass on 03 Aug). Feedback changed what "done" means to me: no longer "it works" but "it fails loudly and its gaps are documented" |
| **What now?** | I deliberately did *not* fix all 44 findings — 21 low-severity ones stay documented instead, because fixing everything at once would bury the critical one. The critical cross-process finding needs a human expert's eyes before I consider it closed |

### Entry 2 — The live run that embarrassed my test suite

| Field | Entry |
|---|---|
| **Learning Goal** | Trustworthy automated ingestion of real security data |
| **Person giving feedback & why I chose them** | The first real live feed refresh (15 Aug). I chose reality over my own tests because a test suite is a model of reality, and models drift |
| **Key takeaways from feedback** | Every test passed, yet the first live run failed: my test's fake connection accepted a keyword (`server_hostname=`) that the real Python `HTTPSConnection` rejects. The bug survived ~2,100 green tests |
| **Action plan (steps to improve)** | 1. Add a regression test asserting the fake mirrors the *real* API signature. 2. Rule for the portfolio: any mock that accepts something the real API wouldn't is a bug in the test |
| **Apply & reflect (what changed?)** | The lesson is now recorded and applied: mocks must mirror the real contract, not what my code wishes existed. Two further real-run defects surfaced the same day (KEV claim lengths, dotted ATT&CK identifiers) and were fixed in the parsers — not by loosening the validation limits |
| **What now?** | Before claiming any subsystem works, run the real thing live and record the result. Live evidence beats test evidence |

### Entry 3 — The assessment documents as feedback

| Field | Entry |
|---|---|
| **Learning Goal** | Same as above |
| **Person giving feedback & why I chose them** | My teacher's handouts (Simplified Rubric, Progress Check prompts, Reflection Sheet). I chose them because they define what "good" means in this course — reading the marking criteria before writing is cheaper than after |
| **Key takeaways from feedback** | The rubric's A-band words are *discerning*, *synthesises*, *related impact* — description earns a C; appraising earns an A. The handout also warns: the output is not the assessment, the **process** is, and everything belongs in the portfolio |
| **Action plan (steps to improve)** | 1. Rebuild my portfolio around the teacher's actual tables (this document, Strategy Tracking, Reflection Sheet). 2. In every Progress Check, judge sources on currency/reliability, relevance and purpose — not just name them |
| **Apply & reflect (what changed?)** | I restructured my whole repo around the criteria codes (E1–E3, PA1–PA3, A2) so each portfolio item names what it evidences |
| **What now?** | After Progress Check One, use the teacher's response as Entry 4 — the rubric explicitly rewards responding to feedback with actions |

## Perspectives

| Perspective | Why selected | How it differs from the others | How it helps my learning |
|---|---|---|---|
| **Adversarial AI reviewers** | Assume I am wrong and try to prove it | Hostile, exhaustive, available at any hour — but they share my training blind spots | Finds defects before they become real-world harm |
| **Authoritative documents** (CISA, MITRE, NVD, Python docs, systemd manual) | Ground truth written by the people who built the things I build on | Impersonal, current, authoritative — but describe happy paths, not my bugs | Keeps my design decisions anchored to how the platform actually behaves |
| **My own test suite** | The only reviewer that sees every line | Mechanical, unforgiving, but only as good as its assumptions | Pins guarantees so they cannot silently regress |
| **Classmates (speed-dating, upcoming)** | Non-experts expose unexplained assumptions | Least technical — most likely to ask the question I forgot to ask | Will test whether I can explain Kobald without jargon — a real test of understanding |
| **External human expert (to be contacted)** | The one perspective type entirely missing from my portfolio so far | Independent of my tools, my tests and my training | Needed before I can honestly call a security-sensitive system "safe" — see `expert-outreach.md` |

**How the perspectives relate:** the documents tell me what is *true*; the adversarial
reviewers tell me where my *code* diverges from it; my tests pin that divergence shut;
classmates and an external expert will tell me whether any of it makes sense outside my
own head. Each covers a blind spot the others cannot see.