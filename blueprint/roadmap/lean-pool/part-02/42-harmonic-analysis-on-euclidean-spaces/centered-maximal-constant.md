---
declaration: theorem
origin: cited
lean: LeanPool.CenteredMaximal.ofReal_phi_le_weakTypeConstant_two
statement: formalized
proof: formalized
---

# Bounds for the centered Hardy-Littlewood maximal constant

> Proves that the weak type (1,1) constant c_2 of the centered maximal operator over axis-parallel squares is at least the explicit radical phi, approximately 1.68551, using a weighted periodic lattice and integrable approximations. Also proves c_d <= 2^d in every natural dimension and 1.685 < phi < 1.686. The operator acts on real-valued integrable functions, with Lebesgue outer measure of strict level sets. Includes the maximal-function API, a Vitali covering argument, lattice witnesses, smearing estimates, and the limiting lower bound. No optimality of phi is claimed.

*Quoted from the card [LeanPool/projects/centered-maximal-constant.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/centered-maximal-constant.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`LeanPool.CenteredMaximal.ofReal_phi_le_weakTypeConstant_two`](https://leanpool.github.io/lean-pool/LeanPool/CenteredMaximal.html#LeanPool.CenteredMaximal.ofReal_phi_le_weakTypeConstant_two) (theorem; a main declaration), declared in [LeanPool/CenteredMaximal.lean, line 63](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CenteredMaximal.lean#L63): “The explicit radical phi is a lower bound for c_2, the infimum of all weak type (1,1) bounds for the centered maximal operator over axis-parallel squares in the real plane.”
- [`LeanPool.CenteredMaximal.weakTypeConstant_le_two_pow`](https://leanpool.github.io/lean-pool/LeanPool/CenteredMaximal.html#LeanPool.CenteredMaximal.weakTypeConstant_le_two_pow) (theorem), declared in [LeanPool/CenteredMaximal.lean, line 58](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CenteredMaximal.lean#L58): “For every natural number d, including zero, the centered maximal operator over axis-parallel cubes in real d-space has weak type (1,1) constant c_d at most 2^d.”
- [`LeanPool.CenteredMaximal.phi_mem_Ioo`](https://leanpool.github.io/lean-pool/LeanPool/CenteredMaximal/Numerics.html#LeanPool.CenteredMaximal.phi_mem_Ioo) (theorem), declared in [LeanPool/CenteredMaximal/Numerics.lean, line 24](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CenteredMaximal/Numerics.lean#L24): “The explicit radical constant phi lies strictly between 1.685 and 1.686.”

## Project

- Authors: Yongxi Lin.
- Source: *A lower bound 1.6855 for the planar centred maximal constant over squares* by Yongxi Lin.
- Project repository: [CoolRmal/centered-maximal-constant](https://github.com/CoolRmal/centered-maximal-constant), at commit [c6a8cb29](https://github.com/CoolRmal/centered-maximal-constant/tree/c6a8cb29e8ecce9ac4614a8c7e4bf6938366f986).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 42B25, 26D15.
- In Lean Pool: [LeanPool/CenteredMaximal](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CenteredMaximal), from the card [LeanPool/projects/centered-maximal-constant.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/centered-maximal-constant.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/centered-maximal-constant.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/centered-maximal-constant.yaml)
- [Lean Pool at 2b205bf9: LeanPool/CenteredMaximal](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/CenteredMaximal)
