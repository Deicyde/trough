---
declaration: theorem
origin: cited
lean: TauCeti.ModularForm.gammaTwo_pow_three
statement: formalized
proof: formalized
---

# `γ₂` is a cube root of `j`

`γ₂³ = j`.

```lean
TauCeti.ModularForm.gammaTwo_pow_three (τ : UpperHalfPlane) :
  TauCeti.ModularForm.gammaTwo τ ^ 3 = TauCeti.ModularForm.j τ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Euler's identity (`TauCeti.tprod_one_add_pow_mul_tprod_one_sub_pow_odd`)](../../../analysis/part-03/special-functions/eulers-identity-tauceti-tprod-one-add-pow-mul-tp.md)
- [TauCeti.ModularForm.gammaTwo_eq_siegelFunction_zero_half](tauceti-modularform-gammatwo-eq-siegelfunction-z.md)
- [Weber's cubic](webers-cubic.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ModularForm.gammaTwo_pow_three`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/SiegelFunction/GammaTwo.html#TauCeti.ModularForm.gammaTwo_pow_three).

## Sources

- [Tau Ceti documentation: `TauCeti.ModularForm.gammaTwo_pow_three`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/SiegelFunction/GammaTwo.html#TauCeti.ModularForm.gammaTwo_pow_three)
- [Source of `TauCeti.ModularForm.gammaTwo_pow_three` in TauCeti/NumberTheory/ModularForms/SiegelFunction/GammaTwo.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ModularForms/SiegelFunction/GammaTwo.lean#L216)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
