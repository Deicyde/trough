---
declaration: class
origin: cited
lean: FirstOrder.ZFC.ModelZF, FirstOrder.ZFC.ext_induction
statement: formalized
---

# First Order Language of ZF Set Theory

> Formalizes ZF set theory inside Lean's `FirstOrder.Language` framework, enabling meta-mathematical arguments such as elementary submodels.

*Quoted from the card [LeanPool/projects/fo-zfc.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/fo-zfc.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd), Apache-2.0.*

## Depends on

No dependencies are recorded: Lean Pool's projects do not import one another, and this chapter reads their source text without running Lean, which edges between declarations need.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [2b205bf9](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd). A found declaration links its page in Lean Pool's documentation, which is built from Lean Pool's newest commit, and its line at this commit.

- [`FirstOrder.ZFC.ModelZF`](https://leanpool.github.io/lean-pool/LeanPool/FoZfc/Replacement.html#FirstOrder.ZFC.ModelZF) (class; a main declaration), declared in [LeanPool/FoZfc/Replacement.lean, line 163](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FoZfc/Replacement.lean#L163): “Bundles the ZF axioms (Emptyset, Pairing, Union, Powerset, Infinity, Regularity, Comprehension, Replacement) into a single model class.”
- [`FirstOrder.ZFC.ext_induction`](https://leanpool.github.io/lean-pool/LeanPool/FoZfc/Axioms.html#FirstOrder.ZFC.ext_induction) (theorem; a main declaration), declared in [LeanPool/FoZfc/Axioms.lean, line 977](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FoZfc/Axioms.lean#L977): “States the principle of mathematical induction over ω externally for any bounded formula in LZFC.”

## Project

- Authors: Tetsuya Ishiu.
- Source: *Set Theory* by Thomas Jech, [https://doi.org/10.1007/3-540-44761-X](https://doi.org/10.1007/3-540-44761-X).
- Project repository: [ishiut/fo_zfc](https://github.com/ishiut/fo_zfc).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 03B10, 03E30.
- In Lean Pool: [LeanPool/FoZfc](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FoZfc), from the card [LeanPool/projects/fo-zfc.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/fo-zfc.yaml).

## Sources

- [Lean Pool at 2b205bf9: LeanPool/projects/fo-zfc.yaml](https://github.com/LeanPool/lean-pool/blob/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/projects/fo-zfc.yaml)
- [Lean Pool at 2b205bf9: LeanPool/FoZfc](https://github.com/LeanPool/lean-pool/tree/2b205bf904013a5e06d8ef03069430dd79e1c8bd/LeanPool/FoZfc)
