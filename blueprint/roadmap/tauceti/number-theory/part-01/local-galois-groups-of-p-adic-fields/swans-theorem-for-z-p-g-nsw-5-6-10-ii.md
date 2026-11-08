---
declaration: theorem
origin: cited
lean: TauCeti.nonempty_linearEquiv_of_projective_of_tensorRat
statement: formalized
proof: formalized
---

# Swan's theorem for `ℤ_p[G]` (NSW (5.6.10)(ii))

Two finitely generated projective
`ℤ_p[G]`-modules with isomorphic rationalizations are isomorphic.

```lean
TauCeti.nonempty_linearEquiv_of_projective_of_tensorRat.{u, v, w} (p : ℕ) [Fact (Nat.Prime p)]
  {G : Type u} [Group G] [Finite G] (M : Type v) (N : Type w) [AddCommGroup M]
  [_root_.Module ℤ_[p] M] [_root_.Module (MonoidAlgebra ℤ_[p] G) M]
  [IsScalarTower ℤ_[p] (MonoidAlgebra ℤ_[p] G) M] [Module.Finite (MonoidAlgebra ℤ_[p] G) M]
  [Module.Projective (MonoidAlgebra ℤ_[p] G) M] [AddCommGroup N] [_root_.Module ℤ_[p] N]
  [_root_.Module (MonoidAlgebra ℤ_[p] G) N] [IsScalarTower ℤ_[p] (MonoidAlgebra ℤ_[p] G) N]
  [Module.Finite (MonoidAlgebra ℤ_[p] G) N] [Module.Projective (MonoidAlgebra ℤ_[p] G) N]
  (h :
    Nonempty (TensorProduct ℤ_[p] M ℚ_[p] ≃ₗ[MonoidAlgebra ℤ_[p] G] TensorProduct ℤ_[p] N ℚ_[p])) :
  Nonempty (M ≃ₗ[MonoidAlgebra ℤ_[p] G] N)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Schur's lemma, vanishing form](../../../quantum-groups/quantum-groups-compact-reconstruction-and-generi/schurs-lemma-vanishing-form.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.nonempty_linearEquiv_of_projective_of_tensorRat`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/GroupAlgebra/Swan.html#TauCeti.nonempty_linearEquiv_of_projective_of_tensorRat).

## Sources

- [Tau Ceti documentation: `TauCeti.nonempty_linearEquiv_of_projective_of_tensorRat`](https://taucetiproject.org/docs/TauCeti/NumberTheory/Padics/GroupAlgebra/Swan.html#TauCeti.nonempty_linearEquiv_of_projective_of_tensorRat)
- [Source of `TauCeti.nonempty_linearEquiv_of_projective_of_tensorRat` in TauCeti/NumberTheory/Padics/GroupAlgebra/Swan.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/NumberTheory/Padics/GroupAlgebra/Swan.lean#L56)
- [Tau Ceti roadmap status: Local Galois groups of p-adic fields](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/LocalGaloisGroups/STATUS.md)
