---
declaration: def
origin: cited
lean: TauCeti.universalGSpaceCellularStandardComparisonHomotopy
statement: formalized
---

# TauCeti.universalGSpaceCellularStandardComparisonHomotopy

The explicit geometric cellular-to-bar map agrees up to equivariant chain homotopy
with Mathlib's abstract comparison of the two projective resolutions.

```lean
TauCeti.universalGSpaceCellularStandardComparisonHomotopy.{u} (k : Type u) [CommRing k] (G : Type u)
  [Group G] :
  Homotopy
    (CategoryTheory.CategoryStruct.comp (CategoryTheory.eqToHom ⋯)
      (TauCeti.universalGSpaceCellularRepStandardHomotopyEquiv k G).hom)
    ((TauCeti.universalGSpaceCellularResolution k G).homotopyEquiv (Rep.standardResolution k G)).hom
```

## Depends on

- [Milnor's join resolution is homotopy equivalent to the standard resolution](milnors-join-resolution-is-homotopy-equivalent-t.md)

## Proof depends on

- [The Mayer–Vietoris isomorphism of a sphere](../singular/the-mayer-vietoris-isomorphism-of-a-sphere.md)
- [The relative small-chain theorem](../singular/the-relative-small-chain-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.universalGSpaceCellularStandardComparisonHomotopy`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/EquivariantChains.html#TauCeti.universalGSpaceCellularStandardComparisonHomotopy).

## Sources

- [Tau Ceti documentation: `TauCeti.universalGSpaceCellularStandardComparisonHomotopy`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/EquivariantChains.html#TauCeti.universalGSpaceCellularStandardComparisonHomotopy)
- [Source of `TauCeti.universalGSpaceCellularStandardComparisonHomotopy` in TauCeti/AlgebraicTopology/ClassifyingSpace/EquivariantChains.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/ClassifyingSpace/EquivariantChains.lean#L286)
- [Tau Ceti roadmap status: Classifying spaces of discrete groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClassifyingSpaces/STATUS.md)
