# Fourier transforms

The Fourier transform as a continuous linear map.

```lean
FourierTransform.fourierCLM.{u_2, u_3, u_4} (R : Type u_2) (E : Type u_3) {F : Type u_4}
  [Semiring R] [AddCommMonoid E] [AddCommMonoid F] [_root_.Module R E] [_root_.Module R F]
  [FourierTransform E F] [FourierAdd E F] [FourierSMul R E F] [TopologicalSpace E]
  [TopologicalSpace F] [ContinuousFourier E F] : E →L[R] F
```

## Depends on

- [Continuous linear map](../../../overview/topology/topological-algebra/continuous-linear-map.md)

## Sources

- [Mathlib documentation: `FourierTransform.fourierCLM`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/Notation.html#FourierTransform.fourierCLM)
- [Source of `FourierTransform.fourierCLM` in Mathlib/Analysis/Fourier/Notation.lean](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/Mathlib/Analysis/Fourier/Notation.lean#L172)
- [Mathlib undergraduate list: Distribution calculus › Tempered distributions](https://github.com/leanprover-community/mathlib4/blob/9bac2d0692944a775113f7c130fd5e5b4608a854/docs/undergrad.yaml#L621)
