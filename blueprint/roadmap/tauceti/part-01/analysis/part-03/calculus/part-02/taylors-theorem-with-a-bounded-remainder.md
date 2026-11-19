---
declaration: theorem
origin: cited
lean: TauCeti.abs_sub_taylorWithinEval_le, ContDiffAt.isBigO_sub_sum_iteratedFDeriv
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

## Informally uses

- [Multivariate Taylor remainder bound without completeness](multivariate-taylor-remainder-bound-without-comp.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.abs_sub_taylorWithinEval_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Taylor/Basic.html#TauCeti.abs_sub_taylorWithinEval_le).

## Other forms

**Taylor's theorem of order `n` with `O(‖x' - x‖ ^ (n + 1))` remainder.** Formalized in Tau Ceti as [`ContDiffAt.isBigO_sub_sum_iteratedFDeriv`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Taylor/Integral.html#ContDiffAt.isBigO_sub_sum_iteratedFDeriv).

```lean
ContDiffAt.isBigO_sub_sum_iteratedFDeriv.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] {f : E → F}
  {x : E} {n : ℕ} (hf : ContDiffAt ℝ (↑n + 1) f x) :
  (fun x' =>
      f x' -
        ∑ k ∈ Finset.range (n + 1),
          (↑k.factorial)⁻¹ • (iteratedFDeriv ℝ k f x) fun x_1 => x' - x) =O[nhds x]
    fun x' => ‖x' - x‖ ^ (n + 1)
```

## Sources

- [Tau Ceti documentation: `TauCeti.abs_sub_taylorWithinEval_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Taylor/Basic.html#TauCeti.abs_sub_taylorWithinEval_le)
- [Source of `TauCeti.abs_sub_taylorWithinEval_le` in TauCeti/Analysis/Calculus/Taylor/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Calculus/Taylor/Basic.lean#L87)
