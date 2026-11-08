---
declaration: theorem
origin: cited
lean: LieTrotter.norm_trotter_sub_le_commutator, LieTrotter.trotter_product
statement: formalized
proof: formalized
---

# Lie–Trotter product formula with commutator scaling

> Proves the Lie–Trotter product formula in a complete normed real algebra with norm-one unit, with an explicit error bound proportional to the commutator.

*Quoted from the card [LeanPool/projects/lie-trotter-commutator.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lie-trotter-commutator.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`LieTrotter.norm_trotter_sub_le_commutator`](https://leanpool.github.io/lean-pool/LeanPool/LieTrotter/Commutator.html#LieTrotter.norm_trotter_sub_le_commutator) (theorem; a main declaration), declared in [LeanPool/LieTrotter/Commutator.lean, line 176](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LieTrotter/Commutator.lean#L176): “For elements A and B of a complete normed real algebra with norm-one unit and every integer n at least one, the norm of the difference between (exp(A/n) exp(B/n))^n and exp(A+B) is at most norm(AB-BA) exp(norm(A)+norm(B))/(2n).”
- [`LieTrotter.trotter_product`](https://leanpool.github.io/lean-pool/LeanPool/LieTrotter/Basic.html#LieTrotter.trotter_product) (theorem; a main declaration), declared in [LeanPool/LieTrotter/Basic.lean, line 312](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LieTrotter/Basic.lean#L312): “For any two elements of a complete normed real algebra with norm-one unit, (exp(A/n) exp(B/n))^n converges in norm to exp(A+B).”

## Project

- Authors: Zayn Blore.
- Project repository: [zblore/lie-trotter-lean](https://github.com/zblore/lie-trotter-lean).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 46H30, 47D06, 15A16.
- In Lean Pool: [LeanPool/LieTrotter](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LieTrotter), from the card [LeanPool/projects/lie-trotter-commutator.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lie-trotter-commutator.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/lie-trotter-commutator.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/lie-trotter-commutator.yaml)
- [Lean Pool at 2b205bf9: LeanPool/LieTrotter](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/LieTrotter)
