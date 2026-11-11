---
declaration: theorem
origin: cited
lean: Polynomial.norm_hermiteIntegral_le
statement: formalized
proof: formalized
---

# Hermite's estimate

if `C` bounds `‖f‖` on the closed disc of radius `‖z‖`, then
`‖F_f(z)‖ ≤ ‖z‖ exp ‖z‖ C`.

```lean
Polynomial.norm_hermiteIntegral_le {f : Polynomial ℂ} {z : ℂ} {C : ℝ}
  (hC : ∀ (u : ℂ), ‖u‖ ≤ ‖z‖ → ‖Polynomial.eval u f‖ ≤ C) :
  ‖f.hermiteIntegral z‖ ≤ ‖z‖ * Real.exp ‖z‖ * C
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Polynomial.norm_hermiteIntegral_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Lindemann/HermiteIntegral.html#Polynomial.norm_hermiteIntegral_le).

## Sources

- [Tau Ceti documentation: `Polynomial.norm_hermiteIntegral_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Lindemann/HermiteIntegral.html#Polynomial.norm_hermiteIntegral_le)
- [Source of `Polynomial.norm_hermiteIntegral_le` in TauCeti/NumberTheory/Transcendental/Lindemann/HermiteIntegral.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/Transcendental/Lindemann/HermiteIntegral.lean#L104)
