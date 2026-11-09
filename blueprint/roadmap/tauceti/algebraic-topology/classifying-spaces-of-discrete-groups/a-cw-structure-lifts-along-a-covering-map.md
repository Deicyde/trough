---
declaration: def
origin: cited
lean: TauCeti.cwComplexPreimage
statement: formalized
---

# A CW structure lifts along a covering map

If `C` is a CW complex in the Hausdorff space
`B` and `p : E → B` is a covering map, then `p ⁻¹' C` is a CW complex in `E`. Its `n`-cells are the
pairs of an `n`-cell of `C` and a point of `E` over the centre of that cell
(`TauCeti.cellPreimageEquiv`); the characteristic map of such a pair is the lift of the
characteristic map of the cell through `p` sending the centre to the chosen point.

```lean
TauCeti.cwComplexPreimage.{u} {E B : Type u} [TopologicalSpace B] {p : E → B} (C : Set B)
  [TopologicalSpace E] [Topology.CWComplex C] [T2Space B] (hp : IsCoveringMap p) :
  Topology.CWComplex (p ⁻¹' C)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.cwComplexPreimage`](https://taucetiproject.org/docs/TauCeti/Topology/CWComplex/Classical/Covering.html#TauCeti.cwComplexPreimage).

## Sources

- [Tau Ceti documentation: `TauCeti.cwComplexPreimage`](https://taucetiproject.org/docs/TauCeti/Topology/CWComplex/Classical/Covering.html#TauCeti.cwComplexPreimage)
- [Source of `TauCeti.cwComplexPreimage` in TauCeti/Topology/CWComplex/Classical/Covering.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Topology/CWComplex/Classical/Covering.lean#L392)
- [Tau Ceti roadmap status: Classifying spaces of discrete groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassifyingSpaces/STATUS.md)
