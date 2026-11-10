---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isEquivalence_spacesBaseChange_of_isIntegralHom_of_universallyInjective, AlgebraicGeometry.Space.essSurj_spacesBaseChange_of_isFirstOrderThickening, AlgebraicGeometry.Space.isEquivalence_spacesBaseChange_of_isFirstOrderThickening, AlgebraicGeometry.Space.essSurj_spacesBaseChange_of_isThickening, AlgebraicGeometry.Space.isEquivalence_spacesBaseChange_of_isThickening, AlgebraicGeometry.Space.faithful_spacesBaseChange_of_isSurjective, AlgebraicGeometry.Space.faithful_spacesBaseChange_of_isThickening, AlgebraicGeometry.Space.full_spacesBaseChange_of_isThickening
statement: formalized
proof: formalized
---

# 76.8 Topological invariance of the étale site

Section 76.8 of the Stacks Project, [Tag 05ZG](https://stacks.math.columbia.edu/tag/05ZG). 3 tags here are carried by 32 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05ZH, a theorem

[Tag 05ZH](https://stacks.math.columbia.edu/tag/05ZH) in the Stacks Project.

**`AlgebraicGeometry.Space.isEquivalence_spacesBaseChange_of_isIntegralHom_of_universallyInjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleEssSurj/IntegralUniversallyInjective.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleEssSurj/IntegralUniversallyInjective.lean#L227). The attribute's comment: “the equivalence at the tag's own class: integral, universally injective and surjective”.

> For every integral, universally injective and surjective morphism `f` of algebraic spaces over
> `S`, base change `V ↦ X ×_Y V` is an equivalence from the spaces-étale site of `Y` to that of
> `X`.

```lean
theorem isEquivalence_spacesBaseChange_of_isIntegralHom_of_universallyInjective (f : X ⟶ Y)
    (hint : IsIntegralHom B S hS f.hom) (hui : UniversallyInjective B S hS f.hom)
    (hsurj : IsSurjective B S hS f.hom) :
    (spacesBaseChange B S hS f).functor.IsEquivalence
```

**`AlgebraicGeometry.Space.essSurj_spacesBaseChange_of_isFirstOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleEssSurj/LiftedEtalePresentation.lean, line 592](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleEssSurj/LiftedEtalePresentation.lean#L592). The attribute's comment: “essential surjectivity at a first-order thickening”.

> Base change `V ↦ X ×_Y V` is essentially surjective from the spaces-étale site of `Y` to that
> of `X`, for the inclusion `f` of a first-order thickening.

```lean
theorem essSurj_spacesBaseChange_of_isFirstOrderThickening (f : X ⟶ Y) [Mono f.hom]
    (hT : IsFirstOrderThickening B S hS Y (Subfunctor.range f.hom)) :
    (spacesBaseChange B S hS f).functor.EssSurj
```

**`AlgebraicGeometry.Space.isEquivalence_spacesBaseChange_of_isFirstOrderThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleEssSurj/LiftedEtalePresentation.lean, line 602](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleEssSurj/LiftedEtalePresentation.lean#L602). The attribute's comment: “the first-order thickening case, not the integral universally injective one”.

> Base change `V ↦ X ×_Y V` is an equivalence from the spaces-étale site of `Y` to that of `X`,
> for the inclusion `f` of a first-order thickening.

```lean
theorem isEquivalence_spacesBaseChange_of_isFirstOrderThickening (f : X ⟶ Y) [Mono f.hom]
    (hT : IsFirstOrderThickening B S hS Y (Subfunctor.range f.hom)) :
    (spacesBaseChange B S hS f).functor.IsEquivalence
```

**`AlgebraicGeometry.Space.essSurj_spacesBaseChange_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleEssSurj/Thickening.lean, line 521](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleEssSurj/Thickening.lean#L521). The attribute's comment: “ESSENTIAL SURJECTIVITY ONLY, at a thickening of ARBITRARY order. This lifts the FIRST-ORDER restriction of `AlgebraicGeometry.Space.essSurj_spacesBaseChange_of_isFirstOrderThickening`, which descends the two maps of the lifted etale equivalence relation by the square-zero lifting property of Stacks 0611; the route here is the source's own, where they are descended by FULLNESS at arbitrary order, `AlgebraicGeometry.Space.full_spacesBaseChange_of_isThickening`, and every uniqueness step is FAITHFULNESS at arbitrary order, `AlgebraicGeometry.Space.faithful_spacesBaseChange_of_isThickening`. Together with `AlgebraicGeometry.Space.fullyFaithfulSpacesBaseChangeOfIsThickening` this gives the EQUIVALENCE at arbitrary order, `AlgebraicGeometry.Space.isEquivalence_spacesBaseChange_of_isThickening`. The source states the tag for an arbitrary INTEGRAL, UNIVERSALLY INJECTIVE and SURJECTIVE morphism, which is a wider class: the library proves only that a thickening inclusion belongs to it (Stacks 05ZL, `AlgebraicGeometry.Space.isIntegralHom_universallyInjective_isSurjective_ι_of_isThickening`) and not the converse, so that wider class is NOT covered”.

> Let `G ⊂ Y` be a thickening of algebraic spaces over `S`, of arbitrary order. Base change
> along the inclusion, `V ↦ G ×_Y V`, is essentially surjective from the spaces-étale site of `Y`
> to that of `G`.

```lean
theorem essSurj_spacesBaseChange_of_isThickening {G : Subfunctor Y.1}
    (hG : IsThickening B S hS Y G) :
    (spacesBaseChange B S hS (IsThickening.inclusion B S hS hG)).functor.EssSurj
```

**`AlgebraicGeometry.Space.isEquivalence_spacesBaseChange_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleEssSurj/Thickening.lean, line 540](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleEssSurj/Thickening.lean#L540). The attribute's comment: “the EQUIVALENCE at a thickening of ARBITRARY order -- all three of faithfulness, fullness and essential surjectivity, with no hypothesis beyond the thickening and no monomorphism hypothesis. What is still NOT covered is the source's wider class of an arbitrary INTEGRAL, UNIVERSALLY INJECTIVE and SURJECTIVE morphism: the library proves only that a thickening inclusion lies in that class (Stacks 05ZL, `AlgebraicGeometry.Space.isIntegralHom_universallyInjective_isSurjective_ι_of_isThickening`), not the converse. The first-order statement `AlgebraicGeometry.Space.isEquivalence_spacesBaseChange_of_isFirstOrderThickening` is subsumed up to the identification of the source of `f` with the range of `f.hom`”.

> Let `G ⊂ Y` be a thickening of algebraic spaces over `S`, of arbitrary order. Base change
> along the inclusion, `V ↦ G ×_Y V`, is an equivalence from the spaces-étale site of `Y` to that
> of `G`.

```lean
theorem isEquivalence_spacesBaseChange_of_isThickening {G : Subfunctor Y.1}
    (hG : IsThickening B S hS Y G) :
    (spacesBaseChange B S hS (IsThickening.inclusion B S hS hG)).functor.IsEquivalence
```

**`AlgebraicGeometry.Space.faithful_spacesBaseChange_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleFaithfulGeneral.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleFaithfulGeneral.lean#L131). The attribute's comment: “FAITHFULNESS ONLY, for an arbitrary morphism surjective on points -- so at a thickening of ARBITRARY order, and under a hypothesis weaker than the source's integral, universally injective and surjective. The library's other Stacks 05ZH statements are restricted to a FIRST-ORDER thickening because they go through the square-zero lifting property of Stacks 0611; this one reproduces the source's own route instead. FULLNESS is also available at arbitrary order, at a thickening, as `AlgebraicGeometry.Space.full_spacesBaseChange_of_isThickening`; ESSENTIAL SURJECTIVITY remains first-order, see `AlgebraicGeometry.Space.isEquivalence_spacesBaseChange_of_isFirstOrderThickening`”.

> Let `f : X ⟶ Y` be a
> morphism of algebraic spaces over `S` which is surjective on points. Base change
> `V ↦ X ×_Y V` is faithful from the spaces-étale site of `Y` to that of `X`.

```lean
theorem faithful_spacesBaseChange_of_isSurjective (f : X ⟶ Y)
    (hf : IsSurjective B S hS f.hom) :
    (spacesBaseChange B S hS f).functor.Faithful
```

**`AlgebraicGeometry.Space.faithful_spacesBaseChange_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleFaithfulGeneral.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleFaithfulGeneral.lean#L163). The attribute's comment: “FAITHFULNESS ONLY, at a thickening of ARBITRARY order. FULLNESS at arbitrary order is `AlgebraicGeometry.Space.full_spacesBaseChange_of_isThickening`; ESSENTIAL SURJECTIVITY at arbitrary order is `AlgebraicGeometry.Space.essSurj_spacesBaseChange_of_isThickening`”.

> Let `G ⊂ X` be a thickening of algebraic spaces over `S`, of arbitrary order. Base change
> along the inclusion, `V ↦ G ×_X V`, is faithful from the spaces-étale site of `X` to that of
> `G`.

```lean
theorem faithful_spacesBaseChange_of_isThickening {G : Subfunctor X.1}
    (hG : IsThickening B S hS X G) :
    (spacesBaseChange B S hS (IsThickening.inclusion B S hS hG)).functor.Faithful
```

**`AlgebraicGeometry.Space.full_spacesBaseChange_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleFullGeneral.lean, line 334](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleFullGeneral.lean#L334). The attribute's comment: “FULLNESS ONLY, at a thickening of ARBITRARY order. Together with `AlgebraicGeometry.Space.faithful_spacesBaseChange_of_isThickening` this gives FULL FAITHFULNESS at arbitrary order, bundled as `AlgebraicGeometry.Space.fullyFaithfulSpacesBaseChangeOfIsThickening`; ESSENTIAL SURJECTIVITY is not covered here; it is proved at arbitrary order in `AlgebraicGeometry.Space.essSurj_spacesBaseChange_of_isThickening`, and the equivalence in `AlgebraicGeometry.Space.isEquivalence_spacesBaseChange_of_isThickening`. The library's other fullness statement, `AlgebraicGeometry.Space.full_spacesBaseChange_of_isFirstOrderThickening`, is restricted to first order because it goes through the square-zero lifting property of Stacks 0611; this one reproduces the source's graph argument instead, and the source's integrality and universal injectivity hypotheses are not needed beyond what a thickening already gives”.

> Let `G ⊂ Y` be a thickening of algebraic spaces over `S`, of arbitrary order. Base change along
> the inclusion, `V ↦ G ×_Y V`, is full from the spaces-étale site of `Y` to that of `G`.

```lean
theorem full_spacesBaseChange_of_isThickening {G : Subfunctor Y.1}
    (hG : IsThickening B S hS Y G) :
    (spacesBaseChange B S hS (IsThickening.inclusion B S hS hG)).functor.Full
```

**`AlgebraicGeometry.Space.fullyFaithfulSpacesBaseChangeOfIsThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleFullGeneral.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleFullGeneral.lean#L347). The attribute's comment: “FULL FAITHFULNESS ONLY, at a thickening of ARBITRARY order; ESSENTIAL SURJECTIVITY is not covered here, and is proved at arbitrary order in `AlgebraicGeometry.Space.essSurj_spacesBaseChange_of_isThickening`”.

> Let `G ⊂ Y` be a thickening of algebraic spaces over `S`, of arbitrary order. Base change along
> the inclusion, `V ↦ G ×_Y V`, is fully faithful from the spaces-étale site of `Y` to that of
> `G`.

```lean
noncomputable def fullyFaithfulSpacesBaseChangeOfIsThickening {G : Subfunctor Y.1}
    (hG : IsThickening B S hS Y G) :
    (spacesBaseChange B S hS (IsThickening.inclusion B S hS hG)).functor.FullyFaithful
```

**`AlgebraicGeometry.Space.fullyFaithfulSpacesBaseChangeOfIsFirstOrderThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleFullyFaithful.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleFullyFaithful.lean#L192). The attribute's comment: “full faithfulness at a first-order thickening”.

> Base change `V ↦ X ×_Y V` along the inclusion `f` of a first-order thickening is fully
> faithful from the spaces-étale site of `Y` to that of `X`.

```lean
noncomputable def fullyFaithfulSpacesBaseChangeOfIsFirstOrderThickening [Mono f.hom]
    (hT : IsFirstOrderThickening B S hS Y (Subfunctor.range f.hom)) :
    (spacesBaseChange B S hS f).functor.FullyFaithful
```

**`AlgebraicGeometry.Space.faithful_spacesBaseChange_of_mono_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleFullyFaithful.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleFullyFaithful.lean#L212). The attribute's comment: “faithfulness at an arbitrary thickening”.

> Base change along the inclusion
> of a thickening — of no prescribed order — is faithful on spaces-étale sites.

```lean
theorem faithful_spacesBaseChange_of_mono_of_isThickening [Mono f.hom]
    (hT : IsThickening B S hS Y (Subfunctor.range f.hom)) :
    (spacesBaseChange B S hS f).functor.Faithful
```

**`AlgebraicGeometry.Space.full_spacesBaseChange_of_mono_of_isThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleFullyFaithful.lean, line 222](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleFullyFaithful.lean#L222). The attribute's comment: “fullness at an arbitrary thickening”.

> Base change along the inclusion of a
> thickening — of no prescribed order — is full on spaces-étale sites.

```lean
theorem full_spacesBaseChange_of_mono_of_isThickening [Mono f.hom]
    (hT : IsThickening B S hS Y (Subfunctor.range f.hom)) :
    (spacesBaseChange B S hS f).functor.Full
```

**`AlgebraicGeometry.Space.fullyFaithfulSpacesBaseChangeOfMonoOfIsThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleFullyFaithful.lean, line 232](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleFullyFaithful.lean#L232). The attribute's comment: “full faithfulness at an arbitrary thickening”.

> Base change `V ↦ X ×_Y V` is fully faithful from the spaces-étale site of `Y` to that of `X`,
> for `f` a monomorphism whose range is a thickening of `Y` of arbitrary order.

```lean
noncomputable def fullyFaithfulSpacesBaseChangeOfMonoOfIsThickening [Mono f.hom]
    (hT : IsThickening B S hS Y (Subfunctor.range f.hom)) :
    (spacesBaseChange B S hS f).functor.FullyFaithful
```

**`AlgebraicGeometry.Space.fullyFaithfulSpacesBaseChangeOfIsThickeningRange`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleFullyFaithfulThickening.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleFullyFaithfulThickening.lean#L63). The attribute's comment: “full faithfulness at a thickening of unbounded order, not the integral universally injective case”.

> Base change `V ↦ X ×_Y V` is fully faithful from the spaces-étale site of `Y` to that of `X`,
> for the inclusion `f` of a thickening of algebraic spaces — a monomorphism whose range is a
> closed subspace with the same points, with no hypothesis on its defining ideal.

```lean
noncomputable def fullyFaithfulSpacesBaseChangeOfIsThickeningRange [Mono f.hom]
    (hT : IsThickening B S hS Y (Subfunctor.range f.hom)) :
    (spacesBaseChange B S hS f).functor.FullyFaithful
```

**`AlgebraicGeometry.Space.fullyFaithfulSpacesBaseChangeOfIsNthOrderThickening`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleFullyFaithfulThickening.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleFullyFaithfulThickening.lean#L88). The attribute's comment: “full faithfulness at a thickening of finite order”.

> Base change `V ↦ X ×_Y V` is fully faithful from the spaces-étale site of `Y` to that of `X`,
> for the inclusion `f` of a thickening of order `n`, whose defining ideal has vanishing `(n+1)`st
> power.

```lean
noncomputable def fullyFaithfulSpacesBaseChangeOfIsNthOrderThickening {n : ℕ} [Mono f.hom]
    (hT : IsNthOrderThickening B S hS n Y (Subfunctor.range f.hom)) :
    (spacesBaseChange B S hS f).functor.FullyFaithful
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.C1573.isEquivalence_spacesBaseChange_of_isThickeningHom`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GrothendieckExistence/EquivalencePort/Thickenings/SpacesEtaleEquivalenceGeneral.lean#L97), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleEquivalenceGeneral.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/SpacesEtaleEquivalenceGeneral.lean#L84) (StacksFrontier): “the equivalence, for the inclusion of a thickening of arbitrary order”.

## Tag 07VW, a lemma

[Tag 07VW](https://stacks.math.columbia.edu/tag/07VW) in the Stacks Project.

**`AlgebraicGeometry.Space.smallEtalePullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleTopologicalInvariance.lean, line 298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleTopologicalInvariance.lean#L298). The attribute's comment: “the base-change functor on the étale schemes, which needs only integrality of `f`; the two equivalences are stated separately”.

> **Stacks 07VW, the base-change functor on the étale schemes.** For an integral morphism
> `f : X ⟶ Y` of algebraic spaces over `S`, base change `V ↦ X ×_Y V` carries the small étale
> site of `Y` to that of `X`.
>
> It is the restriction of base change on the spaces-étale sites along the fully faithful
> comparison functors of Stacks 03G1 — see
> `AlgebraicGeometry.Space.smallEtalePullbackComparisonIso` — which exists because the base change
> of a scheme étale over `Y` is a scheme, by the implication of Stacks 07VV from the target.

```lean
noncomputable def smallEtalePullback (f : X ⟶ Y) (hf : IsIntegralHom B S hS f.hom) :
    SmallEtale B S hS Y.1 ⥤ SmallEtale B S hS X.1
```

**`AlgebraicGeometry.Space.smallEtalePullbackComparisonIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleTopologicalInvariance.lean, line 311](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleTopologicalInvariance.lean#L311). The attribute's comment: “the restriction to the étale schemes is the spaces-étale base change”.

> **Stacks 07VW, canonicity of the base-change functor on the étale schemes.**
> `AlgebraicGeometry.Space.smallEtalePullback` is the restriction of base change on the
> spaces-étale sites: composing it with the comparison functor of `X` recovers base change applied
> to the comparison functor of `Y`.

```lean
noncomputable def smallEtalePullbackComparisonIso (f : X ⟶ Y)
    (hf : IsIntegralHom B S hS f.hom) :
    smallEtalePullback B S hS f hf ⋙ comparisonFunctor B S hS X ≅
      comparisonFunctor B S hS Y ⋙ (spacesBaseChange B S hS f).functor
```

**`AlgebraicGeometry.Space.affineEtalePullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleTopologicalInvariance.lean, line 372](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleTopologicalInvariance.lean#L372). The attribute's comment: “the base-change functor on the affine étale schemes, which needs only integrality of `f`; the two equivalences are stated separately”.

> **Stacks 07VW, the base-change functor on the affine étale schemes.** For an integral
> morphism `f : X ⟶ Y` of algebraic spaces over `S`, base change `V ↦ X ×_Y V` carries the affine
> étale site of `Y` to that of `X`: a base change of an affine chart is affine, because the
> projection is integral and an integral morphism with affine target has affine source.

```lean
noncomputable def affineEtalePullback (f : X ⟶ Y) (hf : IsIntegralHom B S hS f.hom) :
    AffineEtale B S hS Y.1 ⥤ AffineEtale B S hS X.1
```

**`AlgebraicGeometry.Space.affineEtalePullbackInclusionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleTopologicalInvariance.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleTopologicalInvariance.lean#L382). The attribute's comment: “the restriction to the affine étale schemes is the small étale base change”.

> **Stacks 07VW, canonicity of the base-change functor on the affine étale schemes.**
> `AlgebraicGeometry.Space.affineEtalePullback` is the restriction of
> `AlgebraicGeometry.Space.smallEtalePullback` to the affine charts.

```lean
noncomputable def affineEtalePullbackInclusionIso (f : X ⟶ Y)
    (hf : IsIntegralHom B S hS f.hom) :
    affineEtalePullback B S hS f hf ⋙ AffineEtale.inclusion B S hS X.1 ≅
      AffineEtale.inclusion B S hS Y.1 ⋙ smallEtalePullback B S hS f hf
```

**`AlgebraicGeometry.Space.isEquivalence_smallEtalePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TopologicalInvariance/SmallEtale.lean, line 223](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TopologicalInvariance/SmallEtale.lean#L223). The attribute's comment: “the equivalence `Y_étale ⟶ X_étale` of small étale sites, the restriction of the equivalence of Stacks 05ZH on spaces-étale sites (that it is the restriction is `AlgebraicGeometry.Space.smallEtalePullbackComparisonIso`)”.

> **Stacks 07VW, on the étale schemes.** Let `f : X ⟶ Y` be an integral, universally injective
> and surjective morphism of algebraic spaces over `S`. Then base change `V ↦ X ×_Y V` is an
> equivalence from the small étale site of `Y` to that of `X`; it is the restriction of the
> equivalence of Stacks 05ZH on the spaces-étale sites
> (`AlgebraicGeometry.Space.smallEtalePullbackComparisonIso`).
>
> The equivalence of Stacks 05ZH restricts along the fully faithful comparison functors of Stacks
> 03G1 because, for `V` étale over `Y`, `V` is a scheme exactly when `X ×_Y V` is: the projection
> `X ×_Y V ⟶ V` is integral and bijective on points, so Stacks 07VV applies in both directions.

```lean
theorem isEquivalence_smallEtalePullback (f : X ⟶ Y) (hf : IsIntegralHom B S hS f.hom)
    (hinj : UniversallyInjective B S hS f.hom) (hsurj : IsSurjective B S hS f.hom) :
    (smallEtalePullback B S hS f hf).IsEquivalence
```

**`AlgebraicGeometry.Space.isEquivalence_affineEtalePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/TopologicalInvariance/SmallEtale.lean, line 261](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/TopologicalInvariance/SmallEtale.lean#L261). The attribute's comment: “the equivalence `Y_affine,étale ⟶ X_affine,étale` of affine étale sites, the restriction of the equivalence on the small étale sites (that it is the restriction is `AlgebraicGeometry.Space.affineEtalePullbackInclusionIso`)”.

> **Stacks 07VW, on the affine étale schemes.** Let `f : X ⟶ Y` be an integral, universally
> injective and surjective morphism of algebraic spaces over `S`. Then base change `V ↦ X ×_Y V` is
> an equivalence from the affine étale site of `Y` to that of `X`; it is the restriction of the
> equivalence on the small étale sites (`AlgebraicGeometry.Space.affineEtalePullbackInclusionIso`).
>
> For `V` étale over `Y` and a scheme, `V` is affine exactly when `X ×_Y V` is: the projection is
> integral, so an affine `V` has affine base change, and it is surjective and universally closed,
> so an affine base change forces `V` affine by Stacks 07VT.

```lean
theorem isEquivalence_affineEtalePullback (f : X ⟶ Y) (hf : IsIntegralHom B S hS f.hom)
    (hinj : UniversallyInjective B S hS f.hom) (hsurj : IsSurjective B S hS f.hom) :
    (affineEtalePullback B S hS f hf).IsEquivalence
```

## Tag 05ZI, a remark

[Tag 05ZI](https://stacks.math.columbia.edu/tag/05ZI) in the Stacks Project.

**`AlgebraicGeometry.isIso_of_isFinite_of_etale_of_connectedSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Etale/AffineLineFiniteEtaleCovering.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Etale/AffineLineFiniteEtaleCovering.lean#L29). The attribute's comment: “the input: A^1\_k has no nontrivial connected finite étale covering when k is algebraically closed of characteristic 0 (details omitted in the source)”.

> Over an algebraically closed field `k` of characteristic zero, a finite étale morphism
> `Y ⟶ 𝐀¹_k = Spec k[X]` with `Y` connected is an isomorphism.

```lean
theorem isIso_of_isFinite_of_etale_of_connectedSpace {k : Type u} [Field k] [IsAlgClosed k]
    [CharZero k] {Y : Scheme.{u}} (f : Y ⟶ Spec (.of k[X])) [IsFinite f] [Etale f]
    [ConnectedSpace Y] : IsIso f
```

**`AlgebraicGeometry.Space.universalHomeomorphism_squaringMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversalHomeomorphism.lean, line 772](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/UniversalHomeomorphism.lean#L772). The attribute's comment: “the remark's own last sentence: there exists a universal homeomorphism X ⟶ 𝐀¹\_k, exhibited directly by t ↦ t² on affine spaces. NOT asserted: that this X is the same as the quotient Y/G of the remark's alternative construction, that Y ⟶ X is a nontrivial connected finite étale covering, and that 𝐀¹\_k has no nontrivial connected finite étale coverings”.

> **Stacks 05ZI, the last sentence: there is a universal homeomorphism `X ⟶ 𝐀¹_k`, exhibited
> directly by `t ↦ t ^ 2` on affine space.**
>
> Here `X` is the quotient of the affine line by the relation identifying `t` with `-t` away from
> the origin, the algebraic space of Stacks 05Z6, and the morphism is the one Stacks 05VS
> descends from squaring the coordinate. It is universally closed by
> `AlgebraicGeometry.Space.universallyClosed_squaringMap`, universally injective by Stacks 05VS
> part (4), and surjective after every base change by
> `AlgebraicGeometry.Space.isSurjective_pullback_fst_squaringMap`; the criterion is
> `AlgebraicGeometry.Space.universalHomeomorphism_of_universallyClosed_of_universallyInjective`.
>
> Stacks 05Z6 and Stacks 05ZI state this over an algebraically closed field of characteristic
> zero. Only `2 ≠ 0` in `k` is used, and only for universal injectivity.

```lean
theorem universalHomeomorphism_squaringMap (hchar : (2 : k) ≠ 0)
    (hk : B.Contains (Spec (.of k)))
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hk) (Type u)] :
    UniversalHomeomorphism B (Spec (.of k)) hk (squaringMap k B hk)
```

**`AlgebraicGeometry.AffineLineInvolution.whiskerLeft_punctured_comp_toQuotientSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/UniversalHomeomorphismEtaleFailure.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/UniversalHomeomorphismEtaleFailure.lean#L157). The attribute's comment: “a construction input only: the gluing datum of the covering `Y` of the remark, at the level of points. NEITHER assertion of the remark is asserted -- not that a universal homeomorphism of algebraic spaces need be non-representable, and not that Tag 05ZH fails for universal homeomorphisms”.

> **The overlap identity of Stacks 05ZI.** The two maps from the punctured affine line to the
> quotient sheaf of Stacks 02Z1, one through the inclusion of the puncture and one through
> negation of the coordinate, agree. No hypothesis on the ground field is used.

```lean
theorem whiskerLeft_punctured_comp_toQuotientSheaf {C : Type v} [Category.{w} C]
    (J : GrothendieckTopology C) [HasSheafify J (Type u)] (F : C ⥤ Over (Spec (.of k))) :
    F.op.whiskerLeft (yoneda.map (puncturedAffineLineInclusion k)) ≫
        Stacks.Groupoids.toQuotientSheaf J F (involutionRelation k) =
      F.op.whiskerLeft (yoneda.map (puncturedAffineLineInclusion k ≫ affineLineNeg k)) ≫
        Stacks.Groupoids.toQuotientSheaf J F (involutionRelation k)
```

**`AlgebraicGeometry.AffineLineInvolution.yoneda_puncturedChart_comp_quotientChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/UniversalHomeomorphismEtaleFailure.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/UniversalHomeomorphismEtaleFailure.lean#L227). The attribute's comment: “a construction input only: the two chart maps of the doubled-origin line agree over the overlap, which is the remark's `these agree on the overlap by construction of X`. The morphism `Y ⟶ X` itself is not constructed and neither assertion of the remark is asserted”.

> **The gluing datum of the covering of Stacks 05ZI.** The two maps from the punctured affine
> line to the quotient `X` of Stacks 05Z6, one through the inclusion of the puncture and one
> through negation of the coordinate, agree as morphisms of presheaves on the site.
>
> This is the assertion that the two charts of the affine line with doubled origin have the same
> image in `X` over the overlap of the charts, which is what makes the covering of Stacks 05ZI
> well defined. No hypothesis on the ground field is used.

```lean
theorem yoneda_puncturedChart_comp_quotientChart :
    yoneda.map (puncturedChartInclusion k B hk) ≫ quotientChart k B hk =
      yoneda.map (puncturedChartNeg k B hk) ≫ quotientChart k B hk
```

**`AlgebraicGeometry.connectedSpace_affineSpaceWithDoubledZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/UniversalHomeomorphismEtaleFailure.lean, line 296](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/UniversalHomeomorphismEtaleFailure.lean#L296). The attribute's comment: “a construction input only: the doubled-origin affine space is connected. That `Y ⟶ X` is a nontrivial connected finite etale covering is NOT asserted -- this library has no notion of a connected algebraic space”.

> **The connectedness input of Stacks 05ZI.** In positive dimension affine `n`-space over a
> field with its origin doubled is a connected scheme: its two charts are spectra of a polynomial
> ring, hence irreducible, they cover the glued scheme, and their images share the image of the
> generic point.

```lean
theorem connectedSpace_affineSpaceWithDoubledZero (k : Type u) [Field k] (n : ℕ) (hn : 0 < n) :
    ConnectedSpace (affineSpaceWithDoubledZero k n)
```

**`AlgebraicGeometry.chartSwapNegationData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/UniversalHomeomorphismEtaleFailure.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/UniversalHomeomorphismEtaleFailure.lean#L384). The attribute's comment: “a construction input only: the involution of `Y` of the remark's alternative route, negating the coordinate and swapping the two charts. That the induced action of `{+1,-1}` is free and that `X` is its quotient are NOT asserted”.

> **Stacks 05ZI, the alternative construction.** The endomorphism of affine space with
> doubled origin which negates the coordinates and swaps the two charts, packaged with its
> restriction to each chart.
>
> The two chart maps agree over the overlap of the charts because negation preserves the
> complement of the origin, so `AlgebraicGeometry.comp_chartInclusion_eq` applies.

```lean
noncomputable def chartSwapNegationData (k : Type u) [Field k] (n : ℕ) :
    { f : affineSpaceWithDoubledZero k n ⟶ affineSpaceWithDoubledZero k n //
      chartInclusion k n 0 ≫ f = negAffineSpace k n ≫ chartInclusion k n 1 ∧
        chartInclusion k n 1 ≫ f = negAffineSpace k n ≫ chartInclusion k n 0 }
```

**`AlgebraicGeometry.chartSwapNegation_comp_self`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/UniversalHomeomorphismEtaleFailure.lean, line 441](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Thickenings/UniversalHomeomorphismEtaleFailure.lean#L441). The attribute's comment: “a construction input only: that involution is an involution”.

> **Stacks 05ZI, the alternative construction.** Negating the coordinates and swapping the
> two charts of affine space with doubled origin is an involution, so it makes the group of
> order two act on that scheme.

```lean
theorem chartSwapNegation_comp_self (k : Type u) [Field k] (n : ℕ) :
    chartSwapNegation k n ≫ chartSwapNegation k n = 𝟙 _
```

**`AlgebraicGeometry.AffineLineInvolution.isPullback_chartPairToDoubledLine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/DoubledLineEtaleCovering/CartesianSquare.lean, line 622](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Spaces/DoubledLineEtaleCovering/CartesianSquare.lean#L622). The attribute's comment: “the remark's cartesian square: Y ← Y₁ ⨿ Y₂ over X ← 𝐀¹\_k is cartesian”.

> **Stacks 05ZI: the square of the remark is cartesian.** Away from characteristic two a
> morphism into `Y` together with a morphism into the chart `𝐀¹_k` of Stacks 05Z6 having the same
> image in `X` comes from a unique morphism into `Y₁ ⨿ Y₂`.
>
> Locally on the source the morphism into `Y` factors through one of the two charts of the
> doubled line, and there the relation of Stacks 02Z1, being the kernel pair of the chart
> `𝐀¹_k ⟶ X`, supplies the lift through
> `AlgebraicGeometry.AffineLineInvolution.relationToChartPair`. The local lifts agree because the
> two edges of the square are jointly monomorphic, so they glue; and the glued lift is unique for
> the same reason.

```lean
theorem isPullback_chartPairToDoubledLine (hchar : (2 : k) ≠ 0) :
    IsPullback (yoneda.map (chartPairToDoubledLine k B hk))
      (yoneda.map (chartPairToAffineLine k B hk)) (coveringMorphism k B hk)
      (quotientChart k B hk)
```

**`AlgebraicGeometry.AffineLineInvolution.nontrivial_connected_finiteEtale_degreeTwo_coveringMorphism`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/DoubledLineEtaleCovering/FiniteEtaleDegreeTwo.lean, line 397](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Spaces/DoubledLineEtaleCovering/FiniteEtaleDegreeTwo.lean#L397). The attribute's comment: “the remark's covering: Y, the affine line with its origin doubled, is a nontrivial connected finite étale covering of X of degree two”.

> **Stacks 05ZI.** The affine line with its origin doubled is a *nontrivial connected finite
> étale covering of degree two* of the algebraic space `X = 𝐀¹_k/\{x ∼ -x ∣ x ≠ 0\}` of
> Stacks 05Z6: the morphism `Y ⟶ X` of the remark is representable and finite locally free of
> degree two, it is étale, `Y` is a connected scheme, and `Y ⟶ X` admits no section.
>
> The remark states this for `k` algebraically closed of characteristic zero; invertibility of two
> in the ground field is all that is used. Nontriviality is expressed by the absence of a section:
> a covering which is a finite disjoint union of copies of its base has one, so a covering without
> one is not such a disjoint union.

```lean
theorem nontrivial_connected_finiteEtale_degreeTwo_coveringMorphism (hchar : (2 : k) ≠ 0) :
    ((Stacks.Morphisms.IsFiniteLocallyFreeOfRank.property.{u} 2).inverseImage
        (BigFppfOver.toScheme B (Spec (.of k)) hk)).presheaf (coveringMorphism k B hk) ∧
      (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B (Spec (.of k)) hk)).presheaf (coveringMorphism k B hk) ∧
      ConnectedSpace (doubledLine k).left ∧
      ¬ ∃ s : (involutionQuotient k B hk).obj ⟶ yoneda.obj (doubledLineSite k B hk),
        s ≫ coveringMorphism k B hk = 𝟙 (involutionQuotient k B hk).obj
```

**`AlgebraicGeometry.AffineLineInvolution.doubledLine_freeAction_quotient`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/DoubledLineInvolutionQuotient.lean, line 519](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Spaces/DoubledLineInvolutionQuotient.lean#L519). The attribute's comment: “the remark's alternative construction: G = \{±1} acts freely on Y, -1 swapping the two charts and negating the coordinate, and X = Y/G in the sense of Spaces, Definition 02Z3”.

> **Stacks 05ZI, the remark's alternative construction.** Away from characteristic two, the
> affine line with its origin doubled carries an action of the group `G = \{+1, -1\} = ℤˣ` in
> which `-1` swaps the two charts and negates the coordinate. This action is free in the sense of
> condition `(*)` of Stacks 02Z2. The quotient `Y/G` of Spaces, Definition 02Z3, is an algebraic
> space, and it is the algebraic space `X` of Stacks 05Z6: an isomorphism `X ≅ Y/G` carries the
> covering `Y ⟶ X` of the remark to the projection `Y ⟶ Y/G`.

```lean
theorem doubledLine_freeAction_quotient (hchar : (2 : k) ≠ 0)
    [HasSheafify (BigFppfOver.topology B (Spec (.of k)) hk) (Type u)] :
    (∀ b : Bool, doubledChartHom k B hk b ≫ doubledLineInvolution k B hk =
        chartNeg k B hk ≫ doubledChartHom k B hk (!b)) ∧
      (doubledLineAction k B hk (-1)).asIso.hom =
        (Over.post B.inclusion).map (doubledLineInvolution k B hk) ∧
      Space.ActsNontriviallyOnFixedResidueFields
        (Space.underlyingOver B hk (doubledLineSite k B hk)) ℤˣ (doubledLineAction k B hk) ∧
      IsAlgebraicSpace B (Spec (.of k)) hk
        (Space.actionQuotient ℤˣ B hk (doubledLineSite k B hk) (doubledLineAction k B hk)) ∧
      ∃ e : (involutionQuotient k B hk).obj ≅
          Space.actionQuotient ℤˣ B hk (doubledLineSite k B hk) (doubledLineAction k B hk),
        coveringMorphism k B hk ≫ e.hom =
          Stacks.Groupoids.quotientChart (BigFppfOver.topology B (Spec (.of k)) hk)
            (Over.post B.inclusion) (doubledLineSite k B hk)
            (Space.actionRelation (Space.underlyingOver B hk (doubledLineSite k B hk)) ℤˣ
              (doubledLineAction k B hk))
```

**`AlgebraicGeometry.AffineLineInvolution.squaringMap_universalHomeomorphism_not_representable_not_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/SquaringMapEtaleSiteFailure.lean, line 383](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Spaces/SquaringMapEtaleSiteFailure.lean#L383). The attribute's comment: “the remark's two assertions: X ⟶ 𝐀¹\_k is a universal homeomorphism which is not representable, and base change along it is not an equivalence of spaces-étale sites (it is not essentially surjective), so Theorem 05ZH fails for universal homeomorphisms”.

> **Stacks 05ZI.** Let `k` be an algebraically closed field of characteristic zero and let
> `𝐀¹_k ⟶ X ⟶ 𝐀¹_k` be as in Stacks 05Z6, with `X ⟶ 𝐀¹_k` the morphism descended from squaring
> the coordinate. Then:
>
> 1. `X` and `𝐀¹_k` are algebraic spaces and `X ⟶ 𝐀¹_k` is a universal homeomorphism;
> 2. it is not representable: a universal homeomorphism of algebraic spaces need not be
>    representable;
> 3. base change `V ↦ V ×_{𝐀¹_k} X` from the spaces-étale site of `𝐀¹_k` to that of `X` is not
>    essentially surjective;
> 4. hence it is not an equivalence, so Theorem 05ZH fails for universal homeomorphisms.
>
> The functor is `AlgebraicGeometry.Space.spacesBaseChange`, the one Stacks 05ZH is stated for.
> Only `2 ≠ 0` in `k` is used. The general statements are
> `AlgebraicGeometry.AffineLineInvolution.not_relativelyRepresentable_squaringMap` and
> `AlgebraicGeometry.AffineLineInvolution.not_essSurj_spacesBaseChange_squaringMap`. The proof of
> (3) does not use that `𝐀¹_k` has no nontrivial connected finite étale covering. It shows
> directly that the doubled-origin covering of the remark is not a base change.

```lean
theorem squaringMap_universalHomeomorphism_not_representable_not_isEquivalence
    [IsAlgClosed k] [CharZero k] :
    IsAlgebraicSpace B (Spec (.of k)) hk (involutionQuotient k B hk).obj ∧
      IsAlgebraicSpace B (Spec (.of k)) hk
        (Stacks.Groupoids.points (Over.post (X := B.obj hk) B.inclusion) (affineLine k)) ∧
      Space.UniversalHomeomorphism B (Spec (.of k)) hk (squaringMap k B hk) ∧
      ¬ yoneda.relativelyRepresentable (squaringMap k B hk) ∧
      ¬ (Space.spacesBaseChange B (Spec (.of k)) hk
          (squaringSpaceHom k B hk two_ne_zero)).functor.EssSurj ∧
      ¬ (Space.spacesBaseChange B (Spec (.of k)) hk
          (squaringSpaceHom k B hk two_ne_zero)).functor.IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.8, Tag 05ZG](https://stacks.math.columbia.edu/tag/05ZG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
