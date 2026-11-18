---
declaration: theorem
origin: cited
lean: TauCeti.IsSobolevCRCoefficients.integral_inner_crFormalAdjoint, TauCeti.integral_ball_smul_conjWirtingerDeriv_add_eq_circleIntegral, TauCeti.setIntegral_halfDisc_inner_cauchyRiemann_adjoint, TauCeti.setIntegral_im_pos_inner_cauchyRiemann_adjoint, TauCeti.integral_ball_smul_conjWirtingerDeriv_eq_circleIntegral_of_diffContOnCl, TauCeti.setIntegral_halfDisc_inner_crFormalAdjoint, TauCeti.setIntegral_im_pos_inner_crFormalAdjoint, TauCeti.integral_ball_re_mul_conjWirtingerDeriv_eq
statement: formalized
proof: formalized
---

# Green's formula

**Green's formula** for the real Cauchy–Riemann operator with Sobolev coefficients. If `ξ`
has weak derivative `Dξ` on `Ω`, with `ξ` and `Dξ` locally `L^q`, and `1/p + 1/q ≤ 1` with
finite `p, q`, then for every test function `φ`,

`∫ ⟪D* φ, ξ⟫ = ∫ ⟪φ, Dξ 1 + J (Dξ I) + S ξ⟫`.

The `∂_t J` term of `D*` cancels the derivative of `J` in the weak Leibniz rule for `J ξ`.

```lean
TauCeti.IsSobolevCRCoefficients.integral_inner_crFormalAdjoint.{u_1} {V : Type u_1}
  [NormedAddCommGroup V] [InnerProductSpace ℝ V] [CompleteSpace V] {Ω : TopologicalSpace.Opens ℂ}
  {p q : ENNReal} {J S : ℂ → V →L[ℝ] V} {DJ : ℂ → ℂ →L[ℝ] V →L[ℝ] V} {ξ : ℂ → V}
  [FiniteDimensional ℝ V] (hc : TauCeti.IsSobolevCRCoefficients p Ω J DJ S) (hpq : p⁻¹ + q⁻¹ ≤ 1)
  (hp : p ≠ ⊤) (hq : q ≠ ⊤) {Dξ : ℂ → ℂ →L[ℝ] V}
  (hξ : TauCeti.HasWeakFDerivOn MeasureTheory.volume Ω ξ Dξ) (hξq : TauCeti.MemLpLoc q (↑Ω) ξ)
  (hDξq : TauCeti.MemLpLoc q (↑Ω) Dξ) (φ : TestFunction Ω V ⊤) :
  ∫ (z : ℂ), inner ℝ (TauCeti.crFormalAdjoint J DJ S (⇑φ) z) (ξ z) =
    ∫ (z : ℂ), inner ℝ (φ z) ((Dξ z) 1 + (J z) ((Dξ z) Complex.I) + (S z) (ξ z))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hölder's inequality on compact subsets](holders-inequality-on-compact-subsets.md)
- [Stokes' formula for `\bar∂` on a disc](../../part-03/complex/part-04/stokes-formula-for-bar-on-a-disc.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsSobolevCRCoefficients.integral_inner_crFormalAdjoint`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/CauchyRiemann/RoughCoefficients/Weak.html#TauCeti.IsSobolevCRCoefficients.integral_inner_crFormalAdjoint).

## Other forms

**Green's formula for `\bar∂` with boundary term.** Formalized in Tau Ceti as [`TauCeti.integral_ball_smul_conjWirtingerDeriv_add_eq_circleIntegral`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/Green.html#TauCeti.integral_ball_smul_conjWirtingerDeriv_add_eq_circleIntegral).

```lean
TauCeti.integral_ball_smul_conjWirtingerDeriv_add_eq_circleIntegral.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] {g : ℂ → ℂ} {ξ : ℂ → E} {c : ℂ} {r : ℝ} (hr : 0 ≤ r)
  (hg : ∀ z ∈ Metric.closedBall c r, ContDiffAt ℝ 1 g z)
  (hξ : ∀ z ∈ Metric.closedBall c r, ContDiffAt ℝ 1 ξ z) :
  ∫ (z : ℂ) in Metric.ball c r,
      g z • (TauCeti.conjWirtingerDeriv ξ z) 1 + (TauCeti.conjWirtingerDeriv g z) 1 • ξ z =
    (2 * Complex.I)⁻¹ • ∮ (z : ℂ) in C(c, r), g z • ξ z
```

**Green's formula for `∂_s + J ∂_t + S` on the half-disc.** Formalized in Tau Ceti as [`TauCeti.setIntegral_halfDisc_inner_cauchyRiemann_adjoint`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/HalfPlaneAdjoint/Variable.html#TauCeti.setIntegral_halfDisc_inner_cauchyRiemann_adjoint).

```lean
TauCeti.setIntegral_halfDisc_inner_cauchyRiemann_adjoint.{u_1} {V : Type u_1} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [CompleteSpace V] {φ ξ : ℂ → V} {J S : ℂ → V →L[ℝ] V} {r : ℝ}
  (hφ : ContDiff ℝ 1 φ) (hξ : ContDiffOn ℝ 1 ξ (Metric.ball 0 r))
  (hJ : ContDiffOn ℝ 1 J (Metric.ball 0 r)) (hS : ContinuousOn S (Metric.ball 0 r))
  (hφr : tsupport φ ⊆ Metric.ball 0 r) :
  ∫ (z : ℂ) in Metric.ball 0 r ∩ {z | 0 < z.im},
      inner ℝ
        ((fderiv ℝ φ z) 1 + (ContinuousLinearMap.adjoint (J z)) ((fderiv ℝ φ z) Complex.I) -
          (ContinuousLinearMap.adjoint (S z)) (φ z))
        (ξ z) =
    (-∫ (z : ℂ) in Metric.ball 0 r ∩ {z | 0 < z.im},
          inner ℝ (φ z)
            ((fderiv ℝ ξ z) 1 + (J z) ((fderiv ℝ ξ z) Complex.I) + (S z) (ξ z) +
              ((fderiv ℝ J z) Complex.I) (ξ z))) -
      ∫ (s : ℝ) in Set.Ioo (-r) r, inner ℝ (φ ↑s) ((J ↑s) (ξ ↑s))
```

**Green's formula for `∂_s + J ∂_t + S` on the half-plane.** Formalized in Tau Ceti as [`TauCeti.setIntegral_im_pos_inner_cauchyRiemann_adjoint`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/HalfPlaneAdjoint/Variable.html#TauCeti.setIntegral_im_pos_inner_cauchyRiemann_adjoint).

```lean
TauCeti.setIntegral_im_pos_inner_cauchyRiemann_adjoint.{u_1} {V : Type u_1} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [CompleteSpace V] {φ ξ : ℂ → V} {J S : ℂ → V →L[ℝ] V} {U : Set ℂ}
  (hφ : ContDiff ℝ 1 φ) (hφc : HasCompactSupport φ) (hU : IsOpen U) (hξ : ContDiffOn ℝ 1 ξ U)
  (hJ : ContDiffOn ℝ 1 J U) (hS : ContinuousOn S U) (hφU : tsupport φ ⊆ U) :
  ∫ (z : ℂ) in {z | 0 < z.im},
      inner ℝ
        ((fderiv ℝ φ z) 1 + (ContinuousLinearMap.adjoint (J z)) ((fderiv ℝ φ z) Complex.I) -
          (ContinuousLinearMap.adjoint (S z)) (φ z))
        (ξ z) =
    (-∫ (z : ℂ) in {z | 0 < z.im},
          inner ℝ (φ z)
            ((fderiv ℝ ξ z) 1 + (J z) ((fderiv ℝ ξ z) Complex.I) + (S z) (ξ z) +
              ((fderiv ℝ J z) Complex.I) (ξ z))) -
      ∫ (s : ℝ), inner ℝ (φ ↑s) ((J ↑s) (ξ ↑s))
```

**Green's formula for a holomorphic factor.** Formalized in Tau Ceti as [`TauCeti.integral_ball_smul_conjWirtingerDeriv_eq_circleIntegral_of_diffContOnCl`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/Green.html#TauCeti.integral_ball_smul_conjWirtingerDeriv_eq_circleIntegral_of_diffContOnCl).

```lean
TauCeti.integral_ball_smul_conjWirtingerDeriv_eq_circleIntegral_of_diffContOnCl.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] {g : ℂ → ℂ} {ξ : ℂ → E} {c : ℂ} {R : ℝ} (hR : 0 < R)
  (hg : DiffContOnCl ℂ g (Metric.ball c R)) (hξ : ∀ z ∈ Metric.closedBall c R, ContDiffAt ℝ 1 ξ z) :
  ∫ (z : ℂ) in Metric.ball c R, g z • (TauCeti.conjWirtingerDeriv ξ z) 1 =
    (2 * Complex.I)⁻¹ • ∮ (z : ℂ) in C(c, R), g z • ξ z
```

**Green's formula for the formal adjoint on the half-disc.** Formalized in Tau Ceti as [`TauCeti.setIntegral_halfDisc_inner_crFormalAdjoint`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/HalfPlaneAdjoint/Dual.html#TauCeti.setIntegral_halfDisc_inner_crFormalAdjoint).

```lean
TauCeti.setIntegral_halfDisc_inner_crFormalAdjoint.{u_1} {V : Type u_1} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [CompleteSpace V] {φ ξ : ℂ → V} {J S : ℂ → V →L[ℝ] V} {r : ℝ}
  (hφ : ContDiffOn ℝ 1 φ (Metric.ball 0 r)) (hξ : ContDiffOn ℝ 1 ξ (Metric.ball 0 r))
  (hJ : ContDiffOn ℝ 1 J (Metric.ball 0 r)) (hS : ContinuousOn S (Metric.ball 0 r))
  (hφξr : tsupport φ ∩ tsupport ξ ⊆ Metric.ball 0 r) :
  ∫ (z : ℂ) in Metric.ball 0 r ∩ {z | 0 < z.im},
      inner ℝ (TauCeti.crFormalAdjoint J (fderiv ℝ J) S φ z) (ξ z) =
    (∫ (z : ℂ) in Metric.ball 0 r ∩ {z | 0 < z.im},
        inner ℝ (φ z) ((fderiv ℝ ξ z) 1 + (J z) ((fderiv ℝ ξ z) Complex.I) + (S z) (ξ z))) +
      ∫ (s : ℝ) in Set.Ioo (-r) r, inner ℝ (φ ↑s) ((J ↑s) (ξ ↑s))
```

**Green's formula for the formal adjoint on the half-plane.** Formalized in Tau Ceti as [`TauCeti.setIntegral_im_pos_inner_crFormalAdjoint`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/HalfPlaneAdjoint/Dual.html#TauCeti.setIntegral_im_pos_inner_crFormalAdjoint).

```lean
TauCeti.setIntegral_im_pos_inner_crFormalAdjoint.{u_1} {V : Type u_1} [NormedAddCommGroup V]
  [InnerProductSpace ℝ V] [CompleteSpace V] {φ ξ : ℂ → V} {J S : ℂ → V →L[ℝ] V} {U : Set ℂ}
  (hU : IsOpen U) (hφ : ContDiffOn ℝ 1 φ U) (hξ : ContDiffOn ℝ 1 ξ U) (hJ : ContDiffOn ℝ 1 J U)
  (hS : ContinuousOn S U) (hc : IsCompact (tsupport φ ∩ tsupport ξ))
  (hφξU : tsupport φ ∩ tsupport ξ ⊆ U) :
  ∫ (z : ℂ) in {z | 0 < z.im}, inner ℝ (TauCeti.crFormalAdjoint J (fderiv ℝ J) S φ z) (ξ z) =
    (∫ (z : ℂ) in {z | 0 < z.im},
        inner ℝ (φ z) ((fderiv ℝ ξ z) 1 + (J z) ((fderiv ℝ ξ z) Complex.I) + (S z) (ξ z))) +
      ∫ (s : ℝ), inner ℝ (φ ↑s) ((J ↑s) (ξ ↑s))
```

**Green's formula, real form.** Formalized in Tau Ceti as [`TauCeti.integral_ball_re_mul_conjWirtingerDeriv_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Wirtinger/Green.html#TauCeti.integral_ball_re_mul_conjWirtingerDeriv_eq).

```lean
TauCeti.integral_ball_re_mul_conjWirtingerDeriv_eq {g ξ : ℂ → ℂ} {c : ℂ} {r : ℝ} (hr : 0 ≤ r)
  (hg : ∀ z ∈ Metric.closedBall c r, ContDiffAt ℝ 1 g z)
  (hξ : ∀ z ∈ Metric.closedBall c r, ContDiffAt ℝ 1 ξ z) :
  ∫ (z : ℂ) in Metric.ball c r, (g z * (TauCeti.conjWirtingerDeriv ξ z) 1).re =
    (-∫ (z : ℂ) in Metric.ball c r, (ξ z * (TauCeti.conjWirtingerDeriv g z) 1).re) +
      2⁻¹ *
        ∫ (θ : ℝ) in -Real.pi..Real.pi,
          (circleMap 0 r θ * g (circleMap c r θ) * ξ (circleMap c r θ)).re
```

## Sources

- [Tau Ceti documentation: `TauCeti.IsSobolevCRCoefficients.integral_inner_crFormalAdjoint`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/CauchyRiemann/RoughCoefficients/Weak.html#TauCeti.IsSobolevCRCoefficients.integral_inner_crFormalAdjoint)
- [Source of `TauCeti.IsSobolevCRCoefficients.integral_inner_crFormalAdjoint` in TauCeti/Analysis/Complex/CauchyRiemann/RoughCoefficients/Weak.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/CauchyRiemann/RoughCoefficients/Weak.lean#L283)
