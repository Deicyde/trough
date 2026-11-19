---
declaration: theorem
origin: cited
lean: TauCeti.exists_analyticOnNhd_prod_ball_eqOn_sdiff_prod_closedBall, TauCeti.exists_analyticOnNhd_eqOn_sdiff_of_isDiscrete, TauCeti.exists_analyticOnNhd_eqOn_sdiff_of_finite, TauCeti.exists_analyticOnNhd_eqOn_sdiff_singleton
statement: formalized
proof: formalized
---

# Hartogs' extension theorem on product shells

Let `V` be a nontrivial finite-dimensional
complex normed space and `F` a complete complex normed space. For `r₁ < R₁` and `r₂ < R₂`, every
map `f : V × ℂ → F` complex differentiable on
`(ball w₀ R₁ ×ˢ ball c R₂) \ (closedBall w₀ r₁ ×ˢ closedBall c r₂)` extends to an analytic map on
`ball w₀ R₁ ×ˢ ball c R₂`.

```lean
TauCeti.exists_analyticOnNhd_prod_ball_eqOn_sdiff_prod_closedBall.{u_1, u_2} {V : Type u_1}
  {F : Type u_2} [NormedAddCommGroup V] [NormedSpace ℂ V] [Nontrivial V] [NormedAddCommGroup F]
  [NormedSpace ℂ F] [FiniteDimensional ℂ V] [CompleteSpace F] {f : V × ℂ → F} {w₀ : V} {c : ℂ}
  {r₁ R₁ r₂ R₂ : ℝ} (hR₁ : r₁ < R₁) (hR₂ : r₂ < R₂)
  (hf :
    DifferentiableOn ℂ f
      (Metric.ball w₀ R₁ ×ˢ Metric.ball c R₂ \ Metric.closedBall w₀ r₁ ×ˢ Metric.closedBall c r₂)) :
  ∃ g,
    AnalyticOnNhd ℂ g (Metric.ball w₀ R₁ ×ˢ Metric.ball c R₂) ∧
      Set.EqOn g f
        (Metric.ball w₀ R₁ ×ˢ Metric.ball c R₂ \ Metric.closedBall w₀ r₁ ×ˢ Metric.closedBall c r₂)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Hartogs' local removable singularity theorem](hartogs-local-removable-singularity-theorem.md)
- [Osgood's lemma](../../../../geometry/part-01/complex-manifolds-dolbeault-theory-and-kahler-ge/osgoods-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_analyticOnNhd_prod_ball_eqOn_sdiff_prod_closedBall`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Hartogs.html#TauCeti.exists_analyticOnNhd_prod_ball_eqOn_sdiff_prod_closedBall).

## Other forms

**Hartogs' extension theorem across a closed discrete set.** Formalized in Tau Ceti as [`TauCeti.exists_analyticOnNhd_eqOn_sdiff_of_isDiscrete`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Hartogs.html#TauCeti.exists_analyticOnNhd_eqOn_sdiff_of_isDiscrete).

```lean
TauCeti.exists_analyticOnNhd_eqOn_sdiff_of_isDiscrete.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℂ E] [FiniteDimensional ℂ E] [NormedAddCommGroup F]
  [NormedSpace ℂ F] [CompleteSpace F] (hE : 2 ≤ Module.finrank ℂ E) {f : E → F} {U S : Set E}
  (hU : IsOpen U) (hUS : IsOpen (U \ S)) (hS : IsDiscrete (U ∩ S))
  (hf : DifferentiableOn ℂ f (U \ S)) : ∃ g, AnalyticOnNhd ℂ g U ∧ Set.EqOn g f (U \ S)
```

**Hartogs' extension theorem across a finite set.** Formalized in Tau Ceti as [`TauCeti.exists_analyticOnNhd_eqOn_sdiff_of_finite`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Hartogs.html#TauCeti.exists_analyticOnNhd_eqOn_sdiff_of_finite).

```lean
TauCeti.exists_analyticOnNhd_eqOn_sdiff_of_finite.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℂ E] [FiniteDimensional ℂ E] [NormedAddCommGroup F]
  [NormedSpace ℂ F] [CompleteSpace F] (hE : 2 ≤ Module.finrank ℂ E) {f : E → F} {U S : Set E}
  (hU : IsOpen U) (hS : S.Finite) (hf : DifferentiableOn ℂ f (U \ S)) :
  ∃ g, AnalyticOnNhd ℂ g U ∧ Set.EqOn g f (U \ S)
```

**Hartogs' extension theorem across a point in an open set.** Formalized in Tau Ceti as [`TauCeti.exists_analyticOnNhd_eqOn_sdiff_singleton`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Hartogs.html#TauCeti.exists_analyticOnNhd_eqOn_sdiff_singleton).

```lean
TauCeti.exists_analyticOnNhd_eqOn_sdiff_singleton.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℂ E] [FiniteDimensional ℂ E] [NormedAddCommGroup F]
  [NormedSpace ℂ F] [CompleteSpace F] (hE : 2 ≤ Module.finrank ℂ E) {f : E → F} {U : Set E}
  (hU : IsOpen U) (p : E) (hf : DifferentiableOn ℂ f (U \ {p})) :
  ∃ g, AnalyticOnNhd ℂ g U ∧ Set.EqOn g f (U \ {p})
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_analyticOnNhd_prod_ball_eqOn_sdiff_prod_closedBall`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Hartogs.html#TauCeti.exists_analyticOnNhd_prod_ball_eqOn_sdiff_prod_closedBall)
- [Source of `TauCeti.exists_analyticOnNhd_prod_ball_eqOn_sdiff_prod_closedBall` in TauCeti/Analysis/Complex/Hartogs.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Hartogs.lean#L148)
