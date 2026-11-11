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
- [Source of `TauCeti.FiniteEtaleScheme.epi_iff_surjective` in TauCeti/AlgebraicGeometry/FiniteEtale/Limits.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/FiniteEtale/Limits.lean#L264)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
