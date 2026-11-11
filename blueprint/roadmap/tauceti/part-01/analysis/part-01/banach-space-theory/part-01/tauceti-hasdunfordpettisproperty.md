---
declaration: def
origin: cited
lean: TauCeti.HasDunfordPettisProperty
statement: formalized
---

# TauCeti.HasDunfordPettisProperty

A normed space `E` has the *Dunford–Pettis property* if every weakly compact operator from
`E` into a Banach space is Dunford–Pettis. The definition quantifies over Banach spaces in the
universe of `E`; by `TauCeti.HasDunfordPettisProperty.isDunfordPettis` the conclusion then holds
for weakly compact operators into normed spaces in every universe.

```lean
TauCeti.HasDunfordPettisProperty.{u, u_1} (𝕜 : Type u_1) (E : Type u) [RCLike 𝕜]
  [NormedAddCommGroup E] [NormedSpace 𝕜 E] : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.HasDunfordPettisProperty`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/DunfordPettis/Basic.html#TauCeti.HasDunfordPettisProperty).

## Sources

- [Tau Ceti documentation: `TauCeti.HasDunfordPettisProperty`](https://taucetiproject.org/docs/TauCeti/Analysis/Normed/Operator/DunfordPettis/Basic.html#TauCeti.HasDunfordPettisProperty)
- [Source of `TauCeti.HasDunfordPettisProperty` in TauCeti/Analysis/Normed/Operator/DunfordPettis/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Analysis/Normed/Operator/DunfordPettis/Basic.lean#L243)
- [Tau Ceti roadmap status: Banach space theory](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/BanachSpaceTheory/STATUS.md)
