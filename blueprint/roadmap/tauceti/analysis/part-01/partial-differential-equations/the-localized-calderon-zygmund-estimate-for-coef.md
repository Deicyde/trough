---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_lpNorm_smul_iteratedGradient_le_of_sum_mul_inner_eq_of_abs_sub_le
statement: formalized
proof: formalized
---

# The localized Calderón–Zygmund estimate for coefficients of small oscillation

Let `0 < n` and `1 < p < ∞`. There are constants `C` and `δ > 0`, depending only on `n` and `p`,
with the following property. Let `A` be a matrix with `λ ‖ξ‖² ≤ ξᵀ A ξ` and `0 < λ`, let `Ω` be
open, and let `ζ` be smooth with compact support in `Ω`, `‖∇ζ‖ ≤ M₁` and `‖D²ζ‖ ≤ M₂`. Let `a` be
a measurable matrix-valued coefficient on `Ω` with `|aᵢⱼ(x) - Aᵢⱼ| ≤ ε` and `|aᵢⱼ(x)| ≤ Λ` for
almost every `x` in the support of `ζ`, where `ε ≤ δ λ` and `0 ≤ Λ`. Then every
`u ∈ W^{2,p}(Ω)` with `∑ᵢⱼ aᵢⱼ ∂ᵢ∂ⱼu = f` almost everywhere on `Ω`, with `f ∈ Lᵖ(Ω)`, satisfies

`‖ζ D²u‖_{Lᵖ(Ω)} ≤ (C / λ) ‖ζ f‖_{Lᵖ(Ω)} + (C n² Λ / λ + 1) (2 M₁ ‖∇u‖_{Lᵖ(Ω)} + M₂ ‖u‖_{Lᵖ(Ω)})`,

where `D²u` is the weak Hessian `TauCeti.Wkp.iteratedGradient 1 u` and `∇u` is the weak gradient
`TauCeti.Wkp.iteratedGradient 0 (TauCeti.Wkp.lowerOrder 1 u)`. No boundary condition on `u` and
no regularity of `Ω` is assumed.

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

## Depends on

- [TauCeti.Wkp](tauceti-wkp.md)

## Informally uses

- [The Calderón–Zygmund estimate `‖D²u‖_p ≤ C ‖Δu‖_p`](the-calderon-zygmund-estimate-d2u-p-c-u-p.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_lpNorm_smul_iteratedGradient_le_of_sum_mul_inner_eq_of_abs_sub_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Localization.html#TauCeti.PDE.exists_lpNorm_smul_iteratedGradient_le_of_sum_mul_inner_eq_of_abs_sub_le).

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_lpNorm_smul_iteratedGradient_le_of_sum_mul_inner_eq_of_abs_sub_le`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Localization.html#TauCeti.PDE.exists_lpNorm_smul_iteratedGradient_le_of_sum_mul_inner_eq_of_abs_sub_le)
- [Source of `TauCeti.PDE.exists_lpNorm_smul_iteratedGradient_le_of_sum_mul_inner_eq_of_abs_sub_le` in TauCeti/Analysis/PDE/Regularity/Hessian/Localization.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Regularity/Hessian/Localization.lean#L133)
