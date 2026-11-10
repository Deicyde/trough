---
declaration: section
origin: cited
lean: AlgebraicGeometry.isLocallyNoetherian_of_mem_precoverage, AlgebraicGeometry.isLocallyNoetherian_of_isCovering, AlgebraicGeometry.isLocallyNoetherian_of_isCovering_bigFppfOver, AlgebraicGeometry.isLocallyNoetherian_of_locallyOfFiniteType_over, AlgebraicGeometry.isLocallyNoetherian_of_isPullback_over, AlgebraicGeometry.LocallyNoetherianOver.not_hasPullbacks, AlgebraicGeometry.LocallyNoetherianOver.not_isMorphismOfSites_toBigFppfOver, AlgebraicGeometry.ExtendingFunctors.isEquivalence_limitPreservingRestriction_noetherian
statement: formalized
proof: formalized
---

# 98.25 Limit preserving functors on Noetherian schemes

Section 98.25 of the Stacks Project, [Tag 0GE1](https://stacks.math.columbia.edu/tag/0GE1). 5 tags here are carried by 12 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0GE1, the section

[Tag 0GE1](https://stacks.math.columbia.edu/tag/0GE1) in the Stacks Project.

**`AlgebraicGeometry.isLocallyNoetherian_of_mem_precoverage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/LocallyNoetherianObjects.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/LocallyNoetherianObjects.lean#L84). The attribute's comment: “part (3): the members of a covering family of a locally Noetherian scheme”.

> A member of a `τ`-covering family of a locally Noetherian scheme is locally Noetherian.

```lean
public theorem isLocallyNoetherian_of_mem_precoverage (τ : CoveringTopology) {X : Scheme.{u}}
    (hX : IsLocallyNoetherian X) {R : Presieve X}
    (hR : R ∈ Scheme.precoverage (coveringMorphismProperty.{u} τ) X)
    {Y : Scheme.{u}} {f : Y ⟶ X} (hf : R f) : IsLocallyNoetherian Y
```

**`AlgebraicGeometry.isLocallyNoetherian_of_isCovering`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/LocallyNoetherianObjects.lean, line 93](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/LocallyNoetherianObjects.lean#L93). The attribute's comment: “part (3): the sources of a covering of a locally Noetherian object”.

> If a chosen covering family of a big site has locally Noetherian target, then each of its
> sources is locally Noetherian.

```lean
public theorem isLocallyNoetherian_of_isCovering (B : BigSite.{u} τ)
    {𝒰 : Covering (siteCategory B)} (h𝒰 : isCovering τ B 𝒰)
    (hX : IsLocallyNoetherian ((schemeBelowInclusion (cutoff τ B)).obj 𝒰.1)) (i : 𝒰.2.I₀) :
    IsLocallyNoetherian ((schemeBelowInclusion (cutoff τ B)).obj (𝒰.2.X i))
```

**`AlgebraicGeometry.isLocallyNoetherian_of_isCovering_bigFppfOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/LocallyNoetherianObjects.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/LocallyNoetherianObjects.lean#L103). The attribute's comment: “part (3) for the big fppf site over a base scheme”.

> If a covering family of the big fppf category over `S` has locally Noetherian target, then
> each of its sources is locally Noetherian.

```lean
public theorem isLocallyNoetherian_of_isCovering_bigFppfOver (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) {E : Covering (BigFppfOver B S hS)}
    (hE : BigFppfOver.IsCovering B S hS E)
    (hX : IsLocallyNoetherian ((BigFppfOver.toScheme B S hS).obj E.1)) (i : E.2.I₀) :
    IsLocallyNoetherian ((BigFppfOver.toScheme B S hS).obj (E.2.X i))
```

**`AlgebraicGeometry.isLocallyNoetherian_of_locallyOfFiniteType_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/LocallyNoetherianObjects.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/LocallyNoetherianObjects.lean#L115). The attribute's comment: “part (1): a morphism locally of finite type has locally Noetherian source”. References: EGA IV (1.3.3), “special case”.

> If `f : X ⟶ Y` is a morphism of the big site over `S` whose underlying morphism of schemes
> is locally of finite type and whose target is locally Noetherian, then its source is locally
> Noetherian.

```lean
public theorem isLocallyNoetherian_of_locallyOfFiniteType_over (B : BigSite.{u} τ)
    (S : Scheme.{u}) (hS : S.size < cutoff τ B) {X Y : Over (base B S hS)} (f : X ⟶ Y)
    (hY : IsLocallyNoetherian ((schemeBelowInclusion (cutoff τ B)).obj Y.left))
    (hf : LocallyOfFiniteType ((schemeBelowInclusion (cutoff τ B)).map f.left)) :
    IsLocallyNoetherian ((schemeBelowInclusion (cutoff τ B)).obj X.left)
```

**`AlgebraicGeometry.isLocallyNoetherian_of_isPullback_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/LocallyNoetherianObjects.lean, line 141](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/LocallyNoetherianObjects.lean#L141). The attribute's comment: “part (2): the fibre product along a morphism locally of finite type”.

> Let `f : X ⟶ Y` and `g : Z ⟶ Y` be morphisms of the big site over `S` with `f` locally of
> finite type on underlying schemes and `Z` locally Noetherian. Then the vertex of a fibre product
> square on `f` and `g` is locally Noetherian.

```lean
public theorem isLocallyNoetherian_of_isPullback_over (B : BigSite.{u} τ) (S : Scheme.{u})
    (hS : S.size < cutoff τ B) {W X Y Z : Over (base B S hS)}
    {p : W ⟶ X} {q : W ⟶ Z} {f : X ⟶ Y} {g : Z ⟶ Y} (h : IsPullback p q f g)
    (hf : LocallyOfFiniteType ((schemeBelowInclusion (cutoff τ B)).map f.left))
    (hZ : IsLocallyNoetherian ((schemeBelowInclusion (cutoff τ B)).obj Z.left)) :
    IsLocallyNoetherian ((schemeBelowInclusion (cutoff τ B)).obj W.left)
```

## Tag 0GE2, a remark

[Tag 0GE2](https://stacks.math.columbia.edu/tag/0GE2) in the Stacks Project.

**`AlgebraicGeometry.LocallyNoetherianOver.not_hasPullbacks`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Sites/NoetherianSiteNoFibreProducts.lean, line 475](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Sites/NoetherianSiteNoFibreProducts.lean#L475). The attribute's comment: “the first assertion, for tau = fppf and S the spectrum of a countable field”.

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

- [`AlgebraicGeometry.LocallyNoetherianOver.not_isMorphismOfSites_toBigFppfOver`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Sites/NoetherianSiteNotMorphismOfSites.lean#L416), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Examples/Sites/NoetherianSiteNotMorphismOfSites.lean, line 486](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Sites/NoetherianSiteNotMorphismOfSites.lean#L486) (StacksFrontier): “the second assertion, for tau = fppf and S = Spec F_p: the example of Examples, Section 0GE8 that the remark defers to”.

## Tag 0GE3, a lemma

[Tag 0GE3](https://stacks.math.columbia.edu/tag/0GE3) in the Stacks Project.

**`AlgebraicGeometry.ExtendingFunctors.isEquivalence_limitPreservingRestriction_noetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsRestrictionFullness.lean, line 182](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsRestrictionFullness.lean#L182).

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

**`AlgebraicGeometry.locallyOfFinitePresentation_of_limitPreserving_yoneda`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/LimitPreservingNoetherian.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/LimitPreservingNoetherian.lean#L119). References: SGA 3 XI (3.2), “partial”.

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

**`AlgebraicGeometry.ExtendingFunctors.relativelyRepresentable_restriction_of_limitPreservingSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsNoetherianRepresentable.lean, line 398](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsNoetherianRepresentable.lean#L398). The attribute's comment: “implication (1) ⇒ (2)”.

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

**`AlgebraicGeometry.ExtendingFunctors.isRepresentableOnAffineFiniteType_of_relativelyRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsNoetherianRepresentable.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsNoetherianRepresentable.lean#L412). The attribute's comment: “implication (2) ⇒ (3)”.

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

**`AlgebraicGeometry.ExtendingFunctors.relativelyRepresentable_of_isRepresentableOnAffineFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsNoetherianRepresentableConverse.lean, line 951](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsNoetherianRepresentableConverse.lean#L951). The attribute's comment: “implication (3) ⇒ (1)”. References: SGA 3 XI (3.4), “special case”.

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

**`AlgebraicGeometry.ExtendingFunctors.relativelyRepresentable_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsNoetherianRepresentableConverse.lean, line 975](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/ExtendingFunctorsNoetherianRepresentableConverse.lean#L975).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
