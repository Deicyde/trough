---
declaration: theorem
origin: cited
lean: TauCeti.hasFDerivAt_timeDeriv_of_continuousWithinAt, TauCeti.hasDerivWithinAt_spatialDeriv_of_continuousWithinAt
statement: formalized
proof: formalized
---

# Peano's theorem on mixed partial derivatives, differentiating a time derivative in space

Let `u : E → ℝ → F`, let `s ⊆ ℝ` be convex, and let `t ∈ s` be a point at which derivatives within
`s` are unique. Suppose that near `x` in space and near `t` within `s`, the spatial derivative of
`u(·, τ)` at `y` is `v(y, τ)`, and that `v(y, ·)` has time derivative `w(y, τ)` within `s`, with
`w` jointly continuous at `(x, t)`. If `g y` is the time derivative of `u(y, ·)` within `s` at `t`
for every `y` near `x`, then `g` is differentiable at `x` with derivative `w(x, t)`: the spatial
derivative of `∂ₜu` exists and equals `∂ₜ D_y u`.

```lean
TauCeti.hasFDerivAt_timeDeriv_of_continuousWithinAt.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] {u : E → ℝ → F}
  {v w : E → ℝ → E →L[ℝ] F} {g : E → F} {s : Set ℝ} {x : E} {t : ℝ} (hs : Convex ℝ s) (ht : t ∈ s)
  (hst : UniqueDiffWithinAt ℝ s t)
  (hv : ∀ᶠ (p : E × ℝ) in nhds x ×ˢ nhdsWithin t s, HasFDerivAt (fun x => u x p.2) (v p.1 p.2) p.1)
  (hw : ∀ᶠ (p : E × ℝ) in nhds x ×ˢ nhdsWithin t s, HasDerivWithinAt (v p.1) (w p.1 p.2) s p.2)
  (hwc : ContinuousWithinAt (fun p => w p.1 p.2) (Set.univ ×ˢ s) (x, t))
  (hg : ∀ᶠ (y : E) in nhds x, HasDerivWithinAt (u y) (g y) s t) : HasFDerivAt g (w x t) x
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.hasFDerivAt_timeDeriv_of_continuousWithinAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/FDeriv/MixedPartial.html#TauCeti.hasFDerivAt_timeDeriv_of_continuousWithinAt).

## Other forms

**Peano's theorem on mixed partial derivatives, differentiating a spatial derivative in time.** Formalized in Tau Ceti as [`TauCeti.hasDerivWithinAt_spatialDeriv_of_continuousWithinAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/FDeriv/MixedPartial.html#TauCeti.hasDerivWithinAt_spatialDeriv_of_continuousWithinAt).

```lean
TauCeti.hasDerivWithinAt_spatialDeriv_of_continuousWithinAt.{u_1, u_2} {E : Type u_1} {F : Type u_2}
  [NormedAddCommGroup E] [NormedSpace ℝ E] [NormedAddCommGroup F] [NormedSpace ℝ F] {u : E → ℝ → F}
  {v : ℝ → E →L[ℝ] F} {g : E → ℝ → F} {w : E → ℝ → E →L[ℝ] F} {s : Set ℝ} {x : E} {t : ℝ}
  (hs : Convex ℝ s) (ht : t ∈ s)
  (hv : ∀ᶠ (τ : ℝ) in nhdsWithin t s, HasFDerivAt (fun x => u x τ) (v τ) x)
  (hg : ∀ᶠ (p : E × ℝ) in nhds x ×ˢ nhdsWithin t s, HasDerivWithinAt (u p.1) (g p.1 p.2) s p.2)
  (hw : ∀ᶠ (p : E × ℝ) in nhds x ×ˢ nhdsWithin t s, HasFDerivAt (fun x => g x p.2) (w p.1 p.2) p.1)
  (hwc : ContinuousWithinAt (fun p => w p.1 p.2) (Set.univ ×ˢ s) (x, t)) :
  HasDerivWithinAt v (w x t) s t
```

## Sources

- [Tau Ceti documentation: `TauCeti.hasFDerivAt_timeDeriv_of_continuousWithinAt`](https://taucetiproject.org/docs/TauCeti/Analysis/Calculus/FDeriv/MixedPartial.html#TauCeti.hasFDerivAt_timeDeriv_of_continuousWithinAt)
- [Source of `TauCeti.hasFDerivAt_timeDeriv_of_continuousWithinAt` in TauCeti/Analysis/Calculus/FDeriv/MixedPartial.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Calculus/FDeriv/MixedPartial.lean#L78)
