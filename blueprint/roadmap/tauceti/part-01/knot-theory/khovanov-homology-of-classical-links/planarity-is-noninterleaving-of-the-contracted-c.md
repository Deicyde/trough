---
declaration: theorem
origin: cited
lean: TauCeti.PDCode.isPlanar_iff_isNoncrossingMatching
statement: formalized
proof: formalized
---

# Planarity is noninterleaving of the contracted chord diagram

A PD-code with connected
underlying graph is planar exactly when the bands of a spanning-tree contraction of the graph do
not interleave, in any numbering of the half-edges making its single vertex cyclic rotation.

```lean
TauCeti.PDCode.isPlanar_iff_isNoncrossingMatching {n : ℕ} {D : TauCeti.PDCode n}
  (hD : D.toPermutationTriple.IsConnected)
  (c : TauCeti.SpanningTreeContraction D.crossingRotation ↑D.edgePair) {m : ℕ}
  (e : Fin (4 * n) ≃ Fin m) (he : e.permCongr c.rotation = finRotate m) :
  D.IsPlanar ↔ (e.permCongr c.matching).IsNoncrossingMatching
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Euler's formula for a PD-code](../other-results/eulers-formula-for-a-pd-code.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.PDCode.isPlanar_iff_isNoncrossingMatching`](https://taucetiproject.org/docs/TauCeti/KnotTheory/PDCode/ChordDiagram.html#TauCeti.PDCode.isPlanar_iff_isNoncrossingMatching).

## Sources

- [Tau Ceti documentation: `TauCeti.PDCode.isPlanar_iff_isNoncrossingMatching`](https://taucetiproject.org/docs/TauCeti/KnotTheory/PDCode/ChordDiagram.html#TauCeti.PDCode.isPlanar_iff_isNoncrossingMatching)
- [Source of `TauCeti.PDCode.isPlanar_iff_isNoncrossingMatching` in TauCeti/KnotTheory/PDCode/ChordDiagram.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/KnotTheory/PDCode/ChordDiagram.lean#L52)
- [Tau Ceti roadmap status: Khovanov homology of classical links](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/KhovanovHomology/STATUS.md)
