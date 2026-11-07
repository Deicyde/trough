---
declaration: theorem
origin: cited
lean: TauCeti.exists_homeomorph_closedBall_closure_of_isJordanCurve_frontier
statement: formalized
proof: formalized
---

# TauCeti.exists\_homeomorph\_closedBall\_closure\_of\_isJordanCurve\_frontier

**The Riemann map of a Jordan domain extends to a homeomorphism of the
closures.**

```lean
TauCeti.exists_homeomorph_closedBall_closure_of_isJordanCurve_frontier {Ω : Set ℂ} (hΩo : IsOpen Ω)
  (hΩc : IsConnected Ω) (hΩb : Bornology.IsBounded Ω) (hΩJ : TauCeti.IsJordanCurve (frontier Ω)) :
  ∃ g,
    ContinuousOn g (Metric.closedBall 0 1) ∧
      DifferentiableOn ℂ g (Metric.ball 0 1) ∧
        Set.BijOn g (Metric.ball 0 1) Ω ∧ ∃ e, ∀ (z : ↑(Metric.closedBall 0 1)), ↑(e z) = g ↑z
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Generalized winding number](../contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number.md)
- [The homology Cauchy theorem](../contour-integration-and-the-hungerbuhler-wasem-g/the-homology-cauchy-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_homeomorph_closedBall_closure_of_isJordanCurve_frontier`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Jordan/Approach.html#TauCeti.exists_homeomorph_closedBall_closure_of_isJordanCurve_frontier).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_homeomorph_closedBall_closure_of_isJordanCurve_frontier`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Jordan/Approach.html#TauCeti.exists_homeomorph_closedBall_closure_of_isJordanCurve_frontier)
- [Source of `TauCeti.exists_homeomorph_closedBall_closure_of_isJordanCurve_frontier` in TauCeti/Analysis/Complex/Conformal/Jordan/Approach.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/Jordan/Approach.lean#L241)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ConformalMapping/STATUS.md)
