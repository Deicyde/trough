# Inverse Fourier transform

The inverse Fourier transform as a continuous linear map.

```lean
FourierTransform.fourierInvCLM.{u_2, u_3, u_4} (R : Type u_2) (E : Type u_3) {F : Type u_4}
  [Semiring R] [AddCommMonoid E] [AddCommMonoid F] [_root_.Module R E] [_root_.Module R F]
  [FourierTransformInv E F] [FourierInvAdd E F] [FourierInvSMul R E F] [TopologicalSpace E]
  [TopologicalSpace F] [ContinuousFourierInv E F] : E →L[R] F
```

## Depends on

- [Continuous linear map](../../../overview/topology/topological-algebra/continuous-linear-map.md)

## Sources

- [Mathlib documentation: `FourierTransform.fourierInvCLM`](https://leanprover-community.github.io/mathlib4_docs/Mathlib/Analysis/Fourier/Notation.html#FourierTransform.fourierInvCLM)
- [Source of `FourierTransform.fourierInvCLM` in Mathlib/Analysis/Fourier/Notation.lean](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/Mathlib/Analysis/Fourier/Notation.lean#L198)
- [Mathlib undergraduate list: Distribution calculus › Tempered distributions](https://github.com/leanprover-community/mathlib4/blob/15cf10d19dfd4cdee9602318e271fa3ce99c454d/docs/undergrad.yaml#L622)
