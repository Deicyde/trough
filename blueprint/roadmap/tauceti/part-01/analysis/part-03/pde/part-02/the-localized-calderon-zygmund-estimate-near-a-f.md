---
declaration: theorem
origin: cited
lean: TauCeti.exists_lpNorm_smul_iteratedGradient_le_of_traceCLM_comp_eq_of_norm_sub_le_of_normalHalfSpace, TauCeti.PDE.exists_lpNorm_smul_iteratedGradient_le_of_sum_mul_inner_eq_of_abs_sub_le
statement: formalized
proof: formalized
---

# The localized Calderón–Zygmund estimate near a flat boundary

Let `1 < p < ∞`. There are
constants `C` and `δ > 0`, depending only on `E` and `p`, with the following property. Let
`H = {x | a < x.fst}` be a half-space of `ℝ × E`, and let `Ω` and `U` be open with `Ω ∩ U = H ∩ U`.
Let `A₀` be an operator on `ℝ × E` with `λ ‖ξ‖² ≤ ⟪A₀ ξ, ξ⟫` and `0 < λ`, and let `ζ` be smooth with
compact support in `U`, `‖∇ζ‖ ≤ M₁` and `‖D²ζ‖ ≤ M₂`. Let `A` be a field of endomorphisms of
`ℝ × E`, measurable on `Ω`, with `‖A x - A₀‖ ≤ ε` and `‖A x‖ ≤ Λ` for almost every `x ∈ Ω` in the
support of `ζ`, where `ε ≤ δ λ` and `0 ≤ Λ`. Then every `u ∈ W^{2,p}(Ω)` with `ζ u ∈ W^{1,p}_0(Ω)`
which solves `tr (A ∘ D²u) = f` almost everywhere on `Ω`, with `f ∈ Lᵖ(Ω)`, satisfies

`‖ζ D²u‖_{Lᵖ(Ω)} ≤ (C / λ) ‖ζ f‖_{Lᵖ(Ω)} + (C N Λ / λ + 1) (2 M₁ ‖∇u‖_{Lᵖ(Ω)} + M₂ ‖u‖_{Lᵖ(Ω)})`,

where `N` is the dimension of `ℝ × E`, `D²u` is the weak Hessian
`TauCeti.Wkp.iteratedGradient 1 u` and `∇u` is the weak gradient
`TauCeti.Wkp.iteratedGradient 0 (TauCeti.Wkp.lowerOrder 1 u)`. The support of `ζ` may meet the
boundary hyperplane, and nothing is assumed about `∂Ω` outside `U`.

```lean
TauCeti.exists_lpNorm_smul_iteratedGradient_le_of_traceCLM_comp_eq_of_norm_sub_le_of_normalHalfSpace.{u_1}
  {E : Type u_1} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [MeasurableSpace E] [BorelSpace E] {p : ENNReal} [Fact (1 ≤ p)] (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C δ,
    0 < δ ∧
      ∀ (a : ℝ) {A₀ : WithLp 2 (ℝ × E) →L[ℝ] WithLp 2 (ℝ × E)} {lam : ℝ},
        0 < lam →
          (∀ (ξ : WithLp 2 (ℝ × E)), lam * ‖ξ‖ ^ 2 ≤ inner ℝ (A₀ ξ) ξ) →
            ∀ {Omega U : TopologicalSpace.Opens (WithLp 2 (ℝ × E))},
              ↑Omega ∩ ↑U = ↑(TauCeti.normalHalfSpace a) ∩ ↑U →
                ∀ {zeta : WithLp 2 (ℝ × E) → ℝ} {M₁ M₂ : ℝ},
                  ContDiff ℝ (↑⊤) zeta →
                    HasCompactSupport zeta →
                      tsupport zeta ⊆ ↑U →
                        (∀ (x : WithLp 2 (ℝ × E)), ‖gradient zeta x‖ ≤ M₁) →
                          (∀ (x : WithLp 2 (ℝ × E)), ‖fderiv ℝ (gradient zeta) x‖ ≤ M₂) →
                            ∀ {A : WithLp 2 (ℝ × E) → WithLp 2 (ℝ × E) →L[ℝ] WithLp 2 (ℝ × E)}
                              {ε Λ : ℝ},
                              MeasureTheory.AEStronglyMeasurable A
                                  (MeasureTheory.volume.restrict ↑Omega) →
                                ε ≤ δ * lam →
                                  (∀ᵐ (x : WithLp 2 (ℝ × E)) ∂MeasureTheory.volume.restrict ↑Omega,
                                      x ∈ tsupport zeta → ‖A x - A₀‖ ≤ ε) →
                                    0 ≤ Λ →
                                      (∀ᵐ (x :
                                          WithLp 2 (ℝ × E)) ∂MeasureTheory.volume.restrict ↑Omega,
                                          x ∈ tsupport zeta → ‖A x‖ ≤ Λ) →
                                        ∀ (u : TauCeti.Wkp MeasureTheory.volume Omega p 2)
                                          (f :
                                            ↥(MeasureTheory.Lp ℝ p
                                                (MeasureTheory.volume.restrict ↑Omega))),
                                          (∃ v,
                                              ↑↑(TauCeti.W1p.value
                                                      ↑v) =ᵐ[MeasureTheory.volume.restrict ↑Omega]
                                                fun x => zeta x * ↑↑(TauCeti.Wkp.value 2 u) x) →
                                            (∀ᵐ (x :
                                                WithLp 2
                                                  (ℝ × E)) ∂MeasureTheory.volume.restrict ↑Omega,
                                                (TauCeti.traceCLM ℝ (WithLp 2 (ℝ × E)))
                                                    (A x ∘SL
                                                      ↑↑(TauCeti.Wkp.iteratedGradient 1 u) x) =
                                                  ↑↑f x) →
                                              MeasureTheory.lpNorm
                                                  (fun x =>
                                                    zeta x • ↑↑(TauCeti.Wkp.iteratedGradient 1 u) x)
                                                  p (MeasureTheory.volume.restrict ↑Omega) ≤
                                                ↑C / lam *
                                                    MeasureTheory.lpNorm (fun x => zeta x * ↑↑f x) p
                                                      (MeasureTheory.volume.restrict ↑Omega) +
                                                  (↑C / lam *
                                                          ↑(Module.finrank ℝ (WithLp 2 (ℝ × E))) *
                                                        Λ +
                                                      1) *
                                                    (2 * M₁ *
                                                        ‖TauCeti.Wkp.iteratedGradient 0
                                                            (TauCeti.Wkp.lowerOrder 1 u)‖ +
                                                      M₂ * ‖TauCeti.Wkp.value 2 u‖)
```

## Depends on

- [TauCeti.Wkp](../../../part-01/partial-differential-equations/tauceti-wkp.md)

## Informally uses

- [The Calderón–Zygmund estimate `‖D²u‖_p ≤ C ‖Δu‖_p`](../part-01/the-calderon-zygmund-estimate-d2u-p-c-u-p.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_lpNorm_smul_iteratedGradient_le_of_traceCLM_comp_eq_of_norm_sub_le_of_normalHalfSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/HalfSpace/Localization.html#TauCeti.exists_lpNorm_smul_iteratedGradient_le_of_traceCLM_comp_eq_of_norm_sub_le_of_normalHalfSpace).

## Other forms

**The localized Calderón–Zygmund estimate for coefficients of small oscillation.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_lpNorm_smul_iteratedGradient_le_of_sum_mul_inner_eq_of_abs_sub_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Localization.html#TauCeti.PDE.exists_lpNorm_smul_iteratedGradient_le_of_sum_mul_inner_eq_of_abs_sub_le).

```lean
TauCeti.PDE.exists_lpNorm_smul_iteratedGradient_le_of_sum_mul_inner_eq_of_abs_sub_le {n : ℕ}
  {p : ENNReal} [Fact (1 ≤ p)] (hn : 0 < n) (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C δ,
    0 < δ ∧
      ∀ {A : Matrix (Fin n) (Fin n) ℝ} {lam : ℝ},
        0 < lam →
          (∀ (ξ : EuclideanSpace ℝ (Fin n)), lam * ‖ξ‖ ^ 2 ≤ A.toQuadraticForm' ξ.ofLp) →
            ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ (Fin n))}
              {zeta : EuclideanSpace ℝ (Fin n) → ℝ} {M₁ M₂ : ℝ},
              ContDiff ℝ (↑⊤) zeta →
                HasCompactSupport zeta →
                  tsupport zeta ⊆ ↑Omega →
                    (∀ (x : EuclideanSpace ℝ (Fin n)), ‖gradient zeta x‖ ≤ M₁) →
                      (∀ (x : EuclideanSpace ℝ (Fin n)), ‖fderiv ℝ (gradient zeta) x‖ ≤ M₂) →
                        ∀ {a : EuclideanSpace ℝ (Fin n) → Matrix (Fin n) (Fin n) ℝ} {ε Λ : ℝ},
                          MeasureTheory.AEStronglyMeasurable a
                              (MeasureTheory.volume.restrict ↑Omega) →
                            ε ≤ δ * lam →
                              (∀ᵐ (x : EuclideanSpace ℝ (Fin n)),
                                  x ∈ tsupport zeta → ∀ (i j : Fin n), |a x i j - A i j| ≤ ε) →
                                0 ≤ Λ →
                                  (∀ᵐ (x : EuclideanSpace ℝ (Fin n)),
                                      x ∈ tsupport zeta → ∀ (i j : Fin n), |a x i j| ≤ Λ) →
                                    ∀ (u : TauCeti.Wkp MeasureTheory.volume Omega p 2)
                                      (f :
                                        ↥(MeasureTheory.Lp ℝ p
                                            (MeasureTheory.volume.restrict ↑Omega))),
                                      (∀ᵐ (x :
                                          EuclideanSpace ℝ
                                            (Fin n)) ∂MeasureTheory.volume.restrict ↑Omega,
                                          ∑ i,
                                              ∑ j,
                                                a x i j *
                                                  inner ℝ
                                                    ((↑↑(TauCeti.Wkp.iteratedGradient 1 u) x)
                                                      (EuclideanSpace.single i 1))
                                                    (EuclideanSpace.single j 1) =
                                            ↑↑f x) →
                                        MeasureTheory.lpNorm
                                            (fun x =>
                                              zeta x • ↑↑(TauCeti.Wkp.iteratedGradient 1 u) x)
                                            p (MeasureTheory.volume.restrict ↑Omega) ≤
                                          ↑C / lam *
                                              MeasureTheory.lpNorm (fun x => zeta x * ↑↑f x) p
                                                (MeasureTheory.volume.restrict ↑Omega) +
                                            (↑C / lam * ↑n ^ 2 * Λ + 1) *
                                              (2 * M₁ *
                                                  ‖TauCeti.Wkp.iteratedGradient 0
                                                      (TauCeti.Wkp.lowerOrder 1 u)‖ +
                                                M₂ * ‖TauCeti.Wkp.value 2 u‖)
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_lpNorm_smul_iteratedGradient_le_of_traceCLM_comp_eq_of_norm_sub_le_of_normalHalfSpace`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/HalfSpace/Localization.html#TauCeti.exists_lpNorm_smul_iteratedGradient_le_of_traceCLM_comp_eq_of_norm_sub_le_of_normalHalfSpace)
- [Source of `TauCeti.exists_lpNorm_smul_iteratedGradient_le_of_traceCLM_comp_eq_of_norm_sub_le_of_normalHalfSpace` in TauCeti/Analysis/PDE/Regularity/Hessian/HalfSpace/Localization.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/Regularity/Hessian/HalfSpace/Localization.lean#L168)
