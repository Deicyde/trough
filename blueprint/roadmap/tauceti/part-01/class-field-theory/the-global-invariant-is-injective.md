---
declaration: theorem
origin: cited
lean: TauCeti.ClassFieldTheory.globalInv_injective
statement: formalized
proof: formalized
---

# The global invariant is injective

, because the idele-class `H¹` vanishes and the sum of
the local invariants vanishes only on the classes that die in the idele classes.

```lean
TauCeti.ClassFieldTheory.globalInv_injective {K : Type} [Field K] [NumberField K]
  (L : TauCeti.ClassFieldTheory.NormalLayer (TauCeti.AbsoluteGaloisGroup K)) :
  Function.Injective ⇑(TauCeti.ClassFieldTheory.globalInv K L)
```

## Depends on

- [The global invariant](the-global-invariant.md)

## Proof depends on

- [The Galois group of the maximal unramified extension is the profinite integers](../../part-04/local-fields-and-ramification/the-galois-group-of-the-maximal-unramified-exten.md)
- [The local class formation](the-local-class-formation.md)
- [The local invariant](the-local-invariant.md)
- [The semi-local decomposition](../../part-05/number-fields-ramification-frobenius-and-the-lmf/the-semi-local-decomposition.md)
- [Tate's theorem for a class formation](tates-theorem-for-a-class-formation.md)
- [TauCeti.algebraicExtensionNormedField](../../part-04/local-fields-and-ramification/tauceti-algebraicextensionnormedfield.md)
- [TauCeti.relDiscr](../../part-05/number-fields-ramification-frobenius-and-the-lmf/tauceti-reldiscr.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.globalInv_injective`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/ClassFormation.html#TauCeti.ClassFieldTheory.globalInv_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.globalInv_injective`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/ClassFormation.html#TauCeti.ClassFieldTheory.globalInv_injective)
- [Source of `TauCeti.ClassFieldTheory.globalInv_injective` in TauCeti/NumberTheory/ClassFieldTheory/Global/ClassFormation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Global/ClassFormation.lean#L245)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassFieldTheory/STATUS.md)
