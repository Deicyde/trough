---
declaration: theorem
origin: cited
lean: TauCeti.TypeAHeckeAlgebra.instIsSemisimpleRing
statement: formalized
proof: formalized
---

# TauCeti.TypeAHeckeAlgebra.instIsSemisimpleRing

The finite Hecke algebra at a real nonzero parameter is semisimple. In particular,
every module over this algebra is completely reducible.

```lean
TauCeti.TypeAHeckeAlgebra.instIsSemisimpleRing.{u_1} {𝕜 : Type u_1} [RCLike 𝕜] {q : 𝕜ˣ} {n : ℕ}
  [Fact (IsSelfAdjoint ↑q)] : IsSemisimpleRing (TauCeti.TypeAHeckeAlgebra 𝕜 q n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The basis theorem](the-basis-theorem.md)
- [The finite presentation is isomorphic to the stage](the-finite-presentation-is-isomorphic-to-the-sta.md)
- [The Hecke algebra on `n` strands embeds in the infinite type-A Hecke algebra, over every commutative ring and for every unit parameter](the-hecke-algebra-on-n-strands-embeds-in-the-inf.md)
- [Matsumoto's theorem, relational form](../../../group-theory/coxeter/matsumotos-theorem-relational-form.md)
- [TauCeti.InfiniteTypeAHeckeAlgebra](tauceti-infinitetypeaheckealgebra.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TypeAHeckeAlgebra.instIsSemisimpleRing`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/Semisimple.html#TauCeti.TypeAHeckeAlgebra.instIsSemisimpleRing).

## Sources

- [Tau Ceti documentation: `TauCeti.TypeAHeckeAlgebra.instIsSemisimpleRing`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/Semisimple.html#TauCeti.TypeAHeckeAlgebra.instIsSemisimpleRing)
- [Source of `TauCeti.TypeAHeckeAlgebra.instIsSemisimpleRing` in TauCeti/Algebra/TypeAHeckeAlgebra/Semisimple.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/TypeAHeckeAlgebra/Semisimple.lean#L38)
- [Tau Ceti roadmap status: Type-A Hecke algebras, braid traces, and positive quotients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TypeAHeckeAlgebras/STATUS.md)
