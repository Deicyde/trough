---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_schemePoint, AlgebraicGeometry.Stack.SchemePointHasRelativeProperty, AlgebraicGeometry.Stack.surjective_smooth_etale_relativePropertyHypotheses, AlgebraicGeometry.Stack.HasRelativeProperty, AlgebraicGeometry.Stack.hasRelativeProperty_iff_of_equivalences, AlgebraicGeometry.Stack.hasRelativeProperty_iff_of_equivalences', AlgebraicGeometry.Stack.holdsOnEverySchemePoint_iff_hasRelativeProperty, AlgebraicGeometry.Stack.isoClassMap_holdsOnEverySchemePoint_iff
statement: formalized
proof: formalized
---

# 94.10 Properties of morphisms representable by algebraic spaces

Section 94.10 of the Stacks Project, [Tag 03YJ](https://stacks.math.columbia.edu/tag/03YJ). 12 tags here are carried by 26 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03YJ, the section

[Tag 03YJ](https://stacks.math.columbia.edu/tag/03YJ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_schemePoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SchemePointRelativeProperty.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SchemePointRelativeProperty.lean#L82). The attribute's comment: “in the situation of Lemma 045G, every 1-morphism x : (Sch/U)_fppf -> X is representable by algebraic spaces, so that saying x has P makes sense”.

> **Stacks, Section 03YJ.** If the diagonal of a category fibred in groupoids `𝒳` over the
> big fppf site of `S` is representable by algebraic spaces, then every 1-morphism
> `x : (Sch/U)_fppf → 𝒳` from the category represented by a scheme `U` over `S` is representable
> by algebraic spaces. This is condition (3) of Stacks 045G obtained from condition (1).

```lean
theorem isRepresentableByAlgebraicSpaces_schemePoint
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (h𝒳 : HasRepresentableDiagonal B S hS 𝒳) {U : BigFppfOver B S hS}
    (x : schemeFibredCategory B S hS U ⟶ 𝒳) :
    IsRepresentableByAlgebraicSpaces B S hS x.hom
```

**`AlgebraicGeometry.Stack.SchemePointHasRelativeProperty`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SchemePointRelativeProperty.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SchemePointRelativeProperty.lean#L98). The attribute's comment: “for X as in Lemma 045G and P as in Definition 03YK, the property that a 1-morphism x : (Sch/U)_fppf -> X has P”.

> **Stacks, Section 03YJ.** Let `𝒳` be a category fibred in groupoids over the big fppf site
> of `S` whose diagonal is representable by algebraic spaces, and let `𝒫` be a property of
> morphisms of algebraic spaces as in Definition 03YK. A 1-morphism `x : (Sch/U)_fppf → 𝒳` from
> the category represented by a scheme `U` over `S` *has `𝒫`* when it has `𝒫` in the sense of
> Stacks 03YK; it is representable by algebraic spaces by
> `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpaces_schemePoint`.

```lean
abbrev SchemePointHasRelativeProperty
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsStableUnderBaseChange]
    [P.IsLocalAtTarget (Space.Topology.fppf.precoverage B S hS)]
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (h𝒳 : HasRepresentableDiagonal B S hS 𝒳) {U : BigFppfOver B S hS}
    (x : schemeFibredCategory B S hS U ⟶ 𝒳) : Prop
```

**`AlgebraicGeometry.Stack.surjective_smooth_etale_relativePropertyHypotheses`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SchemePointRelativeProperty.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SchemePointRelativeProperty.lean#L111). The attribute's comment: “surjective, smooth and etale are properties as in Definition 03YK”.

> **Stacks, Section 03YJ.** Surjectivity, smoothness and étaleness of morphisms of algebraic
> spaces over `S` are each properties as in Definition 03YK: each is stable under base change and
> local on the base for the fppf topology (Stacks 041Q, 0429 and 042B).

```lean
theorem surjective_smooth_etale_relativePropertyHypotheses :
    ((Space.surjectiveMorphismProperty B S hS).IsStableUnderBaseChange ∧
        (Space.surjectiveMorphismProperty B S hS).IsLocalAtTarget
          (Space.Topology.fppf.precoverage.{u, v} B S hS)) ∧
      ((Space.smoothMorphismProperty B S hS).IsStableUnderBaseChange ∧
        (Space.smoothMorphismProperty B S hS).IsLocalAtTarget
          (Space.Topology.fppf.precoverage.{u, v} B S hS)) ∧
      ((Space.etaleMorphisms B S hS).IsStableUnderBaseChange ∧
        (Space.etaleMorphisms B S hS).IsLocalAtTarget
          (Space.Topology.fppf.precoverage.{u, v} B S hS))
```

## Tag 03YK, a definition

[Tag 03YK](https://stacks.math.columbia.edu/tag/03YK) in the Stacks Project.

**`AlgebraicGeometry.Stack.HasRelativeProperty`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativeProperty.lean, line 51](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativeProperty.lean#L51).

> A 1-morphism of categories fibred in groupoids over the big fppf site of `S` which is
> representable by algebraic spaces *has the property `P`* when every algebraic space representing
> its base change along a scheme-valued point of the target has structural morphism with `P`, read
> as a morphism of algebraic spaces over `S`.

```lean
abbrev HasRelativeProperty
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsStableUnderBaseChange]
    [P.IsLocalAtTarget (Space.Topology.fppf.precoverage B S hS)]
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)}
    (f : 𝒳 ⟶ 𝒴) (_hf : IsRepresentableByAlgebraicSpaces B S hS f.hom) :
    Prop
```

## Tag 0459, a lemma

[Tag 0459](https://stacks.math.columbia.edu/tag/0459) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasRelativeProperty_iff_of_equivalences`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyEquivalence.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyEquivalence.lean#L78). The attribute's comment: “a vertical 1-morphism of a 2-commutative square whose horizontals are equivalences has the relative property exactly when the other vertical one does”.

> In a 2-commutative square of categories fibred in groupoids over the big fppf site of `S`
> whose two horizontal 1-morphisms are equivalences, a vertical 1-morphism representable by
> algebraic spaces has the relative property `P` of Stacks 03YK if and only if the other vertical
> 1-morphism does. Representability of `f'` is deduced from that of `f`.

```lean
theorem hasRelativeProperty_iff_of_equivalences
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsStableUnderBaseChange]
    [P.IsLocalAtTarget (Space.Topology.fppf.precoverage B S hS)]
    (f' : 𝒳' ⟶ 𝒴') (f : 𝒳 ⟶ 𝒴)
    (a : 𝒳'.val ⥤ᵇ 𝒳.val) (b : 𝒴'.val ⥤ᵇ 𝒴.val)
    (α : BasedFunctor.comp a f.hom ≅ BasedFunctor.comp f'.hom b)
    [Functor.IsEquivalence a.toFunctor] [Functor.IsEquivalence b.toFunctor]
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom) :
    HasRelativeProperty.{u, v₂, w₂} B S hS P f hf ↔
      HasRelativeProperty.{u, v₁, w₁} B S hS P f'
        ((isRepresentableByAlgebraicSpaces_iff_of_equivalences B S hS f'.hom f.hom a b α).mp
          hf)
```

**`AlgebraicGeometry.Stack.hasRelativeProperty_iff_of_equivalences'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyEquivalenceIff.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyEquivalenceIff.lean#L182). The attribute's comment: “the same biconditional assembled from the two one-directional statements”.

> **Stacks 0459.** In a 2-commutative square of categories fibred in groupoids over the big fppf
> site of `S` whose two horizontal 1-morphisms are equivalences, a vertical 1-morphism representable
> by algebraic spaces has the relative property at `P` of **Stacks 03YK** exactly when the other
> one does.
>
> The forward direction is `AlgebraicGeometry.Stack.hasRelativeProperty_of_equivalences` and the
> reverse one `AlgebraicGeometry.Stack.relativeProperty_of_equivalences_symm`; neither uses any
> hypothesis on `P`, which is carried only because the statement mentions the abbreviation.
>
> The representability witness for `f'` is an arbitrary one, which is what distinguishes this from
> `AlgebraicGeometry.Stack.hasRelativeProperty_iff_of_equivalences` of
> `StacksFrontier.AlgebraicGeometry.Stacks.RelativePropertyEquivalence`: that form reads the witness
> for `f'` off the one for `f` through Stacks 0457, and is the special case of this one at that
> witness.

```lean
theorem hasRelativeProperty_iff_of_equivalences' (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsStableUnderBaseChange]
    [P.IsLocalAtTarget (Space.Topology.fppf.precoverage B S hS)]
    (f' : 𝒳' ⟶ 𝒴') (f : 𝒳 ⟶ 𝒴)
    (a : 𝒳'.val ⥤ᵇ 𝒳.val) (b : 𝒴'.val ⥤ᵇ 𝒴.val)
    (α : BasedFunctor.comp a f.hom ≅ BasedFunctor.comp f'.hom b)
    [Functor.IsEquivalence a.toFunctor] [Functor.IsEquivalence b.toFunctor]
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom)
    (hf' : IsRepresentableByAlgebraicSpaces B S hS f'.hom) :
    HasRelativeProperty.{u, v₂, w₂} B S hS P f hf ↔
      HasRelativeProperty.{u, v₁, w₁} B S hS P f' hf'
```

## Tag 045A, a lemma

[Tag 045A](https://stacks.math.columbia.edu/tag/045A) in the Stacks Project.

**`AlgebraicGeometry.Stack.holdsOnEverySchemePoint_iff_hasRelativeProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/PresheafRepresentability.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/PresheafRepresentability.lean#L183).

> **Stacks 045A.** Let `P` be a property of morphisms of algebraic spaces over `S` which is
> stable under base change and local on the target for the fppf precoverage. A map `a : F ⟶ G` of
> presheaves on the big fppf site of `S` which is representable by algebraic spaces has `P` in the
> sense of Stacks 03XZ exactly when the 1-morphism of categories fibred in groupoids attached to it
> by Stacks 0458 has the relative property `P` of Stacks 03YK.

```lean
theorem holdsOnEverySchemePoint_iff_hasRelativeProperty
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsStableUnderBaseChange]
    [P.IsLocalAtTarget (Space.Topology.fppf.precoverage B S hS)]
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (a : F ⟶ G)
    (ha : Space.IsRepresentableByAlgebraicSpaces B S hS a) :
    Space.HasProperty B S hS P a ha ↔
      HasRelativeProperty B S hS P (associatedMap B S hS a).1
        ((isRepresentableByAlgebraicSpaces_iff_associatedMap B S hS a).1 ha)
```

## Tag 04TC, a lemma

[Tag 04TC](https://stacks.math.columbia.edu/tag/04TC) in the Stacks Project.

**`AlgebraicGeometry.Stack.isoClassMap_holdsOnEverySchemePoint_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SetoidRelativeProperty.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SetoidRelativeProperty.lean#L55).

> **Stacks 04TC.** For a 1-morphism `f` of categories fibred in setoids over the big fppf site
> of `S` whose induced map `a` of isomorphism-class presheaves is representable by algebraic
> spaces, `a` has a property `P` in the sense of Stacks 03XZ exactly when `f` has `P` in the
> relative sense of Stacks 03YK.

```lean
theorem isoClassMap_holdsOnEverySchemePoint_iff
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsStableUnderBaseChange]
    [P.IsLocalAtTarget (Space.Topology.fppf.precoverage B S hS)]
    {𝒳 𝒴 : CatFiberedInSetoids.{u, v, u + 1, u} (BigFppfOver B S hS)} (f : 𝒳 ⟶ 𝒴)
    (a : 𝒳.val.p.isoClassPresheaf ⟶ 𝒴.val.p.isoClassPresheaf)
    (ha : ∀ (U : BigFppfOver B S hS) (x : 𝒳.val.p.Fiber U),
      a.app (Opposite.op U) (Functor.isoClassMk 𝒳.val.p x) =
        Functor.isoClassMk 𝒴.val.p
          ((Functor.Fiber.mapOfComp 𝒳.val.p 𝒴.val.p
            (CatFiberedInGroupoids.homFunctor f)
            (CatFiberedInGroupoids.homFunctor_comp_p f) U).obj x))
    (hf : IsRepresentableByAlgebraicSpaces B S hS
      (CatFiberedInSetoids.inclusion.map f).hom) :
    Space.HasProperty B S hS P a
        ((isoClassMap_isRepresentableByAlgebraicSpaces_iff B S hS f a ha).mpr hf) ↔
      HasRelativeProperty B S hS P (CatFiberedInSetoids.inclusion.map f) hf
```

## Tag 045B, a lemma

[Tag 045B](https://stacks.math.columbia.edu/tag/045B) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasRelativeProperty_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyComp.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyComp.lean#L301).

> **Stacks 045B.** Let `P` be a property of morphisms of algebraic spaces over `S` which is
> stable under base change, local on the target for the fppf precoverage, and stable under
> composition. If two composable 1-morphisms of categories fibred in groupoids over the big fppf
> site of `S` are representable by algebraic spaces and have the relative property `P` of Stacks
> 03YK, then so does their composite.

```lean
theorem hasRelativeProperty_comp
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsStableUnderBaseChange]
    [P.IsLocalAtTarget (Space.Topology.fppf.precoverage.{u, t} B S hS)]
    [P.IsStableUnderComposition]
    {𝒳 𝒴 𝒵 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)}
    (f : 𝒳 ⟶ 𝒴) (g : 𝒴 ⟶ 𝒵)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom)
    (hg : IsRepresentableByAlgebraicSpaces B S hS g.hom)
    (hPf : HasRelativeProperty B S hS P f hf)
    (hPg : HasRelativeProperty B S hS P g hg) :
    HasRelativeProperty B S hS P (f ≫ g)
      (isRepresentableByAlgebraicSpaces_comp B S hS f g hf hg)
```

## Tag 045C, a lemma

[Tag 045C](https://stacks.math.columbia.edu/tag/045C) in the Stacks Project.

**`AlgebraicGeometry.Stack.isImmersion_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionBaseChange.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionBaseChange.lean#L67). The attribute's comment: “the immersion property of Stacks 04XB, for the first projection”.

> **Stacks 045C at the immersion property of Stacks 04XB.** In a 2-fibre product square over a
> cospan `g : 𝒵 ⟶ 𝒴`, `f : 𝒳 ⟶ 𝒴` of categories fibred in groupoids over the big fppf site of `S`,
> the projection to `𝒵` is an immersion as soon as `f` is.

```lean
theorem isImmersion_baseChange
    (𝒳 𝒴 𝒵 : CatFiberedInGroupoids.{u, max u v, u + 1, max (max (u + 1) w) v}
      (BigFppfOver B S hS))
    (f : 𝒳 ⟶ 𝒴) (g : 𝒵 ⟶ 𝒴)
    (R : Bicategory.TwoCommSq g f) (hR : Bicategory.IsTwoFibreProduct R)
    (hf : Stack.IsImmersion B S hS f) :
    Stack.IsImmersion B S hS R.fst
```

**`AlgebraicGeometry.Stack.isImmersion_twoFibreProductSnd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionBaseChange.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionBaseChange.lean#L83). The attribute's comment: “the immersion property of Stacks 04XB, for the canonical second projection”.

> **Stacks 045C at the immersion property, for the second projection.** The second projection
> of the canonical 2-fibre product square over a cospan `(g, f)` of categories fibred in groupoids
> is an immersion as soon as `g` is.

```lean
theorem isImmersion_twoFibreProductSnd
    {𝒵 𝒴 𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS)}
    (g : 𝒵 ⟶ 𝒴) (f : 𝒳 ⟶ 𝒴) (hg : Stack.IsImmersion B S hS g) :
    Stack.IsImmersion B S hS
      (CatFiberedInGroupoids.twoFibreProductSquare.{u, u, u + 1, u + 1} g f).snd
```

**`AlgebraicGeometry.Stack.isImmersion_snd_of_isTwoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionBaseChange.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionBaseChange.lean#L110). The attribute's comment: “the immersion property of Stacks 04XB, at a 2-fibre product of algebraic stacks”.

> **Stacks 045C at the immersion property, for the second projection of a 2-fibre product
> square of algebraic stacks.** If `g : 𝒵 ⟶ 𝒴` is an immersion in the sense of Stacks 04XB and `P`
> is a 2-fibre product of the cospan `(g, f)` in the 2-category of algebraic stacks, then so is
> `P.snd : P.pt ⟶ 𝒳`.
>
> The statement is obtained at the canonical square — where the stronger terminality hypothesis of
> Stacks 045C holds unconditionally — and transported to `P` along the comparison 1-morphism by
> Stacks 0457 for the relative property.

```lean
theorem isImmersion_snd_of_isTwoFibreProduct
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P)
    (hg : Stack.IsImmersion B S hS g.hom) :
    Stack.IsImmersion B S hS P.snd.hom
```

**`AlgebraicGeometry.Stack.AlgebraicStacks.isImmersion_snd_of_isTwoFibreProduct`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ImmersionBaseChange.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ImmersionBaseChange.lean#L143). The attribute's comment: “the immersion property of Stacks 04XB, conjoined with representability, at a 2-fibre product of algebraic stacks”.

> Base change of an immersion of algebraic stacks. If `g : 𝒵 ⟶ 𝒴` is an immersion of
> algebraic stacks over `S` and `P` is a 2-fibre product of the cospan `(g, f)` in the 2-category of
> algebraic stacks, then `P.snd : P.pt ⟶ 𝒳` is an immersion of algebraic stacks.
>
> Both halves are base-change statements: representability by algebraic spaces is Stacks 0302 and
> the immersion property of Stacks 04XB is Stacks 045C. The attribute records the latter, at the
> level of algebraic stacks. It deliberately does **not** record Stacks 04YL: that tag is a
> definition — its three parts define open immersions, closed immersions and immersions in terms
> of Section 04XB — and says nothing about stability under base change, so a theorem must not
> carry it. The definition itself is carried by `AlgebraicStacks.IsImmersion`.

```lean
theorem isImmersion_snd_of_isTwoFibreProduct
    (P : Bicategory.TwoCommSq g f) (hP : Bicategory.IsTwoFibreProduct P)
    (hg : IsImmersion B S hS g) :
    IsImmersion B S hS P.snd
```

**`AlgebraicGeometry.Stack.hasRelativeProperty_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyBaseChange.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyBaseChange.lean#L135).

> **Stacks 045C.** Let `P` be a property of morphisms of algebraic spaces over `S` which is
> stable under base change and local on the target for the fppf precoverage. In a 2-fibre product
> square over a cospan `g : 𝒵 ⟶ 𝒴`, `f : 𝒳 ⟶ 𝒴` of categories fibred in groupoids over the big
> fppf site of `S`, the projection to `𝒵` has the relative property `P` of Stacks 03YK as soon as
> `f` does.

```lean
theorem hasRelativeProperty_baseChange
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsStableUnderBaseChange]
    [P.IsLocalAtTarget (Space.Topology.fppf.precoverage B S hS)]
    (𝒳 𝒴 𝒵 : CatFiberedInGroupoids.{u, max u v, u + 1, max (max (u + 1) w) v}
      (BigFppfOver B S hS))
    (f : 𝒳 ⟶ 𝒴) (g : 𝒵 ⟶ 𝒴)
    (R : Bicategory.TwoCommSq g f)
    (hR : Bicategory.IsTwoFibreProduct R)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom)
    (hPf : HasRelativeProperty B S hS P f hf) :
    HasRelativeProperty B S hS P R.fst
      (isRepresentableByAlgebraicSpaces_baseChange.{u, v, w} B S hS 𝒳 𝒴 𝒵 f g R hR hf)
```

## Tag 045D, a lemma

[Tag 045D](https://stacks.math.columbia.edu/tag/045D) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasRelativeProperty_of_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyDescent.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyDescent.lean#L266).

> **Stacks 045D.** Let `P` be a property of morphisms of algebraic spaces over `S` which is
> stable under base change and local on the target for the fppf precoverage, let `f : 𝒳 ⟶ 𝒴` be a
> 1-morphism of categories fibred in groupoids over the big fppf site of `S` representable by
> algebraic spaces and let `g : 𝒵 ⟶ 𝒴` be any 1-morphism. Assume that every object of a fibre of
> `𝒴` becomes, after restriction to a covering sieve, isomorphic to the image of an object of `𝒵`.
> Then in a 2-fibre product square over the cospan `(g, f)`, if the projection to `𝒵` has the
> relative property `P` of Stacks 03YK, so does `f`.
>
> This is `AlgebraicGeometry.Stack.relativeProperty_of_baseChange` with the representability of `f`
> assumed as the source assumes it, which is what names the relative property of Stacks 03YK on
> both sides.

```lean
theorem hasRelativeProperty_of_baseChange
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    (𝒳 𝒴 𝒵 : CatFiberedInGroupoids.{u, max u v, u + 1, max (max (u + 1) w) v}
      (BigFppfOver B S hS))
    (P : MorphismProperty (AlgebraicSpaces B S hS))
    [P.IsStableUnderBaseChange]
    [P.IsLocalAtTarget (Space.Topology.fppf.precoverage.{u, max u t} B S hS)]
    (f : 𝒳 ⟶ 𝒴) (g : 𝒵 ⟶ 𝒴)
    (D : Bicategory.TwoCommSq g f)
    (hD : Bicategory.IsTwoFibreProduct D)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom)
    (hg : ∀ (U : BigFppfOver B S hS) (y : 𝒴.val.p.Fiber U),
      ∃ R ∈ BigFppfOver.topology B S hS U,
        ∀ ⦃V : BigFppfOver B S hS⦄ ⦃k : V ⟶ U⦄, R.arrows k →
          ∃ z : 𝒵.val.obj, ∃ φ : (CatFiberedInGroupoids.homFunctor g).obj z ⟶ y.1,
            𝒴.val.p.IsHomLift k φ)
    (hP : HasRelativeProperty B S hS P D.fst
      (isRepresentableByAlgebraicSpaces_baseChange.{u, v, w} B S hS 𝒳 𝒴 𝒵 f g D hD hf)) :
    HasRelativeProperty B S hS P f hf
```

## Tag 045E, a lemma

[Tag 045E](https://stacks.math.columbia.edu/tag/045E) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasRelativeProperty_productMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/ProductRelativeProperty.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/ProductRelativeProperty.lean#L140).

> **Stacks 045E.** A property of morphisms of algebraic spaces over `S` which is stable under
> base change, local on the target for the fppf precoverage and stable under composition, and which
> holds relatively for two 1-morphisms of categories fibred in groupoids over the big fppf site of
> `S` representable by algebraic spaces, holds relatively for their product.
>
> The product factors as `(f₁ × id_{𝒳₂}) ∘ (id_{𝒴₁} × f₂)`; the two factors are handled by
> `AlgebraicGeometry.Stack.hasRelativeProperty_productMap_id_right` and `…_id_left`, and the
> composite by Stacks 045B.

```lean
theorem hasRelativeProperty_productMap (f₁ : 𝒳₁ ⟶ 𝒴₁) (f₂ : 𝒳₂ ⟶ 𝒴₂)
    (hf₁ : IsRepresentableByAlgebraicSpaces B S hS f₁.hom)
    (hf₂ : IsRepresentableByAlgebraicSpaces B S hS f₂.hom)
    (hP₁ : HasRelativeProperty.{u, _, _, t} B S hS P f₁ hf₁)
    (hP₂ : HasRelativeProperty.{u, _, _, t} B S hS P f₂ hf₂) :
    HasRelativeProperty.{u, _, _, t} B S hS P (productMap f₁ f₂)
      (isRepresentableByAlgebraicSpaces_productMap B S hS f₁ f₂ hf₁ hf₂)
```

## Tag 045F, a lemma

[Tag 045F](https://stacks.math.columbia.edu/tag/045F) in the Stacks Project.

**`AlgebraicGeometry.Stack.hasRelativeProperty_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyMono.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/RelativePropertyMono.lean#L58).

> **Stacks 045F.** If a property `P` of morphisms of algebraic spaces over `S` implies a
> property `P'`, then a 1-morphism of categories fibred in groupoids over `(Sch/S)_fppf` which is
> representable by algebraic spaces and has the relative property `P` of Stacks 03YK also has the
> relative property `P'`.
>
> The relative property is a universally quantified statement in which the property occurs only in
> the conclusion, so the implication applies under the quantifiers.

```lean
theorem hasRelativeProperty_mono
    {P P' : MorphismProperty (AlgebraicSpaces B S hS)}
    [P.IsStableUnderBaseChange] [P.IsLocalAtTarget (Space.Topology.fppf.precoverage B S hS)]
    [P'.IsStableUnderBaseChange] [P'.IsLocalAtTarget (Space.Topology.fppf.precoverage B S hS)]
    (hPP' : P ≤ P')
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)} {f : 𝒳 ⟶ 𝒴}
    (hf : IsRepresentableByAlgebraicSpaces B S hS f.hom)
    (hP : HasRelativeProperty B S hS P f hf) :
    HasRelativeProperty B S hS P' f hf
```

## Tag 05UK, a lemma

[Tag 05UK](https://stacks.math.columbia.edu/tag/05UK) in the Stacks Project.

**`AlgebraicGeometry.Stack.full_and_faithful_homFunctor_of_mono_representingMaps`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismFullyFaithful.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/MonomorphismFullyFaithful.lean#L276).

> **Stacks 05UK, with Stacks 003Z: the implication (1) ⟹ (2) of Stacks 04ZZ.** A 1-morphism
> `j : 𝒳 ⟶ 𝒴` of categories fibred in groupoids over the big fppf site of `S` which is
> representable by algebraic spaces and all of whose representing structural morphisms are
> monomorphisms has fully faithful underlying functor.
>
> Faithfulness is Stacks 04Y5 and uses only representability. For fullness: a morphism of the fibre
> `𝒴_U` out of `j(a)` makes a second object of the fibre of `(Sch/U)_fppf ×_𝒴 𝒳` over the terminal
> object of `(Sch/U)_fppf`, next to the one given by `a` itself; the representing algebraic space
> has at most one section there because its structural morphism is injective on sections, so the two
> objects are isomorphic and the `𝒳`-component of the isomorphism is the preimage sought.

```lean
theorem full_and_faithful_homFunctor_of_mono_representingMaps
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 𝒴 : CatFiberedInGroupoids.{u, v, u + 1, w} (BigFppfOver B S hS)} (j : 𝒳 ⟶ 𝒴)
    (hj : IsRepresentableByAlgebraicSpaces B S hS j.hom)
    (hmono : ∀ (U : BigFppfOver B S hS)
      (y : BigFppfOver B U.left.1 U.left.2 ⥤ 𝒴.val.obj)
      (_hy : y ⋙ 𝒴.val.p = Over.map U.hom)
      (F : (BigFppfOver B U.left.1 U.left.2)ᵒᵖ ⥤ Type u)
      (hF : IsAlgebraicSpace B U.left.1 U.left.2 F),
        Nonempty (StacksRepresentableCFG.EquivalenceOver
          (TwoFibreProductOver.fst (Over.map U.hom) 𝒳.val.p 𝒴.val.p y
            (CatFiberedInGroupoids.homFunctor j))
          (presheafOfCategories (F ⋙ typeToCat)).p) →
        Mono (algebraicSpaceMap B S hS U
          ((spacesOverSmallerBaseFunctor B U.left.1 S U.left.2 hS U.hom).obj ⟨F, hF⟩)).hom) :
    (CatFiberedInGroupoids.homFunctor j).Full ∧
      (CatFiberedInGroupoids.homFunctor j).Faithful
```

## Tag 045G, a lemma

[Tag 045G](https://stacks.math.columbia.edu/tag/045G) in the Stacks Project.

**`AlgebraicGeometry.isRepresentableFromSchemes_iff_isRepresentableFromRepresentableCategories`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Algebraic/RepresentableDiagonal/SchemeAndRepresentableSources.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Algebraic/RepresentableDiagonal/SchemeAndRepresentableSources.lean#L164). The attribute's comment: “parts (3) and (5)”.

> **Stacks 045G, conditions (3) and (5).** For a category fibred in groupoids `𝒳` over the big
> fppf site of `S`, every 1-morphism to `𝒳` out of a slice of the site is representable by
> algebraic spaces if and only if every 1-morphism to `𝒳` out of a representable category fibred
> in groupoids is.

```lean
public theorem isRepresentableFromSchemes_iff_isRepresentableFromRepresentableCategories :
    IsRepresentableFromSchemes B S hS 𝒳 ↔
      IsRepresentableFromRepresentableCategories.{u, v, w, u, u + 1} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.hasRepresentableDiagonal_iff_isAlgebraicSpaceIsomPresheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DiagonalCriteria.lean, line 42](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DiagonalCriteria.lean#L42). The attribute's comment: “parts (1) and (2)”.

> The diagonal of a category fibred in groupoids over the big fppf site of `S` is representable
> by algebraic spaces if and only if every isomorphism sheaf `Isom(x, y)` of two objects of a fibre
> is an algebraic space over the scheme the fibre sits over.

```lean
theorem hasRepresentableDiagonal_iff_isAlgebraicSpaceIsomPresheaf :
    HasRepresentableDiagonal B S hS 𝒳 ↔ IsAlgebraicSpaceIsomPresheaf B S hS 𝒳
```

**`AlgebraicGeometry.Stack.isRepresentableFromAlgebraicSpaces_iff_hasAlgebraicSpaceProducts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DiagonalCriteriaAlgebraicSpaceProducts.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DiagonalCriteriaAlgebraicSpaceProducts.lean#L109). The attribute's comment: “parts (7) and (8)”.

> **Stacks 045G, the equivalence of conditions (7) and (8).** Every 1-morphism to `𝒳` out of a
> category fibred in groupoids representable by an algebraic space over `S` is representable by
> algebraic spaces if and only if the 2-fibre product over `𝒳` of any two such 1-morphisms is
> representable by an algebraic space.

```lean
theorem isRepresentableFromAlgebraicSpaces_iff_hasAlgebraicSpaceProducts :
    IsRepresentableFromAlgebraicSpaces.{u, v, w, v₁, w₁} B S hS 𝒳 ↔
      HasAlgebraicSpaceProducts.{u, v, w, v₁, w₁, v₂, w₂} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.hasAlgebraicSpaceRepresentableProducts_iff_isRepresentableFromAlgebraicSpaces`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DiagonalCriteriaAlgebraicSpaceSources.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DiagonalCriteriaAlgebraicSpaceSources.lean#L207). The attribute's comment: “parts (6) and (7)”.

> **Stacks 045G, the equivalence of conditions (6) and (7).** The 2-fibre product over `𝒳` of
> any two 1-morphisms out of representable categories fibred in groupoids is representable by an
> algebraic space if and only if every 1-morphism to `𝒳` out of a category fibred in groupoids
> representable by an algebraic space is representable by algebraic spaces.

```lean
theorem hasAlgebraicSpaceRepresentableProducts_iff_isRepresentableFromAlgebraicSpaces :
    HasAlgebraicSpaceRepresentableProducts.{u, v, w, v₁, w₁, v₂, w₂} B S hS 𝒳 ↔
      IsRepresentableFromAlgebraicSpaces.{u, v, w, v₁, w₁} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.isAlgebraicSpaceIsomPresheaf_iff_isRepresentableFromSchemes`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DiagonalCriteriaProductsToDiagonal.lean, line 434](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DiagonalCriteriaProductsToDiagonal.lean#L434). The attribute's comment: “parts (2) and (3)”.

> **Stacks 045G, the equivalence of conditions (2) and (3).** Every isomorphism sheaf
> `Isom(x, y)` of two objects of a fibre of `𝒳` is an algebraic space over the scheme the fibre sits
> over if and only if every 1-morphism to `𝒳` from the category represented by a scheme over `S` is
> representable by algebraic spaces.

```lean
theorem isAlgebraicSpaceIsomPresheaf_iff_isRepresentableFromSchemes :
    IsAlgebraicSpaceIsomPresheaf B S hS 𝒳 ↔ IsRepresentableFromSchemes B S hS 𝒳
```

**`AlgebraicGeometry.Stack.representableFromCategories_iff_algebraicSpaceProducts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DiagonalCriteriaRepresentableProducts.lean, line 144](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DiagonalCriteriaRepresentableProducts.lean#L144). The attribute's comment: “parts (5) and (6)”.

> **Stacks 045G, the equivalence of conditions (5) and (6).** Every 1-morphism to `𝒳` from a
> representable category fibred in groupoids is representable by algebraic spaces if and only if the
> 2-fibre product over `𝒳` of any two such 1-morphisms is representable by an algebraic space.

```lean
theorem representableFromCategories_iff_algebraicSpaceProducts :
    IsRepresentableFromRepresentableCategories.{u, v, w, v₁, w₁} B S hS 𝒳 ↔
      HasAlgebraicSpaceRepresentableProducts.{u, v, w, v₁, w₁, v₂, w₂} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.hasAlgebraicSpaceSchemePointProducts_iff_isRepresentableFromRepresentableCategories`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DiagonalCriteriaRepresentableSources.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DiagonalCriteriaRepresentableSources.lean#L126). The attribute's comment: “parts (4) and (5)”.

> **Stacks 045G, the equivalence of conditions (4) and (5).** The 2-fibre product over `𝒳` of
> any two scheme-valued points of `𝒳` is representable by an algebraic space if and only if every
> 1-morphism to `𝒳` from a representable category fibred in groupoids is representable by algebraic
> spaces.

```lean
theorem hasAlgebraicSpaceSchemePointProducts_iff_isRepresentableFromRepresentableCategories :
    HasAlgebraicSpaceSchemePointProducts B S hS 𝒳 ↔
      IsRepresentableFromRepresentableCategories.{u, v, w, v₁, w₁} B S hS 𝒳
```

**`AlgebraicGeometry.Stack.isRepresentableFromSchemes_iff_hasAlgebraicSpaceSchemePointProducts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DiagonalCriteriaSchemePoints.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/DiagonalCriteriaSchemePoints.lean#L79). The attribute's comment: “parts (3) and (4)”.

> Every 1-morphism to `𝒳` from the category represented by a scheme over `S` is representable
> by algebraic spaces if and only if the 2-fibre product over `𝒳` of any two such 1-morphisms is
> representable by an algebraic space.

```lean
theorem isRepresentableFromSchemes_iff_hasAlgebraicSpaceSchemePointProducts :
    IsRepresentableFromSchemes B S hS 𝒳 ↔ HasAlgebraicSpaceSchemePointProducts B S hS 𝒳
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 94.10, Tag 03YJ](https://stacks.math.columbia.edu/tag/03YJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
