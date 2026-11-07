---
declaration: def
origin: cited
lean: TauCeti.ClassFieldTheory.localWeilArtinEquiv
statement: formalized
---

# Local reciprocity for the Weil group

For a nonarchimedean local field `K` of
characteristic zero, the local Artin map is an isomorphism of topological groups from `Kˣ` onto
the topological abelianization of the local Weil group (`localWeilArtinEquiv_apply`).

```lean
TauCeti.ClassFieldTheory.localWeilArtinEquiv (K : Type) [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] [CharZero K] :
  Kˣ ≃ₜ* TopologicalAbelianization (TauCeti.ClassFieldTheory.WeilGroup K)
```

## Depends on

- [The Galois group of the maximal unramified extension is the profinite integers](../../part-04/local-fields-and-ramification/the-galois-group-of-the-maximal-unramified-exten.md)
- [The local class formation](the-local-class-formation.md)
- [TauCeti.algebraicExtensionNormedField](../../part-04/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.ClassFormation.tateIso](tauceti-classfieldtheory-classformation-tateiso.md)

## Proof depends on

- [TauCeti.ClassFieldTheory.invMap](tauceti-classfieldtheory-invmap.md)
- [TauCeti.kummerIso](../../part-02/continuous-cohomology-of-profinite-groups/tauceti-kummeriso.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.localWeilArtinEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/WeilGroup/Reciprocity.html#TauCeti.ClassFieldTheory.localWeilArtinEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.localWeilArtinEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/WeilGroup/Reciprocity.html#TauCeti.ClassFieldTheory.localWeilArtinEquiv)
- [Source of `TauCeti.ClassFieldTheory.localWeilArtinEquiv` in TauCeti/NumberTheory/ClassFieldTheory/WeilGroup/Reciprocity.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/WeilGroup/Reciprocity.lean#L67)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassFieldTheory/STATUS.md)
