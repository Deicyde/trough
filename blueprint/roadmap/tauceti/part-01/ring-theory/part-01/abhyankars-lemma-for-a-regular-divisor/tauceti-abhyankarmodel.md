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
- [Source of `TauCeti.abhyankarModel` in TauCeti/RingTheory/DiscreteValuationRing/AbhyankarModel/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/DiscreteValuationRing/AbhyankarModel/Basic.lean#L121)
- [Tau Ceti roadmap status: Abhyankar's lemma for a regular divisor](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/AbhyankarLemma/STATUS.md)
