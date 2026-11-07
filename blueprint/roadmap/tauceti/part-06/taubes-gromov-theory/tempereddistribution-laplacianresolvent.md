---
declaration: def
origin: cited
lean: TemperedDistribution.laplacianResolvent
statement: formalized
---

# TemperedDistribution.laplacianResolvent

The **resolvent of the Laplacian** `(c - Δ)⁻¹` on tempered distributions: the Fourier
multiplier with symbol `((2π)² ‖ξ‖² + c)⁻¹`. For `c > 0` it is the two-sided inverse of `-Δ + c`
(`laplacianResolvent_neg_laplacian_add_smul` and `neg_laplacian_laplacianResolvent_add_smul`);
for `c ≤ 0` the value is not meaningful.

```lean
TemperedDistribution.laplacianResolvent.{u_1, u_2} {E : Type u_1} (F : Type u_2)
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] [NormedAddCommGroup F] [NormedSpace ℂ F] (c : ℝ) :
  TemperedDistribution E F →L[ℂ] TemperedDistribution E F
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TemperedDistribution.laplacianResolvent`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TemperedDistribution/LaplacianResolvent.html#TemperedDistribution.laplacianResolvent).

## Sources

- [Tau Ceti documentation: `TemperedDistribution.laplacianResolvent`](https://taucetiproject.org/docs/TauCeti/Analysis/Distribution/TemperedDistribution/LaplacianResolvent.html#TemperedDistribution.laplacianResolvent)
- [Source of `TemperedDistribution.laplacianResolvent` in TauCeti/Analysis/Distribution/TemperedDistribution/LaplacianResolvent.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Distribution/TemperedDistribution/LaplacianResolvent.lean#L94)
- [Tau Ceti roadmap status: Taubes–Gromov theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TaubesGromov/STATUS.md)
