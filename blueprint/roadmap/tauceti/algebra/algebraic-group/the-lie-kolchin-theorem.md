---
declaration: theorem
origin: cited
lean: TauCeti.Comodule.exists_basis_coefficientMatrix_isUpperTriangular_of_isSolvable, TauCeti.GeneralLinear.exists_map_inv_mul_mul_map_mem_upperTriangularGroup, TauCeti.Symplectic.IsotropicFlag.exists_map_inv_mul_mul_map_mem_matrixSubgroup, TauCeti.Comodule.exists_basis_coefficientMatrix_isUpperTriangular_of_geometricallySolvable, TauCeti.Comodule.exists_basis_coefficientMatrix_isUpperTriangular_of_forall_isUnipotentPoint_derived, TauCeti.Comodule.hasNonzeroWeightVector_of_geometricallySolvable, TauCeti.Comodule.hasNonzeroWeightVector_of_isSolvable
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

## Proof depends on

- [Kolchin's common fixed vector theorem](../../linear-algebra/other-results/kolchins-common-fixed-vector-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Comodule.exists_basis_coefficientMatrix_isUpperTriangular_of_isSolvable`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Solvable/LieKolchin.html#TauCeti.Comodule.exists_basis_coefficientMatrix_isUpperTriangular_of_isSolvable).

## Other forms

**Lie--Kolchin for `GLₙ`-valued points.** Formalized in Tau Ceti as [`TauCeti.GeneralLinear.exists_map_inv_mul_mul_map_mem_upperTriangularGroup`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/GeneralLinear/UpperTriangular/Borel.html#TauCeti.GeneralLinear.exists_map_inv_mul_mul_map_mem_upperTriangularGroup).

```lean
TauCeti.GeneralLinear.exists_map_inv_mul_mul_map_mem_upperTriangularGroup.{u, v} {k : Type u}
  [Field k] {n : ℕ} [IsAlgClosed k] {Q : Type v} [CommRing Q] [HopfAlgebra k Q]
  [Algebra.FiniteType k Q] [IsReduced Q]
  (hconn : TauCeti.geometricallyConnectedCommHopfAlgProperty k ↧Q)
  (hsolv : TauCeti.geometricallySolvablePointsCommHopfAlgProperty k ↧Q)
  (π : ↑(TauCeti.GeneralLinear.coordinateHopfAlgebra k n) →ₐc[k] Q) :
  ∃ P,
    (Matrix.GeneralLinearGroup.map (algebraMap k Q)) P⁻¹ *
          (TauCeti.GeneralLinear.pointsMulEquiv n) (WithConv.toConv ↑π) *
        (Matrix.GeneralLinearGroup.map (algebraMap k Q)) P ∈
      TauCeti.upperTriangularGroup (Fin n) Q
```

**Lie--Kolchin for `Sp₂ₘ`-valued points.** Formalized in Tau Ceti as [`TauCeti.Symplectic.IsotropicFlag.exists_map_inv_mul_mul_map_mem_matrixSubgroup`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Symplectic/IsotropicFlag/Borel.html#TauCeti.Symplectic.IsotropicFlag.exists_map_inv_mul_mul_map_mem_matrixSubgroup).

```lean
TauCeti.Symplectic.IsotropicFlag.exists_map_inv_mul_mul_map_mem_matrixSubgroup.{u, v} {k : Type u}
  [Field k] {m : ℕ} {Q : Type v} [CommRing Q] [HopfAlgebra k Q] [IsAlgClosed k]
  [Algebra.FiniteType k Q] [IsReduced Q]
  (hconn : TauCeti.geometricallyConnectedCommHopfAlgProperty k ↧Q)
  (hsolv : TauCeti.geometricallySolvablePointsCommHopfAlgProperty k ↧Q)
  (π : ↑(TauCeti.Symplectic.coordinateHopfAlgebra k m) →ₐc[k] Q) :
  ∃ P,
    (TauCeti.GLSymplecticFin.map m k (algebraMap k Q)) P⁻¹ *
          (TauCeti.Symplectic.pointsMulEquiv k m) (WithConv.toConv ↑π) *
        (TauCeti.GLSymplecticFin.map m k (algebraMap k Q)) P ∈
      TauCeti.GLSymplecticFin.IsotropicFlag.matrixSubgroup m
```

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

**Lie--Kolchin under unipotence of the derived subgroup.** Formalized in Tau Ceti as [`TauCeti.Comodule.exists_basis_coefficientMatrix_isUpperTriangular_of_forall_isUnipotentPoint_derived`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Solvable/LieKolchin.html#TauCeti.Comodule.exists_basis_coefficientMatrix_isUpperTriangular_of_forall_isUnipotentPoint_derived).

```lean
TauCeti.Comodule.exists_basis_coefficientMatrix_isUpperTriangular_of_forall_isUnipotentPoint_derived.{u,
    v, w}
  {k : Type u} {H : Type v} {M : Type w} [Field k] [IsAlgClosed k] [CommRing H] [HopfAlgebra k H]
  [Algebra.FiniteType k H] [IsReduced H] [AddCommGroup M] [_root_.Module k M]
  [TauCeti.Comodule k H M] [FiniteDimensional k M]
  (hderived :
    ∀ (g : WithConv (↑((↧H).quotient (TauCeti.CommHopfAlgCat.derivedDefiningIdeal H)) →ₐ[k] k)),
      TauCeti.HopfAlgebra.IsUnipotentPoint g) :
  ∃ n b,
    (TauCeti.Comodule.coefficientMatrix b).IsUpperTriangular ∧
      ∀ (i : Fin n), IsGroupLikeElem k (TauCeti.Comodule.coefficientMatrix b i i)
```

**Lie--Kolchin, geometric weight-vector form.** Formalized in Tau Ceti as [`TauCeti.Comodule.hasNonzeroWeightVector_of_geometricallySolvable`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Solvable/LieKolchin.html#TauCeti.Comodule.hasNonzeroWeightVector_of_geometricallySolvable).

```lean
TauCeti.Comodule.hasNonzeroWeightVector_of_geometricallySolvable.{u, v, w} {k : Type u} {H : Type v}
  {M : Type w} [Field k] [IsAlgClosed k] [CommRing H] [HopfAlgebra k H] [Algebra.FiniteType k H]
  [IsReduced H] [AddCommGroup M] [_root_.Module k M] [TauCeti.Comodule k H M]
  [FiniteDimensional k M] [Nontrivial M]
  (hconn : TauCeti.geometricallyConnectedCommHopfAlgProperty k ↧H)
  (hsolv : TauCeti.geometricallySolvablePointsCommHopfAlgProperty k ↧H) :
  TauCeti.Comodule.HasNonzeroWeightVector k H M
```

**Lie--Kolchin, weight-vector form.** Formalized in Tau Ceti as [`TauCeti.Comodule.hasNonzeroWeightVector_of_isSolvable`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Solvable/LieKolchin.html#TauCeti.Comodule.hasNonzeroWeightVector_of_isSolvable).

```lean
TauCeti.Comodule.hasNonzeroWeightVector_of_isSolvable.{u, v, w} {k : Type u} {H : Type v}
  {M : Type w} [Field k] [IsAlgClosed k] [CommRing H] [HopfAlgebra k H] [Algebra.FiniteType k H]
  [IsReduced H] [AddCommGroup M] [_root_.Module k M] [TauCeti.Comodule k H M]
  [FiniteDimensional k M] [Nontrivial M] [ConnectedSpace (PrimeSpectrum H)]
  [Group.IsSolvable (WithConv (H →ₐ[k] k))] : TauCeti.Comodule.HasNonzeroWeightVector k H M
```

## Sources

- [Tau Ceti documentation: `TauCeti.Comodule.exists_basis_coefficientMatrix_isUpperTriangular_of_isSolvable`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Solvable/LieKolchin.html#TauCeti.Comodule.exists_basis_coefficientMatrix_isUpperTriangular_of_isSolvable)
- [Source of `TauCeti.Comodule.exists_basis_coefficientMatrix_isUpperTriangular_of_isSolvable` in TauCeti/Algebra/AlgebraicGroup/Solvable/LieKolchin.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/AlgebraicGroup/Solvable/LieKolchin.lean#L416)
