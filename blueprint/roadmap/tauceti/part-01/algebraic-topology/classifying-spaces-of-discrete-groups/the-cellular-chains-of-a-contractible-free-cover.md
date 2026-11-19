---
declaration: def
origin: cited
lean: TauCeti.cellularResolution
statement: formalized
---

# The cellular chains of a contractible free cover are a projective resolution of the trivial representation of `G` over `R`

if the lift `p ⁻¹' C` of the CW complex `C` is
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

## Proof depends on

- [The Mayer–Vietoris isomorphism of a sphere](../singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The relative small-chain theorem](../singular/the-relative-small-chain-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.cellularResolution`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cellular/Resolution.html#TauCeti.cellularResolution).

## Sources

- [Tau Ceti documentation: `TauCeti.cellularResolution`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cellular/Resolution.html#TauCeti.cellularResolution)
- [Source of `TauCeti.cellularResolution` in TauCeti/AlgebraicTopology/Cellular/Resolution.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/Cellular/Resolution.lean#L162)
- [Tau Ceti roadmap status: Classifying spaces of discrete groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClassifyingSpaces/STATUS.md)
