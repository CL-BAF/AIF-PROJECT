# Strategy Tracking: Test, Judge, Adapt

I am using this table as a record of what actually moved my learning forward. A rating is not a mark for effort; it is my judgement of the evidence each strategy produced.

| Strategy | Why I chose it | Evidence of impact | My judgement | Adaptation / next step |
|---|---|---|---|---|
| Small, dated Git commits | I needed a way to make progress visible and recoverable | Verified commits run from 8 July through 27 July, with test counts recorded at key points | **4/5.** It made the development path easier to explain and reduced the risk of losing a whole idea | Commit the later working-copy changes in smaller slices with a passing-test note |
| Default-deny approval design | I did not want “autonomous” to mean uncontrolled | 13 July runtime-boundary record and later oversight hardening | **5/5.** This turned a value into a concrete testable rule | Capture one harmless approval flow for the final portfolio |
| Adversarial audit / try-to-break-it sessions | I needed a strategy that could prove my confidence wrong | Security/data-integrity fixes, concurrency hardening, and later regression work | **5/5.** It finds uncomfortable but useful information | Ask an external person to challenge one audit finding, not only review my explanation |
| Unit tests plus regression tests | Repeated failures should not silently return | Test counts rose from 98 to 538 in verified commits; the live `build_context` fault was then fixed | **4/5.** Useful, but only when tests represent reality | Keep one live smoke test beside mocks; save a current result rather than quoting old totals |
| Live smoke testing | Passing tests can share the same mistaken assumption | A real task exposed the `build_context` failure despite automated testing | **5/5.** This corrected false confidence | Run a safe, redacted test after major changes and add its evidence |
| Secondary research and official documentation | I needed informed design choices without inventing security rules | Python/platform documentation and CISA/MITRE-style source use informed boundaries and parsing | **4/5.** Strong for foundations, weaker for seeing how my own implementation behaves | Compare documentation with a real run and record disagreements |
| Community outreach and resource planning | Hardware, money and local advice were genuine constraints | Donor, council, regional-development and Rotary correspondence | **4/5.** It made the resource plan more realistic and improved my communication | Verify the donated hardware; record outcomes of the two new enquiries |
| Audience feedback before a presentation | A technically correct explanation can still fail if people cannot follow it | Zoe Dalton's feedback led to clearer slides, plain-language explanation, familiar examples and a demo backup | **4/5.** It improved accessibility, not just appearance | Ask a listener what they understood after the presentation, then revise using that evidence |

## Two strategy changes that matter most

### 1. From “more testing” to “testing that can disagree with me”

At first, a larger test number felt like proof of quality. A live run showed the weakness in that thinking: a fake connection in a test accepted something that the real interface would reject. The test was passing because it matched my incorrect assumption. I changed my strategy by treating a passing suite as evidence to question, then adding a regression expectation that mocks must mirror the real interface. The implication is that I need different kinds of checking — code tests, live tests, audits and human review — because one method cannot expose every blind spot.

### 2. From “get the ideal hardware” to “build a staged, accountable system”

The first plan depended too much on a high-end GPU and cloud capacity. Funding and availability feedback made that unrealistic. I responded by separating the goal from the most expensive equipment: the goal is to learn governed AI design, so I can develop and test many of the important controls on the donated computers and local network first. This made the project more achievable, but it also created a new responsibility: I must be precise about what has actually been tested on the available hardware.

## Weekly check-in prompts

- What did I do that produced evidence, not just activity?
- Which strategy could prove me wrong next week?
- What decision am I delaying because I want more certainty?
- What resource, safety or privacy risk has changed?
- What needs a capture before I can use it in assessed writing?
