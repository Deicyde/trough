---
declaration: theorem
origin: cited
lean: Real.prod_sin_pi_mul_div
statement: formalized
proof: formalized
---

# Real.prod_sin_pi_mul_div

`∏_{k=1}^{m-1} sin(π k / m) = m / 2^{m-1}`. Empty product when `m = 1`.

```lean
Real.prod_sin_pi_mul_div {m : ℕ} (hm : 0 < m) :
  ∏ k ∈ Finset.Ico 1 m, Real.sin (Real.pi * ↑k / ↑m) = ↑m / 2 ^ (m - 1)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Real.prod_sin_pi_mul_div`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Trigonometric/FiniteProduct.html#Real.prod_sin_pi_mul_div).

## Sources

- [Tau Ceti documentation: `Real.prod_sin_pi_mul_div`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Trigonometric/FiniteProduct.html#Real.prod_sin_pi_mul_div)
- [Source of `Real.prod_sin_pi_mul_div` in TauCeti/Analysis/SpecialFunctions/Trigonometric/FiniteProduct.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/SpecialFunctions/Trigonometric/FiniteProduct.lean#L123)
- [Tau Ceti roadmap status: Airy and Scorer functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/SpecialFunctionsAiry/STATUS.md)
