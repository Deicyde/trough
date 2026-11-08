---
declaration: theorem
origin: cited
lean: ContDiffAt.finrank_ker_fderiv_fderiv_norm_sq_sub_sub_comp
statement: formalized
proof: formalized
---

# Symmetric focal points

For a holomorphic immersion and a normal vector `ν`, the points
`i x + ν` and `i x - ν` have the same focal multiplicity, possibly zero: one is a focal point of
`i` at `x` exactly when the other is, and the Hessians at `x` of squared distance from them have
null spaces of the same dimension.

```lean
ContDiffAt.finrank_ker_fderiv_fderiv_norm_sq_sub_sub_comp.{u_1, u_2} {V : Type u_1} {E : Type u_2}
  [NormedAddCommGroup V] [NormedSpace ℂ V] [FiniteDimensional ℂ V] [NormedAddCommGroup E]
  [InnerProductSpace ℂ E] {i : V → E} {x : V} (hi : ContDiffAt ℂ 2 i x)
  (h : Function.Injective ⇑(fderiv ℂ i x)) {ν : E} (hν : ν ∈ (↑(fderiv ℝ i x)).rangeᗮ) :
  Module.finrank ℝ ↥(↑(fderiv ℝ (fderiv ℝ fun y => ‖i y - (i x - ν)‖ ^ 2) x)).ker =
    Module.finrank ℝ ↥(↑(fderiv ℝ (fderiv ℝ fun y => ‖i y - (i x + ν)‖ ^ 2) x)).ker
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Paired principal curvatures](paired-principal-curvatures.md)
- [TauCeti.shapeOperator](tauceti-shapeoperator.md)

## Lean

Formalized in Tau Ceti as [`ContDiffAt.finrank_ker_fderiv_fderiv_norm_sq_sub_sub_comp`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/ShapeOperator.html#ContDiffAt.finrank_ker_fderiv_fderiv_norm_sq_sub_sub_comp).

## Sources

- [Tau Ceti documentation: `ContDiffAt.finrank_ker_fderiv_fderiv_norm_sq_sub_sub_comp`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/ShapeOperator.html#ContDiffAt.finrank_ker_fderiv_fderiv_norm_sq_sub_sub_comp)
- [Source of `ContDiffAt.finrank_ker_fderiv_fderiv_norm_sq_sub_sub_comp` in TauCeti/Analysis/InnerProductSpace/ShapeOperator.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/ShapeOperator.lean#L319)
- [Tau Ceti roadmap status: Complex Morse theory, affine topology and weak Lefschetz](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AffineMorseLefschetz/STATUS.md)
