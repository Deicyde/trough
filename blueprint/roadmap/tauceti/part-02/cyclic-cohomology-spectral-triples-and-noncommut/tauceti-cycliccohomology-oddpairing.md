---
declaration: def
origin: cited
lean: TauCeti.cyclicCohomology.oddPairing
statement: formalized
---

# TauCeti.cyclicCohomology.oddPairing

**Connes' odd pairing** `⟨[u], [φ]⟩ = (1 + i)⁻¹ 2⁻ⁿ Γ(n/2 + 1)⁻¹ φ(u⁻¹ - 1, u - 1, …, u - 1)`
of an invertible `u` with cyclic cohomology classes of odd degree `n = 2m + 1`.

```lean
TauCeti.cyclicCohomology.oddPairing.{u_1, u_2} {A : Type u_1} {M : Type u_2} [Ring A] [Algebra ℂ A]
  [AddCommGroup M] [_root_.Module ℂ M] (u : Aˣ) (m : ℕ) :
  ↑(TauCeti.cyclicCohomology ℂ A M (2 * m + 1)) →ₗ[ℂ] M
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.cyclicCohomology.oddPairing`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/OddPairing/Basic.html#TauCeti.cyclicCohomology.oddPairing).

## Sources

- [Tau Ceti documentation: `TauCeti.cyclicCohomology.oddPairing`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/OddPairing/Basic.html#TauCeti.cyclicCohomology.oddPairing)
- [Source of `TauCeti.cyclicCohomology.oddPairing` in TauCeti/RingTheory/CyclicCohomology/OddPairing/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/CyclicCohomology/OddPairing/Basic.lean#L105)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
