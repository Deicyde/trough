---
declaration: theorem
origin: cited
lean: TauCeti.existsUnique_frobeniusCoalgebra
statement: formalized
proof: formalized
---

# TauCeti.existsUnique_frobeniusCoalgebra

A perfect trace on a finite projective commutative algebra determines a unique
coalgebra with that counit satisfying the Frobenius law.

```lean
TauCeti.existsUnique_frobeniusCoalgebra.{u_1, u_2} (R : Type u_1) (A : Type u_2) [CommSemiring R]
  [CommSemiring A] [Algebra R A] [Module.Finite R A] [Module.Projective R A] (ε : A →ₗ[R] R)
  (hε : ((LinearMap.mul R A).compr₂ ε).IsPerfPair) :
  ∃! c, CoalgebraStruct.counit = ε ∧ Coalgebra.IsFrobenius R A
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [LinearMap.frobeniusCoalgebra](linearmap-frobeniuscoalgebra.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.existsUnique_frobeniusCoalgebra`](https://taucetiproject.org/docs/TauCeti/Algebra/Algebra/Frobenius/Coalgebra.html#TauCeti.existsUnique_frobeniusCoalgebra).

## Sources

- [Tau Ceti documentation: `TauCeti.existsUnique_frobeniusCoalgebra`](https://taucetiproject.org/docs/TauCeti/Algebra/Algebra/Frobenius/Coalgebra.html#TauCeti.existsUnique_frobeniusCoalgebra)
- [Source of `TauCeti.existsUnique_frobeniusCoalgebra` in TauCeti/Algebra/Algebra/Frobenius/Coalgebra.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Algebra/Frobenius/Coalgebra.lean#L243)
- [Tau Ceti roadmap status: Foams](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Foams/STATUS.md)
