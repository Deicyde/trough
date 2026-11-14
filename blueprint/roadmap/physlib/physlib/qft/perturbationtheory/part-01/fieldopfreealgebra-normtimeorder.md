---
declaration: module
origin: cited
lean: FieldSpecification.FieldOpFreeAlgebra.normTimeOrder, FieldSpecification.FieldOpFreeAlgebra.normTimeOrder_ofCrAnListF
statement: formalized
proof: formalized
---

# Norm-time Ordering in the FieldOpFreeAlgebra

The module `Physlib.QFT.PerturbationTheory.FieldOpFreeAlgebra.NormTimeOrder`, [Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormTimeOrder.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormTimeOrder.lean): 2 declarations, 1 with a docstring.

## Norm-time order

**`FieldSpecification.FieldOpFreeAlgebra.normTimeOrder`**, a def, [line 34](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormTimeOrder.lean#L34).

> The normal-time ordering on `FieldOpFreeAlgebra`.

```lean
def normTimeOrder : FieldOpFreeAlgebra 𝓕 →ₗ[ℂ] FieldOpFreeAlgebra 𝓕
```

**`FieldSpecification.FieldOpFreeAlgebra.normTimeOrder_ofCrAnListF`**, a lemma, [line 41](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormTimeOrder.lean#L41).

```lean
lemma normTimeOrder_ofCrAnListF (φs : List 𝓕.CrAnFieldOp) :
    𝓣𝓝ᶠ(ofCrAnListF φs) = normTimeOrderSign φs • ofCrAnListF (normTimeOrderList φs)
```

## Depends on

- [Creation and annihilation free-algebra](fieldopfreealgebra-basic.md)
- [Time ordering of states](fieldspecification-timeorder.md)

## Sources

- [Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormTimeOrder.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/Physlib/QFT/PerturbationTheory/FieldOpFreeAlgebra/NormTimeOrder.lean)
