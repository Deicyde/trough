---
declaration: theorem
origin: cited
lean: TauCeti.ParabolicC2HolderSpace.exists_norm_le_euclideanParabolicOperatorL, TauCeti.PDE.exists_norm_le_of_sum_smul_fderiv_fderiv, TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_and_norm_le_of_sum_smul_fderiv_fderiv, TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_of_holderWith, TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_and_norm_le_of_sum_smul_fderiv_fderiv_add_fderiv_add_mul, TauCeti.ParabolicC2HolderSpace.exists_norm_le_euclideanParabolicOperatorL_add
statement: formalized
proof: formalized
---

# The global Schauder estimate

For `0 < α < 1`, ellipticity constants `λ > 0` and `Λ`, a
bound `K` on the Hölder norms of the coefficients and a bound `T₀` on the horizon, there is a
constant `C` such that on `ℝⁿ × [0, T]`, `T ≤ T₀`, every `u ∈ C_b^{2+α,1+α/2}` satisfies
`‖u‖_{2+α,par} ≤ C (‖P u‖_{α,par} + ‖u(·, 0)‖_{2,α})`,
where `P u = ∂ₜu - aⁱʲ ∂ᵢ∂ⱼu - bⁱ ∂ᵢu - c u`. In particular `u` is determined by `P u` and
`u(·, 0)`, with a bound uniform over the coefficients.

```lean
TauCeti.ParabolicC2HolderSpace.exists_norm_le_euclideanParabolicOperatorL.{u_1} {α : NNReal}
  {ι : Type u_1} [Fintype ι] [DecidableEq ι] {lam Lam : ℝ} (hα₀ : 0 < α) (hα₁ : α < 1)
  (hlam : 0 < lam) (K T₀ : NNReal) :
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
                      ∀ (u : TauCeti.ParabolicC2HolderSpace α (EuclideanSpace ℝ ι) ℝ hT),
                        ‖u‖ ≤
                          C *
                            (‖(TauCeti.ParabolicC2HolderSpace.euclideanParabolicOperatorL ⋯ a b c)
                                  u‖ +
                              ‖u.spatialTrace ⟨0, ⋯⟩‖)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Duhamel's principle in integrated form](duhamels-principle-in-integrated-form.md)
- [First-order Taylor bound for a Hölder derivative](../../../part-03/holder/first-order-taylor-bound-for-a-holder-derivative.md)
- [Hölder bound on the Laplacian of a heat convolution](../part-02/holder-bound-on-the-laplacian-of-a-heat-convolut.md)
- [Hölder bounds on the derivatives of a heat convolution](../part-02/holder-bounds-on-the-derivatives-of-a-heat-convo.md)
- [The Hölder estimate for the Hessian of the Duhamel potential](../part-02/the-holder-estimate-for-the-hessian-of-the-duham.md)
- [The parabolic Hölder estimate of the Cauchy heat potential](../part-03/the-parabolic-holder-estimate-of-the-cauchy-heat.md)
- [Patching local Hölder bounds](../../../part-03/holder/patching-local-holder-bounds.md)
- [The Schauder estimate in a weighted class](../part-03/the-schauder-estimate-in-a-weighted-class.md)
- [The temporal Hölder estimate of the Cauchy heat potential](../part-04/the-temporal-holder-estimate-of-the-cauchy-heat.md)
- [The value-field parabolic Hölder estimate for the Duhamel potential](../part-04/the-value-field-parabolic-holder-estimate-for-th.md)

## Informally uses

- [Interior Schauder estimate at positive times](../part-02/interior-schauder-estimate-at-positive-times.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ParabolicC2HolderSpace.exists_norm_le_euclideanParabolicOperatorL`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Parabolic/Holder/Schauder.html#TauCeti.ParabolicC2HolderSpace.exists_norm_le_euclideanParabolicOperatorL).

## Other forms

**The global Schauder estimate in the `C_b^{2,α}` norm.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_norm_le_of_sum_smul_fderiv_fderiv`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/WholeSpace.html#TauCeti.PDE.exists_norm_le_of_sum_smul_fderiv_fderiv).

```lean
TauCeti.PDE.exists_norm_le_of_sum_smul_fderiv_fderiv {n : ℕ} {α : NNReal} (hα : 0 < α) (hα1 : α < 1)
  (lam Lam : ℝ) (L : NNReal) :
  ∃ C,
    ∀ {a : EuclideanSpace ℝ (Fin (n + 1)) → Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ},
      TauCeti.PDE.UniformlyEllipticOn Set.univ a lam Lam →
        (∀ (i j : Fin (n + 1)), HolderWith L α fun x => a x i j) →
          ∀ (u : TauCeti.CkHolderSpace 2 α (EuclideanSpace ℝ (Fin (n + 1))) ℝ) {N K : NNReal},
            (∀ (x : EuclideanSpace ℝ (Fin (n + 1))), |u x| ≤ ↑N) →
              (HolderWith K α fun x =>
                  ∑ i,
                    ∑ j,
                      a x i j •
                        ((fderiv ℝ (fderiv ℝ ⇑u) x) (EuclideanSpace.single i 1))
                          (EuclideanSpace.single j 1)) →
                ‖u‖ ≤ ↑C * (↑K + ↑N)
```

**The global Schauder estimate on the whole space.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_and_norm_le_of_sum_smul_fderiv_fderiv`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/WholeSpace.html#TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_and_norm_le_of_sum_smul_fderiv_fderiv).

```lean
TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_and_norm_le_of_sum_smul_fderiv_fderiv {n : ℕ}
  {α : NNReal} (hα : 0 < α) (hα1 : α < 1) (lam Lam : ℝ) (L : NNReal) :
  ∃ C,
    ∀ {a : EuclideanSpace ℝ (Fin (n + 1)) → Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ},
      TauCeti.PDE.UniformlyEllipticOn Set.univ a lam Lam →
        (∀ (i j : Fin (n + 1)), HolderWith L α fun x => a x i j) →
          ∀ {u : EuclideanSpace ℝ (Fin (n + 1)) → ℝ} {N K : NNReal},
            ContDiff ℝ 2 u →
              (∀ (x : EuclideanSpace ℝ (Fin (n + 1))), |u x| ≤ ↑N) →
                BddAbove (Set.range fun x => ‖iteratedFDeriv ℝ 2 u x‖) →
                  MemHolder α (iteratedFDeriv ℝ 2 u) →
                    (HolderWith K α fun x =>
                        ∑ i,
                          ∑ j,
                            a x i j •
                              ((fderiv ℝ (fderiv ℝ u) x) (EuclideanSpace.single i 1))
                                (EuclideanSpace.single j 1)) →
                      HolderWith (C * (K + N)) α (iteratedFDeriv ℝ 2 u) ∧
                        (∀ (x : EuclideanSpace ℝ (Fin (n + 1))), ‖fderiv ℝ u x‖ ≤ ↑C * (↑K + ↑N)) ∧
                          ∀ (x : EuclideanSpace ℝ (Fin (n + 1))),
                            ‖iteratedFDeriv ℝ 2 u x‖ ≤ ↑C * (↑K + ↑N)
```

**The global Schauder estimate with lower-order bounds.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_of_holderWith`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/WholeSpace.html#TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_of_holderWith).

```lean
TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_of_holderWith {n : ℕ}
  {α : NNReal} (hα : 0 < α) (hα1 : α < 1) (lam Lam : ℝ) (L : NNReal) :
  ∃ C,
    ∀ {a : EuclideanSpace ℝ (Fin (n + 1)) → Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ},
      TauCeti.PDE.UniformlyEllipticOn Set.univ a lam Lam →
        (∀ (i j : Fin (n + 1)), HolderWith L α fun x => a x i j) →
          ∀ {u : EuclideanSpace ℝ (Fin (n + 1)) → ℝ} {N K : NNReal},
            ContDiff ℝ 2 u →
              (∀ (x : EuclideanSpace ℝ (Fin (n + 1))), |u x| ≤ ↑N) →
                (∀ (x : EuclideanSpace ℝ (Fin (n + 1))), ‖fderiv ℝ u x‖ ≤ ↑N) →
                  (∀ (x : EuclideanSpace ℝ (Fin (n + 1))), ‖iteratedFDeriv ℝ 2 u x‖ ≤ ↑N) →
                    (∀ (S : Set (EuclideanSpace ℝ (Fin (n + 1)))),
                        IsCompact S → ∃ V, HolderOnWith V α (iteratedFDeriv ℝ 2 u) S) →
                      (HolderWith K α fun x =>
                          ∑ i,
                            ∑ j,
                              a x i j •
                                ((fderiv ℝ (fderiv ℝ u) x) (EuclideanSpace.single i 1))
                                  (EuclideanSpace.single j 1)) →
                        HolderWith (C * (K + N)) α (iteratedFDeriv ℝ 2 u)
```

**The global Schauder estimate with lower-order terms on the whole space.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_and_norm_le_of_sum_smul_fderiv_fderiv_add_fderiv_add_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/LowerOrder.html#TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_and_norm_le_of_sum_smul_fderiv_fderiv_add_fderiv_add_mul).

```lean
TauCeti.PDE.exists_holderWith_iteratedFDeriv_two_and_norm_le_of_sum_smul_fderiv_fderiv_add_fderiv_add_mul
  {n : ℕ} {α : NNReal} (hα : 0 < α) (hα1 : α < 1) (lam Lam : ℝ) (L B : NNReal) :
  ∃ C,
    ∀ {a : EuclideanSpace ℝ (Fin (n + 1)) → Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ}
      {b : EuclideanSpace ℝ (Fin (n + 1)) → EuclideanSpace ℝ (Fin (n + 1))}
      {c : EuclideanSpace ℝ (Fin (n + 1)) → ℝ},
      TauCeti.PDE.UniformlyEllipticOn Set.univ a lam Lam →
        (∀ (i j : Fin (n + 1)), HolderWith L α fun x => a x i j) →
          HolderWith L α b →
            (∀ (x : EuclideanSpace ℝ (Fin (n + 1))), ‖b x‖ ≤ ↑B) →
              HolderWith L α c →
                (∀ (x : EuclideanSpace ℝ (Fin (n + 1))), |c x| ≤ ↑B) →
                  ∀ {u : EuclideanSpace ℝ (Fin (n + 1)) → ℝ} {N K : NNReal},
                    ContDiff ℝ 2 u →
                      (∀ (x : EuclideanSpace ℝ (Fin (n + 1))), |u x| ≤ ↑N) →
                        BddAbove (Set.range fun x => ‖iteratedFDeriv ℝ 2 u x‖) →
                          MemHolder α (iteratedFDeriv ℝ 2 u) →
                            (HolderWith K α fun x =>
                                ∑ i,
                                      ∑ j,
                                        a x i j •
                                          ((fderiv ℝ (fderiv ℝ u) x) (EuclideanSpace.single i 1))
                                            (EuclideanSpace.single j 1) +
                                    (fderiv ℝ u x) (b x) +
                                  c x * u x) →
                              HolderWith (C * (K + N)) α (iteratedFDeriv ℝ 2 u) ∧
                                (∀ (x : EuclideanSpace ℝ (Fin (n + 1))),
                                    ‖fderiv ℝ u x‖ ≤ ↑C * (↑K + ↑N)) ∧
                                  ∀ (x : EuclideanSpace ℝ (Fin (n + 1))),
                                    ‖iteratedFDeriv ℝ 2 u x‖ ≤ ↑C * (↑K + ↑N)
```

**The global Schauder estimate with the supremum norm.** Formalized in Tau Ceti as [`TauCeti.ParabolicC2HolderSpace.exists_norm_le_euclideanParabolicOperatorL_add`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Parabolic/Holder/Schauder.html#TauCeti.ParabolicC2HolderSpace.exists_norm_le_euclideanParabolicOperatorL_add).

```lean
TauCeti.ParabolicC2HolderSpace.exists_norm_le_euclideanParabolicOperatorL_add.{u_1} {α : NNReal}
  {ι : Type u_1} [Fintype ι] [DecidableEq ι] {lam Lam : ℝ} (hα₀ : 0 < α) (hα₁ : α < 1)
  (hlam : 0 < lam) (K T₀ : NNReal) :
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
                      ∀ (u : TauCeti.ParabolicC2HolderSpace α (EuclideanSpace ℝ ι) ℝ hT),
                        ‖u‖ ≤
                          C *
                            (‖(TauCeti.ParabolicC2HolderSpace.euclideanParabolicOperatorL ⋯ a b c)
                                    u‖ +
                                ‖u.spatialTrace ⟨0, ⋯⟩‖ +
                              ‖TauCeti.ParabolicC2HolderSpace.valueL u‖)
```

## Sources

- [Tau Ceti documentation: `TauCeti.ParabolicC2HolderSpace.exists_norm_le_euclideanParabolicOperatorL`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Parabolic/Holder/Schauder.html#TauCeti.ParabolicC2HolderSpace.exists_norm_le_euclideanParabolicOperatorL)
- [Source of `TauCeti.ParabolicC2HolderSpace.exists_norm_le_euclideanParabolicOperatorL` in TauCeti/Analysis/PDE/Parabolic/Holder/Schauder.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Parabolic/Holder/Schauder.lean#L491)
