---
declaration: def
origin: cited
lean: TauCeti.bochnerMeasure
statement: formalized
---

# The representing measure of Bochner's theorem

the unique finite Borel measure whose
Fourier-convention transform is `F`, when `F` is continuous and positive definite, and the zero
measure otherwise.

```lean
TauCeti.bochnerMeasure.{u_1} {V : Type u_1} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
  [FiniteDimensional ℝ V] [MeasurableSpace V] [BorelSpace V] (F : V → ℂ) : MeasureTheory.Measure V
```

## Depends on

Its statement uses no other declaration mapped here.

## Informally uses

- [Bochner's theorem](bochners-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.bochnerMeasure`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/BochnerTheorem.html#TauCeti.bochnerMeasure).

## Sources

- [Tau Ceti documentation: `TauCeti.bochnerMeasure`](https://taucetiproject.org/docs/TauCeti/Analysis/Bochner/BochnerTheorem.html#TauCeti.bochnerMeasure)
- [Source of `TauCeti.bochnerMeasure` in TauCeti/Analysis/Bochner/BochnerTheorem.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Bochner/BochnerTheorem.lean#L303)
