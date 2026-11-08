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

- [The local invariant `inv_K : Br K ≃+ ℚ/ℤ` of a nonarchimedean local field `K`, normalized by arithmetic Frobenius](the-local-invariant-inv-k-br-k-q-z-of-a-nonarchi.md)

## Proof depends on

- [Artin's theorem](../../../field-theory/galois/artins-theorem.md)
- [Dedekind's different theorem, the tame case](../../part-02/local-field/dedekinds-different-theorem-the-tame-case.md)
- [The first half of Dedekind's different theorem](../../part-02/local-field/the-first-half-of-dedekinds-different-theorem.md)
- [Hensel's lemma with an estimate over a Henselian discrete valuation ring](../counting-totally-ramified-extensions-of-a-local/part-01/hensels-lemma-with-an-estimate-over-a-henselian.md)
- [Shapiro's lemma in every degree](../../../representation-theory/homological/shapiros-lemma-in-every-degree.md)
- [TauCeti.algebraicExtensionNormedField](../local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.localClassFormation`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/ClassFormation.html#TauCeti.ClassFieldTheory.localClassFormation).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.localClassFormation`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Local/ClassFormation.html#TauCeti.ClassFieldTheory.localClassFormation)
- [Source of `TauCeti.ClassFieldTheory.localClassFormation` in TauCeti/NumberTheory/ClassFieldTheory/Local/ClassFormation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Local/ClassFormation.lean#L116)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassFieldTheory/STATUS.md)
