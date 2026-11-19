---
declaration: theorem
origin: cited
lean: TauCeti.ParabolicC2HolderSpace.isInvertible_euclideanParabolicOperatorL_prod_spatialTraceL
statement: formalized
proof: formalized
---

# The Cauchy problem with variable coefficients is well posed

For `0 < α < 1`, a horizon
`T > 0` and coefficients `aⁱʲ`, `bⁱ`, `c` in `C_b^{α,α/2}(ℝⁿ × [0, T])` with
`lam ‖ξ‖² ≤ ξᵀ a ξ` and `0 < lam`, the initial-data map
`u ↦ (∂ₜu - aⁱʲ ∂ᵢ∂ⱼu - bⁱ ∂ᵢu - c u, u(·, 0))` is an isomorphism of Banach spaces from
`C_b^{2+α,1+α/2}` onto `C_b^{α,α/2} × C_b^{2,α}`. No symmetry of `a` and no sign condition on `c`
is needed.

```lean
TauCeti.ParabolicC2HolderSpace.isInvertible_euclideanParabolicOperatorL_prod_spatialTraceL.{u_1}
  {α : NNReal} {ι : Type u_1} [Fintype ι] [DecidableEq ι] {T : NNReal} (hα₀ : 0 < α) (hα₁ : α < 1)
  (hT : 0 < ↑T) {a : ι → ι → TauCeti.HolderSpace α ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T) ℝ}
  (b : ι → TauCeti.HolderSpace α ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T) ℝ)
  (c : TauCeti.HolderSpace α ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T) ℝ) {lam : ℝ} (hlam : 0 < lam)
  (ha :
    ∀ (p : ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T)) (ξ : EuclideanSpace ℝ ι),
      lam * ‖ξ‖ ^ 2 ≤ (Matrix.of fun i j => ↑(a i j).toHolderSubmodule p).toQuadraticForm' ξ.ofLp) :
  ((TauCeti.ParabolicC2HolderSpace.euclideanParabolicOperatorL ⋯ a b c).prod
      (TauCeti.ParabolicC2HolderSpace.spatialTraceL ⟨0, ⋯⟩)).IsInvertible
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Duhamel's principle in integrated form](../../part-04/pde/part-01/duhamels-principle-in-integrated-form.md)
- [First-order Taylor bound for a Hölder derivative](../../part-03/holder/first-order-taylor-bound-for-a-holder-derivative.md)
- [Hölder bound on the Laplacian of a heat convolution](../../part-04/pde/part-02/holder-bound-on-the-laplacian-of-a-heat-convolut.md)
- [Hölder bounds on the derivatives of a heat convolution](../../part-04/pde/part-02/holder-bounds-on-the-derivatives-of-a-heat-convo.md)
- [The Hölder estimate for the Hessian of the Duhamel potential](../../part-04/pde/part-02/the-holder-estimate-for-the-hessian-of-the-duham.md)
- [The parabolic Hölder estimate of the Cauchy heat potential](../../part-04/pde/part-03/the-parabolic-holder-estimate-of-the-cauchy-heat.md)
- [The temporal Hölder estimate of the Cauchy heat potential](../../part-04/pde/part-04/the-temporal-holder-estimate-of-the-cauchy-heat.md)
- [The value-field parabolic Hölder estimate for the Duhamel potential](../../part-04/pde/part-04/the-value-field-parabolic-holder-estimate-for-th.md)

## Informally uses

- [The global Schauder estimate](../../part-04/pde/part-01/the-global-schauder-estimate.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ParabolicC2HolderSpace.isInvertible_euclideanParabolicOperatorL_prod_spatialTraceL`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Parabolic/Holder/CauchyProblem.html#TauCeti.ParabolicC2HolderSpace.isInvertible_euclideanParabolicOperatorL_prod_spatialTraceL).

## Sources

- [Tau Ceti documentation: `TauCeti.ParabolicC2HolderSpace.isInvertible_euclideanParabolicOperatorL_prod_spatialTraceL`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Parabolic/Holder/CauchyProblem.html#TauCeti.ParabolicC2HolderSpace.isInvertible_euclideanParabolicOperatorL_prod_spatialTraceL)
- [Source of `TauCeti.ParabolicC2HolderSpace.isInvertible_euclideanParabolicOperatorL_prod_spatialTraceL` in TauCeti/Analysis/PDE/Parabolic/Holder/CauchyProblem.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Parabolic/Holder/CauchyProblem.lean#L222)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/PDE/STATUS.md)
