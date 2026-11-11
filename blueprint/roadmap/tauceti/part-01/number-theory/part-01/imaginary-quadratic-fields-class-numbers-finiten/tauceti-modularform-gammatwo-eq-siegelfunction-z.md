---
declaration: theorem
origin: cited
lean: TauCeti.ModularForm.gammaTwo_eq_siegelFunction_zero_half
statement: formalized
proof: formalized
---

# TauCeti.ModularForm.gammaTwo_eq_siegelFunction_zero_half

`γ₂ = (g₀¹² + 16) / g₀⁴` for `g₀ = g_{(0, 1/2)}`.

```lean
TauCeti.ModularForm.gammaTwo_eq_siegelFunction_zero_half (τ : UpperHalfPlane) :
  TauCeti.ModularForm.gammaTwo τ =
    (TauCeti.ModularForm.siegelFunction ![0, 1 / 2] ↑τ ^ 12 + 16) /
      TauCeti.ModularForm.siegelFunction ![0, 1 / 2] ↑τ ^ 4
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ModularForm.gammaTwo_eq_siegelFunction_zero_half`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/SiegelFunction/GammaTwo.html#TauCeti.ModularForm.gammaTwo_eq_siegelFunction_zero_half).

## Sources

- [Tau Ceti documentation: `TauCeti.ModularForm.gammaTwo_eq_siegelFunction_zero_half`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/SiegelFunction/GammaTwo.html#TauCeti.ModularForm.gammaTwo_eq_siegelFunction_zero_half)
- [Source of `TauCeti.ModularForm.gammaTwo_eq_siegelFunction_zero_half` in TauCeti/NumberTheory/ModularForms/SiegelFunction/GammaTwo.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ModularForms/SiegelFunction/GammaTwo.lean#L179)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
