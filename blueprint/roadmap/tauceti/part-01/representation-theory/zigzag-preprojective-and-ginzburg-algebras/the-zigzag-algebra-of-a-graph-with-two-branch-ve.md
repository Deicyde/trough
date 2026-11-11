---
declaration: theorem
origin: cited
lean: TauCeti.not_isIntrinsicallyFormal_zigzagStrictAInfinityAlgebra_of_three_le_degree
statement: formalized
proof: formalized
---

# The zigzag algebra of a graph with two branch vertices in one component is not intrinsically formal

**The zigzag algebra of a graph with two branch vertices in one component is not
intrinsically formal**, over every nontrivial commutative ring in which `2` is invertible: if two
distinct vertices `v` and `w` of `G`, each of degree at least three, are joined by a walk, then
some `A∞` algebra whose cohomology algebra is the path-graded zigzag algebra is not formal. The
detecting deformation is that of `TauCeti.not_isFormal_zigzagLoopAInfinityAlgebra_single_of_walk`
along a path from `v` to `w`. Together with
`TauCeti.not_isIntrinsicallyFormal_zigzagStrictAInfinityAlgebra_of_four_le_degree` this covers
every finite tree other than a path or a tree with exactly one vertex of degree three.

```lean
TauCeti.not_isIntrinsicallyFormal_zigzagStrictAInfinityAlgebra_of_three_le_degree.{u, w}
  {k : Type w} [CommRing k] {V : Type u} {G : SimpleGraph V} [Finite V]
  {hns : ∀ (i : V), ∃ j, G.Adj i j} [Nontrivial k] [Invertible 2] {v w : V}
  [Fintype ↑(G.neighborSet v)] [Fintype ↑(G.neighborSet w)] (hvw : v ≠ w) (hr : G.Reachable v w)
  (hv : 3 ≤ G.degree v) (hw : 3 ≤ G.degree w) :
  ¬(TauCeti.zigzagStrictAInfinityAlgebra k hns).IsIntrinsicallyFormal
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.not_isIntrinsicallyFormal_zigzagStrictAInfinityAlgebra_of_three_le_degree`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/AInfinity/NonFormal.html#TauCeti.not_isIntrinsicallyFormal_zigzagStrictAInfinityAlgebra_of_three_le_degree).

## Sources

- [Tau Ceti documentation: `TauCeti.not_isIntrinsicallyFormal_zigzagStrictAInfinityAlgebra_of_three_le_degree`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Quiver/Zigzag/AInfinity/NonFormal.html#TauCeti.not_isIntrinsicallyFormal_zigzagStrictAInfinityAlgebra_of_three_le_degree)
- [Source of `TauCeti.not_isIntrinsicallyFormal_zigzagStrictAInfinityAlgebra_of_three_le_degree` in TauCeti/RepresentationTheory/Quiver/Zigzag/AInfinity/NonFormal.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RepresentationTheory/Quiver/Zigzag/AInfinity/NonFormal.lean#L201)
- [Tau Ceti roadmap status: Zigzag, preprojective, and Ginzburg algebras](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ZigzagPreprojective/STATUS.md)
