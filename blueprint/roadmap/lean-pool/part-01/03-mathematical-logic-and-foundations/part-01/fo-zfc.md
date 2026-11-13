---
declaration: class
origin: cited
lean: FirstOrder.ZFC.ModelZF, FirstOrder.ZFC.ext_induction
statement: formalized
---

# First Order Language of ZF Set Theory

> Formalizes ZF set theory inside Lean's `FirstOrder.Language` framework, enabling meta-mathematical arguments such as elementary submodels.

*Quoted from the card [LeanPool/projects/fo-zfc.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/fo-zfc.yaml) of [LeanPool/lean-pool](https://github.com/LeanPool/lean-pool) at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5), Apache-2.0.*

## Depends on

No dependencies are recorded: edges between declarations need Lean, and this chapter reads the source text without running it.

## Main results

The card lists 2 main results, each with its informal statement quoted from the card. The scan finds 2 of their declarations in the project's files at commit [701389c0](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5). A found declaration links its page in Lean Pool's documentation, which Lean Pool rebuilds daily from its main branch, and its line at this commit.

- [`FirstOrder.ZFC.ModelZF`](https://leanpool.github.io/lean-pool/LeanPool/FoZfc/Replacement.html#FirstOrder.ZFC.ModelZF) (class; a main declaration), declared in [LeanPool/FoZfc/Replacement.lean, line 163](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/FoZfc/Replacement.lean#L163): “Bundles the ZF axioms (Emptyset, Pairing, Union, Powerset, Infinity, Regularity, Comprehension, Replacement) into a single model class.”
- [`FirstOrder.ZFC.ext_induction`](https://leanpool.github.io/lean-pool/LeanPool/FoZfc/Axioms.html#FirstOrder.ZFC.ext_induction) (theorem; a main declaration), declared in [LeanPool/FoZfc/Axioms.lean, line 977](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/FoZfc/Axioms.lean#L977): “States the principle of mathematical induction over ω externally for any bounded formula in LZFC.”

## Project

- Authors: Tetsuya Ishiu.
- Source: *Set Theory* by Thomas Jech, [https://doi.org/10.1007/3-540-44761-X](https://doi.org/10.1007/3-540-44761-X).
- Project repository: [ishiut/fo_zfc](https://github.com/ishiut/fo_zfc).
- Provenance: human, which in Lean Pool's terms means its Lean proofs were “written by people”.
- License: Apache-2.0.
- MSC2020: 03B10, 03E30.
- In Lean Pool: [LeanPool/FoZfc](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/FoZfc), from the card [LeanPool/projects/fo-zfc.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/fo-zfc.yaml).

## Sources

- [Lean Pool at 701389c0: LeanPool/projects/fo-zfc.yaml](https://github.com/LeanPool/lean-pool/blob/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/projects/fo-zfc.yaml)
- [Lean Pool at 701389c0: LeanPool/FoZfc](https://github.com/LeanPool/lean-pool/tree/701389c04bdd56aabf8dbb9ad729165fdba772b5/LeanPool/FoZfc)
