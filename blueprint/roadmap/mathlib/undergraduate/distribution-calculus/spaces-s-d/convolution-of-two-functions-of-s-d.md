---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: SchwartzMap.convolution
mathlib_file: Mathlib/Analysis/Fourier/Convolution.lean
---

# Convolution of two functions of $\mathcal{S}(\R^d)$

The bilinear convolution of Schwartz functions.

The continuity in the left argument is provided in `SchwartzMap.convolution_continuous_left`.

```lean
SchwartzMap.convolution.{u_1, u_3, u_5, u_6, u_7} {𝕜 : Type u_1} {E : Type u_3} {F₁ : Type u_5}
  {F₂ : Type u_6} {F₃ : Type u_7} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace ℝ E]
  [FiniteDimensional ℝ E] [MeasurableSpace E] [BorelSpace E] [NormedAddCommGroup F₁]
  [NormedSpace ℂ F₁] [NormedSpace 𝕜 F₁] [SMulCommClass ℂ 𝕜 F₁] [NormedAddCommGroup F₂]
  [NormedSpace ℂ F₂] [NormedSpace 𝕜 F₂] [SMulCommClass ℂ 𝕜 F₂] [NormedAddCommGroup F₃]
  [NormedSpace ℂ F₃] [NormedSpace 𝕜 F₃] [SMulCommClass ℂ 𝕜 F₃] (B : F₁ →L[𝕜] F₂ →L[𝕜] F₃) :
  SchwartzMap E F₁ →ₗ[𝕜] SchwartzMap E F₂ →L[𝕜] SchwartzMap E F₃
```

## Depends on

- [Fourier transforms](../tempered-distributions/fourier-transforms.md)
- [Fourier transforms on $\mathcal{S}(\R^d)$](fourier-transforms-on-s-d.md)
- [Homeomorphisms](../../topology/topology-and-metric-spaces/homeomorphisms.md)
- [Inverse Fourier transform](../tempered-distributions/inverse-fourier-transform.md)
- [Stability by multiplication by a slowly growing smooth function](stability-by-multiplication-by-a-slowly-growing.md)

## Sources

- [Mathlib documentation: `SchwartzMap.convolution`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/Convolution.html#SchwartzMap.convolution)
- [Source of `SchwartzMap.convolution` in Mathlib/Analysis/Fourier/Convolution.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Fourier/Convolution.lean#L141)
- [Mathlib undergraduate list: Distribution calculus › Spaces $\mathcal{S}(\R^d)$](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L612)
