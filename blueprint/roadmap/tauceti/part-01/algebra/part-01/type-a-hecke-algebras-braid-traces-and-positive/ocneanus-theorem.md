---
declaration: theorem
origin: cited
lean: TauCeti.InfiniteTypeAHeckeAlgebra.existsUnique_isMarkovTrace, TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace.eq_ocneanuTrace
statement: formalized
proof: formalized
---

# Ocneanu's theorem

For every parameter `z` there is exactly one Markov trace with
parameter `z`.

```lean
TauCeti.InfiniteTypeAHeckeAlgebra.existsUnique_isMarkovTrace.{u_1} {R : Type u_1} [CommRing R]
  {q : Rˣ} (z : R) : ∃! τ, TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace z τ
```

## Depends on

- [TauCeti.InfiniteTypeAHeckeAlgebra](tauceti-infinitetypeaheckealgebra.md)

## Proof depends on

- [The basis theorem](the-basis-theorem.md)
- [The finite presentation is isomorphic to the stage](the-finite-presentation-is-isomorphic-to-the-sta.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.InfiniteTypeAHeckeAlgebra.existsUnique_isMarkovTrace`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/OcneanuTrace.html#TauCeti.InfiniteTypeAHeckeAlgebra.existsUnique_isMarkovTrace).

## Other forms

**Ocneanu's theorem.** Formalized in Tau Ceti as [`TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace.eq_ocneanuTrace`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/OcneanuTrace.html#TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace.eq_ocneanuTrace).

```lean
TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace.eq_ocneanuTrace.{u_1} {R : Type u_1} [CommRing R]
  {q : Rˣ} {z : R} {τ : TauCeti.InfiniteTypeAHeckeAlgebra R q →ₗ[R] R}
  (hτ : TauCeti.InfiniteTypeAHeckeAlgebra.IsMarkovTrace z τ) :
  τ = TauCeti.InfiniteTypeAHeckeAlgebra.ocneanuTrace R q z
```

## Sources

- [Tau Ceti documentation: `TauCeti.InfiniteTypeAHeckeAlgebra.existsUnique_isMarkovTrace`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/OcneanuTrace.html#TauCeti.InfiniteTypeAHeckeAlgebra.existsUnique_isMarkovTrace)
- [Source of `TauCeti.InfiniteTypeAHeckeAlgebra.existsUnique_isMarkovTrace` in TauCeti/Algebra/TypeAHeckeAlgebra/OcneanuTrace.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/TypeAHeckeAlgebra/OcneanuTrace.lean#L493)
- [Tau Ceti roadmap status: Type-A Hecke algebras, braid traces, and positive quotients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TypeAHeckeAlgebras/STATUS.md)
