---
declaration: theorem
origin: cited
lean: Matrix.re_diag_mul_diagonal_mul_star_mem_convexHull
statement: formalized
proof: formalized
---

# Schur's theorem (`Matrix.re_diag_mul_diagonal_mul_star_mem_convexHull`)

For a unitary `U`, the diagonal of `U diag(w) Uᴴ` lies in the convex hull
of the rearrangements `w ∘ σ` of `w`.

```lean
Matrix.re_diag_mul_diagonal_mul_star_mem_convexHull.{u_1, u_2} {𝕜 : Type u_1} {ι : Type u_2}
  [RCLike 𝕜] [Fintype ι] [DecidableEq ι] {U : Matrix ι ι 𝕜} (hU : U ∈ Matrix.unitaryGroup ι 𝕜)
  (w : ι → ℝ) :
  (fun k => RCLike.re (((U * Matrix.diagonal fun i => ↑(w i)) * star U) k k)) ∈
    (convexHull ℝ) (Set.range fun σ => w ∘ ⇑σ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.re_diag_mul_diagonal_mul_star_mem_convexHull`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/UnitaryGroup/SchurHorn.html#Matrix.re_diag_mul_diagonal_mul_star_mem_convexHull).

## Sources

- [Tau Ceti documentation: `Matrix.re_diag_mul_diagonal_mul_star_mem_convexHull`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/UnitaryGroup/SchurHorn.html#Matrix.re_diag_mul_diagonal_mul_star_mem_convexHull)
- [Source of `Matrix.re_diag_mul_diagonal_mul_star_mem_convexHull` in TauCeti/Analysis/Matrix/UnitaryGroup/SchurHorn.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Matrix/UnitaryGroup/SchurHorn.lean#L134)
