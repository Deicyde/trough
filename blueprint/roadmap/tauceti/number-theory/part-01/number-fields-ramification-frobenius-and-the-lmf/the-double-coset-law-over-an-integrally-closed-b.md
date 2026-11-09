---
declaration: def
origin: cited
lean: Ideal.doubleCosetQuotientEquivPrimesOverOfIsIntegralClosure
statement: formalized
---

# The double coset law over an integrally closed base

For `M / K` finite Galois with
group `G`, a subgroup `H` of `G`, the integral closures `B` and `C` of `A` in `M` and in `M ^ H`,
and a prime `Q` of `B` above `p` with decomposition group `D`, the primes of `C` above `p` are
indexed by the double cosets `H \ G / D`.

The class of `σ` corresponds to the contraction `σ Q ∩ C`, by
`Ideal.doubleCosetQuotientEquivPrimesOverOfIsIntegralClosure_mk`.

```lean
Ideal.doubleCosetQuotientEquivPrimesOverOfIsIntegralClosure.{u_1, u_2, u_3, u_4, u_5} {A : Type u_1}
  {K : Type u_2} {M : Type u_3} {B : Type u_4} [CommRing A] [Field K] [Algebra A K]
  [IsFractionRing A K] [Field M] [Algebra K M] [FiniteDimensional K M] [IsGalois K M] [Algebra A M]
  [IsScalarTower A K M] [CommRing B] [Algebra A B] [Algebra B M] [IsScalarTower A B M]
  [IsIntegralClosure B A M] [MulSemiringAction Gal(M/K) B] [SMulDistribClass Gal(M/K) B M]
  (Q : Ideal B) [Q.IsPrime] (p : Ideal A) [Q.LiesOver p] (H : Subgroup Gal(M/K))
  [Algebra A ↥(IntermediateField.fixedField H)]
  [IsScalarTower A K ↥(IntermediateField.fixedField H)] (C : Type u_5) [CommRing C] [Algebra A C]
  [Algebra C ↥(IntermediateField.fixedField H)]
  [IsScalarTower A C ↥(IntermediateField.fixedField H)]
  [IsIntegralClosure C A ↥(IntermediateField.fixedField H)] [Algebra C B] [Algebra C M]
  [IsScalarTower A C B] [IsScalarTower C (↥(IntermediateField.fixedField H)) M]
  [IsScalarTower C B M] [IsDomain A] [IsIntegrallyClosed A] :
  DoubleCoset.Quotient ↑H ↑(MulAction.stabilizer Gal(M/K) Q) ≃ ↑(p.primesOver C)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Ideal.doubleCosetQuotientEquivPrimesOverOfIsIntegralClosure`](https://taucetiproject.org/docs/TauCeti/NumberTheory/RamificationInertia/DoubleCoset/IntegralClosure.html#Ideal.doubleCosetQuotientEquivPrimesOverOfIsIntegralClosure).

## Sources

- [Tau Ceti documentation: `Ideal.doubleCosetQuotientEquivPrimesOverOfIsIntegralClosure`](https://taucetiproject.org/docs/TauCeti/NumberTheory/RamificationInertia/DoubleCoset/IntegralClosure.html#Ideal.doubleCosetQuotientEquivPrimesOverOfIsIntegralClosure)
- [Source of `Ideal.doubleCosetQuotientEquivPrimesOverOfIsIntegralClosure` in TauCeti/NumberTheory/RamificationInertia/DoubleCoset/IntegralClosure.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/RamificationInertia/DoubleCoset/IntegralClosure.lean#L94)
- [Tau Ceti roadmap status: Number fields, ramification, Frobenius, and the LMFDB invariants](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/NumberFieldArithmetic/STATUS.md)
