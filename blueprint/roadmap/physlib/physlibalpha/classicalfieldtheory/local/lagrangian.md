---
declaration: module
origin: cited
lean: ClassicalFieldTheory.Local.Lagrangian, ClassicalFieldTheory.Local.Lagrangian.fiberDerivative, ClassicalFieldTheory.Local.Lagrangian.hasDerivAt_lineMap, ClassicalFieldTheory.Local.Lagrangian.ContinuousInCoordinates, ClassicalFieldTheory.Local.Lagrangian.ContDiffCoordDerivInCoordinates, ClassicalFieldTheory.Local.Lagrangian.SmoothInCoordinates, ClassicalFieldTheory.Local.Lagrangian.ContDiffCoordDerivAlongField, ClassicalFieldTheory.Local.Lagrangian.ContinuousCoordDerivAlongFamily
statement: formalized
proof: formalized
---

# Local Lagrangians

The module `PhyslibAlpha.ClassicalFieldTheory.Local.Lagrangian`, [PhyslibAlpha/ClassicalFieldTheory/Local/Lagrangian.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Lagrangian.lean): 14 declarations (1 instance with no name), 8 with a docstring.

> Local finite-order Lagrangians on jet points, their regularity, and evaluation along fields.

## i. Overview

> This module defines local Lagrangians of finite order for fields on `Space d` with values in
> `EuclideanSpace ℝ (Fin m)`.
>
> In the first local stage of the Classical Field Theory development, a local `k`-th order
> Lagrangian is treated as a function on `JetPoint d m k`. This matches the local book-level picture
> `L : Jet^k(Ω, R^m) → R` while postponing any stronger smoothness packaging until the ambient
> structure on local jet-point data has been made explicit enough to support it naturally.

## ii. Key results

> - `ClassicalFieldTheory.Local.Lagrangian` : local `k`-th order Lagrangians.
> - `ClassicalFieldTheory.Local.Lagrangian.coordDeriv` : coordinate derivatives with respect to the
>   jet coordinates `u^a_I`.
> - `ClassicalFieldTheory.Local.Lagrangian.SmoothInCoordinates` : the combined public regularity
>   package for smooth local lagrangians in explicit jet coordinates.
> - `ClassicalFieldTheory.Local.Lagrangian.alongField` : evaluate a local Lagrangian along the jets
>   of a field.

## iv. References

> * J. Cortés and A. Haupt, Lecture Notes on Mathematical Methods of Classical Physics, Chapter 5.
>   [ref: cortes\_haupt\_2016]

## A. Local Lagrangians

**`ClassicalFieldTheory.Local.Lagrangian`**, a structure, [line 61](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Lagrangian.lean#L61).

> A local `k`-th order Lagrangian for fields `Space d → EuclideanSpace ℝ (Fin m)`.

```lean
structure Lagrangian (d m k : ℕ) where
  /-- The underlying jet-dependent function. -/
  toFun : JetPoint d m k → ℝ
  /-- The derivatives of the Lagrangian with respect to the jet coordinates `u^a_I`. -/
  coordDeriv : DerivativeIndex d k → Fin m → JetPoint d m k → ℝ
  /-- The first derivative of the Lagrangian along affine lines in the jet-fiber coordinates is
  given by the pairing with the coordinate derivatives. -/
  hasDerivAlongFiber :
    ∀ J : JetPoint d m k, ∀ V : JetFiberData d m k,
      HasDerivAt (fun s : ℝ => toFun (J.lineMap V s))
        (∑ I : DerivativeIndex d k, ∑ a : Fin m, coordDeriv I a J * V.coord I a) 0
```

**An instance with no name**, [line 77](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Lagrangian.lean#L77).

```lean
instance : CoeFun (Lagrangian d m k) (fun _ => JetPoint d m k → ℝ)
```

**`ClassicalFieldTheory.Local.Lagrangian.fiberDerivative`**, a def, [line 81](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Lagrangian.lean#L81).

> The derivative of `L` along the fiber-jet direction `V` based at `J`.

```lean
noncomputable def fiberDerivative (L : Lagrangian d m k) (J : JetPoint d m k)
    (V : JetFiberData d m k) : ℝ
```

**`ClassicalFieldTheory.Local.Lagrangian.hasDerivAt_lineMap`**, a lemma, [line 85](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Lagrangian.lean#L85).

```lean
lemma hasDerivAt_lineMap (L : Lagrangian d m k) (J : JetPoint d m k) (V : JetFiberData d m k) :
    HasDerivAt (fun s : ℝ => L (J.lineMap V s)) (L.fiberDerivative J V) 0
```

## B. Regularity packages

**`ClassicalFieldTheory.Local.Lagrangian.ContinuousInCoordinates`**, a def, [line 95](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Lagrangian.lean#L95).

> Continuity of a local lagrangian in the explicit local jet coordinates `(x, u^a_I)`.

```lean
def ContinuousInCoordinates (L : Lagrangian d m k) : Prop
```

**`ClassicalFieldTheory.Local.Lagrangian.ContDiffCoordDerivInCoordinates`**, a def, [line 101](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Lagrangian.lean#L101).

> Intrinsic smoothness of the jet-coordinate derivatives of a local Lagrangian in the explicit
> local jet coordinates `(x, u^a_I)`.

```lean
def ContDiffCoordDerivInCoordinates (L : Lagrangian d m k) : Prop
```

**`ClassicalFieldTheory.Local.Lagrangian.SmoothInCoordinates`**, a def, [line 109](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Lagrangian.lean#L109).

> Public regularity package for a smooth local lagrangian in explicit local jet coordinates:
> continuity of the lagrangian itself together with smoothness of all jet-coordinate derivatives.

```lean
def SmoothInCoordinates (L : Lagrangian d m k) : Prop
```

**`ClassicalFieldTheory.Local.Lagrangian.ContDiffCoordDerivAlongField`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Lagrangian.lean#L113).

> Smoothness of all coefficient functions `x ↦ ∂L/∂u_I^a (j^k f(x))` along a field `f`.

```lean
def ContDiffCoordDerivAlongField (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m)) : Prop
```

**`ClassicalFieldTheory.Local.Lagrangian.ContinuousCoordDerivAlongFamily`**, a def, [line 120](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Lagrangian.lean#L120).

> Continuity of the coefficient family `(s, x) ↦ ∂L/∂u_I^a (j^k(F s)(x))` along a
> one-parameter family of fields `F : ℝ → Space d → EuclideanSpace ℝ (Fin m)`.

```lean
def ContinuousCoordDerivAlongFamily (L : Lagrangian d m k)
    (F : ℝ → Space d → EuclideanSpace ℝ (Fin m)) : Prop
```

**`ClassicalFieldTheory.Local.Lagrangian.continuousAlongField_of_inCoordinates`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Lagrangian.lean#L125).

```lean
lemma continuousAlongField_of_inCoordinates (L : Lagrangian d m k)
    (hcont : ContinuousInCoordinates L) (f : Space d → EuclideanSpace ℝ (Fin m))
    (hf : ContDiff ℝ ∞ f) :
    Continuous (fun x : Space d => L (jetAt k f x))
```

**`ClassicalFieldTheory.Local.Lagrangian.contDiffCoordDerivAlongField_of_inCoordinates`**, a lemma, [line 132](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Lagrangian.lean#L132).

```lean
lemma contDiffCoordDerivAlongField_of_inCoordinates (L : Lagrangian d m k)
    (hcoord : ContDiffCoordDerivInCoordinates L) (f : Space d → EuclideanSpace ℝ (Fin m))
    (hf : ContDiff ℝ ∞ f) :
    ContDiffCoordDerivAlongField L f
```

**`ClassicalFieldTheory.Local.Lagrangian.continuousCoordDerivAlongFamily_of_inCoordinates`**, a lemma, [line 143](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Lagrangian.lean#L143).

```lean
lemma continuousCoordDerivAlongFamily_of_inCoordinates (L : Lagrangian d m k)
    (hcoord : ContDiffCoordDerivInCoordinates L)
    (F : ℝ → Space d → EuclideanSpace ℝ (Fin m))
    (hjet : Continuous (fun p : ℝ × Space d => (p.2, jetCoordinatesAt k (F p.1) p.2))) :
    ContinuousCoordDerivAlongFamily L F
```

## C. Evaluation along a field

**`ClassicalFieldTheory.Local.Lagrangian.alongField`**, a def, [line 162](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Lagrangian.lean#L162).

> Evaluate a local Lagrangian along the `k`-jets of a field.

```lean
noncomputable def alongField (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m)) : Space d → ℝ
```

**`ClassicalFieldTheory.Local.Lagrangian.alongField_apply`**, a lemma, [line 167](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Lagrangian.lean#L167).

```lean
lemma alongField_apply (L : Lagrangian d m k)
    (f : Space d → EuclideanSpace ℝ (Fin m)) (x : Space d) :
    L.alongField f x = L (jetAt k f x)
```

## Depends on

- [Fiber directions on jet points](jetpointfiber.md)
- [Total derivatives on local jet-dependent functions](totalderivative.md)

## Proof depends on

- [Regularity and support for jet-coordinate maps](jetpointregularity.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/Local/Lagrangian.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/Lagrangian.lean)
