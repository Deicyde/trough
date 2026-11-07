---
declaration: def
origin: cited
lean: TauCeti.InfiniteTypeAHeckeAlgebra
statement: formalized
---

# TauCeti.InfiniteTypeAHeckeAlgebra

The infinite type-A Hecke algebra over `R` with parameter `q`: the free `R`-algebra on `ℕ`
modulo `TauCeti.InfiniteTypeAHeckeAlgebra.Rel`. It is the union of its finite stages
`TauCeti.InfiniteTypeAHeckeAlgebra.stage R q n`; see the module docstring for what is proved about
them.

```lean
TauCeti.InfiniteTypeAHeckeAlgebra.{u_1} (R : Type u_1) [CommRing R] (q : Rˣ) : Type u_1
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.InfiniteTypeAHeckeAlgebra`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/Infinite.html#TauCeti.InfiniteTypeAHeckeAlgebra).

## Sources

- [Tau Ceti documentation: `TauCeti.InfiniteTypeAHeckeAlgebra`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/Infinite.html#TauCeti.InfiniteTypeAHeckeAlgebra)
- [Source of `TauCeti.InfiniteTypeAHeckeAlgebra` in TauCeti/Algebra/TypeAHeckeAlgebra/Infinite.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/TypeAHeckeAlgebra/Infinite.lean#L135)
- [Tau Ceti roadmap status: Type-A Hecke algebras, braid traces, and positive quotients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TypeAHeckeAlgebras/STATUS.md)
