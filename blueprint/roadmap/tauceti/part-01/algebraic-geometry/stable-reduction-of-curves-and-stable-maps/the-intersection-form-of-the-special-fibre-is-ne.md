---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.Scheme.Hom.dotProduct_mulVec_specialFiberIntersectionMatrix_nonpos
statement: formalized
proof: formalized
---

# The intersection form of the special fibre is negative semidefinite

Under the hypotheses
of `AlgebraicGeometry.Scheme.Hom.specialFiberIntersectionMatrix_mulVec_specialFiberMultiplicity`,
the intersection matrix `A` of the special fibre satisfies `xᵀ A x ≤ 0` for every vector `x` over
a linearly ordered field ([Stacks, Tag 0C5X](https://stacks.math.columbia.edu/tag/0C5X)).

```lean
AlgebraicGeometry.Scheme.Hom.dotProduct_mulVec_specialFiberIntersectionMatrix_nonpos.{u, u_1}
  {R : Type u} [CommRing R] [IsLocalRing R] [Ring.DimensionLEOne R] {X : AlgebraicGeometry.Scheme}
  (toBase : X ⟶ AlgebraicGeometry.Spec ↧R) [AlgebraicGeometry.IsIntegral X]
  [AlgebraicGeometry.IsNoetherian X] [TauCeti.AlgebraicGeometry.IsRegular X]
  [AlgebraicGeometry.IsProper toBase] (hX : ∀ (x : ↥X), Order.coheight x ≤ 2)
  (hη : toBase (genericPoint ↥X) ≠ IsLocalRing.closedPoint R)
  (h₀ :
    ∀ (η : TauCeti.AlgebraicGeometry.CodimensionOnePoint X)
      (hc : toBase ↑η = IsLocalRing.closedPoint R),
      FiniteDimensional (IsLocalRing.ResidueField R)
        (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology
          (TauCeti.AlgebraicGeometry.InvertibleSheaf.trivial
              (AlgebraicGeometry.Scheme.IdealSheafData.vanishingIdeal
                  { carrier := closure {↑η}, isClosed' := ⋯ }).subscheme).obj
          0))
  (h₁ :
    ∀ (η : TauCeti.AlgebraicGeometry.CodimensionOnePoint X)
      (hc : toBase ↑η = IsLocalRing.closedPoint R),
      FiniteDimensional (IsLocalRing.ResidueField R)
        (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology
          (TauCeti.AlgebraicGeometry.InvertibleSheaf.trivial
              (AlgebraicGeometry.Scheme.IdealSheafData.vanishingIdeal
                  { carrier := closure {↑η}, isClosed' := ⋯ }).subscheme).obj
          1))
  [AlgebraicGeometry.Flat toBase] {π : R} (hπ : IsLocalRing.maximalIdeal R = Ideal.span {π})
  (hreg : IsSMulRegular R π) {K : Type u_1} [Field K] [LinearOrder K] [IsStrictOrderedRing K]
  (x : ↥⋯.toFinset → K) :
  x ⬝ᵥ
      ((AlgebraicGeometry.Scheme.Hom.specialFiberIntersectionMatrix toBase hX hη).map
            Int.cast).mulVec
        x ≤
    0
```

## Depends on

- [AlgebraicGeometry.Scheme.Hom.specialFiberIntersectionMatrix](algebraicgeometry-scheme-hom-specialfiberinterse.md)

## Proof depends on

- [The global dimension of a regular local ring is its Krull dimension](../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [Serre's vanishing theorem on affine opens](../other-results/serres-vanishing-theorem-on-affine-opens.md)
- [TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf](../algebraic-vector-bundles/tauceti-algebraicgeometry-finitelocallyfreesheaf-2.md)
- [TauCeti.globalDimension](../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.Hom.dotProduct_mulVec_specialFiberIntersectionMatrix_nonpos`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/IntersectionNumber/Matrix.html#AlgebraicGeometry.Scheme.Hom.dotProduct_mulVec_specialFiberIntersectionMatrix_nonpos).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.Hom.dotProduct_mulVec_specialFiberIntersectionMatrix_nonpos`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/IntersectionNumber/Matrix.html#AlgebraicGeometry.Scheme.Hom.dotProduct_mulVec_specialFiberIntersectionMatrix_nonpos)
- [Source of `AlgebraicGeometry.Scheme.Hom.dotProduct_mulVec_specialFiberIntersectionMatrix_nonpos` in TauCeti/AlgebraicGeometry/IntersectionNumber/Matrix.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicGeometry/IntersectionNumber/Matrix.lean#L363)
- [Tau Ceti roadmap status: Stable reduction of curves and stable maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/StableReduction/STATUS.md)
