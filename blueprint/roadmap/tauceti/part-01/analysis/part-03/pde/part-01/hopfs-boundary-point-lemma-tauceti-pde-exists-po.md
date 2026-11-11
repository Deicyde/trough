---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_pos_mul_le_sub_of_mul_le_sum_mul_fderiv_fderiv_add_fderiv, TauCeti.PDE.pos_of_hasDerivWithinAt_of_mul_le_sum_mul_fderiv_fderiv_add_fderiv
statement: formalized
proof: formalized
---

# Hopf's boundary-point lemma (`TauCeti.PDE.exists_pos_mul_le_sub_of_mul_le_sum_mul_fderiv_fderiv_add_fderiv`)

**Hopf's boundary-point lemma** for the elliptic operator in non-divergence form
`L u = ∑ᵢⱼ aⁱʲ ∂ᵢ∂ⱼu + bⁱ ∂ᵢu` with zeroth-order coefficient `c`. Let `B = ball y R` and let
`x₀` lie on its bounding sphere. On `B` let `a` be elliptic, `λ ‖ξ‖² ≤ ξᵀ a ξ` with `λ > 0`, with
trace at most `Λ`, let `‖b‖ ≤ β` and `c ≤ γ`. Let `u` be `C²` in `B`, continuous at `x₀` relative
to `B`, a subsolution `c u ≤ L u` there, and strictly below `u x₀` in `B`. If `c = 0`, or `c ≥ 0`
and `u x₀ ≥ 0`, or `u x₀ = 0`, then along the inward normal the difference quotient
`(u x₀ - u (x₀ - t ν)) / t`, with `ν = (x₀ - y) / R` the outer unit normal of `B` at `x₀`, is
bounded below by a positive constant for all small `t > 0`.

In Gilbarg–Trudinger's notation the subsolution condition `c u ≤ L u` reads `L' u ≥ 0` for
`L' = L - c`, so their sign condition `c ≤ 0` is `c ≥ 0` here. Nothing is assumed of `u` or of the
coefficients outside `B`, the coefficients need no regularity, not even measurability, and `a`
need not be symmetric.

```lean
TauCeti.PDE.exists_pos_mul_le_sub_of_mul_le_sum_mul_fderiv_fderiv_add_fderiv.{u_1} {ι : Type u_1}
  [Fintype ι] [DecidableEq ι] {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
  {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {c u : EuclideanSpace ℝ ι → ℝ}
  {y x₀ : EuclideanSpace ℝ ι} {R lam Λ β γ : ℝ} (hR : 0 < R) (hx₀ : x₀ ∈ Metric.sphere y R)
  (hlam : 0 < lam)
  (ha :
    ∀ x ∈ Metric.ball y R,
      ∀ (ξ : EuclideanSpace ℝ ι), lam * ‖ξ‖ ^ 2 ≤ (a x).toQuadraticForm' ξ.ofLp)
  (htr : ∀ x ∈ Metric.ball y R, (a x).trace ≤ Λ) (hb : ∀ x ∈ Metric.ball y R, ‖b x‖ ≤ β)
  (hcγ : ∀ x ∈ Metric.ball y R, c x ≤ γ) (hcd : ∀ x ∈ Metric.ball y R, ContDiffAt ℝ 2 u x)
  (hcont : ContinuousWithinAt u (Metric.ball y R) x₀)
  (hsub :
    ∀ x ∈ Metric.ball y R,
      c x * u x ≤
        ∑ i,
            ∑ j,
              a x i j *
                ((fderiv ℝ (fderiv ℝ u) x) (EuclideanSpace.single i 1))
                  (EuclideanSpace.single j 1) +
          (fderiv ℝ u x) (b x))
  (hlt : ∀ x ∈ Metric.ball y R, u x < u x₀)
  (hsign :
    (∀ x ∈ Metric.ball y R, c x = 0) ∨ (∀ x ∈ Metric.ball y R, 0 ≤ c x) ∧ 0 ≤ u x₀ ∨ u x₀ = 0) :
  ∃ ε > 0, ∃ δ > 0, ∀ t ∈ Set.Ioo 0 δ, ε * t ≤ u x₀ - u (x₀ - t • R⁻¹ • (x₀ - y))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_pos_mul_le_sub_of_mul_le_sum_mul_fderiv_fderiv_add_fderiv`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/HopfLemma.html#TauCeti.PDE.exists_pos_mul_le_sub_of_mul_le_sum_mul_fderiv_fderiv_add_fderiv).

## Other forms

**Hopf's boundary-point lemma, derivative form.** Formalized in Tau Ceti as [`TauCeti.PDE.pos_of_hasDerivWithinAt_of_mul_le_sum_mul_fderiv_fderiv_add_fderiv`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/HopfLemma.html#TauCeti.PDE.pos_of_hasDerivWithinAt_of_mul_le_sum_mul_fderiv_fderiv_add_fderiv).

```lean
TauCeti.PDE.pos_of_hasDerivWithinAt_of_mul_le_sum_mul_fderiv_fderiv_add_fderiv.{u_1} {ι : Type u_1}
  [Fintype ι] [DecidableEq ι] {a : EuclideanSpace ℝ ι → Matrix ι ι ℝ}
  {b : EuclideanSpace ℝ ι → EuclideanSpace ℝ ι} {c u : EuclideanSpace ℝ ι → ℝ}
  {y x₀ : EuclideanSpace ℝ ι} {R lam Λ β γ : ℝ} (hR : 0 < R) (hx₀ : x₀ ∈ Metric.sphere y R)
  (hlam : 0 < lam)
  (ha :
    ∀ x ∈ Metric.ball y R,
      ∀ (ξ : EuclideanSpace ℝ ι), lam * ‖ξ‖ ^ 2 ≤ (a x).toQuadraticForm' ξ.ofLp)
  (htr : ∀ x ∈ Metric.ball y R, (a x).trace ≤ Λ) (hb : ∀ x ∈ Metric.ball y R, ‖b x‖ ≤ β)
  (hcγ : ∀ x ∈ Metric.ball y R, c x ≤ γ) (hcd : ∀ x ∈ Metric.ball y R, ContDiffAt ℝ 2 u x)
  (hcont : ContinuousWithinAt u (Metric.ball y R) x₀)
  (hsub :
    ∀ x ∈ Metric.ball y R,
      c x * u x ≤
        ∑ i,
            ∑ j,
              a x i j *
                ((fderiv ℝ (fderiv ℝ u) x) (EuclideanSpace.single i 1))
                  (EuclideanSpace.single j 1) +
          (fderiv ℝ u x) (b x))
  (hlt : ∀ x ∈ Metric.ball y R, u x < u x₀)
  (hsign :
    (∀ x ∈ Metric.ball y R, c x = 0) ∨ (∀ x ∈ Metric.ball y R, 0 ≤ c x) ∧ 0 ≤ u x₀ ∨ u x₀ = 0)
  {d : ℝ} (hd : HasDerivWithinAt (fun t => u (x₀ + t • R⁻¹ • (x₀ - y))) d (Set.Iic 0) 0) : 0 < d
```

## Sources

- [Tau Ceti documentation: `TauCeti.PDE.exists_pos_mul_le_sub_of_mul_le_sum_mul_fderiv_fderiv_add_fderiv`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/HopfLemma.html#TauCeti.PDE.exists_pos_mul_le_sub_of_mul_le_sum_mul_fderiv_fderiv_add_fderiv)
- [Source of `TauCeti.PDE.exists_pos_mul_le_sub_of_mul_le_sum_mul_fderiv_fderiv_add_fderiv` in TauCeti/Analysis/PDE/MaximumPrinciple/HopfLemma.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/PDE/MaximumPrinciple/HopfLemma.lean#L309)
