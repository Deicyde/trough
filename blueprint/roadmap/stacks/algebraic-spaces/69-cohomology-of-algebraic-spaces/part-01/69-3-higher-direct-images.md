---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isIso_moduleHigherPushforwardEtaleBaseChangeComparison_etaleSquare, AlgebraicGeometry.Space.moduleHigherPushforwardChartBaseChangeIso, AlgebraicGeometry.Space.isQuasicoherentOnSite_rightDerived_modulePushforward, AlgebraicGeometry.Space.isQuasicoherentOnSite_rightDerived_modulePushforward', AlgebraicGeometry.Space.cohomologyAffineChartIsoSectionsHigherDirectImage, AlgebraicGeometry.Space.cohomologyChartIsoSectionsHigherDirectImage
statement: formalized
proof: formalized
---

# 69.3 Higher direct images

Section 69.3 of the Stacks Project, [Tag 071Y](https://stacks.math.columbia.edu/tag/071Y). 3 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 071Z, an equation

[Tag 071Z](https://stacks.math.columbia.edu/tag/071Z) in the Stacks Project.

**`AlgebraicGeometry.Space.isIso_moduleHigherPushforwardEtaleBaseChangeComparison_etaleSquare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleEtaleBaseChangeHFace.lean, line 751](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleEtaleBaseChangeHFace.lean#L751). The attribute's comment: “for the CANONICAL comparison map and for an ÉTALE square: g étale, not merely flat, so this is a special case of Stacks 073K part (1) and not that tag. The existing 071Z attribute carries an isomorphism with the right endpoints that is not identified with the canonical map”.

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

**`AlgebraicGeometry.Space.moduleHigherPushforwardChartBaseChangeIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleHigherPushforwardEtaleBaseChange.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleHigherPushforwardEtaleBaseChange.lean#L187).

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

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_rightDerived_modulePushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/HigherPushforwardQuasicoherent.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/HigherPushforwardQuasicoherent.lean#L149). The attribute's comment: “the reduction to an affine base; the affine case is the hypothesis haffine”.

> **Stacks 0720.** Let `f : X ⟶ Y` be a quasi-compact and quasi-separated morphism of
> algebraic spaces over a scheme `S`, and let `F` be a quasi-coherent `𝒪_X`-module on the small
> étale site of `X`.  Then the higher direct image `R^i f_*F` is quasi-coherent for every `i`.
>
> The affine-base case of the source's proof is the hypothesis `haffine`, and the
> injective-preservation half of Stacks 03F3 for the chart base changes of `f` is the hypothesis
> `h03F3`; everything else is the source's reduction to an affine base, by Stacks 03M0,
> condition (4), and the higher-direct-image clause of Stacks 03LX, with the hypotheses of the
> affine case supplied from those of `f` by Stacks 03HF and Stacks 03KL, part (3).

```lean
theorem isQuasicoherentOnSite_rightDerived_modulePushforward {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (F : Modules.{u, u} B S hS X.1 X.2) [F.IsQuasicoherentOnSite] (i : ℕ)
    (h03F3 : ∀ V : SmallEtale B S hS Y.1,
      (chartBaseChangeModulePullback B S hS f V).PreservesInjectiveObjects)
    (haffine : AffineTargetHigherPushforwardQuasicoherent B S hS i) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    (((modulePushforward B S hS f).rightDerived i).obj F).IsQuasicoherentOnSite
```

**`AlgebraicGeometry.Space.isQuasicoherentOnSite_rightDerived_modulePushforward'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/HigherPushforwardQuasicoherentUnconditional.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/HigherPushforwardQuasicoherentUnconditional.lean#L80).

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

**`AlgebraicGeometry.Space.cohomologyAffineChartIsoSectionsHigherDirectImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/HigherDirectImageSectionsOverAffineChart.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/HigherDirectImageSectionsOverAffineChart.lean#L92). The attribute's comment: “the source's statement and both steps of its proof at the source's own data: f quasi-compact and quasi-separated, F quasi-coherent, V an affine object of Y_etale. The cohomology over V times_Y X is read as the right derived functor of the composite Gamma(V, f'_* -), as in the library's form of Stacks 0D2U”.

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

**`AlgebraicGeometry.Space.cohomologyChartIsoSectionsHigherDirectImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/HigherDirectImageSectionsOverChart.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/HigherDirectImageSectionsOverChart.lean#L215). The attribute's comment: “both steps of the source's proof, with its three citations carried as named hypotheses -- `h072Z` is Stacks 072Z via Stacks 0731(3), `hcoh` is Stacks 0720 together with Stacks 01XB read on the small etale site (Stacks 03DW), and `h03F3` is Stacks 03F3(1) for the etale morphism V times_Y X -> X; the cohomology over V times_Y X is read as the right derived functor of the composite Gamma(V, f'_* -)”.

> **Stacks 08EX.** Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S`, let `F` be an
> `𝒪_X`-module and let `V` be an étale scheme chart of `Y`.  Then the cohomology of `F` over
> `U = V ×_Y X` agrees with the module of sections over `V` of the degree-`q` higher direct image
> `R^q f_*F`, in every degree:
>
> `H^q(V ×_Y X, F) = H^0(V, R^q f_*F)`.
>
> The right hand side is the restriction of `R^q f_*F` to the chart `V`, read through its global
> sections there, and the left hand side is the `q`-th right derived functor of `Γ(V, f'_*−)` for
> `f' : U ⟶ V` the base change of `f`.  The proof is the source's: the higher-direct-image clause
> of Stacks 03LX identifies `(R^q f_*F)|_V` with `R^q f'_*(F|_U)`, and the Leray spectral sequence
> of `f'` degenerates at `E_2`, which is `AlgebraicGeometry.Space.globalSectionsRightDerivedIso`.
>
> Three hypotheses are carried, none of them part of this tag's own content: `h072Z` is
> Stacks 072Z through part (3) of Stacks 0731, `hcoh` is where the source invokes Stacks 0720 and
> Stacks 01XB — for an affine `V` and a quasi-coherent `F` along a quasi-compact and
> quasi-separated `f` it is exactly their conjunction — and `h03F3` is the injective-preservation
> half of Stacks 03F3, part (1), which is discharged for a representable `f` by Stacks 071Z.

```lean
def cohomologyChartIsoSectionsHigherDirectImage (f : X ⟶ Y)
    (F : Modules.{u, u} B S hS X.1 X.2) (V : SmallEtale B S hS Y.1) (q : ℕ)
    (h03F3 : (chartBaseChangeModulePullback B S hS f V).PreservesInjectiveObjects)
    (h072Z : AcyclicPushforwardOfInjective B S hS (chartBaseChangeProjection B S hS f V))
    (hcoh : AcyclicHigherDirectImages B S hS (chartBaseChangeProjection B S hS f V)
      ((chartBaseChangeModulePullback B S hS f V).obj F)) :
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
          ((Stacks.SheafOfModules.Tensor.ringSheaf (smallEtaleRingedSite B S hS (chartBaseChangeTarget B S hS V).1
            (chartBaseChangeTarget B S hS V).2).O))).obj
        ((etaleModulePullback B S hS (chartToSpace B S hS Y V)
            (isEtale_chartToSpace B S hS Y V)).obj
          (((modulePushforward B S hS f).rightDerived q).obj F))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 69.3, Tag 071Y](https://stacks.math.columbia.edu/tag/071Y)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
