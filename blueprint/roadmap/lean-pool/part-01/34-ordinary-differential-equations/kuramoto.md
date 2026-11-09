---
declaration: theorem
origin: cited
lean: kuramotoR_norm_le_one, weighted_lyapunov_descent
statement: formalized
proof: formalized
---

# Finite-N Kuramoto Synchronization

> Formalizes the finite-N Kuramoto model of coupled phase oscillators: the order parameter and its unit bound, the potential/force gradient identities, smoothness and local Lipschitz continuity of the vector field with ODE existence and uniqueness, Lyapunov descent along trajectories, pairwise and semicircle contraction estimates, Hebbian phase/weight dynamics, and full convergence to synchrony under all-to-all coupling from initial phases in an open semicircle.

*Quoted from the card [LeanPool/projects/kuramoto.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/kuramoto.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`kuramotoR_norm_le_one`](https://leanpool.github.io/lean-pool/LeanPool/Kuramoto/OrderParameter.html#kuramotoR_norm_le_one) (theorem; a main declaration), declared in [LeanPool/Kuramoto/OrderParameter.lean, line 28](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Kuramoto/OrderParameter.lean#L28): “The Kuramoto order parameter has norm at most one for any phase configuration.”
- [`weighted_lyapunov_descent`](https://leanpool.github.io/lean-pool/LeanPool/Kuramoto/Weighted.html#weighted_lyapunov_descent) (theorem; a main declaration), declared in [LeanPool/Kuramoto/Weighted.lean, line 185](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Kuramoto/Weighted.lean#L185): “The weighted Kuramoto potential is non-increasing along the gradient flow, since the sum of force times potential-derivative over all oscillators is at most zero.”
- [`allToAll_convergence_to_synchrony`](https://leanpool.github.io/lean-pool/LeanPool/Kuramoto/Frontier.html#allToAll_convergence_to_synchrony) (theorem), declared in [LeanPool/Kuramoto/Frontier.lean, line 1019](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Kuramoto/Frontier.lean#L1019): “Under all-to-all coupling with positive strength and initial phases in an open semicircle, the order parameter norm tends to one, i.e. the oscillators synchronize.”

## Project

- Authors: Ben Cassie.
- Source: *Finite-N Kuramoto synchronization: order-parameter bounds and Lyapunov descent* by Ben Cassie.
- Project repository: [velvetmonkey/kuramoto-lean](https://github.com/velvetmonkey/kuramoto-lean).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0.
- MSC2020: 34D06.
- In Lean Pool: [LeanPool/Kuramoto](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Kuramoto), from the card [LeanPool/projects/kuramoto.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/kuramoto.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/kuramoto.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/kuramoto.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Kuramoto](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Kuramoto)
