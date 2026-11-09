---
declaration: theorem
origin: cited
lean: MarshallHall.marshallHall, MarshallHall.rank_freeProduct_eq_add
statement: formalized
proof: formalized
---

# Marshall Hall's theorem through finite cores

> Formalizes Marshall Hall's finite-index free-factor theorem for finitely generated subgroups of finite-rank free groups. The proof extracts the finitely many suffix states of a subgroup generating set, completes the resulting partial generator actions to permutations of a finite state set, identifies the connected orbit with a finite core, and extends a geodesic spanning tree to obtain an inclusion-compatible free-product decomposition. It also exposes an explicit finite permutation separator for every finitely generated subgroup and element outside it, yielding the LERF consequence. The repository also proves binary and finite-indexed free-group instances of Grushko--Neumann rank additivity, and the arbitrary-factor binary theorem. The arbitrary-factor proof is carried by a finite labelled-graph fold, source-unfold, and monochromatic-vertex contraction reduction.

*Quoted from the card [LeanPool/projects/marshallhalltheorem.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/marshallhalltheorem.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 3 main results, each with its informal statement quoted from the card. The scan finds 3 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`MarshallHall.marshallHall`](https://leanpool.github.io/lean-pool/LeanPool/MarshallHall/MarshallHall/Hall.html#MarshallHall.marshallHall) (theorem; a main declaration), declared in [LeanPool/MarshallHall/MarshallHall/Hall.lean, line 376](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MarshallHall/MarshallHall/Hall.lean#L376): “Every finitely generated subgroup of a finite-rank free group is an inclusion-compatible free factor of a finite-index subgroup.”
- [`LERFChallenge.freeGroup_finite_permutation_separator`](https://leanpool.github.io/lean-pool/LeanPool/MarshallHall/LERFSolution.html#LERFChallenge.freeGroup_finite_permutation_separator) (theorem), declared in [LeanPool/MarshallHall/LERFSolution.lean, line 45](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MarshallHall/LERFSolution.lean#L45): “Every element outside a finitely generated subgroup of a finite-rank free group can be separated by an explicit finite permutation action.”
- [`MarshallHall.rank_freeProduct_eq_add`](https://leanpool.github.io/lean-pool/LeanPool/MarshallHall/MarshallHall.html#MarshallHall.rank_freeProduct_eq_add) (theorem; a main declaration), declared in [LeanPool/MarshallHall/MarshallHall.lean, line 51](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MarshallHall/MarshallHall.lean#L51): “The rank of a free product of finitely generated groups is the sum of their ranks.”

## Project

- Authors: Arthur Freitas Ramos, David Barros Hulak, Ruy J. G. B. de Queiroz.
- Project repository: [arthur742ramos/marshallhalltheorem](https://github.com/arthur742ramos/marshallhalltheorem), at commit [99f41964](https://github.com/arthur742ramos/marshallhalltheorem/tree/99f419644cebf61a5f78eac334fcc1f19b0ccc73).
- Provenance: AI, which in Lean Pool's terms means its Lean proofs were “mostly produced by an AI system”.
- License: Apache-2.0.
- MSC2020: 20E07, 20F65, 05C25.
- In Lean Pool: [LeanPool/MarshallHall](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MarshallHall), from the card [LeanPool/projects/marshallhalltheorem.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/marshallhalltheorem.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/marshallhalltheorem.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/marshallhalltheorem.yaml)
- [Lean Pool at 2b205bf9: LeanPool/MarshallHall](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/MarshallHall)
