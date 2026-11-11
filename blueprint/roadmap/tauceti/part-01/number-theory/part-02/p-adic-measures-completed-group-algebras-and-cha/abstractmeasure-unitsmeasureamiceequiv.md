---
declaration: def
origin: cited
lean: AbstractMeasure.unitsMeasureAmiceEquiv
statement: formalized
---

# AbstractMeasure.unitsMeasureAmiceEquiv

Integral measures on the unit group are the integral series killed by psi.
The map is the Amice transform of inclusion along `Units.val`.

```lean
AbstractMeasure.unitsMeasureAmiceEquiv {p : ℕ} [Fact (Nat.Prime p)] :
  AbstractMeasure ℤ_[p]ˣ ℤ_[p] ℤ_[p] ≃ₗ[ℤ_[p]] ↥(TauCeti.psiSeries p).ker
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`AbstractMeasure.unitsMeasureAmiceEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/Units/Basic.html#AbstractMeasure.unitsMeasureAmiceEquiv).

## Sources

- [Tau Ceti documentation: `AbstractMeasure.unitsMeasureAmiceEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/Units/Basic.html#AbstractMeasure.unitsMeasureAmiceEquiv)
- [Source of `AbstractMeasure.unitsMeasureAmiceEquiv` in TauCeti/NumberTheory/Padics/Measure/Units/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Padics/Measure/Units/Basic.lean#L136)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
