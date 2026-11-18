---
declaration: module
origin: cited
lean: ProbabilisticTheory.JordanAlgebra.quadRepPositiveLinearMap_mul_self, ProbabilisticTheory.JordanAlgebra.quadRepPositiveLinearMap_fundamental
statement: formalized
proof: formalized
---

# Composing quadratic operations

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.Quadratic.Operational`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Operational.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Operational.lean): 2 declarations, 2 with a docstring.

> The fundamental formula as an identity between the positive linear maps `U_a`.

## i. Overview

> For quadratically positive Jordan algebras the positive maps `U_a` compose according to the
> fundamental formula.

## ii. Key results

> - `JordanAlgebra.quadRepPositiveLinearMap_fundamental` : the fundamental formula for the positive
>   maps `U_a`.

## iv. References

> * None.

## A. Composition of positive quadratic operations

**`ProbabilisticTheory.JordanAlgebra.quadRepPositiveLinearMap_mul_self`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Operational.lean#L52).

> Squaring the filtering observable composes its positive quadratic operation with itself.
> This is the bundled operational form of `U_(a²) = U_a ∘ U_a`.

```lean
lemma quadRepPositiveLinearMap_mul_self (a : E) :
    quadRepPositiveLinearMap (a * a) =
      (quadRepPositiveLinearMap a).comp (quadRepPositiveLinearMap a)
```

**`ProbabilisticTheory.JordanAlgebra.quadRepPositiveLinearMap_fundamental`**, a lemma, [line 63](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Operational.lean#L63).

> The quadratic fundamental formula as an equality of positive operations.  Thus a filter
> whose observable is `U_a b` is precisely the sequential filter `U_a`, then `U_b`, then `U_a`.
> The statement is intrinsic Jordan algebra; positivity is used only to bundle the maps.

```lean
lemma quadRepPositiveLinearMap_fundamental (a b : E) :
    quadRepPositiveLinearMap (U a b) =
      (quadRepPositiveLinearMap a).comp
        ((quadRepPositiveLinearMap b).comp (quadRepPositiveLinearMap a))
```

## Depends on

- [Positive quadratic representations](quadratic-order.md)

## Proof depends on

- [The fundamental formula](quadratic-fundamental.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Operational.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Operational.lean)
