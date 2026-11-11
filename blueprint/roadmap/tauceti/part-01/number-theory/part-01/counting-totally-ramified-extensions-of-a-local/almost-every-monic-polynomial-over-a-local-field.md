---
declaration: theorem
origin: cited
lean: MeasureTheory.Measure.ae_separable_monicOfCoeff
statement: formalized
proof: formalized
---

# Almost every monic polynomial over a local field is separable

For every
translation-invariant measure `μ` on the coefficient space `Fin n → K` that is finite on compact
sets, such as Haar measure, the monic polynomial `monicOfCoeff a` with coefficient vector `a` is
separable for `μ`-almost every `a`. This holds in every characteristic.

```lean
MeasureTheory.Measure.ae_separable_monicOfCoeff.{u_1} {K : Type u_1} [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] {n : ℕ} [MeasurableSpace (Fin n → K)]
  [BorelSpace (Fin n → K)] (μ : MeasureTheory.Measure (Fin n → K)) [μ.IsAddLeftInvariant]
  [MeasureTheory.IsFiniteMeasureOnCompacts μ] :
  ∀ᵐ (a : Fin n → K) ∂μ, (TauCeti.Polynomial.monicOfCoeff a).Separable
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Measure.ae_separable_monicOfCoeff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/AESeparable.html#MeasureTheory.Measure.ae_separable_monicOfCoeff).

## Sources

- [Tau Ceti documentation: `MeasureTheory.Measure.ae_separable_monicOfCoeff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/AESeparable.html#MeasureTheory.Measure.ae_separable_monicOfCoeff)
- [Source of `MeasureTheory.Measure.ae_separable_monicOfCoeff` in TauCeti/NumberTheory/LocalField/AESeparable.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/LocalField/AESeparable.lean#L108)
- [Tau Ceti roadmap status: Counting totally ramified extensions of a local field, and Serre's mass formula](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/MassFormula/STATUS.md)
