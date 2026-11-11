---
declaration: theorem
origin: cited
lean: TauCeti.isCurveOfMaximalSlope_of_forall_mem_moreauYosidaResolvent
statement: formalized
proof: formalized
---

# Limits of minimizing movements are curves of maximal slope

Let `φ` be a
bounded-below lower semicontinuous energy and `g` a strong upper gradient of `φ` which is
below the relaxed slope on the effective domain, such as the relaxed slope itself when it
is a strong upper gradient. Then every pointwise limit on `[0,T]` of implicit Euler
interpolants started at a fixed finite-energy point is a curve of maximal slope for `g`,
provided intermediate resolvent selections with a.e.-measurable slope integrands are
supplied. If the descending slope is lower semicontinuous on the effective domain, it is
such a `g` by `TauCeti.relaxedSlope_eq_descendingSlope`.

```lean
TauCeti.isCurveOfMaximalSlope_of_forall_mem_moreauYosidaResolvent.{u_1} {X : Type u_1}
  [MetricSpace X] {φ : X → EReal} {g : X → ENNReal} {τ : ℕ → NNReal} {U : ℕ → ℕ → X}
  {V : ℕ → ℕ → ℝ → X} {u : ℝ → X} {L T : ℝ} (hφ : LowerSemicontinuous φ) (hL : ∀ (x : X), ↑L ≤ φ x)
  (hg : ∀ (x : X), φ x ≠ ⊤ → g x ≤ TauCeti.relaxedSlope φ x)
  (hstrong : TauCeti.IsStrongUpperGradient φ g) {x₀ : X} (hx₀ : φ x₀ ≠ ⊤)
  (hU0 : ∀ (k : ℕ), U k 0 = x₀) (hτ : ∀ (k : ℕ), 0 < τ k)
  (hτ0 : Filter.Tendsto τ Filter.atTop (nhds 0))
  (hV :
    ∀ (k n : ℕ),
      ∀ r ∈ Set.Ioc 0 ↑(τ k), V k n r ∈ TauCeti.moreauYosidaResolvent φ r.toNNReal (U k n))
  (hVU : ∀ (k n : ℕ), V k n ↑(τ k) = U k (n + 1))
  (hmeas :
    ∀ (k : ℕ),
      AEMeasurable (fun t => TauCeti.descendingSlope φ (TauCeti.deGiorgiInterpolant (τ k) (V k) t))
        (MeasureTheory.volume.restrict (Set.Ioc 0 T)))
  (hu : ∀ t ∈ Set.Icc 0 T, Filter.Tendsto (fun k => U k ⌈t / ↑(τ k)⌉₊) Filter.atTop (nhds (u t)))
  (hT : 0 ≤ T) : TauCeti.IsCurveOfMaximalSlope 2 2 φ g u (Set.Icc 0 T)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [De Giorgi energy inequality](../../analysis/part-03/gradient-flow/de-giorgi-energy-inequality.md)
- [Discrete Grönwall bound under coercivity](../../analysis/part-03/specific-limits/discrete-gronwall-bound-under-coercivity.md)
- [Discrete Hölder estimate for a disjoint family of intervals `(sᵢ, tᵢ]` in `[0, T]`](../function/part-01/discrete-holder-estimate-for-a-disjoint-family-o.md)
- [Fundamental theorem for absolutely continuous curves, integrability](../function/part-01/fundamental-theorem-for-absolutely-continuous-cu.md)
- [Hölder estimate along a curve](../function/part-01/holder-estimate-along-a-curve.md)
- [Young's inequality along a curve](../../analysis/part-03/gradient-flow/youngs-inequality-along-a-curve.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.isCurveOfMaximalSlope_of_forall_mem_moreauYosidaResolvent`](https://taucetiproject.org/docs/TauCeti/Analysis/GradientFlow/MaximalSlope/MinimizingMovement.html#TauCeti.isCurveOfMaximalSlope_of_forall_mem_moreauYosidaResolvent).

## Sources

- [Tau Ceti documentation: `TauCeti.isCurveOfMaximalSlope_of_forall_mem_moreauYosidaResolvent`](https://taucetiproject.org/docs/TauCeti/Analysis/GradientFlow/MaximalSlope/MinimizingMovement.html#TauCeti.isCurveOfMaximalSlope_of_forall_mem_moreauYosidaResolvent)
- [Source of `TauCeti.isCurveOfMaximalSlope_of_forall_mem_moreauYosidaResolvent` in TauCeti/Analysis/GradientFlow/MaximalSlope/MinimizingMovement.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/GradientFlow/MaximalSlope/MinimizingMovement.lean#L152)
- [Tau Ceti roadmap status: Optimal transport and Wasserstein geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/OptimalTransport/STATUS.md)
