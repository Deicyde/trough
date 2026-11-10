---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isEquivalence_inverseImage_of_isStackificationEquivalence, AlgebraicGeometry.Stack.isEquivalence_modulePullback_of_isStackificationEquivalence, AlgebraicGeometry.Stack.isEquivalence_quasicoherentPullback_of_isStackificationEquivalence, AlgebraicGeometry.Stack.isEquivalence_modulePullback_of_isStackificationEquivalence_anyUniverse, AlgebraicGeometry.Stack.isEquivalence_quasicoherentPullback_of_isStackificationEquivalence_anyUniverse
statement: formalized
proof: formalized
---

# 96.13 Stackification and sheaves

Section 96.13 of the Stacks Project, [Tag 06WP](https://stacks.math.columbia.edu/tag/06WP). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06WQ, a lemma

[Tag 06WQ](https://stacks.math.columbia.edu/tag/06WQ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isEquivalence_inverseImage_of_isStackificationEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Stackification.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/Stackification.lean#L377).

> **Stacks 06WQ.** If a 1-morphism `F : 𝒳 ⥤ 𝒴` of categories fibred in groupoids over the big
> fppf category of `S` induces an equivalence of stackifications, then the morphism of topoi
> `Sh(𝒳_fppf) ⟶ Sh(𝒴_fppf)` of Stacks 06TS is an equivalence.
>
> The functor displayed is the inverse image of that morphism of topoi, which by Stacks 06TS is
> restriction along `F`; the morphism of topoi is an equivalence exactly when its inverse image
> is.

```lean
theorem isEquivalence_inverseImage_of_isStackificationEquivalence
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 : Type v₁} [Category.{u} 𝒳] {𝒴 : Type v₂} [Category.{u} 𝒴]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (q : 𝒴 ⥤ BigFppfOver B S hS)
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids)
    (F : 𝒳 ⥤ 𝒴) (hF : p.IsFibredOneMorphism q F)
    (heq : letI : p.IsFibered := hp.isFibered
      letI : q.IsFibered := hq.isFibered
      hF.IsStackificationEquivalence (BigFppfOver.topology B S hS)) :
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

**`AlgebraicGeometry.Stack.isEquivalence_modulePullback_of_isStackificationEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/StackificationModules.lean, line 127](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/StackificationModules.lean#L127). The attribute's comment: “modules”.

> **Stacks 06WR, the `Mod` clause.** Let `f : 𝒳 ⥤ 𝒴` be a 1-morphism of categories fibred in
> groupoids over the big fppf category of `S`. If `f` induces an equivalence of stackifications,
> then the inverse image of sheaves of modules of Stacks 06WE is an equivalence
> `Mod(𝒪_𝒴) ⥤ Mod(𝒪_𝒳)`.
>
> Equivalence of stackifications makes `f` a dense subsite inclusion for the associated fppf
> topologies, by the engine of Stacks 06WQ; the structure sheaf of `𝒳` is the restriction along
> `f` of that of `𝒴`, so the inverse image *is* restriction of sections, and the Comparison
> Lemma for sheaves of modules applies.

```lean
theorem isEquivalence_modulePullback_of_isStackificationEquivalence
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {𝒳 : Type u} [Category.{u} 𝒳] {𝒴 : Type u} [Category.{u} 𝒴]
    (p : 𝒳 ⥤ BigFppfOver B S hS) (q : 𝒴 ⥤ BigFppfOver B S hS)
    (hp : p.IsFiberedInGroupoids) (hq : q.IsFiberedInGroupoids)
    (f : 𝒳 ⥤ 𝒴) (hF : p.IsFibredOneMorphism q f)
    (heq : letI : p.IsFibered := hp.isFibered
      letI : q.IsFibered := hq.isFibered
      hF.IsStackificationEquivalence (BigFppfOver.topology B S hS)) :
    (modulePullback.{u, u, u, u, u, u} B S hS p q hp hq f hF.comp_eq
      B.topology le_rfl).IsEquivalence
```

**`AlgebraicGeometry.Stack.isEquivalence_quasicoherentPullback_of_isStackificationEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/StackificationModules.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/StackificationModules.lean#L273). The attribute's comment: “quasi-coherent modules”.

> **Stacks 06WR, the `QCoh` clause.** If `f : 𝒳 ⥤ 𝒴` induces an equivalence of
> stackifications, then the inverse image of quasi-coherent modules is an equivalence
> `QCoh(𝒪_𝒴) ⥤ QCoh(𝒪_𝒳)`.
>
> Fullness and faithfulness come from the equivalence on all modules, since `QCoh` is a full
> subcategory; essential surjectivity needs in addition that `f^*` reflects quasi-coherence,
> which is `AlgebraicGeometry.Stack.isQuasicoherentOnSite_of_modulePullback`.

```lean
theorem isEquivalence_quasicoherentPullback_of_isStackificationEquivalence
    (heq : letI : p.IsFibered := hp.isFibered
      letI : q.IsFibered := hq.isFibered
      hF.IsStackificationEquivalence (BigFppfOver.topology B S hS)) :
    (quasicoherentPullback B S hS p q hp hq f hF).IsEquivalence
```

**`AlgebraicGeometry.Stack.isEquivalence_modulePullback_of_isStackificationEquivalence_anyUniverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/StackificationModulesAnyUniverse.lean, line 265](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/StackificationModulesAnyUniverse.lean#L265). The attribute's comment: “the Mod clause: f^* is an equivalence Mod(𝒪\_𝒴) ⥤ Mod(𝒪\_𝒳), for categories fibred in groupoids in arbitrary universes and modules in any universe containing that of the rings”.

> **Stacks 06WR, the `Mod` clause.**  Let `f : 𝒳 ⥤ 𝒴` be a 1-morphism of categories fibred in
> groupoids over the big fppf category of `S`.  If `f` induces an equivalence of stackifications,
> then the inverse image of sheaves of modules of Stacks 06WE is an equivalence
> `Mod(𝒪_𝒴) ⥤ Mod(𝒪_𝒳)`, for modules with sections in any universe containing `u`.
>
> `f` is a dense subsite inclusion for the associated fppf topologies (Stacks 06WQ), restriction of
> abelian sheaves along it is an equivalence
> (`isEquivalence_sheafPushforwardContinuous_of_isStackificationEquivalence`), and the structure
> sheaf of `𝒳` is the restriction along `f` of that of `𝒴`, so the Comparison Lemma for sheaves of
> modules applies.

```lean
theorem isEquivalence_modulePullback_of_isStackificationEquivalence_anyUniverse
    (heq : letI : p.IsFibered := hp.isFibered
      letI : q.IsFibered := hq.isFibered
      hF.IsStackificationEquivalence' (BigFppfOver.topology B S hS)) :
    (modulePullback.{u, v₁, w, max u m, v₂, w} B S hS p q hp hq f hF.comp_eq
      B.topology le_rfl).IsEquivalence
```

**`AlgebraicGeometry.Stack.isEquivalence_quasicoherentPullback_of_isStackificationEquivalence_anyUniverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/StackificationModulesAnyUniverse.lean, line 293](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/Sheaves/StackificationModulesAnyUniverse.lean#L293). The attribute's comment: “the QCoh clause: f^* is an equivalence QCoh(𝒪\_𝒴) ⥤ QCoh(𝒪\_𝒳), for categories fibred in groupoids in arbitrary universes and modules in any universe containing that of the rings”.

> **Stacks 06WR, the `QCoh` clause.**  Let `f : 𝒳 ⥤ 𝒴` be a 1-morphism of categories fibred in
> groupoids over the big fppf category of `S`.  If `f` induces an equivalence of stackifications,
> then the inverse image of quasi-coherent modules is an equivalence `QCoh(𝒪_𝒴) ⥤ QCoh(𝒪_𝒳)`, for
> modules with sections in any universe containing `u`.
>
> Fullness and faithfulness come from the `Mod` clause, since `QCoh` is a full subcategory;
> essential surjectivity needs in addition that `f^*` reflects quasi-coherence, which holds because
> `f` is cover-dense (`AlgebraicGeometry.Stack.isQuasicoherentOnSite_of_modulePullback'`).

```lean
theorem isEquivalence_quasicoherentPullback_of_isStackificationEquivalence_anyUniverse
    (heq : letI : p.IsFibered := hp.isFibered
      letI : q.IsFibered := hq.isFibered
      hF.IsStackificationEquivalence' (BigFppfOver.topology B S hS)) :
    (quasicoherentPullback'.{u, v₁, w, max u m, v₂, w} B S hS p q hp hq f
      hF.comp_eq).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 96.13, Tag 06WP](https://stacks.math.columbia.edu/tag/06WP)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
