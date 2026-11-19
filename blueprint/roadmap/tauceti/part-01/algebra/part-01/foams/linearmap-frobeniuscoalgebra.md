---
declaration: def
origin: cited
lean: LinearMap.frobeniusCoalgebra
statement: formalized
---

# LinearMap.frobeniusCoalgebra

The coalgebra obtained by transposing multiplication under a perfect trace
pairing. Its counit is the prescribed trace.

```lean
LinearMap.frobeniusCoalgebra.{u_1, u_2} {R : Type u_1} {A : Type u_2} [CommSemiring R]
  [CommSemiring A] [Algebra R A] [Module.Finite R A] [Module.Projective R A] (ε : A →ₗ[R] R)
  [hε : ((LinearMap.mul R A).compr₂ ε).IsPerfPair] : Coalgebra R A
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.frobeniusCoalgebra`](https://taucetiproject.org/docs/TauCeti/Algebra/Algebra/Frobenius/Coalgebra.html#LinearMap.frobeniusCoalgebra).

## Sources

- [Tau Ceti documentation: `LinearMap.frobeniusCoalgebra`](https://taucetiproject.org/docs/TauCeti/Algebra/Algebra/Frobenius/Coalgebra.html#LinearMap.frobeniusCoalgebra)
- [Source of `LinearMap.frobeniusCoalgebra` in TauCeti/Algebra/Algebra/Frobenius/Coalgebra.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Algebra/Frobenius/Coalgebra.lean#L45)
- [Tau Ceti roadmap status: Foams](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Foams/STATUS.md)
