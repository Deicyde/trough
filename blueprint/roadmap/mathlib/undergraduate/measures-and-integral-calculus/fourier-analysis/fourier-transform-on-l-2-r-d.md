---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.Lp.fourierTransformₗᵢ
mathlib_file: Mathlib/Analysis/Fourier/LpSpace.lean
---

# Fourier transform on $\mathrm{L}^2(\R^d)$

The Fourier transform on `L2` as a linear isometry equivalence.

```lean
MeasureTheory.Lp.fourierTransformₗᵢ.{u_1, u_2} (E : Type u_1) (F : Type u_2) [NormedAddCommGroup E]
  [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F] [InnerProductSpace ℂ F]
  [CompleteSpace F] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] :
  ↥(MeasureTheory.Lp F 2 MeasureTheory.volume) ≃ₗᵢ[ℂ] ↥(MeasureTheory.Lp F 2 MeasureTheory.volume)
```

## Depends on

- [Fourier transforms on $\mathcal{S}(\R^d)$](../../distribution-calculus/spaces-s-r-d/fourier-transforms-on-s-r-d.md)
- [Hausdorff space](../../../overview/topology/general-topology/part-01/hausdorff-space.md)
- [Homeomorphisms](../../topology/topology-and-metric-spaces/homeomorphisms.md)
- [Kernel of a linear map](../../linear-algebra/fundamentals/kernel-of-a-linear-map.md)
- [Quotient space (Fundamentals)](../../../overview/linear-algebra/fundamentals/quotient-space.md)
- [Range of a linear map](../../linear-algebra/fundamentals/range-of-a-linear-map.md)
- [Topological module](../../../overview/topology/topological-algebra/topological-module.md)

## Sources

- [Mathlib documentation: `MeasureTheory.Lp.fourierTransformₗᵢ`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/LpSpace.html#MeasureTheory.Lp.fourierTransform%E2%82%97%E1%B5%A2)
- [Source of `MeasureTheory.Lp.fourierTransformₗᵢ` in Mathlib/Analysis/Fourier/LpSpace.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Fourier/LpSpace.lean#L49)
- [Mathlib undergraduate list: Measures and integral calculus › Fourier analysis](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L539)
