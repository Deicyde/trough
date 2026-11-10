---
declaration: section
origin: cited
lean: CategoryTheory.SimplicialSemiRepresentable.augmentation, CategoryTheory.SimplicialSemiRepresentable.augmentation_functor, CategoryTheory.SimplicialSemiRepresentable.componentPushforwardIso, CategoryTheory.SimplicialSemiRepresentable.componentInverseImageIso, CategoryTheory.SimplicialSemiRepresentable.totalPushforward_eq, CategoryTheory.SimplicialSemiRepresentable.totalInverseImageIso, CategoryTheory.SimplicialSemiRepresentable.augmentationSheafLowerShriekAdjunction, CategoryTheory.SimplicialSemiRepresentable.augmentationAbelianLowerShriekAdjunction
statement: formalized
proof: formalized
---

# 85.16 The site associate to a simplicial semi-representable object

Section 85.16 of the Stacks Project, [Tag 0D8A](https://stacks.math.columbia.edu/tag/0D8A). 5 tags here are carried by 45 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0D8B, a lemma

[Tag 0D8B](https://stacks.math.columbia.edu/tag/0D8B) in the Stacks Project.

**`CategoryTheory.SimplicialSemiRepresentable.augmentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/SimplicialSemiRepresentableSite.lean, line 588](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/SimplicialSemiRepresentableSite.lean#L588). The attribute's comment: “j_0 defines an augmentation a_0 : Sh(C/K_0) to Sh(C), case (B) of 0D6Z”.

> **Stacks 0D8B.** The localization functor `j_0 : C/K_0 ⥤ C` defines an augmentation of the
> simplicial site `n ↦ C/K_n` towards `(C, J)`, as in case (B) of Stacks 0D6Z: it is cocontinuous,
> and its composite with the functor of a vertex of simplicial degree `n` is the localization
> functor `j_n`, which does not mention the vertex.

```lean
def augmentation : (simplicialSite J K).Augmentation (Cat.of C) J
```

**`CategoryTheory.SimplicialSemiRepresentable.augmentation_functor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/SimplicialSemiRepresentableSite.lean, line 603](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/SimplicialSemiRepresentableSite.lean#L603). The attribute's comment: “the functor underlying that augmentation is j_0”.

> **Stacks 0D8B.** The functor underlying that augmentation is the degree-zero localization
> functor `j_0`. Together with `CategoryTheory.SimplicialSemiRepresentable.augmentation` this is
> the assertion that `j_0` defines the augmentation.

```lean
theorem augmentation_functor :
    (augmentation J K).functor = sliceForget K (op (SimplexCategory.mk 0))
```

**`CategoryTheory.SimplicialSemiRepresentable.componentPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/SimplicialSemiRepresentableSite.lean, line 702](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/SimplicialSemiRepresentableSite.lean#L702). The attribute's comment: “a_n is the morphism of topoi of j_n: direct images”.

> **Stacks 0D8B.** The morphism of topoi `a_n : Sh(C/K_n) ⟶ Sh(C)` which Stacks 0D70 attaches
> to the augmentation `j_0` is the morphism of topoi of the localization functor `j_n`: their
> direct images agree canonically.
>
> This one is an isomorphism and not an equality. Stacks 0D70 attaches to the augmentation the
> composite of the degree-zero morphism of topoi with the transition morphism of a vertex, whose
> direct image is a composite of two direct images; the direct image of `j_n` is a single one, for
> the composite site functor `C/K_n ⥤ C/K_0 ⥤ C`, which equals `j_n`. Direct images along
> cocontinuous functors compose only up to the canonical comparison, which is what this is.

```lean
noncomputable def componentPushforwardIso (n : SimplexCategory) :
    (SimplicialSiteSituation.Augmentation.componentAugmentation (situation J K) (Cat.of C) J
        (situationAugmentation J K) n).pushforward ≅
      (localizationMorphism J K n).pushforward
```

**`CategoryTheory.SimplicialSemiRepresentable.componentInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/SimplicialSemiRepresentableSite.lean, line 733](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/SimplicialSemiRepresentableSite.lean#L733). The attribute's comment: “a_n is the morphism of topoi of j_n: inverse images”.

> **Stacks 0D8B.** The same identification in inverse images, obtained from uniqueness of left
> adjoints.

```lean
noncomputable def componentInverseImageIso (n : SimplexCategory) :
    (SimplicialSiteSituation.Augmentation.componentAugmentation (situation J K) (Cat.of C) J
        (situationAugmentation J K) n).inverseImage ≅
      (localizationMorphism J K n).inverseImage
```

**`CategoryTheory.SimplicialSemiRepresentable.totalPushforward_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/SimplicialSemiRepresentableSite.lean, line 757](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/SimplicialSemiRepresentableSite.lean#L757). The attribute's comment: “a is the morphism of topoi of j_total: the direct images are equal”.

> **Stacks 0D8B.** The morphism of topoi `a : Sh((C/K)_total) ⟶ Sh(C)` which Stacks 0D70
> attaches to the augmentation `j_0` is the morphism of topoi of the localization functor
> `j_total`: their direct images are *equal*, not merely isomorphic, because the cocontinuous
> functor which Stacks 0D70 attaches to the augmentation is `j_total` on the nose.

```lean
theorem totalPushforward_eq :
    (CocontinuousSimplicialSite.Augmentation.totalMorphismOfTopoi
        (augmentation J K)).pushforward = (totalLocalizationMorphism J K).pushforward
```

**`CategoryTheory.SimplicialSemiRepresentable.totalInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/SimplicialSemiRepresentableSite.lean, line 782](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/SimplicialSemiRepresentableSite.lean#L782). The attribute's comment: “a is the morphism of topoi of j_total: inverse images”.

> **Stacks 0D8B.** The same identification in inverse images, obtained from uniqueness of left
> adjoints.

```lean
noncomputable def totalInverseImageIso :
    (CocontinuousSimplicialSite.Augmentation.totalMorphismOfTopoi
        (augmentation J K)).inverseImage ≅ (totalLocalizationMorphism J K).inverseImage
```

## Tag 09WM, a lemma

[Tag 09WM](https://stacks.math.columbia.edu/tag/09WM) in the Stacks Project.

**`CategoryTheory.SimplicialSemiRepresentable.augmentationSheafLowerShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/SimplicialSemiRepresentableLowerShriek.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/SimplicialSemiRepresentableLowerShriek.lean#L116). The attribute's comment: “part (1): the left adjoint on sheaves of sets”.

> **Stacks 09WM, part (1).** The functor `a^{Sh}_! : Sh((C/K)_total) ⥤ Sh(C)` is left adjoint
> to the inverse image `a^{-1} : Sh(C) ⥤ Sh((C/K)_total)` of the augmentation.
>
> The inverse image of the augmentation is restriction along `j_total`, because `j_total` is
> cocontinuous as well as continuous, and restriction along a continuous functor has a left
> adjoint.

```lean
def augmentationSheafLowerShriekAdjunction :
    augmentationSheafLowerShriek J K ⊣
      (CocontinuousSimplicialSite.Augmentation.totalMorphismOfTopoi
        (augmentation J K)).inverseImage
```

**`CategoryTheory.SimplicialSemiRepresentable.augmentationAbelianLowerShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/SimplicialSemiRepresentableLowerShriek.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/SimplicialSemiRepresentableLowerShriek.lean#L136). The attribute's comment: “part (2): the left adjoint on abelian sheaves”.

> **Stacks 09WM, part (2).** The functor `a_! : Ab((C/K)_total) ⥤ Ab(C)` is left adjoint to the
> inverse image `a^{-1} : Ab(C) ⥤ Ab((C/K)_total)` of the augmentation, which on abelian sheaves as
> on sheaves of sets is restriction along `j_total`.

```lean
def augmentationAbelianLowerShriekAdjunction :
    augmentationAbelianLowerShriek J K ⊣
      (totalForget K).sheafPushforwardContinuous AddCommGrpCat.{u}
        ((situation J K).totalTopology) J
```

**`CategoryTheory.SimplicialSemiRepresentable.augmentationInverseImageComponentIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/SimplicialSemiRepresentableLowerShriek.lean, line 151](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/SimplicialSemiRepresentableLowerShriek.lean#L151). The attribute's comment: “part (3): the inverse image in each simplicial degree”.

> **Stacks 09WM, part (3).** The inverse image of the augmentation followed by restriction to
> the simplicial degree `n` is the inverse image `a_n^{-1}` of the augmentation of that degree,
> which by Stacks 0D8B is the inverse image of the morphism of topoi of the localization functor
> `j_n : C/K_n ⥤ C`, that is restriction along `j_n`. So `a^{-1}ℱ` is in degree `n` the sheaf
> `a_n^{-1}ℱ`.

```lean
def augmentationInverseImageComponentIso (n : SimplexCategory) :
    (CocontinuousSimplicialSite.Augmentation.totalMorphismOfTopoi
          (augmentation J K)).inverseImage ⋙ (situation J K).restrict n ≅
      (localizationMorphism J K n).inverseImage
```

**`CategoryTheory.SimplicialSemiRepresentable.augmentationAbelianPushforwardFork`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/SimplicialSemiRepresentableLowerShriek.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/SimplicialSemiRepresentableLowerShriek.lean#L191). The attribute's comment: “part (4): the direct image is the equalizer of the two vertex maps”.

> **Stacks 09WM, part (4).** The fork of the direct image `a_*𝒢` of an abelian sheaf on the
> total site over the two maps `a_{0,*}𝒢_0 ⟶ a_{1,*}𝒢_1` attached to the two vertices of the
> one-simplex, which are the two cofaces of the cosimplicial sheaf `n ↦ a_{n,*}𝒢_n`. Its map is the
> canonical projection of `a_*𝒢` onto `a_{0,*}𝒢_0`, and it equalises the two because the
> projections form a cone.

```lean
def augmentationAbelianPushforwardFork :
    Fork ((augmentationAbelianComponentDiagram J K G).map
        (SimplexCategory.const (SimplexCategory.mk 0) (SimplexCategory.mk 1) 0))
      ((augmentationAbelianComponentDiagram J K G).map
        (SimplexCategory.const (SimplexCategory.mk 0) (SimplexCategory.mk 1) 1))
```

**`CategoryTheory.SimplicialSemiRepresentable.augmentationAbelianPushforwardForkIsLimit`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/SimplicialSemiRepresentableLowerShriek.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/SimplicialSemiRepresentableLowerShriek.lean#L215). The attribute's comment: “part (4): the equalizer is a limit”.

> **Stacks 09WM, part (4).** That fork is a limit: the direct image `a_*𝒢` is the equalizer of
> the two maps `a_{0,*}𝒢_0 ⟶ a_{1,*}𝒢_1`.
>
> The direct image is by construction the limit of the cosimplicial sheaf `n ↦ a_{n,*}𝒢_n` over the
> whole simplex category, and the degree-zero leg of such a limit is a limit fork of the two maps
> in degrees `0 ⇉ 1`, which is the dual of Simplicial, Lemma 14.20.2.

```lean
def augmentationAbelianPushforwardForkIsLimit :
    IsLimit (augmentationAbelianPushforwardFork J K G)
```

## Tag 0DC0, a lemma

[Tag 0DC0](https://stacks.math.columbia.edu/tag/0DC0) in the Stacks Project.

**`Stacks.Cohomology.SimplicialSummand.cohomologyObj_iso_summand`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentSumNaturality/SummandCohomology.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Simplicial/ComponentSumNaturality/SummandCohomology.lean#L168).

> **Stacks 0DC0.** Cohomology over an object of one summand of a simplicial semi-representable
> site agrees with the cohomology, with coefficients in the corresponding member of the family of
> sheaves attached to the restriction of the sheaf to that simplicial degree.
>
> This is Stacks 0DBZ (`Stacks.Cohomology.SimplicialComponent.cohomologyObj_iso_component`) for the
> component inclusion, transported along the identification `hsite` of the degree-`n` site with the
> disjoint union of the summand slices, followed by the same bigger-site comparison again for the
> inclusion of the `i`-th summand slice.

```lean
def cohomologyObj_iso_summand
    (J : GrothendieckTopology C) (K : FormalCoproduct.{u} C)
    (S : SimplicialSiteSituation.{u}) (n : SimplexCategory)
    (hsite : (⟨S.component n, S.componentTopology n⟩ :
        Σ D : Cat.{u, u}, GrothendieckTopology D) =
      ⟨Cat.of (ComponentOver K), componentwiseTopology J K⟩)
    [HasSheafify S.totalTopology Ab.{u}]
    [HasSheafify (S.componentTopology n) Ab.{u}]
    [HasSheafify (componentwiseTopology J K) Ab.{u}]
    [HasExt.{w} (Sheaf S.totalTopology Ab.{u})]
    [HasExt.{w} (Sheaf (S.componentTopology n) Ab.{u})]
    [HasExt.{w} (Sheaf (componentwiseTopology J K) Ab.{u})]
    (i : K.I) (U : Over (K.obj i))
    [HasSheafify (J.over (K.obj i)) Ab.{u}]
    [HasExt.{w} (Sheaf (J.over (K.obj i)) Ab.{u})]
    (F : Sheaf S.totalTopology Ab.{u}) (p : ℕ) :
    let V : S.component n :=
      Eq.mp (congrArg (fun T : Σ D : Cat.{u, u}, GrothendieckTopology D =>
        (T.1 : Type u)) hsite.symm) (⟨i, U⟩ : ComponentOver K)
    let Fn : Sheaf (componentwiseTopology J K) Ab.{u} :=
      Eq.mp (congrArg (fun T : Σ D : Cat.{u, u}, GrothendieckTopology D =>
        Sheaf T.2 Ab.{u}) hsite)
        (((SimplicialSiteSituation.componentFunctor S n).sheafPullbackCocontinuous
          Ab.{u} (S.componentTopology n) S.totalTopology).obj F)
    Sheaf.H'.{w, u, u} F p ((SimplicialSiteSituation.componentFunctor S n).obj V) ≅
      Sheaf.H'.{w, u, u}
        (((formalCoproductSliceSheavesEquivalence J K Ab.{u}).val.functor.obj Fn) i) p U
```

## Tag 0D9W, a remark

[Tag 0D9W](https://stacks.math.columbia.edu/tag/0D9W) in the Stacks Project.

**`CategoryTheory.SemiRepresentable.Simplicial.totalRingedSite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedAugmentation.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedAugmentation.lean#L183). The attribute's comment: “total_ringed_site”.

> **Stacks 0D9W, total ringed site.** The total localization of a simplicial
> semi-representable object `K` of the underlying site of a ringed site `X`, equipped with the
> pulled-back structure sheaf `a⁻¹O_C`.

```lean
def totalRingedSite (X : AlgebraicGeometry.RingedSite.{u, v, w})
    (K : SimplicialObject (FormalCoproduct.{x} X.C)) : AlgebraicGeometry.RingedSite
```

**`CategoryTheory.SemiRepresentable.Simplicial.degreewiseRingedAugmentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedAugmentation.lean, line 272](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedAugmentation.lean#L272). The attribute's comment: “degreewise_ringed_augmentations”.

> **Stacks 0D9W, degreewise ringed augmentations.** For a simplicial semi-representable
> object `K` of the underlying site of a ringed site `X`, each simplicial degree carries a
> morphism of ringed topoi `a_n : (Sh(C/K_n), O_n) ⟶ (Sh(C), O_C)` from the localization at the
> degree-`n` term to the ambient ringed topos.

```lean
def degreewiseRingedAugmentation (X : AlgebraicGeometry.RingedSite.{u, v, max x u v w})
    (K : SimplicialObject (FormalCoproduct.{x} X.C)) (n : SimplexCategory) :
    AlgebraicGeometry.RingedToposHom
      (AlgebraicGeometry.RingedSite.localizationRingedTopos X (K.obj (op n)))
      (AlgebraicGeometry.RingedSite.ringedTopos.{u, v, max x w} X)
```

**`CategoryTheory.SemiRepresentable.Simplicial.totalRingedAugmentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedAugmentation.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedAugmentation.lean#L372). The attribute's comment: “ringed_augmentation”.

> **Stacks 0D9W, ringed augmentation.** For a simplicial semi-representable object `K` of the
> underlying site of a ringed site `X`, the total ringed site is augmented over `X` by a morphism
> of ringed topoi `a : (Sh((C/K)_total), O) ⟶ (Sh(C), O_C)`.

```lean
def totalRingedAugmentation (X : AlgebraicGeometry.RingedSite.{u, v, w})
    (K : SimplicialObject (FormalCoproduct.{x} X.C)) :
    AlgebraicGeometry.RingedToposHom
      (AlgebraicGeometry.RingedSite.ringedTopos.{max u v x, v, w}
        (totalRingedSite (AlgebraicGeometry.RingedSite.liftedRingedSite.{x, u, v, w} X) K))
      (AlgebraicGeometry.RingedSite.ringedTopos.{u, v, max x w}
        (AlgebraicGeometry.RingedSite.liftedRingedSite.{x, u, v, w} X))
```

**`CategoryTheory.SemiRepresentable.Simplicial.ringedTransitionMorphism_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedAugmentation.lean, line 434](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedAugmentation.lean#L434). The attribute's comment: “flat_transition_morphisms”.

> **Stacks 0D9W, flat transition morphisms.** For a simplicial semi-representable object `K`
> of the underlying site of a ringed site `X`, the morphism of ringed topoi attached to a simplex
> map `φ : [m] ⟶ [n]` is flat.

```lean
theorem ringedTransitionMorphism_isFlat
    (X : AlgebraicGeometry.RingedSite.{u, v, max x u v w})
    (K : SimplicialObject (FormalCoproduct.{x} X.C))
    {m n : SimplexCategory} (φ : m ⟶ n) :
    Stacks.Sheaf.RingedToposFlat.RingedToposHom.IsFlat.{max u v x, max u v x,
        max x u v w, max u v x, max u v x, max x u v w}
      (ringedTransitionMorphism.{x, u, v, w} X K φ).val
```

**`CategoryTheory.SemiRepresentable.Simplicial.degreewiseRingedAugmentation_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedAugmentation.lean, line 497](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedAugmentation.lean#L497). The attribute's comment: “flat_degreewise_augmentations”.

> **Stacks 0D9W, flat degreewise augmentations.** For a simplicial semi-representable object
> `K` of the underlying site of a ringed site `X`, the morphism of ringed topoi
> `a_n : (Sh(C/K_n), O_n) ⟶ (Sh(C), O_C)` is flat in every simplicial degree.

```lean
theorem degreewiseRingedAugmentation_isFlat
    (X : AlgebraicGeometry.RingedSite.{u, v, max x u v w})
    (K : SimplicialObject (FormalCoproduct.{x} X.C)) (n : SimplexCategory) :
    Stacks.Sheaf.RingedToposFlat.RingedToposHom.IsFlat.{max u v x, max u v x,
        max x u v w, v, u, max x u v w}
      (degreewiseRingedAugmentation.{x, u, v, w} X K n)
```

**`CategoryTheory.SemiRepresentable.Simplicial.totalRingedAugmentation_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedAugmentation.lean, line 530](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedAugmentation.lean#L530). The attribute's comment: “flat_augmentation”.

> **Stacks 0D9W, flat augmentation.** For a simplicial semi-representable object `K` of the
> underlying site of a ringed site `X`, the augmentation
> `a : (Sh((C/K)_total), O) ⟶ (Sh(C), O_C)` of the total ringed site is flat.

```lean
theorem totalRingedAugmentation_isFlat (X : AlgebraicGeometry.RingedSite.{u, v, w})
    (K : SimplicialObject (FormalCoproduct.{x} X.C)) :
    Stacks.Sheaf.RingedToposFlat.RingedToposHom.IsFlat.{v, max u v x,
        max x u v w, v, u, max x u v w}
      (totalRingedAugmentation.{x, u, v, w} X K)
```

**`CategoryTheory.SemiRepresentable.Simplicial.totalLowerShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedLowerShriek.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedLowerShriek.lean#L232). The attribute's comment: “lower_shriek”.

> **Stacks 0D9W, item (4).** For a simplicial semi-representable object `K` of the underlying
> site of a ringed site `X`, the inverse image `a^*` of sheaves of modules along the augmentation of
> the total ringed site has a left adjoint `a_! : Mod(O) ⥤ Mod(O_C)`.

```lean
def totalLowerShriekAdjunction :
    totalLowerShriek.{x, u, v, w} X K ⊣ totalInverseImageModules.{x, u, v, w} X K
```

**`CategoryTheory.SemiRepresentable.Simplicial.degreewiseLowerShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedLowerShriek.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedLowerShriek.lean#L270). The attribute's comment: “degreewise_lower_shriek_adjunction”.

> **Stacks 0D9W, the degreewise lower shriek.** The inverse image `a_n^*` of sheaves of modules
> along the degreewise augmentation `a_n : (Sh(C/K_n), O_n) ⟶ (Sh(C), O_C)` has a left adjoint
> `a_{n!} : Mod(O_n) ⥤ Mod(O_C)`.
>
> Exactness of `a_{n!}`, which the source asserts as well, is
> `CategoryTheory.SemiRepresentable.Simplicial.exactFunctor_degreewiseLowerShriek`.

```lean
def degreewiseLowerShriekAdjunction :
    degreewiseLowerShriek.{x, u, v, w} X K n ⊣
      degreewiseInverseImageModules.{x, u, v, w} X K n
```

**`CategoryTheory.SemiRepresentable.Simplicial.exactFunctor_degreewiseLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedLowerShriek.lean, line 331](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedLowerShriek.lean#L331). The attribute's comment: “degreewise_lower_shriek_exact”.

> **Stacks 0D9W, exactness of the degreewise lower shriek.** The functor
> `a_{n!} : Mod(O_n) ⥤ Mod(O_C)` left adjoint to the inverse image `a_n^*` of the degreewise
> augmentation is exact.
>
> Right exactness is formal, `a_{n!}` being a left adjoint. Left exactness is the direct-sum
> formula: the sections of `a_{n!}G` over `V` are the sum, over the pairs `(i, V ⟶ K_{n,i})`, of
> the sections of `G` at the corresponding object of the slice site, so `a_{n!}` is injective on
> sections as soon as `G ⟶ G'` is. That is the content of
> `Stacks.Sites.ReducedLowerShriek.lowerShriek_exact` at the reduction data
> `CategoryTheory.SemiRepresentable.Simplicial.localizationReduction`.

```lean
theorem exactFunctor_degreewiseLowerShriek :
    exactFunctor
      (SheafOfModules.{max x u v w} (Stacks.SheafOfModules.Tensor.ringSheaf
        (AlgebraicGeometry.RingedSite.localizationRingedTopos X (K.obj (op n))).O))
      (SheafOfModules.{max x u v w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
      (degreewiseLowerShriek.{x, u, v, w} X K n)
```

**`CategoryTheory.SemiRepresentable.Simplicial.transitionLowerShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedLowerShriek.lean, line 388](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedLowerShriek.lean#L388). The attribute's comment: “transition_lower_shriek_adjunction”.

> **Stacks 0D9W, the lower shriek of a transition morphism.** For a simplex map
> `φ : [m] ⟶ [n]`, the inverse image `f_φ^*` of sheaves of modules along the transition morphism of
> ringed topoi `f_φ : (Sh(C/K_n), O_n) ⟶ (Sh(C/K_m), O_m)` has a left adjoint
> `f_{φ!} : Mod(O_n) ⥤ Mod(O_m)`.
>
> Exactness of `f_{φ!}`, which the source asserts as well, is
> `CategoryTheory.SemiRepresentable.Simplicial.exactFunctor_transitionLowerShriek`.

```lean
def transitionLowerShriekAdjunction (φ : m ⟶ n) :
    transitionLowerShriek.{x, u, v, w} X K φ ⊣ transitionInverseImageModules.{x, u, v, w} X K φ
```

**`CategoryTheory.SemiRepresentable.Simplicial.exactFunctor_transitionLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedLowerShriek.lean, line 525](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedLowerShriek.lean#L525). The attribute's comment: “transition_lower_shriek_exact”.

> **Stacks 0D9W, exactness of the lower shriek of a transition morphism.** For a simplex map
> `φ : [m] ⟶ [n]`, the functor `f_{φ!} : Mod(O_n) ⥤ Mod(O_m)` left adjoint to the inverse image
> `f_φ^*` is exact.
>
> Right exactness is formal, `f_{φ!}` being a left adjoint. Left exactness is the direct-sum
> formula: the sections of `f_{φ!}G` over an object `W` of the degree-`m` localization are the sum,
> over the components `i` of `K_n` and the arrows `W.left ⟶ K_{n,i}` under `K(φ)`, of the sections
> of `G` at the corresponding object of the slice site.

```lean
theorem exactFunctor_transitionLowerShriek (φ : m ⟶ n) :
    exactFunctor
      (SheafOfModules.{max x u v w} (Stacks.SheafOfModules.inverseImageRing
        (componentwiseTopology X.J (K.obj (op n))) (componentwiseTopology X.J (K.obj (op m)))
        (⟨K.obj (op n), K.obj (op m), K.map φ.op⟩ :
          LocalizationSites.{x} X.C X.J).relocalizationFunctor
        (Stacks.SheafOfModules.Tensor.ringSheaf
          (AlgebraicGeometry.RingedSite.localizationRingedTopos X (K.obj (op m))).O)))
      (SheafOfModules.{max x u v w} (Stacks.SheafOfModules.Tensor.ringSheaf
        (AlgebraicGeometry.RingedSite.localizationRingedTopos X (K.obj (op m))).O))
      (transitionLowerShriek.{x, u, v, w} X K φ)
```

**`CategoryTheory.SemiRepresentable.Simplicial.componentRingedMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedLowerShriek.lean, line 826](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedLowerShriek.lean#L826). The attribute's comment: “component_morphism”.

> **Stacks 0D9W, the morphism of a simplicial degree into the total ringed site.** For a
> simplicial semi-representable object `K` of the underlying site of a ringed site `X`, the
> degree-`n` componentwise localization is a ringed topos over the total ringed site by a morphism
> of ringed topoi `g_n : (Sh(C/K_n), O_n) ⟶ (Sh((C/K)_total), O)`.

```lean
def componentRingedMorphism :
    AlgebraicGeometry.RingedToposHom (componentRingedTopos.{x, u, v, w} X K n)
      (AlgebraicGeometry.RingedSite.ringedTopos.{max u v x, v, w}
        (totalRingedSite.{x, u, v, max x u v w} X K))
```

**`CategoryTheory.SemiRepresentable.Simplicial.componentRingedMorphism_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedLowerShriek.lean, line 845](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedLowerShriek.lean#L845). The attribute's comment: “flat_component_morphism”.

> **Stacks 0D9W, flat component morphism.** The morphism of ringed topoi
> `g_n : (Sh(C/K_n), O_n) ⟶ (Sh((C/K)_total), O)` is flat: its structure map in inverse-image form
> is the identification of `g_n⁻¹O` with `O_n`, hence an isomorphism, and an isomorphism of sheaves
> of commutative rings is flat.

```lean
theorem componentRingedMorphism_isFlat :
    Stacks.Sheaf.RingedToposFlat.RingedToposHom.IsFlat.{max x u v, max x u v,
        max x u v w, v, max u v x, max x u v w}
      (componentRingedMorphism.{x, u, v, w} X K n)
```

**`CategoryTheory.SemiRepresentable.Simplicial.componentLowerShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedLowerShriek.lean, line 881](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedLowerShriek.lean#L881). The attribute's comment: “component_lower_shriek_adjunction”.

> **Stacks 0D9W, the lower shriek of a component morphism.** The inverse image `g_n^*` of
> sheaves of modules along `g_n` has a left adjoint `g_{n!} : Mod(O_n) ⥤ Mod(O)`.
>
> Exactness of `g_{n!}`, which the source asserts as well, is
> `CategoryTheory.SemiRepresentable.Simplicial.exactFunctor_componentLowerShriek`.

```lean
def componentLowerShriekAdjunction :
    componentLowerShriek.{x, u, v, w} X K n ⊣ componentInverseImageModules.{x, u, v, w} X K n
```

**`CategoryTheory.SemiRepresentable.Simplicial.exactFunctor_componentLowerShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedLowerShriek.lean, line 959](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedLowerShriek.lean#L959). The attribute's comment: “component_lower_shriek_exact”.

> **Stacks 0D9W, exactness of the lower shriek of a component morphism.** The functor
> `g_{n!} : Mod(O_n) ⥤ Mod(O)` left adjoint to the inverse image `g_n^*` is exact.
>
> This is Stacks 0D74 for the `Comma`-category model of the total site: right exactness is formal,
> `g_{n!}` being a left adjoint, and left exactness is the direct-sum formula, whose index set at
> an object `Z` of the total site is `componentFibre` — a component of `K_n`, a simplex map
> `Z.right ⟶ [n]` and an arrow of the ambient site into that component. The simplex maps are the
> `φ : [n] ⟶ [m]` of the direct-sum formula of Tag 0D72. The flatness hypothesis of 0D74 is not
> needed here: the structure sheaf of the total site is pulled back from the ambient site, so it
> does not see the arrow along which a summand is taken.

```lean
theorem exactFunctor_componentLowerShriek :
    exactFunctor
      (SheafOfModules.{max x u v w} (Stacks.SheafOfModules.inverseImageRing
        (componentwiseTopology X.J (K.obj (op n))) (totalLocalizationTopology K X.J)
        (componentInclusion K n) (pulledBackRingSheaf X K)))
      (SheafOfModules.{max x u v w} (pulledBackRingSheaf X K))
      (componentLowerShriek.{x, u, v, w} X K n)
```

**`CategoryTheory.SemiRepresentable.Simplicial.pulledBackStructureSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableStructureSheaf.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableStructureSheaf.lean#L258). The attribute's comment: “pulled_back_structure_sheaf”.

> **Stacks 0D9W, pulled-back structure sheaf.** For the canonical localization
> augmentation attached to `K`, set `O = a⁻¹ O_C`. This is restriction along `j_total`,
> viewed as a sheaf valued in commutative rings.

```lean
def pulledBackStructureSheaf (X : AlgebraicGeometry.RingedSite.{u, v, w})
    (K : SimplicialObject (FormalCoproduct.{x} X.C)) :
    Sheaf (totalLocalizationTopology K X.J) CommRingCat.{w}
```

## Tag 0D9X, a remark

[Tag 0D9X](https://stacks.math.columbia.edu/tag/0D9X) in the Stacks Project.

**`CategoryTheory.SemiRepresentable.Simplicial.totalRingedSiteOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean#L142). The attribute's comment: “item (1): the ringed site ((C/K)_total, O)”.

> For a ringed site `(C, O_C)`, an object `U` of `C` and a simplicial object `K` of
> `SR(C, U) = SR(C/U)`, the total localization site `(C/K)_total` of `K` over the slice site `C/U`,
> with the structure sheaf `O = a⁻¹O_U` pulled back from `O_U = O_C|_{C/U}`.

```lean
abbrev totalRingedSiteOver : AlgebraicGeometry.RingedSite
```

**`CategoryTheory.SemiRepresentable.Simplicial.totalRingedAugmentationOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean#L156). The attribute's comment: “item (2): the morphism of ringed topoi a”.

> The augmentation `a : (Sh((C/K)_total), O) ⟶ (Sh(C/U), O_U)` of the total ringed site of a
> simplicial object `K` of `SR(C, U)`, as a morphism of ringed topoi.

```lean
def totalRingedAugmentationOver :
    AlgebraicGeometry.RingedToposHom
      (AlgebraicGeometry.RingedSite.ringedTopos.{max u v x, v, w}
        (totalRingedSite (AlgebraicGeometry.RingedSite.liftedRingedSite.{x} (X.over U)) K))
      (AlgebraicGeometry.RingedSite.ringedTopos.{max u v, v, max x w}
        (AlgebraicGeometry.RingedSite.liftedRingedSite.{x} (X.over U)))
```

**`CategoryTheory.SemiRepresentable.Simplicial.degreewiseRingedAugmentationOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean#L175). The attribute's comment: “item (3): the morphisms of ringed topoi a_n”.

> The degreewise augmentations `a_n : (Sh(C/K_n), O_n) ⟶ (Sh(C/U), O_U)` of a simplicial
> object `K` of `SR(C, U)`, as morphisms of ringed topoi.

```lean
def degreewiseRingedAugmentationOver (n : SimplexCategory) :
    AlgebraicGeometry.RingedToposHom
      (AlgebraicGeometry.RingedSite.localizationRingedTopos
        (AlgebraicGeometry.RingedSite.liftedRingedSite.{x} (X.over U)) (K.obj (op n)))
      (AlgebraicGeometry.RingedSite.ringedTopos.{max u v, v, max x w}
        (AlgebraicGeometry.RingedSite.liftedRingedSite.{x} (X.over U)))
```

**`CategoryTheory.SemiRepresentable.Simplicial.totalLowerShriekOverAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean#L198). The attribute's comment: “item (4): a_! is left adjoint to a^*”.

> For a simplicial object `K` of `SR(C, U)`, the functor `a_! : Mod(O) ⥤ Mod(O_U)` is left
> adjoint to the pullback `a^*` of sheaves of modules along the augmentation
> `a : (Sh((C/K)_total), O) ⟶ (Sh(C/U), O_U)`.

```lean
def totalLowerShriekOverAdjunction :
    totalLowerShriekOver.{x, u, v, w} X U K ⊣
      (totalRingedAugmentationOver.{x, u, v, w} X U K).toModulesHom.pullbackModules
```

**`CategoryTheory.SemiRepresentable.Simplicial.totalRingedAugmentationOver_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean#L208). The attribute's comment: “the results of 0D9W: a is flat”.

> The augmentation `a : (Sh((C/K)_total), O) ⟶ (Sh(C/U), O_U)` of a simplicial object `K` of
> `SR(C, U)` is flat.

```lean
theorem totalRingedAugmentationOver_isFlat :
    Stacks.Sheaf.RingedToposFlat.RingedToposHom.IsFlat.{v, max u v x,
        max x u v w, v, max u v, max x u v w}
      (totalRingedAugmentationOver.{x, u, v, w} X U K)
```

**`CategoryTheory.SemiRepresentable.Simplicial.degreewiseRingedAugmentationOver_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean, line 217](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean#L217). The attribute's comment: “the results of 0D9W: a_n is flat”.

> Every degreewise augmentation `a_n : (Sh(C/K_n), O_n) ⟶ (Sh(C/U), O_U)` of a simplicial
> object `K` of `SR(C, U)` is flat.

```lean
theorem degreewiseRingedAugmentationOver_isFlat (n : SimplexCategory) :
    Stacks.Sheaf.RingedToposFlat.RingedToposHom.IsFlat.{max u v x, max u v x,
        max x u v w, v, max u v, max x u v w}
      (degreewiseRingedAugmentationOver.{x, u, v, w} X U K n)
```

**`CategoryTheory.SemiRepresentable.Simplicial.degreewiseLowerShriekOverAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean#L228). The attribute's comment: “the results of 0D9W: a_{n!} is left adjoint to a_n^*”.

> For a simplicial object `K` of `SR(C, U)`, the inverse image `a_n^*` of sheaves of modules
> along the degreewise augmentation `a_n : (Sh(C/K_n), O_n) ⟶ (Sh(C/U), O_U)` has the left adjoint
> `a_{n!} : Mod(O_n) ⥤ Mod(O_U)`.

```lean
def degreewiseLowerShriekOverAdjunction (n : SimplexCategory) :
    degreewiseLowerShriek.{x, max u v, v, w}
        (AlgebraicGeometry.RingedSite.liftedRingedSite.{x} (X.over U)) K n ⊣
      degreewiseInverseImageModules.{x, max u v, v, w}
        (AlgebraicGeometry.RingedSite.liftedRingedSite.{x} (X.over U)) K n
```

**`CategoryTheory.SemiRepresentable.Simplicial.exactFunctor_degreewiseLowerShriekOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean#L239). The attribute's comment: “the results of 0D9W: a_{n!} is exact”.

> For a simplicial object `K` of `SR(C, U)`, the functor `a_{n!} : Mod(O_n) ⥤ Mod(O_U)` is
> exact.

```lean
theorem exactFunctor_degreewiseLowerShriekOver (n : SimplexCategory) :
    exactFunctor _ _ (degreewiseLowerShriek.{x, max u v, v, w}
      (AlgebraicGeometry.RingedSite.liftedRingedSite.{x} (X.over U)) K n)
```

**`CategoryTheory.SemiRepresentable.Simplicial.ringedTransitionMorphismOver_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean#L248). The attribute's comment: “the results of 0D9W: f_φ is flat”.

> For a simplicial object `K` of `SR(C, U)` and a simplex map `φ : [m] ⟶ [n]`, the morphism of
> ringed topoi `f_φ : (Sh(C/K_n), O_n) ⟶ (Sh(C/K_m), O_m)` is flat.

```lean
theorem ringedTransitionMorphismOver_isFlat {m n : SimplexCategory} (φ : m ⟶ n) :
    Stacks.Sheaf.RingedToposFlat.RingedToposHom.IsFlat.{max u v x, max u v x,
        max x u v w, max u v x, max u v x, max x u v w}
      (ringedTransitionMorphism.{x, max u v, v, w}
        (AlgebraicGeometry.RingedSite.liftedRingedSite.{x} (X.over U)) K φ).val
```

**`CategoryTheory.SemiRepresentable.Simplicial.transitionLowerShriekOverAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean#L259). The attribute's comment: “the results of 0D9W: f_{φ!} is left adjoint to f_φ^*”.

> For a simplicial object `K` of `SR(C, U)` and a simplex map `φ : [m] ⟶ [n]`, the inverse image
> `f_φ^*` of sheaves of modules has the left adjoint `f_{φ!} : Mod(O_n) ⥤ Mod(O_m)`.

```lean
def transitionLowerShriekOverAdjunction {m n : SimplexCategory} (φ : m ⟶ n) :
    transitionLowerShriek.{x, max u v, v, w}
        (AlgebraicGeometry.RingedSite.liftedRingedSite.{x} (X.over U)) K φ ⊣
      transitionInverseImageModules.{x, max u v, v, w}
        (AlgebraicGeometry.RingedSite.liftedRingedSite.{x} (X.over U)) K φ
```

**`CategoryTheory.SemiRepresentable.Simplicial.exactFunctor_transitionLowerShriekOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean#L270). The attribute's comment: “the results of 0D9W: f_{φ!} is exact”.

> For a simplicial object `K` of `SR(C, U)` and a simplex map `φ : [m] ⟶ [n]`, the functor
> `f_{φ!} : Mod(O_n) ⥤ Mod(O_m)` is exact.

```lean
theorem exactFunctor_transitionLowerShriekOver {m n : SimplexCategory} (φ : m ⟶ n) :
    exactFunctor _ _ (transitionLowerShriek.{x, max u v, v, w}
      (AlgebraicGeometry.RingedSite.liftedRingedSite.{x} (X.over U)) K φ)
```

**`CategoryTheory.SemiRepresentable.Simplicial.componentRingedMorphismOver_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean, line 279](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean#L279). The attribute's comment: “the results of 0D9W: g_n is flat”.

> For a simplicial object `K` of `SR(C, U)`, the morphism of ringed topoi
> `g_n : (Sh(C/K_n), O_n) ⟶ (Sh((C/K)_total), O)` is flat.

```lean
theorem componentRingedMorphismOver_isFlat (n : SimplexCategory) :
    Stacks.Sheaf.RingedToposFlat.RingedToposHom.IsFlat.{max x u v, max x u v,
        max x u v w, v, max u v x, max x u v w}
      (componentRingedMorphism.{x, max u v, v, w}
        (AlgebraicGeometry.RingedSite.liftedRingedSite.{x} (X.over U)) K n)
```

**`CategoryTheory.SemiRepresentable.Simplicial.componentLowerShriekOverAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean, line 290](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean#L290). The attribute's comment: “the results of 0D9W: g_{n!} is left adjoint to g_n^*”.

> For a simplicial object `K` of `SR(C, U)`, the inverse image `g_n^*` of sheaves of modules
> along `g_n` has the left adjoint `g_{n!} : Mod(O_n) ⥤ Mod(O)`.

```lean
def componentLowerShriekOverAdjunction (n : SimplexCategory) :
    componentLowerShriek.{x, max u v, v, w}
        (AlgebraicGeometry.RingedSite.liftedRingedSite.{x} (X.over U)) K n ⊣
      componentInverseImageModules.{x, max u v, v, w}
        (AlgebraicGeometry.RingedSite.liftedRingedSite.{x} (X.over U)) K n
```

**`CategoryTheory.SemiRepresentable.Simplicial.exactFunctor_componentLowerShriekOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/RingedOverObject.lean#L301). The attribute's comment: “the results of 0D9W: g_{n!} is exact”.

> For a simplicial object `K` of `SR(C, U)`, the functor `g_{n!} : Mod(O_n) ⥤ Mod(O)` is
> exact.

```lean
theorem exactFunctor_componentLowerShriekOver (n : SimplexCategory) :
    exactFunctor _ _ (componentLowerShriek.{x, max u v, v, w}
      (AlgebraicGeometry.RingedSite.liftedRingedSite.{x} (X.over U)) K n)
```

**`AlgebraicGeometry.SemiRepresentable.Simplicial.totalRingedSite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/TotalRingedSite.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/TotalRingedSite.lean#L89). The attribute's comment: “ringed_total_site”.

> The total localization of a simplicial semi-representable object over a ringed site, together
> with its pulled-back structure sheaf, is a ringed site.

```lean
def totalRingedSite (X : AlgebraicGeometry.RingedSite.{u, v, w})
    (K : SimplicialObject (FormalCoproduct.{x} X.C)) : AlgebraicGeometry.RingedSite
```

**`AlgebraicGeometry.SemiRepresentable.Simplicial.ringedAugmentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/TotalRingedSite.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentable/TotalRingedSite.lean#L140). The attribute's comment: “ringed_augmentation”.

> The total localization of a simplicial semi-representable object over a ringed site has a
> canonical augmentation to the base as a morphism of ringed topoi.

```lean
def ringedAugmentation (X : AlgebraicGeometry.RingedSite.{u, v, w})
    (K : SimplicialObject (FormalCoproduct.{x} X.C)) :
    AlgebraicGeometry.RingedToposHom
      (AlgebraicGeometry.RingedSite.ringedTopos.{max x u v, v, w}
        (totalRingedSite.{x, v, u, max x u v w} (liftedRingedSite.{x, v, u, w} X) K))
      (AlgebraicGeometry.RingedSite.ringedTopos.{u, v, max x w}
        (liftedRingedSite.{x, v, u, w} X))
```

**`CategoryTheory.SemiRepresentable.Simplicial.totalRingedSite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedAugmentation.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Simplicial/SemiRepresentableRingedAugmentation.lean#L183). The attribute's comment: “ringed_total_site”.

> **Stacks 0D9W, total ringed site.** The total localization of a simplicial
> semi-representable object `K` of the underlying site of a ringed site `X`, equipped with the
> pulled-back structure sheaf `a⁻¹O_C`.

```lean
def totalRingedSite (X : AlgebraicGeometry.RingedSite.{u, v, w})
    (K : SimplicialObject (FormalCoproduct.{x} X.C)) : AlgebraicGeometry.RingedSite
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 85.16, Tag 0D8A](https://stacks.math.columbia.edu/tag/0D8A)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
