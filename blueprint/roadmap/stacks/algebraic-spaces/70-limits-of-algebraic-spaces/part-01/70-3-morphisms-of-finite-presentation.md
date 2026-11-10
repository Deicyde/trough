---
declaration: section
origin: cited
lean: AlgebraicGeometry.LimitPreserving, AlgebraicGeometry.RelativelyLimitPreserving, AlgebraicGeometry.isPullback_sectionFiberι, AlgebraicGeometry.relativelyLimitPreserving_iff_affineLimit_isPullback, AlgebraicGeometry.relativelyLimitPreserving_comp, AlgebraicGeometry.relativelyLimitPreserving_of_comp_of_right, AlgebraicGeometry.relativelyLimitPreserving_pullback_fst, AlgebraicGeometry.relativelyLimitPreserving_pullback
statement: formalized
proof: formalized
---

# 70.3 Morphisms of finite presentation

Section 70.3 of the Stacks Project, [Tag 049I](https://stacks.math.columbia.edu/tag/049I). 13 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 049J, a definition

[Tag 049J](https://stacks.math.columbia.edu/tag/049J) in the Stacks Project.

**`AlgebraicGeometry.LimitPreserving`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/LimitPreserving.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/LimitPreserving.lean#L49). The attribute's comment: “part (1)”. References: SGA 3 XI (3.2), “definition of (*)”.

> **Stacks Project, Tag 049J.** A presheaf of sets preserves inverse limits of affine
> schemes as filtered colimits of sets, relative to its underlying-scheme functor.

```lean
abbrev LimitPreserving {C : Type z} [Category C]
    (toScheme : C ⥤ Scheme.{u}) (F : Cᵒᵖ ⥤ Type v) : Prop
```

**`AlgebraicGeometry.RelativelyLimitPreserving`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/LimitPreserving.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/LimitPreserving.lean#L78). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 049J.** A transformation is relatively limit preserving when the
> presheaf of lifts of every target section is limit preserving over that section's base.

```lean
abbrev RelativelyLimitPreserving
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type v}
    (a : F ⟶ G) : Prop
```

## Tag 049K, an equation

[Tag 049K](https://stacks.math.columbia.edu/tag/049K) in the Stacks Project.

**`AlgebraicGeometry.isPullback_sectionFiberι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/SectionFiber.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/SectionFiber.lean#L121).

> **Stacks Project, Tag 049K.** The presheaf of lifts of a section `y` of `G` over `X` through
> a transformation `a : F ⟶ G` of presheaves of sets on the big fppf site over `S` is the fibre
> product
>
> ```text
>   F_y = F|_{(Sch/X)_fppf} ×_{G|_{(Sch/X)_fppf}} *
> ```
>
> of presheaves on the big fppf site over `X`, where `*` is the final presheaf and the morphism
> `* ⟶ G|_{(Sch/X)_fppf}` is the point named by `y`. That is, the inclusion of the fibre into the
> restriction of `F` along the localization functor and its structural morphism to the final
> presheaf exhibit it as the fibre product of the restriction of `a` and of that point.

```lean
theorem isPullback_sectionFiberι :
    IsPullback (sectionFiberι B S hS a X y) (sectionFiberToFinal B S hS a X y)
      (Functor.whiskerLeft (Over.forget X).op a) (pointOfSection B S hS G X y)
```

## Tag 06BC, a lemma

[Tag 06BC](https://stacks.math.columbia.edu/tag/06BC) in the Stacks Project.

**`AlgebraicGeometry.relativelyLimitPreserving_iff_affineLimit_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/AffineCriterion.lean, line 563](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/AffineCriterion.lean#L563).

> The affine-limit comparison square characterizes relative limit
> preservation of a transformation of presheaves.

```lean
public theorem relativelyLimitPreserving_iff_affineLimit_isPullback
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type v}
    (a : F ⟶ G) :
    RelativelyLimitPreserving.{u, v, max w w', w'} B S hS a ↔
      ∀ (I : Type (max w w')) [Category.{w'} I] [IsCofiltered I]
        (D : I ⥤ BigFppfOver B S hS) (c : Cone D),
        IsLimit ((BigFppfOver.toScheme B S hS).mapCone c) →
        (∀ i, IsAffine ((BigFppfOver.toScheme B S hS).obj (D.obj i))) →
        IsAffine ((BigFppfOver.toScheme B S hS).obj c.pt) →
          let U := CategoryTheory.uliftFunctor.{max w w', v}
          let F' := F ⋙ U
          let G' := G ⋙ U
          IsPullback
            (colimit.desc (D.op ⋙ F') (F'.mapCocone c.op))
            (colimMap (Functor.whiskerLeft D.op (Functor.whiskerRight a U)))
            (U.map (a.app (Opposite.op c.pt)))
            (colimit.desc (D.op ⋙ G') (G'.mapCocone c.op))
```

## Tag 049L, a lemma

[Tag 049L](https://stacks.math.columbia.edu/tag/049L) in the Stacks Project.

**`AlgebraicGeometry.relativelyLimitPreserving_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/Sorites.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/Sorites.lean#L45).

> The composition of two relatively limit-preserving transformations is
> relatively limit preserving.

```lean
public theorem relativelyLimitPreserving_comp
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type v}
    (a : F ⟶ G) (b : G ⟶ H)
    (ha : RelativelyLimitPreserving.{u, v, max w w', w'} B S hS a)
    (hb : RelativelyLimitPreserving.{u, v, max w w', w'} B S hS b) :
    RelativelyLimitPreserving.{u, v, max w w', w'} B S hS (a ≫ b)
```

## Tag 0GDY, a lemma

[Tag 0GDY](https://stacks.math.columbia.edu/tag/0GDY) in the Stacks Project.

**`AlgebraicGeometry.relativelyLimitPreserving_of_comp_of_right`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/Sorites.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/Sorites.lean#L74).

> If `b` and `a ≫ b` preserve limits relatively, then so does `a`.

```lean
public theorem relativelyLimitPreserving_of_comp_of_right
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type v}
    (a : F ⟶ G) (b : G ⟶ H)
    (hba : RelativelyLimitPreserving.{u, v, w, w'} B S hS (a ≫ b))
    (hb : RelativelyLimitPreserving.{u, v, w, w'} B S hS b) :
    RelativelyLimitPreserving.{u, v, w, w'} B S hS a
```

## Tag 049M, a lemma

[Tag 049M](https://stacks.math.columbia.edu/tag/049M) in the Stacks Project.

**`AlgebraicGeometry.relativelyLimitPreserving_pullback_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/FibreProducts.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/FibreProducts.lean#L169).

> A relatively limit-preserving transformation of presheaves remains so
> after pullback along any transformation.

```lean
public theorem relativelyLimitPreserving_pullback_fst
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type v}
    (a : F ⟶ G) (b : H ⟶ G)
    (ha : RelativelyLimitPreserving.{u, v, w, w'} B S hS a) :
    RelativelyLimitPreserving.{u, v, w, w'} B S hS
      (pullback.fst b a)
```

## Tag 0GDZ, a lemma

[Tag 0GDZ](https://stacks.math.columbia.edu/tag/0GDZ) in the Stacks Project.

**`AlgebraicGeometry.relativelyLimitPreserving_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/FibreProducts.lean, line 364](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/FibreProducts.lean#L364).

> Relative limit preservation is stable under a fibre product of presheaves
> over a common intermediate presheaf.

```lean
public theorem relativelyLimitPreserving_pullback
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {E F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type v}
    (a : F ⟶ G) (b : H ⟶ G) (c : G ⟶ E)
    (hc : RelativelyLimitPreserving.{u, v, w, w'} B S hS c)
    (hca : RelativelyLimitPreserving.{u, v, w, w'} B S hS (a ≫ c))
    (hcb : RelativelyLimitPreserving.{u, v, w, w'} B S hS (b ≫ c)) :
    RelativelyLimitPreserving.{u, v, w, w'} B S hS
      (pullback.fst a b ≫ a ≫ c)
```

## Tag 049O, a lemma

[Tag 049O](https://stacks.math.columbia.edu/tag/049O) in the Stacks Project.

**`AlgebraicGeometry.limitPreserving_of_isLocallyBijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/Sheafify.lean, line 988](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/Sheafify.lean#L988). The attribute's comment: “locally bijective comparison”.

> An fppf sheaf receiving a locally bijective map from a limit-preserving presheaf is
> limit preserving. Local injectivity makes sections that agree at the limit agree at a later
> stage, and local surjectivity puts every section of the sheaf at a finite stage.

```lean
public theorem limitPreserving_of_isLocallyBijective [UnivLE.{max w w', u}]
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type v} (η : F ⟶ G)
    [Presheaf.IsLocallySurjective (BigFppfOver.topology B S hS) η]
    [Presheaf.IsLocallyInjective (BigFppfOver.topology B S hS) η]
    (hG : Presheaf.IsSheaf (BigFppfOver.topology B S hS) G)
    (hF : LimitPreserving.{u, v, w, w', u + 1} (BigFppfOver.toScheme B S hS) F) :
    LimitPreserving.{u, v, w, w', u + 1} (BigFppfOver.toScheme B S hS) G
```

**`AlgebraicGeometry.limitPreserving_sheafify`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/Sheafify.lean, line 1012](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/Sheafify.lean#L1012).

> Fppf sheafification of a limit-preserving presheaf is limit preserving.

```lean
public theorem limitPreserving_sheafify [UnivLE.{max w w', u}]
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type (max (u + 1) v))
    (hF : LimitPreserving.{u, max (u + 1) v, w, w', u + 1}
      (BigFppfOver.toScheme B S hS) F) :
    LimitPreserving.{u, max (u + 1) v, w, w', u + 1}
      (BigFppfOver.toScheme B S hS)
      ((BigFppfOver.topology B S hS).sheafify F)
```

## Tag 049P, a lemma

[Tag 049P](https://stacks.math.columbia.edu/tag/049P) in the Stacks Project.

**`AlgebraicGeometry.limitPreserving_of_fppfCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/FppfLocal.lean, line 532](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/FppfLocal.lean#L532).

> Limit preservation for an fppf sheaf can be checked on an fppf cover of
> the base scheme.

```lean
public theorem limitPreserving_of_fppfCover
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type v)
    (hF : Presheaf.IsSheaf (BigFppfOver.topology B S hS) F)
    (E : PreZeroHypercover.{u + 1} (B.obj hS))
    (hE : IsFppfCovering ⟨B.obj hS, E⟩)
    (hlocal : ∀ i : E.I₀,
      LimitPreserving.{u, v, w, w', u + 1}
        (Over.forget (E.X i) ⋙ B.inclusion)
        ((Over.map (E.f i)).op ⋙ F)) :
    LimitPreserving.{u, v, w, w', u + 1}
      (BigFppfOver.toScheme B S hS) F
```

## Tag 049Q, a lemma

[Tag 049Q](https://stacks.math.columbia.edu/tag/049Q) in the Stacks Project.

**`AlgebraicGeometry.relativelyLimitPreserving_sheafifyMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/SheafifyRelative.lean, line 538](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/SheafifyRelative.lean#L538).

> Sheafification preserves relative limit preservation of a transformation
> of presheaves on the big fppf site.

```lean
public theorem relativelyLimitPreserving_sheafifyMap [UnivLE.{max w w', u}]
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type (max (u + 1) v)}
    (a : F ⟶ G)
    (ha : RelativelyLimitPreserving.{u, max (u + 1) v, w, w'}
      B S hS a) :
    RelativelyLimitPreserving.{u, max (u + 1) v, w, w'} B S hS
      (sheafifyMap (BigFppfOver.topology B S hS) a)
```

## Tag 04AK, a proposition

[Tag 04AK](https://stacks.math.columbia.edu/tag/04AK) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_iff_relativelyLimitPreserving`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/LimitPreservingIff.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/LimitPreservingIff.lean#L191).

> **Stacks 04AK.** A morphism of algebraic spaces over a scheme `S` is locally of finite
> presentation if and only if it is relatively limit preserving as a transformation of functors
> on the big fppf site of `S`.
>
> Both conditions are read at index categories in the universe of the schemes.

```lean
theorem isLocallyOfFinitePresentation_iff_relativelyLimitPreserving
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    IsLocallyOfFinitePresentation B S hS f ↔
      RelativelyLimitPreserving.{u, u, u, u} B S hS f
```

**`AlgebraicGeometry.relativelyLimitPreserving_of_isLocallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/LimitPreservingOfFinitePresentation.lean, line 226](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/LimitPreservingOfFinitePresentation.lean#L226). The attribute's comment: “locally of finite presentation implies relatively limit preserving”.

> A morphism of algebraic spaces over `S` which is locally of finite presentation is relatively
> limit preserving, for index categories in the universe of the schemes.

```lean
theorem relativelyLimitPreserving_of_isLocallyOfFinitePresentation
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    {a : F ⟶ G} (ha : Space.IsLocallyOfFinitePresentation B S hS a) :
    RelativelyLimitPreserving.{u, u, u, u} B S hS a
```

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_of_relativelyLimitPreserving`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/Representable.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/Representable.lean#L357). The attribute's comment: “the implication from relatively limit preserving to locally of finite presentation”.

> **Stacks 04AK, the implication from relative limit preservation towards local finite
> presentation.** A relatively limit-preserving transformation of presheaves on the big fppf site
> of `S` is locally of finite presentation as a morphism of algebraic spaces.
>
> This is `AlgebraicGeometry.isLocallyOfFinitePresentation_of_relativelyLimitPreserving` with its
> scheme-level input discharged by
> `AlgebraicGeometry.locallyOfFinitePresentation_of_relativelyLimitPreserving_yoneda_map` — the
> implication (2) ⇒ (1) of Stacks 01ZC for a morphism of the site.

```lean
theorem Space.isLocallyOfFinitePresentation_of_relativelyLimitPreserving
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : X ⟶ Y}
    (hf : RelativelyLimitPreserving.{u, u, u, u} B S hS f) :
    Space.IsLocallyOfFinitePresentation B S hS f
```

## Tag 05N0, a remark

[Tag 05N0](https://stacks.math.columbia.edu/tag/05N0) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_terminal_iff_limitPreserving`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/LimitPreservingFunctorOfPoints.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/LimitPreservingFunctorOfPoints.lean#L291).

> **Stacks 05N0.** An algebraic space `X` over a scheme `S` is locally of finite
> presentation over `S` if and only if `X`, read as a functor on the big fppf site of `S`, is
> limit preserving.
>
> This is the case of Stacks 04AK in which the target is the terminal presheaf, so that the
> morphism is the structure morphism of `X` to `S`. Only the implication (1) ⇒ (2) of Stacks
> 04AK is used; the converse is obtained from Stacks 0CM6 instead, so no undischarged
> hypothesis enters. Compare Stacks 05LX,
> `AlgebraicGeometry.Scheme.locallyOfFinitePresentation_iff_isLimitPreserving_yoneda`, which is
> this statement for a scheme.

```lean
theorem isLocallyOfFinitePresentation_terminal_iff_limitPreserving
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X) :
    IsLocallyOfFinitePresentation B S hS (terminal.from X) ↔
      LimitPreserving.{u, u, u, u, u + 1, u} (BigFppfOver.toScheme B S hS) X
```

## Tag 0CM6, a lemma

[Tag 0CM6](https://stacks.math.columbia.edu/tag/0CM6) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_of_affineLimit_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/SurjectiveCriterion.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentation/SurjectiveCriterion.lean#L346).

> **Stacks 0CM6.** A morphism of algebraic spaces over `S` is locally of finite
> presentation as soon as, for every cofiltered inverse limit of affine objects of the site,
> the comparison map from the colimit of the sections of the source to the fibre product of
> the sections over the limit with the colimit of the sections of the target is surjective.

```lean
theorem isLocallyOfFinitePresentation_of_affineLimit_surjective
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hsurj : ∀ (I : Type u) [Category.{u} I] [IsCofiltered I]
      (D : I ⥤ BigFppfOver B S hS) (c : Cone D),
      IsLimit ((BigFppfOver.toScheme B S hS).mapCone c) →
      (∀ i, IsAffine ((BigFppfOver.toScheme B S hS).obj (D.obj i))) →
      IsAffine ((BigFppfOver.toScheme B S hS).obj c.pt) →
      ∀ (x : X.obj (Opposite.op c.pt)) (y : colimit (D.op ⋙ Y)),
        f.app (Opposite.op c.pt) x = colimit.desc (D.op ⋙ Y) (Y.mapCocone c.op) y →
        ∃ z : colimit (D.op ⋙ X),
          colimit.desc (D.op ⋙ X) (X.mapCocone c.op) z = x ∧
          colimMap (Functor.whiskerLeft D.op f) z = y) :
    IsLocallyOfFinitePresentation B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 70.3, Tag 049I](https://stacks.math.columbia.edu/tag/049I)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
