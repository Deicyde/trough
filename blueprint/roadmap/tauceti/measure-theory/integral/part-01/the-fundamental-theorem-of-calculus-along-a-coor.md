---
declaration: theorem
origin: cited
lean: ContDiffOn.integral_fderivWithin_fullSimplex
statement: formalized
proof: formalized
---

# The fundamental theorem of calculus along a coordinate of the standard simplex

For a
function `g` that is `C¹` on `Δᵖ⁺¹`, the integral over `Δᵖ⁺¹` of its partial derivative in the
direction `e_j` is the integral over `Δᵖ` of the difference of its values at the points of the faces
`∑ xᵢ = 1` and `x_j = 0` whose other coordinates are given by `y ∈ Δᵖ`.

```lean
ContDiffOn.integral_fderivWithin_fullSimplex.{u_1} {F : Type u_1} [NormedAddCommGroup F]
  [NormedSpace ℝ F] [CompleteSpace F] {p : ℕ} {g : EuclideanSpace ℝ (Fin (p + 1)) → F}
  (hg : ContDiffOn ℝ 1 g (TauCeti.fullSimplex (p + 1))) (j : Fin (p + 1)) :
  ∫ (x : EuclideanSpace ℝ (Fin (p + 1))) in TauCeti.fullSimplex (p + 1),
      (fderivWithin ℝ g (TauCeti.fullSimplex (p + 1)) x) (EuclideanSpace.single j 1) =
    ∫ (y : EuclideanSpace ℝ (Fin p)) in TauCeti.fullSimplex p,
      g (WithLp.toLp 2 (j.insertNth (1 - ∑ k, y.ofLp k) y.ofLp)) -
        g (WithLp.toLp 2 (j.insertNth 0 y.ofLp))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContDiffOn.integral_fderivWithin_fullSimplex`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/FullSimplex.html#ContDiffOn.integral_fderivWithin_fullSimplex).

## Sources

- [Tau Ceti documentation: `ContDiffOn.integral_fderivWithin_fullSimplex`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Integral/FullSimplex.html#ContDiffOn.integral_fderivWithin_fullSimplex)
- [Source of `ContDiffOn.integral_fderivWithin_fullSimplex` in TauCeti/MeasureTheory/Integral/FullSimplex.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/MeasureTheory/Integral/FullSimplex.lean#L102)
