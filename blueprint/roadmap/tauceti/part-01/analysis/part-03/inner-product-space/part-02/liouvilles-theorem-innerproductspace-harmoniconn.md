---
declaration: theorem
origin: cited
lean: InnerProductSpace.HarmonicOnNhd.apply_eq_apply_of_bounded, TauCeti.eq_zero_of_laplacian_eq_mul_of_isBounded, TauCeti.nonpos_of_eventually_comap_norm_starProjection_le_of_laplacian_nonneg, TauCeti.eq_zero_of_tendsto_comap_norm_starProjection_of_mul_laplacian_nonneg, TauCeti.eq_zero_of_tendsto_cocompact_of_mul_laplacian_nonneg, InnerProductSpace.HarmonicOnNhd.exists_const_forall_eq_of_bounded
statement: formalized
proof: formalized
---

# Liouville's theorem (`InnerProductSpace.HarmonicOnNhd.apply_eq_apply_of_bounded`)

A bounded harmonic function on a finite-dimensional real inner
product space, with values in a real normed space, is constant.

```lean
InnerProductSpace.HarmonicOnNhd.apply_eq_apply_of_bounded.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [NormedAddCommGroup F]
  [NormedSpace ℝ F] {u : E → F} (hu : InnerProductSpace.HarmonicOnNhd u Set.univ)
  (hb : Bornology.IsBounded (Set.range u)) (y z : E) : u y = u z
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Lipschitz bound for bounded harmonic functions](the-lipschitz-bound-for-bounded-harmonic-functio.md)

## Lean

Formalized in Tau Ceti as [`InnerProductSpace.HarmonicOnNhd.apply_eq_apply_of_bounded`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Harmonic/Decay.html#InnerProductSpace.HarmonicOnNhd.apply_eq_apply_of_bounded).

## Other forms

**Liouville theorem for `-Δ + c`, `c > 0`.** Formalized in Tau Ceti as [`TauCeti.eq_zero_of_laplacian_eq_mul_of_isBounded`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Laplacian/ZerothOrderMaximumPrinciple.html#TauCeti.eq_zero_of_laplacian_eq_mul_of_isBounded).

```lean
TauCeti.eq_zero_of_laplacian_eq_mul_of_isBounded.{u_1} {E : Type u_1} [NormedAddCommGroup E]
  [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {c : ℝ} (hc : 0 < c) {f : E → ℝ}
  (hf : ContDiff ℝ 2 f) (hbdd : Bornology.IsBounded (Set.range f))
  (hsol : ∀ (x : E), Laplacian.laplacian f x = c * f x) : f = 0
```

**Liouville theorem for transverse decay.** Formalized in Tau Ceti as [`TauCeti.nonpos_of_eventually_comap_norm_starProjection_le_of_laplacian_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Laplacian/TransverseLiouville.html#TauCeti.nonpos_of_eventually_comap_norm_starProjection_le_of_laplacian_nonneg).

```lean
TauCeti.nonpos_of_eventually_comap_norm_starProjection_le_of_laplacian_nonneg.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {K : Submodule ℝ E}
  (hK : K ≠ ⊥) {f : E → ℝ} (hcont : Continuous f) (hcd : ∀ (x : E), 0 < f x → ContDiffAt ℝ 2 f x)
  (hlap : ∀ (x : E), 0 < f x → 0 ≤ Laplacian.laplacian f x) (hbdd : BddAbove (Set.range f))
  (hdecay :
    ∀ ε > 0, ∀ᶠ (x : E) in Filter.comap (fun x => ‖K.starProjection x‖) Filter.atTop, f x ≤ ε)
  (x : E) : f x ≤ 0
```

**Liouville theorem for transverse decay under the sign condition `f · Δ f ≥ 0`.** Formalized in Tau Ceti as [`TauCeti.eq_zero_of_tendsto_comap_norm_starProjection_of_mul_laplacian_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Laplacian/TransverseLiouville.html#TauCeti.eq_zero_of_tendsto_comap_norm_starProjection_of_mul_laplacian_nonneg).

```lean
TauCeti.eq_zero_of_tendsto_comap_norm_starProjection_of_mul_laplacian_nonneg.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] {K : Submodule ℝ E}
  (hK : K ≠ ⊥) {f : E → ℝ} (hf : ContDiff ℝ 2 f)
  (hsign : ∀ (x : E), 0 ≤ f x * Laplacian.laplacian f x) (hbdd : Bornology.IsBounded (Set.range f))
  (h : Filter.Tendsto f (Filter.comap (fun x => ‖K.starProjection x‖) Filter.atTop) (nhds 0)) :
  f = 0
```

**Liouville theorem under the sign condition `f · Δ f ≥ 0`.** Formalized in Tau Ceti as [`TauCeti.eq_zero_of_tendsto_cocompact_of_mul_laplacian_nonneg`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Laplacian/WeakMaximumPrinciple.html#TauCeti.eq_zero_of_tendsto_cocompact_of_mul_laplacian_nonneg).

```lean
TauCeti.eq_zero_of_tendsto_cocompact_of_mul_laplacian_nonneg.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [Nontrivial E] {f : E → ℝ}
  (hf : ContDiff ℝ 2 f) (hsign : ∀ (x : E), 0 ≤ f x * Laplacian.laplacian f x)
  (h : Filter.Tendsto f (Filter.cocompact E) (nhds 0)) : f = 0
```

**Liouville's theorem.** Formalized in Tau Ceti as [`InnerProductSpace.HarmonicOnNhd.exists_const_forall_eq_of_bounded`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Harmonic/Decay.html#InnerProductSpace.HarmonicOnNhd.exists_const_forall_eq_of_bounded).

```lean
InnerProductSpace.HarmonicOnNhd.exists_const_forall_eq_of_bounded.{u_1, u_2} {E : Type u_1}
  {F : Type u_2} [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E]
  [NormedAddCommGroup F] [NormedSpace ℝ F] {u : E → F}
  (hu : InnerProductSpace.HarmonicOnNhd u Set.univ) (hb : Bornology.IsBounded (Set.range u)) :
  ∃ c, ∀ (x : E), u x = c
```

## Sources

- [Tau Ceti documentation: `InnerProductSpace.HarmonicOnNhd.apply_eq_apply_of_bounded`](https://taucetiproject.org/docs/TauCeti/Analysis/InnerProductSpace/Harmonic/Decay.html#InnerProductSpace.HarmonicOnNhd.apply_eq_apply_of_bounded)
- [Source of `InnerProductSpace.HarmonicOnNhd.apply_eq_apply_of_bounded` in TauCeti/Analysis/InnerProductSpace/Harmonic/Decay.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/InnerProductSpace/Harmonic/Decay.lean#L372)
