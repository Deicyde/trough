---
declaration: theorem
origin: cited
lean: TauCeti.Real.pi_eq_four_mul_agm_sq_div_one_sub_tsum
statement: formalized
proof: formalized
---

# The Gauss–Brent–Salamin formula

with the AGM iteration `a₀ = 1`, `g₀ = 1 / √2` and
`cⱼ² = aⱼ² - gⱼ²`, `π = 4 M(1, 1/√2)² / (1 - ∑_{j ≥ 1} 2^(j+1) cⱼ²)`. Mathlib's
`agmSequences 1 (√2)⁻¹ n` is the pair `(gₙ₊₁, aₙ₊₁)`, so the series index is `n = j - 1`.

```lean
TauCeti.Real.pi_eq_four_mul_agm_sq_div_one_sub_tsum :
  Real.pi =
    4 * ↑(NNReal.agm 1 (NNReal.sqrt 2)⁻¹) ^ 2 /
      (1 -
        ∑' (n : ℕ),
          2 ^ (n + 2) *
            (↑(NNReal.agmSequences 1 (NNReal.sqrt 2)⁻¹ n).2 ^ 2 -
              ↑(NNReal.agmSequences 1 (NNReal.sqrt 2)⁻¹ n).1 ^ 2))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Salamin's formula for complementary moduli](salamins-formula-for-complementary-moduli.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Real.pi_eq_four_mul_agm_sq_div_one_sub_tsum`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/BrentSalamin.html#TauCeti.Real.pi_eq_four_mul_agm_sq_div_one_sub_tsum).

## Sources

- [Tau Ceti documentation: `TauCeti.Real.pi_eq_four_mul_agm_sq_div_one_sub_tsum`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/BrentSalamin.html#TauCeti.Real.pi_eq_four_mul_agm_sq_div_one_sub_tsum)
- [Source of `TauCeti.Real.pi_eq_four_mul_agm_sq_div_one_sub_tsum` in TauCeti/Analysis/SpecialFunctions/EllipticIntegral/BrentSalamin.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/BrentSalamin.lean#L105)
- [Tau Ceti roadmap status: Elliptic integrals, the AGM, and Jacobi elliptic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EllipticIntegrals/STATUS.md)
