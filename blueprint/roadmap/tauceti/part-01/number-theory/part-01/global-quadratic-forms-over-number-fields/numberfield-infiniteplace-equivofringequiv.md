---
declaration: def
origin: cited
lean: NumberField.InfinitePlace.equivOfRingEquiv
statement: formalized
---

# NumberField.InfinitePlace.equivOfRingEquiv

The bijection between the infinite places of two fields induced by a ring isomorphism
`e : K ≃+* L`, sending `w` to `w.comap e.symm`.

```lean
NumberField.InfinitePlace.equivOfRingEquiv.{u_1, u_2} {K : Type u_1} {L : Type u_2} [Field K]
  [Field L] (e : K ≃+* L) : NumberField.InfinitePlace K ≃ NumberField.InfinitePlace L
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`NumberField.InfinitePlace.equivOfRingEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/InfinitePlace/Transport.html#NumberField.InfinitePlace.equivOfRingEquiv).

## Sources

- [Tau Ceti documentation: `NumberField.InfinitePlace.equivOfRingEquiv`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/InfinitePlace/Transport.html#NumberField.InfinitePlace.equivOfRingEquiv)
- [Source of `NumberField.InfinitePlace.equivOfRingEquiv` in TauCeti/NumberTheory/NumberField/InfinitePlace/Transport.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/NumberTheory/NumberField/InfinitePlace/Transport.lean#L63)
- [Tau Ceti roadmap status: Global quadratic forms over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/GlobalQuadraticForms/STATUS.md)
