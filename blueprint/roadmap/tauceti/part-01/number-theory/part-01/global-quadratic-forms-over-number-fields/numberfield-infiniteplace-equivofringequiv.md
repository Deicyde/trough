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
- [Source of `NumberField.InfinitePlace.equivOfRingEquiv` in TauCeti/NumberTheory/NumberField/InfinitePlace/Transport.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/NumberField/InfinitePlace/Transport.lean#L61)
- [Tau Ceti roadmap status: Global quadratic forms over number fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GlobalQuadraticForms/STATUS.md)
