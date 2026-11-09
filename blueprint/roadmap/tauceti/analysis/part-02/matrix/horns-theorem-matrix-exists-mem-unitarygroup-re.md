---
declaration: theorem
origin: cited
lean: Matrix.exists_mem_unitaryGroup_re_diag_mul_diagonal_mul_star_eq
statement: formalized
proof: formalized
---

# Horn's theorem (`Matrix.exists_mem_unitaryGroup_re_diag_mul_diagonal_mul_star_eq`)

Every point `d` of the convex hull of the rearrangements of `w` is the
diagonal of `U diag(w) Uᴴ` for some unitary `U`.

```lean
Matrix.exists_mem_unitaryGroup_re_diag_mul_diagonal_mul_star_eq.{u_1, u_2} {𝕜 : Type u_1}
  {ι : Type u_2} [RCLike 𝕜] [Fintype ι] [DecidableEq ι] {w d : ι → ℝ}
  (hd : d ∈ (convexHull ℝ) (Set.range fun σ => w ∘ ⇑σ)) :
  ∃ U ∈ Matrix.unitaryGroup ι 𝕜,
    ∀ (k : ι), RCLike.re (((U * Matrix.diagonal fun i => ↑(w i)) * star U) k k) = d k
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Horn's theorem (`LinearMap.IsSymmetric.exists_orthonormalBasis_re_inner_apply_self_eq_of_mem_convexHull`)](../inner-product-space/part-01/horns-theorem-linearmap-issymmetric-exists-ortho.md)

## Lean

Formalized in Tau Ceti as [`Matrix.exists_mem_unitaryGroup_re_diag_mul_diagonal_mul_star_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/UnitaryGroup/SchurHorn.html#Matrix.exists_mem_unitaryGroup_re_diag_mul_diagonal_mul_star_eq).

## Sources

- [Tau Ceti documentation: `Matrix.exists_mem_unitaryGroup_re_diag_mul_diagonal_mul_star_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/UnitaryGroup/SchurHorn.html#Matrix.exists_mem_unitaryGroup_re_diag_mul_diagonal_mul_star_eq)
- [Source of `Matrix.exists_mem_unitaryGroup_re_diag_mul_diagonal_mul_star_eq` in TauCeti/Analysis/Matrix/UnitaryGroup/SchurHorn.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Matrix/UnitaryGroup/SchurHorn.lean#L146)
