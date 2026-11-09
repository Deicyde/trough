---
declaration: def
origin: cited
lean: TauCeti.AnalyticStage.amiceEquiv, TauCeti.AnalyticStage.norm_amiceMap, TauCeti.AnalyticStage.amiceMap_surjective
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

Its statement uses no other declaration mapped here.

## Proof depends on

- [Legendre's formula for `(pᵏ)!`](../../part-02/padics/legendres-formula-for-pk.md)

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
- [Source of `TauCeti.AnalyticStage.amiceEquiv` in TauCeti/NumberTheory/Padics/Distribution/Amice/Isometry.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Padics/Distribution/Amice/Isometry.lean#L154)
