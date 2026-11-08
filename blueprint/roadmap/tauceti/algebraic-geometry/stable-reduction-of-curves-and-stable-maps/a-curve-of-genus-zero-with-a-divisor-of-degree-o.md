---
declaration: theorem
origin: cited
lean: TauCeti.HasNodalReduction.of_genus_eq_zero_of_divisor_degree_eq_one
statement: formalized
proof: formalized
---

# A curve of genus zero with a divisor of degree one has nodal reduction

Let `C` be a
regular proper curve over the fraction field `K` of a discrete valuation ring `R`, with `K`
integrally closed in `K(C)`. If `dim_K H¹(C, 𝒪_C) = 0` and some divisor on `C` has degree one,
then `C` has a proper at-worst-nodal model over `R`; indeed `C ≅ ℙ¹_K`, which has the smooth proper
model `ℙ¹_R`.

```lean
TauCeti.HasNodalReduction.of_genus_eq_zero_of_divisor_degree_eq_one.{u} {R K : Type u} [CommRing R]
  [IsDomain R] [IsDiscreteValuationRing R] [Field K] [Algebra R K] [IsFractionRing R K]
  (C : AlgebraicGeometry.Scheme) [C.Over (AlgebraicGeometry.Spec ↧K)]
  [AlgebraicGeometry.Scheme.IsCurveOver K]
  [∀ (y : TauCeti.AlgebraicGeometry.CodimensionOnePoint C),
      IsDiscreteValuationRing ↑(C.presheaf.stalk ↑y)]
  (hk : IsIntegrallyClosedIn K ↑C.functionField)
  (hg :
    Module.finrank K
        (TauCeti.AlgebraicGeometry.Scheme.Modules.Cohomology
          (TauCeti.AlgebraicGeometry.InvertibleSheaf.trivial C).obj 1) =
      0)
  {D : TauCeti.AlgebraicGeometry.SchemeWeilDivisor C}
  (hD :
    (TauCeti.AlgebraicGeometry.SchemeWeilDivisor.relativeDegree (C ↘ AlgebraicGeometry.Spec ↧K)) D =
      1) :
  TauCeti.HasNodalReduction R K C (C ↘ AlgebraicGeometry.Spec ↧K)
```

## Depends on

- [TauCeti.AlgebraicGeometry.AtWorstNodalOfRelativeDimensionOne](tauceti-algebraicgeometry-atworstnodalofrelative.md)

## Proof depends on

- [Krull–Akizuki's length bound](../../ring-theory/other-results/part-01/krull-akizukis-length-bound.md)
- [Riemann's theorem (Stichtenoth, Theorem 1.4.17)](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-02/riemanns-theorem-stichtenoth-theorem-1-4-17.md)
- [The Riemann–Roch theorem (Stichtenoth, Theorem 1.5.15), for the divisor `(ω)` itself](../../field-theory/algebraic-curves-function-fields-divisors-and-ri/part-01/the-riemann-roch-theorem-stichtenoth-theorem-1-5.md)
- [TauCeti.Ring.IsJapanese](../../ring-theory/scheme-stack-cohomology-and-intersection-foundat/tauceti-ring-isjapanese.md)
- [The weak approximation theorem for the places of an algebraic function field (Stichtenoth, Theorem 1.3.1), in the equality form](../../field-theory/function-field/the-weak-approximation-theorem-for-the-places-of.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.HasNodalReduction.of_genus_eq_zero_of_divisor_degree_eq_one`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/StableReduction/GenusZero.html#TauCeti.HasNodalReduction.of_genus_eq_zero_of_divisor_degree_eq_one).

## Sources

- [Tau Ceti documentation: `TauCeti.HasNodalReduction.of_genus_eq_zero_of_divisor_degree_eq_one`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/StableReduction/GenusZero.html#TauCeti.HasNodalReduction.of_genus_eq_zero_of_divisor_degree_eq_one)
- [Source of `TauCeti.HasNodalReduction.of_genus_eq_zero_of_divisor_degree_eq_one` in TauCeti/AlgebraicGeometry/Curves/StableReduction/GenusZero.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/Curves/StableReduction/GenusZero.lean#L73)
- [Tau Ceti roadmap status: Stable reduction of curves and stable maps](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/StableReduction/STATUS.md)
