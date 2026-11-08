---
declaration: theorem
origin: cited
lean: TauCeti.summatory_mul_rpow_neg_le
statement: formalized
proof: formalized
---

# A negative-power Abel bound

Suppose every index has `N`-value at least `1`, and the
partial sums of a real weight `w` are at most `C * t ^ β` on `[1, x]`. Twisting the weight by
`(N i) ^ (-α)` with `α ≥ 0` gives partial sums at most
`C x ^ (β - α) + α C (x ^ (β - α) - 1) / (β - α)`.

For `β > α` this is `O(x ^ (β - α))`, and for `β < α` it is bounded uniformly in `x`. No sign
condition is imposed on `w`: only its partial sums are controlled.

```lean
TauCeti.summatory_mul_rpow_neg_le.{u_1} {ι : Type u_1} (N : ι → ℕ) [Northcott N]
  (hN : ∀ (i : ι), 1 ≤ ↑(N i)) (w : ι → ℝ) {C α β x : ℝ} (hα : 0 ≤ α) (hβα : β ≠ α) (hx : 1 ≤ x)
  (hC : ∀ t ∈ Set.Icc 1 x, TauCeti.summatory N w t ≤ C * t ^ β) :
  TauCeti.summatory N (fun i => w i * ↑(N i) ^ (-α)) x ≤
    C * x ^ (β - α) + α * C * ((x ^ (β - α) - 1) / (β - α))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.summatory_mul_rpow_neg_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/AbelSummation.html#TauCeti.summatory_mul_rpow_neg_le).

## Sources

- [Tau Ceti documentation: `TauCeti.summatory_mul_rpow_neg_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/AbelSummation.html#TauCeti.summatory_mul_rpow_neg_le)
- [Source of `TauCeti.summatory_mul_rpow_neg_le` in TauCeti/NumberTheory/ArithmeticDirichletSeries/AbelSummation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ArithmeticDirichletSeries/AbelSummation.lean#L281)
