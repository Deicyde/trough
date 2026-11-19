---
declaration: theorem
origin: cited
lean: TauCeti.PDE.exists_pos_mul_le_sub_of_mul_le_sum_mul_fderiv_fderiv_add_fderiv, TauCeti.PDE.IsIntervalWeakSupersolution.exists_pos_mul_le_intervalRepresentativeL, TauCeti.PDE.IsIntervalWeakSupersolution.pos_of_hasDerivWithinAt_intervalRepresentativeL, TauCeti.PDE.pos_of_hasDerivWithinAt_of_mul_le_sum_mul_fderiv_fderiv_add_fderiv
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

## Proof depends on

- [The fundamental theorem of calculus for a continuous representative](../../sobolev/part-01/the-fundamental-theorem-of-calculus-for-a-contin.md)
- [The fundamental theorem of calculus for weak derivatives](../../sobolev/part-01/the-fundamental-theorem-of-calculus-for-weak-der.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDE.exists_pos_mul_le_sub_of_mul_le_sum_mul_fderiv_fderiv_add_fderiv`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/HopfLemma.html#TauCeti.PDE.exists_pos_mul_le_sub_of_mul_le_sum_mul_fderiv_fderiv_add_fderiv).

## Other forms

**Hopf's boundary-point lemma for weak supersolutions on an interval.** Formalized in Tau Ceti as [`TauCeti.PDE.IsIntervalWeakSupersolution.exists_pos_mul_le_intervalRepresentativeL`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/IntervalHopf.html#TauCeti.PDE.IsIntervalWeakSupersolution.exists_pos_mul_le_intervalRepresentativeL).

```lean
TauCeti.PDE.IsIntervalWeakSupersolution.exists_pos_mul_le_intervalRepresentativeL {x₀ x₁ : ℝ}
  {a b c d : ℝ → ℝ} (hx : x₀ < x₁)
  {u : ↥(TauCeti.W1p MeasureTheory.volume { carrier := Set.Ioo x₀ x₁, is_open' := ⋯ } 2)}
  {lam Λ β : ℝ} (hlam : 0 < lam)
  (ha : ∀ᵐ (y : ℝ) ∂MeasureTheory.volume.restrict (Set.Ioo x₀ x₁), lam ≤ a y)
  (haΛ : ∀ᵐ (y : ℝ) ∂MeasureTheory.volume.restrict (Set.Ioo x₀ x₁), a y ≤ Λ)
  (ham : MeasureTheory.AEStronglyMeasurable a (MeasureTheory.volume.restrict (Set.Ioo x₀ x₁)))
  (hb : ∀ᵐ (y : ℝ) ∂MeasureTheory.volume.restrict (Set.Ioo x₀ x₁), |b y| ≤ β)
  (hbm : MeasureTheory.AEStronglyMeasurable b (MeasureTheory.volume.restrict (Set.Ioo x₀ x₁)))
  (hc : MeasureTheory.MemLp c 2 (MeasureTheory.volume.restrict (Set.Ioo x₀ x₁)))
  (hd : MeasureTheory.IntegrableOn d (Set.Ioo x₀ x₁) MeasureTheory.volume)
  (hsuper : TauCeti.PDE.IsIntervalWeakSupersolution a b c d u)
  (hu₀ : ((TauCeti.W1p.intervalRepresentativeL hx) u) ⟨x₀, ⋯⟩ = 0)
  (hpos :
    ∀ t ∈ Set.Ioo x₀ x₁, 0 < ((TauCeti.W1p.intervalRepresentativeL hx) u) (Set.projIcc x₀ x₁ ⋯ t)) :
  ∃ ε > 0,
    ∃ δ > 0,
      ∀ h ∈ Set.Ioo 0 δ,
        ε * h ≤ ((TauCeti.W1p.intervalRepresentativeL hx) u) (Set.projIcc x₀ x₁ ⋯ (x₀ + h))
```

**Hopf's boundary-point lemma for weak supersolutions on an interval, derivative form.** Formalized in Tau Ceti as [`TauCeti.PDE.IsIntervalWeakSupersolution.pos_of_hasDerivWithinAt_intervalRepresentativeL`](https://taucetiproject.org/docs/TauCeti/Analysis/PDE/MaximumPrinciple/IntervalHopf.html#TauCeti.PDE.IsIntervalWeakSupersolution.pos_of_hasDerivWithinAt_intervalRepresentativeL).

```lean
TauCeti.PDE.IsIntervalWeakSupersolution.pos_of_hasDerivWithinAt_intervalRepresentativeL {x₀ x₁ : ℝ}
  {a b c d : ℝ → ℝ} (hx : x₀ < x₁)
  {u : ↥(TauCeti.W1p MeasureTheory.volume { carrier := Set.Ioo x₀ x₁, is_open' := ⋯ } 2)}
  {lam Λ β : ℝ} (hlam : 0 < lam)
  (ha : ∀ᵐ (y : ℝ) ∂MeasureTheory.volume.restrict (Set.Ioo x₀ x₁), lam ≤ a y)
  (haΛ : ∀ᵐ (y : ℝ) ∂MeasureTheory.volume.restrict (Set.Ioo x₀ x₁), a y ≤ Λ)
  (ham : MeasureTheory.AEStronglyMeasurable a (MeasureTheory.volume.restrict (Set.Ioo x₀ x₁)))
  (hb : ∀ᵐ (y : ℝ) ∂MeasureTheory.volume.restrict (Set.Ioo x₀ x₁), |b y| ≤ β)
  (hbm : MeasureTheory.AEStronglyMeasurable b (MeasureTheory.volume.restrict (Set.Ioo x₀ x₁)))
  (hc : MeasureTheory.MemLp c 2 (MeasureTheory.volume.restrict (Set.Ioo x₀ x₁)))
  (hd : MeasureTheory.IntegrableOn d (Set.Ioo x₀ x₁) MeasureTheory.volume)
  (hsuper : TauCeti.PDE.IsIntervalWeakSupersolution a b c d u)
  (hu₀ : ((TauCeti.W1p.intervalRepresentativeL hx) u) ⟨x₀, ⋯⟩ = 0)
  (hpos :
    ∀ t ∈ Set.Ioo x₀ x₁, 0 < ((TauCeti.W1p.intervalRepresentativeL hx) u) (Set.projIcc x₀ x₁ ⋯ t))
  {u' : ℝ}
  (hd' :
    HasDerivWithinAt (fun t => ((TauCeti.W1p.intervalRepresentativeL hx) u) (Set.projIcc x₀ x₁ ⋯ t))
      u' (Set.Ici x₀) x₀) :
  0 < u'
```

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
- [Source of `TauCeti.PDE.exists_pos_mul_le_sub_of_mul_le_sum_mul_fderiv_fderiv_add_fderiv` in TauCeti/Analysis/PDE/MaximumPrinciple/HopfLemma.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/PDE/MaximumPrinciple/HopfLemma.lean#L309)
