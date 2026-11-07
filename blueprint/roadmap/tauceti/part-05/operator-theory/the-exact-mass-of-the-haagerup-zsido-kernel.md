---
declaration: theorem
origin: cited
lean: TauCeti.HaagerupZsido.integral_norm_reciprocalKernel
statement: formalized
proof: formalized
---

# The exact mass of the Haagerup–Zsidó kernel

`∫_ℝ ‖k(t)‖ dt = π / 2`.

```lean
TauCeti.HaagerupZsido.integral_norm_reciprocalKernel :
  ∫ (t : ℝ), ‖TauCeti.HaagerupZsido.reciprocalKernel t‖ = Real.pi / 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HaagerupZsido.integral_norm_reciprocalKernel`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/HaagerupZsido/Mass.html#TauCeti.HaagerupZsido.integral_norm_reciprocalKernel).

## Sources

- [Tau Ceti documentation: `TauCeti.HaagerupZsido.integral_norm_reciprocalKernel`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/HaagerupZsido/Mass.html#TauCeti.HaagerupZsido.integral_norm_reciprocalKernel)
- [Source of `TauCeti.HaagerupZsido.integral_norm_reciprocalKernel` in TauCeti/Analysis/Fourier/HaagerupZsido/Mass.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Fourier/HaagerupZsido/Mass.lean#L133)
- [Tau Ceti roadmap status: Operator theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OperatorTheory/STATUS.md)
