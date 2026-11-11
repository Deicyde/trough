---
declaration: theorem
origin: cited
lean: TauCeti.ModularForm.siegelFunction_pow_four_add_add
statement: formalized
proof: formalized
---

# Weber's identity

**Weber's identity** `g₀⁴ + g₁⁴ + g₂⁴ = 0` for the level-two Siegel functions
`g₀ = g_{(0, 1/2)}`, `g₁ = g_{(1/2, 0)}` and `g₂ = g_{(1/2, 1/2)}`. In Weber's notation it reads
`𝔣₁⁸ + 𝔣₂⁸ = 𝔣⁸`.

```lean
TauCeti.ModularForm.siegelFunction_pow_four_add_add (τ : UpperHalfPlane) :
  TauCeti.ModularForm.siegelFunction ![0, 1 / 2] ↑τ ^ 4 +
        TauCeti.ModularForm.siegelFunction ![1 / 2, 0] ↑τ ^ 4 +
      TauCeti.ModularForm.siegelFunction ![1 / 2, 1 / 2] ↑τ ^ 4 =
    0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Euler's identity (`TauCeti.tprod_one_add_pow_mul_tprod_one_sub_pow_odd`)](../../../analysis/part-03/special-functions/eulers-identity-tauceti-tprod-one-add-pow-mul-tp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ModularForm.siegelFunction_pow_four_add_add`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/SiegelFunction/GammaTwo.html#TauCeti.ModularForm.siegelFunction_pow_four_add_add).

## Sources

- [Tau Ceti documentation: `TauCeti.ModularForm.siegelFunction_pow_four_add_add`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/SiegelFunction/GammaTwo.html#TauCeti.ModularForm.siegelFunction_pow_four_add_add)
- [Source of `TauCeti.ModularForm.siegelFunction_pow_four_add_add` in TauCeti/NumberTheory/ModularForms/SiegelFunction/GammaTwo.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ModularForms/SiegelFunction/GammaTwo.lean#L157)
