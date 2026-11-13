---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isEquivalence_inverseImage_of_isEquivalenceOver_stackifications, AlgebraicGeometry.Stack.isEquivalence_modulePullback_of_isStackification_of_isEquivalenceOver, AlgebraicGeometry.Stack.isEquivalence_quasicoherentPullback_of_isStackification_of_isEquivalenceOver
statement: formalized
proof: formalized
---

# 96.13 Stackification and sheaves

Section 96.13 of the Stacks Project, [Tag 06WP](https://stacks.math.columbia.edu/tag/06WP). 2 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06WQ, a lemma

[Tag 06WQ](https://stacks.math.columbia.edu/tag/06WQ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isEquivalence_inverseImage_of_isEquivalenceOver_stackifications`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/StackificationInduced.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/StackificationInduced.lean#L92).

> **Stacks 06WQ.** Let `F : 𝒳 ⥤ 𝒴` be a 1-morphism of categories fibred in groupoids over the
> big fppf category of `S`. If `F` induces an equivalence of stackifications, then the morphism of
> topoi `Sh(𝒳_fppf) ⟶ Sh(𝒴_fppf)` of Stacks 06TS is an equivalence.
>
> That `F` induces an equivalence of stackifications is stated with stackifications
> `G : 𝒳 ⥤ 𝒳'` and `H : 𝒴 ⥤ 𝒴'` in the sense of Stacks 02ZN
> (`CategoryTheory.Functor.IsFibredOneMorphism.IsStackification`), and a 1-morphism
> `E : 𝒳' ⥤ 𝒴'` over the base which is an equivalence over the base and is compatible with `F` by
> a vertical 2-isomorphism `F ⋙ H ≅ G ⋙ E`; by the universal property of stackification
> (Stacks 0435) such an `E` is the 1-morphism of stackifications induced by `F`.
>
> The functor displayed is the inverse image of that morphism of topoi, which by Stacks 06TS is
> restriction along `F`; the morphism of topoi is an equivalence exactly when its inverse image
> is.

```lean
theorem isEquivalence_inverseImage_of_isEquivalenceOver_stackifications
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 : Type v₁} [Category.{u} 𝒳] {𝒴 : Type v₂} [Category.{u} 𝒴]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (q : 𝒴 ⥤ BigFppfOver B S hS)
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids)
    (F : 𝒳 ⥤ 𝒴) (hF : p.IsFibredOneMorphism q F)
    {𝒳' : Type*} [Category.{u} 𝒳'] {𝒴' : Type*} [Category.{u} 𝒴']
    (p' : 𝒳' ⥤ BigFppfOver B S hS) (q' : 𝒴' ⥤ BigFppfOver B S hS) [p'.IsFibered]
    [q'.IsFibered] (G : 𝒳 ⥤ 𝒳') (hG : p.IsFibredOneMorphism p' G)
    (hGst : letI : p.IsFibered := hp.isFibered
      hG.IsStackification (BigFppfOver.topology B S hS))
    (H : 𝒴 ⥤ 𝒴') (hH : q.IsFibredOneMorphism q' H)
    (hHst : letI : q.IsFibered := hq.isFibered
      hH.IsStackification (BigFppfOver.topology B S hS))
    (E : 𝒳' ⥤ 𝒴') (hE : p'.IsFibredOneMorphism q' E) (hEeq : Functor.IsEquivalenceOver p' q' E)
    (α : F ⋙ H ≅ G ⋙ E) (hα : ∀ a : 𝒳, q'.IsHomLift (𝟙 (p.obj a)) (α.hom.app a)) :
    letI : p.IsFibered := hp.isFibered
    letI : q.IsFibered := hq.isFibered
    letI := (hF.isContinuous_and_isCocontinuous_inheritedTopology
      (BigFppfOver.topology B S hS)).1
    (F.sheafPushforwardContinuous (Type (max t u v₁ v₂))
      (p.inheritedTopology (BigFppfOver.topology B S hS))
      (q.inheritedTopology (BigFppfOver.topology B S hS))).IsEquivalence
```

## Tag 06WR, a lemma

[Tag 06WR](https://stacks.math.columbia.edu/tag/06WR) in the Stacks Project.

**`AlgebraicGeometry.Stack.isEquivalence_modulePullback_of_isStackification_of_isEquivalenceOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/StackificationModulesOfStackifications.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/StackificationModulesOfStackifications.lean#L79). The attribute's comment: “the Mod clause: f^* is an equivalence Mod(𝒪\_𝒴) ⥤ Mod(𝒪\_𝒳), for categories fibred in groupoids in arbitrary universes and modules in any universe containing that of the rings”.

> **Stacks 06WR, the `Mod` clause.**  Let `f : 𝒳 ⥤ 𝒴` be a 1-morphism of categories fibred in
> groupoids over the big fppf category of `S`, and suppose `f` induces an equivalence of
> stackifications: `G_𝒳 : 𝒳 ⥤ 𝒳'` and `G_𝒴 : 𝒴 ⥤ 𝒴'` are stackifications in the sense of
> Stacks 02ZN, and the 1-morphism `f' : 𝒳' ⥤ 𝒴'` with a vertical 2-isomorphism
> `f ⋙ G_𝒴 ≅ G_𝒳 ⋙ f'` is an equivalence over the base.  Then the inverse image of sheaves of
> modules of Stacks 06WE is an equivalence `Mod(𝒪_𝒴) ⥤ Mod(𝒪_𝒳)`, for modules with sections in any
> universe containing `u`.
>
> The hypothesis gives the two local criteria of Stacks 02ZN for `f`
> (`CategoryTheory.Functor.IsFibredOneMorphism.isStackificationEquivalence'_of_isEquivalenceOver`),
> from which `isEquivalence_modulePullback_of_isStackificationEquivalence_anyUniverse`
> concludes.

```lean
theorem isEquivalence_modulePullback_of_isStackification_of_isEquivalenceOver
    {hGX : p.IsFibredOneMorphism p' GX} {hGY : q.IsFibredOneMorphism q' GY}
    (hGXs : letI : p.IsFibered := hp.isFibered
      hGX.IsStackification (BigFppfOver.topology B S hS))
    (hGYs : letI : q.IsFibered := hq.isFibered
      hGY.IsStackification (BigFppfOver.topology B S hS))
    (hf' : p'.IsFibredOneMorphism q' f') (hf'eq : Functor.IsEquivalenceOver p' q' f')
    (α : f ⋙ GY ≅ GX ⋙ f') (hα : ∀ a : 𝒳, q'.IsHomLift (𝟙 (p.obj a)) (α.hom.app a)) :
    (modulePullback.{u, v₁, w, max u m, v₂, w} B S hS p q hp hq f hF.comp_eq
      B.topology le_rfl).IsEquivalence
```

**`AlgebraicGeometry.Stack.isEquivalence_quasicoherentPullback_of_isStackification_of_isEquivalenceOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/StackificationModulesOfStackifications.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/StackificationModulesOfStackifications.lean#L112). The attribute's comment: “the QCoh clause: f^* is an equivalence QCoh(𝒪\_𝒴) ⥤ QCoh(𝒪\_𝒳), for categories fibred in groupoids in arbitrary universes and modules in any universe containing that of the rings”.

> **Stacks 06WR, the `QCoh` clause.**  Let `f : 𝒳 ⥤ 𝒴` be a 1-morphism of categories fibred in
> groupoids over the big fppf category of `S`, and suppose `f` induces an equivalence of
> stackifications: `G_𝒳 : 𝒳 ⥤ 𝒳'` and `G_𝒴 : 𝒴 ⥤ 𝒴'` are stackifications in the sense of
> Stacks 02ZN, and the 1-morphism `f' : 𝒳' ⥤ 𝒴'` with a vertical 2-isomorphism
> `f ⋙ G_𝒴 ≅ G_𝒳 ⋙ f'` is an equivalence over the base.  Then the inverse image of quasi-coherent
> modules is an equivalence `QCoh(𝒪_𝒴) ⥤ QCoh(𝒪_𝒳)`, for modules with sections in any universe
> containing `u`.
>
> The hypothesis gives the two local criteria of Stacks 02ZN for `f`
> (`CategoryTheory.Functor.IsFibredOneMorphism.isStackificationEquivalence'_of_isEquivalenceOver`),
> from which
> `isEquivalence_quasicoherentPullback_of_isStackificationEquivalence_anyUniverse`
> concludes.

```lean
theorem isEquivalence_quasicoherentPullback_of_isStackification_of_isEquivalenceOver
    {hGX : p.IsFibredOneMorphism p' GX} {hGY : q.IsFibredOneMorphism q' GY}
    (hGXs : letI : p.IsFibered := hp.isFibered
      hGX.IsStackification (BigFppfOver.topology B S hS))
    (hGYs : letI : q.IsFibered := hq.isFibered
      hGY.IsStackification (BigFppfOver.topology B S hS))
    (hf' : p'.IsFibredOneMorphism q' f') (hf'eq : Functor.IsEquivalenceOver p' q' f')
    (α : f ⋙ GY ≅ GX ⋙ f') (hα : ∀ a : 𝒳, q'.IsHomLift (𝟙 (p.obj a)) (α.hom.app a)) :
    (quasicoherentPullback'.{u, v₁, w, max u m, v₂, w} B S hS p q hp hq f
      hF.comp_eq).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.13, Tag 06WP](https://stacks.math.columbia.edu/tag/06WP)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
