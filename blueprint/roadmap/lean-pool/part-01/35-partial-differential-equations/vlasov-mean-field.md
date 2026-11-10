---
declaration: theorem
origin: cited
lean: Vlasov.vlasovWellPosedness, Vlasov.dobrushin, Vlasov.meanFieldLimit
statement: formalized
proof: formalized
---

# Mean-field derivation and well-posedness of the Vlasov equation

> Formalizes the mean-field limit, Dobrushin stability, and forward-in-time well-posedness for the Vlasov equation via Wasserstein-1 optimal transport.

*Quoted from the card [LeanPool/projects/vlasov-mean-field.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/vlasov-mean-field.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`Vlasov.vlasovWellPosedness`](https://leanpool.github.io/lean-pool/LeanPool/Vlasov/OT/WellPosedness.html#Vlasov.vlasovWellPosedness) (theorem; a main declaration), declared in [LeanPool/Vlasov/OT/WellPosedness.lean, line 1907](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Vlasov/OT/WellPosedness.lean#L1907): “Forward-in-time existence of a Lagrangian solution to the Vlasov equation on any finite horizon, for interaction forces that are Lipschitz gradients of an even pair potential (class AssW) — with no smallness restriction on the Lipschitz constant.”
- [`Vlasov.dobrushin`](https://leanpool.github.io/lean-pool/LeanPool/Vlasov/OT/WellPosedness.html#Vlasov.dobrushin) (theorem; a main declaration), declared in [LeanPool/Vlasov/OT/WellPosedness.lean, line 2097](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Vlasov/OT/WellPosedness.lean#L2097): “A Wasserstein-1 form of Dobrushin's 1979 stability estimate (the original uses a truncated metric) - two Lagrangian Vlasov solutions with finite first moments at every time separate at most at an exponential Gronwall rate.”
- [`Vlasov.meanFieldLimit`](https://leanpool.github.io/lean-pool/LeanPool/Vlasov/Basic.html#Vlasov.meanFieldLimit) (theorem; a main declaration), declared in [LeanPool/Vlasov/Basic.lean, line 1751](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Vlasov/Basic.lean#L1751): “Conditional mean-field limit - given Wasserstein-1 convergence of the initial empirical data and a uniform Dobrushin stability estimate for the empirical curves, the N-particle empirical measures converge to the Vlasov solution uniformly on any finite horizon.”
- [`Vlasov.weak_isLagrangianVlasovSolutionOn`](https://leanpool.github.io/lean-pool/LeanPool/Vlasov/OT/WeakToLagrangian.html#Vlasov.weak_isLagrangianVlasovSolutionOn) (theorem), declared in [LeanPool/Vlasov/OT/WeakToLagrangian.lean, line 1224](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Vlasov/OT/WeakToLagrangian.lean#L1224): “On a time window with L \* T^2 < 1, a weak solution with the standing regularity (even C^2 pair potential AssW2, finite first moments, narrow continuity, time-continuity of the convolution force at each point, continuity of the convolution-derivative field, and a uniform spatial first-moment bound on the window) is Lagrangian - the pushforward of its initial datum along the characteristic flow.”

## Project

- Authors: Joseph K. Miller.
- Source: *A Formalization of the Mean-Field Derivation of the Vlasov Equation* by Joseph K. Miller, [arXiv:2607.08986](https://arxiv.org/abs/2607.08986).
- Project repository: [Hydrodynamical/Vlasov_Meanfield_Formalization](https://github.com/Hydrodynamical/Vlasov_Meanfield_Formalization).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 35Q83, 82C22, 49Q22.
- In Lean Pool: [LeanPool/Vlasov](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Vlasov), from the card [LeanPool/projects/vlasov-mean-field.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/vlasov-mean-field.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/vlasov-mean-field.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/vlasov-mean-field.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Vlasov](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Vlasov)
