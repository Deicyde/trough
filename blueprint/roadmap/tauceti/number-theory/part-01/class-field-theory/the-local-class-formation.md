---
declaration: def
origin: cited
lean: TauCeti.ClassFieldTheory.localClassFormation
statement: formalized
---

# The local class formation

the formation of the units of a separable closure of a
nonarchimedean local field `K` is a class formation, with the invariant `layerInv` of a layer as
invariant map.

```lean
TauCeti.ClassFieldTheory.localClassFormation (K : Type) [Field K] [ValuativeRel K]
  [TopologicalSpace K] [IsNonarchimedeanLocalField K] :
  TauCeti.ClassFieldTheory.ClassFormation (TauCeti.ClassFieldTheory.unitsFormation K)
```

## Depends on

- [The local invariant](the-local-invariant.md)

## Proof depends on

- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [Artin's theorem for a finite group of automorphisms](../../../representation-theory/continuous-cohomology-of-profinite-groups/artins-theorem-for-a-finite-group-of-automorphis.md)
- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Hensel's lemma for the norm](../../../ring-theory/part-02/other-results/part-01/hensels-lemma-for-the-norm.md)
- [Shapiro's lemma in degree one](../../../representation-theory/homological/shapiros-lemma-in-degree-one.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.localClassFormation`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/ClassFormation.html#TauCeti.ClassFieldTheory.localClassFormation).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.localClassFormation`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/ClassFormation.html#TauCeti.ClassFieldTheory.localClassFormation)
- [Source of `TauCeti.ClassFieldTheory.localClassFormation` in TauCeti/NumberTheory/ClassFieldTheory/Local/ClassFormation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Local/ClassFormation.lean#L116)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassFieldTheory/STATUS.md)
