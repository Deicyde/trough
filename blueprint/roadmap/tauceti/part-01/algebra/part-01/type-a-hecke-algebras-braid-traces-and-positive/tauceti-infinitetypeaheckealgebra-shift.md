---
declaration: def
origin: cited
lean: TauCeti.InfiniteTypeAHeckeAlgebra.shift
statement: formalized
---

# TauCeti.InfiniteTypeAHeckeAlgebra.shift

The strand shift by `k`: the algebra endomorphism `T i ↦ T (i + k)` that moves every braid
`k` strands to the right.

```lean
TauCeti.InfiniteTypeAHeckeAlgebra.shift.{u_1} (R : Type u_1) [CommRing R] (q : Rˣ) (k : ℕ) :
  TauCeti.InfiniteTypeAHeckeAlgebra R q →ₐ[R] TauCeti.InfiniteTypeAHeckeAlgebra R q
```

## Depends on

- [TauCeti.InfiniteTypeAHeckeAlgebra](tauceti-infinitetypeaheckealgebra.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.InfiniteTypeAHeckeAlgebra.shift`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/Infinite.html#TauCeti.InfiniteTypeAHeckeAlgebra.shift).

## Sources

- [Tau Ceti documentation: `TauCeti.InfiniteTypeAHeckeAlgebra.shift`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/Infinite.html#TauCeti.InfiniteTypeAHeckeAlgebra.shift)
- [Source of `TauCeti.InfiniteTypeAHeckeAlgebra.shift` in TauCeti/Algebra/TypeAHeckeAlgebra/Infinite.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/TypeAHeckeAlgebra/Infinite.lean#L654)
- [Tau Ceti roadmap status: Type-A Hecke algebras, braid traces, and positive quotients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/TypeAHeckeAlgebras/STATUS.md)
