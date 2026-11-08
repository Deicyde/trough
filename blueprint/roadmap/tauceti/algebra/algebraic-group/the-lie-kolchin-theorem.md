---
declaration: theorem
origin: cited
lean: TauCeti.Comodule.exists_basis_coefficientMatrix_isUpperTriangular_of_isSolvable, TauCeti.Comodule.exists_basis_coefficientMatrix_isUpperTriangular_of_geometricallySolvable
statement: formalized
proof: formalized
---

# The Lie--Kolchin theorem

If the rational points of a reduced connected affine group of
finite type over an algebraically closed field form a solvable group, every finite-dimensional
representation admits a basis in which its coefficient matrix is upper triangular, with
characters on the diagonal.

```lean
TauCeti.Comodule.exists_basis_coefficientMatrix_isUpperTriangular_of_isSolvable.{u, v, w}
  {k : Type u} {H : Type v} {M : Type w} [Field k] [IsAlgClosed k] [CommRing H] [HopfAlgebra k H]
  [Algebra.FiniteType k H] [IsReduced H] [AddCommGroup M] [_root_.Module k M]
  [TauCeti.Comodule k H M] [FiniteDimensional k M] [ConnectedSpace (PrimeSpectrum H)]
  [Group.IsSolvable (WithConv (H →ₐ[k] k))] :
  ∃ n b,
    (TauCeti.Comodule.coefficientMatrix b).IsUpperTriangular ∧
      ∀ (i : Fin n), IsGroupLikeElem k (TauCeti.Comodule.coefficientMatrix b i i)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Comodule.exists_basis_coefficientMatrix_isUpperTriangular_of_isSolvable`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Solvable/LieKolchin.html#TauCeti.Comodule.exists_basis_coefficientMatrix_isUpperTriangular_of_isSolvable).

## Other forms

**The Lie--Kolchin theorem for the geometric object properties.** Formalized in Tau Ceti as [`TauCeti.Comodule.exists_basis_coefficientMatrix_isUpperTriangular_of_geometricallySolvable`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Solvable/LieKolchin.html#TauCeti.Comodule.exists_basis_coefficientMatrix_isUpperTriangular_of_geometricallySolvable).

```lean
TauCeti.Comodule.exists_basis_coefficientMatrix_isUpperTriangular_of_geometricallySolvable.{u, v, w}
  {k : Type u} {H : Type v} {M : Type w} [Field k] [IsAlgClosed k] [CommRing H] [HopfAlgebra k H]
  [Algebra.FiniteType k H] [IsReduced H] [AddCommGroup M] [_root_.Module k M]
  [TauCeti.Comodule k H M] [FiniteDimensional k M]
  (hconn : TauCeti.geometricallyConnectedCommHopfAlgProperty k ↧H)
  (hsolv : TauCeti.geometricallySolvablePointsCommHopfAlgProperty k ↧H) :
  ∃ n b,
    (TauCeti.Comodule.coefficientMatrix b).IsUpperTriangular ∧
      ∀ (i : Fin n), IsGroupLikeElem k (TauCeti.Comodule.coefficientMatrix b i i)
```

## Sources

- [Tau Ceti documentation: `TauCeti.Comodule.exists_basis_coefficientMatrix_isUpperTriangular_of_isSolvable`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Solvable/LieKolchin.html#TauCeti.Comodule.exists_basis_coefficientMatrix_isUpperTriangular_of_isSolvable)
- [Source of `TauCeti.Comodule.exists_basis_coefficientMatrix_isUpperTriangular_of_isSolvable` in TauCeti/Algebra/AlgebraicGroup/Solvable/LieKolchin.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/AlgebraicGroup/Solvable/LieKolchin.lean#L416)
