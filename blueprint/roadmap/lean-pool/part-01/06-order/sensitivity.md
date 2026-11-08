---
declaration: theorem
origin: cited
lean: LeanPoolSensitivity.sensitivity_ge_sqrt_degree
statement: formalized
proof: formalized
---

# Sensitivity Conjecture: sqrt(deg) <= sensitivity

> Formalizes the quantitative Nisan-Szegedy/Huang sensitivity theorem for Boolean functions.

*Quoted from the card [LeanPool/projects/sensitivity.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/sensitivity.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`LeanPoolSensitivity.sensitivity_ge_sqrt_degree`](https://leanpool.github.io/lean-pool/LeanPool/Sensitivity/Main.html#LeanPoolSensitivity.sensitivity_ge_sqrt_degree) (theorem; a main declaration), declared in [LeanPool/Sensitivity/Main.lean, line 46](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Sensitivity/Main.lean#L46): “Proves that the square root of multilinear degree is bounded above by sensitivity.”
- [`LeanPoolSensitivity.degree_le_sensitivity_sq`](https://leanpool.github.io/lean-pool/LeanPool/Sensitivity/Consequences.html#LeanPoolSensitivity.degree_le_sensitivity_sq) (theorem), declared in [LeanPool/Sensitivity/Consequences.lean, line 32](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Sensitivity/Consequences.lean#L32): “Derives the degree bound by the square of sensitivity.”

## Project

- Authors: Samuel Schlesinger.
- Source: [doi:10.4007/annals.2019.190.3.6](https://doi.org/10.4007/annals.2019.190.3.6), [arXiv:1907.00847](https://arxiv.org/abs/1907.00847).
- Project repository: [SamuelSchlesinger/sensitivity-conjecture](https://github.com/SamuelSchlesinger/sensitivity-conjecture).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 06E30, 68Q17.
- In Lean Pool: [LeanPool/Sensitivity](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Sensitivity), from the card [LeanPool/projects/sensitivity.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/sensitivity.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/sensitivity.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/sensitivity.yaml)
- [Lean Pool at 2b205bf9: LeanPool/Sensitivity](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/Sensitivity)
