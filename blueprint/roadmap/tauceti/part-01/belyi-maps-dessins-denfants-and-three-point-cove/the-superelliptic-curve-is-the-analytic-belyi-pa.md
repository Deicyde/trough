---
declaration: theorem
origin: cited
lean: TauCeti.AnalyticBelyiPair.nonempty_iso_superelliptic_iff
statement: formalized
proof: formalized
---

# The superelliptic curve is the analytic Belyi pair of the torus triple

an analytic Belyi
pair is isomorphic to the superelliptic curve exactly when its monodromy triple is isomorphic to
`TauCeti.PermutationTriple.torusTriple`, for any numbering of its fibre over `1/2`.

```lean
TauCeti.AnalyticBelyiPair.nonempty_iso_superelliptic_iff {P : TauCeti.AnalyticBelyiPair}
  (ν : ↑(P.restrict ⁻¹' {TauCeti.ThricePuncturedSphere.basePt}) ≃ Fin 4) :
  Nonempty (P.Iso TauCeti.AnalyticBelyiPair.superelliptic) ↔
    TauCeti.PermutationTriple.IsoClass.mk (⋯.monodromyTriple ν) =
      TauCeti.PermutationTriple.IsoClass.mk TauCeti.PermutationTriple.torusTriple
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Analytic Belyi pairs are classified by finite covers of the thrice-punctured sphere](analytic-belyi-pairs-are-classified-by-finite-co.md)
- [Circle.fundamentalGroupMulEquiv\_fromPath](../../part-07/universal-covers/circle-fundamentalgroupmulequiv-frompath.md)
- [TauCeti.ConnectedCoverClass.isoClassEquiv](tauceti-connectedcoverclass-isoclassequiv.md)
- [TauCeti.CoveringSpace](../../part-07/universal-covers/tauceti-coveringspace.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AnalyticBelyiPair.nonempty_iso_superelliptic_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/Superelliptic.html#TauCeti.AnalyticBelyiPair.nonempty_iso_superelliptic_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.AnalyticBelyiPair.nonempty_iso_superelliptic_iff`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/Superelliptic.html#TauCeti.AnalyticBelyiPair.nonempty_iso_superelliptic_iff)
- [Source of `TauCeti.AnalyticBelyiPair.nonempty_iso_superelliptic_iff` in TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/Superelliptic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/ThricePuncturedSphere/FilledCover/Superelliptic.lean#L248)
- [Tau Ceti roadmap status: Belyi maps, dessins d'enfants, and three-point covers](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/BelyiMaps/STATUS.md)
