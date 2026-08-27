# Learning Goal, Direction and Plan

## Learning goal

**To design, build and safely operate Kobald (formerly Project JARVIS), a governed AI system for research and authorised security work, and learn how trustworthiness is engineered through approval gates, audit trails, evidence handling, testing and honest documentation.**

At the start, I wanted to make a local AI assistant on a GPU server. That was a real interest, but it was too broad and too focused on the final product. I changed the direction after practical limits appeared: TPU quota was denied, an RTX PRO 6000 was unavailable, an L4-based cloud option had a small boot disk, and ongoing cloud cost became a risk. Instead of treating those problems as reasons to stop, I narrowed the learning to a question I could actually investigate: *what makes an AI system safe enough for a person to supervise?*

That change matters. A bigger model would not prove that the system was trustworthy. I can show learning by designing constraints, testing them, recording faults and responding to feedback.

## What success looks like

| Success criterion | Evidence I will use | Why it shows learning, not just output |
|---|---|---|
| A research task can be explored without uncontrolled action | Captured task flow showing an approval pause before a state-changing action | Tests the project principle under a real workflow |
| Important decisions can be traced | Dated commits, change notes and a redacted audit record | Shows why I made a decision and whether it held up |
| I respond to faults rather than hide them | Before/after bug evidence, regression test and reflection | Demonstrates adaptation of strategy |
| I use viewpoints beyond my own | Community presentation feedback, documentation, donor/grant responses and external technical feedback still to be sought | Reduces the chance that I only confirm my own assumptions |
| I manage finite resources responsibly | Budget, hardware record, calendar, backups and deployment rule | Connects time, money, equipment and safety risks |

## Planning timeline

| Date or period | Decision, action or deadline | Evidence status | What it changed |
|---|---|---|---|
| 8 July 2026 | Began the Kobald core in Git | **Verified capture** — initial core commit `6ff5dbe` | Turned a broad idea into small, reviewable phases |
| 13–14 July | Built approval, provenance, ingestion and review-queue iterations | **Verified capture** — commit history records releases from `4edf511` to `c1e7671` | Made safety and evidence handling part of the design rather than an add-on |
| June–August | Contacted local businesses, councils, community groups and Rotary for equipment, advice and presentation opportunities | **Verified capture** — email record summarised in the evidence register | Replaced the unrealistic assumption that I could buy the whole setup myself |
| 11 August | Presented the project to Rotary | **Verified capture** — invitation and follow-up records | Forced me to explain the project in ordinary language and identify specific support needs |
| Term 3, Week 4 | Progress Check Part 1 and Portfolio Checkpoint 2 | Supplied school schedule | A deadline for the first evidence-based reflection |
| Term 3, Week 8 | Progress Check 2 draft | Supplied school schedule | I need genuinely new evidence, not a rewrite of Check 1 |
| Term 3, Week 10 | Progress Checks due | Supplied school schedule | Final AT2 submission point |
| Term 4, Week 1 | Portfolio due | Supplied school schedule | Final AT1 evidence selection and organisation |
| Term 4, Week 5 | Appraisal due | Supplied school schedule | Use the portfolio to make a final judgement about the learning |

## Resource and risk plan

| Resource or risk | My response | Evidence that will show whether it worked |
|---|---|---|
| Limited hardware and funding | Asked for donated/second-hand equipment, made a staged budget and separated essential items from ideal hardware | Donor email summary, grant budget, equipment verification list |
| Cloud cost and capacity | Moved away from relying on a large paid cloud GPU; use local/smaller resources where possible | Original cloud notes and revised plan |
| A bad deployment or uncontrolled action | Default-deny approval design; backup before copy; two-person deployment check where write access is limited | Redacted deploy record and approval-flow capture |
| False confidence from passing tests | Add live smoke tests and regression tests when a real run exposes a gap | Fault-to-fix records in the evidence register |
| Only hearing my own perspective | Seek teacher, audience and technical-expert feedback; follow up once after a week | Feedback record, outreach log and response notes |
| Losing track of work | Use calendar milestones and small dated commits | Commit timeline and weekly review notes |

## Next plan revision

My next decision is to capture the evidence that is currently only reported from my working copy: a current test result, a redacted approval-flow screenshot, the exact hardware specification, and a short external technical response. Until those are captured, I will describe them honestly as working-copy evidence rather than use them as proof.
