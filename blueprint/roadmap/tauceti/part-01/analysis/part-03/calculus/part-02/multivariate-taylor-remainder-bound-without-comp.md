---
declaration: theorem
origin: cited
lean: TauCeti.norm_map_add_sub_sum_iteratedFDeriv_le
statement: formalized
proof: formalized
---

# Multivariate Taylor remainder bound without completeness

If `f` is `C^(n + 1)` at each
point of the segment from `x` to `x + y` and `‖D^(n + 1) f‖ ≤ M` on the open segment, then the
order-`n` Taylor polynomial of `f` at `x` approximates `f (x + y)` with error at most
`M * ‖y‖ ^ (n + 1) / (n + 1)!`.

```lean
TauCeti.norm_map_add_sub_sum_iteratedFDeriv_le.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] {f : E → F}
  {x y : E} {n : ℕ} {M : ℝ} (hf : ∀ t ∈ Set.Icc 0 1, ContDiffAt ℝ (↑n + 1) f (x + t • y))
  (hM : ∀ t ∈ Set.Ioo 0 1, ‖iteratedFDeriv ℝ (n + 1) f (x + t • y)‖ ≤ M) :
  ‖f (x + y) - ∑ k ∈ Finset.range (n + 1), (↑k.factorial)⁻¹ • (iteratedFDeriv ℝ k f x) fun x => y‖ ≤
    M * ‖y‖ ^ (n + 1) / ↑(n + 1).factorial
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Taylor's theorem with a bounded remainder](taylors-theorem-with-a-bounded-remainder.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.norm_map_add_sub_sum_iteratedFDeriv_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Taylor/Integral.html#TauCeti.norm_map_add_sub_sum_iteratedFDeriv_le).

## Sources

- [Tau Ceti documentation: `TauCeti.norm_map_add_sub_sum_iteratedFDeriv_le`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/Taylor/Integral.html#TauCeti.norm_map_add_sub_sum_iteratedFDeriv_le)
- [Source of `TauCeti.norm_map_add_sub_sum_iteratedFDeriv_le` in TauCeti/Analysis/Calculus/Taylor/Integral.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Calculus/Taylor/Integral.lean#L110)
