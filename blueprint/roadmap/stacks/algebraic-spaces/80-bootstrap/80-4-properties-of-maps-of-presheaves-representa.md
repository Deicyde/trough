---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.HasProperty, AlgebraicGeometry.Space.HasProperty.of_isPullback, AlgebraicGeometry.Space.hasProperty_of_isPullback, isRepresentableByAlgebraicSpaces_of_isPullback, AlgebraicGeometry.Space.hasProperty_comp, isRepresentableByAlgebraicSpaces_comp, AlgebraicGeometry.Space.hasProperty_prod_map, AlgebraicGeometry.Space.HasProperty.mono
statement: formalized
proof: formalized
---

# 80.4 Properties of maps of presheaves representable by algebraic spaces

Section 80.4 of the Stacks Project, [Tag 046E](https://stacks.math.columbia.edu/tag/046E). 6 tags here are carried by 7 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03XZ, a definition

[Tag 03XZ](https://stacks.math.columbia.edu/tag/03XZ) in the Stacks Project.

**`AlgebraicGeometry.Space.HasProperty`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RepresentableProperty.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RepresentableProperty.lean#L78).

> **Stacks 03XZ.** A map of presheaves `a : F ⟶ G` on the big fppf site of `S` which is
> representable by algebraic spaces *has property `P`* when, for every object `U` of the site
> and every `ξ : h_U ⟶ G`, the morphism of algebraic spaces `U ×_G F ⟶ U` has `P`.

```lean
abbrev HasProperty (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (a : F ⟶ G)
    (ha : IsRepresentableByAlgebraicSpaces B S hS a) : Prop
```

## Tag 046F, a lemma

[Tag 046F](https://stacks.math.columbia.edu/tag/046F) in the Stacks Project.

**`AlgebraicGeometry.Space.HasProperty.of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BootstrapRepresentableCalculus.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/BootstrapRepresentableCalculus.lean#L98).

> **Stacks 046F.** In a Cartesian square of presheaves on the big fppf site of `S` whose
> right-hand column `a` is representable by algebraic spaces and has a property `P` of morphisms
> of algebraic spaces over `S`, the left-hand column `a'` is representable by algebraic spaces
> (Stacks 03Y0) and has `P`.
>
> Only invariance of `P` under isomorphism is used, which is weaker than the two conditions
> Stacks imposes on `P` in Definition 03XZ.

```lean
theorem HasProperty.of_isPullback {P : MorphismProperty (AlgebraicSpaces B S hS)}
    [P.RespectsIso] {F G F' G' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {a : F ⟶ G} {g : G' ⟶ G}
    {k : F' ⟶ F} {a' : F' ⟶ G'} (sq : IsPullback k a' a g)
    (ha : IsRepresentableByAlgebraicSpaces B S hS a) (h : HasProperty B S hS P a ha) :
    HasProperty B S hS P a' (IsRepresentableByAlgebraicSpaces.of_isPullback sq ha)
```

**`AlgebraicGeometry.Space.hasProperty_of_isPullback`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Properties.lean, line 115](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Properties.lean#L115). The attribute's comment: “property”.

> **Stacks 046F.** A property of morphisms of algebraic spaces over `S` which is stable
> under base change is inherited, as a property of a morphism of presheaves representable by
> algebraic spaces, by every cartesian base change of that morphism.

```lean
lemma hasProperty_of_isPullback (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsStableUnderBaseChange]
    {F G G' H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (p : H ⟶ F) (a' : H ⟶ G') (a : F ⟶ G) (g : G' ⟶ G) (h : IsPullback p a' a g)
    (ha : IsRepresentableByAlgebraicSpaces B S hS a)
    (hP : HasProperty B S hS P a ha) :
    HasProperty B S hS P a'
      (isRepresentableByAlgebraicSpaces_of_isPullback B S hS p a' a g h ha)
```

Declarations registered for the tag:

- [`isRepresentableByAlgebraicSpaces_of_isPullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isRepresentableByAlgebraicSpaces_of_isPullback#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Properties.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Properties.lean#L109) (StacksFrontier): “representability”.

## Tag 046G, a lemma

[Tag 046G](https://stacks.math.columbia.edu/tag/046G) in the Stacks Project.

**`AlgebraicGeometry.Space.hasProperty_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Properties.lean, line 233](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Properties.lean#L233). The attribute's comment: “property of the composite”.

> **Stacks 046G.** A composite of morphisms of presheaves on the big fppf site of `S`
> representable by algebraic spaces has a property `P` of morphisms of algebraic spaces over
> `S` as soon as both factors do, provided `P` is stable under base change, local on the base
> for the fppf topology, and stable under composition.

```lean
theorem hasProperty_comp (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsStableUnderBaseChange] [P.IsLocalAtTarget (Topology.fppf.precoverage B S hS)]
    [P.IsStableUnderComposition]
    {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (a : F ⟶ G) (b : G ⟶ H)
    (ha : IsRepresentableByAlgebraicSpaces B S hS a)
    (hb : IsRepresentableByAlgebraicSpaces B S hS b)
    (hPa : HasProperty B S hS P a ha) (hPb : HasProperty B S hS P b hb) :
    HasProperty B S hS P (a ≫ b)
      (isRepresentableByAlgebraicSpaces_comp B S hS a b ha hb)
```

Declarations registered for the tag:

- [`isRepresentableByAlgebraicSpaces_comp`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isRepresentableByAlgebraicSpaces_comp#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Properties.lean, line 224](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Properties.lean#L224) (StacksFrontier): “representability”.

## Tag 046H, a lemma

[Tag 046H](https://stacks.math.columbia.edu/tag/046H) in the Stacks Project.

**`AlgebraicGeometry.Space.hasProperty_prod_map`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Properties.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/Properties.lean#L267).

> **Stacks 046H.** The product of two morphisms of presheaves on the big fppf site of `S`
> representable by algebraic spaces has a property `P` of morphisms of algebraic spaces over
> `S` as soon as both factors do, provided `P` is stable under base change, local on the base
> for the fppf topology, and stable under composition.
>
> The product is the composite of two base changes of the two factors, so this follows from
> Stacks 046F and Stacks 046G.

```lean
lemma hasProperty_prod_map (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsStableUnderBaseChange] [P.IsLocalAtTarget (Topology.fppf.precoverage B S hS)]
    [P.IsStableUnderComposition]
    {F₁ F₂ G₁ G₂ : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (a₁ : F₁ ⟶ G₁) (a₂ : F₂ ⟶ G₂)
    (h₁ : IsRepresentableByAlgebraicSpaces B S hS a₁)
    (h₂ : IsRepresentableByAlgebraicSpaces B S hS a₂)
    (ha₁ : HasProperty B S hS P a₁ h₁) (ha₂ : HasProperty B S hS P a₂ h₂) :
    HasProperty B S hS P (prod.map a₁ a₂)
      (isRepresentableByAlgebraicSpaces_prod_map B S hS a₁ a₂ h₁ h₂)
```

## Tag 0AM1, a lemma

[Tag 0AM1](https://stacks.math.columbia.edu/tag/0AM1) in the Stacks Project.

**`AlgebraicGeometry.Space.HasProperty.mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RepresentabilityCriteria.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RepresentabilityCriteria.lean#L102).

> The property tested by `AlgebraicGeometry.Space.HasProperty` may be enlarged: if `P` implies
> `Q` for every morphism of algebraic spaces over `S`, then a morphism of presheaves representable
> by algebraic spaces having `P` also has `Q`.

```lean
theorem HasProperty.mono {P Q : MorphismProperty (AlgebraicSpaces B S hS)} (hPQ : P ≤ Q)
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {a : F ⟶ G}
    {ha : IsRepresentableByAlgebraicSpaces B S hS a}
    (h : HasProperty B S hS P a ha) : HasProperty B S hS Q a ha
```

## Tag 04S1, a lemma

[Tag 04S1](https://stacks.math.columbia.edu/tag/04S1) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallySurjective_of_isRepresentableByAlgebraicSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/LocallySurjective.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Representable/Bootstrap/LocallySurjective.lean#L70).

> **Stacks 04S1.** A morphism of fppf sheaves on the big fppf site of `S` which is
> representable by algebraic spaces, surjective, flat and locally of finite presentation is
> locally surjective for the big fppf topology.

```lean
theorem isLocallySurjective_of_isRepresentableByAlgebraicSpaces
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (_hF : Presheaf.IsSheaf (BigFppfOver.topology B S hS) F)
    (_hG : Presheaf.IsSheaf (BigFppfOver.topology B S hS) G)
    (a : F ⟶ G)
    (ha : IsRepresentableByAlgebraicSpaces B S hS a)
    (hflat : HasProperty B S hS (fun _ _ f => IsFlat B S hS f.hom) a ha)
    (hlfp : HasProperty B S hS
      (fun _ _ f => IsLocallyOfFinitePresentation B S hS f.hom) a ha)
    (hsurj : HasProperty B S hS (fun _ _ f => IsSurjective B S hS f.hom) a ha) :
    Presheaf.IsLocallySurjective (BigFppfOver.topology B S hS) a
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 80.4, Tag 046E](https://stacks.math.columbia.edu/tag/046E)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
