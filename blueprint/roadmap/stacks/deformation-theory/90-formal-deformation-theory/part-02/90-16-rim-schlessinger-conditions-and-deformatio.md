---
declaration: section
origin: cited
lean: Deformation.SatisfiesRS, Deformation.isLimit_of_map_isLimit, Deformation.satisfiesRS_of_small_extensions, Deformation.satisfiesRS_iff_comparison_isEquivalence_of_surjective, Deformation.satisfiesRS_iff_comparison_isEquivalence_of_smallExtension, Deformation.satisfiesRS_elementsProjection_iff_bijective, Deformation.schlessingerConditionS1_of_satisfiesRS, Deformation.schlessingerConditionS2_of_satisfiesRS
statement: formalized
proof: formalized
---

# 90.16 Rim-Schlessinger conditions and deformation categories

Section 90.16 of the Stacks Project, [Tag 06J1](https://stacks.math.columbia.edu/tag/06J1). 12 tags here are carried by 20 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06J2, a definition

[Tag 06J2](https://stacks.math.columbia.edu/tag/06J2) in the Stacks Project.

**`Deformation.SatisfiesRS`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RimSchlessinger/Basic.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessinger/Basic.lean#L70). References: SGA 7 VI (2.5).

> Condition (RS): every cospan over a cospan of Artinian local algebras whose second
> morphism is surjective has a pullback cone which remains a pullback cone in the base.

```lean
public abbrev SatisfiesRS {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ
  k] {F : Type u₁} [Category.{v₁} F] (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k) : Prop
```

## Tag 06J3, a lemma

[Tag 06J3](https://stacks.math.columbia.edu/tag/06J3) in the Stacks Project.

**`Deformation.isLimit_of_map_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RimSchlessinger/Basic.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessinger/Basic.lean#L87).

> Under condition (RS), a square over a pullback square is a pullback square when the
> second morphism in the base cospan is surjective.

```lean
public theorem isLimit_of_map_isLimit
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k}
    (hp : SatisfiesRS p)
    {x₁ x₂ x : F} (f₁ : x₁ ⟶ x) (f₂ : x₂ ⟶ x)
    (c : PullbackCone f₁ f₂)
    (hsurj : Function.Surjective (p.map f₂).hom)
    (hc : Nonempty (IsLimit (c.map p))) :
    Nonempty (IsLimit c)
```

## Tag 06J4, a lemma

[Tag 06J4](https://stacks.math.columbia.edu/tag/06J4) in the Stacks Project.

**`Deformation.satisfiesRS_of_small_extensions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RimSchlessingerCategory/SmallExtensionCriterion.lean, line 225](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessingerCategory/SmallExtensionCriterion.lean#L225).

> **Stacks Project, Tag 06J4.** To verify condition (RS) for a category cofibered in
> groupoids, it suffices to consider cospans whose second base morphism is a small
> extension.

```lean
public theorem satisfiesRS_of_small_extensions
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k}
    (hp : IsCofiberedInGroupoids p)
    (hsmall : ∀ {x₁ x₂ x : F} (f₁ : x₁ ⟶ x) (f₂ : x₂ ⟶ x),
      InfinitesimalLifting.IsSmallExtension
          (CommRingCat.ofHom (p.map f₂).hom.toRingHom) →
        ∃ c : PullbackCone f₁ f₂,
          (Nonempty (IsLimit c) ∧ Nonempty (IsLimit (c.map p)))) :
    SatisfiesRS p
```

## Tag 06J5, a lemma

[Tag 06J5](https://stacks.math.columbia.edu/tag/06J5) in the Stacks Project.

**`Deformation.satisfiesRS_iff_comparison_isEquivalence_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RimSchlessingerCategory/ComparisonEquivalence.lean, line 634](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessingerCategory/ComparisonEquivalence.lean#L634). The attribute's comment: “surjective maps”. References: SGA 7 VI (2.6(b)), “homogeneous criterion”.

> **Stacks Project, Tag 06J5.** Condition (RS) holds precisely when the canonical functor
> from the fibre over a pullback to the 2-fibre product of fibres is an equivalence for every
> square whose second map is surjective.

```lean
theorem satisfiesRS_iff_comparison_isEquivalence_of_surjective
    (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k) (hp : IsCofiberedInGroupoids p) :
    SatisfiesRS p ↔
      ∀ {P A₁ A₂ A : ArtinianLocalAlgCat.{u, v, w} Λ k}
        (p₁ : P ⟶ A₁) (p₂ : P ⟶ A₂) (f₁ : A₁ ⟶ A) (f₂ : A₂ ⟶ A)
        (hP : IsPullback p₁ p₂ f₁ f₂)
        (hf₂ : Function.Surjective f₂.hom)
        (P₁ : PushforwardChoice p p₁) (P₂ : PushforwardChoice p p₂)
        (F₁ : PushforwardChoice p f₁) (F₂ : PushforwardChoice p f₂)
        (Qp₁ : PushforwardFunctor P₁) (Qp₂ : PushforwardFunctor P₂)
        (Qf₁ : PushforwardFunctor F₁) (Qf₂ : PushforwardFunctor F₂),
        (squareComparisonFunctor p hp p₁ p₂ f₁ f₂ hP hf₂
          P₁ P₂ F₁ F₂ Qp₁ Qp₂ Qf₁ Qf₂).toFunctor.IsEquivalence
```

**`Deformation.satisfiesRS_iff_comparison_isEquivalence_of_smallExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RimSchlessingerCategory/ComparisonEquivalence.lean, line 661](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessingerCategory/ComparisonEquivalence.lean#L661). The attribute's comment: “small extensions”. References: SGA 7 VI (2.6(b)), “small extensions”.

> **Stacks Project, Tag 06J5.** It is enough to test the comparison functor on squares whose
> second map is a small extension.

```lean
theorem satisfiesRS_iff_comparison_isEquivalence_of_smallExtension
    (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k) (hp : IsCofiberedInGroupoids p) :
    SatisfiesRS p ↔
      ∀ {P A₁ A₂ A : ArtinianLocalAlgCat.{u, v, w} Λ k}
        (p₁ : P ⟶ A₁) (p₂ : P ⟶ A₂) (f₁ : A₁ ⟶ A) (f₂ : A₂ ⟶ A)
        (hP : IsPullback p₁ p₂ f₁ f₂)
        (hsmall : InfinitesimalLifting.IsSmallExtension
          (CommRingCat.ofHom f₂.hom.toRingHom))
        (P₁ : PushforwardChoice p p₁) (P₂ : PushforwardChoice p p₂)
        (F₁ : PushforwardChoice p f₁) (F₂ : PushforwardChoice p f₂)
        (Qp₁ : PushforwardFunctor P₁) (Qp₂ : PushforwardFunctor P₂)
        (Qf₁ : PushforwardFunctor F₁) (Qf₂ : PushforwardFunctor F₂),
        (squareComparisonFunctor p hp p₁ p₂ f₁ f₂ hP
          hsmall.2.2.2.2.1 P₁ P₂ F₁ F₂ Qp₁ Qp₂ Qf₁ Qf₂).toFunctor.IsEquivalence
```

## Tag 06J6, a remark

[Tag 06J6](https://stacks.math.columbia.edu/tag/06J6) in the Stacks Project.

**`Deformation.satisfiesRS_elementsProjection_iff_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RimSchlessingerCategory/SetValuedRS.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessingerCategory/SetValuedRS.lean#L135).

> **Stacks Project, Tag 06J6.** For a set-valued functor `F` on the category of Artinian local
> `Λ`-algebras, condition (RS) for the associated category cofibered in sets holds exactly when
> the canonical map `F(A₁ ×_A A₂) → F(A₁) ×_{F(A)} F(A₂)` is bijective for every fibre-product
> square whose second map is surjective; this is Schlessinger's condition (H4).

```lean
theorem satisfiesRS_elementsProjection_iff_bijective
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (G : ArtinianLocalAlgCat.{u, v, w} Λ k ⥤ Type t) :
    SatisfiesRS (Functor.Elements.π G) ↔
      ∀ {P A₁ A₂ A : ArtinianLocalAlgCat.{u, v, w} Λ k}
        (p₁ : P ⟶ A₁) (p₂ : P ⟶ A₂) (f₁ : A₁ ⟶ A) (f₂ : A₂ ⟶ A)
        (hP : IsPullback p₁ p₂ f₁ f₂), Function.Surjective f₂.hom →
          Function.Bijective (fibreProductComparison G p₁ p₂ f₁ f₂ hP.w.symm)
```

## Tag 06J7, a lemma

[Tag 06J7](https://stacks.math.columbia.edu/tag/06J7) in the Stacks Project.

**`Deformation.schlessingerConditionS1_of_satisfiesRS`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RimSchlessinger/Basic.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessinger/Basic.lean#L270). The attribute's comment: “condition (S1)”.

> Condition (RS) implies Schlessinger's condition (S1).

```lean
public theorem schlessingerConditionS1_of_satisfiesRS
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k}
    (hp : SatisfiesRS p) :
    SchlessingerConditionS1 p
```

**`Deformation.schlessingerConditionS2_of_satisfiesRS`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RimSchlessinger/Basic.lean, line 343](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessinger/Basic.lean#L343). The attribute's comment: “condition (S2)”.

> Condition (RS) implies Schlessinger's condition (S2).

```lean
public theorem schlessingerConditionS2_of_satisfiesRS
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    {p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k}
    (hp : SatisfiesRS p) :
    SchlessingerConditionS2 p
```

## Tag 06J8, a lemma

[Tag 06J8](https://stacks.math.columbia.edu/tag/06J8) in the Stacks Project.

**`Deformation.associatedSatisfiesRS_iff_gluingClassesInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RimSchlessingerCategory/AutomorphismLifting.lean, line 702](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessingerCategory/AutomorphismLifting.lean#L702). The attribute's comment: “conditions (1) and (2)”. References: SGA 7 VI (2.7), “(i) <=> injectivity”.

> For a category cofibered in groupoids satisfying (RS), the associated functor of isomorphism
> classes satisfies (RS) exactly when the comparison on isomorphism classes of gluing data is
> injective.

```lean
theorem associatedSatisfiesRS_iff_gluingClassesInjective
    (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k) (hp : SatisfiesRS p) :
    SatisfiesRS (Functor.Elements.π
        (isomorphismClassesData (BasedCategory.ofFunctor p) hp.1).classes) ↔
      IsInjectiveOnGluingClasses p
```

**`Deformation.gluingClassesInjective_iff_automorphismsLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RimSchlessingerCategory/AutomorphismLifting.lean, line 713](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessingerCategory/AutomorphismLifting.lean#L713). The attribute's comment: “conditions (2) and (3)”. References: SGA 7 VI (2.7), “inj <=> aut surjective”.

> For a category cofibered in groupoids, injectivity on isomorphism classes of gluing data is
> equivalent to lifting automorphisms along every surjection of Artinian local algebras.

```lean
theorem gluingClassesInjective_iff_automorphismsLift
    (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k) (hp : IsCofiberedInGroupoids p) :
    IsInjectiveOnGluingClasses p ↔
      (∀ {A' A : ArtinianLocalAlgCat.{u, v, w} Λ k} (f : A' ⟶ A),
        Function.Surjective f.hom → AutomorphismsLiftAlong p f)
```

**`Deformation.automorphismsLift_iff_smallExtensions`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RimSchlessingerCategory/AutomorphismLifting.lean, line 764](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessingerCategory/AutomorphismLifting.lean#L764). The attribute's comment: “conditions (3) and (4)”. References: SGA 7 VI (2.7), “(ii) vs surjections”.

> For a category cofibered in groupoids, automorphisms lift along every surjection of Artinian
> local algebras exactly when they lift along every small extension.

```lean
theorem automorphismsLift_iff_smallExtensions
    (p : F ⥤ ArtinianLocalAlgCat.{u, v, w} Λ k) (hp : IsCofiberedInGroupoids p) :
    (∀ {A' A : ArtinianLocalAlgCat.{u, v, w} Λ k} (f : A' ⟶ A),
      Function.Surjective f.hom → AutomorphismsLiftAlong p f) ↔
      (∀ {A' A : ArtinianLocalAlgCat.{u, v, w} Λ k} (f : A' ⟶ A),
        InfinitesimalLifting.IsSmallExtension
          (CommRingCat.ofHom f.hom.toRingHom) → AutomorphismsLiftAlong p f)
```

## Tag 06J9, a definition

[Tag 06J9](https://stacks.math.columbia.edu/tag/06J9) in the Stacks Project.

**`Deformation.IsDeformationCategory`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RimSchlessinger/Basic.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessinger/Basic.lean#L129). The attribute's comment: “objects”.

> A predeformation category over `𝒞_Λ` satisfying condition (RS).

```lean
structure IsDeformationCategory {Λ : Type u} {k : Type w} [CommRing Λ] [Field k]
    [Algebra Λ k] {F : Type u₁} [Category.{v₁} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k) : Prop
```

Declarations registered for the tag:

- [`BasedFunctor`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=BasedFunctor#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/RimSchlessinger/Basic.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessinger/Basic.lean#L137) (StacksFrontier): “morphisms”.

## Tag 06JA, a remark

[Tag 06JA](https://stacks.math.columbia.edu/tag/06JA) in the Stacks Project.

**`Deformation.IsDeformationFunctor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RimSchlessinger/Basic.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessinger/Basic.lean#L150). The attribute's comment: “deformation\_functor”.

> A set-valued functor is a deformation functor if its value at the residue
> field is a singleton and its associated cofibered set satisfies (RS).

```lean
public abbrev IsDeformationFunctor
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (F : ArtinianLocalAlgCat.{u, max v w, w} Λ k ⥤ Type t) : Prop
```

**`Deformation.isDeformationCategory_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RimSchlessinger/Basic.lean, line 159](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessinger/Basic.lean#L159). The attribute's comment: “deformation\_functor”.

> A functor is a deformation functor exactly when its associated cofibered set
> is a deformation category.

```lean
public theorem isDeformationCategory_iff
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    (F : ArtinianLocalAlgCat.{u, max v w, w} Λ k ⥤ Type t) :
    IsDeformationCategory (Functor.Elements.π F) ↔
      IsDeformationFunctor F
```

Declarations registered for the tag:

- [`isPredeformationFunctor_isomorphismClasses`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=isPredeformationFunctor_isomorphismClasses#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/RimSchlessinger/Basic.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessinger/Basic.lean#L172) (StacksFrontier): “associated\_predeformation”.

## Tag 06JB, an example

[Tag 06JB](https://stacks.math.columbia.edu/tag/06JB) in the Stacks Project.

**`Deformation.restrictedCoyoneda_isPredeformationFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RimSchlessingerCategory/Prorepresentable.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessingerCategory/Prorepresentable.lean#L47). The attribute's comment: “singleton value at the residue field”.

> **Stacks Project, Tag 06JB.** A functor represented by a complete local algebra takes the
> residue-field object to a one-element set.

```lean
theorem restrictedCoyoneda_isPredeformationFunctor
    (R : CompleteLocalAlgCat.{u, max v w, w} Λ k) :
    IsPredeformationFunctor (restrictedCoyoneda R)
```

**`Deformation.restrictedCoyoneda_satisfiesRS`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RimSchlessingerCategory/Prorepresentable.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessingerCategory/Prorepresentable.lean#L85). The attribute's comment: “the (RS) property”.

> **Stacks Project, Tag 06JB.** A functor represented by a complete local algebra satisfies
> (RS), since maps out of the representing object preserve the relevant fibre products.

```lean
theorem restrictedCoyoneda_satisfiesRS
    (R : CompleteLocalAlgCat.{u, max v w, w} Λ k) :
    SatisfiesRS (Functor.Elements.π (restrictedCoyoneda R))
```

**`Deformation.isDeformationFunctor_of_isProrepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RimSchlessingerCategory/Prorepresentable.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessingerCategory/Prorepresentable.lean#L214). The attribute's comment: “prorepresentable implies deformation”.

> **Stacks Project, Tag 06JB.** Every prorepresentable functor on Artinian local algebras is
> a deformation functor.

```lean
theorem isDeformationFunctor_of_isProrepresentable
    (F : ArtinianLocalAlgCat.{u, max v w, w} Λ k ⥤ Type (max v w))
    (hF : IsProrepresentable F) :
    IsDeformationFunctor F
```

## Tag 06JC, a lemma

[Tag 06JC](https://stacks.math.columbia.edu/tag/06JC) in the Stacks Project.

**`Deformation.satisfiesRS_objectsOverFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RimSchlessinger/Basic.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessinger/Basic.lean#L185). The attribute's comment: “Rim-Schlessinger condition”.

> The category localized at an object of the special fibre inherits the
> Rim–Schlessinger condition.

```lean
public theorem satisfiesRS_objectsOverFunctor
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (hp : SatisfiesRS p)
    (x : p.Fiber (residueFieldObject.{u, v, w} Λ k)) :
    SatisfiesRS
      (objectsOverFunctor p x.1)
```

**`Deformation.isDeformationCategory_objectsOverFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RimSchlessinger/Basic.lean, line 247](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessinger/Basic.lean#L247). The attribute's comment: “deformation category”.

> The category localized at an object of the special fibre is a deformation
> category when the original category satisfies the Rim–Schlessinger condition.

```lean
public theorem isDeformationCategory_objectsOverFunctor
    {Λ : Type u} {k : Type w} [CommRing Λ] [Field k] [Algebra Λ k]
    {F : Type u₁} [Category.{v₁} F]
    (p : F ⥤ ArtinianLocalAlgCat.{u, max v w, w} Λ k)
    (hp : SatisfiesRS p)
    (x : p.Fiber (residueFieldObject.{u, v, w} Λ k)) :
    IsDeformationCategory
      (objectsOverFunctor p x.1)
```

## Tag 06L4, a lemma

[Tag 06L4](https://stacks.math.columbia.edu/tag/06L4) in the Stacks Project.

**`Deformation.satisfiesRS_twoFibreProductOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/RimSchlessinger/TwoFibreProduct.lean, line 286](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/RimSchlessinger/TwoFibreProduct.lean#L286).

> A 2-fibre product of categories satisfying condition (RS) again satisfies condition
> (RS).

```lean
theorem satisfiesRS_twoFibreProductOver
    {Lambda : Type u} {k : Type w} [CommRing Lambda] [Field k] [Algebra Lambda k]
    {H : Type u₁} [Category.{v₁} H]
    {G : Type u₂} [Category.{v₂} G]
    {F : Type u₃} [Category.{v₃} F]
    (pH : H ⥤ ArtinianLocalAlgCat.{u, v, w} Lambda k)
    (pG : G ⥤ ArtinianLocalAlgCat.{u, v, w} Lambda k)
    (pF : F ⥤ ArtinianLocalAlgCat.{u, v, w} Lambda k)
    (f : H ⥤ F) (g : G ⥤ F)
    (hf : f ⋙ pF = pH) (hg : g ⋙ pF = pG)
    (hH : SatisfiesRS pH)
    (hG : SatisfiesRS pG)
    (hF : SatisfiesRS pF) :
    SatisfiesRS
      (TwoFibreProductOver.structureFunctor pH pG pF f g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 90.16, Tag 06J1](https://stacks.math.columbia.edu/tag/06J1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
