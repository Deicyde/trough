---
declaration: theorem
origin: cited
lean: ContinuousOn.analyticOnNhd_of_differentiableAt_update
statement: formalized
proof: formalized
---

# Osgood's lemma

A function of finitely many complex variables which is continuous on an
open set and complex differentiable in each variable separately on it is analytic on it.

```lean
ContinuousOn.analyticOnNhd_of_differentiableAt_update.{u_1, u_2} {E : Type u_1}
  [NormedAddCommGroup E] [NormedSpace ℂ E] [CompleteSpace E] {ι : Type u_2} [Fintype ι]
  [DecidableEq ι] {f : (ι → ℂ) → E} {s : Set (ι → ℂ)} (hc : ContinuousOn f s) (hs : IsOpen s)
  (hd : ∀ y ∈ s, ∀ (i : ι), DifferentiableAt ℂ (fun x => f (Function.update y i x)) (y i)) :
  AnalyticOnNhd ℂ f s
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`ContinuousOn.analyticOnNhd_of_differentiableAt_update`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/CauchyIntegralPolydisc.html#ContinuousOn.analyticOnNhd_of_differentiableAt_update).

## Sources

- [Tau Ceti documentation: `ContinuousOn.analyticOnNhd_of_differentiableAt_update`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/CauchyIntegralPolydisc.html#ContinuousOn.analyticOnNhd_of_differentiableAt_update)
- [Source of `ContinuousOn.analyticOnNhd_of_differentiableAt_update` in TauCeti/Analysis/Complex/CauchyIntegralPolydisc.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/CauchyIntegralPolydisc.lean#L314)
- [Tau Ceti roadmap status: Complex manifolds, Dolbeault theory, and Kähler geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ComplexKahlerGeometry/STATUS.md)
