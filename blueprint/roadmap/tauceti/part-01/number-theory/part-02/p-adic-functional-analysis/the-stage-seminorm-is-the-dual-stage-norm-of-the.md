---
declaration: theorem
origin: cited
lean: TauCeti.LocallyAnalyticDistribution.stageSeminorm_eq_amiceDualNorm
statement: formalized
proof: formalized
---

# The stage seminorm is the dual stage norm of the Amice transform

For a normed
`ℚ_p`-algebra `K`, the norm of a distribution on the stage `LA_h(K)` is
`D_h(Aμ) = supₙ ‖bₙ‖ ‖⌊n / pʰ⌋!‖`, the factorials being taken in `ℚ_p`.

```lean
TauCeti.LocallyAnalyticDistribution.stageSeminorm_eq_amiceDualNorm.{u_1} {p : ℕ}
  [hp : Fact (Nat.Prime p)] {K : Type u_1} [NontriviallyNormedField K] [Algebra ℤ_[p] K]
  [IsBoundedSMul ℤ_[p] K] [IsUltrametricDist K] [CompleteSpace K] [NormedAlgebra ℚ_[p] K]
  (μ : ↥(TauCeti.LocallyAnalyticDistribution p K)) (h : ℕ) :
  (TauCeti.LocallyAnalyticDistribution.stageSeminorm h) μ =
    TauCeti.amiceDualNorm p h (TauCeti.LocallyAnalyticDistribution.amiceTransform μ)
```

## Depends on

- [TauCeti.LocallyAnalyticDistribution](tauceti-locallyanalyticdistribution.md)

## Proof depends on

- [Amice's theorem](amices-theorem.md)
- [Legendre's formula for `(pᵏ)!`](../../part-03/padics/legendres-formula-for-pk.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LocallyAnalyticDistribution.stageSeminorm_eq_amiceDualNorm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Amice/Transform.html#TauCeti.LocallyAnalyticDistribution.stageSeminorm_eq_amiceDualNorm).

## Sources

- [Tau Ceti documentation: `TauCeti.LocallyAnalyticDistribution.stageSeminorm_eq_amiceDualNorm`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Amice/Transform.html#TauCeti.LocallyAnalyticDistribution.stageSeminorm_eq_amiceDualNorm)
- [Source of `TauCeti.LocallyAnalyticDistribution.stageSeminorm_eq_amiceDualNorm` in TauCeti/NumberTheory/Padics/Distribution/Amice/Transform.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Padics/Distribution/Amice/Transform.lean#L249)
- [Tau Ceti roadmap status: P-adic functional analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PadicFunctionalAnalysis/STATUS.md)
