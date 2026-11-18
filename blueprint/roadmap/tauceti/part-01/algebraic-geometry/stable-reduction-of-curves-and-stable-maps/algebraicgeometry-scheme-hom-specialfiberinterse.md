---
declaration: def
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.specialFiberIntersectionMatrix
statement: formalized
---

# AlgebraicGeometry.Scheme.Hom.specialFiberIntersectionMatrix

The **intersection matrix** of the special fibre of a regular model. Let `X` be a regular
Noetherian integral scheme over a local ring `R` of dimension at most one, with all points of
codimension at most two and generic point away from the closed point. Its entry at a pair of
components `Cᵢ`, `Cⱼ` of the special fibre is the intersection number
`(Cⱼ · Cᵢ) = deg 𝒪_X(Cⱼ)|_{Cᵢ}` over the residue field of `R`, where `Cᵢ` carries its reduced
structure and its structure over the residue field through the special fibre.

```lean
AlgebraicGeometry.Scheme.Hom.specialFiberIntersectionMatrix.{u} {R : Type u} [CommRing R]
  [IsLocalRing R] [Ring.DimensionLEOne R] {X : AlgebraicGeometry.Scheme}
  (toBase : X ⟶ AlgebraicGeometry.Spec ↧R) [AlgebraicGeometry.IsIntegral X]
  [AlgebraicGeometry.IsNoetherian X] [TauCeti.AlgebraicGeometry.IsRegular X]
  (hX : ∀ (x : ↥X), Order.coheight x ≤ 2)
  (hη : toBase (genericPoint ↥X) ≠ IsLocalRing.closedPoint R) : Matrix ↥⋯.toFinset ↥⋯.toFinset ℤ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.Hom.specialFiberIntersectionMatrix`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/IntersectionNumber/Matrix.html#AlgebraicGeometry.Scheme.Hom.specialFiberIntersectionMatrix).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.Hom.specialFiberIntersectionMatrix`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/IntersectionNumber/Matrix.html#AlgebraicGeometry.Scheme.Hom.specialFiberIntersectionMatrix)
- [Source of `AlgebraicGeometry.Scheme.Hom.specialFiberIntersectionMatrix` in TauCeti/AlgebraicGeometry/IntersectionNumber/Matrix.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/IntersectionNumber/Matrix.lean#L107)
- [Tau Ceti roadmap status: Stable reduction of curves and stable maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/StableReduction/STATUS.md)
