---
declaration: theorem
origin: cited
lean: TauCeti.eq_zero_of_tendsto_cocompact_of_mul_laplacian_nonneg
statement: formalized
proof: formalized
---

# Liouville theorem under the sign condition `f · Δ f ≥ 0`

A `C²` function on a nontrivial
finite-dimensional real inner product space which tends to zero at infinity and satisfies
`0 ≤ f x * Δ f x` everywhere vanishes identically. The sign condition holds for solutions of
`Δ f = c f` with `c ≥ 0`, and for differences of solutions of semilinear equations `Δ u = F(x, u)`
with `F` nondecreasing in `u`.

```lean
TauCeti.eq_zero_of_tendsto_cocompact_of_mul_laplacian_nonneg.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [Nontrivial E] {f : E → ℝ}
  (hf : ContDiff ℝ 2 f) (hsign : ∀ (x : E), 0 ≤ f x * Laplacian.laplacian f x)
  (h : Filter.Tendsto f (Filter.cocompact E) (nhds 0)) : f = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.eq_zero_of_tendsto_cocompact_of_mul_laplacian_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Laplacian/WeakMaximumPrinciple.html#TauCeti.eq_zero_of_tendsto_cocompact_of_mul_laplacian_nonneg).

## Sources

- [Tau Ceti documentation: `TauCeti.eq_zero_of_tendsto_cocompact_of_mul_laplacian_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Laplacian/WeakMaximumPrinciple.html#TauCeti.eq_zero_of_tendsto_cocompact_of_mul_laplacian_nonneg)
- [Source of `TauCeti.eq_zero_of_tendsto_cocompact_of_mul_laplacian_nonneg` in TauCeti/Analysis/InnerProductSpace/Laplacian/WeakMaximumPrinciple.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/Laplacian/WeakMaximumPrinciple.lean#L274)
