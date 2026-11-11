---
declaration: theorem
origin: cited
lean: TauCeti.abs_sub_taylorWithinEval_le
statement: formalized
proof: formalized
---

# Taylor's theorem with a bounded remainder

If `f` is `C^(n+1)` near each point between
`x₀` and `x`, including the endpoints, and its `(n+1)`st derivative is bounded in absolute
value by `M` strictly between `x₀` and `x`, then its Taylor
polynomial of order `n` about `x₀` approximates `f x` with error at most
`M * |x - x₀|^(n+1) / (n+1)!`.

```lean
TauCeti.abs_sub_taylorWithinEval_le {f : ℝ → ℝ} {n : ℕ} {M x₀ x : ℝ}
  (hf : ∀ t ∈ Set.uIcc x₀ x, ContDiffAt ℝ (↑n + 1) f t)
  (hM : ∀ t ∈ Set.uIoo x₀ x, |iteratedDeriv (n + 1) f t| ≤ M) :
  |f x - taylorWithinEval f n Set.univ x₀ x| ≤ M * |x - x₀| ^ (n + 1) / ↑(n + 1).factorial
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.abs_sub_taylorWithinEval_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Taylor/Basic.html#TauCeti.abs_sub_taylorWithinEval_le).

## Sources

- [Tau Ceti documentation: `TauCeti.abs_sub_taylorWithinEval_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Taylor/Basic.html#TauCeti.abs_sub_taylorWithinEval_le)
- [Source of `TauCeti.abs_sub_taylorWithinEval_le` in TauCeti/Analysis/Calculus/Taylor/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/Taylor/Basic.lean#L75)
