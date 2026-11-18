---
declaration: def
origin: cited
lean: TauCeti.TypeAHeckeAlgebra.atomicTrace
statement: formalized
---

# TauCeti.TypeAHeckeAlgebra.atomicTrace

The atomic trace `x ↦ tr (ρ(x) * D)` on the Hecke algebra on `n` strands, where `ρ` is the
signed checked representation and `D` is the product density of the weights `p`.

```lean
TauCeti.TypeAHeckeAlgebra.atomicTrace.{u_1, u_2} {R : Type u_1} [CommRing R] {ι : Type u_2}
  [LinearOrder ι] (pos : ι → Prop) [DecidablePred pos] (q : Rˣ) (p : ι → R) (n : ℕ) :
  TauCeti.TypeAHeckeAlgebra R q n →ₗ[R] R
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.TypeAHeckeAlgebra.atomicTrace`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/AtomicModel/Basic.html#TauCeti.TypeAHeckeAlgebra.atomicTrace).

## Sources

- [Tau Ceti documentation: `TauCeti.TypeAHeckeAlgebra.atomicTrace`](https://taucetiproject.org/docs/TauCeti/Algebra/TypeAHeckeAlgebra/AtomicModel/Basic.html#TauCeti.TypeAHeckeAlgebra.atomicTrace)
- [Source of `TauCeti.TypeAHeckeAlgebra.atomicTrace` in TauCeti/Algebra/TypeAHeckeAlgebra/AtomicModel/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/TypeAHeckeAlgebra/AtomicModel/Basic.lean#L227)
- [Tau Ceti roadmap status: Type-A Hecke algebras, braid traces, and positive quotients](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/TypeAHeckeAlgebras/STATUS.md)
