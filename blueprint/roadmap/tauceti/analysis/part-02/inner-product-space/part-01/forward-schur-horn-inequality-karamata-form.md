---
declaration: theorem
origin: cited
lean: LinearMap.IsSymmetric.sum_map_re_inner_apply_self_le_sum_map_eigenvalues
statement: formalized
proof: formalized
---

# Forward Schur–Horn inequality, Karamata form

If `φ` is convex on a set `s` containing
the eigenvalues of a symmetric operator `T`, then for every orthonormal basis `e`, the sum of
`φ` over the diagonal entries `Re⟪T (e k), e k⟫` is at most the sum of `φ` over the
eigenvalues.

```lean
LinearMap.IsSymmetric.sum_map_re_inner_apply_self_le_sum_map_eigenvalues.{u_1, u_2, u_4}
  {𝕜 : Type u_1} {E : Type u_2} {κ : Type u_4} [RCLike 𝕜] [NormedAddCommGroup E]
  [InnerProductSpace 𝕜 E] [Fintype κ] [FiniteDimensional 𝕜 E] {T : E →ₗ[𝕜] E} {n : ℕ}
  (hT : T.IsSymmetric) (hn : Module.finrank 𝕜 E = n) (e : OrthonormalBasis κ 𝕜 E) {s : Set ℝ}
  {φ : ℝ → ℝ} (hφ : ConvexOn ℝ s φ) (hs : ∀ (i : Fin n), hT.eigenvalues hn i ∈ s) :
  ∑ k, φ (RCLike.re (inner 𝕜 (T (e k)) (e k))) ≤ ∑ i, φ (hT.eigenvalues hn i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.IsSymmetric.sum_map_re_inner_apply_self_le_sum_map_eigenvalues`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/SchurHorn.html#LinearMap.IsSymmetric.sum_map_re_inner_apply_self_le_sum_map_eigenvalues).

## Sources

- [Tau Ceti documentation: `LinearMap.IsSymmetric.sum_map_re_inner_apply_self_le_sum_map_eigenvalues`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/SchurHorn.html#LinearMap.IsSymmetric.sum_map_re_inner_apply_self_le_sum_map_eigenvalues)
- [Source of `LinearMap.IsSymmetric.sum_map_re_inner_apply_self_le_sum_map_eigenvalues` in TauCeti/Analysis/InnerProductSpace/SchurHorn.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/SchurHorn.lean#L169)
