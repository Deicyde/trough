---
declaration: def
origin: cited
lean: TauCeti.ConnectedCoverClass.isoClassEquiv
statement: formalized
---

# Connected covers of `ℂ ∖ {0, 1}` of degree `n` up to isomorphism are classified by the isomorphism classes of connected triples of degree `n`

```lean
TauCeti.ConnectedCoverClass.isoClassEquiv {n : ℕ} :
  TauCeti.ConnectedCoverClass TauCeti.ThricePuncturedSphere.basePt n ≃ TauCeti.ConnectedIsoClass n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The based Seifert--van Kampen theorem](../fundamental-group/the-based-seifert-van-kampen-theorem.md)
- [The isomorphism `π₁(S¹) ≃* ℤ` is the degree](../universal-covers/the-isomorphism-1-s1-z-is-the-degree.md)
- [TauCeti.CoveringSpace](../universal-covers/tauceti-coveringspace.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ConnectedCoverClass.isoClassEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ThricePuncturedSphere/Classification.html#TauCeti.ConnectedCoverClass.isoClassEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.ConnectedCoverClass.isoClassEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ThricePuncturedSphere/Classification.html#TauCeti.ConnectedCoverClass.isoClassEquiv)
- [Source of `TauCeti.ConnectedCoverClass.isoClassEquiv` in TauCeti/AlgebraicTopology/ThricePuncturedSphere/Classification.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/ThricePuncturedSphere/Classification.lean#L283)
- [Tau Ceti roadmap status: Belyi maps, dessins d'enfants, and three-point covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BelyiMaps/STATUS.md)
