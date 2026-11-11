---
declaration: theorem
origin: cited
lean: TauCeti.ae_tendsto_setLAverage_dyadicCube
statement: formalized
proof: formalized
---

# Lebesgue's differentiation theorem along dyadic cubes

for an integrable `g`, at almost
every `x` the averages of `g` over the dyadic cubes containing `x` converge to `g x` as the level
tends to `-∞`.

```lean
TauCeti.ae_tendsto_setLAverage_dyadicCube.{u_1} {ι : Type u_1} [Fintype ι] {g : (ι → ℝ) → ENNReal}
  (hg : AEMeasurable g MeasureTheory.volume) (hg' : ∫⁻ (x : ι → ℝ), g x ≠ ⊤) :
  ∀ᵐ (x : ι → ℝ),
    Filter.Tendsto (fun k => ⨍⁻ (y : ι → ℝ) in TauCeti.dyadicCube k (TauCeti.dyadicIndex k x), g y)
      Filter.atBot (nhds (g x))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ae_tendsto_setLAverage_dyadicCube`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/DyadicCube.html#TauCeti.ae_tendsto_setLAverage_dyadicCube).

## Sources

- [Tau Ceti documentation: `TauCeti.ae_tendsto_setLAverage_dyadicCube`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/DyadicCube.html#TauCeti.ae_tendsto_setLAverage_dyadicCube)
- [Source of `TauCeti.ae_tendsto_setLAverage_dyadicCube` in TauCeti/MeasureTheory/Measure/Lebesgue/DyadicCube.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Measure/Lebesgue/DyadicCube.lean#L288)
