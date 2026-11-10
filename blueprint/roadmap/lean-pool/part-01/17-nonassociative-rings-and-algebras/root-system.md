---
declaration: def
origin: cited
lean: An.rootPairing, BCn.rootPairing, BCn.isReflective_iff_isClassicalRoot
statement: formalized
---

# Explicit type Aₙ and BCₙ root pairings

> Constructs the type Aₙ and BCₙ root pairings explicitly over ℤ — from signed intervals on Fin n and from the reflective vectors of the standard dot product — proves the pairing and reflection identities exhibiting them as Mathlib `RootPairing`s, and identifies the BCₙ roots with the classical set {±eᵢ, ±2eᵢ, ±eᵢ ± eⱼ}.

*Quoted from the card [LeanPool/projects/root-system.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/root-system.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 4 main results, each with its informal statement quoted from the card. The scan finds 4 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`An.rootPairing`](https://leanpool.github.io/lean-pool/LeanPool/RootSystem/An.html#An.rootPairing) (def; a main declaration), declared in [LeanPool/RootSystem/An.lean, line 456](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RootSystem/An.lean#L456): “Constructs the type Aₙ root pairing over the integers from signed intervals on Fin n, with finiteness, reducedness, and crystallographic properties.” Its source, as the card gives it: “N. Bourbaki, Lie Groups and Lie Algebras, Chapters 4-6, Springer, 2002; J. E. Humphreys, Introduction to Lie Algebras and Representation Theory, GTM 9, Springer, 1972, Ch. III.”
- [`BCn.rootPairing`](https://leanpool.github.io/lean-pool/LeanPool/RootSystem/BCn.html#BCn.rootPairing) (def; a main declaration), declared in [LeanPool/RootSystem/BCn.lean, line 81](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RootSystem/BCn.lean#L81): “Constructs the type BCₙ root pairing from the reflective vectors of the standard dot product on ℤⁿ via a symmetric nondegenerate form.”
- [`BCn.isReflective_iff_isClassicalRoot`](https://leanpool.github.io/lean-pool/LeanPool/RootSystem/BCn.html#BCn.isReflective_iff_isClassicalRoot) (theorem; a main declaration), declared in [LeanPool/RootSystem/BCn.lean, line 259](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RootSystem/BCn.lean#L259): “Characterizes the reflective vectors of the standard dot product on ℤⁿ as exactly the classical type BCₙ roots ±eᵢ, ±2eᵢ, and ±eᵢ ± eⱼ for i ≠ j.”
- [`BCn.range_rootPairing_root`](https://leanpool.github.io/lean-pool/LeanPool/RootSystem/BCn.html#BCn.range_rootPairing_root) (theorem), declared in [LeanPool/RootSystem/BCn.lean, line 265](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RootSystem/BCn.lean#L265): “Identifies the root set of the type BCₙ root pairing with the classical type BCₙ root set.”

## Project

- Authors: Antoine de Saint Germain, Ambrose Tang.
- Source: *Introduction to Lie Algebras and Representation Theory* by James E. Humphreys, [doi:10.1007/978-1-4612-6398-2](https://doi.org/10.1007/978-1-4612-6398-2), [https://antoine-dsg.github.io/root_system/](https://antoine-dsg.github.io/root_system/).
- Project repository: [Antoine-dSG/root_system](https://github.com/Antoine-dSG/root_system).
- Provenance: mix, which in Lean Pool's terms means people and AI “both contributed substantially” to its Lean proofs.
- License: Apache-2.0.
- MSC2020: 17B22, 20F55.
- In Lean Pool: [LeanPool/RootSystem](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RootSystem), from the card [LeanPool/projects/root-system.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/root-system.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/root-system.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/root-system.yaml)
- [Lean Pool at 2b205bf9: LeanPool/RootSystem](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/RootSystem)
