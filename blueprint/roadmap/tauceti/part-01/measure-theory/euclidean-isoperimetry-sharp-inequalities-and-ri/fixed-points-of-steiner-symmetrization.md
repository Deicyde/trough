---
declaration: theorem
origin: cited
lean: TauCeti.forall_steinerSymmetrization_ae_eq_iff_exists_ae_eq_ball
statement: formalized
proof: formalized
---

# Fixed points of Steiner symmetrization

A Lebesgue-measurable set of finite volume
agrees almost everywhere with its Steiner symmetral in every unit direction exactly when it agrees
almost everywhere with a centered open ball.

```lean
TauCeti.forall_steinerSymmetrization_ae_eq_iff_exists_ae_eq_ball.{u_1} {E : Type u_1}
  [NormedAddCommGroup E] [InnerProductSpace ℝ E] [FiniteDimensional ℝ E] [MeasurableSpace E]
  [BorelSpace E] {s : Set E} (hs : MeasureTheory.NullMeasurableSet s MeasureTheory.volume)
  (hfin : MeasureTheory.volume s ≠ ⊤) :
  (∀ (e : E) (he : ‖e‖ = 1), TauCeti.steinerSymmetrization e he s =ᵐ[MeasureTheory.volume] s) ↔
    ∃ r, 0 ≤ r ∧ s =ᵐ[MeasureTheory.volume] Metric.ball 0 r
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Lebesgue's density theorem](../../analysis/part-01/geometric-measure-theory-rectifiability-bv-and-f/lebesgues-density-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.forall_steinerSymmetrization_ae_eq_iff_exists_ae_eq_ball`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/Steiner/Ball.html#TauCeti.forall_steinerSymmetrization_ae_eq_iff_exists_ae_eq_ball).

## Sources

- [Tau Ceti documentation: `TauCeti.forall_steinerSymmetrization_ae_eq_iff_exists_ae_eq_ball`](https://taucetiproject.org/docs/TauCeti/MeasureTheory/Measure/Lebesgue/Steiner/Ball.html#TauCeti.forall_steinerSymmetrization_ae_eq_iff_exists_ae_eq_ball)
- [Source of `TauCeti.forall_steinerSymmetrization_ae_eq_iff_exists_ae_eq_ball` in TauCeti/MeasureTheory/Measure/Lebesgue/Steiner/Ball.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/MeasureTheory/Measure/Lebesgue/Steiner/Ball.lean#L153)
- [Tau Ceti roadmap status: Euclidean isoperimetry, sharp inequalities, and rigidity](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/Isoperimetry/STATUS.md)
