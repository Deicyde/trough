---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.nonempty_groupoidPresentation, AlgebraicGeometry.Stack.SelfIntersection.tripleEquivComposable, AlgebraicGeometry.Stack.SelfIntersection.tripleEquivComposable_fst, AlgebraicGeometry.Stack.SelfIntersection.tripleEquivComposable_last, AlgebraicGeometry.Stack.SelfIntersection.tripleEquivComposable_middle, AlgebraicGeometry.Stack.SelfIntersection.tripleEquivComposable_secondIso, AlgebraicGeometry.Stack.SelfIntersection.tripleEquivComposable_middleIso, AlgebraicGeometry.Stack.SelfIntersection.composition
statement: formalized
proof: formalized
---

# 94.16 From an algebraic stack to a presentation

Section 94.16 of the Stacks Project, [Tag 04T3](https://stacks.math.columbia.edu/tag/04T3). 6 tags here are carried by 31 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04T3, the section

[Tag 04T3](https://stacks.math.columbia.edu/tag/04T3) in the Stacks Project.

**`AlgebraicGeometry.Stack.nonempty_groupoidPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothPresentationExistence.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SmoothPresentationExistence.lean#L152). The attribute's comment: “every algebraic stack has a presentation by a smooth groupoid in algebraic spaces”.

> **Stacks 04T3: every algebraic stack has a presentation.** Let `𝒳` be an algebraic stack
> over `S`. Then there are a smooth groupoid `(U, R, s, t, c)` in algebraic spaces over `S` and an
> equivalence over the big fppf site of `S` from its quotient stack `[U/R]` to `𝒳`.
>
> The groupoid is the self-intersection groupoid of Stacks 04T4 (4) of the presentation of `𝒳` by
> a scheme, which is smooth by Stacks 04T5 (1), and the equivalence is the canonical 1-morphism of
> Stacks 04T4 (5), which is an equivalence by Stacks 04T5 (2).

```lean
theorem nonempty_groupoidPresentation
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val) :
    Nonempty (GroupoidPresentation B S hS 𝒳.val)
```

## Tag 04T4, a lemma

[Tag 04T4](https://stacks.math.columbia.edu/tag/04T4) in the Stacks Project.

**`AlgebraicGeometry.Stack.SelfIntersection.tripleEquivComposable`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersection.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersection.lean#L165). The attribute's comment: “part (2): three-fold product as composable arrows”.

> **Stacks 04T4 (2).** The canonical equivalence, in the 2-category of categories over the
> big fppf site of `S`, between the three-fold 2-fibre product `𝒰 ×_𝒳 𝒰 ×_𝒳 𝒰` and the
> category `ℛ ×_{pr₁, 𝒰, pr₀} ℛ` of composable pairs of arrows of the relation. On fibres over
> a scheme `T` it sends `((a, b, α), c, β)` to `((a, b, α), (b, c, β))`.

```lean
noncomputable def tripleEquivComposable :
    StacksRepresentableCFG.EquivalenceOver (tripleProjection B S hS 𝒰 𝒳 f)
      (composableProjection B S hS 𝒰 𝒳 f)
```

**`AlgebraicGeometry.Stack.SelfIntersection.tripleEquivComposable_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersection.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersection.lean#L174). The attribute's comment: “part (2): first arrow of the comparison”.

> The comparison of Stacks 04T4 (2) leaves the first relation arrow unchanged.

```lean
theorem tripleEquivComposable_fst (x : triple B S hS 𝒰 𝒳 f) :
    ((tripleEquivComposable B S hS 𝒰 𝒳 f).hom.functor.obj x).x = x.x
```

**`AlgebraicGeometry.Stack.SelfIntersection.tripleEquivComposable_last`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersection.lean, line 179](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersection.lean#L179). The attribute's comment: “part (2): last object of the comparison”.

> The comparison of Stacks 04T4 (2) leaves the final object unchanged.

```lean
theorem tripleEquivComposable_last (x : triple B S hS 𝒰 𝒳 f) :
    ((tripleEquivComposable B S hS 𝒰 𝒳 f).hom.functor.obj x).y.y = x.y
```

**`AlgebraicGeometry.Stack.SelfIntersection.tripleEquivComposable_middle`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersection.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersection.lean#L185). The attribute's comment: “part (2): middle object of the comparison”.

> Under the comparison of Stacks 04T4 (2) the second relation arrow starts at the first
> arrow's endpoint.

```lean
theorem tripleEquivComposable_middle (x : triple B S hS 𝒰 𝒳 f) :
    ((tripleEquivComposable B S hS 𝒰 𝒳 f).hom.functor.obj x).y.x = x.x.y
```

**`AlgebraicGeometry.Stack.SelfIntersection.tripleEquivComposable_secondIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersection.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersection.lean#L191). The attribute's comment: “part (2): second isomorphism of the comparison”.

> Under the comparison of Stacks 04T4 (2) the second relation arrow carries the original
> second isomorphism.

```lean
theorem tripleEquivComposable_secondIso (x : triple B S hS 𝒰 𝒳 f) :
    HEq ((tripleEquivComposable B S hS 𝒰 𝒳 f).hom.functor.obj x).y.iso x.iso
```

**`AlgebraicGeometry.Stack.SelfIntersection.tripleEquivComposable_middleIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersection.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersection.lean#L197). The attribute's comment: “part (2): identity at the middle object”.

> Under the comparison of Stacks 04T4 (2) the identification of the two middle objects is
> the identity.

```lean
theorem tripleEquivComposable_middleIso (x : triple B S hS 𝒰 𝒳 f) :
    HEq ((tripleEquivComposable B S hS 𝒰 𝒳 f).hom.functor.obj x).iso
      (Iso.refl x.x.y)
```

**`AlgebraicGeometry.Stack.SelfIntersection.composition`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersection.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersection.lean#L206). The attribute's comment: “part (3): composition of the relation”.

> **Stacks 04T4 (3).** The outer projection `pr₀₂`, induced through the comparison of part
> (2) by the projection of the three-fold product onto its outer two factors: a 1-morphism
> from the category of composable pairs to the relation, sending `((a, b, α), (b, c, β))` to
> `(a, c, β ∘ α)`.

```lean
noncomputable def composition :
    BasedCategory.ofFunctor (composableProjection B S hS 𝒰 𝒳 f) ⥤ᵇ
      (relation B S hS 𝒰 𝒳 f).val
```

**`AlgebraicGeometry.Stack.SelfIntersection.composition_fst`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersection.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersection.lean#L219). The attribute's comment: “part (3): source of the composite”.

> The composite of Stacks 04T4 (3) begins at the first arrow's source.

```lean
theorem composition_fst (x : composable B S hS 𝒰 𝒳 f) :
    ((composition B S hS 𝒰 𝒳 f).toFunctor.obj x).x = x.x.x
```

**`AlgebraicGeometry.Stack.SelfIntersection.composition_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersection.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersection.lean#L224). The attribute's comment: “part (3): target of the composite”.

> The composite of Stacks 04T4 (3) ends at the second arrow's target.

```lean
theorem composition_snd (x : composable B S hS 𝒰 𝒳 f) :
    ((composition B S hS 𝒰 𝒳 f).toFunctor.obj x).y = x.y.y
```

**`AlgebraicGeometry.Stack.SelfIntersection.composition_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersection.lean, line 230](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersection.lean#L230). The attribute's comment: “part (3): composition on fibre objects”.

> On objects the outer arrow of Stacks 04T4 (3) carries the composite of the two
> isomorphisms, including the identification of their middle objects.

```lean
theorem composition_iso (x : composable B S hS 𝒰 𝒳 f) :
    HEq ((composition B S hS 𝒰 𝒳 f).toFunctor.obj x).iso
      (x.x.iso ≪≫ f.toFunctor.mapIso x.iso ≪≫ x.y.iso)
```

**`AlgebraicGeometry.Stack.SelfIntersection.isRepresentableByAlgebraicSpace_relation_of_isAlgebraicStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionAlgebraicSpace.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionAlgebraicSpace.lean#L102). The attribute's comment: “part (1): the relation is an algebraic space”.

> **Stacks 04T4 (1).** Let `𝒳` be an algebraic stack over `S` and let `f : 𝒰 ⟶ 𝒳` be a
> 1-morphism whose source is a category fibred in groupoids representable by an algebraic space over
> `S`. Then the self-intersection `ℛ = 𝒰 ×_{f, 𝒳, f} 𝒰` is representable by an algebraic space.
>
> The diagonal of an algebraic stack is representable by algebraic spaces, which is condition (1) of
> Stacks 045G; condition (8) of Stacks 045G follows, and instantiated at `𝒯₁ = 𝒯₂ = 𝒰` and
> `x = y = f` it is the conclusion.

```lean
theorem isRepresentableByAlgebraicSpace_relation_of_isAlgebraicStack
    (h𝒴 : Stack.IsAlgebraicStack.{u, w} B S hS 𝒴.val)
    (h𝒰 : Stack.IsRepresentableByAlgebraicSpace B S hS 𝒰) :
    Stack.IsRepresentableByAlgebraicSpace B S hS (relation B S hS 𝒰 𝒴 f)
```

**`AlgebraicGeometry.Stack.SelfIntersection.nonempty_fullyFaithful_canonicalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionFullyFaithful.lean, line 394](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionFullyFaithful.lean#L394). The attribute's comment: “part (6): full faithfulness”.

> The canonical morphism `f_can : [U/R] ⟶ 𝒳` of the presentation datum
> `AlgebraicGeometry.Stack.SelfIntersection.selfIntersectionPresentation` is fully faithful.

```lean
theorem nonempty_fullyFaithful_canonicalMap (h𝒳 : IsAlgebraicStack B S hS 𝒳.val) :
    Nonempty ((selfIntersectionPresentation eU eR h𝒳).canonicalMap.toFunctor.FullyFaithful)
```

**`AlgebraicGeometry.Stack.SelfIntersection.relationTarget`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionGroupoid.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionGroupoid.lean#L172). The attribute's comment: “part (4): target morphism of the groupoid”.

> The target morphism `t : R ⟶ U` of the self-intersection groupoid, read in the category of
> algebraic spaces over `S` of Stacks 02X2: the morphism of algebraic spaces named, through Stacks
> 04SW, by the first projection `pr₀ : ℛ ⟶ 𝒰` of the 2-fibre product.
>
> On a test scheme `T` it sends the isomorphism class of a triple `(a, b, α)` to that of `a`.

```lean
noncomputable def relationTarget : R ⟶ U
```

**`AlgebraicGeometry.Stack.SelfIntersection.relationSource`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionGroupoid.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionGroupoid.lean#L181). The attribute's comment: “part (4): source morphism of the groupoid”.

> The source morphism `s : R ⟶ U` of the self-intersection groupoid, read in the category of
> algebraic spaces over `S` of Stacks 02X2: the morphism of algebraic spaces named, through Stacks
> 04SW, by the second projection `pr₁ : ℛ ⟶ 𝒰` of the 2-fibre product.
>
> On a test scheme `T` it sends the isomorphism class of a triple `(a, b, α)` to that of `b`.

```lean
noncomputable def relationSource : R ⟶ U
```

**`AlgebraicGeometry.Stack.SelfIntersection.SelfIntersectionPresentation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionPresentation.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionPresentation.lean#L308). The attribute's comment: “parts (4) and (5), the presentation datum: the groupoid and the canonical morphism from its quotient stack, as a structure”.

> A presentation datum for `f`: a groupoid in algebraic spaces whose object space is the chosen
> representing space of `𝒰` and whose arrow space is the chosen representing space of the
> self-intersection, together with a morphism from its quotient stack to `𝒳` and a vertical
> comparison of that morphism with `f` compatible with descent.

```lean
structure SelfIntersectionPresentation
```

**`AlgebraicGeometry.Stack.SelfIntersection.selfIntersectionPresentation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionPresentation.lean, line 400](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionPresentation.lean#L400). The attribute's comment: “parts (4) and (5), the construction: that datum built from the declarations of this file and its three predecessors”.

> The presentation datum of an algebraic stack `𝒳`: the groupoid
> `AlgebraicGeometry.Stack.SelfIntersection.selfIntersectionGroupoid` over the final algebraic space,
> the canonical morphism `AlgebraicGeometry.Stack.SelfIntersection.canonicalMapToStack`, the
> comparison `extendsFQuotient` with `f`, and `eU` as the chosen equivalence of the object
> fibration.

```lean
noncomputable def selfIntersectionPresentation (h𝒳 : IsAlgebraicStack B S hS 𝒳.val) :
    SelfIntersectionPresentation eU eR
```

## Tag 04T5, a lemma

[Tag 04T5](https://stacks.math.columbia.edu/tag/04T5) in the Stacks Project.

**`AlgebraicGeometry.Stack.SelfIntersection.isSmooth_relationSource_and_relationTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionGroupoidRelativeProperty.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionGroupoidRelativeProperty.lean#L251). The attribute's comment: “part (1): the structure morphisms of the groupoid are smooth”.

> **Stacks 04T5 (1).** If the point `f : 𝒰 ⟶ 𝒳` is smooth in the sense of Stacks 04XB, then the
> source and target morphisms `s`, `t : R ⟶ U` of the self-intersection groupoid of Stacks 04T4 (4)
> are smooth morphisms of algebraic spaces over `S`.

```lean
theorem isSmooth_relationSource_and_relationTarget (hf : IsRelativelySmooth B S hS f) :
    Space.IsSmooth B S hS (relationSource eU eR).hom ∧
      Space.IsSmooth B S hS (relationTarget eU eR).hom
```

**`AlgebraicGeometry.Stack.SelfIntersection.exists_equivalenceOver_canonicalMap_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionSmoothPresentation.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionSmoothPresentation.lean#L65). The attribute's comment: “part (2): canonical equivalence”.

> Let `𝒳` be an algebraic stack over `S`, let `f : 𝒰 ⟶ 𝒳` be a 1-morphism whose source is
> represented by an algebraic space `U` and whose self-intersection is represented by an algebraic
> space `R`, and suppose that every algebraic space representing a base change of `f` along a
> scheme-valued point of `𝒳` has smooth and surjective structural morphism. Then the canonical
> 1-morphism `f_can : [U/R] ⟶ 𝒳` out of the quotient stack of the groupoid of
> `selfIntersectionPresentation eU eR h𝒳` is the forward 1-morphism of an equivalence over the big
> fppf site of `S`.

```lean
theorem exists_equivalenceOver_canonicalMap_of_isSmooth
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val)
    (hsmooth : ∀ (T : BigFppfOver B S hS)
        (y : BigFppfOver B T.left.1 T.left.2 ⥤ 𝒳.val.obj)
        (_hy : y ⋙ 𝒳.val.p = Over.map T.hom)
        (F : (BigFppfOver B T.left.1 T.left.2)ᵒᵖ ⥤ Type u)
        (hF : IsAlgebraicSpace B T.left.1 T.left.2 F),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map T.hom) 𝒰.val.p 𝒳.val.p y
            (CatFiberedInGroupoids.homFunctor f))
          (presheafOfCategories (F ⋙ typeToCat)).p) →
        Space.IsSmooth B S hS (algebraicSpaceMap B S hS T
          ((spacesOverSmallerBaseFunctor B T.left.1 S T.left.2 hS T.hom).obj ⟨F, hF⟩)).hom)
    (hsurj : ∀ (T : BigFppfOver B S hS)
        (y : BigFppfOver B T.left.1 T.left.2 ⥤ 𝒳.val.obj)
        (_hy : y ⋙ 𝒳.val.p = Over.map T.hom)
        (F : (BigFppfOver B T.left.1 T.left.2)ᵒᵖ ⥤ Type u)
        (hF : IsAlgebraicSpace B T.left.1 T.left.2 F),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map T.hom) 𝒰.val.p 𝒳.val.p y
            (CatFiberedInGroupoids.homFunctor f))
          (presheafOfCategories (F ⋙ typeToCat)).p) →
        Space.IsSurjective B S hS (algebraicSpaceMap B S hS T
          ((spacesOverSmallerBaseFunctor B T.left.1 S T.left.2 hS T.hom).obj ⟨F, hF⟩)).hom) :
    ∃ e : StacksRepresentableCFG.EquivalenceOver
        (Stack.quotientStack (selfIntersectionPresentation eU eR h𝒳).groupoid).p 𝒳.val.p,
      e.hom.functor = (selfIntersectionPresentation eU eR h𝒳).canonicalMap.toFunctor
```

**`AlgebraicGeometry.Stack.SelfIntersection.isSmooth_selfIntersectionPresentation_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionSmoothProjections.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionSmoothProjections.lean#L50). The attribute's comment: “part (1): source projection”.

> The source morphism `R ⟶ U` of the groupoid in algebraic spaces
> `AlgebraicGeometry.Stack.SelfIntersection.selfIntersectionPresentation` is smooth when the
> presenting 1-morphism `F` is representable by algebraic spaces and smooth.

```lean
theorem isSmooth_selfIntersectionPresentation_source
    (hF : IsRepresentableByAlgebraicSpaces B S hS F.hom)
    (hsmooth : HasRelativeProperty.{u, u, u + 1, u} B S hS
      (Space.smoothMorphismProperty B S hS) F hF)
    (h𝒳 : IsAlgebraicStack B S hS 𝒳.val) :
    Space.IsSmooth B S hS (selfIntersectionPresentation eU eR h𝒳).groupoid.source.hom
```

**`AlgebraicGeometry.Stack.SelfIntersection.isSmooth_selfIntersectionPresentation_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionSmoothProjections.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionSmoothProjections.lean#L68). The attribute's comment: “part (1): target projection”.

> The target morphism `R ⟶ U` of the groupoid in algebraic spaces
> `AlgebraicGeometry.Stack.SelfIntersection.selfIntersectionPresentation` is smooth when the
> presenting 1-morphism `F` is representable by algebraic spaces and smooth.

```lean
theorem isSmooth_selfIntersectionPresentation_target
    (hF : IsRepresentableByAlgebraicSpaces B S hS F.hom)
    (hsmooth : HasRelativeProperty.{u, u, u + 1, u} B S hS
      (Space.smoothMorphismProperty B S hS) F hF)
    (h𝒳 : IsAlgebraicStack B S hS 𝒳.val) :
    Space.IsSmooth B S hS (selfIntersectionPresentation eU eR h𝒳).groupoid.target.hom
```

## Tag 04WY, a remark

[Tag 04WY](https://stacks.math.columbia.edu/tag/04WY) in the Stacks Project.

**`AlgebraicGeometry.Stack.SelfIntersection.nonempty_isEquivalenceOver_canonicalMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionFlatPresentation.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionFlatPresentation.lean#L187). The attribute's comment: “flat\_presentation\_equivalence”.

> Let `𝒳` be an algebraic stack over `S`, let `f : 𝒰 ⟶ 𝒳` be a 1-morphism whose
> source is represented by an algebraic space `U` and whose self-intersection is represented by an
> algebraic space `R`, and suppose that every algebraic space representing a base change of `f`
> along a scheme-valued point of `𝒳` has surjective, flat and locally finitely presented structural
> morphism. Then the canonical 1-morphism `f_can : [U/R] ⟶ 𝒳` of the presentation datum
> `selfIntersectionPresentation eU eR h𝒳` is an equivalence over the big fppf site of `S`.

```lean
theorem nonempty_isEquivalenceOver_canonicalMap
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val)
    (hCover : ∀ (T : BigFppfOver B S hS)
        (y : BigFppfOver B T.left.1 T.left.2 ⥤ 𝒳.val.obj)
        (_hy : y ⋙ 𝒳.val.p = Over.map T.hom)
        (F : (BigFppfOver B T.left.1 T.left.2)ᵒᵖ ⥤ Type u)
        (hF : IsAlgebraicSpace B T.left.1 T.left.2 F),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map T.hom) 𝒰.val.p 𝒳.val.p y
            (CatFiberedInGroupoids.homFunctor f))
          (presheafOfCategories (F ⋙ typeToCat)).p) →
        let a := algebraicSpaceMap B S hS T
          ((spacesOverSmallerBaseFunctor B T.left.1 S T.left.2 hS T.hom).obj ⟨F, hF⟩)
        (Space.IsSurjective B S hS a.hom ∧ Space.IsFlat B S hS a.hom ∧
          Space.IsLocallyOfFinitePresentation B S hS a.hom)) :
    Nonempty (Functor.IsEquivalenceOver
      (Stack.quotientStack (selfIntersectionPresentation eU eR h𝒳).groupoid).p
      𝒳.val.p
      (selfIntersectionPresentation eU eR h𝒳).canonicalMap.toFunctor)
```

**`AlgebraicGeometry.Stack.SelfIntersection.isFlat_selfIntersectionPresentation_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionFlatProjections.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionFlatProjections.lean#L153). The attribute's comment: “the source projection of a flat presentation is flat”.

> **Stacks 04WY for the source projection, flatness.** The source morphism `R ⟶ U` of the
> groupoid in algebraic spaces of Stacks 04T4 (4) is flat when the presenting 1-morphism is.
>
> The source morphism is induced by the second projection `pr₁` of the self-intersection, which is
> the first leg of the leg exchange (Stacks 003Q) of the canonical 2-fibre product square over the
> cospan `F`, `F`; so this is Stacks 04XC at flatness, read at that square.

```lean
theorem isFlat_selfIntersectionPresentation_source
    (hF : IsRepresentableByAlgebraicSpaces B S hS F.hom)
    (hflat : HasRelativeProperty.{u, u, u + 1, u} B S hS
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (g : X ⟶ Y) => Space.IsFlat B S hS g.hom) F hF)
    (h𝒳 : IsAlgebraicStack B S hS 𝒳.val) :
    Space.IsFlat B S hS (selfIntersectionPresentation eU eR h𝒳).groupoid.source.hom
```

**`AlgebraicGeometry.Stack.SelfIntersection.isFlat_selfIntersectionPresentation_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionFlatProjections.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionFlatProjections.lean#L168). The attribute's comment: “the target projection of a flat presentation is flat”.

> **Stacks 04WY for the target projection, flatness.** The target morphism `R ⟶ U` of the
> groupoid in algebraic spaces of Stacks 04T4 (4) is flat when the presenting 1-morphism is.
>
> The target morphism is induced by the first projection `pr₀` of the self-intersection, which is
> the first leg of the canonical 2-fibre product square over the cospan `F`, `F`; so this is Stacks
> 04XC at flatness, read at that square, with no leg exchange.

```lean
theorem isFlat_selfIntersectionPresentation_target
    (hF : IsRepresentableByAlgebraicSpaces B S hS F.hom)
    (hflat : HasRelativeProperty.{u, u, u + 1, u} B S hS
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (g : X ⟶ Y) => Space.IsFlat B S hS g.hom) F hF)
    (h𝒳 : IsAlgebraicStack B S hS 𝒳.val) :
    Space.IsFlat B S hS (selfIntersectionPresentation eU eR h𝒳).groupoid.target.hom
```

**`AlgebraicGeometry.Stack.SelfIntersection.isLocallyOfFinitePresentation_selfIntersectionPresentation_source`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionFlatProjections.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionFlatProjections.lean#L183). The attribute's comment: “the source projection is locally of finite presentation”.

> **Stacks 04WY for the source projection, local finite presentation.** The source morphism
> `R ⟶ U` of the groupoid in algebraic spaces of Stacks 04T4 (4) is locally of finite presentation
> when the presenting 1-morphism is.
>
> This is Stacks 04XC at local finite presentation, read at the leg exchange (Stacks 003Q) of the
> canonical 2-fibre product square over the cospan `F`, `F`.

```lean
theorem isLocallyOfFinitePresentation_selfIntersectionPresentation_source
    (hF : IsRepresentableByAlgebraicSpaces B S hS F.hom)
    (hlfp : HasRelativeProperty.{u, u, u + 1, u} B S hS
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (g : X ⟶ Y) =>
        Space.IsLocallyOfFinitePresentation B S hS g.hom) F hF)
    (h𝒳 : IsAlgebraicStack B S hS 𝒳.val) :
    Space.IsLocallyOfFinitePresentation B S hS
      (selfIntersectionPresentation eU eR h𝒳).groupoid.source.hom
```

**`AlgebraicGeometry.Stack.SelfIntersection.isLocallyOfFinitePresentation_selfIntersectionPresentation_target`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionFlatProjections.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionFlatProjections.lean#L200). The attribute's comment: “the target projection is locally of finite presentation”.

> **Stacks 04WY for the target projection, local finite presentation.** The target morphism
> `R ⟶ U` of the groupoid in algebraic spaces of Stacks 04T4 (4) is locally of finite presentation
> when the presenting 1-morphism is.
>
> This is Stacks 04XC at local finite presentation, read at the canonical 2-fibre product square
> over the cospan `F`, `F`, with no leg exchange.

```lean
theorem isLocallyOfFinitePresentation_selfIntersectionPresentation_target
    (hF : IsRepresentableByAlgebraicSpaces B S hS F.hom)
    (hlfp : HasRelativeProperty.{u, u, u + 1, u} B S hS
      (fun ⦃X Y : AlgebraicSpaces B S hS⦄ (g : X ⟶ Y) =>
        Space.IsLocallyOfFinitePresentation B S hS g.hom) F hF)
    (h𝒳 : IsAlgebraicStack B S hS 𝒳.val) :
    Space.IsLocallyOfFinitePresentation B S hS
      (selfIntersectionPresentation eU eR h𝒳).groupoid.target.hom
```

**`AlgebraicGeometry.dualNumbers_projections_not_smooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionFlatProjections.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionFlatProjections.lean#L308). The attribute's comment: “the projections of a flat presentation need not be smooth”.

> **Stacks 04WY, the dual-number counterexample.** The cover of a point by the spectrum of its
> dual numbers is surjective, flat and locally of finite presentation, and neither projection of its
> self-fibre product is smooth. So the two projections of a flat presentation locally of finite
> presentation are not smooth in general, unlike the smooth case of Stacks 04T5 (1).

```lean
theorem dualNumbers_projections_not_smooth (k : Type u) [Field k] :
    let U := Spec (.of (TrivSqZeroExt k k))
    let X := Spec (.of k)
    let f : U ⟶ X := Spec.map (CommRingCat.ofHom (TrivSqZeroExt.inlHom k k))
    Surjective f ∧ Flat f ∧ LocallyOfFinitePresentation f ∧
      ¬ Smooth (pullback.fst f f) ∧ ¬ Smooth (pullback.snd f f)
```

**`AlgebraicGeometry.Stack.SelfIntersection.isFlat_relationSource_and_relationTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionGroupoidRelativeProperty.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionGroupoidRelativeProperty.lean#L209). The attribute's comment: “second clause, flatness half: the structure morphisms of the groupoid are flat”.

> **Stacks 04WY**, the flatness half of its clause on the structure morphisms of the groupoid.
> If the point `f : 𝒰 ⟶ 𝒳` is flat in the relative sense of Stacks 03YK, then the source and target
> morphisms `s`, `t : R ⟶ U` of the self-intersection groupoid of Stacks 04T4 (4) are flat
> morphisms of algebraic spaces over `S`.
>
> The source statement is the remark that the conclusion of Stacks 04T5 survives weakening
> smoothness of `f` to flatness together with local finite presentation, and that `s` and `t` are
> then flat and locally of finite presentation; this is its flatness half.

```lean
theorem isFlat_relationSource_and_relationTarget
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom)
    (hP : HasRelativeProperty.{u, u, u + 1, u} B S hS
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (g : F ⟶ G) => Space.IsFlat B S hS g.hom) f hf) :
    Space.IsFlat B S hS (relationSource eU eR).hom ∧
      Space.IsFlat B S hS (relationTarget eU eR).hom
```

**`AlgebraicGeometry.Stack.SelfIntersection.isLocallyOfFinitePresentation_relationSource_and_relationTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionGroupoidRelativeProperty.lean, line 231](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SelfIntersectionGroupoidRelativeProperty.lean#L231). The attribute's comment: “second clause, lfp half: the structure morphisms are locally of finite presentation”.

> **Stacks 04WY**, the local finite presentation half of its clause on the structure morphisms
> of the groupoid. If the point `f : 𝒰 ⟶ 𝒳` is locally of finite presentation in the relative sense
> of Stacks 03YK, then the source and target morphisms `s`, `t : R ⟶ U` of the self-intersection
> groupoid of Stacks 04T4 (4) are locally of finite presentation.
>
> The source statement is the remark that the conclusion of Stacks 04T5 survives weakening
> smoothness of `f` to flatness together with local finite presentation, and that `s` and `t` are
> then flat and locally of finite presentation; this is its local finite presentation half. The
> flatness half is
> `AlgebraicGeometry.Stack.SelfIntersection.isFlat_relationSource_and_relationTarget`.

```lean
theorem isLocallyOfFinitePresentation_relationSource_and_relationTarget
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom)
    (hP : HasRelativeProperty.{u, u, u + 1, u} B S hS
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (g : F ⟶ G) =>
        Space.IsLocallyOfFinitePresentation B S hS g.hom) f hf) :
    Space.IsLocallyOfFinitePresentation B S hS
        (relationSource eU eR).hom ∧
      Space.IsLocallyOfFinitePresentation B S hS
        (relationTarget eU eR).hom
```

## Tag 04TH, a definition

[Tag 04TH](https://stacks.math.columbia.edu/tag/04TH) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.IsSmooth`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SmoothGroupoid.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/SmoothGroupoid.lean#L62).

> **Stacks 04TH.** A groupoid `(U, R, s, t, c)` in algebraic spaces over `B` is *smooth* when
> both its source and its target morphism `R ⟶ U` are smooth morphisms of algebraic spaces.
>
> Despite the name this does not say that the quotient stack `[U/R]` is smooth over anything.

```lean
abbrev IsSmooth (G : GroupoidInAlgebraicSpaces B S hS Z) : Prop
```

## Tag 04TI, a definition

[Tag 04TI](https://stacks.math.columbia.edu/tag/04TI) in the Stacks Project.

**`AlgebraicGeometry.Stack.GroupoidPresentation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/GroupoidPresentation.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/GroupoidPresentation.lean#L57).

> A *presentation* of a category `𝒳` over `(Sch/S)_fppf` is a smooth groupoid
> `(U, R, s, t, c)` in algebraic spaces over `S` together with an equivalence of categories over
> the site from its quotient stack `[U/R]` to `𝒳`.

```lean
structure GroupoidPresentation (𝒳 : BasedCategory.{v, w} (BigFppfOver B S hS))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 94.16, Tag 04T3](https://stacks.math.columbia.edu/tag/04T3)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
