---
declaration: module
origin: cited
lean: LorentzGroup.sum_minkowskiMatrixZ_mul
statement: formalized
proof: formalized
---

# The defining relation of the Lorentz group on its entries

The module `PhyslibAlpha.Relativity.LorentzGroup.Basic`, [PhyslibAlpha/Relativity/LorentzGroup/Basic.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Basic.lean): 1 declaration, 1 with a docstring.

> The relation `Λ η Λᵀ = η` over `ℂ`, read on a single entry and with integer metric entries.

## i. Overview

> `Physlib.Relativity.LorentzGroup.Basic` states the defining relation of the Lorentz group as
> the matrix equation `Λ η Λᵀ = η` over `ℝ`. A classification of invariant tensors contracts
> that relation one metric pairing at a time, over `ℂ` and against entries which a decision
> procedure has to evaluate. `sum_minkowskiMatrixZ_mul` is the relation in exactly that form:
> the entry `(a, b)`, the coefficients cast into `ℂ`, and the metric entries taken from
> `minkowskiMatrixZ` rather than `minkowskiMatrix`.

## ii. Key results

> - `LorentzGroup.sum_minkowskiMatrixZ_mul` : the defining relation on the entry `(a, b)`, over
>   `ℂ` and with integer metric entries.

## iv. References

> The defining relation and its matrix forms are in `Physlib.Relativity.LorentzGroup.Basic`.

## A. The defining relation on an entry

**`LorentzGroup.sum_minkowskiMatrixZ_mul`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Basic.lean#L61).

> The defining relation `Λ η Λᵀ = η` over `ℂ`, read on the entry `(a, b)` and with the
> integer Minkowski matrix in place of `minkowskiMatrix`. This is the form the invariant
> classifications contract against, one metric pairing per pair of slots.

```lean
lemma sum_minkowskiMatrixZ_mul (Λ : LorentzGroup d) (a b : Fin 1 ⊕ Fin d) :
    ∑ x : Fin 1 ⊕ Fin d, ∑ y : Fin 1 ⊕ Fin d, ((minkowskiMatrixZ x y : ℤ) : ℂ)
        * (((Λ.1 a x : ℝ) : ℂ) * ((Λ.1 b y : ℝ) : ℂ))
      = ((minkowskiMatrixZ a b : ℤ) : ℂ)
```

## Depends on

- [The Lorentz Group](../../../physlib/relativity/lorentzgroup/basic.md)
- [The Minkowski matrix over the integers](../minkowskimatrix.md)

## Sources

- [PhyslibAlpha/Relativity/LorentzGroup/Basic.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/Relativity/LorentzGroup/Basic.lean)
