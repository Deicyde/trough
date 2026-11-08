---
declaration: theorem
origin: cited
lean: TauCeti.Real.legendreK_eq_pi_div_two_mul_agm
statement: formalized
proof: formalized
---

# Gauss's theorem

for `k ^ 2 < 1`, the complete elliptic integral of the first kind is
`K(k) = π / (2 M(1, k'))`, where `M` is the arithmetic-geometric mean and `k' = √(1 - k²)` is
the complementary modulus.

```lean
TauCeti.Real.legendreK_eq_pi_div_two_mul_agm {k : ℝ} (hk : k ^ 2 < 1) :
  TauCeti.Real.legendreK k = Real.pi / (2 * ↑(NNReal.agm 1 (√(1 - k ^ 2)).toNNReal))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Real.legendreK_eq_pi_div_two_mul_agm`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Gauss.html#TauCeti.Real.legendreK_eq_pi_div_two_mul_agm).

## Sources

- [Tau Ceti documentation: `TauCeti.Real.legendreK_eq_pi_div_two_mul_agm`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Gauss.html#TauCeti.Real.legendreK_eq_pi_div_two_mul_agm)
- [Source of `TauCeti.Real.legendreK_eq_pi_div_two_mul_agm` in TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Gauss.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/Gauss.lean#L60)
