---
declaration: theorem
origin: cited
lean: TauCeti.FiniteEtaleScheme.epi_iff_surjective
statement: formalized
proof: formalized
---

# TauCeti.FiniteEtaleScheme.epi_iff_surjective

A morphism of finite étale schemes is an epimorphism if and only if its underlying morphism
of schemes is surjective.

```lean
TauCeti.FiniteEtaleScheme.epi_iff_surjective.{u} {S : AlgebraicGeometry.Scheme}
  {X Y : TauCeti.FiniteEtaleScheme S} (g : X ⟶ Y) :
  CategoryTheory.Epi g ↔ AlgebraicGeometry.Surjective (CategoryTheory.Over.Hom.left g.hom)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [TauCeti.FiniteEtaleScheme.exists_isColimit_binaryCofanMk_of_mono](tauceti-finiteetalescheme-exists-iscolimit-binar.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteEtaleScheme.epi_iff_surjective`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/Limits.html#TauCeti.FiniteEtaleScheme.epi_iff_surjective).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteEtaleScheme.epi_iff_surjective`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/Limits.html#TauCeti.FiniteEtaleScheme.epi_iff_surjective)
- [Source of `TauCeti.FiniteEtaleScheme.epi_iff_surjective` in TauCeti/AlgebraicGeometry/FiniteEtale/Limits.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/AlgebraicGeometry/FiniteEtale/Limits.lean#L264)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
