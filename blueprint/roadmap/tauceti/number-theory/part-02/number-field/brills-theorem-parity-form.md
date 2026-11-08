---
declaration: theorem
origin: cited
lean: NumberField.InfinitePlace.even_nrComplexPlaces_iff_zero_lt_discr
statement: formalized
proof: formalized
---

# Brill's theorem, parity form

The number of complex places is even exactly when the
discriminant is positive.

```lean
NumberField.InfinitePlace.even_nrComplexPlaces_iff_zero_lt_discr.{u_1} (K : Type u_1) [Field K]
  [NumberField K] : Even (NumberField.InfinitePlace.nrComplexPlaces K) ↔ 0 < NumberField.discr K
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`NumberField.InfinitePlace.even_nrComplexPlaces_iff_zero_lt_discr`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/InfinitePlace/Basic.html#NumberField.InfinitePlace.even_nrComplexPlaces_iff_zero_lt_discr).

## Sources

- [Tau Ceti documentation: `NumberField.InfinitePlace.even_nrComplexPlaces_iff_zero_lt_discr`](https://taucetiproject.org/docs/TauCeti/NumberTheory/NumberField/InfinitePlace/Basic.html#NumberField.InfinitePlace.even_nrComplexPlaces_iff_zero_lt_discr)
- [Source of `NumberField.InfinitePlace.even_nrComplexPlaces_iff_zero_lt_discr` in TauCeti/NumberTheory/NumberField/InfinitePlace/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/NumberField/InfinitePlace/Basic.lean#L219)
