---
declaration: section
origin: cited
lean: AlgebraicGeometry.BigSite.NoetherianOver.closure_isSite_isContinuous_isCocontinuous, AlgebraicGeometry.LocallyNoetherianOver.not_hasPullbacks, AlgebraicGeometry.LocallyNoetherianOver.not_isMorphismOfSites_toBigFppfOver, AlgebraicGeometry.ExtendingFunctors.isEquivalence_limitPreservingRestriction_noetherian, AlgebraicGeometry.locallyOfFinitePresentation_of_limitPreserving_yoneda, AlgebraicGeometry.ExtendingFunctors.relativelyRepresentable_restriction_of_limitPreservingSheaf, AlgebraicGeometry.ExtendingFunctors.isRepresentableOnAffineFiniteType_of_relativelyRepresentable, AlgebraicGeometry.ExtendingFunctors.relativelyRepresentable_of_isRepresentableOnAffineFiniteType
statement: formalized
proof: formalized
---

# 98.25 Limit preserving functors on Noetherian schemes

Section 98.25 of the Stacks Project, [Tag 0GE1](https://stacks.math.columbia.edu/tag/0GE1). 5 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GE1, the section

[Tag 0GE1](https://stacks.math.columbia.edu/tag/0GE1) in the Stacks Project.

**`AlgebraicGeometry.BigSite.NoetherianOver.closure_isSite_isContinuous_isCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/LocallyNoetherianSite.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/LocallyNoetherianSite.lean#L327). The attribute's comment: “all five parts, for each of the topologies Zariski, étale, smooth, syntomic, fppf”.

> **Stacks 0GE1.** Let `τ` be one of the topologies Zariski, étale, smooth, syntomic and fppf,
> let `B` be a big `τ`-site and `S` a scheme of `B`, and let `(Noetherian/S)` be the full
> subcategory of `(Sch/S)` on the locally Noetherian objects.
> 1. If `f : X ⟶ Y` is a morphism of `(Sch/S)` locally of finite type with `Y` locally
>    Noetherian, then `X` is locally Noetherian.
> 2. For morphisms `f : X ⟶ Y` and `g : Z ⟶ Y` of `(Noetherian/S)` with `f` locally of finite
>    type, the fibre product `X ×_Y Z` exists in `(Noetherian/S)` and agrees with the fibre
>    product in `(Sch/S)`.
> 3. The members of a covering of `(Sch/S)_τ` of a locally Noetherian object are locally
>    Noetherian.
> 4. The coverings of `(Sch/S)_τ` whose objects lie in `(Noetherian/S)` make `(Noetherian/S)` a
>    site, `(Noetherian/S)_τ`.
> 5. The inclusion `(Noetherian/S)_τ ⥤ (Sch/S)_τ` is fully faithful, continuous and cocontinuous:
>    it carries coverings to coverings and preserves the fibre products of their members, every
>    covering of `(Sch/S)_τ` of an object of `(Noetherian/S)` is refined by the image of a
>    covering of `(Noetherian/S)_τ`, and on the generated topologies it is
>    `Functor.IsContinuous` and `Functor.IsCocontinuous`.
>
> The source assumes `S` locally Noetherian; the statement holds without it.

```lean
theorem closure_isSite_isContinuous_isCocontinuous :
    (∀ {X Y : Over (base B S hS)} (f : X ⟶ Y), locallyNoetherianOver B S hS Y →
      LocallyOfFiniteType ((schemeBelowInclusion (cutoff τ B)).map f.left) →
        locallyNoetherianOver B S hS X) ∧
    (∀ {X Y Z : NoetherianOver B S hS} (f : X ⟶ Y) (g : Z ⟶ Y),
      LocallyOfFiniteType ((schemeBelowInclusion (cutoff τ B)).map f.hom.left) →
        HasPullback f g ∧ PreservesLimit (cospan f g) (ι B S hS)) ∧
    (∀ E : Covering.{u + 1, u, u + 1} (Over (base B S hS)), IsOverCovering B S hS E →
      locallyNoetherianOver B S hS E.1 → ∀ i, locallyNoetherianOver B S hS (E.2.X i)) ∧
    IsSite (IsCovering B S hS) ∧
    ((ι B S hS).Full ∧ (ι B S hS).Faithful ∧
      (∀ E : Covering.{u + 1, u, u + 1} (NoetherianOver B S hS), IsCovering B S hS E →
        IsOverCovering B S hS ⟨(ι B S hS).obj E.1, E.2.map (ι B S hS)⟩ ∧
        ∀ (i : E.2.I₀) {T : NoetherianOver B S hS} (g : T ⟶ E.1),
          HasPullback (E.2.f i) g ∧ PreservesLimit (cospan (E.2.f i) g) (ι B S hS)) ∧
      (∀ (X : NoetherianOver B S hS) (F : PreZeroHypercover.{u + 1} ((ι B S hS).obj X)),
        IsOverCovering B S hS ⟨_, F⟩ → ∃ E : PreZeroHypercover.{u + 1} X,
          IsCovering B S hS ⟨X, E⟩ ∧ Nonempty ((E.map (ι B S hS)).Hom F)) ∧
      (ι B S hS).IsContinuous (topology B S hS) (overTopology τ B S hS) ∧
      (ι B S hS).IsCocontinuous (topology B S hS) (overTopology τ B S hS))
```

## Tag 0GE2, a remark

[Tag 0GE2](https://stacks.math.columbia.edu/tag/0GE2) in the Stacks Project.

**`AlgebraicGeometry.LocallyNoetherianOver.not_hasPullbacks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Sites/NoetherianSiteNoFibreProducts.lean, line 475](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Sites/NoetherianSiteNoFibreProducts.lean#L475). The attribute's comment: “the first assertion, for tau = fppf and S the spectrum of a countable field”.

> **Stacks 0GE2, first assertion.** *The site `(Noetherian/S)_τ` does not have fibre
> products*, here for `τ = fppf` and `S = Spec k` with `k` a countable field.
>
> The diagram without a fibre product is `Spec K ⟶ S ⟵ Spec K` for `K = k(u₀, u₁, u₂, …)`. A
> fibre product would be a locally Noetherian scheme receiving, compatibly, the square-zero
> extensions `Spec (K ⊕ Kⁿ)` with their two maps to `Spec K`; all of these meet it in one point,
> whose local ring would have to dominate maximal ideals of unbounded embedding dimension.

```lean
public theorem not_hasPullbacks (B : BigFppfSite.{u}) (baseField : Type u) [Field baseField]
    [Countable baseField] (hS : B.Contains (Spec (.of baseField))) :
    ¬ HasPullbacks (LocallyNoetherianOver B (Spec (.of baseField)) hS)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.LocallyNoetherianOver.not_isMorphismOfSites_toBigFppfOver`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Sites/NoetherianSiteNotMorphismOfSites.lean#L416), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Examples/Sites/NoetherianSiteNotMorphismOfSites.lean, line 486](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Sites/NoetherianSiteNotMorphismOfSites.lean#L486) (StacksFrontier): “the second assertion, for tau = fppf and S = Spec F\_p: the example of Examples, Section 0GE8 that the remark defers to”.

## Tag 0GE3, a lemma

[Tag 0GE3](https://stacks.math.columbia.edu/tag/0GE3) in the Stacks Project.

**`AlgebraicGeometry.ExtendingFunctors.isEquivalence_limitPreservingRestriction_noetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsRestrictionFullness.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsRestrictionFullness.lean#L182).

> **Stacks 0GE3.** Let `S` be a locally Noetherian scheme and let `τ` be one of the five
> topologies — Zariski, étale, smooth, syntomic and fppf. Restriction along the inclusion of the
> full subcategory of locally Noetherian objects of `Sch/S` is an equivalence from the category of
> limit preserving sheaves on `(Sch/S)_τ` to the category of limit preserving sheaves on the site
> `(Noetherian/S)_τ`.
>
> Faithfulness is the sharp uniqueness statement of Stacks 0EUW, essential surjectivity is the
> existence statement of Stacks 0EUW together with the sheaf property of the extension supplied by
> Stacks 0GDW, and fullness is the functoriality of that extension.

```lean
theorem isEquivalence_limitPreservingRestriction_noetherian (τ : CoveringTopology)
    {S : Scheme.{u}} [IsLocallyNoetherian S] :
    (limitPreservingRestriction (P := IsLocallyNoetherianOver (S := S)) τ
      (hasCoveringPullbacks_isLocallyNoetherianOver τ)).IsEquivalence
```

## Tag 0GE4, a lemma

[Tag 0GE4](https://stacks.math.columbia.edu/tag/0GE4) in the Stacks Project.

**`AlgebraicGeometry.locallyOfFinitePresentation_of_limitPreserving_yoneda`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/LimitPreservingNoetherian.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/LimitPreservingNoetherian.lean#L119). References: SGA 3 XI (3.2), “partial”.

> A limit-preserving representable functor on the locally Noetherian site
> represents a scheme locally of finite presentation over the base.

```lean
theorem locallyOfFinitePresentation_of_limitPreserving_yoneda
    (B : BigFppfSite.{u}) (S : Scheme.{u})
    [IsLocallyNoetherian S] (hS : B.Contains S)
    (X : LocallyNoetherianOver B S hS)
    (hX : LimitPreserving.{u, u, u, u, u + 1, u}
      (LocallyNoetherianOver.toScheme B S hS) (yoneda.obj X)) :
    LocallyOfFinitePresentation (B.inclusion.map X.1.hom)
```

## Tag 0GE5, a lemma

[Tag 0GE5](https://stacks.math.columbia.edu/tag/0GE5) in the Stacks Project.

**`AlgebraicGeometry.ExtendingFunctors.relativelyRepresentable_restriction_of_limitPreservingSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsNoetherianRepresentable.lean, line 397](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsNoetherianRepresentable.lean#L397). The attribute's comment: “implication (1) ⇒ (2)”.

> **Stacks 0GE5, implication (1) ⇒ (2).** Let `S` be a locally Noetherian scheme, let `τ` be
> one of the five topologies — Zariski, étale, smooth, syntomic and fppf — and let `F'`, `G'` be
> limit preserving sheaves on `(Sch/S)_τ`. If a transformation `a' : F' ⟶ G'` is representable, in
> the sense of Categories Definition 001X, then so is its restriction `a` to the full subcategory of
> locally Noetherian objects: for every locally Noetherian object `V` over `S` and every map
> `V ⟶ G` the fibre product `F ×_G V` is represented by a locally Noetherian object over `S`.
>
> Only limit preservation of `F'` and `G'` enters the proof; the sheaf condition and the topology
> are carried because the source states them, and the sharper statement is
> `AlgebraicGeometry.ExtendingFunctors.relativelyRepresentable_restriction`.

```lean
theorem relativelyRepresentable_restriction_of_limitPreservingSheaf
    (τ : CoveringTopology) [IsLocallyNoetherian S]
    {F' G' : (Over S)ᵒᵖ ⥤ Type (max w (u + 1))} (a' : F' ⟶ G')
    (hF' : IsLimitPreservingSheaf τ F') (hG' : IsLimitPreservingSheaf τ G')
    (h1 : (uliftYoneda.{max w (u + 1)}).relativelyRepresentable a') :
    (uliftYoneda.{max w (u + 1)}).relativelyRepresentable
      (Functor.whiskerLeft (IsLocallyNoetherianOver (S := S)).ι.op a')
```

**`AlgebraicGeometry.ExtendingFunctors.isRepresentableOnAffineFiniteType_of_relativelyRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsNoetherianRepresentable.lean, line 411](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsNoetherianRepresentable.lean#L411). The attribute's comment: “implication (2) ⇒ (3)”.

> **Stacks 0GE5, implication (2) ⇒ (3).** If the restriction of `a'` to the locally Noetherian
> objects over `S` is representable, then it is representable at every test object which is affine
> of finite type over `S` and maps into an affine open of `S`: criterion (3) is criterion (2) with
> its test object restricted.

```lean
theorem isRepresentableOnAffineFiniteType_of_relativelyRepresentable
    {P : ObjectProperty (Over S)}
    {F G : P.FullSubcategoryᵒᵖ ⥤ Type (max w (u + 1))} {a : F ⟶ G}
    (h : (uliftYoneda.{max w (u + 1)}).relativelyRepresentable a) :
    IsRepresentableOnAffineFiniteType.{w} a
```

**`AlgebraicGeometry.ExtendingFunctors.relativelyRepresentable_of_isRepresentableOnAffineFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsNoetherianRepresentableConverse.lean, line 951](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsNoetherianRepresentableConverse.lean#L951). The attribute's comment: “implication (3) ⇒ (1)”. References: SGA 3 XI (3.4), “special case”.

> **Stacks 0GE5, implication (3) ⇒ (1).** Let `S` be a locally Noetherian scheme, let `τ` be one
> of the five topologies — Zariski, étale, smooth, syntomic and fppf — and let `F'`, `G'` be limit
> preserving sheaves on `(Sch/S)_τ`. If the restriction `a` of a transformation `a' : F' ⟶ G'` to the
> locally Noetherian objects over `S` is representable at every test object which is affine of finite
> type over `S` and maps into an affine open of `S`, then `a'` itself is representable, in the sense
> of Categories Definition 001X.
>
> For an arbitrary object `T` of `Sch/S` and a section of `G'` over it, the fibre product is
> represented over every member of the basis of opens of `T` which are affine and lie over an affine
> open of `S`; those representing objects glue by Stacks 01LH, the local sections of `F'` glue
> because `F'` is a Zariski sheaf, and the glued object has the universal property of the fibre
> product at every object of `Sch/S`, both the existence and the uniqueness being local on that
> object.

```lean
theorem relativelyRepresentable_of_isRepresentableOnAffineFiniteType
    (τ : CoveringTopology) [IsLocallyNoetherian S]
    {F' G' : (Over S)ᵒᵖ ⥤ Type (max w (u + 1))} (a' : F' ⟶ G')
    (hF' : IsLimitPreservingSheaf τ F') (hG' : IsLimitPreservingSheaf τ G')
    (h3 : IsRepresentableOnAffineFiniteType.{w}
      (Functor.whiskerLeft (IsLocallyNoetherianOver (S := S)).ι.op a')) :
    (uliftYoneda.{max w (u + 1)}).relativelyRepresentable a'
```

**`AlgebraicGeometry.ExtendingFunctors.relativelyRepresentable_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsNoetherianRepresentableConverse.lean, line 975](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsNoetherianRepresentableConverse.lean#L975).

> **Stacks 0GE5.** Let `S` be a locally Noetherian scheme, let `τ` be one of the five
> topologies — Zariski, étale, smooth, syntomic and fppf — and let `F'`, `G'` be limit preserving
> sheaves on `(Sch/S)_τ`. For a transformation `a' : F' ⟶ G'` with restriction `a` to the full
> subcategory of locally Noetherian objects over `S`, the following are equivalent:
>
> 1. `a'` is representable;
> 2. `a` is representable;
> 3. `a` is representable at every test object which is affine of finite type over `S` and maps into
>    an affine open of `S`.

```lean
theorem relativelyRepresentable_tfae (τ : CoveringTopology) [IsLocallyNoetherian S]
    {F' G' : (Over S)ᵒᵖ ⥤ Type (max w (u + 1))} (a' : F' ⟶ G')
    (hF' : IsLimitPreservingSheaf τ F') (hG' : IsLimitPreservingSheaf τ G') :
    List.TFAE
      [(uliftYoneda.{max w (u + 1)}).relativelyRepresentable a',
       (uliftYoneda.{max w (u + 1)}).relativelyRepresentable
         (Functor.whiskerLeft (IsLocallyNoetherianOver (S := S)).ι.op a'),
       IsRepresentableOnAffineFiniteType.{w}
         (Functor.whiskerLeft (IsLocallyNoetherianOver (S := S)).ι.op a')]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 98.25, Tag 0GE1](https://stacks.math.columbia.edu/tag/0GE1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
