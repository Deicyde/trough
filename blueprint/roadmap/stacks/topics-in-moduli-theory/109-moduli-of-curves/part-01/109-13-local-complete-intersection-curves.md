---
declaration: section
origin: cited
lean: AlgebraicGeometry.isLciFamily_iff_isSyntomicFamily, AlgebraicGeometry.curvesLci_isStrictlyFull, AlgebraicGeometry.CurvesLci, AlgebraicGeometry.isLciFamily_curveFamilyOfSchemeMorphism_iff, AlgebraicGeometry.factorsThroughCurvesLci_iff, AlgebraicGeometry.factorsThroughCurvesLci_over_field_iff, AlgebraicGeometry.isOpenImmersion_curvesSubstackInclusion_lci, AlgebraicGeometry.factorsThrough_curvesSubstack_lci_tfae
statement: formalized
proof: formalized
---

# 109.13 Local complete intersection curves

Section 109.13 of the Stacks Project, [Tag 0E0J](https://stacks.math.columbia.edu/tag/0E0J). 1 tag here is carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DZV, a lemma

[Tag 0DZV](https://stacks.math.columbia.edu/tag/0DZV) in the Stacks Project.

**`AlgebraicGeometry.isLciFamily_iff_isSyntomicFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersection.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersection.lean#L135). The attribute's comment: “part (1), the equivalence of (b) and (c) for a family of curves: its structure morphism is a local complete intersection morphism if and only if it is syntomic”.

> **Stacks 0DZV, part (1).** The equivalence of conditions (b) and (c): a family of curves has
> a local complete intersection structure morphism exactly when its structure morphism is syntomic.
>
> A syntomic morphism of algebraic spaces is one which is flat and a local complete intersection
> morphism, by Tag 06C9, and the structure morphism of a family of curves is flat, so the flatness
> half of that conjunction is supplied by the family itself.

```lean
theorem isLciFamily_iff_isSyntomicFamily (X : CurveFamily B hZ) :
    IsLciFamily B hZ X ↔ Space.IsSyntomic B integerBase hZ X.toBase.hom
```

**`AlgebraicGeometry.curvesLci_isStrictlyFull`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersection.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersection.lean#L174). The attribute's comment: “strict fullness of the local complete intersection subcategory of the category of families of curves, which is the first of the three conditions of Tag 04YM making it an open substack; the remaining two rest on the algebraicity of the stack of curves (Tag 0D5A), which this library does not have”.

> **Stacks 0DZV.** The condition that a family of curves have a local complete intersection
> structure morphism is invariant under isomorphism, so `Curves^{lci}` is a strictly full
> subcategory of the category of families of curves: the first of the three conditions making it an
> open substack.
>
> An isomorphism of families of curves is a morphism of families, so this is base-change invariance
> of the condition applied to the inverse isomorphism.

```lean
theorem curvesLci_isStrictlyFull :
    (show ObjectProperty (CurveFamily B hZ) from
      IsLciFamily B hZ).IsClosedUnderIsomorphisms
```

**`AlgebraicGeometry.CurvesLci`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersection.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersection.lean#L185). The attribute's comment: “the local complete intersection subcategory of the category of families of curves, which is the underlying full subcategory of the open substack Curves^{lci} of the source; the stack of curves is not constructed in this library, so this is a subcategory of the category of families of curves of Tag 0D4Z and not an open substack of a stack”.

> **Stacks 0DZV.** The subcategory `Curves^{lci}`: the strictly full subcategory of families of
> curves whose structure morphism is a local complete intersection morphism.

```lean
abbrev CurvesLci
```

**`AlgebraicGeometry.isLciFamily_curveFamilyOfSchemeMorphism_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersection.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersection.lean#L211). The attribute's comment: “part (2), condition (b): for the family of curves attached to a proper flat morphism of schemes of finite presentation whose source has dimension at most one, the structure morphism of the family is a local complete intersection morphism if and only if that morphism of schemes is one, i.e. — over the spectrum of a field — if and only if the proper scheme is a local complete intersection over the field”.

> **Stacks 0DZV, part (2).** Condition (b) read on the family of curves attached to a proper
> flat morphism of schemes of finite presentation whose source has dimension at most one: that
> family has a local complete intersection structure morphism exactly when the morphism of schemes
> is a local complete intersection morphism.
>
> Over the spectrum of a field the right-hand side is the condition that the proper scheme be a
> local complete intersection over that field, which is condition (b) of part (2) of the source;
> see `AlgebraicGeometry.factorsThroughCurvesLci_over_field_iff`. No hypothesis on the base is
> needed, so the statement is proved over an arbitrary base scheme of the site.
>
> Both sides pass through syntomicity. The every-étale-chart condition of Tag 03MJ at a morphism of
> the site is the scheme-level condition itself for a property étale local on the source and target,
> which syntomicity is by Tag 04R3; at the level of schemes syntomicity is flatness together with
> the local complete intersection property by Tag 069K, and the morphism is flat by hypothesis; at
> the level of algebraic spaces it is the same conjunction by Tag 06C9, whose flatness half the
> family supplies.

```lean
theorem isLciFamily_curveFamilyOfSchemeMorphism_iff
    {T W : BigFppfOver B integerBase hZ} (g : T ⟶ W)
    (hflat : Flat ((BigFppfOver.toScheme B integerBase hZ).map g))
    (hproper : IsProper ((BigFppfOver.toScheme B integerBase hZ).map g))
    (hlfp : LocallyOfFinitePresentation ((BigFppfOver.toScheme B integerBase hZ).map g))
    (hqc : Space.IsQuasiCompact B integerBase hZ (schemeSpaceMap g).hom)
    (hsep : Space.IsSeparated B integerBase hZ (schemeSpaceMap g).hom)
    (hqsep : Space.IsQuasiSeparated B integerBase hZ (schemeSpaceMap g).hom)
    (hdim : topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) ≤ 1) :
    IsLciFamily B hZ
        (curveFamilyOfSchemeMorphism B hZ g hflat hproper hlfp hqc hsep hqsep hdim) ↔
      IsLocalCompleteIntersectionMorphism
        ((BigFppfOver.toScheme B integerBase hZ).map g)
```

**`AlgebraicGeometry.factorsThroughCurvesLci_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersection.lean, line 258](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersection.lean#L258). The attribute's comment: “part (1), the equivalence of (a) and (b): the classifying 1-morphism factors through the local complete intersection substack if and only if every family of curves in its image has a local complete intersection structure morphism. The stack of curves is not constructed in this library (Tag 0D5A is not proved here), so the algebraic stack, the identification of its objects with families of curves, and the open substack together with its specification are carried as explicit named hypotheses”.

> **Stacks 0DZV, part (1).** The equivalence of conditions (a) and (b). Let `𝒳` be an algebraic
> stack over the big fppf site of the integers whose objects are identified with families of curves
> by `Φ`, and let `V` be an open substack of `𝒳` whose objects are exactly those identified with
> families having a local complete intersection structure morphism. Then a 1-morphism into `𝒳` from
> a category over the site factors through `V`, over the site and up to a 2-isomorphism, if and only
> if every family of curves in its image has a local complete intersection structure morphism.
>
> This result **assumes** what Stacks 0D5A would supply and this library does not have: an algebraic
> stack of curves, and the fact that the local complete intersection condition cuts an open substack
> out of it. Granted those, it is the criterion of Stacks 0507 together with the translation of
> membership of the substack into the condition on the corresponding family.

```lean
theorem factorsThroughCurvesLci_iff
    {𝒳 : Stack.AlgebraicStacks.{u, w} B integerBase hZ}
    (Φ : 𝒳.val.val.obj ⥤ CurveFamily B hZ) (V : Stack.OpenSubstack 𝒳)
    (hV : ∀ Z : 𝒳.val.val.obj, V.property Z ↔ IsLciFamily B hZ (Φ.obj Z))
    {𝒟 : BasedCategory.{u, u + 1} (BigFppfOver B integerBase hZ)} (f : 𝒟 ⥤ᵇ 𝒳.val.val) :
    (∃ q : 𝒟 ⥤ᵇ Stack.fullSubcategoryBased 𝒳 V.property,
        Nonempty (q.comp (Stack.fullSubcategoryBasedInclusion 𝒳 V.property) ≅ f)) ↔
      ∀ Y : 𝒟.obj, IsLciFamily B hZ (Φ.obj (f.obj Y))
```

**`AlgebraicGeometry.factorsThroughCurvesLci_over_field_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersection.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersection.lean#L299). The attribute's comment: “part (2), the equivalence of (a) and (b): for a proper flat morphism of finite presentation from a scheme of dimension at most one to the spectrum of a field, the classifying 1-morphism factors through the local complete intersection substack if and only if the source is a local complete intersection over that field. As in part (1) the algebraic stack of curves, the identification of its objects with families of curves, and the open substack together with its specification are carried as explicit named hypotheses, the stack of curves not being constructed in this library. The hypothesis that the base be the spectrum of a field is kept, making this the instance the source states, but is not used: the equivalence holds over any base scheme of the site”.

> **Stacks 0DZV, part (2).** The equivalence of conditions (a) and (b) for a proper scheme over
> a field of dimension at most one. Let `X → Spec(k)` be a proper flat morphism of schemes of finite
> presentation over a field `k` whose source has dimension at most one, and let `f` be a 1-morphism
> into the stack of curves all of whose objects classify the attached family of curves. Then `f`
> factors through the local complete intersection open substack exactly when `X` is a local complete
> intersection over `k`, that is, exactly when `X → Spec(k)` is a local complete intersection
> morphism.
>
> The hypothesis `_hk` that the base be the spectrum of a field is what makes this the statement of
> part (2) of the source rather than a statement over an arbitrary base, and it is deliberately kept
> although the argument does not use it: the underlying equivalence
> `AlgebraicGeometry.isLciFamily_curveFamilyOfSchemeMorphism_iff` holds over an arbitrary base
> scheme of the site, so this statement is a strict instance of it and nothing is weakened by its
> presence. Nonemptiness of the source category of `f` is used, to convert the universally
> quantified right-hand side of `AlgebraicGeometry.factorsThroughCurvesLci_iff` into the single
> condition the source states. Properness, finite presentation, flatness and the dimension bound are
> the hypotheses of `AlgebraicGeometry.curveFamilyOfSchemeMorphism` and are all used, through it.
>
> Like `AlgebraicGeometry.factorsThroughCurvesLci_iff` this **assumes** an algebraic stack of curves
> and that the condition cuts an open substack out of it; neither is available in this library,
> Stacks 0D5A not being proved here.

```lean
theorem factorsThroughCurvesLci_over_field_iff
    {𝒳 : Stack.AlgebraicStacks.{u, w} B integerBase hZ}
    (Φ : 𝒳.val.val.obj ⥤ CurveFamily B hZ) (V : Stack.OpenSubstack 𝒳)
    (hV : ∀ Z : 𝒳.val.val.obj, V.property Z ↔ IsLciFamily B hZ (Φ.obj Z))
    {T W : BigFppfOver B integerBase hZ} (g : T ⟶ W)
    (hflat : Flat ((BigFppfOver.toScheme B integerBase hZ).map g))
    (hproper : IsProper ((BigFppfOver.toScheme B integerBase hZ).map g))
    (hlfp : LocallyOfFinitePresentation ((BigFppfOver.toScheme B integerBase hZ).map g))
    (hqc : Space.IsQuasiCompact B integerBase hZ (schemeSpaceMap g).hom)
    (hsep : Space.IsSeparated B integerBase hZ (schemeSpaceMap g).hom)
    (hqsep : Space.IsQuasiSeparated B integerBase hZ (schemeSpaceMap g).hom)
    (hdim : topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) ≤ 1)
    (k : Type u) [Field k]
    (_hk : (BigFppfOver.toScheme B integerBase hZ).obj W = Spec (.of k))
    {𝒟 : BasedCategory.{u, u + 1} (BigFppfOver B integerBase hZ)} (f : 𝒟 ⥤ᵇ 𝒳.val.val)
    (hne : Nonempty 𝒟.obj)
    (hf : ∀ Y : 𝒟.obj, Φ.obj (f.obj Y) =
      curveFamilyOfSchemeMorphism B hZ g hflat hproper hlfp hqc hsep hqsep hdim) :
    (∃ q : 𝒟 ⥤ᵇ Stack.fullSubcategoryBased 𝒳 V.property,
        Nonempty (q.comp (Stack.fullSubcategoryBasedInclusion 𝒳 V.property) ≅ f)) ↔
      IsLocalCompleteIntersectionMorphism
        ((BigFppfOver.toScheme B integerBase hZ).map g)
```

**`AlgebraicGeometry.isOpenImmersion_curvesSubstackInclusion_lci`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersectionSubstack.lean, line 101](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersectionSubstack.lean#L101). The attribute's comment: “the inclusion of Curves^{lci} into Curves is representable by algebraic spaces and an open immersion”.

> **Stacks 0DZV, `Curves^{lci}` is open in `Curves`.** The inclusion into the category fibred
> in groupoids of families of curves of the full subcategory `Curves^{lci}` of the families whose
> structure morphism is a local complete intersection morphism is representable by algebraic spaces
> and an open immersion.

```lean
theorem isOpenImmersion_curvesSubstackInclusion_lci :
    Stack.IsRepresentableByAlgebraicSpaces B integerBase hZ
        (curvesSubstackInclusion B hZ (IsLciFamily B hZ)
          (isOpenCurvesLocus_isLciFamily B hZ).prop_of_hom).hom ∧
      Stack.IsOpenImmersion B integerBase hZ
        (curvesSubstackInclusion B hZ (IsLciFamily B hZ)
          (isOpenCurvesLocus_isLciFamily B hZ).prop_of_hom)
```

**`AlgebraicGeometry.factorsThrough_curvesSubstack_lci_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersectionSubstack.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersectionSubstack.lean#L118). The attribute's comment: “part (1)”.

> **Stacks 0DZV, part (1).** Let `X → S` be a family of curves and `z : (Sch/S) → Curves` a
> classifying morphism for it, a scheme-valued point together with an isomorphism `z(S) ≅ X`.
> Then the following are equivalent:
>
> * (a) `z` factors through `Curves^{lci}`, over the site and up to a 2-isomorphism;
> * (b) `X → S` is a local complete intersection morphism;
> * (c) `X → S` is syntomic.

```lean
theorem factorsThrough_curvesSubstack_lci_tfae (S : BigFppfOver B integerBase hZ)
    (z : BigFppfOver B S.left.1 S.left.2 ⥤ (curvesFiberedCategory B hZ).val.obj)
    (hz : z ⋙ (curvesFiberedCategory B hZ).val.p = Over.map S.hom)
    (X : CurveFamily B hZ) (ξ : z.obj (Over.mk (𝟙 S.left)) ≅ X) :
    List.TFAE
      [∃ g : BasedCategory.ofFunctor (Over.map S.hom) ⥤ᵇ
            Stack.objectPropertySubcategory B integerBase hZ
              (curvesFiberedCategory B hZ).val (IsLciFamily B hZ),
          Nonempty (g.comp (Stack.objectPropertyInclusion B integerBase hZ
            (curvesFiberedCategory B hZ).val (IsLciFamily B hZ)) ≅ { toFunctor := z, w := hz }),
        Space.IsLocalCompleteIntersection B integerBase hZ X.toBase.hom,
        Space.IsSyntomic B integerBase hZ X.toBase.hom]
```

**`AlgebraicGeometry.factorsThrough_curvesSubstack_lci_over_field_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersectionSubstack.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersectionSubstack.lean#L142). The attribute's comment: “part (2)”.

> **Stacks 0DZV, part (2).** Let `g : T ⟶ W` be a morphism of the big fppf site of the integers
> whose target scheme is the spectrum of a field `k`, whose underlying morphism of schemes is
> proper, and whose source scheme `X` has dimension at most one, and let `z : (Sch/Spec(k)) →
> Curves` classify the family of curves of `g`. Then `z` factors through `Curves^{lci}` if and only
> if `X` is a local complete intersection over `k`, that is, `g` is a local complete intersection
> morphism.

```lean
theorem factorsThrough_curvesSubstack_lci_over_field_iff
    {T W : BigFppfOver B integerBase hZ} (g : T ⟶ W) (k : Type u) [Field k]
    (hW : (BigFppfOver.toScheme B integerBase hZ).obj W = Spec (.of k))
    (hproper : IsProper ((BigFppfOver.toScheme B integerBase hZ).map g))
    (hdim : topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) ≤ 1)
    (z : BigFppfOver B W.left.1 W.left.2 ⥤ (curvesFiberedCategory B hZ).val.obj)
    (hz : z ⋙ (curvesFiberedCategory B hZ).val.p = Over.map W.hom)
    (ξ : z.obj (Over.mk (𝟙 W.left)) ≅ curveFamilyOfSchemeMorphism B hZ g
      (flat_of_eq_spec_field _ k hW) hproper
      (locallyOfFinitePresentation_of_eq_spec_field _ k hW)
      (Space.isQuasiCompact_yoneda_map B integerBase hZ g inferInstance)
      ((Space.isSeparated_yoneda_map_iff B integerBase hZ g).2 inferInstance)
      ((Space.isQuasiSeparated_yoneda_map_iff B integerBase hZ g).2 inferInstance) hdim) :
    (∃ q : BasedCategory.ofFunctor (Over.map W.hom) ⥤ᵇ
          Stack.objectPropertySubcategory B integerBase hZ
            (curvesFiberedCategory B hZ).val (IsLciFamily B hZ),
        Nonempty (q.comp (Stack.objectPropertyInclusion B integerBase hZ
          (curvesFiberedCategory B hZ).val (IsLciFamily B hZ)) ≅
            { toFunctor := z, w := hz })) ↔
      IsLocalCompleteIntersectionMorphism ((BigFppfOver.toScheme B integerBase hZ).map g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 109.13, Tag 0E0J](https://stacks.math.columbia.edu/tag/0E0J)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
