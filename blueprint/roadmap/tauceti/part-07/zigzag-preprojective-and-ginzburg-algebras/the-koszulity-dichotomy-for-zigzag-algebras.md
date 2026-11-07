---
declaration: theorem
origin: cited
lean: TauCeti.forall_exists_isLinear_zigzagGradedSimple_iff
statement: formalized
proof: formalized
---

# The Koszulity dichotomy for zigzag algebras

for a connected finite simple graph `G` on at
least two vertices, every graded vertex simple of `ZigzagAlgebra k G` admits a linear graded
projective resolution if and only if `G` is not isomorphic to the diagram of any valid Dynkin
type.

```lean
TauCeti.forall_exists_isLinear_zigzagGradedSimple_iff.{u, w} (k : Type w) [Field k] {V : Type u}
  {G : SimpleGraph V} [Finite V] [Nontrivial V] (hG : G.Connected) :
  (∀ (v : V), ∃ r, r.IsLinear) ↔ ¬∃ t, t.Valid ∧ Nonempty (G ≃g TauCeti.diagramGraph t.cartanMatrix)
```

## Depends on

- [TauCeti.GradedProjectiveResolution.IsLinear](../../part-04/grothendieck-groups-cartan-maps-and-euler-forms/tauceti-gradedprojectiveresolution-islinear.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.forall_exists_isLinear_zigzagGradedSimple_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Projective/Koszul/NonDynkin.html#TauCeti.forall_exists_isLinear_zigzagGradedSimple_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.forall_exists_isLinear_zigzagGradedSimple_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Projective/Koszul/NonDynkin.html#TauCeti.forall_exists_isLinear_zigzagGradedSimple_iff)
- [Source of `TauCeti.forall_exists_isLinear_zigzagGradedSimple_iff` in TauCeti/RepresentationTheory/Quiver/Zigzag/Projective/Koszul/NonDynkin.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Quiver/Zigzag/Projective/Koszul/NonDynkin.lean#L83)
- [Tau Ceti roadmap status: Zigzag, preprojective, and Ginzburg algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ZigzagPreprojective/STATUS.md)
