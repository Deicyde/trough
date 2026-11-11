---
declaration: def
origin: cited
lean: TauCeti.cyclicCohomology.evenPairingK0
statement: formalized
---

# Connes' even pairing on algebraic `K₀`

The class of a finitely generated projective
module isomorphic to the image `A^ι e` of an idempotent matrix `e` is sent to the pairing
`c ↦ ⟨[e], c⟩` of `e` with cyclic cohomology classes of degree `2m`; see
`TauCeti.cyclicCohomology.evenPairingK0_of_linearEquiv_range`.

```lean
TauCeti.cyclicCohomology.evenPairingK0.{u, u_1, u_2} (R : Type u_1) {A : Type u} (M : Type u_2)
  [Field R] [CharZero R] [Ring A] [Algebra R A] [AddCommGroup M] [_root_.Module R M] (m : ℕ) :
  TauCeti.ExactK0 (TauCeti.finiteProjectiveModulesExactStructure A) →+
    ↑(TauCeti.cyclicCohomology R A M (2 * m)) →ₗ[R] M
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The dual Noether isomorphism](../../../category-theory/exact/the-dual-noether-isomorphism.md)
- [The Noether isomorphism for exact categories](../../../category-theory/exact/the-noether-isomorphism-for-exact-categories.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.cyclicCohomology.evenPairingK0`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/EvenPairing/AlgebraicK0.html#TauCeti.cyclicCohomology.evenPairingK0).

## Sources

- [Tau Ceti documentation: `TauCeti.cyclicCohomology.evenPairingK0`](https://taucetiproject.org/docs/TauCeti/RingTheory/CyclicCohomology/EvenPairing/AlgebraicK0.html#TauCeti.cyclicCohomology.evenPairingK0)
- [Source of `TauCeti.cyclicCohomology.evenPairingK0` in TauCeti/RingTheory/CyclicCohomology/EvenPairing/AlgebraicK0.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/CyclicCohomology/EvenPairing/AlgebraicK0.lean#L137)
- [Tau Ceti roadmap status: Cyclic cohomology, spectral triples and noncommutative tori](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/NoncommutativeGeometry/STATUS.md)
