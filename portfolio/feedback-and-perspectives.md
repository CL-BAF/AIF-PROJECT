# Perspectives, Feedback and My Responses

The distinction matters: a **perspective** helps me make a decision before I act; **feedback** reacts to something I have already done. I have recorded both because they have influenced different parts of Kobald.

## Perspectives used before decisions

| Perspective | What it said or implied | Decision it influenced | My synthesis |
|---|---|---|---|
| Official technical documentation | Interfaces, libraries and services have specific limits; documented behaviour matters more than what a mock happens to allow | Keep the standard-library-focused core and test against real interfaces | Strong authority for intended behaviour, but it mostly describes normal use. I must pair it with live testing. |
| Security-source perspective | Threat information should be traceable, current and reviewed before being trusted | Use provenance, allowlisted ingestion and a human review state | Useful for the data model, but source authority does not automatically make my parser or workflow safe. |
| Community/funder perspective | Support depends on clear goals, a realistic budget, local benefit and the right eligibility path | Break the hardware plan into stages; document needs instead of asking vaguely | This challenged my assumption that a good technical idea would be funded on its own. |
| Donor/technical-contact perspective | Available equipment can help, but it is not the same as the ideal system; a brief and parts list are needed | Make a specific equipment inventory and prioritise missing essentials | It made planning concrete. I still need to verify the exact second-PC specification. |
| Non-technical audience perspective | A presentation needs a clear hook, readable slides, plain language and a contingency if a live demo fails | Rework the Rotary presentation around explanation and a prepared demo | This showed that communication is part of responsible technology, because people cannot consent to or support what they cannot understand. |

### Synthesis before action

I did not treat these as a list of opinions. The technical sources told me how to constrain and verify the system; the community responses told me what was realistic to build and explain with the resources I had. Together they changed my direction: I stopped measuring the project only by model size or hardware ambition, and started measuring it by whether the workflow was accountable, explainable and possible to test.

## Targeted feedback after action

| Feedback event | Takeaway | My response | Evidence of change / next check |
|---|---|---|---|
| Zoe Dalton reviewed the Rotary presentation (9 Aug) | Improve readability; explain AI basics and risks; use the JARVIS reference carefully; keep language conversational; prepare a recorded demo backup | Simplified the explanation and made the project purpose clearer for a mixed audience | Presentation proceeded on 11 Aug. I will add a short audience-understanding note if available. |
| Grant and community responses during June | Some opportunities were ineligible, out of area, had no budget, or were better suited to a school co-application/future grant cycle | Logged alternatives, refined the staged budget and continued with realistic local outreach | New Lions Club and GTE enquiries were sent on 24 Aug; response pending. |
| Live system behaviour exposed a task-breaking `build_context` error | Automated checks had not covered a real execution path | Fixed the error and added a test path instead of dismissing the failure as an exception | Verified 26 July fix record. I will capture the current regression result. |
| A networking setup had to combine a kill-switch VPN with private access | “It should work” was not enough for a safety-sensitive deployment choice | Tested the coexistence and documented the result | Verified 26 July record. I will keep private connection details out of the public portfolio. |

## Feedback still needed

The feedback I most need is not “this is cool” or “your code looks good.” I need an external technical person to inspect one narrow question: **Does my approval/audit approach make sense for a student-built research assistant, and what failure mode am I still missing?** This is targeted because it addresses the main limitation in my current evidence — too much of the safety loop originates with me.

My planned response rule is: record the exact takeaway, decide whether it changes the plan, apply one realistic action, then explain whether the action improved the learning. If I disagree with the advice, I will explain why rather than pretending every feedback item must be adopted.
