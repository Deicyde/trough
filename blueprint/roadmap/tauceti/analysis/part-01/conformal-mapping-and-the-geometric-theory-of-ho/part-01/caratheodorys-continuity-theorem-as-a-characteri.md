---
declaration: theorem
origin: cited
lean: TauCeti.exists_continuousOn_closedBall_eqOn_iff_locallyConnectedSpace_frontier, TauCeti.exists_continuousOn_closedBall_eqOn_of_locallyConnectedSpace_frontier, TauCeti.exists_continuousOn_bijOn_upperHalfPlaneSet_of_locallyConnectedSpace_frontier
statement: formalized
proof: formalized
---

# Carathéodory's continuity theorem, as a characterization

A holomorphic injection of a disc
onto a bounded region extends continuously to the closed disc if and only if the boundary of the
region is locally connected.

```lean
TauCeti.exists_continuousOn_closedBall_eqOn_iff_locallyConnectedSpace_frontier {f : ℂ → ℂ} {c : ℂ}
  {r : ℝ} (hr : 0 < r) (hf : DifferentiableOn ℂ f (Metric.ball c r))
  (hinj : Set.InjOn f (Metric.ball c r)) (hb : Bornology.IsBounded (f '' Metric.ball c r)) :
  (∃ F, ContinuousOn F (Metric.closedBall c r) ∧ Set.EqOn F f (Metric.ball c r)) ↔
    LocallyConnectedSpace ↑(frontier (f '' Metric.ball c r))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Cauchy estimate](../../../part-02/complex/part-01/cauchy-estimate.md)
- [Generalized winding number (HW Def 2.1)](../../contour-integration-and-the-hungerbuhler-wasem-g/generalized-winding-number-hw-def-2-1.md)
- [Hurwitz's theorem](hurwitzs-theorem.md)
- [Montel's selection theorem](../../../part-02/complex/part-02/montels-selection-theorem.md)
- [Rouché's theorem for a disc, classical form](../part-02/rouches-theorem-for-a-disc-classical-form.md)
- [Strict Schwarz lemma](../part-02/strict-schwarz-lemma.md)
- [Wolff's lemma (`TauCeti.exists_circleLIntegral_sq_lt`)](../../../../measure-theory/integral/part-02/wolffs-lemma-tauceti-exists-circlelintegral-sq-l.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_continuousOn_closedBall_eqOn_iff_locallyConnectedSpace_frontier`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Caratheodory.html#TauCeti.exists_continuousOn_closedBall_eqOn_iff_locallyConnectedSpace_frontier).

## Other forms

**Carathéodory's continuity theorem.** Formalized in Tau Ceti as [`TauCeti.exists_continuousOn_closedBall_eqOn_of_locallyConnectedSpace_frontier`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Caratheodory.html#TauCeti.exists_continuousOn_closedBall_eqOn_of_locallyConnectedSpace_frontier).

```lean
TauCeti.exists_continuousOn_closedBall_eqOn_of_locallyConnectedSpace_frontier {f : ℂ → ℂ} {c : ℂ}
  {r : ℝ} (hr : 0 < r) (hf : DifferentiableOn ℂ f (Metric.ball c r))
  (hinj : Set.InjOn f (Metric.ball c r)) (hb : Bornology.IsBounded (f '' Metric.ball c r))
  [LocallyConnectedSpace ↑(frontier (f '' Metric.ball c r))] :
  ∃ F, ContinuousOn F (Metric.closedBall c r) ∧ Set.EqOn F f (Metric.ball c r)
```

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

## Sources

- [Tau Ceti documentation: `TauCeti.exists_continuousOn_closedBall_eqOn_iff_locallyConnectedSpace_frontier`](https://taucetiproject.org/docs/TauCeti/Analysis/Complex/Conformal/Caratheodory.html#TauCeti.exists_continuousOn_closedBall_eqOn_iff_locallyConnectedSpace_frontier)
- [Source of `TauCeti.exists_continuousOn_closedBall_eqOn_iff_locallyConnectedSpace_frontier` in TauCeti/Analysis/Complex/Conformal/Caratheodory.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/Complex/Conformal/Caratheodory.lean#L220)
- [Tau Ceti roadmap status: Conformal mapping and the geometric theory of holomorphic functions](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/ConformalMapping/STATUS.md)
