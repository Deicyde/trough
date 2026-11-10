---
declaration: theorem
origin: cited
lean: TauCeti.topologicalGeneratorRankNat_absoluteGaloisGroup
statement: formalized
proof: formalized
---

# The generator rank of a local absolute Galois group (NSW (7.4.1))

For a finite extension
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

- [Burnside's basis theorem, cardinal form](../../../topology/algebra/part-01/burnsides-basis-theorem-cardinal-form.md)
- [The finite level of the generator theorem (NSW, proof of (7.4.1))](../../part-02/local-field/the-finite-level-of-the-generator-theorem-nsw-pr.md)
- [The Kummer isomorphism](../../../representation-theory/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)
- [The Schreier bound](../../../topology/algebra/part-01/the-schreier-bound.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [The wild inertia subgroup](../local-fields-and-ramification/the-wild-inertia-subgroup.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.topologicalGeneratorRankNat_absoluteGaloisGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Generation/AbsoluteGaloisGroup.html#TauCeti.topologicalGeneratorRankNat_absoluteGaloisGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.topologicalGeneratorRankNat_absoluteGaloisGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Generation/AbsoluteGaloisGroup.html#TauCeti.topologicalGeneratorRankNat_absoluteGaloisGroup)
- [Source of `TauCeti.topologicalGeneratorRankNat_absoluteGaloisGroup` in TauCeti/NumberTheory/LocalField/Generation/AbsoluteGaloisGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/Generation/AbsoluteGaloisGroup.lean#L113)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalGaloisGroups/STATUS.md)
