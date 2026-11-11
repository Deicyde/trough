---
declaration: theorem
origin: cited
lean: TauCeti.exists_continuousOn_closedBall_eqOn_of_locallyConnectedSpace_frontier, TauCeti.exists_continuousOn_bijOn_upperHalfPlaneSet_of_locallyConnectedSpace_frontier, TauCeti.exists_continuousOn_closedBall_eqOn_iff_locallyConnectedSpace_frontier
statement: formalized
proof: formalized
---

# Carathéodory's continuity theorem

A holomorphic injection of a disc onto a bounded region
whose boundary is locally connected extends continuously to the closed disc.

No injectivity is claimed for the extension on the circle, and none is needed for continuity.

```lean
TauCeti.exists_continuousOn_closedBall_eqOn_of_locallyConnectedSpace_frontier {f : ℂ → ℂ} {c : ℂ}
  {r : ℝ} (hr : 0 < r) (hf : DifferentiableOn ℂ f (Metric.ball c r))
  (hinj : Set.InjOn f (Metric.ball c r)) (hb : Bornology.IsBounded (f '' Metric.ball c r))
  [LocallyConnectedSpace ↑(frontier (f '' Metric.ball c r))] :
  ∃ F, ContinuousOn F (Metric.closedBall c r) ∧ Set.EqOn F f (Metric.ball c r)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cauchy estimate](cauchy-estimate.md)
- [Generalized winding number (HW Def 2.1)](../../../part-01/contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)
- [Hurwitz's theorem](hurwitzs-theorem.md)
- [Montel's selection theorem](../part-02/montels-selection-theorem.md)
- [Poincaré defect identity (norm form)](../part-03/poincare-defect-identity-norm-form.md)
- [Rouché's theorem for a disc, classical form](../part-03/rouches-theorem-for-a-disc-classical-form.md)
- [Strict Schwarz lemma](../part-03/strict-schwarz-lemma.md)
- [Wolff's lemma (`TauCeti.exists_circleLIntegral_sq_lt`)](../../../../measure-theory/integral/part-02/wolffs-lemma-tauceti-exists-circlelintegral-sq-l.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_continuousOn_closedBall_eqOn_of_locallyConnectedSpace_frontier`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Caratheodory.html#TauCeti.exists_continuousOn_closedBall_eqOn_of_locallyConnectedSpace_frontier).

## Other forms

**Carathéodory's continuity theorem on the upper half-plane.** Formalized in Tau Ceti as [`TauCeti.exists_continuousOn_bijOn_upperHalfPlaneSet_of_locallyConnectedSpace_frontier`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/UpperHalfPlane/LocallyConnectedBoundary.html#TauCeti.exists_continuousOn_bijOn_upperHalfPlaneSet_of_locallyConnectedSpace_frontier).

```lean
TauCeti.exists_continuousOn_bijOn_upperHalfPlaneSet_of_locallyConnectedSpace_frontier {Ω : Set ℂ}
  (hΩo : IsOpen Ω) (hΩs : IsSimplyConnected Ω) (hΩb : Bornology.IsBounded Ω)
  [LocallyConnectedSpace ↑(frontier Ω)] {p : ℂ} (hp : p ∈ frontier Ω) :
  ∃ f,
    ContinuousOn f {z | 0 ≤ z.im} ∧
      DifferentiableOn ℂ f UpperHalfPlane.upperHalfPlaneSet ∧
        Set.BijOn f UpperHalfPlane.upperHalfPlaneSet Ω ∧
          insert p (f '' {z | 0 ≤ z.im}) = closure Ω ∧
            insert p (f '' {z | z.im = 0}) = frontier Ω ∧
              Filter.Tendsto f (Bornology.cobounded ℂ ⊓ Filter.principal {z | 0 ≤ z.im}) (nhds p)
```

**Carathéodory's continuity theorem, as a characterization.** Formalized in Tau Ceti as [`TauCeti.exists_continuousOn_closedBall_eqOn_iff_locallyConnectedSpace_frontier`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Caratheodory.html#TauCeti.exists_continuousOn_closedBall_eqOn_iff_locallyConnectedSpace_frontier).

```lean
TauCeti.exists_continuousOn_closedBall_eqOn_iff_locallyConnectedSpace_frontier {f : ℂ → ℂ} {c : ℂ}
  {r : ℝ} (hr : 0 < r) (hf : DifferentiableOn ℂ f (Metric.ball c r))
  (hinj : Set.InjOn f (Metric.ball c r)) (hb : Bornology.IsBounded (f '' Metric.ball c r)) :
  (∃ F, ContinuousOn F (Metric.closedBall c r) ∧ Set.EqOn F f (Metric.ball c r)) ↔
    LocallyConnectedSpace ↑(frontier (f '' Metric.ball c r))
```

## Sources

- [Tau Ceti documentation: `TauCeti.exists_continuousOn_closedBall_eqOn_of_locallyConnectedSpace_frontier`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Caratheodory.html#TauCeti.exists_continuousOn_closedBall_eqOn_of_locallyConnectedSpace_frontier)
- [Source of `TauCeti.exists_continuousOn_closedBall_eqOn_of_locallyConnectedSpace_frontier` in TauCeti/Analysis/Complex/Conformal/Caratheodory.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Complex/Conformal/Caratheodory.lean#L207)
