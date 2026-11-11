---
declaration: theorem
origin: cited
lean: AlgebraicGeometry.Scheme.isProjectiveOver_of_isCurveOver
statement: formalized
proof: formalized
---

# A regular proper curve is projective

if `X` is a curve over `k` whose codimension-one
local rings are discrete valuation rings, then `X` is a closed subscheme, over `k`, of the
projective space `Proj (Sym_k V)` of a finite-dimensional `k`-vector space `V`. No hypothesis on
the constants of the function field `k(X)` is needed.

```lean
AlgebraicGeometry.Scheme.isProjectiveOver_of_isCurveOver.{u} {k : Type u} [Field k]
  (X : AlgebraicGeometry.Scheme) [X.Over (AlgebraicGeometry.Spec ↧k)]
  [AlgebraicGeometry.Scheme.IsCurveOver k]
  [∀ (y : TauCeti.AlgebraicGeometry.CodimensionOnePoint X),
      IsDiscreteValuationRing ↑(X.presheaf.stalk ↑y)] :
  AlgebraicGeometry.Scheme.IsProjectiveOver k
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Krull–Akizuki for Mathlib's `integralClosure`](../../ring-theory/part-02/other-results/part-02/krull-akizuki-for-mathlibs-integralclosure.md)
- [Riemann's theorem](../../field-theory/function-field/part-02/riemanns-theorem.md)
- [The Riemann–Roch theorem (Stichtenoth, Theorem 1.5.15), for the divisor `(ω)` itself](the-riemann-roch-theorem-stichtenoth-theorem-1-5.md)
- [TauCeti.Divisor.sectionRing](tauceti-divisor-sectionring.md)
- [The weak approximation theorem](../../field-theory/function-field/part-02/the-weak-approximation-theorem.md)

## Lean

Formalized in Tau Ceti as [`AlgebraicGeometry.Scheme.isProjectiveOver_of_isCurveOver`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/TwoChartModel/ProjectiveEmbedding.html#AlgebraicGeometry.Scheme.isProjectiveOver_of_isCurveOver).

## Sources

- [Tau Ceti documentation: `AlgebraicGeometry.Scheme.isProjectiveOver_of_isCurveOver`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/Curves/TwoChartModel/ProjectiveEmbedding.html#AlgebraicGeometry.Scheme.isProjectiveOver_of_isCurveOver)
- [Source of `AlgebraicGeometry.Scheme.isProjectiveOver_of_isCurveOver` in TauCeti/AlgebraicGeometry/Curves/TwoChartModel/ProjectiveEmbedding.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/Curves/TwoChartModel/ProjectiveEmbedding.lean#L181)
- [Tau Ceti roadmap status: Algebraic curves — function fields, divisors, and Riemann–Roch](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AlgebraicCurves/STATUS.md)
