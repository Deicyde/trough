---
declaration: theorem
origin: cited
lean: TauCeti.TypeAHeckeAlgebra.atomicTrace_eq_ocneanuTrace
statement: formalized
proof: formalized
---

# The atomic trace is the Ocneanu trace

If the weights sum to `1` and the right slice
`(if pos b then q ^ 2 else -1) * p b + (q ^ 2 - 1) * ∑ (c > b), p c` equals `q * z` for every
letter `b`, then on the Hecke algebra on any number of strands the atomic trace is the Ocneanu
trace with parameter `z`, along the embedding into the infinite type-A Hecke algebra.

```lean
TauCeti.TypeAHeckeAlgebra.atomicTrace_eq_ocneanuTrace.{u_1, u_2} {R : Type u_1} [CommRing R]
  {ι : Type u_2} {n : ℕ} [LinearOrder ι] (pos : ι → Prop) [DecidablePred pos] (q : Rˣ) (p : ι → R)
  [Fintype ι] {z : R} (hp : ∑ a, p a = 1)
  (hz :
    ∀ (b : ι), (if pos b then ↑q ^ 2 else -1) * p b + (↑q ^ 2 - 1) * ∑ c with b < c, p c = ↑q * z)
  (x : TauCeti.TypeAHeckeAlgebra R q n) :
  (TauCeti.TypeAHeckeAlgebra.atomicTrace pos q p n) x =
    (TauCeti.InfiniteTypeAHeckeAlgebra.ocneanuTrace R q z)
      ((TauCeti.TypeAHeckeAlgebra.toInfinite R q n) x)
```

## Depends on

- [TauCeti.InfiniteTypeAHeckeAlgebra](tauceti-infinitetypeaheckealgebra.md)
- [TauCeti.TypeAHeckeAlgebra.atomicTrace](tauceti-typeaheckealgebra-atomictrace.md)

## Proof depends on

- [The basis theorem](the-basis-theorem.md)
- [The finite presentation is isomorphic to the stage](the-finite-presentation-is-isomorphic-to-the-sta.md)
- [The Hecke algebra on `n` strands embeds in the infinite type-A Hecke algebra, over every commutative ring and for every unit parameter](the-hecke-algebra-on-n-strands-embeds-in-the-inf.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.TypeAHeckeAlgebra.atomicTrace_eq_ocneanuTrace`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/AtomicModel/Basic.html#TauCeti.TypeAHeckeAlgebra.atomicTrace_eq_ocneanuTrace).

## Sources

- [Tau Ceti documentation: `TauCeti.TypeAHeckeAlgebra.atomicTrace_eq_ocneanuTrace`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/AtomicModel/Basic.html#TauCeti.TypeAHeckeAlgebra.atomicTrace_eq_ocneanuTrace)
- [Source of `TauCeti.TypeAHeckeAlgebra.atomicTrace_eq_ocneanuTrace` in TauCeti/Algebra/TypeAHeckeAlgebra/AtomicModel/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/TypeAHeckeAlgebra/AtomicModel/Basic.lean#L327)
- [Tau Ceti roadmap status: Type-A Hecke algebras, braid traces, and positive quotients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TypeAHeckeAlgebras/STATUS.md)
