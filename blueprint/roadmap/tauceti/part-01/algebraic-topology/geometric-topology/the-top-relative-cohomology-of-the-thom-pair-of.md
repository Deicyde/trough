---
declaration: def
origin: cited
lean: TauCeti.prodThomPairSingularCohomologyEquiv
statement: formalized
---

# The top relative cohomology of the Thom pair of a product bundle

for `F` of dimension
`r`, `Hʳ(B × F, B × (F ∖ {0}); R, M) ≃ₗ[k] (H₀(B; R) ⟶ M)`. A class goes to its evaluation on
`Hᵣ(B × F, B × (F ∖ {0}); R)`, read on `H₀(B; R)` through
`TauCeti.prodThomPairSingularHomologyIso`.

```lean
TauCeti.prodThomPairSingularCohomologyEquiv.{w, u_1} {k : Type u_1} [CommRing k] (R M : ModuleCat k)
  [Module.Projective k ↑R] (B : Type w) [TopologicalSpace B] (F : Type w) [NormedAddCommGroup F]
  [NormedSpace ℝ F] [FiniteDimensional ℝ F] :
  ↑((TauCeti.prodThomPair B F).singularCohomology R k M (Module.finrank ℝ F)) ≃ₗ[k]
    ((AlgebraicTopology.singularHomologyFunctor (ModuleCat k) 0).obj R).obj ↧B ⟶ M
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [The relative universal coefficient theorem below the first non-projective homology, over any commutative ring `k`](../cohomology/the-relative-universal-coefficient-theorem-below.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.prodThomPairSingularCohomologyEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/ProdThomPair.html#TauCeti.prodThomPairSingularCohomologyEquiv).

## Sources

- [Tau Ceti documentation: `TauCeti.prodThomPairSingularCohomologyEquiv`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/Cohomology/ProdThomPair.html#TauCeti.prodThomPairSingularCohomologyEquiv)
- [Source of `TauCeti.prodThomPairSingularCohomologyEquiv` in TauCeti/AlgebraicTopology/Cohomology/ProdThomPair.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/Cohomology/ProdThomPair.lean#L89)
- [Tau Ceti roadmap status: Geometric topology](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/GeometricTopology/STATUS.md)
