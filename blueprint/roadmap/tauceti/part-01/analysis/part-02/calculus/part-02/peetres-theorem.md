---
declaration: theorem
origin: cited
lean: LinearMap.exists_apply_eq_zero_of_iteratedFDeriv_eq_zero, LinearMap.exists_apply_eq_apply_of_iteratedFDeriv_eq, LinearMap.exists_forall_mem_ball_apply_eq_zero
statement: formalized
proof: formalized
---

# Peetre's theorem

Let `P` be a linear map from smooth functions `E → F` to functions
`E → G`, local on the open set `U` (`(P u) x = 0` whenever `u` vanishes near `x ∈ U`) and with
`P u` continuous on `U` for every `u`. Then `P` has locally finite order: for every compact
`K ⊆ U` there is `r` such that `(P u) x = 0` whenever `x ∈ K` and the derivatives of `u` of order at
most `r` vanish at `x`. No continuity of `P` is assumed.

```lean
LinearMap.exists_apply_eq_zero_of_iteratedFDeriv_eq_zero.{u_1, u_2, u_3} {E : Type u_1}
  {F : Type u_2} {G : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F]
  [NormedSpace ℝ F] [NormedAddCommGroup G] [NormedSpace ℝ G] {U : Set E} [FiniteDimensional ℝ E]
  [CompleteSpace F]
  (P : ContMDiffMap (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ F) E F ↑⊤ →ₗ[ℝ] E → G)
  (hU : IsOpen U)
  (hloc :
    ∀ (u : ContMDiffMap (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ F) E F ↑⊤),
      ∀ x ∈ U, ⇑u =ᶠ[nhds x] 0 → P u x = 0)
  (hcont :
    ∀ (u : ContMDiffMap (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ F) E F ↑⊤),
      ContinuousOn (P u) U)
  {K : Set E} (hK : IsCompact K) (hKU : K ⊆ U) :
  ∃ r,
    ∀ x ∈ K,
      ∀ (u : ContMDiffMap (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ F) E F ↑⊤),
        (∀ i ≤ r, iteratedFDeriv ℝ i (⇑u) x = 0) → P u x = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Peetre's estimate on punctured balls](peetres-estimate-on-punctured-balls.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.exists_apply_eq_zero_of_iteratedFDeriv_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/LocalOperator.html#LinearMap.exists_apply_eq_zero_of_iteratedFDeriv_eq_zero).

## Other forms

**Peetre's theorem, in jet form.** Formalized in Tau Ceti as [`LinearMap.exists_apply_eq_apply_of_iteratedFDeriv_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/LocalOperator.html#LinearMap.exists_apply_eq_apply_of_iteratedFDeriv_eq).

```lean
LinearMap.exists_apply_eq_apply_of_iteratedFDeriv_eq.{u_1, u_2, u_3} {E : Type u_1} {F : Type u_2}
  {G : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  [NormedAddCommGroup G] [NormedSpace ℝ G] {U : Set E} [FiniteDimensional ℝ E] [CompleteSpace F]
  (P : ContMDiffMap (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ F) E F ↑⊤ →ₗ[ℝ] E → G)
  (hU : IsOpen U)
  (hloc :
    ∀ (u : ContMDiffMap (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ F) E F ↑⊤),
      ∀ x ∈ U, ⇑u =ᶠ[nhds x] 0 → P u x = 0)
  (hcont :
    ∀ (u : ContMDiffMap (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ F) E F ↑⊤),
      ContinuousOn (P u) U)
  {K : Set E} (hK : IsCompact K) (hKU : K ⊆ U) :
  ∃ r,
    ∀ x ∈ K,
      ∀ (u v : ContMDiffMap (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ F) E F ↑⊤),
        (∀ i ≤ r, iteratedFDeriv ℝ i (⇑u) x = iteratedFDeriv ℝ i (⇑v) x) → P u x = P v x
```

**Peetre's theorem, local form.** Formalized in Tau Ceti as [`LinearMap.exists_forall_mem_ball_apply_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/LocalOperator.html#LinearMap.exists_forall_mem_ball_apply_eq_zero).

```lean
LinearMap.exists_forall_mem_ball_apply_eq_zero.{u_1, u_2, u_3} {E : Type u_1} {F : Type u_2}
  {G : Type u_3} [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F]
  [NormedAddCommGroup G] [NormedSpace ℝ G] {U : Set E} [FiniteDimensional ℝ E] [CompleteSpace F]
  (P : ContMDiffMap (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ F) E F ↑⊤ →ₗ[ℝ] E → G)
  (hU : IsOpen U)
  (hloc :
    ∀ (u : ContMDiffMap (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ F) E F ↑⊤),
      ∀ x ∈ U, ⇑u =ᶠ[nhds x] 0 → P u x = 0)
  (hcont :
    ∀ (u : ContMDiffMap (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ F) E F ↑⊤),
      ContinuousOn (P u) U)
  {x₀ : E} (hx₀ : x₀ ∈ U) :
  ∃ ρ > 0,
    Metric.ball x₀ ρ ⊆ U ∧
      ∃ r,
        ∀ y ∈ Metric.ball x₀ ρ,
          ∀ (u : ContMDiffMap (modelWithCornersSelf ℝ E) (modelWithCornersSelf ℝ F) E F ↑⊤),
            (∀ i ≤ r, iteratedFDeriv ℝ i (⇑u) y = 0) → P u y = 0
```

## Sources

- [Tau Ceti documentation: `LinearMap.exists_apply_eq_zero_of_iteratedFDeriv_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/LocalOperator.html#LinearMap.exists_apply_eq_zero_of_iteratedFDeriv_eq_zero)
- [Source of `LinearMap.exists_apply_eq_zero_of_iteratedFDeriv_eq_zero` in TauCeti/Analysis/Calculus/LocalOperator.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/LocalOperator.lean#L420)
