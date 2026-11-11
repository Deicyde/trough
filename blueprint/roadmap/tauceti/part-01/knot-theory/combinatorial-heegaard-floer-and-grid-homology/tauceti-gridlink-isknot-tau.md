---
declaration: def
origin: cited
lean: TauCeti.GridLink.IsKnot.tau
statement: formalized
---

# TauCeti.GridLink.IsKnot.tau

The integer invariant `τ` of a grid knot, evaluated on a presenting knot diagram.

It is independent of the representative by `GridDiagram.IsKnot.tau_eq_of_movesTo`.
The coefficient ring is retained explicitly, as in the diagram invariant.

```lean
TauCeti.GridLink.IsKnot.tau.{u_1} {L : TauCeti.GridLink} (hL : L.IsKnot) (K : Type u_1) [CommRing K]
  [CharP K 2] : ℤ
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.GridLink.IsKnot.tau`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Move/Tau.html#TauCeti.GridLink.IsKnot.tau).

## Sources

- [Tau Ceti documentation: `TauCeti.GridLink.IsKnot.tau`](https://taucetiproject.org/docs/TauCeti/KnotTheory/Grid/Move/Tau.html#TauCeti.GridLink.IsKnot.tau)
- [Source of `TauCeti.GridLink.IsKnot.tau` in TauCeti/KnotTheory/Grid/Move/Tau.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/KnotTheory/Grid/Move/Tau.lean#L40)
- [Tau Ceti roadmap status: Combinatorial Heegaard Floer and grid homology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CombinatorialHeegaardFloer/STATUS.md)
