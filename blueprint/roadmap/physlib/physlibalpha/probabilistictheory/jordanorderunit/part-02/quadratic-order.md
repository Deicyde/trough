---
declaration: module
origin: cited
lean: ProbabilisticTheory.JordanAlgebra.IsQuadraticallyPositive, ProbabilisticTheory.JordanAlgebra.quadRep_nonneg, ProbabilisticTheory.JordanAlgebra.quadRepPositiveLinearMap, ProbabilisticTheory.JordanAlgebra.coe_quadRepPositiveLinearMap, ProbabilisticTheory.JordanAlgebra.quadRepPositiveLinearMap_apply, ProbabilisticTheory.JordanAlgebra.quadRepPositiveLinearMap_one, ProbabilisticTheory.JordanAlgebra.quadRep_monotone
statement: formalized
proof: formalized
---

# Positive quadratic representations

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.Quadratic.Order`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Order.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Order.lean): 7 declarations, 5 with a docstring.

> Quadratically positive Jordan order-unit spaces, where each `U_a` is a positive linear map.

## i. Overview

> The quadratic representation `U_a` is the Jordan version of the operation `b ↦ a b a`. A Jordan
> order-unit space is quadratically positive when every `U_a` preserves the positive cone; then each
> `U_a` is a positive linear map.

## ii. Key results

> - `JordanAlgebra.IsQuadraticallyPositive` : quadratically positive Jordan order-unit spaces.
> - `JordanAlgebra.quadRepPositiveLinearMap` : `U_a` as a positive linear map.

## iv. References

> * None.

## A. Quadratically positive Jordan algebras

**`ProbabilisticTheory.JordanAlgebra.IsQuadraticallyPositive`**, a class, [line 53](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Order.lean#L53).

> Every quadratic representation `U_a` preserves the positive cone.

```lean
class IsQuadraticallyPositive (E : Type*) [NonAssocCommRing E] [PartialOrder E]
    [IsOrderedAddMonoid E] [Module ℝ E] [SMulCommClass ℝ E E] : Prop where
  quadRep_nonneg : ∀ (a : E) {b : E}, 0 ≤ b → 0 ≤ U a b
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_nonneg`**, a lemma, [line 60](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Order.lean#L60).

> Quadratic representations map nonnegative observables to nonnegative observables.

```lean
lemma quadRep_nonneg (a : E) {b : E} (hb : 0 ≤ b) : 0 ≤ U a b
```

## B. The positive linear map `U_a`

**`ProbabilisticTheory.JordanAlgebra.quadRepPositiveLinearMap`**, a def, [line 66](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Order.lean#L66).

> The quadratic representation as a bundled positive linear operation.

```lean
def quadRepPositiveLinearMap (a : E) : E →ₚ[ℝ] E
```

**`ProbabilisticTheory.JordanAlgebra.coe_quadRepPositiveLinearMap`**, a lemma, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Order.lean#L70).

```lean
lemma coe_quadRepPositiveLinearMap (a : E) :
    (quadRepPositiveLinearMap a : E →ₗ[ℝ] E) = U a
```

**`ProbabilisticTheory.JordanAlgebra.quadRepPositiveLinearMap_apply`**, a lemma, [line 75](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Order.lean#L75).

```lean
lemma quadRepPositiveLinearMap_apply (a b : E) : quadRepPositiveLinearMap a b = U a b
```

**`ProbabilisticTheory.JordanAlgebra.quadRepPositiveLinearMap_one`**, a lemma, [line 80](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Order.lean#L80).

> The unit has the identity quadratic operation.

```lean
lemma quadRepPositiveLinearMap_one :
    quadRepPositiveLinearMap (1 : E) = PositiveLinearMap.id ℝ E
```

**`ProbabilisticTheory.JordanAlgebra.quadRep_monotone`**, a lemma, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Order.lean#L87).

> Positivity of `U a` implies monotonicity.

```lean
lemma quadRep_monotone (a : E) : Monotone (U a)
```

## Depends on

- [Powers, multiplication operators and the quadratic representation](../part-01/operator.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Order.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/Quadratic/Order.lean)
