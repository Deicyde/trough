---
declaration: theorem
origin: cited
lean: Matrix.range_re_diag_unitary_mul_diagonal_mul_star, Matrix.IsHermitian.range_re_diag_unitary_mul_mul_star, Matrix.range_re_diag_unitary_mul_diagonal_single_mul_star
statement: formalized
proof: formalized
---

# The Schur–Horn theorem (`Matrix.range_re_diag_unitary_mul_diagonal_mul_star`)

The diagonals of the matrices `U diag(w) Uᴴ`, for `U` unitary,
form exactly the convex hull of the rearrangements of `w`. In the language of moment maps: the
image of the unitary orbit of `diag(w)` under the moment map of the diagonal torus is the
permutohedron of `w`.

```lean
Matrix.range_re_diag_unitary_mul_diagonal_mul_star.{u_1, u_2} {𝕜 : Type u_1} {ι : Type u_2}
  [RCLike 𝕜] [Fintype ι] [DecidableEq ι] (w : ι → ℝ) :
  (Set.range fun U k => RCLike.re (((↑U * Matrix.diagonal fun i => ↑(w i)) * ↑(star U)) k k)) =
    (convexHull ℝ) (Set.range fun σ => w ∘ ⇑σ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Horn's theorem (`Matrix.exists_mem_unitaryGroup_re_diag_mul_diagonal_mul_star_eq`)](horns-theorem-matrix-exists-mem-unitarygroup-re.md)
- [Schur's theorem (`Matrix.re_diag_mul_diagonal_mul_star_mem_convexHull`)](schurs-theorem-matrix-re-diag-mul-diagonal-mul-s.md)

## Lean

Formalized in Tau Ceti as [`Matrix.range_re_diag_unitary_mul_diagonal_mul_star`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/UnitaryGroup/SchurHorn.html#Matrix.range_re_diag_unitary_mul_diagonal_mul_star).

## Other forms

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

- [Tau Ceti documentation: `Matrix.range_re_diag_unitary_mul_diagonal_mul_star`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/UnitaryGroup/SchurHorn.html#Matrix.range_re_diag_unitary_mul_diagonal_mul_star)
- [Source of `Matrix.range_re_diag_unitary_mul_diagonal_mul_star` in TauCeti/Analysis/Matrix/UnitaryGroup/SchurHorn.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Matrix/UnitaryGroup/SchurHorn.lean#L194)
