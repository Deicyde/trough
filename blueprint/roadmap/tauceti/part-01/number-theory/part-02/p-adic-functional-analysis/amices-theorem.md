---
declaration: def
origin: cited
lean: TauCeti.AnalyticStage.amiceEquiv, TauCeti.AnalyticStage.norm_amiceMap, TauCeti.LocallyAnalyticDistribution.mem_range_amiceTransform_iff, TauCeti.AnalyticStage.amiceMap_surjective
statement: formalized
---

# Amice's theorem

Amice's map `(cₙ) ↦ ∑ₙ e_{h,n} • cₙ`, where
`e_{h,n}(x) = ⌊n / pʰ⌋! (x choose n)`, is an isometric isomorphism from the null sequences in `E`
onto the analytic stage `LA_h(E)`.

```lean
TauCeti.AnalyticStage.amiceEquiv.{u_1, u_2} (p : ℕ) [hp : Fact (Nat.Prime p)] (h : ℕ) {E : Type u_1}
  [NormedAddCommGroup E] [_root_.Module ℤ_[p] E] [IsBoundedSMul ℤ_[p] E] [IsUltrametricDist E]
  [CompleteSpace E] (S : Type u_2) [Semiring S] [_root_.Module S E] [ContinuousConstSMul S E]
  [SMulCommClass ℤ_[p] S E] : ZeroAtInftyContinuousMap ℕ E ≃ₗᵢ[S] TauCeti.AnalyticStage p h E
```

## Depends on

- [TauCeti.AnalyticStage.transition](tauceti-analyticstage-transition.md)

## Proof depends on

- [Legendre's formula for `(pᵏ)!`](../padics/legendres-formula-for-pk.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AnalyticStage.amiceEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Amice/Isometry.html#TauCeti.AnalyticStage.amiceEquiv).

## Other forms

**Amice's theorem.** Formalized in Tau Ceti as [`TauCeti.AnalyticStage.norm_amiceMap`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Amice/Isometry.html#TauCeti.AnalyticStage.norm_amiceMap).

```lean
TauCeti.AnalyticStage.norm_amiceMap.{u_1, u_2} {p : ℕ} [hp : Fact (Nat.Prime p)] {h : ℕ}
  {E : Type u_1} [NormedAddCommGroup E] [_root_.Module ℤ_[p] E] [IsBoundedSMul ℤ_[p] E]
  [IsUltrametricDist E] [CompleteSpace E] (S : Type u_2) [Semiring S] [_root_.Module S E]
  [ContinuousConstSMul S E] [SMulCommClass ℤ_[p] S E] (c : ZeroAtInftyContinuousMap ℕ E) :
  ‖(TauCeti.AnalyticStage.amiceMap p h S) c‖ = ‖c‖
```

**Amice's theorem for distributions.** Formalized in Tau Ceti as [`TauCeti.LocallyAnalyticDistribution.mem_range_amiceTransform_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Amice/Transform.html#TauCeti.LocallyAnalyticDistribution.mem_range_amiceTransform_iff).

```lean
TauCeti.LocallyAnalyticDistribution.mem_range_amiceTransform_iff.{u_1} {p : ℕ}
  [hp : Fact (Nat.Prime p)] {K : Type u_1} [NontriviallyNormedField K] [Algebra ℤ_[p] K]
  [IsBoundedSMul ℤ_[p] K] [IsUltrametricDist K] [CompleteSpace K] [NormedAlgebra ℚ_[p] K]
  {F : PowerSeries K} :
  F ∈ TauCeti.LocallyAnalyticDistribution.amiceTransform.range ↔ PowerSeries.OnOpenDisc 1 F
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

- [Tau Ceti documentation: `TauCeti.AnalyticStage.amiceEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Amice/Isometry.html#TauCeti.AnalyticStage.amiceEquiv)
- [Source of `TauCeti.AnalyticStage.amiceEquiv` in TauCeti/NumberTheory/Padics/Distribution/Amice/Isometry.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Padics/Distribution/Amice/Isometry.lean#L154)
