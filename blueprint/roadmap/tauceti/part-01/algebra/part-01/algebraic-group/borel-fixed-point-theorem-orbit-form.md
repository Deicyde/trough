---
declaration: theorem
origin: cited
lean: TauCeti.Comodule.exists_projectiveOrbitMap_eq_identity_of_isClosed_of_isSolvable, TauCeti.Comodule.exists_fixed_mem_of_isClosed_of_isSolvable
statement: formalized
proof: formalized
---

# Borel fixed-point theorem, orbit form

Every nonempty closed invariant subset
of projective space contains a rational line whose full scheme-point orbit is a singleton.

```lean
TauCeti.Comodule.exists_projectiveOrbitMap_eq_identity_of_isClosed_of_isSolvable.{u}
  {k H M : Type u} [Field k] [IsAlgClosed k] [CommRing H] [HopfAlgebra k H] [Algebra.FiniteType k H]
  [IsReduced H] [ConnectedSpace (PrimeSpectrum H)] [Group.IsSolvable (WithConv (H →ₐ[k] k))]
  [AddCommGroup M] [_root_.Module k M] [TauCeti.Comodule k H M] [Module.Finite k M]
  {Z :
    Set
      ↥(AlgebraicGeometry.Proj (TauCeti.SymmetricAlgebra.homogeneousSubmodule k (Module.Dual k M)))}
  (hZ : IsClosed Z) (hne : Z.Nonempty)
  (hinvariant :
    ∀ (g : WithConv (H →ₐ[k] k)),
      Set.MapsTo (⇑(TauCeti.Comodule.projectivePointTranslation g).hom) Z Z) :
  ∃ m,
    ∃ (hm : Module.IsUnimodular k m),
      (TauCeti.Comodule.projectiveOrbitMap m hm) (Bialgebra.counitAlgHom k H).kernelPoint ∈ Z ∧
        ∀ (x : ↥(AlgebraicGeometry.Spec ↧H)),
          (TauCeti.Comodule.projectiveOrbitMap m hm) x =
            (TauCeti.Comodule.projectiveOrbitMap m hm) (Bialgebra.counitAlgHom k H).kernelPoint
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The global dimension of a regular local ring is its Krull dimension](../../../ring-theory/part-01/purity-of-the-branch-locus/the-global-dimension-of-a-regular-local-ring-is.md)
- [The Jacobian criterion for étaleness](../../../ring-theory/part-02/other-results/part-02/the-jacobian-criterion-for-etaleness.md)
- [The Lie--Kolchin theorem](the-lie-kolchin-theorem.md)
- [Serre's theorem (`TauCeti.IsRegularLocalRing.of_hasProjectiveDimensionLE`)](../../../ring-theory/part-01/purity-of-the-branch-locus/serres-theorem-tauceti-isregularlocalring-of-has.md)
- [TauCeti.globalDimension](../../../ring-theory/part-01/purity-of-the-branch-locus/tauceti-globaldimension.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.Comodule.exists_projectiveOrbitMap_eq_identity_of_isClosed_of_isSolvable`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Representation/ProjectiveOrbit/FixedPoint/Existence.html#TauCeti.Comodule.exists_projectiveOrbitMap_eq_identity_of_isClosed_of_isSolvable).

## Other forms

**Borel fixed-point theorem, projective form.** Formalized in Tau Ceti as [`TauCeti.Comodule.exists_fixed_mem_of_isClosed_of_isSolvable`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Representation/ProjectiveOrbit/FixedPoint/Existence.html#TauCeti.Comodule.exists_fixed_mem_of_isClosed_of_isSolvable).

```lean
TauCeti.Comodule.exists_fixed_mem_of_isClosed_of_isSolvable.{u} {k H M : Type u} [Field k]
  [IsAlgClosed k] [CommRing H] [HopfAlgebra k H] [Algebra.FiniteType k H] [IsReduced H]
  [ConnectedSpace (PrimeSpectrum H)] [Group.IsSolvable (WithConv (H →ₐ[k] k))] [AddCommGroup M]
  [_root_.Module k M] [TauCeti.Comodule k H M] [Module.Finite k M]
  {Z :
    Set
      ↥(AlgebraicGeometry.Proj (TauCeti.SymmetricAlgebra.homogeneousSubmodule k (Module.Dual k M)))}
  (hZ : IsClosed Z) (hne : Z.Nonempty)
  (hinvariant :
    ∀ (g : WithConv (H →ₐ[k] k)),
      Set.MapsTo (⇑(TauCeti.Comodule.projectivePointTranslation g).hom) Z Z) :
  ∃ x ∈ Z,
    x ∈
        closedPoints
          ↥(AlgebraicGeometry.Proj
              (TauCeti.SymmetricAlgebra.homogeneousSubmodule k (Module.Dual k M))) ∧
      ∀ (g : WithConv (H →ₐ[k] k)), (TauCeti.Comodule.projectivePointTranslation g).hom x = x
```

## Sources

- [Tau Ceti documentation: `TauCeti.Comodule.exists_projectiveOrbitMap_eq_identity_of_isClosed_of_isSolvable`](https://taucetiproject.org/docs/TauCeti/Algebra/AlgebraicGroup/Representation/ProjectiveOrbit/FixedPoint/Existence.html#TauCeti.Comodule.exists_projectiveOrbitMap_eq_identity_of_isClosed_of_isSolvable)
- [Source of `TauCeti.Comodule.exists_projectiveOrbitMap_eq_identity_of_isClosed_of_isSolvable` in TauCeti/Algebra/AlgebraicGroup/Representation/ProjectiveOrbit/FixedPoint/Existence.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/AlgebraicGroup/Representation/ProjectiveOrbit/FixedPoint/Existence.lean#L49)
