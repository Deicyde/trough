---
declaration: theorem
origin: cited
lean: TauCeti.GridDiagram.IsKnot.unblockedHomologyIsomorphic_of_movesTo
statement: formalized
proof: formalized
---

# Invariance of `GH⁻` under grid moves

Knot grid diagrams connected by arbitrary grid
moves have isomorphic unblocked grid homologies as Alexander-graded `K[U]`-modules.

```lean
TauCeti.GridDiagram.IsKnot.unblockedHomologyIsomorphic_of_movesTo.{u_1} {n m : ℕ}
  {G : TauCeti.GridDiagram n} {G' : TauCeti.GridDiagram m} (hG : G.IsKnot) (K : Type u_1)
  [CommRing K] [CharP K 2] (hG' : G'.IsKnot) (h : G.MovesTo G') :
  hG.UnblockedHomologyIsomorphic hG' K
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Graded Nakayama lemma for free complexes over a polynomial ring](../../algebra/part-02/homology/graded-nakayama-lemma-for-free-complexes-over-a.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.GridDiagram.IsKnot.unblockedHomologyIsomorphic_of_movesTo`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Homology/Invariance.html#TauCeti.GridDiagram.IsKnot.unblockedHomologyIsomorphic_of_movesTo).

## Sources

- [Tau Ceti documentation: `TauCeti.GridDiagram.IsKnot.unblockedHomologyIsomorphic_of_movesTo`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Homology/Invariance.html#TauCeti.GridDiagram.IsKnot.unblockedHomologyIsomorphic_of_movesTo)
- [Source of `TauCeti.GridDiagram.IsKnot.unblockedHomologyIsomorphic_of_movesTo` in TauCeti/KnotTheory/Grid/Homology/Invariance.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/KnotTheory/Grid/Homology/Invariance.lean#L97)
- [Tau Ceti roadmap status: Combinatorial Heegaard Floer and grid homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/CombinatorialHeegaardFloer/STATUS.md)
