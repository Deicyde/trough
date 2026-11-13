---
declaration: section
origin: cited
lean: Stacks.EtaleCohomology.etaleCohomology_isAddTorsion_and_derivedEtaleCohomology_isAddTorsion, Stacks.EtaleCohomology.etaleCohomology_isAddTorsion, Stacks.EtaleCohomology.smallEtaleDerivedDirectImage, Stacks.EtaleCohomology.torsionSheafProperty_rightDerived_smallEtaleDirectImageAb, Stacks.EtaleCohomology.torsionCohomologyProperty_smallEtaleDerivedDirectImage
statement: formalized
proof: formalized
---

# 59.78 Torsion sheaves

Section 59.78 of the Stacks Project, [Tag 0DDB](https://stacks.math.columbia.edu/tag/0DDB). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DDC, a lemma

[Tag 0DDC](https://stacks.math.columbia.edu/tag/0DDC) in the Stacks Project.

**`Stacks.EtaleCohomology.etaleCohomology_isAddTorsion_and_derivedEtaleCohomology_isAddTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionDerivedEtaleCohomology.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionDerivedEtaleCohomology.lean#L182). The attribute's comment: “parts (1) and (2), as the conjunction of the sheaf case and the `D⁺` case”.

> **Stacks 0DDC.** Let `X` be a quasi-compact and quasi-separated scheme.
>
> 1. If `𝓕` is a torsion abelian sheaf on `X_étale`, then `H^n_étale(X, 𝓕)` is a torsion abelian
>    group for all `n`.
> 2. If `K` in `D⁺(X_étale)` has torsion cohomology sheaves, then `H^n_étale(X, K)` is a torsion
>    abelian group for all `n`.
>
> Part (1) is `etaleCohomology_isAddTorsion` and part (2) is `derivedEtaleCohomology_isAddTorsion`;
> both hold under exactly the source's hypotheses on `X`, so the tag's assertion is their
> conjunction. Here `H^n_étale(X, -)` is the right derived functor of global sections on the small
> étale site, and `H^n_étale(X, K)` the homology of its total right derived functor on `D⁺`.

```lean
theorem etaleCohomology_isAddTorsion_and_derivedEtaleCohomology_isAddTorsion (X : Scheme.{u})
    [CompactSpace X] [QuasiSeparatedSpace X] :
    (∀ (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}),
        Stacks.Torsion.torsionSheafProperty X.smallEtaleTopology F → ∀ n : ℕ,
        IsAddTorsion
          (((Sheaf.Γ X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}).rightDerived n).obj F)) ∧
      ∀ (K : DerivedCategory.Plus
          (Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})),
        Stacks.Torsion.torsionCohomologyProperty.{max (u + 1) v} X.smallEtaleTopology K.obj →
        ∀ n : ℤ,
        IsAddTorsion
          ((DerivedCategory.Plus.homologyFunctor AddCommGrpCat.{max (u + 1) v} n).obj
            ((Sheaf.Γ X.smallEtaleTopology
              AddCommGrpCat.{max (u + 1) v}).rightDerivedFunctorPlus.obj K))
```

**`Stacks.EtaleCohomology.etaleCohomology_isAddTorsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionEtaleCohomology.lean, line 337](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionEtaleCohomology.lean#L337). The attribute's comment: “part (1) only, with no extra hypothesis; étale cohomology is the right derived functor of global sections on the small étale site. Part (2) is not proved here”. References: SGA 4 IX (1.2), “(ii), (v)”.

> **Stacks 0DDC (1).** Let `X` be a quasi-compact and quasi-separated scheme. If `𝓕` is a
> torsion abelian sheaf on the small étale site of `X`, then `H^n_étale(X, 𝓕)` is a torsion abelian
> group for every `n`. Indeed `𝓕` is the colimit of its torsion subsheaves, étale cohomology of a
> quasi-compact and quasi-separated scheme commutes with filtered colimits, and the cohomology of
> the `d`-torsion subsheaf is annihilated by `d`.

```lean
theorem etaleCohomology_isAddTorsion (X : Scheme.{u})
    [CompactSpace X] [QuasiSeparatedSpace X]
    (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})
    (hF : Stacks.Torsion.torsionSheafProperty X.smallEtaleTopology F) (n : ℕ) :
    IsAddTorsion
      (((Sheaf.Γ X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}).rightDerived n).obj F)
```

## Tag 0DDD, a lemma

[Tag 0DDD](https://stacks.math.columbia.edu/tag/0DDD) in the Stacks Project.

**`Stacks.EtaleCohomology.smallEtaleDerivedDirectImage`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionHigherDirectImage.lean, line 277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionHigherDirectImage.lean#L277). The attribute's comment: “part (2), the bounded-below clause: the derived direct image of an object of `D^+(X_étale)` is an object of `D^+(Y_étale)`, this being the codomain of the right derived functor of `f_*` on bounded-below derived categories”.

> **The derived direct image on bounded-below derived categories of abelian étale sheaves**:
> `Rf_* : D^+(X_étale) ⥤ D^+(Y_étale)`, the right derived functor of `f_*` on bounded-below derived
> categories.
>
> This definition states the first clause of part (2) of [Stacks, Tag 0DDD] — that `Rf_* K` is
> again an object of `D^+(Y_étale)` — which is the codomain of this functor. The remaining clause,
> that its cohomology sheaves are torsion when those of `K` are, is
> `torsionCohomologyProperty_smallEtaleDerivedDirectImage`.

```lean
public abbrev smallEtaleDerivedDirectImage :
    DerivedCategory.Plus (Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}) ⥤
      DerivedCategory.Plus (Sheaf Y.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})
```

**`Stacks.EtaleCohomology.torsionSheafProperty_rightDerived_smallEtaleDirectImageAb`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionHigherDirectImage.lean, line 346](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionHigherDirectImage.lean#L346). The attribute's comment: “part (1): for `f` quasi-compact and quasi-separated and `F` a torsion abelian sheaf on `X_étale`, every higher direct image `R^n f_* F` is a torsion abelian sheaf on `Y_étale`”.

> **Part (1) of [Stacks, Tag 0DDD].** For a quasi-compact and quasi-separated morphism of
> schemes `f : X ⟶ Y` and a torsion abelian sheaf `F` on `X_étale`, the higher direct image
> `R^n f_* F` is a torsion abelian sheaf on `Y_étale`, for every `n`.
>
> Tag 072W for abelian sheaves identifies `R^n f_* F` with the sheafification of the cohomology
> presheaf and identifies that presheaf's values with étale cohomology over `V ×_Y X`; affine
> objects are cover dense in the small étale site of `Y`, and for `V` affine the scheme `V ×_Y X`
> is quasi-compact and quasi-separated, which is where the quasi-compactness and
> quasi-separatedness of `f` enter, through `compactSpace_smallEtaleBaseChange_obj` and
> `quasiSeparatedSpace_smallEtaleBaseChange_obj`; Tag 0DDC (1) over that object then makes
> `H^n(V ×_Y X, F)` torsion, which is where the torsion hypothesis on `F` is consumed. So the
> cohomology presheaf is locally torsion, and the sheafification of a locally torsion presheaf is a
> torsion abelian sheaf.

```lean
public theorem torsionSheafProperty_rightDerived_smallEtaleDirectImageAb
    [QuasiCompact f] [QuasiSeparated f] (n : ℕ)
    (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v})
    (hF : torsionSheafProperty X.smallEtaleTopology F) :
    torsionSheafProperty Y.smallEtaleTopology
      (((smallEtaleDirectImageAb.{max (u + 1) v} f).rightDerived n).obj F)
```

**`Stacks.EtaleCohomology.torsionCohomologyProperty_smallEtaleDerivedDirectImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionHigherDirectImage.lean, line 405](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/TorsionHigherDirectImage.lean#L405). The attribute's comment: “part (2), the torsion clause: for `f` quasi-compact and quasi-separated and `K` in `D^+(X_étale)` with torsion cohomology sheaves, every cohomology sheaf of `Rf_* K` is a torsion abelian sheaf on `Y_étale`. The bounded-below clause is the codomain of `smallEtaleDerivedDirectImage`”.

> **Part (2) of [Stacks, Tag 0DDD], the torsion clause.** For a quasi-compact and
> quasi-separated morphism of schemes `f : X ⟶ Y` and an object `K` of `D^+(X_étale)` whose
> cohomology sheaves are torsion, all cohomology sheaves of `Rf_* K` are torsion abelian sheaves on
> `Y_étale`. That `Rf_* K` is again an object of `D^+(Y_étale)` is the codomain of
> `smallEtaleDerivedDirectImage`, which states that clause of the tag.
>
> This is dévissage from part (1). The torsion abelian sheaves on `Y_étale` form a Serre
> subcategory ([Stacks, Tag 0DD7]), hence a weak Serre class; part (1) says that `R^p f_*` carries
> torsion abelian sheaves on `X_étale` into it; and
> `CategoryTheory.Functor.derivedCategoryBPlus_rightDerivedFunctorPlus_obj` propagates that from
> the second page `E_2^{p,q} = R^p f_* H^q(K)` of the spectral sequence of a Cartan--Eilenberg
> resolution to its abutment `H^{p+q}(Rf_* K)`.

```lean
public theorem torsionCohomologyProperty_smallEtaleDerivedDirectImage
    [QuasiCompact f] [QuasiSeparated f]
    (K : DerivedCategory.Plus (Sheaf X.smallEtaleTopology AddCommGrpCat.{max (u + 1) v}))
    (hK : torsionCohomologyProperty.{max (u + 1) v} X.smallEtaleTopology
      (DerivedCategory.Plus.ι.obj K)) :
    torsionCohomologyProperty.{max (u + 1) v} Y.smallEtaleTopology
      (DerivedCategory.Plus.ι.obj ((smallEtaleDerivedDirectImage.{v} f).obj K))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.78, Tag 0DDB](https://stacks.math.columbia.edu/tag/0DDB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
