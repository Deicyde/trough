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
- [Source of `AbstractMeasure.unitsMeasureAmiceEquiv` in TauCeti/NumberTheory/Padics/Measure/Units/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Padics/Measure/Units/Basic.lean#L136)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
