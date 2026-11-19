---
declaration: theorem
origin: cited
lean: TauCeti.ParabolicC2HolderSpace.exists_rpow_mul_norm_restrictL_le_euclideanParabolicOperatorL_add_norm_valueL, TauCeti.ParabolicC2HolderSpace.exists_rpow_mul_norm_restrictL_le_euclideanParabolicOperatorL, TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv, TauCeti.PDE.exists_holderOnWith_preciseRepresentative_gradient_of_holderOnWith_matrixBilinearForm_of_memLp, TauCeti.PDE.exists_holderOnWith_preciseRepresentative_gradient_of_holderOnWith_matrixBilinearForm, TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_of_holderOnWith, TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_laplacian, TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_closedBall_of_sum_smul_fderiv_fderiv_of_mul_rpow_le, TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_closedBall_of_sum_smul_fderiv_fderiv, TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_add_fderiv_add_mul
statement: formalized
proof: formalized
---

# Interior Schauder estimate at positive times

For `0 < α < 1`, ellipticity constants
`λ > 0` and `Λ`, a bound `K` on the Hölder norms of the coefficients and a bound `T₀` on the
horizon, there is a constant `C` such that on `ℝⁿ × [0, T]`, `T ≤ T₀`, every
`u ∈ C_b^{2+α,1+α/2}` and every `0 < δ < T` satisfy

`δ^(1 + α/2) ‖u‖_{2+α,par;[δ,T]} ≤ C (‖P u‖_{α,par} + ‖u‖_∞)`,

where `‖u‖_{2+α,par;[δ,T]}` is the norm of the restriction of `u` to `ℝⁿ × [δ, T]` and
`P u = ∂ₜu - aⁱʲ ∂ᵢ∂ⱼu - bⁱ ∂ᵢu - c u`. Unlike the global Schauder estimate, the right side
does not involve the `C^{2,α}` norm of the initial values.

```lean
TauCeti.ParabolicC2HolderSpace.exists_rpow_mul_norm_restrictL_le_euclideanParabolicOperatorL_add_norm_valueL.{u_2}
  {α : NNReal} {ι : Type u_2} [Fintype ι] [DecidableEq ι] {lam Lam : ℝ} (hα₀ : 0 < α) (hα₁ : α < 1)
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
                      ∀ (u : TauCeti.ParabolicC2HolderSpace α (EuclideanSpace ℝ ι) ℝ hT) {δ : ℝ}
                        (hδ : 0 < δ) (hδT : δ < ↑T),
                        δ ^ (1 + ↑α / 2) * ‖(TauCeti.ParabolicC2HolderSpace.restrictL ⋯ ⋯ hδT) u‖ ≤
                          C *
                            (‖(TauCeti.ParabolicC2HolderSpace.euclideanParabolicOperatorL ⋯ a b c)
                                  u‖ +
                              ‖TauCeti.ParabolicC2HolderSpace.valueL u‖)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Campanato's theorem](../../../../measure-theory/function/part-01/campanatos-theorem.md)
- [The du Bois-Reymond lemma](../../../part-03/distribution/the-du-bois-reymond-lemma.md)
- [First-order Taylor bound for a Hölder derivative](../../../part-03/holder/first-order-taylor-bound-for-a-holder-derivative.md)
- [The global Schauder estimate](../part-01/the-global-schauder-estimate.md)
- [Green's first identity against `H¹₀(Ω)`](greens-first-identity-against-h10.md)
- [Green's second identity against a test function](../../sobolev/part-01/greens-second-identity-against-a-test-function.md)
- [Gårding's inequality on `H¹(Ω)`](gardings-inequality-on-h1.md)
- [Hölder's inequality for disjoint pieces](../../../../measure-theory/function/part-01/holders-inequality-for-disjoint-pieces.md)
- [Jensen's inequality for the square of a mean](../../../../measure-theory/integral/part-02/jensens-inequality-for-the-square-of-a-mean.md)
- [The Lipschitz bound for bounded harmonic functions](../../../part-03/inner-product-space/part-02/the-lipschitz-bound-for-bounded-harmonic-functio.md)
- [Meyers–Serrin: `H = W` in `W^{k,p}(Ω)`](../../sobolev/part-02/meyers-serrin-h-w-in-w-k-p.md)
- [The Mihlin–Hörmander multiplier theorem on `Lᵖ`](../../../part-02/partial-differential-equations/the-mihlin-hormander-multiplier-theorem-on-lp.md)
- [The Poincaré inequality on a ball](../../sobolev/part-02/the-poincare-inequality-on-a-ball.md)
- [Rademacher's theorem for locally Lipschitz functions](../../../part-03/calculus/part-02/rademachers-theorem-for-locally-lipschitz-functi.md)
- [The Schauder estimate in a weighted class](../part-03/the-schauder-estimate-in-a-weighted-class.md)
- [Second-order Taylor bound for a Hölder second derivative](../../../part-03/holder/second-order-taylor-bound-for-a-holder-second-de.md)
- [Weyl's lemma for continuous functions](../../../part-03/inner-product-space/part-03/weyls-lemma-for-continuous-functions.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ParabolicC2HolderSpace.exists_rpow_mul_norm_restrictL_le_euclideanParabolicOperatorL_add_norm_valueL`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Parabolic/Holder/PositiveTime.html#TauCeti.ParabolicC2HolderSpace.exists_rpow_mul_norm_restrictL_le_euclideanParabolicOperatorL_add_norm_valueL).

## Other forms

**Interior Schauder estimate at positive times, from the initial values.** Formalized in Tau Ceti as [`TauCeti.ParabolicC2HolderSpace.exists_rpow_mul_norm_restrictL_le_euclideanParabolicOperatorL`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Parabolic/Holder/PositiveTime.html#TauCeti.ParabolicC2HolderSpace.exists_rpow_mul_norm_restrictL_le_euclideanParabolicOperatorL).

```lean
TauCeti.ParabolicC2HolderSpace.exists_rpow_mul_norm_restrictL_le_euclideanParabolicOperatorL.{u_2}
  {α : NNReal} {ι : Type u_2} [Fintype ι] [DecidableEq ι] {lam Lam : ℝ} (hα₀ : 0 < α) (hα₁ : α < 1)
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
                      ∀ (u : TauCeti.ParabolicC2HolderSpace α (EuclideanSpace ℝ ι) ℝ hT) {M : ℝ},
                        (∀ (x : EuclideanSpace ℝ ι),
                            |(TauCeti.ParabolicC2HolderSpace.valueL u)
                                  (TauCeti.ParabolicSpaceTime.slabMk x ⟨0, ⋯⟩)| ≤
                              M) →
                          ∀ {δ : ℝ} (hδ : 0 < δ) (hδT : δ < ↑T),
                            δ ^ (1 + ↑α / 2) *
                                ‖(TauCeti.ParabolicC2HolderSpace.restrictL ⋯ ⋯ hδT) u‖ ≤
                              C *
                                (‖(TauCeti.ParabolicC2HolderSpace.euclideanParabolicOperatorL ⋯ a b
                                        c)
                                      u‖ +
                                  M)
```

**Interior Schauder estimate for constant-coefficient operators, classical form.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/Basic.html#TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv).

```lean
TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv {n : ℕ} {α : NNReal}
  (hα : 0 < α) (hα1 : α < 1) :
  ∃ C,
    0 ≤ C ∧
      ∀ {A : Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ} {lam Lam : ℝ},
        0 < lam →
          (∀ (ξ : EuclideanSpace ℝ (Fin (n + 1))), lam * ‖ξ‖ ^ 2 ≤ A.toQuadraticForm' ξ.ofLp) →
            (∀ (ξ : EuclideanSpace ℝ (Fin (n + 1))), A.toQuadraticForm' ξ.ofLp ≤ Lam * ‖ξ‖ ^ 2) →
              ∀ {U S : Set (EuclideanSpace ℝ (Fin (n + 1)))}
                {u : EuclideanSpace ℝ (Fin (n + 1)) → ℝ} {K : NNReal} {R : ℝ},
                IsOpen U →
                  ContDiffOn ℝ 2 u U →
                    Bornology.IsBounded S →
                      0 < R →
                        Metric.cthickening R S ⊆ U →
                          HolderOnWith K α
                              (fun x =>
                                ∑ i,
                                  ∑ j,
                                    A i j •
                                      ((fderiv ℝ (fderiv ℝ u) x) (EuclideanSpace.single i 1))
                                        (EuclideanSpace.single j 1))
                              (Metric.thickening R S) →
                            HolderOnWith
                              (C * (Lam / lam) ^ (1 + (↑n + 1) / 4 + ↑α / 2) *
                                  (↑K / lam +
                                    R ^ (-((↑n + 1) / 2 + ↑α)) *
                                      (MeasureTheory.eLpNorm (iteratedFDeriv ℝ 2 u) 2
                                          (MeasureTheory.volume.restrict
                                            (Metric.thickening R S))).toReal)).toNNReal
                              α (iteratedFDeriv ℝ 2 u) S
```

**Interior Schauder estimate for divergence-form equations with a scalar datum.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_preciseRepresentative_gradient_of_holderOnWith_matrixBilinearForm_of_memLp`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/DivergenceFormSchauder.html#TauCeti.PDE.exists_holderOnWith_preciseRepresentative_gradient_of_holderOnWith_matrixBilinearForm_of_memLp).

```lean
TauCeti.PDE.exists_holderOnWith_preciseRepresentative_gradient_of_holderOnWith_matrixBilinearForm_of_memLp
  {n : ℕ} {α β : NNReal} (hβ : 0 < β) (hβ1 : β < 1) (hβα : β ≤ α) {q : ENNReal} (hq : 2 ≤ q)
  (hβq : ↑β ≤ 1 - (↑n + 1) / q.toReal) {lam Lam M : ℝ} :
  ∃ C,
    0 ≤ C ∧
      ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ (Fin (n + 1)))}
        {u : ↥(TauCeti.W1p MeasureTheory.volume Omega 2)}
        {a : EuclideanSpace ℝ (Fin (n + 1)) → Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ}
        {G : EuclideanSpace ℝ (Fin (n + 1)) → EuclideanSpace ℝ (Fin (n + 1))}
        {f : EuclideanSpace ℝ (Fin (n + 1)) → ℝ} {Ka KG : NNReal}
        {S : Set (EuclideanSpace ℝ (Fin (n + 1)))} {R : ℝ},
        TauCeti.PDE.UniformlyEllipticOn S a lam Lam →
          HolderOnWith Ka α (fun x => TauCeti.PDE.matrixBilinearForm (a x))
              (Metric.thickening R S) →
            HolderOnWith KG α G (Metric.thickening R S) →
              ↑Ka * R ^ ↑α ≤ M →
                MeasureTheory.MemLp f q (MeasureTheory.volume.restrict (Metric.thickening R S)) →
                  (∀ (φ : TestFunction Omega ℝ ⊤),
                      TauCeti.PDE.energyFormH1 a 0 0 u
                          ((TauCeti.W1p.ofTestFunctionₗ MeasureTheory.volume Omega 2) φ) =
                        (∫ (x : EuclideanSpace ℝ (Fin (n + 1))) in ↑Omega,
                            inner ℝ (G x) (gradient (⇑φ) x)) +
                          ∫ (x : EuclideanSpace ℝ (Fin (n + 1))) in ↑Omega, f x * φ x) →
                    0 < R →
                      Metric.thickening R S ⊆ ↑Omega →
                        HolderOnWith
                          (C *
                              (↑KG * R ^ (↑α - ↑β) +
                                  R ^ (1 - (↑n + 1) / q.toReal - ↑β) *
                                    (MeasureTheory.eLpNorm f q
                                        (MeasureTheory.volume.restrict
                                          (Metric.thickening R S))).toReal +
                                R ^ (-((↑n + 1) / 2 + ↑β)) * ‖TauCeti.W1p.gradient u‖)).toNNReal
                          β
                          (TauCeti.MeasureTheory.preciseRepresentative MeasureTheory.volume
                            ↑↑(TauCeti.W1p.gradient u))
                          S
```

**Interior Schauder estimate for divergence-form equations with Hölder coefficients.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_preciseRepresentative_gradient_of_holderOnWith_matrixBilinearForm`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/DivergenceFormSchauder.html#TauCeti.PDE.exists_holderOnWith_preciseRepresentative_gradient_of_holderOnWith_matrixBilinearForm).

```lean
TauCeti.PDE.exists_holderOnWith_preciseRepresentative_gradient_of_holderOnWith_matrixBilinearForm
  {n : ℕ} {α : NNReal} (hα : 0 < α) (hα1 : α < 1) {lam Lam M : ℝ} :
  ∃ C,
    0 ≤ C ∧
      ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ (Fin (n + 1)))}
        {u : ↥(TauCeti.W1p MeasureTheory.volume Omega 2)}
        {a : EuclideanSpace ℝ (Fin (n + 1)) → Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ}
        {G : EuclideanSpace ℝ (Fin (n + 1)) → EuclideanSpace ℝ (Fin (n + 1))} {Ka KG : NNReal}
        {S : Set (EuclideanSpace ℝ (Fin (n + 1)))} {R : ℝ},
        TauCeti.PDE.UniformlyEllipticOn S a lam Lam →
          HolderOnWith Ka α (fun x => TauCeti.PDE.matrixBilinearForm (a x))
              (Metric.thickening R S) →
            HolderOnWith KG α G (Metric.thickening R S) →
              ↑Ka * R ^ ↑α ≤ M →
                (∀ (φ : TestFunction Omega ℝ ⊤),
                    TauCeti.PDE.energyFormH1 a 0 0 u
                        ((TauCeti.W1p.ofTestFunctionₗ MeasureTheory.volume Omega 2) φ) =
                      ∫ (x : EuclideanSpace ℝ (Fin (n + 1))) in ↑Omega,
                        inner ℝ (G x) (gradient (⇑φ) x)) →
                  0 < R →
                    Metric.thickening R S ⊆ ↑Omega →
                      HolderOnWith
                        (C * (↑KG + R ^ (-((↑n + 1) / 2 + ↑α)) * ‖TauCeti.W1p.gradient u‖)).toNNReal
                        α
                        (TauCeti.MeasureTheory.preciseRepresentative MeasureTheory.volume
                          ↑↑(TauCeti.W1p.gradient u))
                        S
```

**The interior Schauder estimate for Hölder coefficients.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_of_holderOnWith`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/HolderCoefficient.html#TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_of_holderOnWith).

```lean
TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_of_holderOnWith {n : ℕ}
  {α : NNReal} (hα : 0 < α) (hα1 : α < 1) {Ω K : Set (EuclideanSpace ℝ (Fin (n + 1)))}
  (hΩ : IsOpen Ω) (hK : IsCompact K) (hKΩ : K ⊆ Ω)
  {a : EuclideanSpace ℝ (Fin (n + 1)) → Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ}
  (ha :
    ∀ x ∈ K,
      ∃ r > 0, ∃ L, ∀ (i j : Fin (n + 1)), HolderOnWith L α (fun y => a y i j) (Metric.ball x r))
  (hell :
    ∀ x ∈ K,
      ∃ lam,
        0 < lam ∧
          ∀ (ξ : EuclideanSpace ℝ (Fin (n + 1))), lam * ‖ξ‖ ^ 2 ≤ (a x).toQuadraticForm' ξ.ofLp) :
  ∃ C,
    ∀ {u : EuclideanSpace ℝ (Fin (n + 1)) → ℝ} {N M : NNReal},
      ContDiffOn ℝ 2 u Ω →
        (∀ x ∈ Ω, |u x| ≤ ↑N) →
          (∀ x ∈ Ω, ‖fderiv ℝ u x‖ ≤ ↑N) →
            (∀ x ∈ Ω, ‖iteratedFDeriv ℝ 2 u x‖ ≤ ↑N) →
              (∀ S ⊆ Ω, IsCompact S → ∃ V, HolderOnWith V α (iteratedFDeriv ℝ 2 u) S) →
                HolderOnWith M α
                    (fun x =>
                      ∑ i,
                        ∑ j,
                          a x i j •
                            ((fderiv ℝ (fderiv ℝ u) x) (EuclideanSpace.single i 1))
                              (EuclideanSpace.single j 1))
                    Ω →
                  HolderOnWith (C * (M + N)) α (iteratedFDeriv ℝ 2 u) K
```

**Interior Schauder estimate for Poisson's equation, classical form.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_laplacian`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/Basic.html#TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_laplacian).

```lean
TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_laplacian {n : ℕ} {α : NNReal} (hα : 0 < α)
  (hα1 : α < 1) :
  ∃ C,
    0 ≤ C ∧
      ∀ {U S : Set (EuclideanSpace ℝ (Fin (n + 1)))} {u : EuclideanSpace ℝ (Fin (n + 1)) → ℝ}
        {K : NNReal} {R : ℝ},
        IsOpen U →
          ContDiffOn ℝ 2 u U →
            Bornology.IsBounded S →
              0 < R →
                Metric.cthickening R S ⊆ U →
                  HolderOnWith K α (Laplacian.laplacian u) (Metric.thickening R S) →
                    HolderOnWith
                      (C *
                          (↑K +
                            R ^ (-((↑n + 1) / 2 + ↑α)) *
                              (MeasureTheory.eLpNorm (iteratedFDeriv ℝ 2 u) 2
                                  (MeasureTheory.volume.restrict
                                    (Metric.thickening R S))).toReal)).toNNReal
                      α (iteratedFDeriv ℝ 2 u) S
```

**The interior Schauder estimate in scaled form.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_closedBall_of_sum_smul_fderiv_fderiv_of_mul_rpow_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/Scaled.html#TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_closedBall_of_sum_smul_fderiv_fderiv_of_mul_rpow_le).

```lean
TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_closedBall_of_sum_smul_fderiv_fderiv_of_mul_rpow_le
  {n : ℕ} {α : NNReal} (hα : 0 < α) (hα1 : α < 1) (lam Lam : ℝ) (M : NNReal) :
  ∃ C,
    0 ≤ C ∧
      ∀ {a : EuclideanSpace ℝ (Fin (n + 1)) → Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ}
        {x₀ : EuclideanSpace ℝ (Fin (n + 1))} {r : ℝ} {Ka Mu K : NNReal}
        {u : EuclideanSpace ℝ (Fin (n + 1)) → ℝ},
        0 < r →
          TauCeti.PDE.UniformlyEllipticOn (Metric.ball x₀ (2 * r)) a lam Lam →
            (∀ (i j : Fin (n + 1)), HolderOnWith Ka α (fun x => a x i j) (Metric.ball x₀ (2 * r))) →
              ↑Ka * r ^ ↑α ≤ ↑M →
                ContDiffOn ℝ 2 u (Metric.ball x₀ (2 * r)) →
                  (∀ x ∈ Metric.ball x₀ (2 * r), |u x| ≤ ↑Mu) →
                    (∀ ρ < 2 * r,
                        ∃ V, HolderOnWith V α (iteratedFDeriv ℝ 2 u) (Metric.closedBall x₀ ρ)) →
                      HolderOnWith K α
                          (fun x =>
                            ∑ i,
                              ∑ j,
                                a x i j •
                                  ((fderiv ℝ (fderiv ℝ u) x) (EuclideanSpace.single i 1))
                                    (EuclideanSpace.single j 1))
                          (Metric.ball x₀ (2 * r)) →
                        HolderOnWith (C * (r ^ (-(2 + ↑α)) * ↑Mu + ↑K)).toNNReal α
                          (iteratedFDeriv ℝ 2 u) (Metric.closedBall x₀ r)
```

**The interior Schauder estimate on small balls.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_closedBall_of_sum_smul_fderiv_fderiv`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/Interior.html#TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_closedBall_of_sum_smul_fderiv_fderiv).

```lean
TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_closedBall_of_sum_smul_fderiv_fderiv {n : ℕ}
  {α : NNReal} (hα : 0 < α) (hα1 : α < 1) :
  ∃ C₀,
    0 < C₀ ∧
      ∀ {lam Lam : ℝ} {L M : NNReal} {R : ℝ},
        0 < lam →
          2 * (C₀ * (Lam / lam) ^ (1 + (↑n + 1) / 4 + ↑α / 2)) * (↑n + 1) ^ 2 *
                ((1 + 2 ^ ↑α) * ↑L * R ^ ↑α) ≤
              lam →
            ∀ {ρ : ℝ},
              ρ < R →
                ∃ C,
                  ∀ {a : EuclideanSpace ℝ (Fin (n + 1)) → Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ}
                    {x₀ : EuclideanSpace ℝ (Fin (n + 1))},
                    (∀ (ξ : EuclideanSpace ℝ (Fin (n + 1))),
                        lam * ‖ξ‖ ^ 2 ≤ (a x₀).toQuadraticForm' ξ.ofLp) →
                      (∀ (ξ : EuclideanSpace ℝ (Fin (n + 1))),
                          (a x₀).toQuadraticForm' ξ.ofLp ≤ Lam * ‖ξ‖ ^ 2) →
                        (∀ (i j : Fin (n + 1)),
                            HolderOnWith L α (fun x => a x i j) (Metric.closedBall x₀ R)) →
                          (∀ x ∈ Metric.closedBall x₀ R, ∀ (i j : Fin (n + 1)), |a x i j| ≤ ↑M) →
                            ∀ {u : EuclideanSpace ℝ (Fin (n + 1)) → ℝ} {N K V : NNReal},
                              ContDiffOn ℝ 2 u (Metric.ball x₀ R) →
                                (∀ x ∈ Metric.ball x₀ R, |u x| ≤ ↑N) →
                                  (∀ x ∈ Metric.ball x₀ R, ‖fderiv ℝ u x‖ ≤ ↑N) →
                                    (∀ x ∈ Metric.ball x₀ R, ‖iteratedFDeriv ℝ 2 u x‖ ≤ ↑N) →
                                      HolderOnWith V α (iteratedFDeriv ℝ 2 u) (Metric.ball x₀ R) →
                                        HolderOnWith K α
                                            (fun x =>
                                              ∑ i,
                                                ∑ j,
                                                  a x i j •
                                                    ((fderiv ℝ (fderiv ℝ u) x)
                                                        (EuclideanSpace.single i 1))
                                                      (EuclideanSpace.single j 1))
                                            (Metric.ball x₀ R) →
                                          HolderOnWith (C * (K + N)) α (iteratedFDeriv ℝ 2 u)
                                            (Metric.closedBall x₀ ρ)
```

**The interior Schauder estimate with lower-order terms.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_add_fderiv_add_mul`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Schauder/LowerOrder.html#TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_add_fderiv_add_mul).

```lean
TauCeti.PDE.exists_holderOnWith_iteratedFDeriv_two_of_sum_smul_fderiv_fderiv_add_fderiv_add_mul
  {n : ℕ} {α : NNReal} (hα : 0 < α) (hα1 : α < 1) {Ω K : Set (EuclideanSpace ℝ (Fin (n + 1)))}
  (hΩ : IsOpen Ω) (hK : IsCompact K) (hKΩ : K ⊆ Ω)
  {a : EuclideanSpace ℝ (Fin (n + 1)) → Matrix (Fin (n + 1)) (Fin (n + 1)) ℝ}
  {b : EuclideanSpace ℝ (Fin (n + 1)) → EuclideanSpace ℝ (Fin (n + 1))}
  {c : EuclideanSpace ℝ (Fin (n + 1)) → ℝ}
  (ha :
    ∀ x ∈ K,
      ∃ r > 0, ∃ L, ∀ (i j : Fin (n + 1)), HolderOnWith L α (fun y => a y i j) (Metric.ball x r))
  (hb : ∀ x ∈ K, ∃ r > 0, ∃ L, HolderOnWith L α b (Metric.ball x r))
  (hc : ∀ x ∈ K, ∃ r > 0, ∃ L, HolderOnWith L α c (Metric.ball x r))
  (hell :
    ∀ x ∈ K,
      ∃ lam,
        0 < lam ∧
          ∀ (ξ : EuclideanSpace ℝ (Fin (n + 1))), lam * ‖ξ‖ ^ 2 ≤ (a x).toQuadraticForm' ξ.ofLp) :
  ∃ C,
    ∀ {u : EuclideanSpace ℝ (Fin (n + 1)) → ℝ} {N M : NNReal},
      ContDiffOn ℝ 2 u Ω →
        (∀ x ∈ Ω, |u x| ≤ ↑N) →
          (∀ x ∈ Ω, ‖fderiv ℝ u x‖ ≤ ↑N) →
            (∀ x ∈ Ω, ‖iteratedFDeriv ℝ 2 u x‖ ≤ ↑N) →
              (∀ S ⊆ Ω, IsCompact S → ∃ V, HolderOnWith V α (iteratedFDeriv ℝ 2 u) S) →
                HolderOnWith M α
                    (fun x =>
                      ∑ i,
                            ∑ j,
                              a x i j •
                                ((fderiv ℝ (fderiv ℝ u) x) (EuclideanSpace.single i 1))
                                  (EuclideanSpace.single j 1) +
                          (fderiv ℝ u x) (b x) +
                        c x * u x)
                    Ω →
                  HolderOnWith (C * (M + N)) α (iteratedFDeriv ℝ 2 u) K
```

## Sources

- [Tau Ceti documentation: `TauCeti.ParabolicC2HolderSpace.exists_rpow_mul_norm_restrictL_le_euclideanParabolicOperatorL_add_norm_valueL`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Parabolic/Holder/PositiveTime.html#TauCeti.ParabolicC2HolderSpace.exists_rpow_mul_norm_restrictL_le_euclideanParabolicOperatorL_add_norm_valueL)
- [Source of `TauCeti.ParabolicC2HolderSpace.exists_rpow_mul_norm_restrictL_le_euclideanParabolicOperatorL_add_norm_valueL` in TauCeti/Analysis/PDE/Parabolic/Holder/PositiveTime.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/Parabolic/Holder/PositiveTime.lean#L357)
