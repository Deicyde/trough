---
declaration: theorem
origin: cited
lean: TauCeti.fderiv_fderiv_norm_sq_sub_comp_add_I_smul
statement: formalized
proof: formalized
---

# The complex Hessian identity for squared distance

For a holomorphic `C²` map, the sum
of the real Hessian on `v` and `I • v` is four times the squared norm of the complex derivative.
The identity holds at every point; at a critical point it is the intrinsic Hessian identity used
in the squared-distance Morse-index estimate.

```lean
TauCeti.fderiv_fderiv_norm_sq_sub_comp_add_I_smul.{u_1, u_2} {V : Type u_1} {E : Type u_2}
  [NormedAddCommGroup V] [NormedSpace ℂ V] [NormedAddCommGroup E] [InnerProductSpace ℂ E]
  {i : V → E} {a : E} {x : V} (hi : ContDiffAt ℂ 2 i x) (v : V) :
  ((fderiv ℝ (fderiv ℝ fun y => ‖i y - a‖ ^ 2) x) v) v +
      ((fderiv ℝ (fderiv ℝ fun y => ‖i y - a‖ ^ 2) x) (Complex.I • v)) (Complex.I • v) =
    4 * ‖(fderiv ℂ i x) v‖ ^ 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.fderiv_fderiv_norm_sq_sub_comp_add_I_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/SquaredDistance.html#TauCeti.fderiv_fderiv_norm_sq_sub_comp_add_I_smul).

## Sources

- [Tau Ceti documentation: `TauCeti.fderiv_fderiv_norm_sq_sub_comp_add_I_smul`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/SquaredDistance.html#TauCeti.fderiv_fderiv_norm_sq_sub_comp_add_I_smul)
- [Source of `TauCeti.fderiv_fderiv_norm_sq_sub_comp_add_I_smul` in TauCeti/Analysis/InnerProductSpace/SquaredDistance.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/InnerProductSpace/SquaredDistance.lean#L138)
- [Tau Ceti roadmap status: Complex Morse theory, affine topology and weak Lefschetz](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/AffineMorseLefschetz/STATUS.md)
