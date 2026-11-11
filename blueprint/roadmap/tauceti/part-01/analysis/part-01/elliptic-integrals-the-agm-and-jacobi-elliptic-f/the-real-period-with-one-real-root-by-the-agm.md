---
declaration: theorem
origin: cited
lean: WeierstrassCurve.realPeriod_eq_two_mul_pi_div_agm_of_one_real_root
statement: formalized
proof: formalized
---

# The real period with one real root, by the AGM

If
`Ψ₂Sq(x) = 4 (x - e₁)((x - a)² + b²)` with `b ≠ 0`, then
`Ω(W) = 2π / M(2√A, √(2A + 2(e₁ - a)))`, where `A = √((e₁ - a)² + b²)` and `M` is the
arithmetic-geometric mean.

```lean
WeierstrassCurve.realPeriod_eq_two_mul_pi_div_agm_of_one_real_root (W : WeierstrassCurve ℝ)
  {e₁ a b : ℝ} (hb : b ≠ 0)
  (hW : ∀ (x : ℝ), Polynomial.eval x W.Ψ₂Sq = 4 * (x - e₁) * ((x - a) ^ 2 + b ^ 2)) :
  W.realPeriod =
    2 * Real.pi /
      ↑((2 * √√((e₁ - a) ^ 2 + b ^ 2)).toNNReal.agm
          (√(2 * √((e₁ - a) ^ 2 + b ^ 2) + 2 * (e₁ - a))).toNNReal)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Gauss's theorem](gausss-theorem.md)

## Lean

Formalized in Tau Ceti as [`WeierstrassCurve.realPeriod_eq_two_mul_pi_div_agm_of_one_real_root`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/RealPeriod.html#WeierstrassCurve.realPeriod_eq_two_mul_pi_div_agm_of_one_real_root).

## Sources

- [Tau Ceti documentation: `WeierstrassCurve.realPeriod_eq_two_mul_pi_div_agm_of_one_real_root`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/RealPeriod.html#WeierstrassCurve.realPeriod_eq_two_mul_pi_div_agm_of_one_real_root)
- [Source of `WeierstrassCurve.realPeriod_eq_two_mul_pi_div_agm_of_one_real_root` in TauCeti/Analysis/SpecialFunctions/EllipticIntegral/RealPeriod.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/SpecialFunctions/EllipticIntegral/RealPeriod.lean#L125)
- [Tau Ceti roadmap status: Elliptic integrals, the AGM, and Jacobi elliptic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EllipticIntegrals/STATUS.md)
