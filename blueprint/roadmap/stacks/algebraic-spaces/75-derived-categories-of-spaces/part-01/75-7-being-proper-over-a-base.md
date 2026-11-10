---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.not_tfae_isProper_closedSubspace, AlgebraicGeometry.Space.IsProperOver, AlgebraicGeometry.Space.isProper_reducedClosedSubspace_iff_exists, AlgebraicGeometry.Space.exists_isProper_closedSubspace_iff_forall, AlgebraicGeometry.Space.isProperOver_of_subset, AlgebraicGeometry.Space.isProperOver_preimage, AlgebraicGeometry.Space.isProperOver_image_of_universallyClosed, AlgebraicGeometry.Space.isProperOver_image_of_isSeparated
statement: formalized
proof: formalized
---

# 75.7 Being proper over a base

Section 75.7 of the Stacks Project, [Tag 0CZB](https://stacks.math.columbia.edu/tag/0CZB). 11 tags here are carried by 23 declarations of the repository (all in StacksFrontier) and 14 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CZB, the section

[Tag 0CZB](https://stacks.math.columbia.edu/tag/0CZB) in the Stacks Project.

**`AlgebraicGeometry.Space.not_tfae_isProper_closedSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean#L189). The attribute's comment: “the remark after Definition 0CZD: Lemma 0CZC is false if f is not locally of finite type”.

> **Lemma 0CZC fails without local finite type** (the remark after Definition 0CZD, Section
> 0CZB). Over every big fppf site there are a scheme `S`, a morphism `f : X ⟶ Y` of algebraic spaces
> over `S` which is not locally of finite type, and a closed subset `T ⊆ |X|` for which the three
> conditions of Lemma 0CZC are not equivalent: (1) the reduced induced closed subspace on `T` is
> proper over `Y`, (2) some closed subspace with points `T` is, (3) every one is.

```lean
theorem not_tfae_isProper_closedSubspace (B : BigFppfSite.{u}) :
    ∃ (S : Scheme.{u}) (hS : B.Contains S) (X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
      (hX : IsAlgebraicSpace B S hS X) (_hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
      (T : Set (points B S hS X)) (hT : IsClosed T),
      ¬ IsLocallyOfFiniteType B S hS f ∧
      ¬ [IsProper B S hS ((reducedClosedSubspace B S hS X hX T hT).ι ≫ f),
          ∃ (Z : Subfunctor X) (_ : IsClosedSubspace B S hS Z),
            Set.range (pointsMap B S hS Z.toFunctor Z.ι) = T ∧ IsProper B S hS (Z.ι ≫ f),
          ∀ (Z : Subfunctor X) (_ : IsClosedSubspace B S hS Z),
            Set.range (pointsMap B S hS Z.toFunctor Z.ι) = T →
              IsProper B S hS (Z.ι ≫ f)].TFAE
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.IsProperOver`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperClosedSubset.lean#L60), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean#L63) (StacksFrontier): “the notion of the section: a closed subset T ⊆ |X| is proper over Y, for f locally of finite type, when the reduced induced closed subspace on T is proper over Y (Definition 0CZD)”.
- [`AlgebraicGeometry.Space.isProper_reducedClosedSubspace_iff_exists`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubset.lean#L414), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean#L67) (StacksFrontier): “the equivalence of the conditions of Lemma 0CZC that the notion rests on: the reduced induced subspace is proper over Y iff some closed subspace with points T is”.
- [`AlgebraicGeometry.Space.exists_isProper_closedSubspace_iff_forall`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubset.lean#L439), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean#L71) (StacksFrontier): “the equivalence of the conditions of Lemma 0CZC that the notion rests on: some closed subspace with points T is proper over Y iff every one is”.
- [`AlgebraicGeometry.Space.isProperOver_of_subset`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperClosedSubset.lean#L169), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean#L75) (StacksFrontier): “Lemma 0CZE of the section: a closed subset of a closed subset proper over Y is proper over Y”.
- [`AlgebraicGeometry.Space.isProperOver_preimage`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubsetBaseChange.lean#L135), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean#L78) (StacksFrontier): “Lemma 0CZF of the section: the inverse image of a closed subset proper over Y under a base change is proper over the new base”.
- [`AlgebraicGeometry.Space.isProperOver_image_of_universallyClosed`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubsetImage.lean#L200), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean#L81) (StacksFrontier): “Lemma 0CZG of the section: images of closed subsets proper over the base, under a universally closed morphism”.
- [`AlgebraicGeometry.Space.isProperOver_image_of_isSeparated`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubsetImage.lean#L256), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean#L85) (StacksFrontier): “Lemma 0CZG of the section: images of closed subsets proper over the base, under a morphism to a space separated over the base”.
- [`AlgebraicGeometry.Space.isProperOver_preimage_of_isProper`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubsetImage.lean#L280), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean#L89) (StacksFrontier): “Lemma 0CZG of the section: inverse images of closed subsets proper over the base, under a proper morphism”.
- [`AlgebraicGeometry.Space.isProperOver_iUnion`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubsetUnion.lean#L228), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean#L92) (StacksFrontier): “Lemma 0CZH of the section: a finite union of closed subsets proper over Y is proper over Y”.
- [`AlgebraicGeometry.Space.hasProperSupport_tfae`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperModuleSupport.lean#L223), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean#L95) (StacksFrontier): “Lemma 0CZI of the section: the equivalent conditions for a module to have support proper over Y”.
- [`AlgebraicGeometry.Space.isProperOver_supportOfSheaf_modulePullback`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ModuleSupportProperBaseChange.lean#L60), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean#L98) (StacksFrontier): “Lemma 0CZJ of the section: support proper over the base is preserved by base change”.
- [`AlgebraicGeometry.Space.isSerreClass_isCoherentProperOver`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperSupportSerre.lean#L259), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperOverBase.lean#L101) (StacksFrontier): “Lemma 0CZK of the section, part (2): the coherent modules with support proper over Y form a Serre subcategory”.

## Tag 0CZC, a lemma

[Tag 0CZC](https://stacks.math.columbia.edu/tag/0CZC) in the Stacks Project.

**`AlgebraicGeometry.Space.isProper_reducedClosedSubspace_iff_exists`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubset.lean, line 414](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubset.lean#L414). The attribute's comment: “conditions (1) and (2)”. References: EGA II (5.4.10), “indep. of subscheme”.

> **Stacks 0CZC, conditions (1) and (2).** For a morphism of algebraic spaces over `S` locally
> of finite type and a closed set `T` of points of the source, the reduced induced closed subspace
> on `T` is proper over the target exactly when some closed subspace with set of points `T` is
> proper over the target.
>
> The forward implication must exhibit a closed subspace with set of points `T`, which is the
> existence clause of Stacks 03IQ. That clause is now available unconditionally: the reduced
> induced subspace *is* a closed subspace by
> `AlgebraicGeometry.Space.isClosedSubspace_reducedClosedSubspace_of_closedImmersionDescent`
> applied to
> `AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveEtale_isClosedImmersion`, which is
> Stacks 02W8 at the closed immersions.

```lean
theorem isProper_reducedClosedSubspace_iff_exists (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f)
    (T : Set (points B S hS X)) (hT : IsClosed T) :
    IsProperOver B S hS hX hY f hf T hT ↔
      ∃ (Z : Subfunctor X) (_ : IsClosedSubspace B S hS Z),
        Set.range (pointsMap B S hS Z.toFunctor Z.ι) = T ∧ IsProper B S hS (Z.ι ≫ f)
```

**`AlgebraicGeometry.Space.exists_isProper_closedSubspace_iff_forall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubset.lean, line 439](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubset.lean#L439). The attribute's comment: “conditions (2) and (3)”. References: EGA II (5.4.10), “indep. of subscheme”.

> **Stacks 0CZC, conditions (2) and (3).** If one closed subspace with a given closed set of
> points is proper over the target, then every closed subspace with that set of points is.
>
> The implication from (3) to (2) must exhibit a closed subspace with set of points `T`, which is
> the existence clause of Stacks 03IQ. That clause is now available unconditionally: the reduced
> induced subspace *is* a closed subspace by
> `AlgebraicGeometry.Space.isClosedSubspace_reducedClosedSubspace_of_closedImmersionDescent`
> applied to
> `AlgebraicGeometry.Space.isEffectiveDescentAlongSurjectiveEtale_isClosedImmersion`, which is
> Stacks 02W8 at the closed immersions.

```lean
theorem exists_isProper_closedSubspace_iff_forall (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f)
    (T : Set (points B S hS X)) (hT : IsClosed T) :
    (∃ (Z : Subfunctor X) (_ : IsClosedSubspace B S hS Z),
        Set.range (pointsMap B S hS Z.toFunctor Z.ι) = T ∧ IsProper B S hS (Z.ι ≫ f)) ↔
      ∀ (Z : Subfunctor X) (_ : IsClosedSubspace B S hS Z),
        Set.range (pointsMap B S hS Z.toFunctor Z.ι) = T → IsProper B S hS (Z.ι ≫ f)
```

## Tag 0CZD, a definition

[Tag 0CZD](https://stacks.math.columbia.edu/tag/0CZD) in the Stacks Project.

**`AlgebraicGeometry.Space.IsProperOver`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperClosedSubset.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperClosedSubset.lean#L60).

> **Stacks 0CZD.** A closed subset of the points of an algebraic space `X` is *proper over
> `Y`* when the reduced induced closed subspace of `X` supported on it is proper over `Y`.

```lean
abbrev IsProperOver (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (_hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (_hf : IsLocallyOfFiniteType B S hS f) (T : Set (points B S hS X))
    (hT : IsClosed T) : Prop
```

## Tag 0CZE, a lemma

[Tag 0CZE](https://stacks.math.columbia.edu/tag/0CZE) in the Stacks Project.

**`AlgebraicGeometry.Space.isProperOver_of_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperClosedSubset.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperClosedSubset.lean#L169).

> **Stacks 0CZE.** A closed subset of a closed subset proper over the base is proper over the
> base.
>
> The reduced closed subspace on the smaller set is a subfunctor of the one on the larger set, so
> the inclusion between them is a closed immersion and hence proper; composing with properness
> over `Y` of the larger one gives the result.

```lean
theorem isProperOver_of_subset (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f)
    (T' T : Set (points B S hS X)) (hT' : _root_.IsClosed T') (hT : _root_.IsClosed T)
    (hsub : T' ⊆ T) (hproper : IsProperOver B S hS hX hY f hf T hT) :
    IsProperOver B S hS hX hY f hf T' hT'
```

## Tag 0CZF, a lemma

[Tag 0CZF](https://stacks.math.columbia.edu/tag/0CZF) in the Stacks Project.

**`AlgebraicGeometry.Space.isProperOver_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubsetBaseChange.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubsetBaseChange.lean#L135). The attribute's comment: “properness”.

> **Stacks 0CZF, properness.** In a cartesian square of algebraic spaces over `S` whose right
> vertical morphism is locally of finite type, the inverse image of a closed subset proper over
> the base is proper over the new base.

```lean
theorem isProperOver_preimage {X' X Y' Y : AlgebraicSpaces B S hS}
    {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y}
    (sq : IsPullback g' f' f g) (hf : IsLocallyOfFiniteType B S hS f.hom)
    (T : Set (points B S hS X.1)) (hT : IsClosed T)
    (hproper : IsProperOver B S hS X.property Y.property f.hom hf T hT) :
    IsProperOver B S hS X'.property Y'.property f'.hom
      ((isLocallyOfFiniteType_isStableUnderBaseChange B S hS).of_isPullback sq hf)
      (pointsMap B S hS X'.1 g'.hom ⁻¹' T)
      (isClosed_preimage_pointsMap B S hS X'.property X.property g'.hom hT)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isClosed_preimage_pointsMap`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullback.lean#L55), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubsetBaseChange.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubsetBaseChange.lean#L79) (StacksFrontier): “closedness”.

## Tag 0CZG, a lemma

[Tag 0CZG](https://stacks.math.columbia.edu/tag/0CZG) in the Stacks Project.

**`AlgebraicGeometry.Space.isClosed_image_of_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubsetImage.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubsetImage.lean#L187). The attribute's comment: “image\_universally\_closed”.

> **Stacks 0CZG, closedness of the image under a universally closed morphism.** A universally
> closed morphism of algebraic spaces over `S` carries closed subsets of its space of points to
> closed subsets: it is closed, by Stacks 03HI.

```lean
theorem isClosed_image_of_universallyClosed (_hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : UniversallyClosed B S hS f)
    (T : Set (points B S hS X)) (hT : IsClosed T) :
    IsClosed (pointsMap B S hS X f '' T)
```

**`AlgebraicGeometry.Space.isProperOver_image_of_universallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubsetImage.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubsetImage.lean#L200). The attribute's comment: “image\_universally\_closed”.

> **Stacks 0CZG, properness of the image under a universally closed morphism.** The image of a
> closed subset proper over the base under a universally closed morphism is proper over the base.
>
> The restriction of a universally closed morphism to the reduced induced subspace is universally
> closed, the inclusion of that subspace being universally closed, so
> `AlgebraicGeometry.Space.isProper_ι_comp_of_universallyClosed_ι_comp` applies.

```lean
theorem isProperOver_image_of_universallyClosed (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (hA : IsAlgebraicSpace B S hS A)
    (f : X ⟶ Y) (g : Y ⟶ A) (hf : UniversallyClosed B S hS f)
    (hXft : IsLocallyOfFiniteType B S hS (f ≫ g))
    (hYft : IsLocallyOfFiniteType B S hS g)
    (T : Set (points B S hS X)) (hT : IsClosed T)
    (hTproper : IsProperOver B S hS hX hA (f ≫ g) hXft T hT) :
    IsProperOver B S hS hY hA g hYft (pointsMap B S hS X f '' T)
      (isClosed_image_of_universallyClosed B S hS hX hY f hf T hT)
```

**`AlgebraicGeometry.Space.isClosed_image_of_isProperOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubsetImage.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubsetImage.lean#L236). The attribute's comment: “image\_separated”.

> **Stacks 0CZG, closedness of the image in a separated target.** If the structure morphism of
> `Y` is separated and the closed subset `T` of the points of `X` is proper over the base, then the
> image of `T` in the points of `Y` is closed.
>
> The reduced induced subspace on `T` is universally closed over the base, so its morphism to `Y`
> is universally closed by Stacks 04NX, the structure morphism of `Y` being separated.

```lean
theorem isClosed_image_of_isProperOver (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (hA : IsAlgebraicSpace B S hS A)
    (f : X ⟶ Y) (pX : X ⟶ A) (pY : Y ⟶ A) (hcomm : f ≫ pY = pX)
    (hpX : IsLocallyOfFiniteType B S hS pX) (_hpY : IsLocallyOfFiniteType B S hS pY)
    (hsep : IsSeparated B S hS pY)
    (T : Set (points B S hS X)) (hT : IsClosed T)
    (hproper : IsProperOver B S hS hX hA pX hpX T hT) :
    IsClosed (pointsMap B S hS X f '' T)
```

**`AlgebraicGeometry.Space.isProperOver_image_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubsetImage.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubsetImage.lean#L256). The attribute's comment: “image\_separated”.

> **Stacks 0CZG, properness of the image in a separated target.** The image in `Y` of a closed
> subset of `X` proper over the base is proper over the base when the structure morphism of `Y` is
> separated.
>
> As for closedness, the reduced induced subspace on `T` is universally closed over `Y` by
> Stacks 04NX, so `AlgebraicGeometry.Space.isProper_ι_comp_of_universallyClosed_ι_comp` applies. The
> closedness of the image is an explicit hypothesis, as `AlgebraicGeometry.Space.IsProperOver` is a
> predicate on closed subsets.

```lean
theorem isProperOver_image_of_isSeparated (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (hA : IsAlgebraicSpace B S hS A)
    (f : X ⟶ Y) (pX : X ⟶ A) (pY : Y ⟶ A) (hcomm : f ≫ pY = pX)
    (hpX : IsLocallyOfFiniteType B S hS pX) (hpY : IsLocallyOfFiniteType B S hS pY)
    (hsep : IsSeparated B S hS pY)
    (T : Set (points B S hS X)) (hT : IsClosed T)
    (hproper : IsProperOver B S hS hX hA pX hpX T hT)
    (hImage : IsClosed (pointsMap B S hS X f '' T)) :
    IsProperOver B S hS hY hA pY hpY (pointsMap B S hS X f '' T) hImage
```

**`AlgebraicGeometry.Space.isProperOver_preimage_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubsetImage.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubsetImage.lean#L280). The attribute's comment: “inverse\_image\_proper”.

> **Stacks 0CZG, properness of the inverse image.** The inverse image of a closed subset
> proper over the base under a proper morphism is proper over the base.

```lean
theorem isProperOver_preimage_of_isProper (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (hA : IsAlgebraicSpace B S hS A)
    (f : X ⟶ Y) (g : Y ⟶ A) (hf : IsProper B S hS f)
    (hXft : IsLocallyOfFiniteType B S hS (f ≫ g))
    (hYft : IsLocallyOfFiniteType B S hS g)
    (T : Set (points B S hS Y)) (hT : IsClosed T)
    (hTproper : IsProperOver B S hS hY hA g hYft T hT) :
    IsProperOver B S hS hX hA (f ≫ g) hXft (pointsMap B S hS X f ⁻¹' T)
      (isClosed_preimage_pointsMap B S hS hX hY f hT)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isClosed_preimage_pointsMap`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Chow/FlatPullback.lean#L55), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubsetImage.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubsetImage.lean#L88) (StacksFrontier).

## Tag 0CZH, a lemma

[Tag 0CZH](https://stacks.math.columbia.edu/tag/0CZH) in the Stacks Project.

**`AlgebraicGeometry.Space.isProperOver_iUnion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubsetUnion.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperClosedSubsetUnion.lean#L228).

> **Stacks 0CZH.** A finite union of closed subsets of the points of `X`, each proper over
> `Y`, is proper over `Y`.

```lean
theorem isProperOver_iUnion {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f)
    {ι : Type v} [Finite ι] (T : ι → Set (points B S hS X))
    (hT : ∀ i, IsClosed (T i))
    (hproper : ∀ i, IsProperOver B S hS hX hY f hf (T i) (hT i)) :
    IsProperOver B S hS hX hY f hf (⋃ i, T i) (isClosed_iUnion_of_finite hT)
```

## Tag 0CZI, a lemma

[Tag 0CZI](https://stacks.math.columbia.edu/tag/0CZI) in the Stacks Project.

**`AlgebraicGeometry.Space.hasProperSupport_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperModuleSupport.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperModuleSupport.lean#L223).

> **Stacks 0CZI.**  Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is
> locally of finite type and let `F` be a finite type quasi-coherent `𝒪_X`-module.  The following
> are equivalent:
>
> 1. the support of `F` is proper over `Y`;
> 2. the scheme-theoretic support of `F`, Stacks 07U1, is proper over `Y`;
> 3. there are a closed subspace `Z ⊆ X` and a finite type quasi-coherent `𝒪_Z`-module `G` with
>    `Z → Y` proper and `(Z → X)_* G = F`.
>
> The support of `F` is closed by Stacks 07TZ, so Definition 0CZD applies to it; the
> scheme-theoretic support is a closed subspace whose set of points is that support by Stacks 07U0
> part (4), so (1) and (2) agree by Stacks 0CZC, which says that properness over the base of a
> closed subspace depends only on its set of points.  (2) implies (3) by the existence clause of
> Stacks 07U0, together with part (3) of the same lemma for finite type of the module.  (3)
> implies (1) because the support of `F` is contained in the set of points of `Z`, which is proper
> over `Y` by Stacks 0CZC, so Stacks 0CZE applies.

```lean
theorem hasProperSupport_tfae (F : Modules.{u, u} B S hS X.1 X.2)
    (hF : F.IsQuasicoherentOnSite) (hFft : SheafOfModules.IsFiniteTypeOnSite F)
    (hft : PresheafOfModules.IsFiniteType (smallEtaleRingedSite B S hS X.1 X.2).J F.val) :
    List.TFAE
      [HasProperSupport B S hS X.2 Y.2 f hf ((SheafOfModules.toSheaf _).obj F),
        IsProper B S hS ((schemeTheoreticSupport B S hS X F).ι ≫ f),
        ∃ (Z : ClosedSubspaces B S hS X.1)
          (G : Modules.{u, u} B S hS (closedSubspaceToSpace B S hS X Z).1
            (closedSubspaceToSpace B S hS X Z).2),
          G.IsQuasicoherentOnSite ∧ SheafOfModules.IsFiniteTypeOnSite G ∧
            IsProper B S hS (Z.1.ι ≫ f) ∧
            Nonempty ((modulePushforward B S hS
              (closedSubspaceInclusion B S hS X Z)).obj G ≅ F)]
```

## Tag 0CZJ, a lemma

[Tag 0CZJ](https://stacks.math.columbia.edu/tag/0CZJ) in the Stacks Project.

**`AlgebraicGeometry.Space.isProperOver_supportOfSheaf_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Properness/ModuleSupportProperBaseChange.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ModuleSupportProperBaseChange.lean#L60).

> In a cartesian square of algebraic spaces over `S` whose right vertical morphism `f` is
> locally of finite type, the support of the pullback along the upper horizontal morphism of a
> finite type, quasi-coherent `𝒪_X`-module whose support is proper over `Y` is proper over `Y'`.
> It takes the quasi-coherence of `F` (`_hqc`), its finite type (`hft`) and the properness of its
> support over `Y` (`hproper`) as hypotheses.

```lean
theorem isProperOver_supportOfSheaf_modulePullback {X' X Y' Y : AlgebraicSpaces B S hS}
    {g' : X' ⟶ X} {f' : X' ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y}
    (sq : IsPullback g' f' f g) (hf : IsLocallyOfFiniteType B S hS f.hom)
    (F : Modules.{u, u} B S hS X.1 X.2)
    (_hqc : SheafOfModules.IsQuasicoherentOnSite F)
    (hft : SheafOfModules.IsFiniteTypeOnSite F)
    (hproper : IsProperOver B S hS X.property Y.property f.hom hf
      (supportOfSheaf B S hS X.1 ((SheafOfModules.toSheaf _).obj F))
      (letI := hft; isClosed_supportOfSheaf_of_isFiniteTypeOnSite B S hS X.1 X.property F)) :
    IsProperOver B S hS X'.property Y'.property f'.hom
      ((isLocallyOfFiniteType_isStableUnderBaseChange B S hS).of_isPullback sq hf)
      (supportOfSheaf B S hS X'.1
        ((SheafOfModules.toSheaf _).obj ((modulePullback B S hS g').obj F)))
      (isClosed_supportOfSheaf_modulePullback B S hS g' F hft)
```

## Tag 0CZK, a lemma

[Tag 0CZK](https://stacks.math.columbia.edu/tag/0CZK) in the Stacks Project.

**`AlgebraicGeometry.Space.hasProperSupport_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicSystemProperSupport.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/CoherentAdicSystemProperSupport.lean#L108). The attribute's comment: “part (1), quotients”.

> **Stacks 0CZK, part (1), the quotient clause.** A quotient of an `𝒪_X`-module of finite
> type whose support is proper over `Y` again has support proper over `Y`.
>
> The quotient is of finite type by Stacks 03DL(5), so its support is closed by Stacks 07TZ; an
> epimorphism of sheaves of modules is a local surjection, so that support is contained in the
> support of the source by Stacks 04KB(5); and a closed subset of a closed subset proper over the
> base is proper over the base by Stacks 0CZE.

```lean
theorem hasProperSupport_of_epi (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f)
    {M N : Modules.{u, u} B S hS X hX} (p : M ⟶ N) [Epi p]
    (hMft : SheafOfModules.IsFiniteTypeOnSite M)
    (hM : HasProperSupport B S hS hX hY f hf ((SheafOfModules.toSheaf _).obj M)) :
    HasProperSupport B S hS hX hY f hf ((SheafOfModules.toSheaf _).obj N)
```

**`AlgebraicGeometry.Space.hasProperSupport_toSheaf_of_sectionwiseSplit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperSupport.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperSupport.lean#L225). The attribute's comment: “part (1), direct sums”.

> **Stacks 0CZK, part (1), the direct sum clause.** A direct sum of two `𝒪_X`-modules whose
> supports are proper over `Y` again has support proper over `Y`.
>
> The support of a module is the support of its underlying abelian sheaf, and the two inclusions,
> the two projections and the three identities they satisfy on sections carry over to the
> underlying abelian sheaves unchanged, so this is
> `AlgebraicGeometry.Space.hasProperSupport_of_sectionwiseSplit` read off the sections of the
> modules.

```lean
theorem hasProperSupport_toSheaf_of_sectionwiseSplit (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f)
    {P M N : Modules.{u, v} B S hS X hX}
    (i₁ : M ⟶ P) (i₂ : N ⟶ P) (p₁ : P ⟶ M) (p₂ : P ⟶ N)
    (hi₁ : ∀ (U : SmallEtale B S hS X) (σ : M.val.obj (op U)),
      p₁.val.app (op U) (i₁.val.app (op U) σ) = σ)
    (hi₂ : ∀ (U : SmallEtale B S hS X) (σ : N.val.obj (op U)),
      p₂.val.app (op U) (i₂.val.app (op U) σ) = σ)
    (htotal : ∀ (U : SmallEtale B S hS X) (τ : P.val.obj (op U)),
      i₁.val.app (op U) (p₁.val.app (op U) τ) +
        i₂.val.app (op U) (p₂.val.app (op U) τ) = τ)
    (hM : HasProperSupport B S hS hX hY f hf ((SheafOfModules.toSheaf _).obj M))
    (hN : HasProperSupport B S hS hX hY f hf ((SheafOfModules.toSheaf _).obj N)) :
    HasProperSupport B S hS hX hY f hf ((SheafOfModules.toSheaf _).obj P)
```

**`AlgebraicGeometry.Space.hasProperSupport_X₂_of_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperSupportSerre.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperSupportSerre.lean#L163). The attribute's comment: “part (1), extensions”.

> **Stacks 0CZK, part (1), the extension clause.**  An extension of `𝒪_X`-modules whose
> supports are proper over `Y` again has support proper over `Y`: the middle term of a short exact
> sequence of `𝒪_X`-modules whose outer terms have support proper over `Y` has support proper
> over `Y`.
>
> The support of the middle term is *exactly* the union of the supports of the outer two.  It is
> contained in that union by
> `AlgebraicGeometry.Space.supportOfSheaf_middle_subset_union`; it contains the support of the
> first term because the first map is a monomorphism and the support of the third because the
> second map is an epimorphism, hence a local surjection, which are the two halves of Stacks
> 04KB.  So the support is closed, being a union of two closed supports, and a finite union of
> closed subsets proper over `Y` is proper over `Y` by Stacks 0CZH.
>
> No finiteness hypothesis appears: as for a direct sum, the containment of supports is an
> equality, so closedness of the support of the extension comes from the two given supports and
> not from the finite type closure of Stacks 05VR.

```lean
theorem hasProperSupport_X₂_of_shortExact (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f)
    {T : ShortComplex (Modules.{u, u} B S hS X hX)} (hT : T.ShortExact)
    (h₁ : HasProperSupport B S hS hX hY f hf ((SheafOfModules.toSheaf _).obj T.X₁))
    (h₃ : HasProperSupport B S hS hX hY f hf ((SheafOfModules.toSheaf _).obj T.X₃)) :
    HasProperSupport B S hS hX hY f hf ((SheafOfModules.toSheaf _).obj T.X₂)
```

**`AlgebraicGeometry.Space.hasProperSupport_cokernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperSupportSerre.lean, line 201](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperSupportSerre.lean#L201). The attribute's comment: “part (1), cokernels”.

> **Stacks 0CZK, part (1), the cokernel clause.**  The cokernel of a map `u : M ⟶ N` of
> `𝒪_X`-modules whose target is of finite type and has support proper over `Y` again has support
> proper over `Y`.
>
> The cokernel is a quotient of `N`, so this is the quotient clause
> `AlgebraicGeometry.Space.hasProperSupport_of_epi`.  Stacks 0CZK assumes proper support of both
> `M` and `N`; the source of `u` plays no part.

```lean
theorem hasProperSupport_cokernel (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f)
    {M N : Modules.{u, u} B S hS X hX} (u : M ⟶ N)
    (hNft : SheafOfModules.IsFiniteTypeOnSite N)
    (hN : HasProperSupport B S hS hX hY f hf ((SheafOfModules.toSheaf _).obj N)) :
    HasProperSupport B S hS hX hY f hf ((SheafOfModules.toSheaf _).obj
      (cokernel (C := Modules.{u, u} B S hS X hX) u))
```

**`AlgebraicGeometry.Space.hasProperSupport_abelianImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperSupportSerre.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperSupportSerre.lean#L222). The attribute's comment: “part (1), images”.

> **Stacks 0CZK, part (1), the image clause.**  The image of a map `u : M ⟶ N` of
> `𝒪_X`-modules whose source is of finite type and has support proper over `Y` again has support
> proper over `Y`.
>
> `CategoryTheory.Abelian.coimage u` is by definition `cokernel (kernel.ι u)`, hence a quotient of
> `M`, so it has support proper over `Y` by the quotient clause
> `AlgebraicGeometry.Space.hasProperSupport_of_epi`; and
> `CategoryTheory.Abelian.coimageIsoImage` identifies it with the image, whose support is
> therefore the same by Stacks 04KB.  Stacks 0CZK assumes proper support of both `M` and `N`; the
> target of `u` plays no part.

```lean
theorem hasProperSupport_abelianImage (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f)
    {M N : Modules.{u, u} B S hS X hX} (u : M ⟶ N)
    (hMft : SheafOfModules.IsFiniteTypeOnSite M)
    (hM : HasProperSupport B S hS hX hY f hf ((SheafOfModules.toSheaf _).obj M)) :
    HasProperSupport B S hS hX hY f hf ((SheafOfModules.toSheaf _).obj
      (Abelian.image (C := Modules.{u, u} B S hS X hX) u))
```

**`AlgebraicGeometry.Space.isSerreClass_isCoherentProperOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperSupportSerre.lean, line 259](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Properness/ProperSupportSerre.lean#L259). The attribute's comment: “part (2), the Serre subcategory; the locally Noetherian hypothesis on Y is absent because the abelian structure on Coh(O\_X) is Stacks 07UC in the hypothesis-free form `AlgebraicGeometry.Space.coherentModules_abelian_of_closure`”.

> **Stacks 0CZK, part (2).**  The coherent `𝒪_X`-modules whose support is proper over `Y`
> form a Serre subcategory of the abelian category `Coh(𝒪_X)` of coherent `𝒪_X`-modules.
>
> The property is `AlgebraicGeometry.Space.isCoherentProperOver`, the one cutting out the source
> of equation 76.42.5.1, and the abelian structure on `Coh(𝒪_X)` is Stacks 07UC in the form
> `AlgebraicGeometry.Space.coherentModules_abelian_of_closure`, which needs no locally Noetherian
> hypothesis in this tree; the hypothesis of the source is therefore absent.
>
> By Stacks 02MP it is enough to exhibit one object with the property and to show that the middle
> term of an exact sequence whose outer terms have the property has it.  The zero module has
> empty support.  For the exactness condition: the kernel `K` of `T.X₂ ⟶ T.X₃`, formed in the
> ambient category of all `𝒪_X`-modules, is a quotient of `T.X₁` because the sequence is exact,
> so it has support proper over `Y` by the quotient clause of part (1); the support of `T.X₂` is
> contained in the union of the support of `K` and the support of `T.X₃`, by
> `AlgebraicGeometry.Space.supportOfSheaf_subset_union_kernel`; and the support of `T.X₂` is
> closed because a coherent module is of finite type, by Stacks 07TZ.  Stacks 0CZH and 0CZE then
> finish, in the form `AlgebraicGeometry.Space.hasProperSupport_of_subset_union`.

```lean
theorem isSerreClass_isCoherentProperOver (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f) :
    letI : Abelian (CoherentModules.{u, u} B S hS X hX) :=
      coherentModules_abelian_of_closure B S hS X hX
    (isCoherentProperOver B S hS hX hY f hf).IsSerreClass
```

## Tag 08GC, a lemma

[Tag 08GC](https://stacks.math.columbia.edu/tag/08GC) in the Stacks Project.

**`AlgebraicGeometry.Space.isCoherent_rightDerived_modulePushforward_of_hasProperSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperSupportCoherentPushforward.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperSupportCoherentPushforward.lean#L206). The attribute's comment: “granted three named hypotheses, none of them this conclusion. (1) h08AR, Stacks 08AR itself — coherence of the higher direct images of a coherent module along a proper morphism to Y — which has no presence in this library, nor has its scheme-level counterpart Stacks 02O5, the dévissage for coherent modules, Chow's lemma and the vanishing for relatively ample invertible sheaves that would prove it all being absent; it is carried in its own shape, with the module coherent and the conclusion coherent. (2) h0734, the degeneration of the relative Leray spectral sequence of Stacks 0734 that the source's last step is, namely R^p f\_*(i\_* G) = R^p (f ∘ i)\_* G when the higher direct images along i vanish; the formalized Stacks 0734 is stated for ringed topoi with all three universes equal and the small étale ringed topos of an algebraic space is RingedTopos u (u+1) u, so it does not apply, and the vanishing that h0734 asks for is discharged here from Stacks 07UH. (3) h03DW, the étale-affine case of Stacks 03DW, which is the hypothesis of the vanishing half of the formalized Stacks 07UH and is quoted in the form that lemma takes it. Stacks 0CZI, Stacks 07UH, Stacks 081Y, Stacks 04ZK and the coherence step of Stacks 07UG are applied and not assumed, so the source's hypotheses are all consumed: proper support is the input of Stacks 0CZI, and f locally of finite type together with Y locally Noetherian give local Noetherianity of X by Stacks 04ZK, which is what makes the module of Stacks 0CZI coherent”.

> **Stacks 08GC.**  Let `S` be a scheme, let `f : X ⟶ Y` be a morphism of algebraic spaces
> over `S` which is locally of finite type with `Y` locally Noetherian, and let `𝓕` be a coherent
> `𝒪_X`-module whose support is proper over `Y`.  Then `R^p f_*𝓕` is a coherent `𝒪_Y`-module for
> every `p`.
>
> The proof is the source's.  Properness of the support feeds Stacks 0CZI,
> `AlgebraicGeometry.Space.hasProperSupport_tfae`, whose third condition produces a closed
> subspace `Z ⊆ X` proper over `Y` and a quasi-coherent `𝒪_Z`-module `𝓖` of finite type with
> `i_*𝓖 ≅ 𝓕`, where `i : Z → X` is the inclusion; `𝓖` is coherent because `X` is locally
> Noetherian by Stacks 04ZK, which is where `hf` and `hY` are used, so that the step of
> Stacks 07UG applies.  A closed immersion is finite by Stacks 081Y, so the higher direct images
> along `i` vanish by the vanishing half of Stacks 07UH; `h0734` then identifies `R^p f_*(i_*𝓖)`
> with `R^p (i ≫ f)_*𝓖`, which `h08AR` makes coherent, and coherence transports along the two
> isomorphisms because it is invariant under isomorphism of modules.
>
> The three carried inputs are `h03DW`, the input of the vanishing half of Stacks 07UH; `h08AR`,
> Stacks 08AR; and `h0734`, the degeneration of the relative Leray spectral sequence.  See the
> module documentation for each.

```lean
theorem isCoherent_rightDerived_modulePushforward_of_hasProperSupport
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f.hom)
    (hY : HasEtaleLocalProperty B S hS Y.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : IsCoherent B S hS X.1 X.2 F)
    (hsupp : HasProperSupport B S hS X.2 Y.2 f.hom hf ((SheafOfModules.toSheaf _).obj F))
    (h03DW : ∀ (Z : ClosedSubspaces B S hS X.1)
      (hrep : yoneda.relativelyRepresentable (closedSubspaceInclusion B S hS X Z).hom)
      (G : Modules.{u, u} B S hS (closedSubspaceToSpace B S hS X Z).1
        (closedSubspaceToSpace B S hS X Z).2) (n : ℕ),
      ChartwiseIsZeroHigherDirectImage B S hS (closedSubspaceInclusion B S hS X Z) hrep G n)
    (h08AR : CoherentHigherDirectImageOfProper B S hS Y)
    (h0734 : HigherDirectImageCompOfAcyclic B S hS f) (p : ℕ) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    IsCoherent B S hS Y.1 Y.2 (((modulePushforward B S hS f).rightDerived p).obj F)
```

**`AlgebraicGeometry.Space.isCoherent_higherDirectImage_of_hasProperSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperSupportHigherDirectImageCoherence.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperSupportHigherDirectImageCoherence.lean#L155). References: EGA III (3.2.1), “more general”; EGA III (4.1.10), “more general”.

> **Stacks 08GC.**  Let `S` be a scheme, let `f : X ⟶ Y` be a morphism of algebraic spaces
> over `S` which is locally of finite type with `Y` locally Noetherian, and let `𝓕` be a coherent
> `𝒪_X`-module whose support is proper over `Y`.  Then `R^p f_*𝓕` is a coherent `𝒪_Y`-module for
> every `p`.
>
> By `AlgebraicGeometry.Space.exists_closedSubspace_higherDirectImage_iso`,
> `R^p f_*𝓕 ≅ R^p (i ≫ f)_*𝓖` for a closed subspace `i : Z → X` proper over `Y` and a coherent
> `𝒪_Z`-module `𝓖`; that is coherent by Stacks 08AR.

```lean
theorem isCoherent_higherDirectImage_of_hasProperSupport (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f.hom)
    (hY : HasEtaleLocalProperty B S hS Y.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : IsCoherent B S hS X.1 X.2 F)
    (hsupp : HasProperSupport B S hS X.2 Y.2 f.hom hf ((SheafOfModules.toSheaf _).obj F))
    (p : ℕ) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    IsCoherent B S hS Y.1 Y.2 (((modulePushforward B S hS f).rightDerived p).obj F)
```

**`AlgebraicGeometry.Space.isCoherent_rightDerived_modulePushforward_of_properSupport`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperSupportHigherDirectImageCoherent.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Perfect/ProperSupportHigherDirectImageCoherent.lean#L49).

> Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is locally of finite type,
> with `Y` locally Noetherian, and let `𝓕` be a coherent `𝒪_X`-module with support proper over
> `Y`. Then `R^p f_*𝓕` is a coherent `𝒪_Y`-module for every `p`.

```lean
theorem isCoherent_rightDerived_modulePushforward_of_properSupport
    {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f.hom)
    (hY : HasEtaleLocalProperty B S hS Y.1 (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (F : Modules.{u, u} B S hS X.1 X.2) (hF : IsCoherent B S hS X.1 X.2 F)
    (hsupp : HasProperSupport B S hS X.2 Y.2 f.hom hf ((SheafOfModules.toSheaf _).obj F))
    (p : ℕ) :
    have := hasInjectiveResolutions_modules B S hS X.1 X.2
    IsCoherent B S hS Y.1 Y.2 (((modulePushforward B S hS f).rightDerived p).obj F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 75.7, Tag 0CZB](https://stacks.math.columbia.edu/tag/0CZB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
