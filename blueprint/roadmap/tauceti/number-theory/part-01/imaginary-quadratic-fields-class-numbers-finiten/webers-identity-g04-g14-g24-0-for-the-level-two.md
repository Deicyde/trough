---
declaration: theorem
origin: cited
lean: TauCeti.ModularForm.siegelFunction_pow_four_add_add
statement: formalized
proof: formalized
---

# Weber's identity `g₀⁴ + g₁⁴ + g₂⁴ = 0` for the level-two Siegel functions `g₀ = g_{(0, 1/2)}`, `g₁ = g_{(1/2, 0)}` and `g₂ = g_{(1/2, 1/2)}`

In Weber's notation it reads
`𝔣₁⁸ + 𝔣₂⁸ = 𝔣⁸`.

```lean
TauCeti.ModularForm.siegelFunction_pow_four_add_add (τ : UpperHalfPlane) :
  TauCeti.ModularForm.siegelFunction ![0, 1 / 2] ↑τ ^ 4 +
        TauCeti.ModularForm.siegelFunction ![1 / 2, 0] ↑τ ^ 4 +
      TauCeti.ModularForm.siegelFunction ![1 / 2, 1 / 2] ↑τ ^ 4 =
    0
```

## Depends on

- [The Siegel function `g_r(τ)` attached to `r = (r₁, r₂) ∈ ℝ²`](the-siegel-function-g-r-attached-to-r-r1-r2-r2.md)

## Proof depends on

- [Euler's identity `∏_{n ≥ 1} (1 + qⁿ) ∏_{n ≥ 0} (1 - q^{2n+1}) = 1` for `‖q‖ < 1`](eulers-identity-n-1-1-qn-n-0-1-q-2n-1-1-for-q-1.md)
- [TauCeti.qTheta](tauceti-qtheta.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ModularForm.siegelFunction_pow_four_add_add`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/SiegelFunction/GammaTwo.html#TauCeti.ModularForm.siegelFunction_pow_four_add_add).

## Sources

- [Tau Ceti documentation: `TauCeti.ModularForm.siegelFunction_pow_four_add_add`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ModularForms/SiegelFunction/GammaTwo.html#TauCeti.ModularForm.siegelFunction_pow_four_add_add)
- [Source of `TauCeti.ModularForm.siegelFunction_pow_four_add_add` in TauCeti/NumberTheory/ModularForms/SiegelFunction/GammaTwo.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ModularForms/SiegelFunction/GammaTwo.lean#L157)
