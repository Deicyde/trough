---
declaration: theorem
origin: cited
lean: TauCeti.Real.pi_eq_four_mul_agm_mul_agm_div_one_sub_tsum
statement: formalized
proof: formalized
---

# Salamin's formula for complementary moduli

if `x, y > 0` and `x² + y² = 1`, then
`π = 4 M(1, x) M(1, y) / (1 - ∑ₙ 2ⁿ⁺¹ (cₙ₊₁(x)² + cₙ₊₁(y)²))`, where `M` is the AGM and
`cₙ₊₁(x)² = aₙ₊₁² - gₙ₊₁²` is the squared correction of the AGM iteration started at `(1, x)`.
Mathlib's `agmSequences 1 x n` is the pair `(gₙ₊₁, aₙ₊₁)`.

```lean
TauCeti.Real.pi_eq_four_mul_agm_mul_agm_div_one_sub_tsum {x y : NNReal} (hx : 0 < x) (hy : 0 < y)
  (hxy : x ^ 2 + y ^ 2 = 1) :
  Real.pi =
    4 * ↑(NNReal.agm 1 x) * ↑(NNReal.agm 1 y) /
      (1 -
        ∑' (n : ℕ),
          2 ^ (n + 1) *
            (↑(NNReal.agmSequences 1 x n).2 ^ 2 - ↑(NNReal.agmSequences 1 x n).1 ^ 2 +
              (↑(NNReal.agmSequences 1 y n).2 ^ 2 - ↑(NNReal.agmSequences 1 y n).1 ^ 2)))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Gauss's theorem](gausss-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Real.pi_eq_four_mul_agm_mul_agm_div_one_sub_tsum`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/BrentSalamin.html#TauCeti.Real.pi_eq_four_mul_agm_mul_agm_div_one_sub_tsum).

## Sources

- [Tau Ceti documentation: `TauCeti.Real.pi_eq_four_mul_agm_mul_agm_div_one_sub_tsum`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/BrentSalamin.html#TauCeti.Real.pi_eq_four_mul_agm_mul_agm_div_one_sub_tsum)
- [Source of `TauCeti.Real.pi_eq_four_mul_agm_mul_agm_div_one_sub_tsum` in TauCeti/Analysis/SpecialFunctions/EllipticIntegral/BrentSalamin.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/BrentSalamin.lean#L49)
