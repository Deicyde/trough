---
declaration: theorem
origin: cited
lean: TauCeti.existsUnique_toeplitz_eq_iff_adjoint_comp_comp_eq
statement: formalized
proof: formalized
---

# Brown–Halmos theorem

A bounded operator `T` on Hardy space is a Toeplitz operator `T_a`
for a unique essentially bounded symbol `a` if and only if `S† T S = T`, where `S = T_z` is the
forward shift.

```lean
TauCeti.existsUnique_toeplitz_eq_iff_adjoint_comp_comp_eq
  (T : TauCeti.HardySpace →L[ℂ] TauCeti.HardySpace) :
  (∃! a, TauCeti.toeplitz a = T) ↔
    ContinuousLinearMap.adjoint (TauCeti.toeplitz (fourierLp ⊤ 1)) ∘SL
        T ∘SL TauCeti.toeplitz (fourierLp ⊤ 1) =
      T
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.existsUnique_toeplitz_eq_iff_adjoint_comp_comp_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Hardy/BrownHalmos.html#TauCeti.existsUnique_toeplitz_eq_iff_adjoint_comp_comp_eq).

## Sources

- [Tau Ceti documentation: `TauCeti.existsUnique_toeplitz_eq_iff_adjoint_comp_comp_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Fourier/Hardy/BrownHalmos.html#TauCeti.existsUnique_toeplitz_eq_iff_adjoint_comp_comp_eq)
- [Source of `TauCeti.existsUnique_toeplitz_eq_iff_adjoint_comp_comp_eq` in TauCeti/Analysis/Fourier/Hardy/BrownHalmos.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Fourier/Hardy/BrownHalmos.lean#L243)
