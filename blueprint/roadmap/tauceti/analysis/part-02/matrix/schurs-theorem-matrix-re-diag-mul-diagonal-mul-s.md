---
declaration: theorem
origin: cited
lean: Matrix.re_diag_mul_diagonal_mul_star_mem_convexHull, lp.tendsto_of_tendsto_toWeakSpace_one
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

## Other forms

**Schur's theorem.** Formalized in Tau Ceti as [`lp.tendsto_of_tendsto_toWeakSpace_one`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Lp/Schur.html#lp.tendsto_of_tendsto_toWeakSpace_one).

```lean
lp.tendsto_of_tendsto_toWeakSpace_one.{u_1, u_2, u_3} {𝕜 : Type u_1} {ι : Type u_2} [RCLike 𝕜]
  {α : Type u_3} {l : Filter α} [l.IsCountablyGenerated] {x : α → ↥(lp (fun x => 𝕜) 1)}
  {y : ↥(lp (fun x => 𝕜) 1)}
  (hx :
    Filter.Tendsto (fun n => (toWeakSpace 𝕜 ↥(lp (fun x => 𝕜) 1)) (x n)) l
      (nhds ((toWeakSpace 𝕜 ↥(lp (fun x => 𝕜) 1)) y))) :
  Filter.Tendsto x l (nhds y)
```

## Sources

- [Tau Ceti documentation: `Matrix.re_diag_mul_diagonal_mul_star_mem_convexHull`](https://taucetiproject.org/docs/TauCeti/Analysis/Matrix/UnitaryGroup/SchurHorn.html#Matrix.re_diag_mul_diagonal_mul_star_mem_convexHull)
- [Source of `Matrix.re_diag_mul_diagonal_mul_star_mem_convexHull` in TauCeti/Analysis/Matrix/UnitaryGroup/SchurHorn.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Matrix/UnitaryGroup/SchurHorn.lean#L134)
