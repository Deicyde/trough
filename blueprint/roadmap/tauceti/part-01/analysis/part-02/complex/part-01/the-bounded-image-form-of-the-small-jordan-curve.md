---
declaration: theorem
origin: cited
lean: TauCeti.exists_isJordanCurve_superset_closure_image_ball_inter_sphere_diam_le_of_isBounded
statement: formalized
proof: formalized
---

# The bounded-image form of the small-Jordan-curve theorem

A holomorphic injection of a
disc onto a bounded domain has finite Dirichlet integral by the conformal area formula, so for
every positive tolerance and radius bound, some closed image crosscut can be chosen on a Jordan
curve in the closure of the image domain whose diameter is at most the tolerance.

This is the form used for the Riemann map of a bounded Jordan domain.

```lean
TauCeti.exists_isJordanCurve_superset_closure_image_ball_inter_sphere_diam_le_of_isBounded
  {f : ℂ → ℂ} {c ζ : ℂ} {r : ℝ} (hζ : dist ζ c = r) (hr : 0 < r)
  (hf : DifferentiableOn ℂ f (Metric.ball c r)) (hinj : Set.InjOn f (Metric.ball c r))
  (hb : Bornology.IsBounded (f '' Metric.ball c r))
  (hfrontier : TauCeti.IsJordanCurve (frontier (f '' Metric.ball c r))) {ε R : ℝ} (hε : 0 < ε)
  (hR : 0 < R) :
  ∃ ρ ∈ Set.Ioo 0 R,
    ρ < 2 * r ∧
      ∃ J,
        TauCeti.IsJordanCurve J ∧
          closure (f '' (Metric.ball c r ∩ Metric.sphere ζ ρ)) ⊆ J ∧
            J ⊆
                closure (f '' (Metric.ball c r ∩ Metric.sphere ζ ρ)) ∪
                  frontier (f '' Metric.ball c r) ∧
              J ⊆ closure (f '' Metric.ball c r) ∧ Metric.diam J ≤ ε
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Wolff's lemma (`TauCeti.exists_circleLIntegral_sq_lt`)](../../../../measure-theory/integral/part-02/wolffs-lemma-tauceti-exists-circlelintegral-sq-l.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_isJordanCurve_superset_closure_image_ball_inter_sphere_diam_le_of_isBounded`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Crosscut/SmallJordanCurve.html#TauCeti.exists_isJordanCurve_superset_closure_image_ball_inter_sphere_diam_le_of_isBounded).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_isJordanCurve_superset_closure_image_ball_inter_sphere_diam_le_of_isBounded`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Crosscut/SmallJordanCurve.html#TauCeti.exists_isJordanCurve_superset_closure_image_ball_inter_sphere_diam_le_of_isBounded)
- [Source of `TauCeti.exists_isJordanCurve_superset_closure_image_ball_inter_sphere_diam_le_of_isBounded` in TauCeti/Analysis/Complex/Conformal/Crosscut/SmallJordanCurve.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Conformal/Crosscut/SmallJordanCurve.lean#L139)
