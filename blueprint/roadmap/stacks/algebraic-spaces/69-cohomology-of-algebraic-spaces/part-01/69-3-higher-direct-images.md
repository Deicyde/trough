---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isIso_moduleHigherPushforwardEtaleBaseChangeComparison_etaleSquare, AlgebraicGeometry.Space.moduleHigherPushforwardChartBaseChangeIso, AlgebraicGeometry.Space.isQuasicoherentOnSite_rightDerived_modulePushforward', AlgebraicGeometry.Space.cohomologyAffineChartIsoSectionsHigherDirectImage
statement: formalized
proof: formalized
---

# 69.3 Higher direct images

Section 69.3 of the Stacks Project, [Tag 071Y](https://stacks.math.columbia.edu/tag/071Y). 3 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 071Z, an equation

[Tag 071Z](https://stacks.math.columbia.edu/tag/071Z) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_moduleHigherPushforwardEtaleBaseChangeComparison_etaleSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleEtaleBaseChangeHFace.lean, line 782](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ModuleEtaleBaseChangeHFace.lean#L782). The attribute's comment: “for the CANONICAL comparison map and for an ÉTALE square: g étale, not merely flat, so this is a special case of Stacks 073K part (1) and not that tag. The existing 071Z attribute carries an isomorphism with the right endpoints that is not identified with the canonical map”.

> **Stacks 071Z read as a statement about the canonical maps, in the étale case.**  For a
> cartesian square of algebraic spaces whose bottom arrow `g` is étale, the canonical base-change
> comparison
>
> `(R^n f_*F)|_{Y'} ⟶ R^n f'_*(F|_{X'})`
>
> is an isomorphism in every degree `n`.
>
> This is `AlgebraicGeometry.Space.isIso_moduleHigherPushforwardEtaleBaseChangeComparison` with its
> underived hypothesis discharged by
> `AlgebraicGeometry.Space.isIso_moduleEtaleBaseChangeComparison`.  The injective-preservation
> input of the comparison map — part (1) of Stacks 03F3 for étale restriction of modules along `i`,
> which is étale by Stacks 03FU — is
> `AlgebraicGeometry.Space.preservesInjectiveObjects_etaleModulePullback` and is used, not assumed.
> So nothing is assumed here beyond the cartesian square and the étaleness of `g`.
>
> **This is the étale case and not Stacks 073K, part (1)**, for the same reason as the underived
> statement: `hg` is `AlgebraicGeometry.Space.IsEtale`, and étale is strictly stronger than the
> flatness of `g` that Stacks 073K assumes.

```lean
theorem isIso_moduleHigherPushforwardEtaleBaseChangeComparison_etaleSquare
    (sq : IsPullback i f' f g) (hg : IsEtale B S hS g.hom) (n : ℕ) :
    IsIso (moduleHigherPushforwardEtaleBaseChangeComparison B S hS i f' f g sq hg
      (preservesInjectiveObjects_etaleModulePullback B S hS i
        (isEtale_of_isPullback B S hS f' i g f sq.flip hg)) n)
```

**`AlgebraicGeometry.Space.moduleHigherPushforwardChartBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleHigherPushforwardEtaleBaseChange.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ModuleHigherPushforwardEtaleBaseChange.lean#L187).

> For a representable morphism `f : X ⟶ Y` of algebraic
> spaces and an étale scheme chart `V` of `Y`, the higher direct images of `𝒪_X`-modules commute
> with restriction to the chart:
>
> `R^n f'_*(F|_U) = (R^n f_*F)|_V`,
>
> naturally in the `𝒪_X`-module `F`, where `U = V ×_Y X` is the pullback chart of `X` and
> `f' : U ⟶ V` is the base change of `f`. The morphism `f` is not assumed quasi-compact or
> quasi-separated, `V ⟶ Y` is not assumed surjective and `F` is not assumed quasi-coherent.

```lean
noncomputable def moduleHigherPushforwardChartBaseChangeIso (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f.hom) (V : SmallEtale B S hS Y.1) (n : ℕ) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    have := hasInjectiveResolutions_modules B S hS
      (chartSpace B S hS X ((smallBaseChange B S hS f hf).obj V)).1
      (chartSpace B S hS X ((smallBaseChange B S hS f hf).obj V)).2
    etaleModulePullback B S hS
          (chartToSpace B S hS X ((smallBaseChange B S hS f hf).obj V))
          (isEtale_chartToSpace B S hS X ((smallBaseChange B S hS f hf).obj V)) ⋙
        (modulePushforward B S hS (smallBaseChangeChartMap B S hS f hf V)).rightDerived n ≅
      (modulePushforward B S hS f).rightDerived n ⋙
        etaleModulePullback B S hS (chartToSpace B S hS Y V)
          (isEtale_chartToSpace B S hS Y V)
```

## Tag 0720, a lemma

[Tag 0720](https://stacks.math.columbia.edu/tag/0720) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_rightDerived_modulePushforward'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/HigherPushforwardQuasicoherentUnconditional.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/HigherPushforwardQuasicoherentUnconditional.lean#L77).

> **Stacks 0720.** Let `f : X ⟶ Y` be a quasi-compact and quasi-separated morphism of
> algebraic spaces over a scheme `S`, and let `F` be a quasi-coherent `𝒪_X`-module on the small
> étale site of `X`. Then the higher direct image `R^i f_*F` is quasi-coherent for every `i`.

```lean
theorem isQuasicoherentOnSite_rightDerived_modulePushforward' {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite] (i : ℕ) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    (((modulePushforward B S hS f).rightDerived i).obj F).IsQuasicoherentOnSite
```

## Tag 08EX, a lemma

[Tag 08EX](https://stacks.math.columbia.edu/tag/08EX) in the Stacks Project.

**`AlgebraicGeometry.Space.cohomologyAffineChartIsoSectionsHigherDirectImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/HigherDirectImageSectionsOverAffineChart.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/HigherDirectImageSectionsOverAffineChart.lean#L96). The attribute's comment: “the complete statement at the source's own data, with no extra hypothesis: f quasi-compact and quasi-separated, F quasi-coherent, V an affine object of Y\_etale. The three inputs of the source's proof (03F3(1) for the etale inclusion, 072Z via 0731(3), and 0720 with 01XB on the small etale site) are theorems of the library, applied here. The cohomology over V times\_Y X is read as the right derived functor of the composite Gamma(V, f'\_* -), as in the library's form of Stacks 0D2U. The degree q ranges over the natural numbers, which loses nothing: in the right-derived-functor convention both sides vanish in negative degrees. This is the sole registration of 08EX”.

> **Stacks 08EX.** Let `f : X ⟶ Y` be a quasi-compact and quasi-separated morphism of
> algebraic spaces over `S`, let `F` be a quasi-coherent `𝒪_X`-module and let `V` be an affine
> étale chart of `Y`.  Then the cohomology of `F` over `U = V ×_Y X` agrees with the module of
> sections over `V` of the degree-`q` higher direct image `R^q f_*F`, in every degree:
>
> `H^q(V ×_Y X, F) = H^0(V, R^q f_*F)`.

```lean
def cohomologyAffineChartIsoSectionsHigherDirectImage (f : X ⟶ Y)
    (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : F.IsQuasicoherentOnSite)
    (V : SmallEtale B S hS Y.1) (hV : IsAffineChart B S hS Y.1 V) (q : ℕ) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    have := hasInjectiveResolutions_modules B S hS (chartBaseChangeSpace B S hS f V).1
      (chartBaseChangeSpace B S hS f V).2
    have := enoughInjectives_modules B S hS (chartBaseChangeTarget B S hS V).1
      (chartBaseChangeTarget B S hS V).2
    ((modulePushforward B S hS (chartBaseChangeProjection B S hS f V) ⋙
            globalSectionsFunctor.{u + 1, u, u, u}
              ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS
                (chartBaseChangeTarget B S hS V).1
                (chartBaseChangeTarget B S hS V).2).O))).rightDerived q).obj
        ((chartBaseChangeModulePullback B S hS f V).obj F) ≅
      (globalSectionsFunctor.{u + 1, u, u, u}
          ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS
            (chartBaseChangeTarget B S hS V).1
            (chartBaseChangeTarget B S hS V).2).O))).obj
        ((etaleModulePullback B S hS (chartToSpace B S hS Y V)
            (isEtale_chartToSpace B S hS Y V)).obj
          (((modulePushforward B S hS f).rightDerived q).obj F))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 69.3, Tag 071Y](https://stacks.math.columbia.edu/tag/071Y)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
