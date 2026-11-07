---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.globalInv_injective
statement: formalized
proof: formalized
---

# TauCeti.ClassFieldTheory.globalInv\_injective

**The global invariant is injective**, because the idele-class `H¹` vanishes and the sum of
the local invariants vanishes only on the classes that die in the idele classes.

```lean
TauCeti.ClassFieldTheory.globalInv_injective {K : Type} [Field K] [NumberField K]
  (L : TauCeti.ClassFieldTheory.NormalLayer (TauCeti.AbsoluteGaloisGroup K)) :
  Function.Injective ⇑(TauCeti.ClassFieldTheory.globalInv K L)
```

## Depends on

- [TauCeti.ClassFieldTheory.globalInv](tauceti-classfieldtheory-globalinv.md)

## Proof depends on

- [The Galois group of the maximal unramified extension is the profinite integers](../../part-04/local-fields-and-ramification/the-galois-group-of-the-maximal-unramified-exten.md)
- [The local class formation](the-local-class-formation.md)
- [TauCeti.algebraicExtensionNormedField](../../part-04/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.ClassFieldTheory.ClassFormation.tateIso](tauceti-classfieldtheory-classformation-tateiso.md)
- [TauCeti.ClassFieldTheory.invMap](tauceti-classfieldtheory-invmap.md)
- [TauCeti.relDiscr](../../part-05/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)
- [TauCeti.semilocalEquiv](../../part-05/number-fields-ramification-frobenius-and-the-lmf/tauceti-semilocalequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.globalInv_injective`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/ClassFormation.html#TauCeti.ClassFieldTheory.globalInv_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.globalInv_injective`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/ClassFormation.html#TauCeti.ClassFieldTheory.globalInv_injective)
- [Source of `TauCeti.ClassFieldTheory.globalInv_injective` in TauCeti/NumberTheory/ClassFieldTheory/Global/ClassFormation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Global/ClassFormation.lean#L245)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassFieldTheory/STATUS.md)
