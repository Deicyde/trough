---
declaration: section
origin: cited
lean: AlgebraicGeometry.isLciFamily_iff_isSyntomicFamily, AlgebraicGeometry.curvesLci_isStrictlyFull, AlgebraicGeometry.isLciFamily_curveFamilyOfSchemeMorphism_iff, AlgebraicGeometry.curvesLci, AlgebraicGeometry.factorsThrough_curvesLci_tfae, AlgebraicGeometry.factorsThrough_curvesLci_over_field_iff, AlgebraicGeometry.exists_openSubstack_curvesLci, AlgebraicGeometry.isOpenImmersion_curvesSubstackInclusion_lci
statement: formalized
proof: formalized
---

# 109.13 Local complete intersection curves

Section 109.13 of the Stacks Project, [Tag 0E0J](https://stacks.math.columbia.edu/tag/0E0J). 1 tag here is carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DZV, a lemma

[Tag 0DZV](https://stacks.math.columbia.edu/tag/0DZV) in the Stacks Project.

**`AlgebraicGeometry.isLciFamily_iff_isSyntomicFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersection.lean, line 135](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersection.lean#L135). The attribute's comment: “part (1), the equivalence of (b) and (c) for a family of curves: its structure morphism is a local complete intersection morphism if and only if it is syntomic”.

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

**`AlgebraicGeometry.curvesLci_isStrictlyFull`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersection.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersection.lean#L173). The attribute's comment: “strict fullness of the local complete intersection subcategory of the category of families of curves, which is the first of the three conditions of Tag 04YM making it an open substack”.

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

**`AlgebraicGeometry.isLciFamily_curveFamilyOfSchemeMorphism_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersection.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersection.lean#L208). The attribute's comment: “part (2), condition (b): for the family of curves attached to a proper flat morphism of schemes of finite presentation whose source has dimension at most one, the structure morphism of the family is a local complete intersection morphism if and only if that morphism of schemes is one, i.e. — over the spectrum of a field — if and only if the proper scheme is a local complete intersection over the field”.

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

**`AlgebraicGeometry.curvesLci`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersectionOpenSubstack.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersectionOpenSubstack.lean#L90). The attribute's comment: “the open substack Curves^\{lci} of the algebraic stack of curves”.

> **Stacks 0DZV, the open substack `Curves^{lci}`.** The open substack of the algebraic stack of
> curves (Stacks 0D5A) of the families of curves whose structure morphism is a local complete
> intersection morphism, cut out by the method of Section 0E0E.

```lean
abbrev curvesLci :
    Stack.OpenSubstack
      (curvesAlgebraicStack B hZ (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ))
```

**`AlgebraicGeometry.factorsThrough_curvesLci_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersectionOpenSubstack.lean, line 144](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersectionOpenSubstack.lean#L144). The attribute's comment: “part (1), on the open substack Curves^\{lci} of the algebraic stack of curves”.

> **Stacks 0DZV, part (1).** Let `X → S` be a family of curves and `z : (Sch/S) → Curves` a
> classifying morphism for it, a scheme-valued point of the algebraic stack of curves together with
> an isomorphism between the family it classifies at `S` and `X`. Then the following are
> equivalent:
>
> * (a) `z` factors through `Curves^{lci}`, over the site and up to a 2-isomorphism;
> * (b) `X → S` is a local complete intersection morphism;
> * (c) `X → S` is syntomic.

```lean
theorem factorsThrough_curvesLci_tfae (S : BigFppfOver B integerBase hZ)
    (z : BigFppfOver B S.left.1 S.left.2 ⥤
      (curvesAlgebraicStack B hZ
        (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ)).val.val.obj)
    (hz : z ⋙ (curvesAlgebraicStack B hZ
      (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ)).val.val.p = Over.map S.hom)
    (X : CurveFamily B hZ)
    (ξ : (curvesSmallEquivalence B hZ
      (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ)).inverse.obj
        (z.obj (Over.mk (𝟙 S.left))) ≅ X) :
    List.TFAE
      [∃ g : BasedCategory.ofFunctor (Over.map S.hom) ⥤ᵇ
            Stack.fullSubcategoryBased _ (curvesLci.{u, w} B hZ).property,
          Nonempty (g.comp (Stack.fullSubcategoryBasedInclusion _
            (curvesLci.{u, w} B hZ).property) ≅ { toFunctor := z, w := hz }),
        Space.IsLocalCompleteIntersection B integerBase hZ X.toBase.hom,
        Space.IsSyntomic B integerBase hZ X.toBase.hom]
```

**`AlgebraicGeometry.factorsThrough_curvesLci_over_field_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersectionOpenSubstack.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersectionOpenSubstack.lean#L172). The attribute's comment: “part (2), on the open substack Curves^\{lci} of the algebraic stack of curves”.

> **Stacks 0DZV, part (2).** Let `g : T ⟶ W` be a morphism of the big fppf site of the integers
> whose target scheme is the spectrum of a field `k`, whose underlying morphism of schemes is
> proper, and whose source scheme `X` has dimension at most one, and let `z : (Sch/Spec(k)) →
> Curves` classify the family of curves of `g`. Then `z` factors through `Curves^\{lci}` if and only
> if `X` is a local complete intersection over `k`, that is, `g` is a local complete intersection
> morphism.

```lean
theorem factorsThrough_curvesLci_over_field_iff
    {T W : BigFppfOver B integerBase hZ} (g : T ⟶ W) (k : Type u) [Field k]
    (hW : (BigFppfOver.toScheme B integerBase hZ).obj W = Spec (.of k))
    (hproper : IsProper ((BigFppfOver.toScheme B integerBase hZ).map g))
    (hdim : topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) ≤ 1)
    (z : BigFppfOver B W.left.1 W.left.2 ⥤
      (curvesAlgebraicStack B hZ
        (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ)).val.val.obj)
    (hz : z ⋙ (curvesAlgebraicStack B hZ
      (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ)).val.val.p = Over.map W.hom)
    (ξ : (curvesSmallEquivalence B hZ
      (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ)).inverse.obj
        (z.obj (Over.mk (𝟙 W.left))) ≅
      curveFamilyOfSchemeMorphism B hZ g (flat_of_eq_spec_field _ k hW) hproper
        (locallyOfFinitePresentation_of_eq_spec_field _ k hW)
        (Space.isQuasiCompact_yoneda_map B integerBase hZ g inferInstance)
        ((Space.isSeparated_yoneda_map_iff B integerBase hZ g).2 inferInstance)
        ((Space.isQuasiSeparated_yoneda_map_iff B integerBase hZ g).2 inferInstance) hdim) :
    (∃ q : BasedCategory.ofFunctor (Over.map W.hom) ⥤ᵇ
          Stack.fullSubcategoryBased _ (curvesLci.{u, w} B hZ).property,
        Nonempty (q.comp (Stack.fullSubcategoryBasedInclusion _
          (curvesLci.{u, w} B hZ).property) ≅ { toFunctor := z, w := hz })) ↔
      IsLocalCompleteIntersectionMorphism ((BigFppfOver.toScheme B integerBase hZ).map g)
```

**`AlgebraicGeometry.exists_openSubstack_curvesLci`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersectionOpenSubstack.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersectionOpenSubstack.lean#L210).

> **Stacks 0DZV.** There is an open substack `Curves^{lci}` of the algebraic stack of curves
> such that
>
> 1. for a family of curves `X → S` with classifying morphism `z : (Sch/S) → Curves`, the following
>    are equivalent: (a) `z` factors through `Curves^{lci}`, (b) `X → S` is a local complete
>    intersection morphism, (c) `X → S` is syntomic;
> 2. for a proper scheme `X` of dimension at most one over a field `k` (a morphism `g` of the site
>    to `Spec(k)`) with classifying morphism `z : (Sch/Spec(k)) → Curves`, `z` factors through
>    `Curves^{lci}` if and only if `X` is a local complete intersection over `k`.
>
> The open substack is `AlgebraicGeometry.curvesLci`.

```lean
theorem exists_openSubstack_curvesLci :
    ∃ U : Stack.OpenSubstack
        (curvesAlgebraicStack B hZ (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ)),
      (∀ (S : BigFppfOver B integerBase hZ)
        (z : BigFppfOver B S.left.1 S.left.2 ⥤
          (curvesAlgebraicStack B hZ
            (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ)).val.val.obj)
        (hz : z ⋙ (curvesAlgebraicStack B hZ
          (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ)).val.val.p = Over.map S.hom)
        (X : CurveFamily B hZ)
        (_ : (curvesSmallEquivalence B hZ
          (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ)).inverse.obj
            (z.obj (Over.mk (𝟙 S.left))) ≅ X),
        List.TFAE
          [∃ g : BasedCategory.ofFunctor (Over.map S.hom) ⥤ᵇ
                Stack.fullSubcategoryBased _ U.property,
              Nonempty (g.comp (Stack.fullSubcategoryBasedInclusion _ U.property) ≅
                { toFunctor := z, w := hz }),
            Space.IsLocalCompleteIntersection B integerBase hZ X.toBase.hom,
            Space.IsSyntomic B integerBase hZ X.toBase.hom]) ∧
      ∀ {T W : BigFppfOver B integerBase hZ} (g : T ⟶ W) (k : Type u) [Field k]
        (hW : (BigFppfOver.toScheme B integerBase hZ).obj W = Spec (.of k))
        (hproper : IsProper ((BigFppfOver.toScheme B integerBase hZ).map g))
        (hdim : topologicalKrullDim ((BigFppfOver.toScheme B integerBase hZ).obj T) ≤ 1)
        (z : BigFppfOver B W.left.1 W.left.2 ⥤
          (curvesAlgebraicStack B hZ
            (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ)).val.val.obj)
        (hz : z ⋙ (curvesAlgebraicStack B hZ
          (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ)).val.val.p = Over.map W.hom)
        (_ : (curvesSmallEquivalence B hZ
          (curvesFiberedCategory_isAlgebraicStack.{u, w} B hZ)).inverse.obj
            (z.obj (Over.mk (𝟙 W.left))) ≅
          curveFamilyOfSchemeMorphism B hZ g (flat_of_eq_spec_field _ k hW) hproper
            (locallyOfFinitePresentation_of_eq_spec_field _ k hW)
            (Space.isQuasiCompact_yoneda_map B integerBase hZ g inferInstance)
            ((Space.isSeparated_yoneda_map_iff B integerBase hZ g).2 inferInstance)
            ((Space.isQuasiSeparated_yoneda_map_iff B integerBase hZ g).2 inferInstance) hdim),
        (∃ q : BasedCategory.ofFunctor (Over.map W.hom) ⥤ᵇ
              Stack.fullSubcategoryBased _ U.property,
            Nonempty (q.comp (Stack.fullSubcategoryBasedInclusion _ U.property) ≅
              { toFunctor := z, w := hz })) ↔
          IsLocalCompleteIntersectionMorphism ((BigFppfOver.toScheme B integerBase hZ).map g)
```

**`AlgebraicGeometry.isOpenImmersion_curvesSubstackInclusion_lci`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersectionSubstack.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersectionSubstack.lean#L101). The attribute's comment: “the inclusion of Curves^\{lci} into Curves is representable by algebraic spaces and an open immersion”.

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

**`AlgebraicGeometry.factorsThrough_curvesSubstack_lci_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersectionSubstack.lean, line 118](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersectionSubstack.lean#L118). The attribute's comment: “part (1)”.

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

**`AlgebraicGeometry.factorsThrough_curvesSubstack_lci_over_field_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersectionSubstack.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/CurvesLocalCompleteIntersectionSubstack.lean#L142). The attribute's comment: “part (2)”.

> **Stacks 0DZV, part (2).** Let `g : T ⟶ W` be a morphism of the big fppf site of the integers
> whose target scheme is the spectrum of a field `k`, whose underlying morphism of schemes is
> proper, and whose source scheme `X` has dimension at most one, and let `z : (Sch/Spec(k)) →
> Curves` classify the family of curves of `g`. Then `z` factors through `Curves^\{lci}` if and only
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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
