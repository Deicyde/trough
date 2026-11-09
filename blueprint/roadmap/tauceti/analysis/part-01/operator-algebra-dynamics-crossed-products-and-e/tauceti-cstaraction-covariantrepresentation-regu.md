---
declaration: def
origin: cited
lean: TauCeti.CStarAction.CovariantRepresentation.regular
statement: formalized
---

# TauCeti.CStarAction.CovariantRepresentation.regular

The regular covariant representation on `L²(G, H)` induced by a representation `ρ` of `A` on
`H`: `a` acts by `ξ ↦ (r ↦ ρ (α_{r⁻¹}(a)) (ξ r))` and `s` by left translation
`ξ ↦ (r ↦ ξ (s⁻¹ r))`.

```lean
TauCeti.CStarAction.CovariantRepresentation.regular.{u_1, u_2, u_3} {G : Type u_1} {A : Type u_2}
  {H : Type u_3} [Group G] [TopologicalSpace G] [NonUnitalCStarAlgebra A] [NormedAddCommGroup H]
  [InnerProductSpace ℂ H] [CompleteSpace H] [IsTopologicalGroup G] [MeasurableSpace G]
  [BorelSpace G] (α : TauCeti.CStarAction G A) (ρ : A →⋆ₙₐ[ℂ] H →L[ℂ] H)
  (μ : MeasureTheory.Measure G) [μ.IsMulLeftInvariant] [μ.InnerRegularCompactLTTop]
  [MeasureTheory.IsLocallyFiniteMeasure μ] : α.CovariantRepresentation ↥(MeasureTheory.Lp H 2 μ)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.CStarAction.CovariantRepresentation.regular`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/Covariant/Regular.html#TauCeti.CStarAction.CovariantRepresentation.regular).

## Sources

- [Tau Ceti documentation: `TauCeti.CStarAction.CovariantRepresentation.regular`](https://taucetiproject.org/docs/TauCeti/Analysis/CStarAlgebra/Action/Covariant/Regular.html#TauCeti.CStarAction.CovariantRepresentation.regular)
- [Source of `TauCeti.CStarAction.CovariantRepresentation.regular` in TauCeti/Analysis/CStarAlgebra/Action/Covariant/Regular.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Analysis/CStarAlgebra/Action/Covariant/Regular.lean#L124)
- [Tau Ceti roadmap status: Operator-algebra dynamics, crossed products, and equilibrium](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/OperatorAlgebraDynamics/STATUS.md)
