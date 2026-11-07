---
declaration: def
origin: cited
lean: TauCeti.isotypicTensorEquivOfBijective
statement: formalized
---

# Every module over `A ≅ End_k S` is `S` tensored with its multiplicity space

Evaluation
`s ⊗ T ↦ T s` is an isomorphism of `A`-modules `S ⊗[k] (S →ₗ[A] M) ≃ₗ[A] M`, with `A` acting on
the left factor.

```lean
TauCeti.isotypicTensorEquivOfBijective.{u_1, u_2, u_3, u_4} {k : Type u_1} {A : Type u_2}
  {S : Type u_3} {M : Type u_4} [CommSemiring k] [Semiring A] [Algebra k A] [AddCommMonoid S]
  [_root_.Module k S] [_root_.Module A S] [IsScalarTower k A S] [AddCommMonoid M]
  [_root_.Module k M] [_root_.Module A M] [IsScalarTower k A M]
  (h : Function.Bijective ⇑(Algebra.lsmul k k S)) [Module.Finite k S] [Module.Projective k S] :
  TensorProduct k S (S →ₗ[A] M) ≃ₗ[A] M
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isotypicTensorEquivOfBijective`](https://taucetiproject.org/docs/TauCeti/RingTheory/Morita/ModuleEnd.html#TauCeti.isotypicTensorEquivOfBijective).

## Sources

- [Tau Ceti documentation: `TauCeti.isotypicTensorEquivOfBijective`](https://taucetiproject.org/docs/TauCeti/RingTheory/Morita/ModuleEnd.html#TauCeti.isotypicTensorEquivOfBijective)
- [Source of `TauCeti.isotypicTensorEquivOfBijective` in TauCeti/RingTheory/Morita/ModuleEnd.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Morita/ModuleEnd.lean#L190)
- [Tau Ceti roadmap status: Clifford bundles, spin structures, and Dirac geometry](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/SpinGeometry/STATUS.md)
