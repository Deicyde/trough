---
declaration: theorem
origin: cited
lean: TauCeti.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_laplacian, TauCeti.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_laplacian_real, TauCeti.exists_eLpNorm_lineDerivOp_lineDerivOp_le_eLpNorm_laplacian, TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_sum_mul_inner_eq, TauCeti.PDE.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_sum_smul_fderiv_fderiv, TauCeti.PDE.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_sum_smul_fderiv_fderiv_real, TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_traceCLM_compLpL_eq, TauCeti.exists_eLpNorm_fourierMultiplierCLM_hessianSymbolLp_le, TauCeti.PDE.exists_norm_iteratedGradient_le_of_sum_mul_inner_eq_of_dist_lt_abs_sub_le, TauCeti.PDE.exists_norm_iteratedGradient_le_mul_norm_of_sum_mul_inner_eq_of_abs_sub_le, TauCeti.PDE.exists_norm_iteratedGradient_le_of_sum_mul_inner_eq_of_uniformContinuous, TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_integral_laplacian_smul_eq, TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_traceCLM_comp_eq_of_norm_sub_le_of_normalHalfSpace, TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_integral_laplacian_smul_eq_of_normalHalfSpace, TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_traceCLM_comp_eq_of_normalHalfSpace, TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_traceCLM_compLpL_eq_of_normalHalfSpace
statement: formalized
proof: formalized
---

# The Calderón–Zygmund estimate `‖D²u‖_p ≤ C ‖Δu‖_p`

Let `1 < p < ∞`, and let `V` be a
finite-dimensional real inner product space with its volume measure. There is a constant `C` with

`‖D²u‖_{Lᵖ} ≤ C ‖Δu‖_{Lᵖ}`

for every Schwartz function `u` on `V` with values in a complex Hilbert space, where `D²u` is the
second Fréchet derivative of `u`.

```lean
TauCeti.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_laplacian.{u_1, u_2} {F : Type u_1}
  [NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F] {V : Type u_2}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] [MeasurableSpace V]
  [BorelSpace V] {p : ENNReal} (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀ (u : SchwartzMap V F),
      MeasureTheory.eLpNorm (iteratedFDeriv ℝ 2 ⇑u) p MeasureTheory.volume ≤
        ↑C * MeasureTheory.eLpNorm (⇑(Laplacian.laplacian u)) p MeasureTheory.volume
```

## Depends on

- [TauCeti.Wkp](tauceti-wkp.md)

## Proof depends on

- [The Calderón–Zygmund theorem, weak type `(1, 1)`](../../../measure-theory/integral/the-calderon-zygmund-theorem-weak-type-1-1.md)
- [The interior Calderón–Zygmund estimate for continuous coefficients](the-interior-calderon-zygmund-estimate-for-conti.md)
- [Rademacher's theorem for locally Lipschitz functions](../calculus/part-01/rademachers-theorem-for-locally-lipschitz-functi.md)
- [Radial fundamental theorem of calculus](../../../measure-theory/constructions/radial-fundamental-theorem-of-calculus.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_laplacian`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Lp.html#TauCeti.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_laplacian).

## Other forms

**The Calderón–Zygmund estimate `‖D²u‖_p ≤ C ‖Δu‖_p` for real functions.** Formalized in Tau Ceti as [`TauCeti.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_laplacian_real`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Lp.html#TauCeti.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_laplacian_real).

```lean
TauCeti.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_laplacian_real.{u_2} {V : Type u_2}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [FiniteDimensional ℝ V] [MeasurableSpace V]
  [BorelSpace V] {p : ENNReal} (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀ (u : SchwartzMap V ℝ),
      MeasureTheory.eLpNorm (iteratedFDeriv ℝ 2 ⇑u) p MeasureTheory.volume ≤
        ↑C * MeasureTheory.eLpNorm (⇑(Laplacian.laplacian u)) p MeasureTheory.volume
```

**The Calderón–Zygmund estimate for a second directional derivative.** Formalized in Tau Ceti as [`TauCeti.exists_eLpNorm_lineDerivOp_lineDerivOp_le_eLpNorm_laplacian`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Lp.html#TauCeti.exists_eLpNorm_lineDerivOp_lineDerivOp_le_eLpNorm_laplacian).

```lean
TauCeti.exists_eLpNorm_lineDerivOp_lineDerivOp_le_eLpNorm_laplacian.{u_1} {n : ℕ} {F : Type u_1}
  [NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F] (v w : EuclideanSpace ℝ (Fin n))
  {p : ENNReal} (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀ (u : SchwartzMap (EuclideanSpace ℝ (Fin n)) F),
      MeasureTheory.eLpNorm (⇑(LineDeriv.lineDerivOp v (LineDeriv.lineDerivOp w u))) p
          MeasureTheory.volume ≤
        ↑C * MeasureTheory.eLpNorm (⇑(Laplacian.laplacian u)) p MeasureTheory.volume
```

**The Calderón–Zygmund estimate for constant coefficients in `W^{2,p}(ℝⁿ)`.** Formalized in Tau Ceti as [`TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_sum_mul_inner_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Sobolev.html#TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_sum_mul_inner_eq).

```lean
TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_sum_mul_inner_eq {n : ℕ} {p : ENNReal}
  [Fact (1 ≤ p)] (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀ {A : Matrix (Fin n) (Fin n) ℝ} {lam : ℝ},
      0 < lam →
        (∀ (ξ : EuclideanSpace ℝ (Fin n)), lam * ‖ξ‖ ^ 2 ≤ A.toQuadraticForm' ξ.ofLp) →
          ∀ (u : TauCeti.Wkp MeasureTheory.volume ⊤ p 2)
            (f : ↥(MeasureTheory.Lp ℝ p (MeasureTheory.volume.restrict ↑⊤))),
            (∀ᵐ (x : EuclideanSpace ℝ (Fin n)),
                ∑ i,
                    ∑ j,
                      A i j *
                        inner ℝ
                          ((↑↑(TauCeti.Wkp.iteratedGradient 1 u) x) (EuclideanSpace.single i 1))
                          (EuclideanSpace.single j 1) =
                  ↑↑f x) →
              ‖TauCeti.Wkp.iteratedGradient 1 u‖ ≤ ↑C / lam * ‖f‖
```

**The Calderón–Zygmund estimate for constant-coefficient operators.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_sum_smul_fderiv_fderiv`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/ConstantCoefficient.html#TauCeti.PDE.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_sum_smul_fderiv_fderiv).

```lean
TauCeti.PDE.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_sum_smul_fderiv_fderiv.{u_1} {n : ℕ}
  {p : ENNReal} {F : Type u_1} [NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F]
  (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀ {A : Matrix (Fin n) (Fin n) ℝ} {lam : ℝ},
      0 < lam →
        (∀ (ξ : EuclideanSpace ℝ (Fin n)), lam * ‖ξ‖ ^ 2 ≤ A.toQuadraticForm' ξ.ofLp) →
          ∀ (u : SchwartzMap (EuclideanSpace ℝ (Fin n)) F),
            MeasureTheory.eLpNorm (iteratedFDeriv ℝ 2 ⇑u) p MeasureTheory.volume ≤
              ENNReal.ofReal (↑C / lam) *
                MeasureTheory.eLpNorm
                  (fun x =>
                    ∑ i,
                      ∑ j,
                        A i j •
                          ((fderiv ℝ (fderiv ℝ ⇑u) x) (EuclideanSpace.single i 1))
                            (EuclideanSpace.single j 1))
                  p MeasureTheory.volume
```

**The Calderón–Zygmund estimate for constant-coefficient operators, real-valued form.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_sum_smul_fderiv_fderiv_real`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/ConstantCoefficient.html#TauCeti.PDE.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_sum_smul_fderiv_fderiv_real).

```lean
TauCeti.PDE.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_sum_smul_fderiv_fderiv_real {n : ℕ}
  {p : ENNReal} (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀ {A : Matrix (Fin n) (Fin n) ℝ} {lam : ℝ},
      0 < lam →
        (∀ (ξ : EuclideanSpace ℝ (Fin n)), lam * ‖ξ‖ ^ 2 ≤ A.toQuadraticForm' ξ.ofLp) →
          ∀ (u : SchwartzMap (EuclideanSpace ℝ (Fin n)) ℝ),
            MeasureTheory.eLpNorm (iteratedFDeriv ℝ 2 ⇑u) p MeasureTheory.volume ≤
              ENNReal.ofReal (↑C / lam) *
                MeasureTheory.eLpNorm
                  (fun x =>
                    ∑ i,
                      ∑ j,
                        A i j •
                          ((fderiv ℝ (fderiv ℝ ⇑u) x) (EuclideanSpace.single i 1))
                            (EuclideanSpace.single j 1))
                  p MeasureTheory.volume
```

**The Calderón–Zygmund estimate for strong solutions in `W^{2,p}`.** Formalized in Tau Ceti as [`TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_traceCLM_compLpL_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Sobolev.html#TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_traceCLM_compLpL_eq).

```lean
TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_traceCLM_compLpL_eq.{u_1} {p : ENNReal}
  [Fact (1 ≤ p)] {V : Type u_1} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
  [FiniteDimensional ℝ V] [MeasurableSpace V] [BorelSpace V] (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀ (u : TauCeti.Wkp MeasureTheory.volume ⊤ p 2)
      (f : ↥(MeasureTheory.Lp ℝ p (MeasureTheory.volume.restrict ↑⊤))),
      (ContinuousLinearMap.compLpL p (MeasureTheory.volume.restrict ↑⊤) (TauCeti.traceCLM ℝ V))
            (TauCeti.Wkp.iteratedGradient 1 u) =
          f →
        ‖TauCeti.Wkp.iteratedGradient 1 u‖ ≤ ↑C * ‖f‖
```

**The Calderón–Zygmund estimate for the Hessian multiplier.** Formalized in Tau Ceti as [`TauCeti.exists_eLpNorm_fourierMultiplierCLM_hessianSymbolLp_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Lp.html#TauCeti.exists_eLpNorm_fourierMultiplierCLM_hessianSymbolLp_le).

```lean
TauCeti.exists_eLpNorm_fourierMultiplierCLM_hessianSymbolLp_le.{u_1} {n : ℕ} {F : Type u_1}
  [NormedAddCommGroup F] [InnerProductSpace ℂ F] [CompleteSpace F] (hn : 3 ≤ n)
  (v w : EuclideanSpace ℝ (Fin n)) {p : ENNReal} (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀ (f : ↥(MeasureTheory.Lp F 2 MeasureTheory.volume)),
      MeasureTheory.eLpNorm
          (↑↑((MeasureTheory.Lp.fourierMultiplierCLM F (TauCeti.hessianSymbolLp v w)) f)) p
          MeasureTheory.volume ≤
        ↑C * MeasureTheory.eLpNorm (↑↑f) p MeasureTheory.volume
```

**The Calderón–Zygmund estimate in `W^{2,p}(ℝⁿ)` for coefficients of small local oscillation.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_norm_iteratedGradient_le_of_sum_mul_inner_eq_of_dist_lt_abs_sub_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/WholeSpace.html#TauCeti.PDE.exists_norm_iteratedGradient_le_of_sum_mul_inner_eq_of_dist_lt_abs_sub_le).

```lean
TauCeti.PDE.exists_norm_iteratedGradient_le_of_sum_mul_inner_eq_of_dist_lt_abs_sub_le {n : ℕ}
  {p : ENNReal} [Fact (1 ≤ p)] (hn : 0 < n) (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C δ,
    0 < δ ∧
      ∀ {lam Λ ρ : ℝ},
        0 < lam →
          0 < ρ →
            ∀ {a : EuclideanSpace ℝ (Fin n) → Matrix (Fin n) (Fin n) ℝ},
              MeasureTheory.AEStronglyMeasurable a MeasureTheory.volume →
                (∀ (x ξ : EuclideanSpace ℝ (Fin n)),
                    lam * ‖ξ‖ ^ 2 ≤ (a x).toQuadraticForm' ξ.ofLp) →
                  (∀ (x : EuclideanSpace ℝ (Fin n)) (i j : Fin n), |a x i j| ≤ Λ) →
                    (∀ (x y : EuclideanSpace ℝ (Fin n)),
                        dist x y < ρ → ∀ (i j : Fin n), |a x i j - a y i j| ≤ δ * lam) →
                      ∀ (u : TauCeti.Wkp MeasureTheory.volume ⊤ p 2)
                        (f : ↥(MeasureTheory.Lp ℝ p (MeasureTheory.volume.restrict ↑⊤))),
                        (∀ᵐ (x : EuclideanSpace ℝ (Fin n)),
                            ∑ i,
                                ∑ j,
                                  a x i j *
                                    inner ℝ
                                      ((↑↑(TauCeti.Wkp.iteratedGradient 1 u) x)
                                        (EuclideanSpace.single i 1))
                                      (EuclideanSpace.single j 1) =
                              ↑↑f x) →
                          ‖TauCeti.Wkp.iteratedGradient 1 u‖ ≤
                            ↑C * (‖f‖ / lam + (1 + Λ / lam) ^ 2 / ρ ^ 2 * ‖TauCeti.Wkp.value 2 u‖)
```

**The Calderón–Zygmund estimate in `W^{2,p}(ℝⁿ)` for coefficients of small oscillation.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_norm_iteratedGradient_le_mul_norm_of_sum_mul_inner_eq_of_abs_sub_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/VariableCoefficient.html#TauCeti.PDE.exists_norm_iteratedGradient_le_mul_norm_of_sum_mul_inner_eq_of_abs_sub_le).

```lean
TauCeti.PDE.exists_norm_iteratedGradient_le_mul_norm_of_sum_mul_inner_eq_of_abs_sub_le {n : ℕ}
  {p : ENNReal} [Fact (1 ≤ p)] (hn : 0 < n) (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C δ,
    0 < δ ∧
      ∀ {A : Matrix (Fin n) (Fin n) ℝ} {lam : ℝ},
        0 < lam →
          (∀ (ξ : EuclideanSpace ℝ (Fin n)), lam * ‖ξ‖ ^ 2 ≤ A.toQuadraticForm' ξ.ofLp) →
            ∀ {a : EuclideanSpace ℝ (Fin n) → Matrix (Fin n) (Fin n) ℝ}
              {s : Set (EuclideanSpace ℝ (Fin n))} {ε : ℝ},
              IsClosed s →
                ε ≤ δ * lam →
                  (∀ᵐ (x : EuclideanSpace ℝ (Fin n)),
                      x ∈ s → ∀ (i j : Fin n), |a x i j - A i j| ≤ ε) →
                    ∀ (u : TauCeti.Wkp MeasureTheory.volume ⊤ p 2)
                      (f : ↥(MeasureTheory.Lp ℝ p (MeasureTheory.volume.restrict ↑⊤))),
                      (∀ᵐ (x : EuclideanSpace ℝ (Fin n)), x ∉ s → ↑↑(TauCeti.Wkp.value 2 u) x = 0) →
                        (∀ᵐ (x : EuclideanSpace ℝ (Fin n)),
                            ∑ i,
                                ∑ j,
                                  a x i j *
                                    inner ℝ
                                      ((↑↑(TauCeti.Wkp.iteratedGradient 1 u) x)
                                        (EuclideanSpace.single i 1))
                                      (EuclideanSpace.single j 1) =
                              ↑↑f x) →
                          ‖TauCeti.Wkp.iteratedGradient 1 u‖ ≤ ↑C / lam * ‖f‖
```

**The Calderón–Zygmund estimate in `W^{2,p}(ℝⁿ)` for uniformly continuous coefficients.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_norm_iteratedGradient_le_of_sum_mul_inner_eq_of_uniformContinuous`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/WholeSpace.html#TauCeti.PDE.exists_norm_iteratedGradient_le_of_sum_mul_inner_eq_of_uniformContinuous).

```lean
TauCeti.PDE.exists_norm_iteratedGradient_le_of_sum_mul_inner_eq_of_uniformContinuous {n : ℕ}
  {p : ENNReal} [Fact (1 ≤ p)] (hn : 0 < n) (hp : 1 < p) (hp_top : p ≠ ⊤)
  {a : EuclideanSpace ℝ (Fin n) → Matrix (Fin n) (Fin n) ℝ} (ha : UniformContinuous a) {lam Λ : ℝ}
  (hlam : 0 < lam)
  (hA : ∀ (x ξ : EuclideanSpace ℝ (Fin n)), lam * ‖ξ‖ ^ 2 ≤ (a x).toQuadraticForm' ξ.ofLp)
  (haΛ : ∀ (x : EuclideanSpace ℝ (Fin n)) (i j : Fin n), |a x i j| ≤ Λ) :
  ∃ C,
    ∀ (u : TauCeti.Wkp MeasureTheory.volume ⊤ p 2)
      (f : ↥(MeasureTheory.Lp ℝ p (MeasureTheory.volume.restrict ↑⊤))),
      (∀ᵐ (x : EuclideanSpace ℝ (Fin n)),
          ∑ i,
              ∑ j,
                a x i j *
                  inner ℝ ((↑↑(TauCeti.Wkp.iteratedGradient 1 u) x) (EuclideanSpace.single i 1))
                    (EuclideanSpace.single j 1) =
            ↑↑f x) →
        ‖TauCeti.Wkp.iteratedGradient 1 u‖ ≤ C * (‖f‖ + ‖TauCeti.Wkp.value 2 u‖)
```

**The Calderón–Zygmund estimate in `W^{2,p}`, against test functions.** Formalized in Tau Ceti as [`TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_integral_laplacian_smul_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Sobolev.html#TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_integral_laplacian_smul_eq).

```lean
TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_integral_laplacian_smul_eq.{u_1} {p : ENNReal}
  [Fact (1 ≤ p)] {V : Type u_1} [NormedAddCommGroup V] [InnerProductSpace ℝ V]
  [FiniteDimensional ℝ V] [MeasurableSpace V] [BorelSpace V] (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀ (u : TauCeti.Wkp MeasureTheory.volume ⊤ p 2)
      (f : ↥(MeasureTheory.Lp ℝ p (MeasureTheory.volume.restrict ↑⊤))),
      (∀ (φ : TestFunction ⊤ ℝ ⊤),
          ∫ (x : V), Laplacian.laplacian (⇑φ) x • ↑↑(TauCeti.Wkp.value 2 u) x =
            ∫ (x : V), φ x • ↑↑f x) →
        ‖TauCeti.Wkp.iteratedGradient 1 u‖ ≤ ↑C * ‖f‖
```

**The Calderón–Zygmund estimate on a half-space for coefficients of small oscillation.** Formalized in Tau Ceti as [`TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_traceCLM_comp_eq_of_norm_sub_le_of_normalHalfSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/HalfSpace.html#TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_traceCLM_comp_eq_of_norm_sub_le_of_normalHalfSpace).

```lean
TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_traceCLM_comp_eq_of_norm_sub_le_of_normalHalfSpace.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {p : ENNReal} [Fact (1 ≤ p)] (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C δ,
    0 < δ ∧
      ∀ (a : ℝ) {A : WithLp 2 (ℝ × E) → WithLp 2 (ℝ × E) →L[ℝ] WithLp 2 (ℝ × E)}
        {s : Set (WithLp 2 (ℝ × E))} {μ ε : ℝ},
        0 < μ →
          IsClosed s →
            ε ≤ δ * μ →
              (∀ᵐ (x :
                  WithLp 2 (ℝ × E)) ∂MeasureTheory.volume.restrict ↑(TauCeti.normalHalfSpace a),
                  x ∈ s → ‖A x - μ • 1‖ ≤ ε) →
                ∀ (u : TauCeti.Wkp MeasureTheory.volume (TauCeti.normalHalfSpace a) p 2)
                  (f :
                    ↥(MeasureTheory.Lp ℝ p
                        (MeasureTheory.volume.restrict ↑(TauCeti.normalHalfSpace a)))),
                  TauCeti.Wkp.firstOrder 1 u ∈
                      TauCeti.w1p0Submodule MeasureTheory.volume (TauCeti.normalHalfSpace a) p →
                    (∀ᵐ (x :
                        WithLp 2
                          (ℝ × E)) ∂MeasureTheory.volume.restrict ↑(TauCeti.normalHalfSpace a),
                        x ∉ s → ↑↑(TauCeti.Wkp.value 2 u) x = 0) →
                      (∀ᵐ (x :
                          WithLp 2
                            (ℝ × E)) ∂MeasureTheory.volume.restrict ↑(TauCeti.normalHalfSpace a),
                          (TauCeti.traceCLM ℝ (WithLp 2 (ℝ × E)))
                              (A x ∘SL ↑↑(TauCeti.Wkp.iteratedGradient 1 u) x) =
                            ↑↑f x) →
                        ‖TauCeti.Wkp.iteratedGradient 1 u‖ ≤ ↑C / μ * ‖f‖
```

**The Calderón–Zygmund estimate on a half-space, against test functions.** Formalized in Tau Ceti as [`TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_integral_laplacian_smul_eq_of_normalHalfSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/HalfSpace.html#TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_integral_laplacian_smul_eq_of_normalHalfSpace).

```lean
TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_integral_laplacian_smul_eq_of_normalHalfSpace.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {p : ENNReal} [Fact (1 ≤ p)] (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀ (a : ℝ) (u : TauCeti.Wkp MeasureTheory.volume (TauCeti.normalHalfSpace a) p 2)
      (f : ↥(MeasureTheory.Lp ℝ p (MeasureTheory.volume.restrict ↑(TauCeti.normalHalfSpace a)))),
      TauCeti.Wkp.firstOrder 1 u ∈
          TauCeti.w1p0Submodule MeasureTheory.volume (TauCeti.normalHalfSpace a) p →
        (∀ (φ : TestFunction (TauCeti.normalHalfSpace a) ℝ ⊤),
            ∫ (x : WithLp 2 (ℝ × E)), Laplacian.laplacian (⇑φ) x • ↑↑(TauCeti.Wkp.value 2 u) x =
              ∫ (x : WithLp 2 (ℝ × E)), φ x • ↑↑f x) →
          ‖TauCeti.Wkp.iteratedGradient 1 u‖ ≤ ↑C * ‖f‖
```

**The Calderón–Zygmund estimate on a half-space, for constant coefficients.** Formalized in Tau Ceti as [`TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_traceCLM_comp_eq_of_normalHalfSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/HalfSpace.html#TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_traceCLM_comp_eq_of_normalHalfSpace).

```lean
TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_traceCLM_comp_eq_of_normalHalfSpace.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {p : ENNReal} [Fact (1 ≤ p)] (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀ {A : WithLp 2 (ℝ × E) →L[ℝ] WithLp 2 (ℝ × E)} {lam : ℝ},
      0 < lam →
        (∀ (ξ : WithLp 2 (ℝ × E)), lam * ‖ξ‖ ^ 2 ≤ inner ℝ (A ξ) ξ) →
          ∀ (a : ℝ) (u : TauCeti.Wkp MeasureTheory.volume (TauCeti.normalHalfSpace a) p 2)
            (f :
              ↥(MeasureTheory.Lp ℝ p (MeasureTheory.volume.restrict ↑(TauCeti.normalHalfSpace a)))),
            TauCeti.Wkp.firstOrder 1 u ∈
                TauCeti.w1p0Submodule MeasureTheory.volume (TauCeti.normalHalfSpace a) p →
              (∀ᵐ (x :
                  WithLp 2 (ℝ × E)) ∂MeasureTheory.volume.restrict ↑(TauCeti.normalHalfSpace a),
                  (TauCeti.traceCLM ℝ (WithLp 2 (ℝ × E)))
                      (A ∘SL ↑↑(TauCeti.Wkp.iteratedGradient 1 u) x) =
                    ↑↑f x) →
                ‖TauCeti.Wkp.iteratedGradient 1 u‖ ≤ ↑C / lam * ‖f‖
```

**The Calderón–Zygmund estimate on a half-space, for strong solutions.** Formalized in Tau Ceti as [`TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_traceCLM_compLpL_eq_of_normalHalfSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/HalfSpace.html#TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_traceCLM_compLpL_eq_of_normalHalfSpace).

```lean
TauCeti.exists_norm_iteratedGradient_le_mul_norm_of_traceCLM_compLpL_eq_of_normalHalfSpace.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {p : ENNReal} [Fact (1 ≤ p)] (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C,
    ∀ (a : ℝ) (u : TauCeti.Wkp MeasureTheory.volume (TauCeti.normalHalfSpace a) p 2)
      (f : ↥(MeasureTheory.Lp ℝ p (MeasureTheory.volume.restrict ↑(TauCeti.normalHalfSpace a)))),
      TauCeti.Wkp.firstOrder 1 u ∈
          TauCeti.w1p0Submodule MeasureTheory.volume (TauCeti.normalHalfSpace a) p →
        (ContinuousLinearMap.compLpL p (MeasureTheory.volume.restrict ↑(TauCeti.normalHalfSpace a))
                (TauCeti.traceCLM ℝ (WithLp 2 (ℝ × E))))
              (TauCeti.Wkp.iteratedGradient 1 u) =
            f →
          ‖TauCeti.Wkp.iteratedGradient 1 u‖ ≤ ↑C * ‖f‖
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_laplacian`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Lp.html#TauCeti.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_laplacian)
- [Source of `TauCeti.exists_eLpNorm_iteratedFDeriv_two_le_eLpNorm_laplacian` in TauCeti/Analysis/PDE/Regularity/Hessian/Lp.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Regularity/Hessian/Lp.lean#L444)
- [Tau Ceti roadmap status: Partial differential equations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/PDE/STATUS.md)
