---
declaration: class
origin: cited
lean: TauCeti.Excellence.RegularAlgebraMap
statement: formalized
---

# TauCeti.Excellence.RegularAlgebraMap

An `R`-algebra `B` is a *regular algebra*, or `R → B` is a *regular ring map*, if `B` is flat
over `R` and for every prime `p` of `R` the fibre `κ(p) ⊗[R] B` is geometrically regular over the
residue field `κ(p)` (Stacks, Definition 15.42.1).

```lean
TauCeti.Excellence.RegularAlgebraMap.{u, v} (R : Type u) (B : Type v) [CommRing R] [CommRing B]
  [Algebra R B] : Prop
```

## Depends on

- [TauCeti.Excellence.GeometricallyRegular](tauceti-excellence-geometricallyregular.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Excellence.RegularAlgebraMap`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/RegularAlgebraMap.html#TauCeti.Excellence.RegularAlgebraMap).

## Sources

- [Tau Ceti documentation: `TauCeti.Excellence.RegularAlgebraMap`](https://taucetiproject.org/docs/TauCeti/RingTheory/RegularLocalRing/RegularAlgebraMap.html#TauCeti.Excellence.RegularAlgebraMap)
- [Source of `TauCeti.Excellence.RegularAlgebraMap` in TauCeti/RingTheory/RegularLocalRing/RegularAlgebraMap.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/RegularLocalRing/RegularAlgebraMap.lean#L54)
- [Tau Ceti roadmap status: Scheme, stack, cohomology and intersection foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SchemeAndStackFoundations/STATUS.md)
