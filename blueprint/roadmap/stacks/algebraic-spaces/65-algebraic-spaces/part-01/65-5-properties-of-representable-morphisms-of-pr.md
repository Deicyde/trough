---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.HasSchemeProperty, CategoryTheory.MorphismProperty.presheaf, CategoryTheory.Presheaf.isLocallySurjective_bot, CategoryTheory.Sheaf.IsLocallySurjective, CategoryTheory.MorphismProperty.relative_map_iff, CategoryTheory.MorphismProperty.relative_isStableUnderComposition, CategoryTheory.MorphismProperty.relative_isStableUnderBaseChange, AlgebraicGeometry.Space.presheaf_of_isLocallySurjective_pullback
statement: formalized
proof: formalized
---

# 65.5 Properties of representable morphisms of presheaves

Section 65.5 of the Stacks Project, [Tag 02WI](https://stacks.math.columbia.edu/tag/02WI). 11 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 9 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 025V, a definition

[Tag 025V](https://stacks.math.columbia.edu/tag/025V) in the Stacks Project.

**`AlgebraicGeometry.Space.HasSchemeProperty`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RepresentableProperty.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RepresentableProperty.lean#L107).

> **Stacks 025V.** A representable map of presheaves `a : F ⟶ G` on the big fppf site of `S`
> *has property `P`*, for `P` a property of morphisms of schemes, when for every object `U` of
> the site and every `ξ : h_U ⟶ G` the resulting morphism of schemes `V_ξ ⟶ U` has `P`.

```lean
abbrev Space.HasSchemeProperty (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (P : MorphismProperty Scheme.{u}) {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (a : F ⟶ G) :
    Prop
```

Declarations registered for the tag:

- [`CategoryTheory.MorphismProperty.presheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.presheaf#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/RepresentableProperty.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RepresentableProperty.lean#L93) (StacksFrontier): “a representable map of presheaves has a property of morphisms of schemes when every represented base change of it has that property”.

## Tag 02YN, a remark

[Tag 02YN](https://stacks.math.columbia.edu/tag/02YN) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.MorphismProperty.presheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.presheaf#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Presentation/Surjective.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Presentation/Surjective.lean#L63) (StacksFrontier): “surjectivity after representable base change, the default for morphisms of algebraic spaces”.
- [`CategoryTheory.Presheaf.isLocallySurjective_bot`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Presheaf.lean#L44), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Presentation/Surjective.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Presentation/Surjective.lean#L65) (StacksFrontier): “objectwise surjectivity of a map of presheaves”.
- [`CategoryTheory.Sheaf.IsLocallySurjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Sheaf.IsLocallySurjective#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Presentation/Surjective.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Presentation/Surjective.lean#L67) (StacksFrontier): “local surjectivity of a map of sheaves”.

## Tag 02WJ, a lemma

[Tag 02WJ](https://stacks.math.columbia.edu/tag/02WJ) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.MorphismProperty.relative_map_iff`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.relative_map_iff#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch65.lean, line 31](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch65.lean#L31) (StacksFrontier): “`h_f` has the relative property `P` if and only if `f` has `P`, for `P` stable under base change; stated for any fully faithful functor preserving fibre products”.

## Tag 02WK, a lemma

[Tag 02WK](https://stacks.math.columbia.edu/tag/02WK) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.MorphismProperty.relative_isStableUnderComposition`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.relative_isStableUnderComposition#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch65.lean, line 35](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch65.lean#L35) (StacksFrontier): “the relative property attached to `P` is stable under composition when `P` is; stated for any fully faithful functor”.

## Tag 02WL, a lemma

[Tag 02WL](https://stacks.math.columbia.edu/tag/02WL) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.MorphismProperty.relative_isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.relative_isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch65.lean, line 27](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch65.lean#L27) (StacksFrontier). References: SGA 4 VI (1.9.1), “more general”.

## Tag 03KD, a lemma

[Tag 03KD](https://stacks.math.columbia.edu/tag/03KD) in the Stacks Project.

**`AlgebraicGeometry.Space.presheaf_of_isLocallySurjective_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Presentation/Descent.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Presentation/Descent.lean#L46).

> A morphism property of a representable transformation descends along a transformation
> which becomes surjective after fppf sheafification.

```lean
theorem presheaf_of_isLocallySurjective_pullback (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (P : MorphismProperty Scheme.{u})
    [P.IsStableUnderBaseChange] [P.IsLocalAtTarget Scheme.fppfPrecoverage]
    {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (a : F ⟶ G) (b : H ⟶ G)
    (ha : yoneda.relativelyRepresentable a)
    (hb : Presheaf.IsLocallySurjective (BigFppfOver.topology B S hS) b)
    (hbase : (P.inverseImage (BigFppfOver.toScheme B S hS)).presheaf (pullback.snd a b)) :
    (P.inverseImage (BigFppfOver.toScheme B S hS)).presheaf a
```

## Tag 02WM, a lemma

[Tag 02WM](https://stacks.math.columbia.edu/tag/02WM) in the Stacks Project.

**`AlgebraicGeometry.Space.hasSchemeProperty_prod_map`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Product.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Product.lean#L55).

> **Stacks 02WM.** Let `P` be a property of morphisms of schemes which is stable under
> composition. If two representable morphisms of presheaves `a₁ : F₁ ⟶ G₁` and `a₂ : F₂ ⟶ G₂`
> on the big fppf site of `S` both have `P` in the sense of Stacks 025V, then so does their
> product `a₁ × a₂ : F₁ × F₂ ⟶ G₁ × G₂`.

```lean
theorem hasSchemeProperty_prod_map (P : MorphismProperty Scheme.{u})
    [P.IsStableUnderComposition] {F₁ F₂ G₁ G₂ : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (a₁ : F₁ ⟶ G₁) (a₂ : F₂ ⟶ G₂)
    (h₁ : HasSchemeProperty B S hS P a₁) (h₂ : HasSchemeProperty B S hS P a₂) :
    HasSchemeProperty B S hS P (prod.map a₁ a₂)
```

## Tag 02YO, a lemma

[Tag 02YO](https://stacks.math.columbia.edu/tag/02YO) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.MorphismProperty.relative_monotone`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.MorphismProperty.relative_monotone#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch65.lean, line 29](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch65.lean#L29) (StacksFrontier).

## Tag 05VM, a lemma

[Tag 05VM](https://stacks.math.columbia.edu/tag/05VM) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallySurjective_of_representable_flat_locallyOfFinitePresentation_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Presentation/Surjective.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Presentation/Surjective.lean#L74).

> **Stacks Project, Tag 05VM.** A representable map of sheaves whose scheme-valued base
> changes are surjective, flat, and locally of finite presentation is locally surjective for the
> fppf topology.

```lean
theorem isLocallySurjective_of_representable_flat_locallyOfFinitePresentation_surjective
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G : Sheaf (BigFppfOver.topology B S hS) (Type u)} (a : F ⟶ G)
    (ha : (MorphismProperty.presheaf
      (MorphismProperty.inverseImage
        ((fun _ _ f => Flat f ∧ LocallyOfFinitePresentation f ∧ Surjective f) :
          MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS))) a.hom) :
    Sheaf.IsLocallySurjective a
```

## Tag 025W, a lemma

[Tag 025W](https://stacks.math.columbia.edu/tag/025W) in the Stacks Project.

**`AlgebraicGeometry.yoneda_relativelyRepresentable_diag_tfae_bigFppfOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RepresentableProperty.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RepresentableProperty.lean#L116).

> **Stacks 025W.** For a presheaf `F` on the big fppf site of `S`, representability of the
> diagonal of `F`, representability of every scheme-valued point of `F`, and representability of
> the fibre product of every pair of scheme-valued points of `F` are equivalent.

```lean
theorem yoneda_relativelyRepresentable_diag_tfae_bigFppfOver
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) :
    List.TFAE
      [yoneda.relativelyRepresentable (Limits.diag F),
        ∀ (U : BigFppfOver B S hS) (ξ : F.obj (Opposite.op U)),
          yoneda.relativelyRepresentable (yonedaEquiv.symm ξ),
        ∀ (U V : BigFppfOver B S hS) (ξ : F.obj (Opposite.op U))
          (ξ' : F.obj (Opposite.op V)),
          (Limits.pullback (yonedaEquiv.symm ξ) (yonedaEquiv.symm ξ')).IsRepresentable]
```

Declarations registered for the tag:

- [`CategoryTheory.yoneda_relativelyRepresentable_diag_tfae`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/Pullback.lean#L120), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/RepresentableProperty.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RepresentableProperty.lean#L98) (StacksFrontier): “stated for the Yoneda embedding of an arbitrary category with binary products and fibre products”.

## Tag 0CB7, a lemma

[Tag 0CB7](https://stacks.math.columbia.edu/tag/0CB7) in the Stacks Project.

**`AlgebraicGeometry.Space.presheaf_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Presentation/Diagonal.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Presentation/Diagonal.lean#L81).

> A property of all pairwise fibre products of representables over a presheaf passes to its
> diagonal.

```lean
theorem presheaf_diagonal (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (P : MorphismProperty Scheme.{u}) [P.IsStableUnderBaseChange]
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (h : ∀ (U V : BigFppfOver B S hS) (a : F.obj (op U)) (b : F.obj (op V)),
      ∃ (W : BigFppfOver B S hS)
        (i : yoneda.obj W ≅ pullback (yonedaEquiv.symm a) (yonedaEquiv.symm b))
        (f : W ⟶ U ⨯ V),
        yoneda.map (f ≫ prod.fst) =
          i.hom ≫ pullback.fst (yonedaEquiv.symm a) (yonedaEquiv.symm b) ∧
        yoneda.map (f ≫ prod.snd) =
          i.hom ≫ pullback.snd (yonedaEquiv.symm a) (yonedaEquiv.symm b) ∧
        P ((BigFppfOver.toScheme B S hS).map f)) :
    (P.inverseImage (BigFppfOver.toScheme B S hS)).presheaf (diag F)
```

**`AlgebraicGeometry.Space.sheaf_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Presentation/DiagonalFunctor.lean, line 449](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Presentation/DiagonalFunctor.lean#L449). The attribute's comment: “for the sheafified Yoneda embedding, which is the one the diagonal of a formal algebraic space is tested against”.

> **Stacks 0CB7** for the sheafified Yoneda embedding of the big fppf site over `S`: if
> every pair of scheme-valued points of an fppf sheaf `X` of `Type (u + 1)` has a fibre product
> represented by an object `W` of the site whose canonical morphism to the product of the two
> sources has `Q`, then the diagonal of `X` has `Q` relative to the sheafified Yoneda embedding.

```lean
theorem sheaf_diagonal (Q : MorphismProperty (BigFppfOver B S hS))
    [Q.IsStableUnderBaseChange]
    (X : Sheaf (BigFppfOver.topology B S hS) (Type (u + 1)))
    (h : ∀ (U V : BigFppfOver B S hS)
      (α : (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).obj U ⟶ X)
      (β : (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).obj V ⟶ X),
      ∃ (W : BigFppfOver B S hS)
        (i : (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).obj W ≅ pullback α β)
        (f : W ⟶ U ⨯ V),
        (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).map (f ≫ Limits.prod.fst) =
          i.hom ≫ pullback.fst α β ∧
        (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)).map (f ≫ Limits.prod.snd) =
          i.hom ≫ pullback.snd α β ∧
        Q f) :
    Q.relative (Sheaf.sheafifiedYoneda (BigFppfOver.topology B S hS)) (diag X)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 65.5, Tag 02WI](https://stacks.math.columbia.edu/tag/02WI)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
