---
declaration: def
origin: cited
lean: TauCeti.cycleCocycle
statement: formalized
---

# TauCeti.cycleCocycle

The character of a cycle, as a cyclic cocycle.

```lean
TauCeti.cycleCocycle.{u_1, u_2, u_3, u_4} {R : Type u_1} {A : Type u_2} {Ω : Type u_3}
  {M : Type u_4} [CommRing R] [NonUnitalSemiring A] [_root_.Module R A] [Ring Ω] [Algebra R Ω]
  [AddCommGroup M] [_root_.Module R M] {d : Ω →ₗ[R] Ω} {τ : Ω →ₗ[R] M} {ρ : A →ₙₐ[R] Ω} {n : ℕ}
  {𝒜 : ℤ → Submodule R Ω} [GradedAlgebra 𝒜] [IsScalarTower R A A] [SMulCommClass R A A]
  (hd : TauCeti.IsDGAlgebra 𝒜 d) (hρ : ∀ (a : A), ρ a ∈ 𝒜 0)
  (hτ : TauCeti.IsClosedGradedTrace 𝒜 d n τ) : ↥(TauCeti.cyclicCocycles R A M n)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.cycleCocycle`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/Cycle.html#TauCeti.cycleCocycle).

## Sources

- [Tau Ceti documentation: `TauCeti.cycleCocycle`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/Cycle.html#TauCeti.cycleCocycle)
- [Source of `TauCeti.cycleCocycle` in TauCeti/RingTheory/CyclicCohomology/Cycle.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/CyclicCohomology/Cycle.lean#L278)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
