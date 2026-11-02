---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: FourierTransform.fourierInvCLM
mathlib_file: Mathlib/Analysis/Fourier/Notation.lean
---

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
- [Source of `FourierTransform.fourierInvCLM` in Mathlib/Analysis/Fourier/Notation.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Fourier/Notation.lean#L190)
- [Mathlib undergraduate list: Distribution calculus › Tempered distributions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L622)
