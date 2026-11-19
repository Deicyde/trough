---
declaration: def
origin: cited
lean: TauCeti.classifyingSpaceCohomologyIsoGroupCohomology
statement: formalized
---

# The cohomology of the classifying space with local coefficients in a representation is group cohomology

for every group `G` and every representation `A` of `G` over a commutative ring `k`,
the direct cohomology `Hⁿ(BG; A)` of Milnor's classifying space with coefficients in the local
system associated to `A` is Mathlib's group cohomology `Hⁿ(G, A)` of `A` itself. It comes from the
free resolution of `k` by the singular chains of `universalGSpace G`.

```lean
TauCeti.classifyingSpaceCohomologyIsoGroupCohomology.{u} (k : Type u) [CommRing k] {G : Type u}
  [Group G] (A : Rep.{u, u, u} k G) (n : ℕ) :
  (TauCeti.classifyingSpaceLocalSystem k A).cohomology n ≅ groupCohomology A n
```

## Depends on

- [The local-coefficient cohomology of the base of a contractible free cover is group cohomology](the-local-coefficient-cohomology-of-the-base-of.md)
- [TauCeti.classifyingSpaceLocalSystem](tauceti-classifyingspacelocalsystem.md)

## Proof depends on

- [The fundamental group at `x` acts on every homotopy group based at `x`](../universal-covers/the-fundamental-group-at-x-acts-on-every-homotop.md)
- [Whitehead's theorem (Hatcher, Theorem 4.5)](../algebraic-topology-of-spaces-and-manifolds/whiteheads-theorem-hatcher-theorem-4-5.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.classifyingSpaceCohomologyIsoGroupCohomology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/LocalCoefficients.html#TauCeti.classifyingSpaceCohomologyIsoGroupCohomology).

## Sources

- [Tau Ceti documentation: `TauCeti.classifyingSpaceCohomologyIsoGroupCohomology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/LocalCoefficients.html#TauCeti.classifyingSpaceCohomologyIsoGroupCohomology)
- [Source of `TauCeti.classifyingSpaceCohomologyIsoGroupCohomology` in TauCeti/AlgebraicTopology/ClassifyingSpace/LocalCoefficients.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/AlgebraicTopology/ClassifyingSpace/LocalCoefficients.lean#L231)
- [Tau Ceti roadmap status: Classifying spaces of discrete groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/ClassifyingSpaces/STATUS.md)
