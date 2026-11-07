---
declaration: def
origin: cited
lean: TauCeti.GridDiagram.IsKnot.tau
statement: formalized
---

# The invariant `τ` of a knot grid diagram

minus the largest Alexander degree of a
homogeneous element of the unblocked grid homology `GH⁻(G)` that is not `K[U]`-torsion.

Over a Noetherian `K`, the supremum is attained as soon as `GH⁻(G)` is not a torsion module
(`isGreatest_nonTorsionDegrees_neg_tau`); if `GH⁻(G)` is torsion the value is `0`, the supremum
of the empty set. It is an invariant of the presented knot: knot grids connected by grid moves
have the same `τ` (`tau_eq_of_movesTo`, in `Homology/Invariance.lean`). This is the grid
definition of the concordance invariant `τ` of Ozsváth--Stipsicz--Szabó.

```lean
TauCeti.GridDiagram.IsKnot.tau.{u_1} {n : ℕ} {G : TauCeti.GridDiagram n} (hG : G.IsKnot)
  (K : Type u_1) [CommRing K] [CharP K 2] : ℤ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GridDiagram.IsKnot.tau`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Homology/Tau.html#TauCeti.GridDiagram.IsKnot.tau).

## Sources

- [Tau Ceti documentation: `TauCeti.GridDiagram.IsKnot.tau`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Homology/Tau.html#TauCeti.GridDiagram.IsKnot.tau)
- [Source of `TauCeti.GridDiagram.IsKnot.tau` in TauCeti/KnotTheory/Grid/Homology/Tau.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/KnotTheory/Grid/Homology/Tau.lean#L88)
- [Tau Ceti roadmap status: Combinatorial Heegaard Floer and grid homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/CombinatorialHeegaardFloer/STATUS.md)
