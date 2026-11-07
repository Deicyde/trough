---
declaration: def
origin: cited
lean: TauCeti.puiseuxField.levelGalEquivRootsOfUnity
statement: formalized
---

# TauCeti.puiseuxField.levelGalEquivRootsOfUnity

If the coefficient field has a primitive `d`-th root of unity, then the Galois group of the
level-`d` subfield of the Puiseux field over `K⸨X⸩` is the group of `d`-th roots of unity of `K`.
The inverse is `levelKummer` (`TauCeti.puiseuxField.levelGalEquivRootsOfUnity_symm_apply`).

```lean
TauCeti.puiseuxField.levelGalEquivRootsOfUnity.{u_1} (K : Type u_1) [Field K] (d : ℕ+)
  [HasEnoughRootsOfUnity K ↑d] :
  Gal(↥(TauCeti.puiseuxField.level K d)/LaurentSeries K) ≃* ↥(rootsOfUnity (↑d) K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.puiseuxField.levelGalEquivRootsOfUnity`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Level/Kummer.html#TauCeti.puiseuxField.levelGalEquivRootsOfUnity).

## Sources

- [Tau Ceti documentation: `TauCeti.puiseuxField.levelGalEquivRootsOfUnity`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Level/Kummer.html#TauCeti.puiseuxField.levelGalEquivRootsOfUnity)
- [Source of `TauCeti.puiseuxField.levelGalEquivRootsOfUnity` in TauCeti/RingTheory/LaurentSeries/Level/Kummer.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/LaurentSeries/Level/Kummer.lean#L301)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
