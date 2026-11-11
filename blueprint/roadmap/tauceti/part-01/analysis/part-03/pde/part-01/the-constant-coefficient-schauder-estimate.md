---
declaration: theorem
origin: cited
lean: TauCeti.ParabolicC2HolderSpace.exists_norm_le_euclideanParabolicOperatorL_const
statement: formalized
proof: formalized
---

# The constant-coefficient Schauder estimate

For `0 < α < 1` and fixed ellipticity bounds
`0 < lam` and `Lam`, there is a constant `C` such that for every matrix `A` with
`lam ‖ξ‖² ≤ ξᵀ A ξ ≤ Lam ‖ξ‖²`, every horizon `T > 0` and every `u ∈ C_b^{2+α,1+α/2}` on
`ℝⁿ × [0, T]`,
`‖u‖ ≤ C (1 + T) (‖∂ₜu - ∑ᵢⱼ Aᵢⱼ ∂ᵢ∂ⱼu‖ + ‖u(·, 0)‖)`.

```lean
TauCeti.ParabolicC2HolderSpace.exists_norm_le_euclideanParabolicOperatorL_const.{u_1} {α : NNReal}
  {ι : Type u_1} [Fintype ι] [DecidableEq ι] (hα₀ : 0 < α) (hα₁ : α < 1) {lam Lam : ℝ}
  (hlam : 0 < lam) :
  ∃ C,
    0 ≤ C ∧
      ∀ (A : Matrix ι ι ℝ),
        (∀ (ξ : EuclideanSpace ℝ ι), lam * ‖ξ‖ ^ 2 ≤ A.toQuadraticForm' ξ.ofLp) →
          (∀ (ξ : EuclideanSpace ℝ ι), A.toQuadraticForm' ξ.ofLp ≤ Lam * ‖ξ‖ ^ 2) →
            ∀ (T : NNReal) (hT : 0 < ↑T)
              (u : TauCeti.ParabolicC2HolderSpace α (EuclideanSpace ℝ ι) ℝ hT),
              ‖u‖ ≤
                C * (1 + ↑T) *
                  (‖(TauCeti.ParabolicC2HolderSpace.euclideanParabolicOperatorL ⋯
                          (fun i j => TauCeti.HolderSpace.const (A i j)) 0 0)
                        u‖ +
                    ‖u.spatialTrace ⟨0, ⋯⟩‖)
```

## Depends on

- [TauCeti.ParabolicC2HolderSpace](../../../part-01/partial-differential-equations/tauceti-parabolicc2holderspace.md)

## Proof depends on

- [Duhamel's principle in integrated form](duhamels-principle-in-integrated-form.md)
- [First-order Taylor bound for a Hölder derivative](../../holder/first-order-taylor-bound-for-a-holder-derivative.md)
- [Hölder bound on the Laplacian of a heat convolution](../part-02/holder-bound-on-the-laplacian-of-a-heat-convolut.md)
- [Hölder bounds on the derivatives of a heat convolution](../part-02/holder-bounds-on-the-derivatives-of-a-heat-convo.md)
- [The Hölder estimate for the Hessian of the Duhamel potential](../part-02/the-holder-estimate-for-the-hessian-of-the-duham.md)
- [The parabolic Hölder estimate of the Cauchy heat potential](../part-02/the-parabolic-holder-estimate-of-the-cauchy-heat.md)
- [The temporal Hölder estimate of the Cauchy heat potential](../part-02/the-temporal-holder-estimate-of-the-cauchy-heat.md)
- [The value-field parabolic Hölder estimate for the Duhamel potential](../part-03/the-value-field-parabolic-holder-estimate-for-th.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ParabolicC2HolderSpace.exists_norm_le_euclideanParabolicOperatorL_const`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Parabolic/Holder/ConstantCoefficient/CauchyProblem.html#TauCeti.ParabolicC2HolderSpace.exists_norm_le_euclideanParabolicOperatorL_const).

## Sources

- [Tau Ceti documentation: `TauCeti.ParabolicC2HolderSpace.exists_norm_le_euclideanParabolicOperatorL_const`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Parabolic/Holder/ConstantCoefficient/CauchyProblem.html#TauCeti.ParabolicC2HolderSpace.exists_norm_le_euclideanParabolicOperatorL_const)
- [Source of `TauCeti.ParabolicC2HolderSpace.exists_norm_le_euclideanParabolicOperatorL_const` in TauCeti/Analysis/PDE/Parabolic/Holder/ConstantCoefficient/CauchyProblem.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Parabolic/Holder/ConstantCoefficient/CauchyProblem.lean#L221)
