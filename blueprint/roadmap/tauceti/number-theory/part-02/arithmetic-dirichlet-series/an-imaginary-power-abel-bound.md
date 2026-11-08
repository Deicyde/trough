---
declaration: theorem
origin: cited
lean: TauCeti.norm_summatory_mul_cpow_le_of_summatory_le
statement: formalized
proof: formalized
---

# An imaginary-power Abel bound

Suppose every index has `N`-value at least `1`, and the
partial sums of `w` are bounded by `C * t ^ θ` on `[1, x]` for a positive exponent `θ`. Twisting
the weight by `(N i) ^ (-z)` with `Re z = 0` preserves that exponent, at the cost of the explicit
factor `1 + ‖z‖ / θ`.

```lean
TauCeti.norm_summatory_mul_cpow_le_of_summatory_le.{u_1} {ι : Type u_1} (N : ι → ℕ) [Northcott N]
  (hN : ∀ (i : ι), 1 ≤ ↑(N i)) (w : ι → ℂ) {C θ x : ℝ} (hx : 1 ≤ x) (hθ : 0 < θ) (z : ℂ)
  (hz : z.re = 0) (hC : ∀ t ∈ Set.Icc 1 x, ‖TauCeti.summatory N w t‖ ≤ C * t ^ θ) :
  ‖TauCeti.summatory N (fun i => w i * ↑(N i) ^ (-z)) x‖ ≤ C * (1 + ‖z‖ / θ) * x ^ θ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.norm_summatory_mul_cpow_le_of_summatory_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/AbelSummation.html#TauCeti.norm_summatory_mul_cpow_le_of_summatory_le).

## Sources

- [Tau Ceti documentation: `TauCeti.norm_summatory_mul_cpow_le_of_summatory_le`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ArithmeticDirichletSeries/AbelSummation.html#TauCeti.norm_summatory_mul_cpow_le_of_summatory_le)
- [Source of `TauCeti.norm_summatory_mul_cpow_le_of_summatory_le` in TauCeti/NumberTheory/ArithmeticDirichletSeries/AbelSummation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ArithmeticDirichletSeries/AbelSummation.lean#L237)
