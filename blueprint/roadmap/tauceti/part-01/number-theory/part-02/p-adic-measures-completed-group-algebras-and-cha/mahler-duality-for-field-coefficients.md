---
declaration: theorem
origin: cited
lean: AbstractMeasure.norm_toCLMEquiv_eq_iSup_coeff
statement: formalized
proof: formalized
---

# Mahler duality for field coefficients

Over a complete ultrametric nontrivially normed
field with a contractive `ℤ_[p]`-algebra structure, such as a complete extension of `ℚ_p`, the
operator norm of a measure on `ℤ_p` is the supremum of the norms of the coefficients of its Amice
transform.

```lean
AbstractMeasure.norm_toCLMEquiv_eq_iSup_coeff.{u_1} {p : ℕ} [Fact (Nat.Prime p)] {K : Type u_1}
  [NontriviallyNormedField K] [Algebra ℤ_[p] K] [IsBoundedSMul ℤ_[p] K] [IsUltrametricDist K]
  [CompleteSpace K] (μ : AbstractMeasure ℤ_[p] K K) :
  ‖AbstractMeasure.toCLMEquiv μ‖ = ⨆ n, ‖(PowerSeries.coeff n) (AbstractMeasure.amiceTransform μ)‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AbstractMeasure.norm_toCLMEquiv_eq_iSup_coeff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/MahlerDuality.html#AbstractMeasure.norm_toCLMEquiv_eq_iSup_coeff).

## Sources

- [Tau Ceti documentation: `AbstractMeasure.norm_toCLMEquiv_eq_iSup_coeff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/MahlerDuality.html#AbstractMeasure.norm_toCLMEquiv_eq_iSup_coeff)
- [Source of `AbstractMeasure.norm_toCLMEquiv_eq_iSup_coeff` in TauCeti/NumberTheory/Padics/Measure/MahlerDuality.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Padics/Measure/MahlerDuality.lean#L199)
