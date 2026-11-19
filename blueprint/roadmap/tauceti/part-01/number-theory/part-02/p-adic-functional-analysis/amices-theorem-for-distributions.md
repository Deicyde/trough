---
declaration: theorem
origin: cited
lean: TauCeti.LocallyAnalyticDistribution.mem_range_amiceTransform_iff, TauCeti.AnalyticStage.norm_amiceMap, TauCeti.AnalyticStage.amiceMap_surjective
statement: formalized
proof: formalized
---

# Amice's theorem for distributions

When the complete field `K` is a normed
`ℚ_p`-algebra, a power series over `K` is the Amice transform of a locally analytic distribution
exactly when it converges on the open unit disc. Together with `amiceTransform_injective`, the
Amice transform identifies distributions with the power series on the open unit disc.

```lean
TauCeti.LocallyAnalyticDistribution.mem_range_amiceTransform_iff.{u_1} {p : ℕ}
  [hp : Fact (Nat.Prime p)] {K : Type u_1} [NontriviallyNormedField K] [Algebra ℤ_[p] K]
  [IsBoundedSMul ℤ_[p] K] [IsUltrametricDist K] [CompleteSpace K] [NormedAlgebra ℚ_[p] K]
  {F : PowerSeries K} :
  F ∈ TauCeti.LocallyAnalyticDistribution.amiceTransform.range ↔ PowerSeries.OnOpenDisc 1 F
```

## Depends on

- [TauCeti.LocallyAnalyticDistribution](tauceti-locallyanalyticdistribution.md)

## Proof depends on

- [Amice's theorem](amices-theorem.md)
- [Legendre's formula for `(pᵏ)!`](../../part-03/padics/legendres-formula-for-pk.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LocallyAnalyticDistribution.mem_range_amiceTransform_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Amice/Transform.html#TauCeti.LocallyAnalyticDistribution.mem_range_amiceTransform_iff).

## Other forms

**Amice's theorem.** Formalized in Tau Ceti as [`TauCeti.AnalyticStage.norm_amiceMap`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Amice/Isometry.html#TauCeti.AnalyticStage.norm_amiceMap).

```lean
TauCeti.AnalyticStage.norm_amiceMap.{u_1, u_2} {p : ℕ} [hp : Fact (Nat.Prime p)] {h : ℕ}
  {E : Type u_1} [NormedAddCommGroup E] [_root_.Module ℤ_[p] E] [IsBoundedSMul ℤ_[p] E]
  [IsUltrametricDist E] [CompleteSpace E] (S : Type u_2) [Semiring S] [_root_.Module S E]
  [ContinuousConstSMul S E] [SMulCommClass ℤ_[p] S E] (c : ZeroAtInftyContinuousMap ℕ E) :
  ‖(TauCeti.AnalyticStage.amiceMap p h S) c‖ = ‖c‖
```

**Amice's theorem: surjectivity.** Formalized in Tau Ceti as [`TauCeti.AnalyticStage.amiceMap_surjective`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Amice/Isometry.html#TauCeti.AnalyticStage.amiceMap_surjective).

```lean
TauCeti.AnalyticStage.amiceMap_surjective.{u_1, u_2} (p : ℕ) [hp : Fact (Nat.Prime p)] (h : ℕ)
  {E : Type u_1} [NormedAddCommGroup E] [_root_.Module ℤ_[p] E] [IsBoundedSMul ℤ_[p] E]
  [IsUltrametricDist E] [CompleteSpace E] (S : Type u_2) [Semiring S] [_root_.Module S E]
  [ContinuousConstSMul S E] [SMulCommClass ℤ_[p] S E] :
  Function.Surjective ⇑(TauCeti.AnalyticStage.amiceMap p h S)
```

## Sources

- [Tau Ceti documentation: `TauCeti.LocallyAnalyticDistribution.mem_range_amiceTransform_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Amice/Transform.html#TauCeti.LocallyAnalyticDistribution.mem_range_amiceTransform_iff)
- [Source of `TauCeti.LocallyAnalyticDistribution.mem_range_amiceTransform_iff` in TauCeti/NumberTheory/Padics/Distribution/Amice/Transform.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Padics/Distribution/Amice/Transform.lean#L338)
- [Tau Ceti roadmap status: P-adic functional analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PadicFunctionalAnalysis/STATUS.md)
