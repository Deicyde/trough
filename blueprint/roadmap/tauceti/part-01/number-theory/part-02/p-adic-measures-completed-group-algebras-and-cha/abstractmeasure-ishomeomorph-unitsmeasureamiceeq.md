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
- [Source of `AbstractMeasure.isHomeomorph_unitsMeasureAmiceEquiv_weak` in TauCeti/NumberTheory/Padics/Measure/Units/Amice.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/Padics/Measure/Units/Amice.lean#L39)
- [Tau Ceti roadmap status: p-adic measures, completed group algebras, and characteristic ideals](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PadicMeasuresIwasawaAlgebras/STATUS.md)
