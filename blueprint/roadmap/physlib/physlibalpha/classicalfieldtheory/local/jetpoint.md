---
declaration: module
origin: cited
lean: ClassicalFieldTheory.Local.JetCoordinates, ClassicalFieldTheory.Local.JetPoint, ClassicalFieldTheory.Local.JetPoint.coord, ClassicalFieldTheory.Local.JetPoint.value, ClassicalFieldTheory.Local.JetPoint.value_apply, ClassicalFieldTheory.Local.JetPoint.ext, ClassicalFieldTheory.Local.JetPoint.ofBaseCoordinates, ClassicalFieldTheory.Local.JetPoint.toBaseCoordinates
statement: formalized
proof: formalized
---

# Coordinate-level jet points

The module `PhyslibAlpha.ClassicalFieldTheory.Local.JetPoint`, [PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean): 22 declarations, 8 with a docstring.

> Coordinate-level jet points of fields on `Space d` and the jets of a field at a point.

## i. Overview

> This module introduces the coordinate-level point of the locally trivialized `k`-jet bundle for
> fields on `Space d` with values in `EuclideanSpace ℝ (Fin m)`.
>
> This module only formalizes the local coordinate model `Jet^k(Ω, ℝ^m) ≃ Ω × V`; it does not
> attempt to define global jet bundles.
>
> At this core stage, a jet point is represented by:
>
> - its base point in `Space d`,
> - and its jet coordinates indexed by derivative indices of order at most `k`.
>
> In particular, the zero-th order field value is not stored separately: it is the zero derivative
> coordinate.

## ii. Key results

> - `ClassicalFieldTheory.Local.JetCoordinates`
> - `ClassicalFieldTheory.Local.JetPoint`
> - `ClassicalFieldTheory.Local.jetCoordinatesAt`
> - `ClassicalFieldTheory.Local.jetAt`

## iv. References

> * J. Cortés and A. Haupt, Lecture Notes on Mathematical Methods of Classical Physics,
>   arXiv:1612.03100v2, Chapter 5, Section 5.1. [ref: cortes\_haupt\_2016]

## A. Jet coordinates

**`ClassicalFieldTheory.Local.JetCoordinates`**, an abbrev, [line 67](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean#L67).

> Coordinate data `u^a_I` for `k`-th order jet points.
>
> For each derivative index `I`, these are the scalar components of the corresponding
> `EuclideanSpace ℝ (Fin m)` fiber coordinate. We keep this componentwise form because the
> local Euler-Lagrange formulas are indexed by both `I` and `a`.

```lean
abbrev JetCoordinates (d m k : ℕ)
```

## B. Jet points

**`ClassicalFieldTheory.Local.JetPoint`**, a structure, [line 76](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean#L76).

> The coordinate-level points of the locally trivialized `k`-jet bundle for fields
> `Space d → EuclideanSpace ℝ (Fin m)`.

```lean
structure JetPoint (d m k : ℕ) where
  /-- The base point of the jet point. -/
  base : Space d
  /-- The jet coordinates indexed by all derivative indices of order at most `k`. -/
  fiber : JetCoordinates d m k
```

**`ClassicalFieldTheory.Local.JetPoint.coord`**, a def, [line 87](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean#L87).

> The coordinate `u^a_I` of a jet point.

```lean
def coord (J : JetPoint d m k) (I : DerivativeIndex d k) (a : Fin m) : ℝ
```

**`ClassicalFieldTheory.Local.JetPoint.value`**, a def, [line 90](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean#L90).

> The zero-th order value encoded by a jet point.

```lean
def value (J : JetPoint d m k) : EuclideanSpace ℝ (Fin m)
```

**`ClassicalFieldTheory.Local.JetPoint.value_apply`**, a lemma, [line 94](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean#L94).

```lean
lemma value_apply (J : JetPoint d m k) (a : Fin m) :
    J.value a = J.coord 0 a
```

**`ClassicalFieldTheory.Local.JetPoint.ext`**, a lemma, [line 99](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean#L99).

```lean
lemma ext (J K : JetPoint d m k) (hbase : J.base = K.base)
    (hcoord : ∀ I a, J.coord I a = K.coord I a) :
    J = K
```

**`ClassicalFieldTheory.Local.JetPoint.ofBaseCoordinates`**, a def, [line 113](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean#L113).

> Build a jet point from a base point and its jet coordinates.

```lean
def ofBaseCoordinates (x : Space d) (u : JetCoordinates d m k) : JetPoint d m k
```

**`ClassicalFieldTheory.Local.JetPoint.toBaseCoordinates`**, a def, [line 118](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean#L118).

> The base point and jet coordinates of a jet point.

```lean
def toBaseCoordinates (J : JetPoint d m k) : Space d × JetCoordinates d m k
```

**`ClassicalFieldTheory.Local.JetPoint.ofBaseCoordinates_base`**, a lemma, [line 121](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean#L121).

```lean
lemma ofBaseCoordinates_base (x : Space d) (u : JetCoordinates d m k) :
    (ofBaseCoordinates x u).base = x
```

**`ClassicalFieldTheory.Local.JetPoint.ofBaseCoordinates_fiber`**, a lemma, [line 125](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean#L125).

```lean
lemma ofBaseCoordinates_fiber (x : Space d) (u : JetCoordinates d m k) :
    (ofBaseCoordinates x u).fiber = u
```

**`ClassicalFieldTheory.Local.JetPoint.ofBaseCoordinates_coord`**, a lemma, [line 129](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean#L129).

```lean
lemma ofBaseCoordinates_coord (x : Space d) (u : JetCoordinates d m k)
    (I : DerivativeIndex d k) (a : Fin m) :
    (ofBaseCoordinates x u).coord I a = u I a
```

**`ClassicalFieldTheory.Local.JetPoint.ofBaseCoordinates_base_fiber`**, a lemma, [line 134](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean#L134).

```lean
lemma ofBaseCoordinates_base_fiber (J : JetPoint d m k) :
    ofBaseCoordinates J.base J.fiber = J
```

**`ClassicalFieldTheory.Local.JetPoint.toBaseCoordinates_ofBaseCoordinates`**, a lemma, [line 142](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean#L142).

```lean
lemma toBaseCoordinates_ofBaseCoordinates (x : Space d) (u : JetCoordinates d m k) :
    (ofBaseCoordinates x u).toBaseCoordinates = (x, u)
```

## C. Jet points of fields

**`ClassicalFieldTheory.Local.jetCoordinatesAt`**, a def, [line 153](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean#L153).

> The jet-coordinate function determined by a field `g`.

```lean
noncomputable def jetCoordinatesAt (k : ℕ) (g : Space d → EuclideanSpace ℝ (Fin m))
    (x : Space d) :
    JetCoordinates d m k
```

**`ClassicalFieldTheory.Local.jetAt`**, a def, [line 159](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean#L159).

> The coordinate-level `k`-jet point of a field `f` at the point `x`.

```lean
noncomputable def jetAt (k : ℕ) (f : Space d → EuclideanSpace ℝ (Fin m)) (x : Space d) :
    JetPoint d m k
```

**`ClassicalFieldTheory.Local.jetAt_base`**, a lemma, [line 165](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean#L165).

```lean
lemma jetAt_base (k : ℕ) (f : Space d → EuclideanSpace ℝ (Fin m)) (x : Space d) :
    (jetAt k f x).base = x
```

**`ClassicalFieldTheory.Local.jetAt_value`**, a lemma, [line 169](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean#L169).

```lean
lemma jetAt_value (k : ℕ) (f : Space d → EuclideanSpace ℝ (Fin m)) (x : Space d) :
    (jetAt k f x).value = f x
```

**`ClassicalFieldTheory.Local.jetAt_coord`**, a lemma, [line 175](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean#L175).

```lean
lemma jetAt_coord (k : ℕ) (f : Space d → EuclideanSpace ℝ (Fin m)) (x : Space d)
    (I : DerivativeIndex d k) (a : Fin m) :
    (jetAt k f x).coord I a = ∂^[I.1] (fun y => (f y) a) x
```

**`ClassicalFieldTheory.Local.jetAt_coord_zero`**, a lemma, [line 179](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean#L179).

```lean
lemma jetAt_coord_zero (k : ℕ) (f : Space d → EuclideanSpace ℝ (Fin m)) (x : Space d)
    (a : Fin m) :
    (jetAt k f x).coord 0 a = (f x) a
```

**`ClassicalFieldTheory.Local.jetCoordinatesAt_eq`**, a lemma, [line 185](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean#L185).

```lean
lemma jetCoordinatesAt_eq (k : ℕ) (g : Space d → EuclideanSpace ℝ (Fin m)) (x : Space d)
    (I : DerivativeIndex d k) (a : Fin m) :
    jetCoordinatesAt k g x I a = ∂^[I.1] (fun y => (g y) a) x
```

**`ClassicalFieldTheory.Local.jetCoordinatesAt_zero`**, a lemma, [line 189](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean#L189).

```lean
lemma jetCoordinatesAt_zero (k : ℕ) (g : Space d → EuclideanSpace ℝ (Fin m))
    (x : Space d) (a : Fin m) :
    jetCoordinatesAt k g x 0 a = (g x) a
```

**`ClassicalFieldTheory.Local.jetAt_eq_ofBaseCoordinates`**, a lemma, [line 194](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean#L194).

```lean
lemma jetAt_eq_ofBaseCoordinates (k : ℕ) (f : Space d → EuclideanSpace ℝ (Fin m))
    (x : Space d) :
    jetAt k f x = JetPoint.ofBaseCoordinates x (jetCoordinatesAt k f x)
```

## Depends on

- [Bounded derivative indices](../../../physlib/spaceandtime/space/part-01/derivatives-derivativeindex.md)
- [Iterated derivatives on `Space d`](../../../physlib/spaceandtime/space/part-01/derivatives-iterated.md)

## Sources

- [PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean at 2a1dfe43](https://github.com/leanprover-community/physlib/blob/2a1dfe43134b49b643642f13d33031754021bb5d/PhyslibAlpha/ClassicalFieldTheory/Local/JetPoint.lean)
