---
declaration: theorem
origin: cited
lean: AbstractMeasure.isHomeomorph_unitsMeasureAmiceEquiv_weak
statement: formalized
proof: formalized
---

# AbstractMeasure.isHomeomorph_unitsMeasureAmiceEquiv_weak

The unit-measure Amice equivalence is a homeomorphism for the weak measure topology
and the coefficientwise p-adic topology on the series kernel.

```lean
AbstractMeasure.isHomeomorph_unitsMeasureAmiceEquiv_weak {p : ℕ} [Fact (Nat.Prime p)] :
  IsHomeomorph ⇑AbstractMeasure.unitsMeasureAmiceEquiv
```

## Depends on

- [AbstractMeasure.unitsMeasureAmiceEquiv](abstractmeasure-unitsmeasureamiceequiv.md)

## Lean

Formalized in Tau Ceti as [`AbstractMeasure.isHomeomorph_unitsMeasureAmiceEquiv_weak`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/Units/Amice.html#AbstractMeasure.isHomeomorph_unitsMeasureAmiceEquiv_weak).

## Sources

- [Tau Ceti documentation: `AbstractMeasure.isHomeomorph_unitsMeasureAmiceEquiv_weak`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/Measure/Units/Amice.html#AbstractMeasure.isHomeomorph_unitsMeasureAmiceEquiv_weak)
- [Source of `AbstractMeasure.isHomeomorph_unitsMeasureAmiceEquiv_weak` in TauCeti/NumberTheory/Padics/Measure/Units/Amice.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Padics/Measure/Units/Amice.lean#L39)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
