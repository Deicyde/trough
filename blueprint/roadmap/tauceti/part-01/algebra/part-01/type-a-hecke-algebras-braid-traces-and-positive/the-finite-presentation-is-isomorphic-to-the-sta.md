---
declaration: def
origin: cited
lean: TauCeti.TypeAHeckeAlgebra.stageEquiv
statement: formalized
---

# The finite presentation is isomorphic to the stage

the Hecke algebra on `n` strands is
isomorphic to the stage of the first `n` strands of the infinite type-A Hecke algebra, by the map
`T i ↦ T i`.

```lean
TauCeti.TypeAHeckeAlgebra.stageEquiv.{u_1} (R : Type u_1) [CommRing R] (q : Rˣ) (n : ℕ) :
  TauCeti.TypeAHeckeAlgebra R q n ≃ₐ[R] ↥(TauCeti.InfiniteTypeAHeckeAlgebra.stage R q n)
```

## Depends on

- [The Hecke algebra on `n` strands embeds in the infinite type-A Hecke algebra, over every commutative ring and for every unit parameter](the-hecke-algebra-on-n-strands-embeds-in-the-inf.md)
- [TauCeti.InfiniteTypeAHeckeAlgebra](tauceti-infinitetypeaheckealgebra.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TypeAHeckeAlgebra.stageEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/Embedding.html#TauCeti.TypeAHeckeAlgebra.stageEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.TypeAHeckeAlgebra.stageEquiv`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/Embedding.html#TauCeti.TypeAHeckeAlgebra.stageEquiv)
- [Source of `TauCeti.TypeAHeckeAlgebra.stageEquiv` in TauCeti/Algebra/TypeAHeckeAlgebra/Embedding.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/TypeAHeckeAlgebra/Embedding.lean#L154)
- [Tau Ceti roadmap status: Type-A Hecke algebras, braid traces, and positive quotients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TypeAHeckeAlgebras/STATUS.md)
