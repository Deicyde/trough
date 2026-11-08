---
declaration: theorem
origin: cited
lean: LinearMap.IsSymmetric.sum_re_inner_apply_self_le_sum_eigenvalues
statement: formalized
proof: formalized
---

# Ky Fan's trace inequality

for a symmetric `T` and an orthonormal family `(wᵢ)` with `k`
members, `∑ᵢ re ⟪T wᵢ, wᵢ⟫` is at most the sum `λ₀ + ⋯ + λₖ₋₁` of the `k` largest eigenvalues
of `T`.

```lean
LinearMap.IsSymmetric.sum_re_inner_apply_self_le_sum_eigenvalues.{u_1, u_2, u_6} {𝕜 : Type u_1}
  {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] [FiniteDimensional 𝕜 E]
  {T : E →ₗ[𝕜] E} {n : ℕ} (hT : T.IsSymmetric) (hn : Module.finrank 𝕜 E = n) {ι : Type u_6}
  [Fintype ι] {w : ι → E} (hw : Orthonormal 𝕜 w) :
  ∑ i, RCLike.re (inner 𝕜 (T (w i)) (w i)) ≤ ∑ j with ↑j < Fintype.card ι, hT.eigenvalues hn j
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Abel's inequality, comparison form](../../../../algebra/other-results/abels-inequality-comparison-form.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.IsSymmetric.sum_re_inner_apply_self_le_sum_eigenvalues`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/KyFan.html#LinearMap.IsSymmetric.sum_re_inner_apply_self_le_sum_eigenvalues).

## Sources

- [Tau Ceti documentation: `LinearMap.IsSymmetric.sum_re_inner_apply_self_le_sum_eigenvalues`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/KyFan.html#LinearMap.IsSymmetric.sum_re_inner_apply_self_le_sum_eigenvalues)
- [Source of `LinearMap.IsSymmetric.sum_re_inner_apply_self_le_sum_eigenvalues` in TauCeti/Analysis/InnerProductSpace/KyFan.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/KyFan.lean#L502)
