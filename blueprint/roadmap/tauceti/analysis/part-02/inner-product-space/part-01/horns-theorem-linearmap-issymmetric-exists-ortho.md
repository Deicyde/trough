---
declaration: theorem
origin: cited
lean: LinearMap.IsSymmetric.exists_orthonormalBasis_re_inner_apply_self_eq_of_mem_convexHull
statement: formalized
proof: formalized
---

# Horn's theorem (`LinearMap.IsSymmetric.exists_orthonormalBasis_re_inner_apply_self_eq_of_mem_convexHull`)

Every point `d` of the convex hull of the rearrangements of the spectrum
of a symmetric operator `T` is the diagonal of `T` in some orthonormal basis: there is an
orthonormal basis `e` with `Re⟪T eₖ, eₖ⟫ = dₖ` for every `k`.

```lean
LinearMap.IsSymmetric.exists_orthonormalBasis_re_inner_apply_self_eq_of_mem_convexHull.{u_1, u_2}
  {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  {T : E →ₗ[𝕜] E} {n : ℕ} [FiniteDimensional 𝕜 E] (hT : T.IsSymmetric) (hn : Module.finrank 𝕜 E = n)
  {d : Fin n → ℝ} (hd : d ∈ (convexHull ℝ) (Set.range fun σ => hT.eigenvalues hn ∘ ⇑σ)) :
  ∃ e, ∀ (k : Fin n), RCLike.re (inner 𝕜 (T (e k)) (e k)) = d k
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Rado's theorem](../../convex/rados-theorem.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.IsSymmetric.exists_orthonormalBasis_re_inner_apply_self_eq_of_mem_convexHull`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/SchurHorn.html#LinearMap.IsSymmetric.exists_orthonormalBasis_re_inner_apply_self_eq_of_mem_convexHull).

## Sources

- [Tau Ceti documentation: `LinearMap.IsSymmetric.exists_orthonormalBasis_re_inner_apply_self_eq_of_mem_convexHull`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/SchurHorn.html#LinearMap.IsSymmetric.exists_orthonormalBasis_re_inner_apply_self_eq_of_mem_convexHull)
- [Source of `LinearMap.IsSymmetric.exists_orthonormalBasis_re_inner_apply_self_eq_of_mem_convexHull` in TauCeti/Analysis/InnerProductSpace/SchurHorn.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/SchurHorn.lean#L375)
