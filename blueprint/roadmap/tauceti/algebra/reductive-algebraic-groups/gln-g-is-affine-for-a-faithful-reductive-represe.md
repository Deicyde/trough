---
declaration: theorem
origin: cited
lean: TauCeti.Comodule.isIso_fppfHomogeneousQuotientToCoinvariantsPoints_ker_coordinateBialgHom
statement: formalized
proof: formalized
---

# `GLₙ/G` is affine for a faithful reductive representation

Let `G` be a reductive group
over a field of characteristic zero and `ρ : G → GLₙ` a faithful representation with coordinate
morphism `ρ* : O(GLₙ) ⟶ O(G)`. Restriction to the functions on `GLₙ` invariant under right
translation by `G` identifies the fppf homogeneous quotient `GLₙ/G` with the sheaf of points of
`Spec O(GLₙ)^G`.

```lean
TauCeti.Comodule.isIso_fppfHomogeneousQuotientToCoinvariantsPoints_ker_coordinateBialgHom.{u}
  {k H M : Type u} [Field k] [CharZero k] [CommRing H] [HopfAlgebra k H] [Algebra.FiniteType k H]
  [AddCommMonoid M] [_root_.Module k M] [TauCeti.Comodule k H M] {n : ℕ}
  (b : Module.Basis (Fin n) k M) (hM : TauCeti.Comodule.IsFaithful)
  (hH : TauCeti.reductiveCommHopfAlgProperty k (TauCeti.FiniteTypeCommHopfAlgCat.of k H)) :
  CategoryTheory.IsIso
    (TauCeti.HopfIdeal.ker
        (TauCeti.Comodule.coordinateBialgHom b)).fppfHomogeneousQuotientToCoinvariantsPoints
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Matsushima's criterion, affine direction, in characteristic zero](../algebraic-group/matsushimas-criterion-affine-direction-in-charac.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Comodule.isIso_fppfHomogeneousQuotientToCoinvariantsPoints_ker_coordinateBialgHom`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/GeneralLinear.html#TauCeti.Comodule.isIso_fppfHomogeneousQuotientToCoinvariantsPoints_ker_coordinateBialgHom).

## Sources

- [Tau Ceti documentation: `TauCeti.Comodule.isIso_fppfHomogeneousQuotientToCoinvariantsPoints_ker_coordinateBialgHom`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/GeneralLinear.html#TauCeti.Comodule.isIso_fppfHomogeneousQuotientToCoinvariantsPoints_ker_coordinateBialgHom)
- [Source of `TauCeti.Comodule.isIso_fppfHomogeneousQuotientToCoinvariantsPoints_ker_coordinateBialgHom` in TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/GeneralLinear.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Algebra/AlgebraicGroup/Fppf/Quotient/Homogeneous/GeneralLinear.lean#L51)
- [Tau Ceti roadmap status: Reductive algebraic groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ReductiveGroups/STATUS.md)
