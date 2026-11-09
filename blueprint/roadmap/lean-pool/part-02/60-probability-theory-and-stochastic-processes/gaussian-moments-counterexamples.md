---
declaration: theorem
origin: cited
lean: GaussianMomentsCounterexamples.not_GMC_of_three_le
statement: formalized
proof: formalized
---

# Gaussian Moments Conjecture counterexamples

> Proves explicit complex polynomial counterexamples to the Gaussian Moments Conjecture in every dimension at least three, using genuine expectations under finite products of standard real Gaussian measures. Retains reusable polynomial integrability, Stein identities, complex contractions, coefficient formulas, injective-coordinate marginals, and related moment results.

*Quoted from the card [LeanPool/projects/gaussian-moments-counterexamples.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/gaussian-moments-counterexamples.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`GaussianMomentsCounterexamples.not_GMC_of_three_le`](https://leanpool.github.io/lean-pool/LeanPool/GaussianMomentsCounterexamples/Counterexamples.html#GaussianMomentsCounterexamples.not_GMC_of_three_le) (theorem; a main declaration), declared in [LeanPool/GaussianMomentsCounterexamples/Counterexamples.lean, line 93](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GaussianMomentsCounterexamples/Counterexamples.lean#L93): “For every n at least three, the Gaussian Moments Conjecture fails: some complex polynomial has all positive pure Gaussian moments zero, while a polynomial multiplier prevents eventual mixed-moment vanishing.”
- [`GaussianMomentsCounterexamples.master_three`](https://leanpool.github.io/lean-pool/LeanPool/GaussianMomentsCounterexamples/Counterexamples.html#GaussianMomentsCounterexamples.master_three) (theorem), declared in [LeanPool/GaussianMomentsCounterexamples/Counterexamples.lean, line 32](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GaussianMomentsCounterexamples/Counterexamples.lean#L32): “For every complex univariate polynomial A and positive m, the expectation of A(Q3) times P3 to power m equals m! times the degree-m coefficient of A(X) times (1+X) to power m-1. The explicit P3 has degree four and five terms in its natural complex coordinates.”
- [`GaussianMomentsCounterexamples.master_four`](https://leanpool.github.io/lean-pool/LeanPool/GaussianMomentsCounterexamples/Counterexamples.html#GaussianMomentsCounterexamples.master_four) (theorem), declared in [LeanPool/GaussianMomentsCounterexamples/Counterexamples.lean, line 40](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GaussianMomentsCounterexamples/Counterexamples.lean#L40): “The analogous arbitrary-A coefficient identity for the explicit four-variable polynomial P4, of degree three and six terms in its natural complex coordinates, gives an independent counterexample.”

## Project

- Authors: Christopher D. Long.
- Source: [arXiv:2607.18186](https://arxiv.org/abs/2607.18186).
- Project repository: [long-mathematics/gaussian-moments-counterexamples](https://github.com/long-mathematics/gaussian-moments-counterexamples), at commit [c31bb63a](https://github.com/long-mathematics/gaussian-moments-counterexamples/tree/c31bb63aaa7cfccf1191893f8e7d04fa71bae025).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0.
- MSC2020: 60E05, 13F20.
- In Lean Pool: [LeanPool/GaussianMomentsCounterexamples](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GaussianMomentsCounterexamples), from the card [LeanPool/projects/gaussian-moments-counterexamples.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/gaussian-moments-counterexamples.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/gaussian-moments-counterexamples.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/gaussian-moments-counterexamples.yaml)
- [Lean Pool at 2b205bf9: LeanPool/GaussianMomentsCounterexamples](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/GaussianMomentsCounterexamples)
