---
declaration: def
origin: cited
lean: TauCeti.classifyingSpaceSingularHomologyIsoGroupHomology
statement: formalized
---

# The singular homology of the classifying space is group homology

for every group `G`,
the singular homology `Hₙ(BG; k)` of Milnor's classifying space with coefficients in a
commutative ring `k` is Mathlib's group homology `Hₙ(G, k)` of the trivial representation. It
comes from the free resolution of `k` by the singular chains of `universalGSpace G`.

```lean
TauCeti.classifyingSpaceSingularHomologyIsoGroupHomology.{u} (k : Type u) [CommRing k] (G : Type u)
  [Group G] (n : ℕ) :
  HomologicalComplex.homology ((TauCeti.singularChains k).obj ↧(TauCeti.classifyingSpace G)) n ≅
    groupHomology (Rep.trivial k G k) n
```

## Depends on

- [The singular chains of a contractible free `G`-space are a projective resolution](the-singular-chains-of-a-contractible-free-g-spa.md)

## Proof depends on

- [The fundamental group at `x` acts on every homotopy group based at `x`](../../part-07/universal-covers/the-fundamental-group-at-x-acts-on-every-homotop.md)
- [Whitehead's theorem](../algebraic-topology-of-spaces-and-manifolds/whiteheads-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.classifyingSpaceSingularHomologyIsoGroupHomology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/Homology.html#TauCeti.classifyingSpaceSingularHomologyIsoGroupHomology).

## Sources

- [Tau Ceti documentation: `TauCeti.classifyingSpaceSingularHomologyIsoGroupHomology`](https://taucetiproject.org/docs/TauCeti/AlgebraicTopology/ClassifyingSpace/Homology.html#TauCeti.classifyingSpaceSingularHomologyIsoGroupHomology)
- [Source of `TauCeti.classifyingSpaceSingularHomologyIsoGroupHomology` in TauCeti/AlgebraicTopology/ClassifyingSpace/Homology.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicTopology/ClassifyingSpace/Homology.lean#L65)
- [Tau Ceti roadmap status: Classifying spaces of discrete groups](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/ClassifyingSpaces/STATUS.md)
