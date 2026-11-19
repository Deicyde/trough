---
declaration: theorem
origin: cited
lean: TauCeti.exists_homeomorph_closedBall_closure_of_isJordanCurve_frontier
statement: formalized
proof: formalized
---

# The Riemann map of a Jordan domain extends to a homeomorphism of the closures

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

- [Carathéodory's continuity theorem](../../part-03/complex/part-01/caratheodorys-continuity-theorem.md)
- [Cauchy estimate](../../part-03/complex/part-01/cauchy-estimate.md)
- [The converse of Cauchy's theorem](../../part-03/contour/the-converse-of-cauchys-theorem.md)
- [Generalized winding number (HW Def 2.1)](../contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)
- [The homology Cauchy theorem](../contour-integration-and-the-hungerbuhler-wasem-g/the-homology-cauchy-theorem.md)
- [Hurwitz's theorem](../../part-03/complex/part-02/hurwitzs-theorem.md)
- [Janiszewski's theorem](../../part-03/complex/part-02/janiszewskis-theorem.md)
- [The Jordan–Brouwer separation theorem](../../../algebraic-topology/singular/the-jordan-brouwer-separation-theorem.md)
- [Montel's selection theorem](../../part-03/complex/part-03/montels-selection-theorem.md)
- [Piecewise `C¹` on the interval between `a` and `b`](../contour-integration-and-the-hungerbuhler-wasem-g/piecewise-c1-on-the-interval-between-a-and-b.md)
- [Poincaré defect identity (norm form)](../../part-03/complex/part-03/poincare-defect-identity-norm-form.md)
- [The Riemann mapping theorem](the-riemann-mapping-theorem.md)
- [Rouché's theorem for a disc, classical form](../../part-03/complex/part-04/rouches-theorem-for-a-disc-classical-form.md)
- [Strict Schwarz lemma](../../part-03/complex/part-04/strict-schwarz-lemma.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_homeomorph_closedBall_closure_of_isJordanCurve_frontier`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Jordan/Approach.html#TauCeti.exists_homeomorph_closedBall_closure_of_isJordanCurve_frontier).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_homeomorph_closedBall_closure_of_isJordanCurve_frontier`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Jordan/Approach.html#TauCeti.exists_homeomorph_closedBall_closure_of_isJordanCurve_frontier)
- [Source of `TauCeti.exists_homeomorph_closedBall_closure_of_isJordanCurve_frontier` in TauCeti/Analysis/Complex/Conformal/Jordan/Approach.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Analysis/Complex/Conformal/Jordan/Approach.lean#L222)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/ConformalMapping/STATUS.md)
