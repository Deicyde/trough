---
declaration: def
origin: cited
lean: LinearMap.traceDualBasis
statement: formalized
---

# LinearMap.traceDualBasis

The basis dual to `b` for the trace pairing, with the same indexing type.

```lean
LinearMap.traceDualBasis.{u_1, u_2, u_3} {R : Type u_1} {A : Type u_2} [CommSemiring R]
  [CommSemiring A] [Algebra R A] (ε : A →ₗ[R] R) [hε : ((LinearMap.mul R A).compr₂ ε).IsPerfPair]
  {ι : Type u_3} [Finite ι] (b : Module.Basis ι R A) : Module.Basis ι R A
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`LinearMap.traceDualBasis`](https://taucetiproject.org/docs/TauCeti/Algebra/Algebra/Frobenius/Coalgebra.html#LinearMap.traceDualBasis).

## Sources

- [Tau Ceti documentation: `LinearMap.traceDualBasis`](https://taucetiproject.org/docs/TauCeti/Algebra/Algebra/Frobenius/Coalgebra.html#LinearMap.traceDualBasis)
- [Source of `LinearMap.traceDualBasis` in TauCeti/Algebra/Algebra/Frobenius/Coalgebra.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Algebra/Frobenius/Coalgebra.lean#L190)
- [Tau Ceti roadmap status: Foams](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Foams/STATUS.md)
