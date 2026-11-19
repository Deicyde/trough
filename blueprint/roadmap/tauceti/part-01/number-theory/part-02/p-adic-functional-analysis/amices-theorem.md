---
declaration: def
origin: cited
lean: TauCeti.AnalyticStage.amiceEquiv
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

- [Legendre's formula for `(pᵏ)!`](../../part-03/padics/legendres-formula-for-pk.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AnalyticStage.amiceEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Amice/Isometry.html#TauCeti.AnalyticStage.amiceEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.AnalyticStage.amiceEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Distribution/Amice/Isometry.html#TauCeti.AnalyticStage.amiceEquiv)
- [Source of `TauCeti.AnalyticStage.amiceEquiv` in TauCeti/NumberTheory/Padics/Distribution/Amice/Isometry.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Padics/Distribution/Amice/Isometry.lean#L154)
- [Tau Ceti roadmap status: P-adic functional analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PadicFunctionalAnalysis/STATUS.md)
