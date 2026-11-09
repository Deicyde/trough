---
declaration: theorem
origin: cited
lean: TauCeti.hurwitz, TauCeti.hurwitz_forall_ne, TauCeti.hurwitz_forall_ne_or_forall_eq, TauCeti.hurwitz_injOn, TauCeti.eventually_finsum_analyticOrderNatAt_ball_eq, TauCeti.hurwitz_eventually_exists_eq, TauCeti.hurwitz_eventually_exists_eq_zero
statement: formalized
proof: formalized
---

# Hurwitz's theorem

On a connected open set, a locally uniform limit of functions that are
holomorphic for all sufficiently large `i` and nowhere zero for infinitely many `i` is itself
either nowhere zero or identically zero.

This is the value `v = 0` of `TauCeti.hurwitz_forall_ne_or_forall_eq`. The dichotomy is genuine:
for `ι = ℕ` and `l = atTop`, the constant functions `F n z = 1 / (n + 1 : ℂ)` on any `Ω` converge
locally uniformly to `0`, so the second alternative cannot be dropped.

```lean
TauCeti.hurwitz.{u_1} {ι : Type u_1} {l : Filter ι} {Ω : Set ℂ} {F : ι → ℂ → ℂ} {g : ℂ → ℂ}
  (hΩ : IsOpen Ω) (hconn : IsPreconnected Ω) (hF : ∀ᶠ (i : ι) in l, DifferentiableOn ℂ (F i) Ω)
  (hconv : TendstoLocallyUniformlyOn F g l Ω) (hne : ∃ᶠ (i : ι) in l, ∀ z ∈ Ω, F i z ≠ 0) :
  (∀ z ∈ Ω, g z ≠ 0) ∨ ∀ z ∈ Ω, g z = 0
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Rouché's theorem for a disc, classical form](../part-02/rouches-theorem-for-a-disc-classical-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.hurwitz`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Hurwitz.html#TauCeti.hurwitz).

## Other forms

**Hurwitz's theorem for an omitted value.** Formalized in Tau Ceti as [`TauCeti.hurwitz_forall_ne`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Hurwitz.html#TauCeti.hurwitz_forall_ne).

```lean
TauCeti.hurwitz_forall_ne.{u_1} {ι : Type u_1} {l : Filter ι} {Ω : Set ℂ} {F : ι → ℂ → ℂ}
  {g : ℂ → ℂ} (hΩ : IsOpen Ω) (hconn : IsPreconnected Ω)
  (hF : ∀ᶠ (i : ι) in l, DifferentiableOn ℂ (F i) Ω) (hconv : TendstoLocallyUniformlyOn F g l Ω)
  {v : ℂ} (hne : ∃ᶠ (i : ι) in l, ∀ z ∈ Ω, F i z ≠ v) (hnc : ¬∀ z ∈ Ω, g z = v) (z : ℂ) :
  z ∈ Ω → g z ≠ v
```

**Hurwitz's theorem for an omitted value, dichotomy form.** Formalized in Tau Ceti as [`TauCeti.hurwitz_forall_ne_or_forall_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Hurwitz.html#TauCeti.hurwitz_forall_ne_or_forall_eq).

```lean
TauCeti.hurwitz_forall_ne_or_forall_eq.{u_1} {ι : Type u_1} {l : Filter ι} {Ω : Set ℂ}
  {F : ι → ℂ → ℂ} {g : ℂ → ℂ} (hΩ : IsOpen Ω) (hconn : IsPreconnected Ω)
  (hF : ∀ᶠ (i : ι) in l, DifferentiableOn ℂ (F i) Ω) (hconv : TendstoLocallyUniformlyOn F g l Ω)
  {v : ℂ} (hne : ∃ᶠ (i : ι) in l, ∀ z ∈ Ω, F i z ≠ v) : (∀ z ∈ Ω, g z ≠ v) ∨ ∀ z ∈ Ω, g z = v
```

**Hurwitz's theorem for injectivity.** Formalized in Tau Ceti as [`TauCeti.hurwitz_injOn`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Hurwitz.html#TauCeti.hurwitz_injOn).

```lean
TauCeti.hurwitz_injOn.{u_1} {ι : Type u_1} {l : Filter ι} {Ω : Set ℂ} {F : ι → ℂ → ℂ} {g : ℂ → ℂ}
  (hΩ : IsOpen Ω) (hconn : IsPreconnected Ω) (hF : ∀ᶠ (i : ι) in l, DifferentiableOn ℂ (F i) Ω)
  (hconv : TendstoLocallyUniformlyOn F g l Ω) (hinj : ∃ᶠ (i : ι) in l, Set.InjOn (F i) Ω) :
  Set.InjOn g Ω ∨ ∃ v, ∀ z ∈ Ω, g z = v
```

**Hurwitz's theorem, counting form.** Formalized in Tau Ceti as [`TauCeti.eventually_finsum_analyticOrderNatAt_ball_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Hurwitz.html#TauCeti.eventually_finsum_analyticOrderNatAt_ball_eq).

```lean
TauCeti.eventually_finsum_analyticOrderNatAt_ball_eq.{u_1} {ι : Type u_1} {l : Filter ι}
  {F : ι → ℂ → ℂ} {g : ℂ → ℂ} {c : ℂ} {r : ℝ} (hg : AnalyticOnNhd ℂ g (Metric.closedBall c r))
  (hF : ∀ᶠ (i : ι) in l, AnalyticOnNhd ℂ (F i) (Metric.closedBall c r))
  (hconv : TendstoUniformlyOn F g l (Metric.sphere c r)) (hne : ∀ z ∈ Metric.sphere c r, g z ≠ 0) :
  ∀ᶠ (i : ι) in l,
    ∑ᶠ (z : ℂ) (_ : z ∈ Metric.ball c r), analyticOrderNatAt (F i) z =
      ∑ᶠ (z : ℂ) (_ : z ∈ Metric.ball c r), analyticOrderNatAt g z
```

**Hurwitz's theorem: values of the limit are limits of values.** Formalized in Tau Ceti as [`TauCeti.hurwitz_eventually_exists_eq`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Hurwitz.html#TauCeti.hurwitz_eventually_exists_eq).

```lean
TauCeti.hurwitz_eventually_exists_eq.{u_1} {ι : Type u_1} {l : Filter ι} {Ω : Set ℂ} {F : ι → ℂ → ℂ}
  {g : ℂ → ℂ} [l.NeBot] (hΩ : IsOpen Ω) (hconn : IsPreconnected Ω)
  (hF : ∀ᶠ (i : ι) in l, DifferentiableOn ℂ (F i) Ω) (hconv : TendstoLocallyUniformlyOn F g l Ω)
  {v z₀ : ℂ} (hz₀ : z₀ ∈ Ω) (hgz₀ : g z₀ = v) (hnc : ¬∀ z ∈ Ω, g z = v) {ε : ℝ} (hε : 0 < ε) :
  ∀ᶠ (i : ι) in l, ∃ z ∈ Ω ∩ Metric.ball z₀ ε, F i z = v
```

**Hurwitz's theorem: zeros of the limit are limits of zeros.** Formalized in Tau Ceti as [`TauCeti.hurwitz_eventually_exists_eq_zero`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Hurwitz.html#TauCeti.hurwitz_eventually_exists_eq_zero).

```lean
TauCeti.hurwitz_eventually_exists_eq_zero.{u_1} {ι : Type u_1} {l : Filter ι} {Ω : Set ℂ}
  {F : ι → ℂ → ℂ} {g : ℂ → ℂ} [l.NeBot] (hΩ : IsOpen Ω) (hconn : IsPreconnected Ω)
  (hF : ∀ᶠ (i : ι) in l, DifferentiableOn ℂ (F i) Ω) (hconv : TendstoLocallyUniformlyOn F g l Ω)
  {z₀ : ℂ} (hz₀ : z₀ ∈ Ω) (hgz₀ : g z₀ = 0) (hnc : ¬∀ z ∈ Ω, g z = 0) {ε : ℝ} (hε : 0 < ε) :
  ∀ᶠ (i : ι) in l, ∃ z ∈ Ω ∩ Metric.ball z₀ ε, F i z = 0
```

## Sources

- [Tau Ceti documentation: `TauCeti.hurwitz`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Hurwitz.html#TauCeti.hurwitz)
- [Source of `TauCeti.hurwitz` in TauCeti/Analysis/Complex/Conformal/Hurwitz.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/Hurwitz.lean#L214)
