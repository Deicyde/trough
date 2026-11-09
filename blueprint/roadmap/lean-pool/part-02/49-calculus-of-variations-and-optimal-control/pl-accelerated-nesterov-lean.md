---
declaration: theorem
origin: cited
lean: PLAcceleratedNesterovLean.nesterov_pl_accelerated_rate
statement: formalized
proof: formalized
---

# Accelerated Nesterov convergence under local Polyak-Lojasiewicz conditions

> Formalizes accelerated Nesterov convergence near a smooth minimizer manifold under a local Polyak-Lojasiewicz condition, including embedded-manifold and C3 public theorem statements with explicit exponential rate and prefactor.

*Quoted from the card [LeanPool/projects/pl-accelerated-nesterov-lean.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/pl-accelerated-nesterov-lean.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`PLAcceleratedNesterovLean.nesterov_pl_accelerated_rate`](https://leanpool.github.io/lean-pool/LeanPool/PLAcceleratedNesterovLean/MainTheorem.html#PLAcceleratedNesterovLean.nesterov_pl_accelerated_rate) (theorem; a main declaration), declared in [LeanPool/PLAcceleratedNesterovLean/MainTheorem.lean, line 55](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PLAcceleratedNesterovLean/MainTheorem.lean#L55): “Proves an accelerated Nesterov convergence rate for state positions near a C2 embedded minimizer manifold, with an existential momentum parameter, explicit exponential decay, and prefactor 2.” Its source, as the card gives it: “Z. Feng and H. Yuan, Optimal local linear convergence of Nesterov's accelerated gradient method for C2 functions under the Polyak-Lojasiewicz inequality, arXiv:2603.21516.”
- [`PLAcceleratedNesterovLean.nesterov_pl_accelerated_rate_c3`](https://leanpool.github.io/lean-pool/LeanPool/PLAcceleratedNesterovLean/MainTheorem.html#PLAcceleratedNesterovLean.nesterov_pl_accelerated_rate_c3) (theorem), declared in [LeanPool/PLAcceleratedNesterovLean/MainTheorem.lean, line 90](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PLAcceleratedNesterovLean/MainTheorem.lean#L90): “Proves the corresponding C3 public theorem, deriving the minimizer geometry internally from smoothness and the Polyak-Lojasiewicz condition.” Its source, as the card gives it: “Z. Feng and H. Yuan, Optimal local linear convergence of Nesterov's accelerated gradient method for C2 functions under the Polyak-Lojasiewicz inequality, arXiv:2603.21516.”
- [`PLAcceleratedNesterovLean.nesterov_convergence_at_base_point_position_theta`](https://leanpool.github.io/lean-pool/LeanPool/PLAcceleratedNesterovLean/Convergence/NesterovConvergence.html#PLAcceleratedNesterovLean.nesterov_convergence_at_base_point_position_theta) (theorem), declared in [LeanPool/PLAcceleratedNesterovLean/Convergence/NesterovConvergence.lean, line 351](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PLAcceleratedNesterovLean/Convergence/NesterovConvergence.lean#L351): “Provides the reusable local theta-retuned convergence theorem used by the public accelerated-rate statements.” Its source, as the card gives it: “Z. Feng and H. Yuan, Optimal local linear convergence of Nesterov's accelerated gradient method for C2 functions under the Polyak-Lojasiewicz inequality, arXiv:2603.21516.”

## Project

- Authors: Max Obreiter, Tobias Steinbrecher, Robert Foerster.
- Source: *Optimal local linear convergence of Nesterov's accelerated gradient method for C2 functions under the Polyak-Lojasiewicz inequality* by Zixu Feng, Hao Yuan, [arXiv:2603.21516](https://arxiv.org/abs/2603.21516).
- Project repository: [M1ngXU/PL-Accelerated-Nesterov-Lean](https://github.com/M1ngXU/PL-Accelerated-Nesterov-Lean).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0.
- MSC2020: 49M37, 65K05, 58C15.
- In Lean Pool: [LeanPool/PLAcceleratedNesterovLean](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PLAcceleratedNesterovLean), from the card [LeanPool/projects/pl-accelerated-nesterov-lean.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/pl-accelerated-nesterov-lean.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/pl-accelerated-nesterov-lean.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/pl-accelerated-nesterov-lean.yaml)
- [Lean Pool at 2b205bf9: LeanPool/PLAcceleratedNesterovLean](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/PLAcceleratedNesterovLean)
