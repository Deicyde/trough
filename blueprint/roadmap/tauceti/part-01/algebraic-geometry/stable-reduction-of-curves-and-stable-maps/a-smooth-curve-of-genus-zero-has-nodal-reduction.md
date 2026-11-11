---
declaration: theorem
origin: cited
lean: TauCeti.HasNodalReduction.exists_finrank_le_two_of_genus_eq_zero
statement: formalized
proof: formalized
---

# A smooth curve of genus zero has nodal reduction after a separable extension of degree at most two

Let `C` be a smooth proper geometrically integral curve over the fraction field `K` of
a discrete valuation ring `R`, with `dim_K H¹(C, 𝒪_C) = 0`. Then there is a finite separable
extension `K'` of `K` of degree at most two, with a chosen place above the closed point of `R` and
local ring `R'`, such that `C_{K'}` has a proper at-worst-nodal model over `R'`; indeed
`C_{K'} ≅ ℙ¹_{K'}`, which has the smooth proper model `ℙ¹_{R'}`.

```lean
TauCeti.HasNodalReduction.exists_finrank_le_two_of_genus_eq_zero.{u} {R K : Type u} [CommRing R]
  [IsDomain R] [IsDiscreteValuationRing R] [Field K] [Algebra R K] [IsFractionRing R K]
  (C : AlgebraicGeometry.Scheme) [C.Over (AlgebraicGeometry.Spec ↧K)]
  [AlgebraicGeometry.IsProper (C ↘ AlgebraicGeometry.Spec ↧K)]
  [AlgebraicGeometry.SmoothOfRelativeDimension 1 (C ↘ AlgebraicGeometry.Spec ↧K)]
  [AlgebraicGeometry.GeometricallyIntegral (C ↘ AlgebraicGeometry.Spec ↧K)]
  (hg :
    Module.finrank K
        (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology
          (TauCeti.AlgebraicGeometry.InvertibleSheaf.trivial C).obj 1) =
      0) :
  ∃ E,
    Module.finrank K E.extensionField ≤ 2 ∧
      TauCeti.HasNodalReduction E.localRing E.extensionField
        (TauCeti.genericFiber K E.extensionField (C ↘ AlgebraicGeometry.Spec ↧K)).left
        (TauCeti.genericFiber K E.extensionField (C ↘ AlgebraicGeometry.Spec ↧K)).hom
```

## Depends on

- [TauCeti.AlgebraicGeometry.AtWorstNodalOfRelativeDimensionOne](tauceti-algebraicgeometry-atworstnodalofrelative.md)

## Proof depends on

- [The global dimension of a regular local ring is its Krull dimension](../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [The Jacobian criterion for étaleness](../../ring-theory/part-02/other-results/part-02/the-jacobian-criterion-for-etaleness.md)
- [Krull–Akizuki for Mathlib's `integralClosure`](../../ring-theory/part-02/other-results/part-02/krull-akizuki-for-mathlibs-integralclosure.md)
- [Kummer's theorem (Stichtenoth, Corollary 3.3.8)](../../field-theory/function-field/part-01/kummers-theorem-stichtenoth-corollary-3-3-8.md)
- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [The Riemann–Roch theorem (Stichtenoth, Theorem 1.5.15), for the divisor `(ω)` itself](../algebraic-curves-function-fields-divisors-and-ri/the-riemann-roch-theorem-stichtenoth-theorem-1-5.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [Serre's vanishing theorem on affine opens](../other-results/serres-vanishing-theorem-on-affine-opens.md)
- [TauCeti.AlgebraicGeometry.FiniteLocallyFreeSheaf](../algebraic-vector-bundles/tauceti-algebraicgeometry-finitelocallyfreesheaf-2.md)
- [TauCeti.globalDimension](../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HasNodalReduction.exists_finrank_le_two_of_genus_eq_zero`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/StableReduction/GenusZero.html#TauCeti.HasNodalReduction.exists_finrank_le_two_of_genus_eq_zero).

## Sources

- [Tau Ceti documentation: `TauCeti.HasNodalReduction.exists_finrank_le_two_of_genus_eq_zero`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/StableReduction/GenusZero.html#TauCeti.HasNodalReduction.exists_finrank_le_two_of_genus_eq_zero)
- [Source of `TauCeti.HasNodalReduction.exists_finrank_le_two_of_genus_eq_zero` in TauCeti/AlgebraicGeometry/Curves/StableReduction/GenusZero.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Curves/StableReduction/GenusZero.lean#L93)
- [Tau Ceti roadmap status: Stable reduction of curves and stable maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/StableReduction/STATUS.md)
