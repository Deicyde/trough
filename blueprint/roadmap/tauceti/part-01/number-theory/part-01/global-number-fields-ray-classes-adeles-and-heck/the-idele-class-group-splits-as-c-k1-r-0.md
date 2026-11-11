---
declaration: def
origin: cited
lean: TauCeti.GlobalNumberFields.normOneProdEquiv
statement: formalized
---

# The idele class group splits as `C_K¹ × ℝ>0`

The infinite place `w` determines the
isomorphism of topological groups sending an idele class `c` to its norm-one part
`c · s(‖c‖)⁻¹` and its norm `‖c‖`, where `s = ideleClassNormSection K w`.

```lean
TauCeti.GlobalNumberFields.normOneProdEquiv.{u_1} {K : Type u_1} [Field K] [NumberField K]
  (w : NumberField.InfinitePlace K) :
  NumberField.IdeleClassGroup (NumberField.RingOfIntegers K) K ≃ₜ*
    ↥(TauCeti.GlobalNumberFields.IdeleClassGroup.normOne K) × NNRealˣ
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [IsDedekindDomain.FiniteAdeleRing.sIntegralAdeles](isdedekinddomain-finiteadelering-sintegraladeles.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.GlobalNumberFields.normOneProdEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/Ideles/Norm/Splitting.html#TauCeti.GlobalNumberFields.normOneProdEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.GlobalNumberFields.normOneProdEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/Global/Ideles/Norm/Splitting.html#TauCeti.GlobalNumberFields.normOneProdEquiv)
- [Source of `TauCeti.GlobalNumberFields.normOneProdEquiv` in TauCeti/NumberTheory/NumberField/Global/Ideles/Norm/Splitting.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/Global/Ideles/Norm/Splitting.lean#L128)
- [Tau Ceti roadmap status: Global number fields, ray classes, adeles, and Hecke characters](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/GlobalNumberFields/STATUS.md)
