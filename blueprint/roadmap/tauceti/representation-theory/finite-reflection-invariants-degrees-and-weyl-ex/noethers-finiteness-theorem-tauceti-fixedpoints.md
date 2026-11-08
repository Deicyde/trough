---
declaration: theorem
origin: cited
lean: TauCeti.FixedPoints.finiteType_subalgebra
statement: formalized
proof: formalized
---

# Noether's finiteness theorem (`TauCeti.FixedPoints.finiteType_subalgebra`)

Over a Noetherian base ring `R`, the invariants of a finite
group acting on a finite-type `R`-algebra form a finite-type `R`-algebra.

```lean
TauCeti.FixedPoints.finiteType_subalgebra.{u_1, u_2, u_3} (R : Type u_1) (A : Type u_2)
  (G : Type u_3) [CommRing R] [CommRing A] [Algebra R A] [Group G] [MulSemiringAction G A]
  [SMulCommClass G R A] [IsNoetherianRing R] [Algebra.FiniteType R A] [Finite G] :
  Algebra.FiniteType R ↥(FixedPoints.subalgebra R A G)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FixedPoints.finiteType_subalgebra`](https://taucetiproject.org/docs/TauCeti/RingTheory/Invariant/FiniteType.html#TauCeti.FixedPoints.finiteType_subalgebra).

## Sources

- [Tau Ceti documentation: `TauCeti.FixedPoints.finiteType_subalgebra`](https://taucetiproject.org/docs/TauCeti/RingTheory/Invariant/FiniteType.html#TauCeti.FixedPoints.finiteType_subalgebra)
- [Source of `TauCeti.FixedPoints.finiteType_subalgebra` in TauCeti/RingTheory/Invariant/FiniteType.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Invariant/FiniteType.lean#L95)
- [Tau Ceti roadmap status: Finite reflection invariants, degrees, and Weyl exponents](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ReflectionInvariantTheory/STATUS.md)
