---
declaration: def
origin: cited
lean: TauCeti.AnalyticBelyiPair.isoClassEquivConnectedCoverClass
statement: formalized
---

# Analytic Belyi pairs are classified by finite covers of the thrice-punctured sphere

Restricting the Belyi map over `ℂ ∖ {0, 1}` and filling the punctures are inverse bijections between
isomorphism classes of analytic Belyi pairs of degree `n` and isomorphism classes of connected
degree-`n` covers of `ℂ ∖ {0, 1}`.

```lean
TauCeti.AnalyticBelyiPair.isoClassEquivConnectedCoverClass (n : ℕ) :
  Quotient (TauCeti.AnalyticBelyiPair.isoSetoid n) ≃
    TauCeti.ConnectedCoverClass TauCeti.ThricePuncturedSphere.basePt n
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The isomorphism `π₁(S¹) ≃* ℤ` is the degree](../../part-07/universal-covers/the-isomorphism-1-s1-z-is-the-degree.md)
- [TauCeti.CoveringSpace](../../part-07/universal-covers/tauceti-coveringspace.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AnalyticBelyiPair.isoClassEquivConnectedCoverClass`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/AnalyticBelyiPair.html#TauCeti.AnalyticBelyiPair.isoClassEquivConnectedCoverClass).

## Sources

- [Tau Ceti documentation: `TauCeti.AnalyticBelyiPair.isoClassEquivConnectedCoverClass`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/AnalyticBelyiPair.html#TauCeti.AnalyticBelyiPair.isoClassEquivConnectedCoverClass)
- [Source of `TauCeti.AnalyticBelyiPair.isoClassEquivConnectedCoverClass` in TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/AnalyticBelyiPair.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/AnalyticBelyiPair.lean#L284)
- [Tau Ceti roadmap status: Belyi maps, dessins d'enfants, and three-point covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BelyiMaps/STATUS.md)
