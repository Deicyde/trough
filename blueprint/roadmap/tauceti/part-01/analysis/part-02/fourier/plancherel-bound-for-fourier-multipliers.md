---
declaration: theorem
origin: cited
lean: MeasureTheory.Lp.norm_fourierMultiplierCLM_le, TauCeti.norm_rieszTransform_le
statement: formalized
proof: formalized
---

# Plancherel bound for Fourier multipliers

`‖T_m‖ ≤ ‖m‖_∞`.

```lean
MeasureTheory.Lp.norm_fourierMultiplierCLM_le.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F]
  (m : ↥(MeasureTheory.Lp ℂ ⊤ MeasureTheory.volume)) :
  ‖MeasureTheory.Lp.fourierMultiplierCLM F m‖ ≤ ‖m‖
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MeasureTheory.Lp.norm_fourierMultiplierCLM_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/L2Multiplier.html#MeasureTheory.Lp.norm_fourierMultiplierCLM_le).

## Other forms

**Plancherel bound for the Riesz transform.** Formalized in Tau Ceti as [`TauCeti.norm_rieszTransform_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/RieszTransform/Basic.html#TauCeti.norm_rieszTransform_le).

```lean
TauCeti.norm_rieszTransform_le.{u_1, u_2} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [MeasurableSpace E] [BorelSpace E] [FiniteDimensional ℝ E] {F : Type u_2}
  [NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F] (v : E) :
  ‖TauCeti.rieszTransform F v‖ ≤ ‖v‖
```

## Sources

- [Tau Ceti documentation: `MeasureTheory.Lp.norm_fourierMultiplierCLM_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/L2Multiplier.html#MeasureTheory.Lp.norm_fourierMultiplierCLM_le)
- [Source of `MeasureTheory.Lp.norm_fourierMultiplierCLM_le` in TauCeti/Analysis/Fourier/L2Multiplier.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Fourier/L2Multiplier.lean#L125)
