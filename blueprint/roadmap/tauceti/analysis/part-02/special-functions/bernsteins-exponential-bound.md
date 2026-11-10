---
declaration: theorem
origin: cited
lean: Real.exp_le_one_add_add_sq_div_of_le
statement: formalized
proof: formalized
---

# Bernstein's exponential bound

If `x ≤ c` with `0 ≤ c < 3`, then
`exp x ≤ 1 + x + x ^ 2 / (2 * (1 - c / 3))`. Only an upper bound on `x` is needed: negative `x`
are covered by `Real.exp_le_one_add_add_sq_div_two_of_nonpos`.

```lean
Real.exp_le_one_add_add_sq_div_of_le {x c : ℝ} (hxc : x ≤ c) (hc0 : 0 ≤ c) (hc3 : c < 3) :
  Real.exp x ≤ 1 + x + x ^ 2 / (2 * (1 - c / 3))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Real.exp_le_one_add_add_sq_div_of_le`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Exp/QuadraticBound.html#Real.exp_le_one_add_add_sq_div_of_le).

## Sources

- [Tau Ceti documentation: `Real.exp_le_one_add_add_sq_div_of_le`](https://taucetiproject.org/docs/TauCeti/Analysis/SpecialFunctions/Exp/QuadraticBound.html#Real.exp_le_one_add_add_sq_div_of_le)
- [Source of `Real.exp_le_one_add_add_sq_div_of_le` in TauCeti/Analysis/SpecialFunctions/Exp/QuadraticBound.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/SpecialFunctions/Exp/QuadraticBound.lean#L76)
