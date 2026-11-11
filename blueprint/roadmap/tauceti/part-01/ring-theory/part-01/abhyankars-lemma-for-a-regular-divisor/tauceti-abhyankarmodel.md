---
declaration: abbrev
origin: cited
lean: TauCeti.abhyankarModel
statement: formalized
---

# TauCeti.abhyankarModel

The local model of Abhyankar's lemma, `(B[y]/(y ^ e − u))[x]/(x ^ d − ϖ y)`: the standard
cover of `B[y]/(y ^ e − u)` along `ϖ y` with exponent `d`. In it `x ^ (e d) = u ϖ ^ e`
(`TauCeti.abhyankarModelRoot_pow_mul`), and `y = x ^ d / ϖ` once `ϖ` is inverted.

```lean
TauCeti.abhyankarModel.{u} {B : Type u} [CommRing B] (ϖ u : B) (e d : ℕ) : Type u
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.abhyankarModel`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/AbhyankarModel/Basic.html#TauCeti.abhyankarModel).

## Sources

- [Tau Ceti documentation: `TauCeti.abhyankarModel`](https://taucetiproject.org/docs/TauCeti/RingTheory/DiscreteValuationRing/AbhyankarModel/Basic.html#TauCeti.abhyankarModel)
- [Source of `TauCeti.abhyankarModel` in TauCeti/RingTheory/DiscreteValuationRing/AbhyankarModel/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/DiscreteValuationRing/AbhyankarModel/Basic.lean#L119)
- [Tau Ceti roadmap status: Abhyankar's lemma for a regular divisor](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/AbhyankarLemma/STATUS.md)
