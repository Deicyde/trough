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

- [TauCeti.GradedProjectiveResolution.IsLinear](../../algebra/part-01/grothendieck-groups-cartan-maps-and-euler-forms/tauceti-gradedprojectiveresolution-islinear.md)

## Proof depends on

- [The entrywise graded Cartan formula](../quiver/the-entrywise-graded-cartan-formula.md)
- [The Koszul defect formula](../quiver/the-koszul-defect-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.forall_exists_isLinear_zigzagGradedSimple_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Projective/Koszul/NonDynkin.html#TauCeti.forall_exists_isLinear_zigzagGradedSimple_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.forall_exists_isLinear_zigzagGradedSimple_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Projective/Koszul/NonDynkin.html#TauCeti.forall_exists_isLinear_zigzagGradedSimple_iff)
- [Source of `TauCeti.forall_exists_isLinear_zigzagGradedSimple_iff` in TauCeti/RepresentationTheory/Quiver/Zigzag/Projective/Koszul/NonDynkin.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Quiver/Zigzag/Projective/Koszul/NonDynkin.lean#L83)
- [Tau Ceti roadmap status: Zigzag, preprojective, and Ginzburg algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ZigzagPreprojective/STATUS.md)
