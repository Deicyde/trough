---
declaration: module
origin: cited
lean: ProbabilisticTheory.NormedJordanAlgebra.isBoundedBilinearMap_mul, ProbabilisticTheory.NormedJordanAlgebra.continuous_mul_left, ProbabilisticTheory.NormedJordanAlgebra.continuous_mul_right, ProbabilisticTheory.NormedJordanAlgebra.mulLeftCLM, ProbabilisticTheory.NormedJordanAlgebra.mulLeftCLM_apply, ProbabilisticTheory.NormedJordanAlgebra.norm_quadRep_le, ProbabilisticTheory.NormedJordanAlgebra.quadRepCLM, ProbabilisticTheory.NormedJordanAlgebra.quadRepCLM_apply
statement: formalized
proof: formalized
---

# Generators of JB automorphism groups

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.JB.Dynamics`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean): 9 declarations, 7 with a docstring.

> The Jordan product is bounded, and generators of Jordan automorphism families are derivations.

## i. Overview

> The Jordan product of a normed Jordan algebra is a bounded bilinear map, so multiplication operators
> and quadratic representations are continuous linear maps. The generator of a differentiable
> one-parameter family of Jordan automorphisms is a Jordan derivation.

## ii. Key results

> - `NormedJordanAlgebra.isBoundedBilinearMap_mul` : the Jordan product is bounded bilinear.
> - `NormedJordanAlgebra.mulLeftCLM`, `NormedJordanAlgebra.quadRepCLM` : `L_a` and `U_a` as continuous
>   linear maps.
> - `NormedJordanAlgebra.isDerivation_of_isAutomorphismFamily` : the generator of a family of
>   automorphisms is a derivation.
> - `NormedJordanAlgebra.norm_quadRep_le` : `‖U_a b‖ ≤ 3 ‖a‖² ‖b‖`.

## iv. References

> * None.

## A. The Jordan product is bounded bilinear

**`ProbabilisticTheory.NormedJordanAlgebra.isBoundedBilinearMap_mul`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean#L55).

> The Jordan product of a normed Jordan algebra is bounded bilinear, with bound constant `1`.

```lean
lemma isBoundedBilinearMap_mul :
    IsBoundedBilinearMap ℝ (fun p : E × E => p.1 * p.2)
```

**`ProbabilisticTheory.NormedJordanAlgebra.continuous_mul_left`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean#L64).

> Left Jordan multiplication by a fixed element is continuous.

```lean
lemma continuous_mul_left (a : E) : Continuous fun x : E => a * x
```

**`ProbabilisticTheory.NormedJordanAlgebra.continuous_mul_right`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean#L68).

> Right Jordan multiplication by a fixed element is continuous.

```lean
lemma continuous_mul_right (a : E) : Continuous fun x : E => x * a
```

## B. Continuous multiplication and quadratic operators

**`ProbabilisticTheory.NormedJordanAlgebra.mulLeftCLM`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean#L77).

> Left Jordan multiplication as a bounded linear operator, with operator bound `‖a‖`.

```lean
noncomputable def mulLeftCLM (a : E) : E →L[ℝ] E
```

**`ProbabilisticTheory.NormedJordanAlgebra.mulLeftCLM_apply`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean#L81).

```lean
lemma mulLeftCLM_apply (a b : E) : mulLeftCLM a b = a * b
```

**`ProbabilisticTheory.NormedJordanAlgebra.norm_quadRep_le`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean#L85).

> A uniform norm bound for the quadratic representation:
> `‖U_a b‖ ≤ 3 ‖a‖² ‖b‖`. The sharp constant is not needed for continuity.

```lean
lemma norm_quadRep_le (a b : E) : ‖U a b‖ ≤ 3 * ‖a‖ ^ 2 * ‖b‖
```

**`ProbabilisticTheory.NormedJordanAlgebra.quadRepCLM`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean#L104).

> The quadratic representation as a bounded linear operator.

```lean
noncomputable def quadRepCLM (a : E) : E →L[ℝ] E
```

**`ProbabilisticTheory.NormedJordanAlgebra.quadRepCLM_apply`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean#L108).

```lean
lemma quadRepCLM_apply (a b : E) : quadRepCLM a b = U a b
```

## C. The derivation corollary

**`ProbabilisticTheory.NormedJordanAlgebra.isDerivation_of_isAutomorphismFamily`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean#L113).

> **The generator of a differentiable family of Jordan automorphisms is a Jordan derivation.**

```lean
lemma isDerivation_of_isAutomorphismFamily {α : ℝ → E → E}
    (hα0 : ∀ a, α 0 a = a) (hmul : ∀ t a b, α t (a * b) = α t a * α t b)
    {D : E →ₗ[ℝ] E} (hD : IsGenerator α D) : IsDerivation D
```

## Depends on

- [Derivations](../../algebra/derivation.md)
- [Generators of one-parameter groups](../../dynamics/generator.md)
- [Normed Jordan algebras and JB-algebras](jb-basic.md)
- [Powers, multiplication operators and the quadratic representation](operator.md)

## Proof depends on

- [Generators of automorphism groups are derivations](../../dynamics/generatorisderivation.md)

## Sources

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean)
