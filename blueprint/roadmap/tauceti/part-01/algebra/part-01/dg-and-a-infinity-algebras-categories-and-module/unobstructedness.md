---
declaration: theorem
origin: cited
lean: TauCeti.AInfinityAlgebra.IsDeformationOfOrder.exists_isFormalDeformation
statement: formalized
proof: formalized
---

# Unobstructedness

If the positive-arity Hochschild cohomology of degree two vanishes,
every deformation of order `n` extends to a formal deformation with the same coefficients up to
order `n`.

```lean
TauCeti.AInfinityAlgebra.IsDeformationOfOrder.exists_isFormalDeformation.{uR, uA} {R : Type uR}
  {A : Type uA} [CommRing R] [AddCommGroup A] [_root_.Module R A] {𝒜 : TauCeti.AInfinityAlgebra R A}
  [Subsingleton (TauCeti.AInfinityAlgebra.PositiveHochschild.Cohomology 𝒜 2)] {n : ℕ}
  {φ : ℕ → TauCeti.ReducedTensorWords R A →ₗ[R] A} (h : 𝒜.IsDeformationOfOrder n φ) :
  ∃ φ', 𝒜.IsFormalDeformation φ' ∧ ∀ i ≤ n, φ' i = φ i
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The Hochschild differential squares to zero](the-hochschild-differential-squares-to-zero.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.AInfinityAlgebra.IsDeformationOfOrder.exists_isFormalDeformation`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Algebra/Deformation.html#TauCeti.AInfinityAlgebra.IsDeformationOfOrder.exists_isFormalDeformation).

## Sources

- [Tau Ceti documentation: `TauCeti.AInfinityAlgebra.IsDeformationOfOrder.exists_isFormalDeformation`](https://taucetiproject.org/docs/TauCeti/Algebra/Homology/AInfinity/Algebra/Deformation.html#TauCeti.AInfinityAlgebra.IsDeformationOfOrder.exists_isFormalDeformation)
- [Source of `TauCeti.AInfinityAlgebra.IsDeformationOfOrder.exists_isFormalDeformation` in TauCeti/Algebra/Homology/AInfinity/Algebra/Deformation.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Algebra/Homology/AInfinity/Algebra/Deformation.lean#L398)
- [Tau Ceti roadmap status: DG and A-infinity algebras, categories, and modules](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/DGAInfinity/STATUS.md)
