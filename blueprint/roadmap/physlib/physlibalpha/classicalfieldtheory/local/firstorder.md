---
declaration: module
origin: cited
lean: ClassicalFieldTheory.Local.FirstOrderJetCoordinates, ClassicalFieldTheory.Local.FirstOrderJetPoint, ClassicalFieldTheory.Local.FirstOrderJetFiberData, ClassicalFieldTheory.Local.FirstOrderLagrangian, ClassicalFieldTheory.Local.firstDerivativeIndex, ClassicalFieldTheory.Local.firstDerivativeIndex_coe, ClassicalFieldTheory.Local.firstDerivativeIndex_order, ClassicalFieldTheory.Local.JetPoint.firstDerivCoord
statement: formalized
proof: formalized
---

# First-order local field theory

The module `PhyslibAlpha.ClassicalFieldTheory.Local.FirstOrder`, [PhyslibAlpha/ClassicalFieldTheory/Local/FirstOrder.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstOrder.lean): 19 declarations, 11 with a docstring.

> Aliases and projections specializing the local field theory API to first-order jets.

## i. Overview

> This module provides a thin usability layer for first-order local field theory, i.e. the
> specialization of the local CFT stack to `k = 1`.
>
> The definitions here do not introduce a new theory. They are aliases and projections for the
> existing coordinate-readout stack:
>
> - first-order jet points are `JetPoint d m 1`,
> - first-order lagrangians are `Lagrangian d m 1`,
> - field values are still the zero-order jet coordinates,
> - first derivatives are the coordinates indexed by `MultiIndex.increment 0 i`.
>
> This keeps the general finite-order API as the source of truth while making the common first-order
> case easier to state in examples and later mechanics bridges.

## ii. Key results

> - `ClassicalFieldTheory.Local.FirstOrderJetPoint`
> - `ClassicalFieldTheory.Local.FirstOrderLagrangian`
> - `ClassicalFieldTheory.Local.firstDerivativeIndex`
> - `ClassicalFieldTheory.Local.JetPoint.firstDerivCoord`
> - `ClassicalFieldTheory.Local.firstOrderJetAt`

## iv. References

> * J. Cortés and A. Haupt, Lecture Notes on Mathematical Methods of Classical Physics,
>   arXiv:1612.03100v2, Chapter 5. [ref: cortes\_haupt\_2016]

## A. First-order aliases

**`ClassicalFieldTheory.Local.FirstOrderJetCoordinates`**, an abbrev, [line 64](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstOrder.lean#L64).

> Coordinate data for first-order local jet points.

```lean
abbrev FirstOrderJetCoordinates (d m : ℕ)
```

**`ClassicalFieldTheory.Local.FirstOrderJetPoint`**, an abbrev, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstOrder.lean#L67).

> Coordinate-level first-order jet points.

```lean
abbrev FirstOrderJetPoint (d m : ℕ)
```

**`ClassicalFieldTheory.Local.FirstOrderJetFiberData`**, an abbrev, [line 70](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstOrder.lean#L70).

> Fiber-direction data for first-order jet points.

```lean
abbrev FirstOrderJetFiberData (d m : ℕ)
```

**`ClassicalFieldTheory.Local.FirstOrderLagrangian`**, an abbrev, [line 73](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstOrder.lean#L73).

> First-order local lagrangians.

```lean
abbrev FirstOrderLagrangian (d m : ℕ)
```

## B. First derivative indices

**`ClassicalFieldTheory.Local.firstDerivativeIndex`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstOrder.lean#L81).

> The first-derivative coordinate index in the source direction `i`.

```lean
def firstDerivativeIndex (d : ℕ) (i : Fin d) : DerivativeIndex d 1
```

**`ClassicalFieldTheory.Local.firstDerivativeIndex_coe`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstOrder.lean#L85).

```lean
lemma firstDerivativeIndex_coe (d : ℕ) (i : Fin d) :
    ((firstDerivativeIndex d i : DerivativeIndex d 1) : MultiIndex d) =
      Physlib.MultiIndex.increment 0 i
```

**`ClassicalFieldTheory.Local.firstDerivativeIndex_order`**, a lemma, [line 89](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstOrder.lean#L89).

```lean
lemma firstDerivativeIndex_order (d : ℕ) (i : Fin d) :
    ((firstDerivativeIndex d i : DerivativeIndex d 1) : MultiIndex d).order = 1
```

## C. First-order jet projections

**`ClassicalFieldTheory.Local.JetPoint.firstDerivCoord`**, a def, [line 103](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstOrder.lean#L103).

> The first derivative coordinate `u^a_i` of a first-order jet point.

```lean
def firstDerivCoord (J : FirstOrderJetPoint d m) (i : Fin d) (a : Fin m) : ℝ
```

**`ClassicalFieldTheory.Local.JetPoint.firstDerivVector`**, a def, [line 107](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstOrder.lean#L107).

> The bundled target vector of first derivative coordinates in the source direction `i`.

```lean
def firstDerivVector (J : FirstOrderJetPoint d m) (i : Fin d) : EuclideanSpace ℝ (Fin m)
```

**`ClassicalFieldTheory.Local.JetPoint.firstDerivVector_apply`**, a lemma, [line 111](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstOrder.lean#L111).

```lean
lemma firstDerivVector_apply (J : FirstOrderJetPoint d m) (i : Fin d) (a : Fin m) :
    J.firstDerivVector i a = J.firstDerivCoord i a
```

**`ClassicalFieldTheory.Local.JetPoint.firstDerivCoord_ofBaseCoordinates`**, a lemma, [line 116](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstOrder.lean#L116).

```lean
lemma firstDerivCoord_ofBaseCoordinates (x : Space d) (u : FirstOrderJetCoordinates d m)
    (i : Fin d) (a : Fin m) :
    (JetPoint.ofBaseCoordinates x u).firstDerivCoord i a = u (firstDerivativeIndex d i) a
```

## D. First-order evaluation and variational API

**`ClassicalFieldTheory.Local.firstOrderJetAt`**, an abbrev, [line 128](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstOrder.lean#L128).

> The first-order coordinate-level jet point of a field at a point.

```lean
noncomputable abbrev firstOrderJetAt (f : Space d → EuclideanSpace ℝ (Fin m)) (x : Space d) :
    FirstOrderJetPoint d m
```

**`ClassicalFieldTheory.Local.firstOrderJetAt_base`**, a lemma, [line 133](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstOrder.lean#L133).

```lean
lemma firstOrderJetAt_base (f : Space d → EuclideanSpace ℝ (Fin m)) (x : Space d) :
    (firstOrderJetAt f x).base = x
```

**`ClassicalFieldTheory.Local.firstOrderJetAt_value`**, a lemma, [line 136](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstOrder.lean#L136).

```lean
lemma firstOrderJetAt_value (f : Space d → EuclideanSpace ℝ (Fin m)) (x : Space d) :
    (firstOrderJetAt f x).value = f x
```

**`ClassicalFieldTheory.Local.firstOrderJetAt_firstDerivCoord`**, a lemma, [line 141](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstOrder.lean#L141).

```lean
lemma firstOrderJetAt_firstDerivCoord (f : Space d → EuclideanSpace ℝ (Fin m))
    (x : Space d) (i : Fin d) (a : Fin m) :
    (firstOrderJetAt f x).firstDerivCoord i a =
      ∂^[Physlib.MultiIndex.increment 0 i] (fun y => (f y) a) x
```

**`ClassicalFieldTheory.Local.firstOrderActionDensity`**, an abbrev, [line 147](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstOrder.lean#L147).

> Evaluate a first-order local lagrangian along the first jets of a field.

```lean
noncomputable abbrev firstOrderActionDensity (L : FirstOrderLagrangian d m)
    (f : Space d → EuclideanSpace ℝ (Fin m)) : Space d → ℝ
```

**`ClassicalFieldTheory.Local.firstOrderAction`**, an abbrev, [line 152](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstOrder.lean#L152).

> The action of a first-order local lagrangian.

```lean
noncomputable abbrev firstOrderAction (L : FirstOrderLagrangian d m)
    (f : Space d → EuclideanSpace ℝ (Fin m)) : ℝ
```

**`ClassicalFieldTheory.Local.firstOrderEulerLagrangeOp`**, an abbrev, [line 157](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstOrder.lean#L157).

> The Euler-Lagrange operator of a first-order local lagrangian.

```lean
noncomputable abbrev firstOrderEulerLagrangeOp (L : FirstOrderLagrangian d m)
    (f : Space d → EuclideanSpace ℝ (Fin m)) : Space d → EuclideanSpace ℝ (Fin m)
```

**`ClassicalFieldTheory.Local.firstOrder_isCritical_iff_eulerLagrange_zero`**, a lemma, [line 161](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstOrder.lean#L161).

```lean
lemma firstOrder_isCritical_iff_eulerLagrange_zero
    (L : FirstOrderLagrangian d m) (f : Space d → EuclideanSpace ℝ (Fin m))
    (hLf : IsAdmissibleForAction L f)
    (hL : Lagrangian.SmoothInCoordinates L) :
    IsCritical L f ↔ firstOrderEulerLagrangeOp L f = 0
```

## Depends on

- [Local action functionals](action.md)
- [Local Euler-Lagrange operators](eulerlagrange.md)

## Proof depends on

- [First variation and the Euler-Lagrange criterion](firstvariation.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/Local/FirstOrder.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/FirstOrder.lean)
