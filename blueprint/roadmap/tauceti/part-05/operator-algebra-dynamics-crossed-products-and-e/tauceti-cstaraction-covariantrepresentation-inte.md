---
declaration: theorem
origin: cited
lean: TauCeti.CStarAction.CovariantRepresentation.integratedOperator_convolution
statement: formalized
proof: formalized
---

# TauCeti.CStarAction.CovariantRepresentation.integratedOperator\_convolution

The integrated form of a covariant pair is multiplicative for twisted convolution with respect
to a left-invariant measure: `(π ⋊ U) (f ⋆ g) = (π ⋊ U) f * (π ⋊ U) g`.

```lean
TauCeti.CStarAction.CovariantRepresentation.integratedOperator_convolution.{u_1, u_2, u_3}
  {G : Type u_1} {A : Type u_2} {H : Type u_3} [Group G] [TopologicalSpace G] [MeasurableSpace G]
  [OpensMeasurableSpace G] [NonUnitalCStarAlgebra A] [NormedAddCommGroup H] [InnerProductSpace ℂ H]
  [CompleteSpace H] {α : TauCeti.CStarAction G A} (P : α.CovariantRepresentation H)
  (μ : MeasureTheory.Measure G) [MeasureTheory.IsFiniteMeasureOnCompacts μ] [IsTopologicalGroup G]
  [MeasurableMul G] [μ.IsMulLeftInvariant] (f g : CompactlySupportedContinuousMap G A) :
  (P.integratedOperator μ) (((α.convolution μ) f) g) =
    (P.integratedOperator μ) f * (P.integratedOperator μ) g
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CStarAction.CovariantRepresentation.integratedOperator_convolution`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/Covariant/Integrated.html#TauCeti.CStarAction.CovariantRepresentation.integratedOperator_convolution).

## Sources

- [Tau Ceti documentation: `TauCeti.CStarAction.CovariantRepresentation.integratedOperator_convolution`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/Covariant/Integrated.html#TauCeti.CStarAction.CovariantRepresentation.integratedOperator_convolution)
- [Source of `TauCeti.CStarAction.CovariantRepresentation.integratedOperator_convolution` in TauCeti/Analysis/CStarAlgebra/Action/Covariant/Integrated.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/CStarAlgebra/Action/Covariant/Integrated.lean#L158)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
