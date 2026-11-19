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

Its statement uses no other declaration mapped here.

## Proof depends on

- [The entrywise graded Cartan formula](../quiver/the-entrywise-graded-cartan-formula.md)
- [The Koszul defect formula](../quiver/the-koszul-defect-formula.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.forall_exists_isLinear_zigzagGradedSimple_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Projective/Koszul/NonDynkin.html#TauCeti.forall_exists_isLinear_zigzagGradedSimple_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.forall_exists_isLinear_zigzagGradedSimple_iff`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/Projective/Koszul/NonDynkin.html#TauCeti.forall_exists_isLinear_zigzagGradedSimple_iff)
- [Source of `TauCeti.forall_exists_isLinear_zigzagGradedSimple_iff` in TauCeti/RepresentationTheory/Quiver/Zigzag/Projective/Koszul/NonDynkin.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/Quiver/Zigzag/Projective/Koszul/NonDynkin.lean#L83)
- [Tau Ceti roadmap status: Zigzag, preprojective, and Ginzburg algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ZigzagPreprojective/STATUS.md)
