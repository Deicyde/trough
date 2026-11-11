---
declaration: theorem
origin: cited
lean: TauCeti.exists_log_normalizedValuationWithZero_zpow_sub_one_le
statement: formalized
proof: formalized
---

# The one-factor estimate

Let `K` be a nonarchimedean local field of characteristic zero,
that is, a finite extension of `ℚ_[p]`. For every fixed `α ∈ K` there is a constant `C`,
depending on `α` and `K`, such that

`v_K(α ^ b - 1) ≤ C (1 + log max(1, |b|))` for every integer `b` with `α ^ b ≠ 1`.

```lean
TauCeti.exists_log_normalizedValuationWithZero_zpow_sub_one_le.{u_1} {K : Type u_1} [Field K]
  [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] [CharZero K] (α : K) :
  ∃ C,
    ∀ (b : ℤ),
      α ^ b ≠ 1 →
        ↑((TauCeti.normalizedValuationWithZero K) (α ^ b - 1)).log ≤ C * (1 + Real.log (max 1 |↑b|))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_log_normalizedValuationWithZero_zpow_sub_one_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/UnitFiltration/Pow/SubOne.html#TauCeti.exists_log_normalizedValuationWithZero_zpow_sub_one_le).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_log_normalizedValuationWithZero_zpow_sub_one_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/UnitFiltration/Pow/SubOne.html#TauCeti.exists_log_normalizedValuationWithZero_zpow_sub_one_le)
- [Source of `TauCeti.exists_log_normalizedValuationWithZero_zpow_sub_one_le` in TauCeti/NumberTheory/LocalField/UnitFiltration/Pow/SubOne.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/UnitFiltration/Pow/SubOne.lean#L217)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
