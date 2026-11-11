---
declaration: theorem
origin: cited
lean: TauCeti.FiniteEtaleScheme.exists_isColimit_binaryCofanMk_of_mono
statement: formalized
proof: formalized
---

# TauCeti.FiniteEtaleScheme.exists_isColimit_binaryCofanMk_of_mono

Every monomorphism `i : X ⟶ Y` of finite étale schemes over `S` is the inclusion of a direct
summand: there is a finite étale `Z` over `S` with a morphism `u : Z ⟶ Y` exhibiting `Y` as the
coproduct of `X` and `Z`. Here `Z` is the open complement of the image of `i`.

```lean
TauCeti.FiniteEtaleScheme.exists_isColimit_binaryCofanMk_of_mono.{u} {S : AlgebraicGeometry.Scheme}
  {X Y : TauCeti.FiniteEtaleScheme S} (i : X ⟶ Y) [CategoryTheory.Mono i] :
  ∃ Z u, Nonempty (CategoryTheory.Limits.IsColimit (CategoryTheory.Limits.BinaryCofan.mk i u))
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.FiniteEtaleScheme.exists_isColimit_binaryCofanMk_of_mono`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/Limits.html#TauCeti.FiniteEtaleScheme.exists_isColimit_binaryCofanMk_of_mono).

## Sources

- [Tau Ceti documentation: `TauCeti.FiniteEtaleScheme.exists_isColimit_binaryCofanMk_of_mono`](https://taucetiproject.org/docs/TauCeti/AlgebraicGeometry/FiniteEtale/Limits.html#TauCeti.FiniteEtaleScheme.exists_isColimit_binaryCofanMk_of_mono)
- [Source of `TauCeti.FiniteEtaleScheme.exists_isColimit_binaryCofanMk_of_mono` in TauCeti/AlgebraicGeometry/FiniteEtale/Limits.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/AlgebraicGeometry/FiniteEtale/Limits.lean#L200)
- [Tau Ceti roadmap status: Étale cohomology foundations](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EtaleCohomologyFoundations/STATUS.md)
