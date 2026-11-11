---
declaration: theorem
origin: cited
lean: LinearMap.IsSymmetric.range_re_inner_apply_self_eq_convexHull_eigenvalues_comp_perm, LinearMap.IsSymmetric.exists_orthonormalBasis_re_inner_apply_self_eq_iff
statement: formalized
proof: formalized
---

# The Schur–Horn theorem (`LinearMap.IsSymmetric.range_re_inner_apply_self_eq_convexHull_eigenvalues_comp_perm`)

The diagonals `(Re⟪T eₖ, eₖ⟫)ₖ` of a symmetric operator `T` in
the orthonormal bases `e` indexed by `Fin n` form exactly the convex hull of the rearrangements of
the spectrum of `T`.

```lean
LinearMap.IsSymmetric.range_re_inner_apply_self_eq_convexHull_eigenvalues_comp_perm.{u_1, u_2}
  {𝕜 : Type u_1} {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E]
  {T : E →ₗ[𝕜] E} {n : ℕ} [FiniteDimensional 𝕜 E] (hT : T.IsSymmetric)
  (hn : Module.finrank 𝕜 E = n) :
  (Set.range fun e k => RCLike.re (inner 𝕜 (T (e k)) (e k))) =
    (convexHull ℝ) (Set.range fun σ => hT.eigenvalues hn ∘ ⇑σ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Horn's theorem (`LinearMap.IsSymmetric.exists_orthonormalBasis_re_inner_apply_self_eq_of_mem_convexHull`)](../part-01/horns-theorem-linearmap-issymmetric-exists-ortho.md)
- [Rado's theorem](../../../part-02/convex/rados-theorem.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.IsSymmetric.range_re_inner_apply_self_eq_convexHull_eigenvalues_comp_perm`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/SchurHorn.html#LinearMap.IsSymmetric.range_re_inner_apply_self_eq_convexHull_eigenvalues_comp_perm).

## Other forms

**The Schur–Horn theorem, majorization form.** Formalized in Tau Ceti as [`LinearMap.IsSymmetric.exists_orthonormalBasis_re_inner_apply_self_eq_iff`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/SchurHorn.html#LinearMap.IsSymmetric.exists_orthonormalBasis_re_inner_apply_self_eq_iff).

```lean
LinearMap.IsSymmetric.exists_orthonormalBasis_re_inner_apply_self_eq_iff.{u_1, u_2} {𝕜 : Type u_1}
  {E : Type u_2} [RCLike 𝕜] [NormedAddCommGroup E] [InnerProductSpace 𝕜 E] {T : E →ₗ[𝕜] E} {n : ℕ}
  [FiniteDimensional 𝕜 E] (hT : T.IsSymmetric) (hn : Module.finrank 𝕜 E = n) {d : Fin n → ℝ} :
  (∃ e, ∀ (k : Fin n), RCLike.re (inner 𝕜 (T (e k)) (e k)) = d k) ↔
    (∀ (k : ℕ),
        TauCeti.prefixSum k (d ∘ ⇑(Tuple.sortDesc d)) ≤ TauCeti.prefixSum k (hT.eigenvalues hn)) ∧
      ∑ i, d i = ∑ i, hT.eigenvalues hn i
```

## Sources

- [Tau Ceti documentation: `LinearMap.IsSymmetric.range_re_inner_apply_self_eq_convexHull_eigenvalues_comp_perm`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/SchurHorn.html#LinearMap.IsSymmetric.range_re_inner_apply_self_eq_convexHull_eigenvalues_comp_perm)
- [Source of `LinearMap.IsSymmetric.range_re_inner_apply_self_eq_convexHull_eigenvalues_comp_perm` in TauCeti/Analysis/InnerProductSpace/SchurHorn.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/InnerProductSpace/SchurHorn.lean#L398)
