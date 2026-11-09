---
declaration: theorem
origin: cited
lean: TauCeti.Henselization.henselian
statement: formalized
proof: formalized
---

# The henselization of a pair is henselian

The pair formed by the henselization of
`(R, I)` and the extended ideal is a henselian pair, with no hypothesis on `R` or `I`.

```lean
TauCeti.Henselization.henselian.{u} {R : Type u} [CommRing R] (I : Ideal R) :
  HenselianRing (↑(TauCeti.Henselization.algebra I)) (TauCeti.Henselization.extended I)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Henselization.henselian`](https://taucetiproject.org/docs/TauCeti/RingTheory/Henselization/Henselian.html#TauCeti.Henselization.henselian).

## Sources

- [Tau Ceti documentation: `TauCeti.Henselization.henselian`](https://taucetiproject.org/docs/TauCeti/RingTheory/Henselization/Henselian.html#TauCeti.Henselization.henselian)
- [Source of `TauCeti.Henselization.henselian` in TauCeti/RingTheory/Henselization/Henselian.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Henselization/Henselian.lean#L152)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
