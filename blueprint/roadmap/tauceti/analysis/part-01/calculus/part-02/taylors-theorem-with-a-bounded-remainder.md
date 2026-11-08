---
declaration: theorem
origin: cited
lean: TauCeti.abs_sub_taylorWithinEval_le
statement: formalized
proof: formalized
---

# Taylor's theorem with a bounded remainder

If `f` is `C^(n+1)` and its `(n+1)`st
derivative is bounded in absolute value by `M`, then its Taylor polynomial of order `n` about `x₀`
approximates `f x` with error at most `M * |x - x₀|^(n+1) / (n+1)!`.

```lean
TauCeti.abs_sub_taylorWithinEval_le {f : ℝ → ℝ} {n : ℕ} (hf : ContDiff ℝ (↑n + 1) f) {M : ℝ}
  (hM : ∀ (t : ℝ), |iteratedDeriv (n + 1) f t| ≤ M) (x₀ x : ℝ) :
  |f x - taylorWithinEval f n Set.univ x₀ x| ≤ M * |x - x₀| ^ (n + 1) / ↑(n + 1).factorial
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.abs_sub_taylorWithinEval_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Taylor.html#TauCeti.abs_sub_taylorWithinEval_le).

## Sources

- [Tau Ceti documentation: `TauCeti.abs_sub_taylorWithinEval_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Taylor.html#TauCeti.abs_sub_taylorWithinEval_le)
- [Source of `TauCeti.abs_sub_taylorWithinEval_le` in TauCeti/Analysis/Calculus/Taylor.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Calculus/Taylor.lean#L52)
