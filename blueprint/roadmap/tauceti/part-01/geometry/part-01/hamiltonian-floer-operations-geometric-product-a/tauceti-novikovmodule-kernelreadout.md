---
declaration: def
origin: cited
lean: TauCeti.NovikovModule.kernelReadout
statement: formalized
---

# TauCeti.NovikovModule.kernelReadout

The **operator readout** of a functional kernel `φ` on `X ⊗ C₀^∨`, for the degree function
`d₀` on the output generators: the operator kernel `(-1)^(d₀ q) φ(x, q)`. This is a
coefficientwise sign involution, with the sign of the graded bidual map
`p ↦ (f ↦ (-1)^(|p| |f|) f(p))`; when `C₀` is free of finite rank in each degree it induces the
identification `Hom(X ⊗ C₀^∨, R) ≅ Hom(X, C₀)`. The same formula converts operator kernels to
functionals (`NovikovModule.kernelReadout_kernelReadout`).

```lean
TauCeti.NovikovModule.kernelReadout.{u_1, u_2, u_3} {R : Type u_1} {S : Type u_2} {S₀ : Type u_3}
  [CommRing R] (d₀ : S₀ → ℤ) (φ : S → S₀ → R) (x : S) (q : S₀) : R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.NovikovModule.kernelReadout`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovModule/Readout.html#TauCeti.NovikovModule.kernelReadout).

## Sources

- [Tau Ceti documentation: `TauCeti.NovikovModule.kernelReadout`](https://taucetiproject.org/docs/TauCeti/RingTheory/NovikovModule/Readout.html#TauCeti.NovikovModule.kernelReadout)
- [Source of `TauCeti.NovikovModule.kernelReadout` in TauCeti/RingTheory/NovikovModule/Readout.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/NovikovModule/Readout.lean#L106)
- [Tau Ceti roadmap status: Hamiltonian Floer operations: geometric product and multiplicative PSS](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/HamiltonianFloerOperations/STATUS.md)
