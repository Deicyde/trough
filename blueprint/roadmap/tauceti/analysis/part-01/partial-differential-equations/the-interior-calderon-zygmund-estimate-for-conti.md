---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_lpNorm_iteratedGradient_le_of_sum_mul_inner_add_inner_add_mul_eq_of_continuousAt, TauCeti.PDE.exists_mul_lpNorm_iteratedGradient_ball_le_of_sum_mul_inner_add_inner_add_mul_eq
statement: formalized
proof: formalized
---

# The interior Calderón–Zygmund estimate for continuous coefficients

Let `0 < n` and
`1 < p < ∞`, let `Ω ⊆ ℝⁿ` be open and `K ⊆ Ω` compact, and let `a` be a matrix-valued coefficient,
measurable on `Ω` and continuous at each `x ∈ K`, such that `a x` is elliptic at each `x ∈ K`,
that is, `λₓ ‖ξ‖² ≤ ξᵀ a(x) ξ` for some `λₓ > 0`. Let `b` and `c` be measurable lower-order
coefficients with `‖b(x)‖ ≤ β` and `|c(x)| ≤ γ` for almost every `x ∈ Ω`. Then there is a
constant `C`, depending on `a`, `β`, `γ`, `K` and `Ω` but not on `u` or `f`, such that every
`u ∈ W^{2,p}(Ω)` with `∑ᵢⱼ aᵢⱼ ∂ᵢ∂ⱼu + ⟪b, ∇u⟫ + c u = f ∈ Lᵖ(Ω)` almost everywhere on `Ω`
satisfies

`‖D²u‖_{Lᵖ(K)} ≤ C (‖f‖_{Lᵖ(Ω)} + ‖u‖_{Lᵖ(Ω)})`,

where `D²u` is the weak Hessian `TauCeti.Wkp.iteratedGradient 1 u` and `∇u` the weak gradient
`TauCeti.Wkp.iteratedGradient 0 (TauCeti.Wkp.lowerOrder 1 u)`. No boundary condition on `u`
and no regularity of `Ω` are assumed, and the gradient of `u` does not appear on the right.

```lean
TauCeti.PDE.exists_lpNorm_iteratedGradient_le_of_sum_mul_inner_add_inner_add_mul_eq_of_continuousAt
  {n : ℕ} {p : ENNReal} [Fact (1 ≤ p)] (hn : 0 < n) (hp : 1 < p) (hp_top : p ≠ ⊤)
  {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ (Fin n))} {K : Set (EuclideanSpace ℝ (Fin n))}
  (hK : IsCompact K) (hKΩ : K ⊆ ↑Omega) {a : EuclideanSpace ℝ (Fin n) → Matrix (Fin n) (Fin n) ℝ}
  (ha : MeasureTheory.AEStronglyMeasurable a (MeasureTheory.volume.restrict ↑Omega))
  (hcont : ∀ x ∈ K, ContinuousAt a x)
  (hell :
    ∀ x ∈ K,
      ∃ lam,
        0 < lam ∧ ∀ (ξ : EuclideanSpace ℝ (Fin n)), lam * ‖ξ‖ ^ 2 ≤ (a x).toQuadraticForm' ξ.ofLp)
  {b : EuclideanSpace ℝ (Fin n) → EuclideanSpace ℝ (Fin n)} {β : ℝ}
  (hb : MeasureTheory.AEStronglyMeasurable b (MeasureTheory.volume.restrict ↑Omega))
  (hbβ : ∀ᵐ (x : EuclideanSpace ℝ (Fin n)) ∂MeasureTheory.volume.restrict ↑Omega, ‖b x‖ ≤ β)
  {c : EuclideanSpace ℝ (Fin n) → ℝ} {γ : ℝ}
  (hc : MeasureTheory.AEStronglyMeasurable c (MeasureTheory.volume.restrict ↑Omega))
  (hcγ : ∀ᵐ (x : EuclideanSpace ℝ (Fin n)) ∂MeasureTheory.volume.restrict ↑Omega, |c x| ≤ γ) :
  ∃ C,
    ∀ (u : TauCeti.Wkp MeasureTheory.volume Omega p 2)
      (f : ↥(MeasureTheory.Lp ℝ p (MeasureTheory.volume.restrict ↑Omega))),
      (∀ᵐ (x : EuclideanSpace ℝ (Fin n)) ∂MeasureTheory.volume.restrict ↑Omega,
          ∑ i,
                  ∑ j,
                    a x i j *
                      inner ℝ ((↑↑(TauCeti.Wkp.iteratedGradient 1 u) x) (EuclideanSpace.single i 1))
                        (EuclideanSpace.single j 1) +
                inner ℝ (b x) (↑↑(TauCeti.Wkp.iteratedGradient 0 (TauCeti.Wkp.lowerOrder 1 u)) x) +
              c x * ↑↑(TauCeti.Wkp.value 2 u) x =
            ↑↑f x) →
        MeasureTheory.lpNorm (↑↑(TauCeti.Wkp.iteratedGradient 1 u)) p
            (MeasureTheory.volume.restrict K) ≤
          C * (‖f‖ + ‖TauCeti.Wkp.value 2 u‖)
```

## Depends on

- [TauCeti.Wkp](tauceti-wkp.md)

## Proof depends on

- [Hölder's inequality for Young's exponents](../../../measure-theory/euclidean-isoperimetry-sharp-inequalities-and-ri/part-02/holders-inequality-for-youngs-exponents.md)
- [The localized Calderón–Zygmund estimate for coefficients of small oscillation](the-localized-calderon-zygmund-estimate-for-coef.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_lpNorm_iteratedGradient_le_of_sum_mul_inner_add_inner_add_mul_eq_of_continuousAt`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/ContinuousCoefficient.html#TauCeti.PDE.exists_lpNorm_iteratedGradient_le_of_sum_mul_inner_add_inner_add_mul_eq_of_continuousAt).

## Other forms

**The interior Calderón–Zygmund estimate on balls for coefficients of small oscillation.** Formalized in Tau Ceti as [`TauCeti.PDE.exists_mul_lpNorm_iteratedGradient_ball_le_of_sum_mul_inner_add_inner_add_mul_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/Interior.html#TauCeti.PDE.exists_mul_lpNorm_iteratedGradient_ball_le_of_sum_mul_inner_add_inner_add_mul_eq).

```lean
TauCeti.PDE.exists_mul_lpNorm_iteratedGradient_ball_le_of_sum_mul_inner_add_inner_add_mul_eq {n : ℕ}
  {p : ENNReal} [Fact (1 ≤ p)] (hn : 0 < n) (hp : 1 < p) (hp_top : p ≠ ⊤) :
  ∃ C δ,
    0 < δ ∧
      ∀ {A : Matrix (Fin n) (Fin n) ℝ} {lam : ℝ},
        0 < lam →
          (∀ (ξ : EuclideanSpace ℝ (Fin n)), lam * ‖ξ‖ ^ 2 ≤ A.toQuadraticForm' ξ.ofLp) →
            ∀ {Omega : TopologicalSpace.Opens (EuclideanSpace ℝ (Fin n))}
              {x₀ : EuclideanSpace ℝ (Fin n)} {r R : ℝ},
              r < R →
                Metric.ball x₀ R ⊆ ↑Omega →
                  ∀ {a : EuclideanSpace ℝ (Fin n) → Matrix (Fin n) (Fin n) ℝ}
                    {b : EuclideanSpace ℝ (Fin n) → EuclideanSpace ℝ (Fin n)}
                    {c : EuclideanSpace ℝ (Fin n) → ℝ} {ε Λ β γ : ℝ},
                    MeasureTheory.AEStronglyMeasurable a
                        (MeasureTheory.volume.restrict (Metric.ball x₀ R)) →
                      ε ≤ δ * lam →
                        (∀ᵐ (x : EuclideanSpace ℝ (Fin n)),
                            x ∈ Metric.ball x₀ R → ∀ (i j : Fin n), |a x i j - A i j| ≤ ε) →
                          (∀ᵐ (x : EuclideanSpace ℝ (Fin n)),
                              x ∈ Metric.ball x₀ R → ∀ (i j : Fin n), |a x i j| ≤ Λ) →
                            MeasureTheory.AEStronglyMeasurable b
                                (MeasureTheory.volume.restrict (Metric.ball x₀ R)) →
                              (∀ᵐ (x : EuclideanSpace ℝ (Fin n)),
                                  x ∈ Metric.ball x₀ R → ‖b x‖ ≤ β) →
                                MeasureTheory.AEStronglyMeasurable c
                                    (MeasureTheory.volume.restrict (Metric.ball x₀ R)) →
                                  (∀ᵐ (x : EuclideanSpace ℝ (Fin n)),
                                      x ∈ Metric.ball x₀ R → |c x| ≤ γ) →
                                    ∀ (u : TauCeti.Wkp MeasureTheory.volume Omega p 2)
                                      (f : EuclideanSpace ℝ (Fin n) → ℝ),
                                      (∀ᵐ (x :
                                          EuclideanSpace ℝ
                                            (Fin
                                              n)) ∂MeasureTheory.volume.restrict (Metric.ball x₀ R),
                                          ∑ i,
                                                  ∑ j,
                                                    a x i j *
                                                      inner ℝ
                                                        ((↑↑(TauCeti.Wkp.iteratedGradient 1 u) x)
                                                          (EuclideanSpace.single i 1))
                                                        (EuclideanSpace.single j 1) +
                                                inner ℝ (b x)
                                                  (↑↑(TauCeti.Wkp.iteratedGradient 0
                                                          (TauCeti.Wkp.lowerOrder 1 u))
                                                    x) +
                                              c x * ↑↑(TauCeti.Wkp.value 2 u) x =
                                            f x) →
                                        (R - r) ^ 2 *
                                            MeasureTheory.lpNorm
                                              (↑↑(TauCeti.Wkp.iteratedGradient 1 u)) p
                                              (MeasureTheory.volume.restrict (Metric.ball x₀ r)) ≤
                                          ↑C *
                                            (R ^ 2 / lam *
                                                MeasureTheory.lpNorm f p
                                                  (MeasureTheory.volume.restrict
                                                    (Metric.ball x₀ R)) +
                                              (1 + (Λ + β * R + γ * R ^ 2) / lam) ^ 2 *
                                                MeasureTheory.lpNorm (↑↑(TauCeti.Wkp.value 2 u)) p
                                                  (MeasureTheory.volume.restrict
                                                    (Metric.ball x₀ R)))
```

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_lpNorm_iteratedGradient_le_of_sum_mul_inner_add_inner_add_mul_eq_of_continuousAt`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/Regularity/Hessian/ContinuousCoefficient.html#TauCeti.PDE.exists_lpNorm_iteratedGradient_le_of_sum_mul_inner_add_inner_add_mul_eq_of_continuousAt)
- [Source of `TauCeti.PDE.exists_lpNorm_iteratedGradient_le_of_sum_mul_inner_add_inner_add_mul_eq_of_continuousAt` in TauCeti/Analysis/PDE/Regularity/Hessian/ContinuousCoefficient.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/PDE/Regularity/Hessian/ContinuousCoefficient.lean#L160)
