---
declaration: theorem
origin: cited
lean: LinearMap.IsSymmetric.range_re_inner_apply_self_eq_convexHull_eigenvalues_comp_perm, LinearMap.IsSymmetric.exists_orthonormalBasis_re_inner_apply_self_eq_iff, Matrix.range_re_diag_unitary_mul_diagonal_mul_star, Matrix.IsHermitian.range_re_diag_unitary_mul_mul_star, Matrix.range_re_diag_unitary_mul_diagonal_single_mul_star
statement: formalized
proof: formalized
---

# The Schur–Horn theorem

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

- [Horn's theorem](../part-01/horns-theorem.md)
- [Rado's theorem](../../convex/rados-theorem.md)
- [Schur's theorem (`Matrix.re_diag_mul_diagonal_mul_star_mem_convexHull`)](../../matrix/schurs-theorem-matrix-re-diag-mul-diagonal-mul-s.md)

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

**The Schur–Horn theorem.** Formalized in Tau Ceti as [`Matrix.range_re_diag_unitary_mul_diagonal_mul_star`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/UnitaryGroup/SchurHorn.html#Matrix.range_re_diag_unitary_mul_diagonal_mul_star).

```lean
Matrix.range_re_diag_unitary_mul_diagonal_mul_star.{u_1, u_2} {𝕜 : Type u_1} {ι : Type u_2}
  [RCLike 𝕜] [Fintype ι] [DecidableEq ι] (w : ι → ℝ) :
  (Set.range fun U k => RCLike.re (((↑U * Matrix.diagonal fun i => ↑(w i)) * ↑(star U)) k k)) =
    (convexHull ℝ) (Set.range fun σ => w ∘ ⇑σ)
```

**The Schur–Horn theorem for a Hermitian matrix.** Formalized in Tau Ceti as [`Matrix.IsHermitian.range_re_diag_unitary_mul_mul_star`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/UnitaryGroup/SchurHorn.html#Matrix.IsHermitian.range_re_diag_unitary_mul_mul_star).

```lean
Matrix.IsHermitian.range_re_diag_unitary_mul_mul_star.{u_1, u_2} {𝕜 : Type u_1} {ι : Type u_2}
  [RCLike 𝕜] [Fintype ι] [DecidableEq ι] {A : Matrix ι ι 𝕜} (hA : A.IsHermitian) :
  (Set.range fun U k => RCLike.re ((↑U * A * ↑(star U)) k k)) =
    (convexHull ℝ) (Set.range fun σ => hA.eigenvalues ∘ ⇑σ)
```

**The Schur–Horn theorem in rank at most one.** Formalized in Tau Ceti as [`Matrix.range_re_diag_unitary_mul_diagonal_single_mul_star`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/UnitaryGroup/SchurHorn.html#Matrix.range_re_diag_unitary_mul_diagonal_single_mul_star).

```lean
Matrix.range_re_diag_unitary_mul_diagonal_single_mul_star.{u_1, u_2} {𝕜 : Type u_1} {ι : Type u_2}
  [RCLike 𝕜] [Fintype ι] [DecidableEq ι] (i₀ : ι) (c : ℝ) :
  (Set.range fun U k =>
      RCLike.re (((↑U * Matrix.diagonal fun i => ↑(Pi.single i₀ c i)) * ↑(star U)) k k)) =
    (convexHull ℝ) (Set.range fun i => Pi.single i c)
```

## Sources

- [Tau Ceti documentation: `LinearMap.IsSymmetric.range_re_inner_apply_self_eq_convexHull_eigenvalues_comp_perm`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/SchurHorn.html#LinearMap.IsSymmetric.range_re_inner_apply_self_eq_convexHull_eigenvalues_comp_perm)
- [Source of `LinearMap.IsSymmetric.range_re_inner_apply_self_eq_convexHull_eigenvalues_comp_perm` in TauCeti/Analysis/InnerProductSpace/SchurHorn.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/SchurHorn.lean#L398)
