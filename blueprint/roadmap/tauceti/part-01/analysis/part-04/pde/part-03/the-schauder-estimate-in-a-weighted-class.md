---
declaration: theorem
origin: cited
lean: TauCeti.ParabolicC2HolderSpace.exists_norm_le_of_eq_exp_mul, TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_of_support_subset_closedBall, TauCeti.ParabolicC2HolderSpace.exists_norm_le_euclideanParabolicOperatorL_add_of_forall_lt_dist, TauCeti.ParabolicC2HolderSpace.exists_norm_le_of_spatialSecondFDerivL_eq_zero, TauCeti.ParabolicC2HolderSpace.exists_norm_euclideanInitialDataCLE_symm_le, TauCeti.ParabolicC2HolderSpace.exists_norm_euclideanInitialDataCLE_weighted_symm_le
statement: formalized
proof: formalized
---

# The Schauder estimate in a weighted class

For `0 < α < 1`, ellipticity constants
`λ > 0` and `Λ`, a bound `K` on the Hölder norms of the coefficients, a bound `L` on the Hölder
norms of the partial derivatives `∂ᵢℓ` and `∂ᵢ∂ⱼℓ` of the logarithm of the weight, and a bound
`T₀` on the horizon, there is a constant `C` with the following property. On `ℝⁿ × [0, T]`,
`T ≤ T₀`, let `u = exp ℓ * v` with `v ∈ C_b^{2+α,1+α/2}`, and let `u` be a classical solution of
`P u = exp ℓ * g` with `g ∈ C_b^{α,α/2}`, where `P u = ∂ₜu - aⁱʲ ∂ᵢ∂ⱼu - bⁱ ∂ᵢu - c u`. Then
`‖v‖_{2+α,par} ≤ C (‖g‖_{α,par} + ‖v(·, 0)‖_{2,α})`.

```lean
TauCeti.ParabolicC2HolderSpace.exists_norm_le_of_eq_exp_mul.{u_1} {α : NNReal} {ι : Type u_1}
  [Fintype ι] [DecidableEq ι] (hα₀ : 0 < α) (hα₁ : α < 1) {lam Lam : ℝ} (hlam : 0 < lam)
  (K L T₀ : NNReal) :
  ∃ C,
    0 ≤ C ∧
      ∀ (T : NNReal) (hT : 0 < ↑T),
        T ≤ T₀ →
          ∀ (a : ι → ι → TauCeti.HolderSpace α ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T) ℝ)
            (b : ι → TauCeti.HolderSpace α ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T) ℝ)
            (c : TauCeti.HolderSpace α ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T) ℝ),
            (∀ (p : ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T)) (ξ : EuclideanSpace ℝ ι),
                lam * ‖ξ‖ ^ 2 ≤
                  (Matrix.of fun i j => ↑(a i j).toHolderSubmodule p).toQuadraticForm' ξ.ofLp) →
              (∀ (p : ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T)) (ξ : EuclideanSpace ℝ ι),
                  (Matrix.of fun i j => ↑(a i j).toHolderSubmodule p).toQuadraticForm' ξ.ofLp ≤
                    Lam * ‖ξ‖ ^ 2) →
                (∀ (i j : ι), ‖a i j‖ ≤ ↑K) →
                  (∀ (i : ι), ‖b i‖ ≤ ↑K) →
                    ‖c‖ ≤ ↑K →
                      ∀ (dℓ : ι → TauCeti.HolderSpace α (EuclideanSpace ℝ ι) ℝ)
                        (d2ℓ : ι → ι → TauCeti.HolderSpace α (EuclideanSpace ℝ ι) ℝ),
                        (∀ (i : ι), ‖dℓ i‖ ≤ ↑L) →
                          (∀ (i j : ι), ‖d2ℓ i j‖ ≤ ↑L) →
                            ∀ (ℓ : EuclideanSpace ℝ ι → ℝ),
                              ContDiff ℝ 2 ℓ →
                                (∀ (i : ι) (x : EuclideanSpace ℝ ι),
                                    (fderiv ℝ ℓ x) (EuclideanSpace.single i 1) =
                                      ↑(dℓ i).toHolderSubmodule x) →
                                  (∀ (i j : ι) (x : EuclideanSpace ℝ ι),
                                      ((fderiv ℝ (fderiv ℝ ℓ) x) (EuclideanSpace.single i 1))
                                          (EuclideanSpace.single j 1) =
                                        ↑(d2ℓ i j).toHolderSubmodule x) →
                                    ∀
                                      (v :
                                        TauCeti.ParabolicC2HolderSpace α (EuclideanSpace ℝ ι) ℝ hT)
                                      (u : EuclideanSpace ℝ ι → ℝ → ℝ)
                                      (g :
                                        TauCeti.HolderSpace α
                                          ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T) ℝ),
                                      (∀ (y : EuclideanSpace ℝ ι) (s : ↑(Set.Icc 0 ↑T)),
                                          u y ↑s =
                                            Real.exp (ℓ y) *
                                              (TauCeti.ParabolicC2HolderSpace.valueL v)
                                                (TauCeti.ParabolicSpaceTime.slabMk y s)) →
                                        (∀ (x : EuclideanSpace ℝ ι) (t : ↑(Set.Icc 0 ↑T)),
                                            derivWithin (u x) (Set.Icc 0 ↑T) ↑t -
                                                (∑ i,
                                                      ∑ j,
                                                        ↑(a i j).toHolderSubmodule
                                                            (TauCeti.ParabolicSpaceTime.slabMk x
                                                              t) *
                                                          ((fderiv ℝ (fderiv ℝ fun y => u y ↑t) x)
                                                              (EuclideanSpace.single i 1))
                                                            (EuclideanSpace.single j 1) +
                                                    ∑ i,
                                                      ↑(b i).toHolderSubmodule
                                                          (TauCeti.ParabolicSpaceTime.slabMk x t) *
                                                        (fderiv ℝ (fun y => u y ↑t) x)
                                                          (EuclideanSpace.single i 1) +
                                                  ↑c.toHolderSubmodule
                                                      (TauCeti.ParabolicSpaceTime.slabMk x t) *
                                                    u x ↑t) =
                                              Real.exp (ℓ x) *
                                                ↑g.toHolderSubmodule
                                                  (TauCeti.ParabolicSpaceTime.slabMk x t)) →
                                          ‖v‖ ≤ C * (‖g‖ + ‖v.spatialTrace ⟨0, ⋯⟩‖)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Cauchy problem with variable coefficients is well posed](../../../part-02/partial-differential-equations/the-cauchy-problem-with-variable-coefficients-is.md)
- [The constant-coefficient Schauder estimate](../part-01/the-constant-coefficient-schauder-estimate.md)
- [First-order Taylor bound for a Hölder derivative](../../../part-03/holder/first-order-taylor-bound-for-a-holder-derivative.md)
- [Hölder's bound on an average](../../../../measure-theory/integral/part-02/holders-bound-on-an-average.md)

## Informally uses

- [The global Schauder estimate](../part-01/the-global-schauder-estimate.md)
- [Interior Schauder estimate at positive times](../part-02/interior-schauder-estimate-at-positive-times.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ParabolicC2HolderSpace.exists_norm_le_of_eq_exp_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Parabolic/Holder/Weight/Estimate.html#TauCeti.ParabolicC2HolderSpace.exists_norm_le_of_eq_exp_mul).

## Other forms

**Schauder estimate for a Hessian supported in a ball.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_of_support_subset_closedBall`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/CompactSupport.html#TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_of_support_subset_closedBall).

```lean
TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_of_support_subset_closedBall {n : ℕ} {α : NNReal}
  (hα : 0 < α) (hα1 : α < 1) :
  ∃ C,
    0 < C ∧
      ∀ {a : EuclideanSpace ℝ (Fin (n + 1)) → Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ}
        {x₀ : EuclideanSpace ℝ (Fin (n + 1))} {lam Lam : ℝ},
        0 < lam →
          (∀ (ξ : EuclideanSpace ℝ (Fin (n + 1))), lam * ‖ξ‖ ^ 2 ≤ (a x₀).toQuadraticForm' ξ.ofLp) →
            (∀ (ξ : EuclideanSpace ℝ (Fin (n + 1))),
                (a x₀).toQuadraticForm' ξ.ofLp ≤ Lam * ‖ξ‖ ^ 2) →
              ∀ {L K : NNReal} {R r : ℝ},
                0 ≤ R →
                  0 < r →
                    2 * (C * (Lam / lam) ^ (1 + (↑n + 1) / 4 + ↑α / 2)) * (↑n + 1) ^ 2 *
                          (↑L * R ^ ↑α + ↑L * 2 ^ ↑α * r ^ ↑α) ≤
                        lam →
                      (∀ (i j : Fin (n + 1)),
                          HolderOnWith L α (fun x => a x i j) (Metric.closedBall x₀ R)) →
                        ∀ {u : EuclideanSpace ℝ (Fin (n + 1)) → ℝ},
                          ContDiff ℝ 2 u →
                            MemHolder α (iteratedFDeriv ℝ 2 u) →
                              Function.support (iteratedFDeriv ℝ 2 u) ⊆ Metric.closedBall x₀ R →
                                (HolderWith K α fun x =>
                                    ∑ i,
                                      ∑ j,
                                        a x i j •
                                          ((fderiv ℝ (fderiv ℝ u) x) (EuclideanSpace.single i 1))
                                            (EuclideanSpace.single j 1)) →
                                  HolderWith
                                    (2 * (C * (Lam / lam) ^ (1 + (↑n + 1) / 4 + ↑α / 2)) *
                                        (↑K / lam +
                                          ((↑n + 1) ^ 2 * (↑L * 2 ^ ↑α) / lam *
                                                (MeasureTheory.volume (Metric.ball 0 r) ^
                                                    (-2⁻¹)).toReal +
                                              r ^ (-((↑n + 1) / 2 + ↑α))) *
                                            (MeasureTheory.eLpNorm (iteratedFDeriv ℝ 2 u) 2
                                                MeasureTheory.volume).toReal)).toNNReal
                                    α (iteratedFDeriv ℝ 2 u)
```

**The Schauder estimate for maps of small support.** Formalized in Tau Ceti as [`TauCeti.ParabolicC2HolderSpace.exists_norm_le_euclideanParabolicOperatorL_add_of_forall_lt_dist`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Parabolic/Holder/Schauder.html#TauCeti.ParabolicC2HolderSpace.exists_norm_le_euclideanParabolicOperatorL_add_of_forall_lt_dist).

```lean
TauCeti.ParabolicC2HolderSpace.exists_norm_le_euclideanParabolicOperatorL_add_of_forall_lt_dist.{u_1}
  {α : NNReal} {ι : Type u_1} [Fintype ι] [DecidableEq ι] {lam Lam : ℝ} (hα₀ : 0 < α) (hα₁ : α < 1)
  (hlam : 0 < lam) (K T₀ : NNReal) :
  ∃ r₀ > 0,
    ∃ C,
      0 ≤ C ∧
        ∀ (T : NNReal) (hT : 0 < ↑T),
          T ≤ T₀ →
            ∀ (a : ι → ι → TauCeti.HolderSpace α ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T) ℝ)
              (b : ι → TauCeti.HolderSpace α ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T) ℝ)
              (c : TauCeti.HolderSpace α ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T) ℝ),
              (∀ (p : ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T)) (ξ : EuclideanSpace ℝ ι),
                  lam * ‖ξ‖ ^ 2 ≤
                    (Matrix.of fun i j => ↑(a i j).toHolderSubmodule p).toQuadraticForm' ξ.ofLp) →
                (∀ (p : ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T)) (ξ : EuclideanSpace ℝ ι),
                    (Matrix.of fun i j => ↑(a i j).toHolderSubmodule p).toQuadraticForm' ξ.ofLp ≤
                      Lam * ‖ξ‖ ^ 2) →
                  (∀ (i j : ι), ‖a i j‖ ≤ ↑K) →
                    (∀ (i : ι), ‖b i‖ ≤ ↑K) →
                      ‖c‖ ≤ ↑K →
                        ∀ (w : TauCeti.ParabolicC2HolderSpace α (EuclideanSpace ℝ ι) ℝ hT)
                          (p : ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T)) {r : ℝ},
                          0 ≤ r →
                            r ≤ r₀ →
                              (∀ (q : ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T)),
                                  r < dist q p → (TauCeti.ParabolicC2HolderSpace.valueL w) q = 0) →
                                ‖w‖ ≤
                                  C *
                                    (‖(TauCeti.ParabolicC2HolderSpace.euclideanParabolicOperatorL ⋯
                                              a b c)
                                            w‖ +
                                        ‖w.spatialTrace ⟨0, ⋯⟩‖ +
                                      ‖TauCeti.ParabolicC2HolderSpace.valueL w‖)
```

**The Schauder estimate for maps of small support.** Formalized in Tau Ceti as [`TauCeti.ParabolicC2HolderSpace.exists_norm_le_of_spatialSecondFDerivL_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Parabolic/Holder/VariableCoefficient.html#TauCeti.ParabolicC2HolderSpace.exists_norm_le_of_spatialSecondFDerivL_eq_zero).

```lean
TauCeti.ParabolicC2HolderSpace.exists_norm_le_of_spatialSecondFDerivL_eq_zero.{u_1} {α : NNReal}
  {ι : Type u_1} [Fintype ι] [DecidableEq ι] {T : NNReal} (hα₀ : 0 < α) (hα₁ : α < 1) {lam : ℝ}
  (hlam : 0 < lam) (M : ℝ) (hT : 0 < ↑T) :
  ∃ r₀ > 0,
    ∃ C,
      0 ≤ C ∧
        ∀ (a : ι → ι → TauCeti.HolderSpace α ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T) ℝ)
          (b : ι → TauCeti.HolderSpace α ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T) ℝ)
          (c : TauCeti.HolderSpace α ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T) ℝ),
          (∀ (p : ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T)) (ξ : EuclideanSpace ℝ ι),
              lam * ‖ξ‖ ^ 2 ≤
                (Matrix.of fun i j => ↑(a i j).toHolderSubmodule p).toQuadraticForm' ξ.ofLp) →
            (∀ (i j : ι), ‖a i j‖ ≤ M) →
              (∀ (i : ι), ‖b i‖ ≤ M) →
                ‖c‖ ≤ M →
                  ∀ (z₀ : ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T))
                    (u : TauCeti.ParabolicC2HolderSpace α (EuclideanSpace ℝ ι) ℝ hT),
                    (∀ (p : ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T)),
                        r₀ < dist p z₀ →
                          ↑(TauCeti.ParabolicC2HolderSpace.spatialSecondFDerivL u).toHolderSubmodule
                              p =
                            0) →
                      ‖u‖ ≤
                        C *
                          (‖(TauCeti.ParabolicC2HolderSpace.euclideanParabolicOperatorL ⋯ a b c)
                                  u‖ +
                              ‖u.spatialTrace ⟨0, ⋯⟩‖ +
                            ‖TauCeti.ParabolicC2HolderSpace.valueL u‖)
```

**The Schauder estimate for the Cauchy problem.** Formalized in Tau Ceti as [`TauCeti.ParabolicC2HolderSpace.exists_norm_euclideanInitialDataCLE_symm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Parabolic/Holder/Solvability.html#TauCeti.ParabolicC2HolderSpace.exists_norm_euclideanInitialDataCLE_symm_le).

```lean
TauCeti.ParabolicC2HolderSpace.exists_norm_euclideanInitialDataCLE_symm_le.{u_1} {α : NNReal}
  {ι : Type u_1} [Fintype ι] [DecidableEq ι] (hα₀ : 0 < α) (hα₁ : α < 1) {lam : ℝ} (hlam : 0 < lam)
  (K T₀ : NNReal) :
  ∃ C,
    0 ≤ C ∧
      ∀ (T : NNReal) (hT : 0 < ↑T),
        T ≤ T₀ →
          ∀ (a : ι → ι → TauCeti.HolderSpace α ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T) ℝ)
            (b : ι → TauCeti.HolderSpace α ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T) ℝ)
            (c : TauCeti.HolderSpace α ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T) ℝ)
            (ha :
              ∀ (p : ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T)) (ξ : EuclideanSpace ℝ ι),
                lam * ‖ξ‖ ^ 2 ≤
                  (Matrix.of fun i j => ↑(a i j).toHolderSubmodule p).toQuadraticForm' ξ.ofLp),
            (∀ (i j : ι), ‖a i j‖ ≤ ↑K) →
              (∀ (i : ι), ‖b i‖ ≤ ↑K) →
                ‖c‖ ≤ ↑K →
                  ‖↑(TauCeti.ParabolicC2HolderSpace.euclideanInitialDataCLE hα₀ hα₁ hT a b c
                            ⋯).symm‖ ≤
                    C
```

**The Schauder estimate for the weighted Cauchy problem.** Formalized in Tau Ceti as [`TauCeti.ParabolicC2HolderSpace.exists_norm_euclideanInitialDataCLE_weighted_symm_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Parabolic/Holder/Weight/Solvability.html#TauCeti.ParabolicC2HolderSpace.exists_norm_euclideanInitialDataCLE_weighted_symm_le).

```lean
TauCeti.ParabolicC2HolderSpace.exists_norm_euclideanInitialDataCLE_weighted_symm_le.{u_1}
  {α : NNReal} {ι : Type u_1} [Fintype ι] [DecidableEq ι] (hα₀ : 0 < α) (hα₁ : α < 1) {lam : ℝ}
  (hlam : 0 < lam) (K L T₀ : NNReal) :
  ∃ C,
    0 ≤ C ∧
      ∀ (T : NNReal) (hT : 0 < ↑T),
        T ≤ T₀ →
          ∀ (a : ι → ι → TauCeti.HolderSpace α ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T) ℝ)
            (b : ι → TauCeti.HolderSpace α ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T) ℝ)
            (c : TauCeti.HolderSpace α ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T) ℝ)
            (dℓ : ι → TauCeti.HolderSpace α (EuclideanSpace ℝ ι) ℝ)
            (d2ℓ : ι → ι → TauCeti.HolderSpace α (EuclideanSpace ℝ ι) ℝ)
            (ha :
              ∀ (p : ↑(TauCeti.ParabolicSpaceTime.slab 0 ↑T)) (ξ : EuclideanSpace ℝ ι),
                lam * ‖ξ‖ ^ 2 ≤
                  (Matrix.of fun i j => ↑(a i j).toHolderSubmodule p).toQuadraticForm' ξ.ofLp),
            (∀ (i j : ι), ‖a i j‖ ≤ ↑K) →
              (∀ (i : ι), ‖b i‖ ≤ ↑K) →
                ‖c‖ ≤ ↑K →
                  (∀ (i : ι), ‖dℓ i‖ ≤ ↑L) →
                    (∀ (i j : ι), ‖d2ℓ i j‖ ≤ ↑L) →
                      ‖↑(TauCeti.ParabolicC2HolderSpace.euclideanInitialDataCLE hα₀ hα₁ hT a
                                (TauCeti.ParabolicC2HolderSpace.euclideanWeightedFirstOrderCoeff a b
                                  dℓ)
                                (TauCeti.ParabolicC2HolderSpace.euclideanWeightedZerothOrderCoeff a
                                  b c dℓ d2ℓ)
                                ⋯).symm‖ ≤
                        C
```

## Sources

- [Tau Ceti documentation: `TauCeti.ParabolicC2HolderSpace.exists_norm_le_of_eq_exp_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Parabolic/Holder/Weight/Estimate.html#TauCeti.ParabolicC2HolderSpace.exists_norm_le_of_eq_exp_mul)
- [Source of `TauCeti.ParabolicC2HolderSpace.exists_norm_le_of_eq_exp_mul` in TauCeti/Analysis/PDE/Parabolic/Holder/Weight/Estimate.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Parabolic/Holder/Weight/Estimate.lean#L81)
