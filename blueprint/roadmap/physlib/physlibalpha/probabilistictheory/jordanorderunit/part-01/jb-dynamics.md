---
declaration: module
origin: cited
lean: PhyslibAlpha.ProbabilisticTheory.NormedJordanAlgebra.isBoundedBilinearMap_mul, PhyslibAlpha.ProbabilisticTheory.NormedJordanAlgebra.continuous_mul_left, PhyslibAlpha.ProbabilisticTheory.NormedJordanAlgebra.continuous_mul_right, PhyslibAlpha.ProbabilisticTheory.NormedJordanAlgebra.mulLeftCLM, PhyslibAlpha.ProbabilisticTheory.NormedJordanAlgebra.mulLeftCLM_apply, PhyslibAlpha.ProbabilisticTheory.NormedJordanAlgebra.norm_quadRep_le, PhyslibAlpha.ProbabilisticTheory.NormedJordanAlgebra.quadRepCLM, PhyslibAlpha.ProbabilisticTheory.NormedJordanAlgebra.quadRepCLM_apply
statement: formalized
proof: formalized
---

# Generators of JB automorphism groups

The module `PhyslibAlpha.ProbabilisticTheory.JordanOrderUnit.JB.Dynamics`, [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean): 9 declarations, 7 with a docstring.

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

**`PhyslibAlpha.ProbabilisticTheory.NormedJordanAlgebra.isBoundedBilinearMap_mul`**, a lemma, [line 55](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean#L55).

> The Jordan product of a normed Jordan algebra is bounded bilinear, with bound constant `1`.

```lean
lemma isBoundedBilinearMap_mul :
    IsBoundedBilinearMap ℝ (fun p : E × E => p.1 * p.2)
```

**`PhyslibAlpha.ProbabilisticTheory.NormedJordanAlgebra.continuous_mul_left`**, a lemma, [line 64](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean#L64).

> Left Jordan multiplication by a fixed element is continuous.

```lean
lemma continuous_mul_left (a : E) : Continuous fun x : E => a * x
```

**`PhyslibAlpha.ProbabilisticTheory.NormedJordanAlgebra.continuous_mul_right`**, a lemma, [line 68](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean#L68).

> Right Jordan multiplication by a fixed element is continuous.

```lean
lemma continuous_mul_right (a : E) : Continuous fun x : E => x * a
```

## B. Continuous multiplication and quadratic operators

**`PhyslibAlpha.ProbabilisticTheory.NormedJordanAlgebra.mulLeftCLM`**, a def, [line 77](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean#L77).

> Left Jordan multiplication as a bounded linear operator, with operator bound `‖a‖`.

```lean
noncomputable def mulLeftCLM (a : E) : E →L[ℝ] E
```

**`PhyslibAlpha.ProbabilisticTheory.NormedJordanAlgebra.mulLeftCLM_apply`**, a lemma, [line 81](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean#L81).

```lean
lemma mulLeftCLM_apply (a b : E) : mulLeftCLM a b = a * b
```

**`PhyslibAlpha.ProbabilisticTheory.NormedJordanAlgebra.norm_quadRep_le`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean#L85).

> A uniform norm bound for the quadratic representation:
> `‖U_a b‖ ≤ 3 ‖a‖² ‖b‖`. The sharp constant is not needed for continuity.

```lean
lemma norm_quadRep_le (a b : E) : ‖U a b‖ ≤ 3 * ‖a‖ ^ 2 * ‖b‖
```

**`PhyslibAlpha.ProbabilisticTheory.NormedJordanAlgebra.quadRepCLM`**, a def, [line 104](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean#L104).

> The quadratic representation as a bounded linear operator.

```lean
noncomputable def quadRepCLM (a : E) : E →L[ℝ] E
```

**`PhyslibAlpha.ProbabilisticTheory.NormedJordanAlgebra.quadRepCLM_apply`**, a lemma, [line 108](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean#L108).

```lean
lemma quadRepCLM_apply (a b : E) : quadRepCLM a b = U a b
```

## C. The derivation corollary

**`PhyslibAlpha.ProbabilisticTheory.NormedJordanAlgebra.isDerivation_of_isAutomorphismFamily`**, a lemma, [line 113](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean#L113).

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

- [PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean at 8c87bdfb](https://github.com/leanprover-community/physlib/blob/8c87bdfb015de47e82da811567aaa7a2a05353f4/PhyslibAlpha/ProbabilisticTheory/JordanOrderUnit/JB/Dynamics.lean)
