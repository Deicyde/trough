---
declaration: theorem
origin: cited
lean: TauCeti.sq_le_mul_one_add_div_pow_of_sq_le_mul_sub
statement: formalized
proof: formalized
---

# Discrete Grönwall bound under coercivity

Let `D n ≥ 0` with `D 0 = 0` grow by steps
`D (n + 1) ≤ D n + d n` whose squared lengths are paid for by an energy `e`,
`d n ² ≤ 2τ (e n - e (n + 1))`, and let the energy satisfy the coercivity bound
`2τ' (A - e n) ≤ D n ²`, where `4τ ≤ τ'`. Then `D n ² ≤ 2τ' (e 0 - A) (1 + 8τ / τ')ⁿ`.

With `c = τ + τ' / 4`, the quantity `N n = D n ² + 2c (e n - A)` dominates `D n ² / 2` by the
coercivity bound, and grows at most by the factor `1 + 8τ / τ'` per step by the triangle
inequality, Young's inequality and the energy decrease along a step.

```lean
TauCeti.sq_le_mul_one_add_div_pow_of_sq_le_mul_sub {D d e : ℕ → ℝ} {τ τ' A : ℝ} (hτ : 0 < τ)
  (hττ' : 4 * τ ≤ τ') (hD0 : D 0 = 0) (hD : ∀ (n : ℕ), 0 ≤ D n)
  (htri : ∀ (n : ℕ), D (n + 1) ≤ D n + d n) (hstep : ∀ (n : ℕ), d n ^ 2 ≤ 2 * τ * (e n - e (n + 1)))
  (hcoer : ∀ (n : ℕ), 2 * τ' * (A - e n) ≤ D n ^ 2) (n : ℕ) :
  D n ^ 2 ≤ 2 * τ' * (e 0 - A) * (1 + 8 * τ / τ') ^ n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.sq_le_mul_one_add_div_pow_of_sq_le_mul_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecificLimits/DiscreteGronwall.html#TauCeti.sq_le_mul_one_add_div_pow_of_sq_le_mul_sub).

## Sources

- [Tau Ceti documentation: `TauCeti.sq_le_mul_one_add_div_pow_of_sq_le_mul_sub`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecificLimits/DiscreteGronwall.html#TauCeti.sq_le_mul_one_add_div_pow_of_sq_le_mul_sub)
- [Source of `TauCeti.sq_le_mul_one_add_div_pow_of_sq_le_mul_sub` in TauCeti/Analysis/SpecificLimits/DiscreteGronwall.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/SpecificLimits/DiscreteGronwall.lean#L59)
