---
declaration: theorem
origin: cited
lean: TauCeti.TypeAHeckeAlgebra.toInfinite_injective
statement: formalized
proof: formalized
---

# The Hecke algebra on `n` strands embeds in the infinite type-A Hecke algebra, over every commutative ring and for every unit parameter

```lean
TauCeti.TypeAHeckeAlgebra.toInfinite_injective.{u_1} (R : Type u_1) [CommRing R] (q : Rˣ) (n : ℕ) :
  Function.Injective ⇑(TauCeti.TypeAHeckeAlgebra.toInfinite R q n)
```

## Depends on

- [TauCeti.InfiniteTypeAHeckeAlgebra](tauceti-infinitetypeaheckealgebra.md)

## Proof depends on

- [The basis theorem](the-basis-theorem.md)
- [Matsumoto's theorem, relational form](../../../group-theory/coxeter/matsumotos-theorem-relational-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TypeAHeckeAlgebra.toInfinite_injective`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/Embedding.html#TauCeti.TypeAHeckeAlgebra.toInfinite_injective).

## Sources

- [Tau Ceti documentation: `TauCeti.TypeAHeckeAlgebra.toInfinite_injective`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/Embedding.html#TauCeti.TypeAHeckeAlgebra.toInfinite_injective)
- [Source of `TauCeti.TypeAHeckeAlgebra.toInfinite_injective` in TauCeti/Algebra/TypeAHeckeAlgebra/Embedding.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/TypeAHeckeAlgebra/Embedding.lean#L141)
- [Tau Ceti roadmap status: Type-A Hecke algebras, braid traces, and positive quotients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TypeAHeckeAlgebras/STATUS.md)
