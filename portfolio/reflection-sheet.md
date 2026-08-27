# Reflection Sheet

## What evidence best shows my progress?

The strongest evidence is not a feature list. It is the sequence where a constraint or fault changed what I did next: the 13 July runtime boundary made human approval a design rule; the live `build_context` failure led to a fix and test path on 26 July; and the VPN/private-network compatibility test showed that security decisions must be checked in the real setup. The dated Git record makes these decisions traceable.

## Which strategies were effective, and why?

The most effective strategies were adversarial audit sessions and live smoke testing. They were effective because they could contradict my belief that the project worked. Conventional automated tests were still valuable, but a real run exposed a gap that tests had not. I now use multiple checks because they fail differently.

## Which perspectives mattered?

Technical documentation and security sources shaped what the system should do. Donor, funding and audience perspectives shaped what I could realistically build and explain. I synthesised them by changing the project from a “best hardware” plan to a staged, governed-system plan. Neither group of perspectives was enough by itself.

## What feedback did I receive, and what did I do with it?

The clearest direct feedback was on my Rotary presentation: make the slides easier to read, explain AI and its risks in everyday language, use a familiar hook, and have a demo backup. I revised the communication approach before presenting. I also treated system failures as feedback: I fixed the `build_context` problem instead of presenting the passing tests as proof that nothing was wrong.

## What would I change next time?

I would seek an external technical perspective earlier. I contacted people early for equipment and community support, but I have not yet captured a specialist response about Kobald’s approval and audit design. Starting that conversation earlier would give me more time to apply the advice, test the result and reflect on it before final submission.

## Next action

Send a short, targeted request for technical feedback; capture a current safe test and approval-flow example; verify the donated hardware; then update the evidence register with the response and my decision.
