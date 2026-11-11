---
declaration: section
origin: cited
lean: AlgebraicGeometry.isIso_changeBigSiteYonedaHom, AlgebraicGeometry.changeBigSiteYonedaIso, AlgebraicGeometry.isAlgebraicSpace_sheafPullback, sheafPullback_sheafify_yoneda_natIso, AlgebraicGeometry.changeBigSiteSheafPullback_fullyFaithful, AlgebraicGeometry.changeBigSite, AlgebraicGeometry.changeBigSite_fullyFaithful, AlgebraicGeometry.mem_essentialImage_changeBigSite_iff
statement: formalized
proof: formalized
---

# 65.15 Change of big site

Section 65.15 of the Stacks Project, [Tag 03FO](https://stacks.math.columbia.edu/tag/03FO). 2 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03FP, a lemma

[Tag 03FP](https://stacks.math.columbia.edu/tag/03FP) in the Stacks Project.

**`AlgebraicGeometry.isIso_changeBigSiteYonedaHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChangeOfBigSiteRepresentable.lean, line 148](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ChangeOfBigSiteRepresentable.lean#L148). The attribute's comment: “part (1), canonically”.

> **Stacks 03FP, part (1), for the canonical comparison.** The inverse image of the sheaf
> represented by a test object of the smaller localized big fppf site is the sheaf represented by
> its image, by the comparison determined by the transport of the identity.
>
> The isomorphism of Stacks 03FP, part (1) is only produced as *some* isomorphism, so it cannot be
> evaluated on sections. The argument transfers invertibility to the canonical comparison: the two
> differ by precomposition with a morphism of the enlarged site, because a map out of a
> representable sheaf is its own Yoneda transpose; that morphism is invertible because the canonical
> comparison is bijective on sections over the image of the test object, where the chosen
> isomorphism is bijective as well; and precomposition with an invertible morphism preserves
> invertibility.

```lean
theorem isIso_changeBigSiteYonedaHom (T : BigFppfOver B S hS) :
    IsIso (changeBigSiteYonedaHom B B' h S hS T)
```

**`AlgebraicGeometry.changeBigSiteYonedaIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChangeOfBigSiteRepresentable.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ChangeOfBigSiteRepresentable.lean#L183). The attribute's comment: “part (1), canonically”.

> **The inverse image of a representable algebraic space is represented by the image of the
> test object**, by the canonical comparison of
> `AlgebraicGeometry.changeBigSiteYonedaHom`.

```lean
def changeBigSiteYonedaIso (T : BigFppfOver B S hS) :
    yoneda.obj ((inclusionOver h S hS).obj T) ≅
      ((changeBigSite B B' h S hS).obj ((schemeSpaceFunctor B S hS).obj T)).obj
```

**`AlgebraicGeometry.isAlgebraicSpace_sheafPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChangeOfBigSiteUnconditional.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ChangeOfBigSiteUnconditional.lean#L118). The attribute's comment: “part (2)”.

> **Stacks 03FP, part (2).** Enlarging the big fppf site preserves algebraic spaces over the
> base scheme: the inverse image of an algebraic space over `S` on the smaller localized site is an
> algebraic space over `S` on the larger one.
>
> This is `AlgebraicGeometry.isAlgebraicSpace_sheafPullback_of_descent` with its descent hypothesis
> discharged by `AlgebraicGeometry.descentForQuotients`.

```lean
theorem isAlgebraicSpace_sheafPullback
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F) :
    letI J := overTopology .fppf B S hS
    letI K := overTopology .fppf B' S (largerContains h hS)
    letI i := inclusionOver h S hS
    letI : i.IsContinuous J K :=
      (inclusionOver_isMorphismOfSites (τ := .fppf) B B' h S hS).toIsContinuous
    letI : (i.sheafPushforwardContinuous (Type u) J K).IsRightAdjoint :=
      inclusionOver_sheafPushforwardContinuous_isRightAdjoint B B' h S hS
    IsAlgebraicSpace B' S (largerContains h hS)
      ((i.sheafPullback (Type u) J K).obj ⟨F, hF.isSheaf⟩).obj
```

Declarations registered for the tag:

- [`sheafPullback_sheafify_yoneda_natIso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Continuous/PullbackOfRepresentable.lean#L219), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/ChangeOfBigSite.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ChangeOfBigSite.lean#L73) (StacksFrontier): “part (1), canonical naturality”.
- [`sheafPullback_sheafify_yoneda_natIso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Continuous/PullbackOfRepresentable.lean#L219), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Continuous/PullbackOfRepresentable.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Continuous/PullbackOfRepresentable.lean#L257) (StacksFrontier): “part (1), canonical naturality”.

## Tag 04W1, a lemma

[Tag 04W1](https://stacks.math.columbia.edu/tag/04W1) in the Stacks Project.

**`AlgebraicGeometry.changeBigSiteSheafPullback_fullyFaithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChangeOfBigSiteFullyFaithful.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ChangeOfBigSiteFullyFaithful.lean#L118). The attribute's comment: “full faithfulness, for the sheaf-valued inverse image”.

> **Stacks 04W1, full faithfulness**, with no descent hypothesis. Inverse image along the
> inclusion of localized big fppf sites is fully faithful on the algebraic spaces over `S` defined
> using the smaller site, as a functor into the sheaves on the larger site.

```lean
theorem changeBigSiteSheafPullback_fullyFaithful :
    Nonempty (changeBigSiteSheafPullback B B' h S hS).FullyFaithful
```

**`AlgebraicGeometry.changeBigSite`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChangeOfBigSiteUnconditional.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ChangeOfBigSiteUnconditional.lean#L164). The attribute's comment: “the functor”.

> **Stacks 04W1, the functor.** Inverse image along the inclusion of localized big fppf sites,
> as a functor from the algebraic spaces over `S` defined using the smaller site to those defined
> using the larger one, with no hypothesis.
>
> This is `AlgebraicGeometry.changeBigSiteOfDescent` with its descent hypothesis discharged by
> `AlgebraicGeometry.descentForQuotients`.

```lean
def changeBigSite :
    AlgebraicSpaces B S hS ⥤ AlgebraicSpaces B' S (largerContains h hS)
```

**`AlgebraicGeometry.changeBigSite_fullyFaithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChangeOfBigSiteUnconditional.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ChangeOfBigSiteUnconditional.lean#L176). The attribute's comment: “full faithfulness”.

> **Stacks 04W1, full faithfulness.** Inverse image along the inclusion of localized big fppf
> sites is fully faithful as a functor on the algebraic spaces over `S`.
>
> This is `AlgebraicGeometry.changeBigSiteOfDescent_fullyFaithful` with its descent hypothesis
> discharged. It is the statement of 04W1 proper, where
> `AlgebraicGeometry.changeBigSiteSheafPullback_fullyFaithful` is the same conclusion for the
> functor valued in sheaves on the larger site.

```lean
theorem changeBigSite_fullyFaithful :
    Nonempty (changeBigSite B B' h S hS).FullyFaithful
```

**`AlgebraicGeometry.mem_essentialImage_changeBigSite_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChangeOfBigSiteUnconditional.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ChangeOfBigSiteUnconditional.lean#L228). The attribute's comment: “the essential image”.

> **Stacks 04W1, the essential image.** An algebraic space on the enlarged big fppf site
> descends precisely when an object of the smaller site surjects onto it as a map of sheaves and
> another object of the smaller site surjects onto the kernel pair of that surjection.
>
> This is `AlgebraicGeometry.mem_essentialImage_changeBigSiteOfDescent_iff` with both descent
> hypotheses discharged.

```lean
theorem mem_essentialImage_changeBigSite_iff
    (X' : AlgebraicSpaces B' S (largerContains h hS)) :
    (∃ X : AlgebraicSpaces B S hS,
      Nonempty ((changeBigSite B B' h S hS).obj X ≅ X')) ↔
      (letI K := BigFppfOver.topology B' S (largerContains h hS)
       let i := inclusionOver h S hS
       ∃ (U R : BigFppfOver B S hS) (f : yoneda.obj (i.obj U) ⟶ X'.obj)
         (g : yoneda.obj (i.obj R) ⟶ pullback f f),
         Presheaf.IsLocallySurjective K f ∧ Presheaf.IsLocallySurjective K g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 65.15, Tag 03FO](https://stacks.math.columbia.edu/tag/03FO)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
