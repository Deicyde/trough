---
declaration: theorem
origin: cited
lean: LinearMap.frobeniusCoalgebra_comul_eq_sum
statement: formalized
proof: formalized
---

# LinearMap.frobeniusCoalgebra_comul_eq_sum

The dual-basis formula for the reconstructed coproduct, valid for every
finite basis, not just a chosen one.

```lean
LinearMap.frobeniusCoalgebra_comul_eq_sum.{u_1, u_2, u_3} {R : Type u_1} {A : Type u_2}
  [CommSemiring R] [CommSemiring A] [Algebra R A] [Module.Finite R A] [Module.Projective R A]
  (ε : A →ₗ[R] R) [hε : ((LinearMap.mul R A).compr₂ ε).IsPerfPair] {ι : Type u_3} [Fintype ι]
  (b : Module.Basis ι R A) (a : A) :
  CoalgebraStruct.comul a = ∑ i, b i ⊗ₜ[R] ((ε.traceDualBasis b) i * a)
```

## Depends on

- [LinearMap.frobeniusCoalgebra](linearmap-frobeniuscoalgebra.md)
- [LinearMap.traceDualBasis](linearmap-tracedualbasis.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.frobeniusCoalgebra_comul_eq_sum`](https://taucetiproject.org/docs/TauCeti/Algebra/Algebra/Frobenius/Coalgebra.html#LinearMap.frobeniusCoalgebra_comul_eq_sum).

## Sources

- [Tau Ceti documentation: `LinearMap.frobeniusCoalgebra_comul_eq_sum`](https://taucetiproject.org/docs/TauCeti/Algebra/Algebra/Frobenius/Coalgebra.html#LinearMap.frobeniusCoalgebra_comul_eq_sum)
- [Source of `LinearMap.frobeniusCoalgebra_comul_eq_sum` in TauCeti/Algebra/Algebra/Frobenius/Coalgebra.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Algebra/Algebra/Frobenius/Coalgebra.lean#L214)
- [Tau Ceti roadmap status: Foams](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/Foams/STATUS.md)
