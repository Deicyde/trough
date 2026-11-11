---
declaration: theorem
origin: cited
lean: LinearMap.IsSymmetric.re_trace_comp_le_sum_eigenvalues_mul_eigenvalues
statement: formalized
proof: formalized
---

# The von Neumann trace inequality

For symmetric `T` and `S` with eigenvalues listed in
decreasing order, `Re tr (T S) ≤ ∑ᵢ λᵢ(T) λᵢ(S)`.

```lean
LinearMap.IsSymmetric.re_trace_comp_le_sum_eigenvalues_mul_eigenvalues.{u_1, u_2} {𝕜 : Type u_1}
  {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E]
  {T S : E →ₗ[𝕜] E} {n : ℕ} (hT : T.IsSymmetric) (hS : S.IsSymmetric)
  (hn : Module.finrank 𝕜 E = n) :
  RCLike.re ((LinearMap.trace 𝕜 E) (T ∘ₗ S)) ≤ ∑ i, hT.eigenvalues hn i * hS.eigenvalues hn i
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.IsSymmetric.re_trace_comp_le_sum_eigenvalues_mul_eigenvalues`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/HoffmanWielandt/Basic.html#LinearMap.IsSymmetric.re_trace_comp_le_sum_eigenvalues_mul_eigenvalues).

## Sources

- [Tau Ceti documentation: `LinearMap.IsSymmetric.re_trace_comp_le_sum_eigenvalues_mul_eigenvalues`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/HoffmanWielandt/Basic.html#LinearMap.IsSymmetric.re_trace_comp_le_sum_eigenvalues_mul_eigenvalues)
- [Source of `LinearMap.IsSymmetric.re_trace_comp_le_sum_eigenvalues_mul_eigenvalues` in TauCeti/Analysis/InnerProductSpace/HoffmanWielandt/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/HoffmanWielandt/Basic.lean#L76)
