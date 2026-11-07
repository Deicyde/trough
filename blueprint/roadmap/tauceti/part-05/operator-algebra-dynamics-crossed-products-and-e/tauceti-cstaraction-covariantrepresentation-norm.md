---
declaration: theorem
origin: cited
lean: TauCeti.CStarAction.CovariantRepresentation.norm_integratedOperator_le
statement: formalized
proof: formalized
---

# TauCeti.CStarAction.CovariantRepresentation.norm\_integratedOperator\_le

The integrated form is bounded by the coefficient function's L¹ norm.

```lean
TauCeti.CStarAction.CovariantRepresentation.norm_integratedOperator_le.{u_1, u_2, u_3}
  {G : Type u_1} {A : Type u_2} {H : Type u_3} [Group G] [TopologicalSpace G] [MeasurableSpace G]
  [OpensMeasurableSpace G] [NonUnitalCStarAlgebra A] [NormedAddCommGroup H] [InnerProductSpace ℂ H]
  [CompleteSpace H] {α : TauCeti.CStarAction G A} (P : α.CovariantRepresentation H)
  (μ : MeasureTheory.Measure G) [MeasureTheory.IsFiniteMeasureOnCompacts μ]
  (f : CompactlySupportedContinuousMap G A) : ‖(P.integratedOperator μ) f‖ ≤ ∫ (g : G), ‖f g‖ ∂μ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CStarAction.CovariantRepresentation.norm_integratedOperator_le`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/Covariant/Integrated.html#TauCeti.CStarAction.CovariantRepresentation.norm_integratedOperator_le).

## Sources

- [Tau Ceti documentation: `TauCeti.CStarAction.CovariantRepresentation.norm_integratedOperator_le`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/Covariant/Integrated.html#TauCeti.CStarAction.CovariantRepresentation.norm_integratedOperator_le)
- [Source of `TauCeti.CStarAction.CovariantRepresentation.norm_integratedOperator_le` in TauCeti/Analysis/CStarAlgebra/Action/Covariant/Integrated.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/CStarAlgebra/Action/Covariant/Integrated.lean#L114)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
