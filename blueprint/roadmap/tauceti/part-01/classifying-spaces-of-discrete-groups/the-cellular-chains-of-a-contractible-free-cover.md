---
declaration: def
origin: cited
lean: TauCeti.cellularResolution
statement: formalized
---

# The cellular chains of a contractible free cover are a projective resolution

of the
trivial representation of `G` over `R`: if the lift `p ⁻¹' C` of the CW complex `C` is
contractible, its cellular chain complex, on which `G` acts through translation of the lifted
cells, is a complex of free representations whose augmentation is a quasi-isomorphism.

```lean
TauCeti.cellularResolution.{w} {E B : Type w} [TopologicalSpace E] [TopologicalSpace B] {p : E → B}
  (C : Set B) {G : Type w} [Group G] [MulAction G E] (hG : IsQuotientCoveringMap p G) [T2Space B]
  [Topology.CWComplex C] (R : Type w) [CommRing R] [ContractibleSpace ↑(p ⁻¹' C)] :
  CategoryTheory.ProjectiveResolution (Rep.trivial R G R)
```

## Depends on

- [A CW structure lifts along a covering map](a-cw-structure-lifts-along-a-covering-map.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.cellularResolution`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cellular/Resolution.html#TauCeti.cellularResolution).

## Sources

- [Tau Ceti documentation: `TauCeti.cellularResolution`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cellular/Resolution.html#TauCeti.cellularResolution)
- [Source of `TauCeti.cellularResolution` in TauCeti/AlgebraicTopology/Cellular/Resolution.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/Cellular/Resolution.lean#L162)
- [Tau Ceti roadmap status: Classifying spaces of discrete groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassifyingSpaces/STATUS.md)
