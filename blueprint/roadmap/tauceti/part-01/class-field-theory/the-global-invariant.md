---
declaration: def
origin: cited
lean: TauCeti.ClassFieldTheory.globalInv
statement: formalized
---

# The global invariant

`H²(Gal(L/F), C_L) → ℚ/ℤ` of a finite normal layer `L/F` inside
`Kˢ`: the invariant of a class is the sum of the local invariants of a lift to the ideles of its
inflation to some refinement of the layer. By `globalInv_eq` it does not depend on the refinement
or on the lift, and `globalInv_unique` characterizes it by the equations `globalInv_ideleToClassH2`
and `globalInv_infl`.

```lean
TauCeti.ClassFieldTheory.globalInv (K : Type) [Field K] [NumberField K]
  (L : TauCeti.ClassFieldTheory.NormalLayer (TauCeti.AbsoluteGaloisGroup K)) :
  ↑(L.H (TauCeti.ClassFieldTheory.globalFormation K) 2) →+ AddCircle 1
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

Formalized in Tau Ceti as [`TauCeti.ClassFieldTheory.globalInv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/ClassFormation.html#TauCeti.ClassFieldTheory.globalInv).

## Sources

- [Tau Ceti documentation: `TauCeti.ClassFieldTheory.globalInv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassFieldTheory/Global/ClassFormation.html#TauCeti.ClassFieldTheory.globalInv)
- [Source of `TauCeti.ClassFieldTheory.globalInv` in TauCeti/NumberTheory/ClassFieldTheory/Global/ClassFormation.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/ClassFieldTheory/Global/ClassFormation.lean#L169)
- [Tau Ceti roadmap status: Class field theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassFieldTheory/STATUS.md)
