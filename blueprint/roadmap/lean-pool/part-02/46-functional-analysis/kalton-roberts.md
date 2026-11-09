---
declaration: theorem
origin: cited
lean: KaltonRoberts.KR_constant_lt
statement: formalized
proof: formalized
---

# Halving the Kalton-Roberts upper bound

> Formalizes the paper-style Boolean-algebra theorem that every approximately additive real-valued set function is uniformly close to a finitely additive signed measure, proving the certified Kalton-Roberts constant bound below 19.838.

*Quoted from the card [LeanPool/projects/kalton-roberts.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/kalton-roberts.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`KaltonRoberts.KR_constant_lt`](https://leanpool.github.io/lean-pool/LeanPool/KaltonRoberts/MainTheorem.html#KaltonRoberts.KR_constant_lt) (theorem; a main declaration), declared in [LeanPool/KaltonRoberts/MainTheorem.lean, line 349](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/KaltonRoberts/MainTheorem.lean#L349): “Proves the headline certified bound that the Kalton-Roberts constant is strictly less than 9919/500, i.e. 19.838.”
- [`KaltonRoberts.KR_constant_le_C₂`](https://leanpool.github.io/lean-pool/LeanPool/KaltonRoberts/MainTheorem.html#KaltonRoberts.KR_constant_le_C%E2%82%82) (theorem), declared in [LeanPool/KaltonRoberts/MainTheorem.lean, line 339](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/KaltonRoberts/MainTheorem.lean#L339): “Proves the exact rational upper bound C₂ = 694198146664396294486127753 / 34994834677886019996000000 for the Kalton-Roberts constant.”
- [`KaltonRoberts.set_algebra_bound_C₂`](https://leanpool.github.io/lean-pool/LeanPool/KaltonRoberts/MainTheorem.html#KaltonRoberts.set_algebra_bound_C%E2%82%82) (theorem), declared in [LeanPool/KaltonRoberts/MainTheorem.lean, line 326](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/KaltonRoberts/MainTheorem.lean#L326): “States the paper-style set-algebra formulation, where every approximately additive function on a Boolean subalgebra of sets is within C₂ times the error of a finitely additive signed measure.”

## Project

- Authors: Ho Boon Suan.
- Source: *Halving the original Kalton-Roberts upper bound for nearly additive set functions* by Ho Boon Suan, Tomasz Kania, [arXiv:2606.06807](https://arxiv.org/abs/2606.06807).
- Project repository: [boonsuan/KaltonRoberts](https://github.com/boonsuan/KaltonRoberts).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: MIT, under which the project was published; Lean Pool redistributes it under Apache-2.0.
- MSC2020: 46B20, 28A12, 05C35.
- In Lean Pool: [LeanPool/KaltonRoberts](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/KaltonRoberts), from the card [LeanPool/projects/kalton-roberts.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/kalton-roberts.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/kalton-roberts.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/kalton-roberts.yaml)
- [Lean Pool at 2b205bf9: LeanPool/KaltonRoberts](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/KaltonRoberts)
