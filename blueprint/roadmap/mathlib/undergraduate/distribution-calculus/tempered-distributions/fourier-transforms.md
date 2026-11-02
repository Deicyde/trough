---
declaration: def
origin: cited
mathlib: true
mathlib_declaration: FourierTransform.fourierCLM
mathlib_file: Mathlib/Analysis/Fourier/Notation.lean
---

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
- [Source of `FourierTransform.fourierCLM` in Mathlib/Analysis/Fourier/Notation.lean](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/Mathlib/Analysis/Fourier/Notation.lean#L164)
- [Mathlib undergraduate list: Distribution calculus › Tempered distributions](https://github.com/leanprover-community/mathlib4/blob/1b1ccf4b088b32fa3f23f2de1127433254a81e1e/docs/undergrad.yaml#L621)
