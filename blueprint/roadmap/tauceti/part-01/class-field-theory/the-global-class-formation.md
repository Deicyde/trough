---
declaration: def
origin: cited
lean: TauCeti.ClassFieldTheory.globalClassFormation
statement: formalized
---

# The global class formation

the idele-class formation of `K` is a class formation, whose
invariant on a layer is the global invariant (`globalClassFormation_inv`).

```lean
TauCeti.ClassFieldTheory.globalClassFormation (K : Type) [Field K] [NumberField K] :
  TauCeti.ClassFieldTheory.ClassFormation (TauCeti.ClassFieldTheory.globalFormation K)
```

## Depends on

- [The local invariant](the-local-invariant.md)
- [The semi-local decomposition](../../part-05/number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition.md)

## Proof depends on

- [The Galois group of the maximal unramified extension is the profinite integers](../../part-04/local-fields-and-ramification/the-galois-group-of-the-maximal-unramified-exten.md)
- [The local class formation](the-local-class-formation.md)
- [Tate's theorem for a class formation](tates-theorem-for-a-class-formation.md)
- [TauCeti.algebraicExtensionNormedField](../../part-04/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.relDiscr](../../part-05/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.globalClassFormation`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/ClassFormation.html#TauCeti.ClassFieldTheory.globalClassFormation).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.globalClassFormation`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/ClassFormation.html#TauCeti.ClassFieldTheory.globalClassFormation)
- [Source of `TauCeti.ClassFieldTheory.globalClassFormation` in TauCeti/NumberTheory/ClassFieldTheory/Global/ClassFormation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Global/ClassFormation.lean#L265)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassFieldTheory/STATUS.md)
