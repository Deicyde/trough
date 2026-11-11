---
declaration: theorem
origin: cited
lean: TauCeti.ModularForm.prod_X_sub_C_siegelFunction_pow_twelve
statement: formalized
proof: formalized
---

# Weber's cubic

The twelfth powers of the level-two Siegel functions `g₀ = g_{(0, 1/2)}`,
`g₁ = g_{(1/2, 0)}` and `g₂ = g_{(1/2, 1/2)}` are the three roots of `(X + 16)³ - j X`.

```lean
TauCeti.ModularForm.prod_X_sub_C_siegelFunction_pow_twelve (τ : UpperHalfPlane) :
  (Polynomial.X - Polynomial.C (TauCeti.ModularForm.siegelFunction ![0, 1 / 2] ↑τ ^ 12)) *
        (Polynomial.X - Polynomial.C (TauCeti.ModularForm.siegelFunction ![1 / 2, 0] ↑τ ^ 12)) *
      (Polynomial.X - Polynomial.C (TauCeti.ModularForm.siegelFunction ![1 / 2, 1 / 2] ↑τ ^ 12)) =
    (Polynomial.X + 16) ^ 3 - Polynomial.C (TauCeti.ModularForm.j τ) * Polynomial.X
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Euler's identity (`TauCeti.tprod_one_add_pow_mul_tprod_one_sub_pow_odd`)](../../../analysis/part-03/special-functions/eulers-identity-tauceti-tprod-one-add-pow-mul-tp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ModularForm.prod_X_sub_C_siegelFunction_pow_twelve`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/SiegelFunction/JInvariant.html#TauCeti.ModularForm.prod_X_sub_C_siegelFunction_pow_twelve).

## Sources

- [Tau Ceti documentation: `TauCeti.ModularForm.prod_X_sub_C_siegelFunction_pow_twelve`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/SiegelFunction/JInvariant.html#TauCeti.ModularForm.prod_X_sub_C_siegelFunction_pow_twelve)
- [Source of `TauCeti.ModularForm.prod_X_sub_C_siegelFunction_pow_twelve` in TauCeti/NumberTheory/ModularForms/SiegelFunction/JInvariant.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ModularForms/SiegelFunction/JInvariant.lean#L221)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
