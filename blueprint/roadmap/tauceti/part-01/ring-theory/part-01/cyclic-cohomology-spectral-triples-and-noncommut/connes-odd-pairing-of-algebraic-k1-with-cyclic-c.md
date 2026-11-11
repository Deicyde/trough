---
declaration: def
origin: cited
lean: TauCeti.AlgebraicK1.oddPairing
statement: formalized
---

# Connes' odd pairing of algebraic `K₁` with cyclic cohomology in degree `2m + 1`

the class
of an invertible matrix `u` is sent to the functional `[φ] ↦ ⟨[u], [φ]⟩` on `HC²ᵐ⁺¹(A; M)`,
computed through the matrix extension `φ#Tr`. It is a homomorphism to the additive group of
functionals, written multiplicatively.

```lean
TauCeti.AlgebraicK1.oddPairing.{u_1, u_2} (A : Type u_1) (M : Type u_2) [Ring A] [Algebra ℂ A]
  [AddCommGroup M] [_root_.Module ℂ M] (m : ℕ) :
  TauCeti.AlgebraicK1 A →* Multiplicative (↑(TauCeti.cyclicCohomology ℂ A M (2 * m + 1)) →ₗ[ℂ] M)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.AlgebraicK1.oddPairing`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/OddPairing/AlgebraicK1.html#TauCeti.AlgebraicK1.oddPairing).

## Sources

- [Tau Ceti documentation: `TauCeti.AlgebraicK1.oddPairing`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/OddPairing/AlgebraicK1.html#TauCeti.AlgebraicK1.oddPairing)
- [Source of `TauCeti.AlgebraicK1.oddPairing` in TauCeti/RingTheory/CyclicCohomology/OddPairing/AlgebraicK1.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/CyclicCohomology/OddPairing/AlgebraicK1.lean#L74)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
