---
declaration: def
origin: cited
lean: TauCeti.ContCohomology.dimensionShiftIso
statement: formalized
---

# Dimension shifting in every positive degree

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
- [Source of `TauCeti.ContCohomology.dimensionShiftIso` in TauCeti/RepresentationTheory/Homological/ContCohomology/DimensionShifting/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RepresentationTheory/Homological/ContCohomology/DimensionShifting/Basic.lean#L185)
- [Tau Ceti roadmap status: Continuous cohomology of profinite groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ProfiniteCohomology/STATUS.md)
