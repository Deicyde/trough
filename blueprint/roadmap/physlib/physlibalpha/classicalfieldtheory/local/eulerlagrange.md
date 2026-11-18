---
declaration: module
origin: cited
lean: ClassicalFieldTheory.Local.eulerLagrangeTerm, ClassicalFieldTheory.Local.eulerLagrangeTerm_apply, ClassicalFieldTheory.Local.eulerLagrangeComponent, ClassicalFieldTheory.Local.eulerLagrangeComponent_apply, ClassicalFieldTheory.Local.eulerLagrangeOp, ClassicalFieldTheory.Local.eulerLagrangeOp_apply, ClassicalFieldTheory.Local.eulerLagrangeOp_eq
statement: formalized
proof: formalized
---

# Local Euler-Lagrange operators

The module `PhyslibAlpha.ClassicalFieldTheory.Local.EulerLagrange`, [PhyslibAlpha/ClassicalFieldTheory/Local/EulerLagrange.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/EulerLagrange.lean): 7 declarations, 3 with a docstring.

> The local Euler-Lagrange operator of a local Lagrangian, built componentwise.

## i. Overview

> This module defines the local Euler-Lagrange operator associated with a local Lagrangian.
>
> In the first implementation pass, the derivatives of the Lagrangian with respect to the jet
> coordinates are packaged explicitly as part of the local Lagrangian data. This keeps the formula
> close to the one in the book while avoiding a premature smooth structure on `JetPoint`.

## ii. Key results

> - `ClassicalFieldTheory.Local.eulerLagrangeTerm` : a single summand in the local
>   Euler-Lagrange formula.
> - `ClassicalFieldTheory.Local.eulerLagrangeComponent` : one component `E_a(L)` of the operator.
> - `ClassicalFieldTheory.Local.eulerLagrangeOp` : the full local Euler-Lagrange operator.

## iv. References

> * J. Cortés and A. Haupt, Lecture Notes on Mathematical Methods of Classical Physics, Chapter 5.
>   [ref: cortes\_haupt\_2016]

## A. Euler-Lagrange summands

**`ClassicalFieldTheory.Local.eulerLagrangeTerm`**, a def, [line 55](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/EulerLagrange.lean#L55).

> The summand `(-1)^|I| D_I (∂L/∂u^a_I)` in the local Euler-Lagrange formula.

```lean
noncomputable def eulerLagrangeTerm (L : Lagrangian d m k) (I : DerivativeIndex d k) (a : Fin m)
    (f : Space d → EuclideanSpace ℝ (Fin m)) : Space d → ℝ
```

**`ClassicalFieldTheory.Local.eulerLagrangeTerm_apply`**, a lemma, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/EulerLagrange.lean#L61).

```lean
lemma eulerLagrangeTerm_apply (L : Lagrangian d m k) (I : DerivativeIndex d k) (a : Fin m)
    (f : Space d → EuclideanSpace ℝ (Fin m)) (x : Space d) :
    eulerLagrangeTerm L I a f x =
      (-1 : ℝ) ^ I.1.order * iteratedTotalDerivative k I.1 (L.coordDeriv I a) f x
```

## B. Components of the Euler-Lagrange operator

**`ClassicalFieldTheory.Local.eulerLagrangeComponent`**, a def, [line 72](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/EulerLagrange.lean#L72).

> The `a`-th component of the local Euler-Lagrange operator.

```lean
noncomputable def eulerLagrangeComponent (L : Lagrangian d m k) (a : Fin m)
    (f : Space d → EuclideanSpace ℝ (Fin m)) : Space d → ℝ
```

**`ClassicalFieldTheory.Local.eulerLagrangeComponent_apply`**, a lemma, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/EulerLagrange.lean#L77).

```lean
lemma eulerLagrangeComponent_apply (L : Lagrangian d m k) (a : Fin m)
    (f : Space d → EuclideanSpace ℝ (Fin m)) (x : Space d) :
    eulerLagrangeComponent L a f x = ∑ I : DerivativeIndex d k, eulerLagrangeTerm L I a f x
```

## C. The full operator

**`ClassicalFieldTheory.Local.eulerLagrangeOp`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/EulerLagrange.lean#L87).

> The local Euler-Lagrange operator attached to a local Lagrangian.

```lean
noncomputable def eulerLagrangeOp (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m)) :
    Space d → EuclideanSpace ℝ (Fin m)
```

**`ClassicalFieldTheory.Local.eulerLagrangeOp_apply`**, a lemma, [line 91](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/EulerLagrange.lean#L91).

```lean
lemma eulerLagrangeOp_apply (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m))
    (x : Space d) (a : Fin m) :
    eulerLagrangeOp L f x a = eulerLagrangeComponent L a f x
```

**`ClassicalFieldTheory.Local.eulerLagrangeOp_eq`**, a lemma, [line 97](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/EulerLagrange.lean#L97).

```lean
lemma eulerLagrangeOp_eq (L : Lagrangian d m k) (f : Space d → EuclideanSpace ℝ (Fin m)) :
    eulerLagrangeOp L f = fun x => WithLp.toLp 2 fun a => eulerLagrangeComponent L a f x
```

## Depends on

- [Local Lagrangians](lagrangian.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/Local/EulerLagrange.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/EulerLagrange.lean)
