---
declaration: theorem
origin: cited
lean: TauCeti.topologicalGeneratorRankNat_absoluteGaloisGroup
statement: formalized
proof: formalized
---

# The generator rank of a local absolute Galois group

(NSW (7.4.1)). For a finite extension
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

- [Dimension shifting in every positive degree](../../part-02/continuous-cohomology-of-profinite-groups/dimension-shifting-in-every-positive-degree.md)
- [Existence of the Tate module of a finite layer](existence-of-the-tate-module-of-a-finite-layer.md)
- [The Kummer isomorphism](../../part-02/continuous-cohomology-of-profinite-groups/the-kummer-isomorphism.md)
- [The local class formation](../../part-01/class-field-theory/the-local-class-formation.md)
- [The local invariant](../../part-01/class-field-theory/the-local-invariant.md)
- [Local reciprocity for `A(L)`](local-reciprocity-for-a-l.md)
- [The strict cohomological dimension through integral coefficients](../../part-02/continuous-cohomology-of-profinite-groups/the-strict-cohomological-dimension-through-integ.md)
- [Swan's theorem for `ℤ_p\[G\]`](swans-theorem-for-z-p-g.md)
- [Tate's theorem for a class formation](../../part-01/class-field-theory/tates-theorem-for-a-class-formation.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [The wild inertia subgroup](../local-fields-and-ramification/the-wild-inertia-subgroup.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.topologicalGeneratorRankNat_absoluteGaloisGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Generation/AbsoluteGaloisGroup.html#TauCeti.topologicalGeneratorRankNat_absoluteGaloisGroup).

## Sources

- [Tau Ceti documentation: `TauCeti.topologicalGeneratorRankNat_absoluteGaloisGroup`](https://taucetiproject.org/docs/TauCeti/NumberTheory/LocalField/Generation/AbsoluteGaloisGroup.html#TauCeti.topologicalGeneratorRankNat_absoluteGaloisGroup)
- [Source of `TauCeti.topologicalGeneratorRankNat_absoluteGaloisGroup` in TauCeti/NumberTheory/LocalField/Generation/AbsoluteGaloisGroup.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/LocalField/Generation/AbsoluteGaloisGroup.lean#L113)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalGaloisGroups/STATUS.md)
