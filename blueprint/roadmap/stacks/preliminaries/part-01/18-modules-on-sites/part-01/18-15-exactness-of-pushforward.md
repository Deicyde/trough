---
declaration: section
origin: cited
lean: main_statement_equivalence, main_statement_faithful, Stacks.Topos.AbelianPushforward.abelianPushforward_exact, CategoryTheory.Functor.exactFunctor_sheafPushforwardContinuous_of_isAlmostCocontinuous, CategoryTheory.Functor.exactFunctor_sheafPushforwardContinuous_of_isAlmostCocontinuous_of_smallCategory, Stacks.SheafOfModules.PushforwardRightExact.exactFunctor_pushforward_of_isAlmostCocontinuous, Stacks.SheafOfModules.PushforwardRightExact.exactFunctor_pushforward_of_isAlmostCocontinuous_of_univLE, Stacks.SheafOfModules.PushforwardRightExact.exactFunctor_pushforward_of_isAlmostCocontinuous_of_smallCategory
statement: formalized
proof: formalized
---

# 18.15 Exactness of pushforward

Section 18.15 of the Stacks Project, [Tag 04BC](https://stacks.math.columbia.edu/tag/04BC). 3 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04DA, a lemma

[Tag 04DA](https://stacks.math.columbia.edu/tag/04DA) in the Stacks Project.

**`main_statement_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/AbelianPushforwardFaithful.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/AbelianPushforwardFaithful.lean#L163).

> **Statement 1 (Equivalence).** Let `f : Sh(C) → Sh(D)` be a morphism of
> topoi. The following are equivalent:
> 1. For all `F` in `Ab(C)`, the counit `ε_F : f^{-1} f_* F → F` is surjective
>    (an epimorphism) in `Ab(C)`.
> 2. The functor `f_* : Ab(C) → Ab(D)` reflects surjections.

```lean
theorem main_statement_equivalence (f : MorphismOfTopoiAb JC JD) :
    (∀ F : AbSh JC, Epi (f.counit F)) ↔ f.ReflectsSurjections
```

**`main_statement_faithful`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/AbelianPushforwardFaithful.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/AbelianPushforwardFaithful.lean#L177).

> **Statement 2 (Faithfulness).** If the equivalent conditions of Statement 1
> hold (we phrase the hypothesis via condition (1): the counit is surjective for
> every abelian sheaf `F`), then `f_* : Ab(C) → Ab(D)` is faithful.

```lean
theorem main_statement_faithful (f : MorphismOfTopoiAb JC JD)
    (h : ∀ F : AbSh JC, Epi (f.counit F)) : f.IsFaithful
```

## Tag 04DB, a lemma

[Tag 04DB](https://stacks.math.columbia.edu/tag/04DB) in the Stacks Project.

**`Stacks.Topos.AbelianPushforward.abelianPushforward_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Topos/AbelianPushforwardExact.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Topos/AbelianPushforwardExact.lean#L254).

> **Stacks 04DB.** Let `f : Sh(C) ⟶ Sh(D)` be a morphism of topoi and assume at least one of
>
> 1. `f_*` takes surjections of sheaves of sets to surjections,
> 2. `f_*` takes surjections of abelian sheaves to surjections,
> 3. `f_*` commutes with coequalizers of sheaves of sets,
> 4. `f_*` commutes with pushouts of sheaves of sets.
>
> Then `f_* : Ab(C) ⟶ Ab(D)` is exact.
>
> Each of (1), (3) and (4) is reduced to (2): (3) and (4) give (1) because every epimorphism of
> sheaves of sets is a regular epimorphism, and (1) gives (2) through the identification of the
> underlying sheaf of sets of a direct image with the direct image of the underlying sheaf.

```lean
theorem abelianPushforward_exact [HasSheafify J (Type w)]
    (h : f.pushforward.PreservesEpimorphisms ∨
      (abelianPushforward J f).PreservesEpimorphisms ∨
      PreservesColimitsOfShape WalkingParallelPair f.pushforward ∨
      PreservesColimitsOfShape WalkingSpan f.pushforward) :
    exactFunctor (Sheaf J AddCommGrpCat.{w}) (Sheaf K AddCommGrpCat.{w'})
      (abelianPushforward J f)
```

## Tag 04BD, a lemma

[Tag 04BD](https://stacks.math.columbia.edu/tag/04BD) in the Stacks Project.

**`CategoryTheory.Functor.exactFunctor_sheafPushforwardContinuous_of_isAlmostCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardRightExact.lean, line 329](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardRightExact.lean#L329). The attribute's comment: “part (1)”.

> **Stacks 04BD (1).** Let `f : D → C` be a morphism of sites associated to the continuous
> functor `v : C ⥤ D`, and assume `v` is almost cocontinuous. Then the direct image
> `f_* = v^s : Ab(D) ⥤ Ab(C)`, restriction of sheaves of abelian groups along `v.op`, is exact.
>
> The four site universes are unrelated and there is no hypothesis beyond the source's. Both
> sheafification facts the right exact half needs — existence, and that sheafification inverts
> exactly the locally bijective morphisms, which is what makes `Sheaf K AddCommGrpCat` abelian —
> are available at the universe `max uC vC uD vD` that a statement about two sites at once is
> forced to use, because that universe dominates each site's own `max u v`; see
> `CategoryTheory.GrothendieckTopology.hasSheafify_addCommGrpCat` and
> `CategoryTheory.GrothendieckTopology.wEqualsLocallyBijective_addCommGrpCat`.

```lean
public theorem exactFunctor_sheafPushforwardContinuous_of_isAlmostCocontinuous
    {C : Type uC} [Category.{vC} C] {D : Type uD} [Category.{vD} D]
    {J : GrothendieckTopology C} {K : GrothendieckTopology D} {v : C ⥤ D}
    (hv : IsMorphismOfSites.{max uC vC uD vD} v J K)
    (ha : IsAlmostCocontinuous v J K) :
    letI : v.IsContinuous J K := hv.toIsContinuous
    exactFunctor (Sheaf K AddCommGrpCat.{max uC vC uD vD})
      (Sheaf J AddCommGrpCat.{max uC vC uD vD})
      (v.sheafPushforwardContinuous AddCommGrpCat.{max uC vC uD vD} J K)
```

**`CategoryTheory.Functor.exactFunctor_sheafPushforwardContinuous_of_isAlmostCocontinuous_of_smallCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardRightExact.lean, line 354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardRightExact.lean#L354). The attribute's comment: “part (1), for small sites”.

> **Stacks 04BD (1)** for sites that are small categories, with sheaves of abelian groups in the
> site's own universe: the setting of the source, in which the hypotheses are exactly the source's,
> namely a morphism of sites whose continuous functor is almost cocontinuous.

```lean
public theorem exactFunctor_sheafPushforwardContinuous_of_isAlmostCocontinuous_of_smallCategory
    {C : Type u} [SmallCategory C] {D : Type u} [SmallCategory D]
    {J : GrothendieckTopology C} {K : GrothendieckTopology D} {v : C ⥤ D}
    (hv : IsMorphismOfSites.{u} v J K) (ha : IsAlmostCocontinuous v J K) :
    letI : v.IsContinuous J K := hv.toIsContinuous
    exactFunctor (Sheaf K AddCommGrpCat.{u}) (Sheaf J AddCommGrpCat.{u})
      (v.sheafPushforwardContinuous AddCommGrpCat.{u} J K)
```

**`Stacks.SheafOfModules.PushforwardRightExact.exactFunctor_pushforward_of_isAlmostCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardRightExact.lean, line 423](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardRightExact.lean#L423). The attribute's comment: “part (2)”.

> **Stacks 04BD (2).** Let `f : D → C` be a morphism of sites associated to the continuous
> functor `v : C ⥤ D` with `v` almost cocontinuous, and let `f^♯ : S ⟶ f_* R` make `f` a morphism of
> ringed sites. Then the direct image `f_* : Mod(R) ⥤ Mod(S)` is exact.
>
> As in part (1) this additionally assumes that sheafification of `AddCommGrpCat.{m}`-valued
> presheaves exists and inverts exactly the locally bijective morphisms, for both topologies; that is
> what makes the two categories of sheaves of modules abelian, and it holds automatically in the
> setting of the source, as recorded by
> `exactFunctor_pushforward_of_isAlmostCocontinuous_of_smallCategory`.

```lean
public theorem exactFunctor_pushforward_of_isAlmostCocontinuous
    {C : Type uC} [Category.{vC} C] {D : Type uD} [Category.{vD} D]
    {J : GrothendieckTopology C} {K : GrothendieckTopology D} {v : C ⥤ D}
    (hv : IsMorphismOfSites.{max uC vC uD vD} v J K)
    (ha : IsAlmostCocontinuous v J K)
    {S : Sheaf J RingCat.{r}} {R : Sheaf K RingCat.{r}}
    (φ : letI : v.IsContinuous J K := hv.toIsContinuous
      S ⟶ (v.sheafPushforwardContinuous RingCat.{r} J K).obj R)
    [HasSheafify J AddCommGrpCat.{m}] [HasSheafify K AddCommGrpCat.{m}]
    [J.WEqualsLocallyBijective AddCommGrpCat.{m}]
    [K.WEqualsLocallyBijective AddCommGrpCat.{m}] :
    letI : v.IsContinuous J K := hv.toIsContinuous
    exactFunctor (SheafOfModules.{m} R) (SheafOfModules.{m} S)
      (SheafOfModules.pushforward φ)
```

**`Stacks.SheafOfModules.PushforwardRightExact.exactFunctor_pushforward_of_isAlmostCocontinuous_of_univLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardRightExact.lean, line 446](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardRightExact.lean#L446). The attribute's comment: “part (2)”.

> **Stacks 04BD (2)** with the four sheafification hypotheses replaced by the single universe
> inequality they follow from: the module universe `m` dominates both sites. This is the sharpest
> form the statement takes with `m` still a variable — at `m = max uC vC uD vD` the inequality is
> an instance, so there the statement holds with no hypothesis beyond the source's.

```lean
public theorem exactFunctor_pushforward_of_isAlmostCocontinuous_of_univLE
    {C : Type uC} [Category.{vC} C] {D : Type uD} [Category.{vD} D]
    {J : GrothendieckTopology C} {K : GrothendieckTopology D} {v : C ⥤ D}
    (hv : IsMorphismOfSites.{max uC vC uD vD} v J K)
    (ha : IsAlmostCocontinuous v J K)
    {S : Sheaf J RingCat.{r}} {R : Sheaf K RingCat.{r}}
    (φ : letI : v.IsContinuous J K := hv.toIsContinuous
      S ⟶ (v.sheafPushforwardContinuous RingCat.{r} J K).obj R)
    [UnivLE.{max uC vC uD vD, m}] :
    letI : v.IsContinuous J K := hv.toIsContinuous
    exactFunctor (SheafOfModules.{m} R) (SheafOfModules.{m} S)
      (SheafOfModules.pushforward φ)
```

**`Stacks.SheafOfModules.PushforwardRightExact.exactFunctor_pushforward_of_isAlmostCocontinuous_of_smallCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardRightExact.lean, line 476](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardRightExact.lean#L476). The attribute's comment: “part (2), for small sites”.

> **Stacks 04BD (2)** for sites that are small categories, with the sheaf of rings and the
> sheaves of modules in the site's own universe: the setting of the source, in which the hypotheses
> are exactly the source's.

```lean
public theorem exactFunctor_pushforward_of_isAlmostCocontinuous_of_smallCategory
    {C : Type u} [SmallCategory C] {D : Type u} [SmallCategory D]
    {J : GrothendieckTopology C} {K : GrothendieckTopology D} {v : C ⥤ D}
    (hv : IsMorphismOfSites.{u} v J K) (ha : IsAlmostCocontinuous v J K)
    {S : Sheaf J RingCat.{u}} {R : Sheaf K RingCat.{u}}
    (φ : letI : v.IsContinuous J K := hv.toIsContinuous
      S ⟶ (v.sheafPushforwardContinuous RingCat.{u} J K).obj R) :
    letI : v.IsContinuous J K := hv.toIsContinuous
    exactFunctor (SheafOfModules.{u} R) (SheafOfModules.{u} S)
      (SheafOfModules.pushforward φ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.15, Tag 04BC](https://stacks.math.columbia.edu/tag/04BC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
