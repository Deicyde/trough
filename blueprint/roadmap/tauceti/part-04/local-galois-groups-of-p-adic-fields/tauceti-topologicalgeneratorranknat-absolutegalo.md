---
declaration: theorem
origin: cited
lean: TauCeti.topologicalGeneratorRankNat_absoluteGaloisGroup
statement: formalized
proof: formalized
---

# TauCeti.topologicalGeneratorRankNat\_absoluteGaloisGroup

**The generator rank of a local absolute Galois group** (NSW (7.4.1)). For a finite extension
`K` of `ℚ_p`, the absolute Galois group `G_K` needs exactly `[K : ℚ_p] + 2` topological
generators. A witness of topological finite generation is
`TauCeti.isTopologicallyFinitelyGenerated_fieldAbsoluteGaloisGroup`.

```lean
TauCeti.topologicalGeneratorRankNat_absoluteGaloisGroup (p : ℕ) [Fact (Nat.Prime p)] (K : Type)
  [Field K] [ValuativeRel K] [TopologicalSpace K] [IsNonarchimedeanLocalField K] [Algebra ℚ_[p] K]
  [Module.Finite ℚ_[p] K] [ValuativeExtension ℚ_[p] K]
  (hG : TauCeti.IsTopologicallyFinitelyGenerated (Field.absoluteGaloisGroup K)) :
  TauCeti.topologicalGeneratorRankNat (Field.absoluteGaloisGroup K) hG = Module.finrank ℚ_[p] K + 2
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The local class formation](../../part-01/class-field-theory/the-local-class-formation.md)
- [Local reciprocity for `A(L)`](local-reciprocity-for-a-l.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.ClassFormation.tateIso](../../part-01/class-field-theory/tauceti-classfieldtheory-classformation-tateiso.md)
- [TauCeti.ClassFieldTheory.invMap](../../part-01/class-field-theory/tauceti-classfieldtheory-invmap.md)
- [TauCeti.ContCohomology.dimensionShiftIso](../../part-02/continuous-cohomology-of-profinite-groups/tauceti-contcohomology-dimensionshiftiso.md)
- [TauCeti.kummerIso](../../part-02/continuous-cohomology-of-profinite-groups/tauceti-kummeriso.md)
- [TauCeti.nonempty\_layerTateModule](tauceti-nonempty-layertatemodule.md)
- [TauCeti.nonempty\_linearEquiv\_of\_projective\_of\_tensorRat](tauceti-nonempty-linearequiv-of-projective-of-te.md)
- [TauCeti.strictCohomologicalDimensionLE\_iff\_forall\_openSubgroup](../../part-02/continuous-cohomology-of-profinite-groups/tauceti-strictcohomologicaldimensionle-iff-foral.md)
- [TauCeti.wildInertiaSubgroup](../local-fields-and-ramification/tauceti-wildinertiasubgroup.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.topologicalGeneratorRankNat_absoluteGaloisGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Generation/AbsoluteGaloisGroup.html#TauCeti.topologicalGeneratorRankNat_absoluteGaloisGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.topologicalGeneratorRankNat_absoluteGaloisGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Generation/AbsoluteGaloisGroup.html#TauCeti.topologicalGeneratorRankNat_absoluteGaloisGroup)
- [Source of `TauCeti.topologicalGeneratorRankNat_absoluteGaloisGroup` in TauCeti/NumberTheory/LocalField/Generation/AbsoluteGaloisGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/Generation/AbsoluteGaloisGroup.lean#L113)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalGaloisGroups/STATUS.md)
