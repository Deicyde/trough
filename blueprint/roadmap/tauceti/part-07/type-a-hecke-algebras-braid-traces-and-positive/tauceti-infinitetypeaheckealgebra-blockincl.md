---
declaration: def
origin: cited
lean: TauCeti.InfiniteTypeAHeckeAlgebra.blockIncl
statement: formalized
---

# TauCeti.InfiniteTypeAHeckeAlgebra.blockIncl

The disjoint block map: the algebra map from the tensor product of the stages `a` and `b` to
the stage `a + b` that places the first factor on the first `a` strands and the second factor,
shifted by `a`, on the next `b` strands. Its injectivity, which would make it an embedding,
needs the basis theorem and is not proved here.

```lean
TauCeti.InfiniteTypeAHeckeAlgebra.blockIncl.{u_1} (R : Type u_1) [CommRing R] (q : Rˣ) (a b : ℕ) :
  TensorProduct R ↥(TauCeti.InfiniteTypeAHeckeAlgebra.stage R q a)
      ↥(TauCeti.InfiniteTypeAHeckeAlgebra.stage R q b) →ₐ[R]
    ↥(TauCeti.InfiniteTypeAHeckeAlgebra.stage R q (a + b))
```

## Depends on

- [TauCeti.InfiniteTypeAHeckeAlgebra](tauceti-infinitetypeaheckealgebra.md)
- [TauCeti.InfiniteTypeAHeckeAlgebra.shift](tauceti-infinitetypeaheckealgebra-shift.md)
- [TauCeti.InfiniteTypeAHeckeAlgebra.stage](tauceti-infinitetypeaheckealgebra-stage.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.InfiniteTypeAHeckeAlgebra.blockIncl`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/Infinite.html#TauCeti.InfiniteTypeAHeckeAlgebra.blockIncl).

## Sources

- [Tau Ceti documentation: `TauCeti.InfiniteTypeAHeckeAlgebra.blockIncl`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/Infinite.html#TauCeti.InfiniteTypeAHeckeAlgebra.blockIncl)
- [Source of `TauCeti.InfiniteTypeAHeckeAlgebra.blockIncl` in TauCeti/Algebra/TypeAHeckeAlgebra/Infinite.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/TypeAHeckeAlgebra/Infinite.lean#L720)
- [Tau Ceti roadmap status: Type-A Hecke algebras, braid traces, and positive quotients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/TypeAHeckeAlgebras/STATUS.md)
