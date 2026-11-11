---
declaration: def
origin: cited
lean: ContinuousMonoidHom.unitCharacterEval
statement: formalized
---

# ContinuousMonoidHom.unitCharacterEval

Evaluation of pseudo-measures on `ℤ_pˣ` at a nontrivial continuous character `κ`: the
pseudo-measure `z` is sent to `n_g(z)(κ) / (κ g - 1)` in `ℚ_p`, for any `g` with `κ g ≠ 1`, where
`n_g(z) = (δ_g - 1) z` is the cleared numerator. The value does not depend on `g`
(`unitCharacterEval_eq_div`).

```lean
ContinuousMonoidHom.unitCharacterEval {p : ℕ} [Fact (Nat.Prime p)] (κ : ℤ_[p]ˣ →ₜ* ℤ_[p])
  (hκ : κ ≠ 1) : ↥(AbstractMeasure.unitsPseudomeasures p) →+ ℚ_[p]
```

## Depends on

- [AbstractMeasure.unitsPseudomeasures](abstractmeasure-unitspseudomeasures.md)

## Lean

Formalized in Tau Ceti as [`ContinuousMonoidHom.unitCharacterEval`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/Units/Pseudomeasure.html#ContinuousMonoidHom.unitCharacterEval).

## Sources

- [Tau Ceti documentation: `ContinuousMonoidHom.unitCharacterEval`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/Units/Pseudomeasure.html#ContinuousMonoidHom.unitCharacterEval)
- [Source of `ContinuousMonoidHom.unitCharacterEval` in TauCeti/NumberTheory/Padics/Measure/Units/Pseudomeasure.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Padics/Measure/Units/Pseudomeasure.lean#L122)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
