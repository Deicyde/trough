---
declaration: def
origin: cited
lean: TauCeti.ContCohomology.dimensionShiftIso
statement: formalized
---

# TauCeti.ContCohomology.dimensionShiftIso

**Dimension shifting in every positive degree**, `Hⁱ⁺¹(G, M) ≅ Hⁱ(G, Coind_1^G M ⧸ M)` for
`i ≥ 1` and a compact group `G`, as an isomorphism of Mathlib's canonical continuous cohomology. Its
inverse is the connecting map of `TauCeti.ContCohomology.coindShortExact G ⊥ M`
(`dimensionShiftIso_inv`), an isomorphism by `isIso_coindShortExact_bot_delta`. The analogous
statement on the explicit low-degree model, for a profinite `G` and in the direction of the
connecting map, is `TauCeti.ContCohomology.explicitDimensionShift1 :
H¹(G, Coind_1^G M ⧸ M) ≃+ H²(G, M)`.

```lean
TauCeti.ContCohomology.dimensionShiftIso.{u} (G : Type u) [Group G] [TopologicalSpace G]
  [IsTopologicalGroup G] [CompactSpace G] (M : Type u) [AddCommGroup M] [TopologicalSpace M]
  [DiscreteTopology M] [DistribMulAction G M] [ContinuousSMul G M] (i : ℕ) (hi : 0 < i) :
  continuousCohomology (i + 1) (TauCeti.ofDiscreteModule ℤ G M) ≅
    continuousCohomology i
      (TauCeti.ofDiscreteModule ℤ G (TauCeti.ContCohomology.CoindQuotient G ⊥ M))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.ContCohomology.dimensionShiftIso`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/DimensionShifting/Basic.html#TauCeti.ContCohomology.dimensionShiftIso).

## Sources

- [Tau Ceti documentation: `TauCeti.ContCohomology.dimensionShiftIso`](https://taucetiproject.org/docs/TauCeti/RepresentationTheory/Homological/ContCohomology/DimensionShifting/Basic.html#TauCeti.ContCohomology.dimensionShiftIso)
- [Source of `TauCeti.ContCohomology.dimensionShiftIso` in TauCeti/RepresentationTheory/Homological/ContCohomology/DimensionShifting/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RepresentationTheory/Homological/ContCohomology/DimensionShifting/Basic.lean#L185)
- [Tau Ceti roadmap status: Continuous cohomology of profinite groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ProfiniteCohomology/STATUS.md)
