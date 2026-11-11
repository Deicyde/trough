---
declaration: def
origin: cited
lean: TauCeti.classifyingSpaceSingularCohomologyIsoGroupCohomology
statement: formalized
---

# The singular cohomology of the classifying space is group cohomology

for every group
`G`, the singular cohomology `Hⁿ(BG; M)` of Milnor's classifying space with coefficients in a
module `M` over a commutative ring `k` is Mathlib's group cohomology `Hⁿ(G, M)` of the trivial
representation `M`. It comes from the free resolution of `k` by the singular chains of
`universalGSpace G`.

```lean
TauCeti.classifyingSpaceSingularCohomologyIsoGroupCohomology.{u} (k : Type u) [CommRing k]
  (G : Type u) [Group G] (M : Type u) [AddCommGroup M] [_root_.Module k M] (n : ℕ) :
  TopCat.singularCohomology (↧k) k (↧M) (↧(TauCeti.classifyingSpace G)) n ≅
    groupCohomology (Rep.trivial k G M) n
```

## Depends on

- [The singular chains of a contractible free `G`-space are a projective resolution of the trivial representation of `G` over `k`](the-singular-chains-of-a-contractible-free-g-spa.md)

## Proof depends on

- [The fundamental group at `x` acts on every homotopy group based at `x`](../universal-covers/the-fundamental-group-at-x-acts-on-every-homotop.md)
- [Whitehead's theorem (Hatcher, Theorem 4.5)](../algebraic-topology-of-spaces-and-manifolds/whiteheads-theorem-hatcher-theorem-4-5.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.classifyingSpaceSingularCohomologyIsoGroupCohomology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/Cohomology.html#TauCeti.classifyingSpaceSingularCohomologyIsoGroupCohomology).

## Sources

- [Tau Ceti documentation: `TauCeti.classifyingSpaceSingularCohomologyIsoGroupCohomology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/Cohomology.html#TauCeti.classifyingSpaceSingularCohomologyIsoGroupCohomology)
- [Source of `TauCeti.classifyingSpaceSingularCohomologyIsoGroupCohomology` in TauCeti/AlgebraicTopology/ClassifyingSpace/Cohomology.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicTopology/ClassifyingSpace/Cohomology.lean#L84)
- [Tau Ceti roadmap status: Classifying spaces of discrete groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ClassifyingSpaces/STATUS.md)
