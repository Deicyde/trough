---
declaration: instance
origin: cited
lean: BrauerGroup.BruaerGroup, BrauerGroupHom.Br, WedderburnArtin
statement: formalized
---

# Brauer Group Core

> Formalizes central simple algebra infrastructure, Wedderburn-Artin structure theorems, and finite-field triviality for Brauer groups.

*Quoted from the card [LeanPool/projects/brauergroup_new.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/brauergroup_new.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 8 main results, each with its informal statement quoted from the card. The scan finds 8 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`BrauerGroup.BruaerGroup`](https://leanpool.github.io/lean-pool/LeanPool/BrauerGroupNew/BrauerGroup.html#BrauerGroup.BruaerGroup) (instance; a main declaration), declared in [LeanPool/BrauerGroupNew/BrauerGroup.lean, line 409](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BrauerGroupNew/BrauerGroup.lean#L409): “Constructs the Brauer group of a field from Brauer equivalence classes of central simple algebras.”
- [`BrauerGroupHom.Br`](https://leanpool.github.io/lean-pool/LeanPool/BrauerGroupNew/BrauerGroup.html#BrauerGroupHom.Br) (def; a main declaration), declared in [LeanPool/BrauerGroupNew/BrauerGroup.lean, line 678](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BrauerGroupNew/BrauerGroup.lean#L678): “Constructs the Brauer group functor from fields to commutative groups via scalar extension.”
- [`WedderburnArtin`](https://leanpool.github.io/lean-pool/LeanPool/BrauerGroupNew/Wedderburn.html#WedderburnArtin) (theorem; a main declaration), declared in [LeanPool/BrauerGroupNew/Wedderburn.lean, line 403](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BrauerGroupNew/Wedderburn.lean#L403): “Proves a Wedderburn-Artin decomposition for simple Artinian rings as matrix algebras over division rings.”
- [`trivialBrauer`](https://leanpool.github.io/lean-pool/LeanPool/BrauerGroupNew/FiniteField.html#trivialBrauer) (theorem), declared in [LeanPool/BrauerGroupNew/FiniteField.lean, line 38](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BrauerGroupNew/FiniteField.lean#L38): “Proves that every element of the Brauer group of a finite field is trivial.”
- [`WedderburnArtin_algebra_version`](https://leanpool.github.io/lean-pool/LeanPool/BrauerGroupNew/Wedderburn.html#WedderburnArtin_algebra_version) (lemma), declared in [LeanPool/BrauerGroupNew/Wedderburn.lean, line 525](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BrauerGroupNew/Wedderburn.lean#L525): “Gives an algebra equivalence form of Wedderburn-Artin for finite-dimensional central simple algebras.”
- [`IsCentralSimple.TensorProduct.simple`](https://leanpool.github.io/lean-pool/LeanPool/BrauerGroupNew/CentralSimple.html#IsCentralSimple.TensorProduct.simple) (instance), declared in [LeanPool/BrauerGroupNew/CentralSimple.lean, line 493](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BrauerGroupNew/CentralSimple.lean#L493): “Proves simplicity of tensor products of central simple algebras over a field.”
- [`IsCentralSimple.TensorProduct.isCentral`](https://leanpool.github.io/lean-pool/LeanPool/BrauerGroupNew/CentralSimple.html#IsCentralSimple.TensorProduct.isCentral) (instance), declared in [LeanPool/BrauerGroupNew/CentralSimple.lean, line 252](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BrauerGroupNew/CentralSimple.lean#L252): “Proves centrality of tensor products of central algebras over a field.”
- [`CSA_implies_CSA`](https://leanpool.github.io/lean-pool/LeanPool/BrauerGroupNew/CentralSimple.html#CSA_implies_CSA) (theorem), declared in [LeanPool/BrauerGroupNew/CentralSimple.lean, line 569](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BrauerGroupNew/CentralSimple.lean#L569): “Shows that the division algebra factor in a matrix presentation of a central simple algebra is central over the base field.”

## Project

- Authors: Yunzhou Xie, Yichen Feng, Jujian Zhang, Yael Dillies.
- Source: *Central Simple Algebras and Galois Cohomology* by Philippe Gille, Tamás Szamuely, [https://doi.org/10.1017/9781316661277](https://doi.org/10.1017/9781316661277).
- Project repository: [Whysoserioushah/BrauerGroup](https://github.com/Whysoserioushah/BrauerGroup).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 16K20, 16K50, 16S35.
- In Lean Pool: [LeanPool/BrauerGroupNew](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BrauerGroupNew), from the card [LeanPool/projects/brauergroup_new.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/brauergroup_new.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/brauergroup_new.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/brauergroup_new.yaml)
- [Lean Pool at 2b205bf9: LeanPool/BrauerGroupNew](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/BrauerGroupNew)
