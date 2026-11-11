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
- [Source of `AbstractMeasure.norm_toCLMEquiv_eq_iSup_coeff` in TauCeti/NumberTheory/Padics/Measure/MahlerDuality.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Padics/Measure/MahlerDuality.lean#L198)
- [Tau Ceti roadmap status: P-adic functional analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PadicFunctionalAnalysis/STATUS.md)
