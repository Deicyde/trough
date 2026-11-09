---
declaration: theorem
origin: cited
lean: Polynomial.hermiteIntegral_eq_sumIDeriv
statement: formalized
proof: formalized
---

# Hermite's identity

integration by parts evaluates Hermite's integral as
`F_f(z) = exp z * (sumIDeriv f)(0) - (sumIDeriv f)(z)`.

```lean
Polynomial.hermiteIntegral_eq_sumIDeriv (f : Polynomial ℂ) (z : ℂ) :
  f.hermiteIntegral z =
    Complex.exp z * Polynomial.eval 0 (Polynomial.sumIDeriv f) -
      Polynomial.eval z (Polynomial.sumIDeriv f)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Polynomial.hermiteIntegral_eq_sumIDeriv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Lindemann/HermiteIntegral.html#Polynomial.hermiteIntegral_eq_sumIDeriv).

## Sources

- [Tau Ceti documentation: `Polynomial.hermiteIntegral_eq_sumIDeriv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Transcendental/Lindemann/HermiteIntegral.html#Polynomial.hermiteIntegral_eq_sumIDeriv)
- [Source of `Polynomial.hermiteIntegral_eq_sumIDeriv` in TauCeti/NumberTheory/Transcendental/Lindemann/HermiteIntegral.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Transcendental/Lindemann/HermiteIntegral.lean#L86)
