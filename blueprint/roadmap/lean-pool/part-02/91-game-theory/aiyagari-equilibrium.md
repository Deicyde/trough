---
declaration: theorem
origin: cited
lean: LeanEconomics.aiyagariTauchen_equilibriumRate_unique_Ioo
statement: formalized
proof: formalized
---

# Normalized capped log-household clearing and dynamic programming

> Proves conditional uniqueness of a rate solving the unit-wage normalized clearing equation: mean household assets equal α / ((1 - α) \* (r + δ)), with α = 9/25 and δ = 2/25. Households have capped log utility, discount 24/25, no borrowing, and monotone finite earnings transitions with positive one-step access to a lowest-income state; an explicit cap-slack inequality is required. Finite Tauchen chains instantiate the household model. Bisection converges to a given solution of this normalized equation along a stationary-distribution selection. Equivalence to full competitive market clearing for arbitrary earnings scales is not established. Preserves Bellman contraction, Berge maximum theorems, stationary Markov theory, Euler inequalities, consumption concavity and marginal-propensity bounds.

*Quoted from the card [LeanPool/projects/aiyagari-equilibrium.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/aiyagari-equilibrium.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`LeanEconomics.aiyagariTauchen_equilibriumRate_unique_Ioo`](https://leanpool.github.io/lean-pool/LeanPool/AiyagariEquilibrium/Models/AiyagariTauchenWitness.html#LeanEconomics.aiyagariTauchen_equilibriumRate_unique_Ioo) (theorem; a main declaration), declared in [LeanPool/AiyagariEquilibrium/Models/AiyagariTauchenWitness.lean, line 112](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AiyagariEquilibrium/Models/AiyagariTauchenWitness.lean#L112): “For capped log households with discount 24/25, no borrowing and a finite Tauchen chain with persistence in [0,1), two rates in (-2/25, 1/24) whose stationary household distributions have mean assets equal to 9 / (16 \* (r + 2/25)) coincide, provided the explicit asset-cap inequality holds at their larger rate. This is the prescribed unit-wage normalized clearing equation; a bridge to full competitive equilibrium for arbitrary earnings scales is not supplied.”
- [`LeanEconomics.IncomeFluctuation.aiyagari1994_log_bisection`](https://leanpool.github.io/lean-pool/LeanPool/AiyagariEquilibrium/Equilibrium/Bisection.html#LeanEconomics.IncomeFluctuation.aiyagari1994_log_bisection) (theorem), declared in [LeanPool/AiyagariEquilibrium/Equilibrium/Bisection.lean, line 231](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AiyagariEquilibrium/Equilibrium/Bisection.lean#L231): “Given a rate satisfying the same unit-wage normalized clearing equation in a compact interval inside (-2/25, 1/24), a stationary-distribution selection and the stated cap, monotonicity and reachability hypotheses, bisection on normalized excess supply brackets that rate, bounds midpoint error by the initial width divided by 2^(n+1), and has left endpoints converging to it. Existence of a solution to this equation is assumed.”
- [`LeanEconomics.continuousAt_maxValue`](https://leanpool.github.io/lean-pool/LeanPool/AiyagariEquilibrium/Topology/Berge.html#LeanEconomics.continuousAt_maxValue) (theorem), declared in [LeanPool/AiyagariEquilibrium/Topology/Berge.lean, line 142](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AiyagariEquilibrium/Topology/Berge.lean#L142): “A continuous objective maximized over a nonempty compact-valued correspondence that is upper and lower hemicontinuous has a continuous maximum value at the parameter.”
- [`LeanEconomics.Blackwell.contractingWith`](https://leanpool.github.io/lean-pool/LeanPool/AiyagariEquilibrium/DynamicProgramming/Blackwell.html#LeanEconomics.Blackwell.contractingWith) (theorem), declared in [LeanPool/AiyagariEquilibrium/DynamicProgramming/Blackwell.lean, line 116](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AiyagariEquilibrium/DynamicProgramming/Blackwell.lean#L116): “A monotone operator on bounded continuous real functions that discounts constants by a nonnegative factor below one is a contraction with that factor.”

## Project

- Authors: Robert Kirkby.
- Project repository: [LeanEconomics/LeanEconomics](https://github.com/LeanEconomics/LeanEconomics), at commit [8295256b](https://github.com/LeanEconomics/LeanEconomics/tree/8295256bbd64ab488c8cb436d68e7064db560dfc).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 91B50, 90C39, 60J05.
- In Lean Pool: [LeanPool/AiyagariEquilibrium](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AiyagariEquilibrium), from the card [LeanPool/projects/aiyagari-equilibrium.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/aiyagari-equilibrium.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/aiyagari-equilibrium.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/aiyagari-equilibrium.yaml)
- [Lean Pool at 2b205bf9: LeanPool/AiyagariEquilibrium](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/AiyagariEquilibrium)
