---
declaration: section
origin: cited
lean: CategoryTheory.Functor.IsStack, CategoryTheory.Functor.isStack_iff_isEquivalence_toDescentData, CategoryTheory.Functor.IsStack.fullSubcategory, CategoryTheory.BasedCategory.isStack_iff_of_equivalence, CategoryTheory.BasedStack, CategoryTheory.BasedStack.Hom, CategoryTheory.BasedStack.homCategory, CategoryTheory.BasedStack.bicategory
statement: formalized
proof: formalized
---

# 8.4 Stacks

Section 8.4 of the Stacks Project, [Tag 0268](https://stacks.math.columbia.edu/tag/0268). 9 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 026F, a definition

[Tag 026F](https://stacks.math.columbia.edu/tag/026F) in the Stacks Project.

**`CategoryTheory.Functor.IsStack`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Descent/IsStack/Defs.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Descent/IsStack/Defs.lean#L44). The attribute's comment: “for a functor, the three conditions being the three fields”.

> The three conditions of Stacks 026F for a functor `p : 𝒳 ⥤ 𝒮`: `p` is a fibred category, the
> presheaves `Mor(x, y)` of Stacks 02ZB are sheaves, and descent along a covering sieve is
> effective.
>
> Condition (2) refers to the chosen pullbacks that condition (1) provides, which is why its field
> reintroduces `isFibered` as an instance.

```lean
structure IsStack (p : 𝒳 ⥤ 𝒮) (J : GrothendieckTopology 𝒮) : Prop
```

## Tag 02ZF, a lemma

[Tag 02ZF](https://stacks.math.columbia.edu/tag/02ZF) in the Stacks Project.

**`CategoryTheory.Functor.isStack_iff_isEquivalence_toDescentData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/DescentDataEquivalence.lean, line 375](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/DescentDataEquivalence.lean#L375).

> **Stacks 02ZF.** Let `p : 𝒳 ⥤ 𝒮` be a fibred category over a site `(𝒮, J)`. Then `p` is a stack
> if and only if, for every covering `𝒰 = {f i : U i ⟶ U}` of the site, the functor `𝒳_U ⥤ DD(𝒰)`
> sending an object of the fibre over `U` to its canonical descent datum relative to `𝒰` is an
> equivalence.

```lean
theorem isStack_iff_isEquivalence_toDescentData (J : GrothendieckTopology 𝒮) :
    p.IsStack J ↔ ∀ ⦃U : 𝒮⦄ (𝒰 : PreZeroHypercover.{max u₁ v₁} U), 𝒰.sieve₀ ∈ J U →
      ((pullbackPseudofunctor p).toDescentData 𝒰.f).IsEquivalence
```

## Tag 04TU, a lemma

[Tag 04TU](https://stacks.math.columbia.edu/tag/04TU) in the Stacks Project.

**`CategoryTheory.Functor.IsStack.fullSubcategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Descent/IsStack.lean, line 113](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Descent/IsStack.lean#L113).

> Let `p : 𝒳 ⥤ 𝒮` be a stack over the site `(𝒮, J)` and let `P` cut out a full subcategory of
> `𝒳`. If `P` is closed under strongly cartesian pullbacks and locally closed, both read fibrewise
> through `IsoOverId`, then the restriction of `p` to that full subcategory is a stack.

```lean
theorem IsStack.fullSubcategory (p : 𝒳 ⥤ 𝒮) (J : GrothendieckTopology 𝒮) (hp : IsStack p J)
    (P : ObjectProperty 𝒳) (h1 : ClosedUnderStronglyCartesian p P)
    (h3 : haveI : p.IsPreFibered := hp.isFibered.toIsPreFibered; LocallyClosed p P J) :
    IsStack (Functor.restrict p P) J
```

## Tag 042W, a lemma

[Tag 042W](https://stacks.math.columbia.edu/tag/042W) in the Stacks Project.

**`CategoryTheory.BasedCategory.isStack_iff_of_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/Transport.lean, line 32](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/Transport.lean#L32).

> Let `(𝒞, J)` be a site and let `𝒳`, `𝒴` be categories over `𝒞`. If `𝒳` and `𝒴` are equivalent
> as categories over `𝒞`, then `𝒳` is a stack over `𝒞` if and only if `𝒴` is.

```lean
theorem BasedCategory.isStack_iff_of_equivalence
    (e : BasedCategory.Equivalence 𝒳 𝒴) (J : GrothendieckTopology 𝒞) :
    𝒳.p.IsStack J ↔ 𝒴.p.IsStack J
```

## Tag 02ZG, a definition

[Tag 02ZG](https://stacks.math.columbia.edu/tag/02ZG) in the Stacks Project.

**`CategoryTheory.BasedStack`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/TwoCategory.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/TwoCategory.lean#L62). The attribute's comment: “(1)”.

> **Stacks 02ZG (1)**.
> An object of the 2-category of stacks over the site `(𝒞, J)`: a category over `𝒞` whose structure
> functor is a stack.

```lean
structure BasedStack (𝒞 : Type u₁) [Category.{v₁} 𝒞] (J : GrothendieckTopology 𝒞)
```

**`CategoryTheory.BasedStack.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/TwoCategory.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/TwoCategory.lean#L78). The attribute's comment: “(2)”.

> **Stacks 02ZG (2)**.
> A 1-morphism of stacks over `𝒞`: a functor `G` between the underlying categories with
> `p' ∘ G = p`, which carries strongly cartesian morphisms to strongly cartesian morphisms. The
> first condition is the field `w` of a `BasedFunctor` and is repeated as `comp_eq` inside
> `Functor.IsFibredOneMorphism`.

```lean
structure Hom (𝒳 𝒴 : BasedStack.{v₁, v₂, u₁, u₂} 𝒞 J)
```

**`CategoryTheory.BasedStack.homCategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/TwoCategory.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/TwoCategory.lean#L109). The attribute's comment: “(3)”.

> **Stacks 02ZG (3)**.
> The 2-morphisms between two 1-morphisms of stacks: the morphisms of functors `t` with
> `p'(t_x) = 𝟙 (p x)` for every object `x`, that is the `BasedNatTrans` between the underlying
> functors over `𝒞`. Nothing is imposed on a 2-morphism beyond that, so this category of
> 1-morphisms is the one of the ambient 2-category `BasedCategory 𝒞`.

```lean
instance homCategory (𝒳 𝒴 : BasedStack.{v₁, v₂, u₁, u₂} 𝒞 J) : Category (𝒳 ⟶ 𝒴)
```

**`CategoryTheory.BasedStack.bicategory`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/TwoCategory.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/TwoCategory.lean#L203).

> **Stacks 02ZG**.
> The 2-category of stacks over the site `(𝒞, J)`: the sub-2-category of the 2-category of fibred
> categories over `𝒞` (Stacks 02XP) whose objects are the stacks over `𝒞`, whose 1-morphisms are the
> functors over `𝒞` preserving strongly cartesian morphisms, and whose 2-morphisms are the morphisms
> of functors whose components lie over identities.

```lean
instance bicategory : Bicategory (BasedStack.{v₁, v₂, u₁, u₂} 𝒞 J)
```

## Tag 026G, a lemma

[Tag 026G](https://stacks.math.columbia.edu/tag/026G) in the Stacks Project.

**`CategoryTheory.TwoFibreProductOver.isStack_structureFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/TwoFibreProductDescentIndependentBase.lean, line 647](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/TwoFibreProductDescentIndependentBase.lean#L647).

> The 2-fibre product of stacks over a site `(𝒞, J)` is a stack, with the hom universe of the
> site independent of the hom universe of the three categories of the cospan: if `p𝒳`, `p𝒴`, `p𝒮`
> are stacks over `(𝒞, J)` and `F`, `G` are 1-morphisms of fibred categories over `𝒞`, then the
> structure functor of the explicit 2-fibre product `𝒳 ×_𝒮 𝒴` is again a stack.

```lean
theorem isStack_structureFunctor
    (p𝒳 : 𝒳 ⥤ 𝒞) (p𝒴 : 𝒴 ⥤ 𝒞) (p𝒮 : 𝒮 ⥤ 𝒞) (F : 𝒳 ⥤ 𝒮) (G : 𝒴 ⥤ 𝒮)
    (J : GrothendieckTopology 𝒞) (h𝒳 : Functor.IsStack p𝒳 J) (h𝒴 : Functor.IsStack p𝒴 J)
    (h𝒮 : Functor.IsStack p𝒮 J) (hF : Functor.IsFibredOneMorphism p𝒳 p𝒮 F)
    (hG : Functor.IsFibredOneMorphism p𝒴 p𝒮 G) :
    Functor.IsStack (TwoFibreProductOver.structureFunctor p𝒳 p𝒴 p𝒮 F G) J
```

## Tag 04WQ, a lemma

[Tag 04WQ](https://stacks.math.columbia.edu/tag/04WQ) in the Stacks Project.

**`CategoryTheory.Stack.Hom.isFullyFaithful_iff_morSheafIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Descent/IsPrestack.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Descent/IsPrestack.lean#L248).

> **Stacks 04WQ**. A 1-morphism of stacks is fully faithful if and only if it induces
> isomorphisms on the sheaves of morphisms.
>
> Condition (1) is read fibrewise here rather than on the total categories, which is what makes the
> implication from (2) available without the reduction to strongly cartesian morphisms of the Stacks
> proof; see `Stack.Hom.IsFullyFaithful`.

```lean
theorem isFullyFaithful_iff_morSheafIso (F : Stack.Hom T T') :
    F.IsFullyFaithful ↔ F.MorSheafIso
```

## Tag 046N, a lemma

[Tag 046N](https://stacks.math.columbia.edu/tag/046N) in the Stacks Project.

**`CategoryTheory.Functor.isEquivalenceOver_iff_locallyEssSurjOnFibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/InheritedTopology/FullyFaithfulEquivalence.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/InheritedTopology/FullyFaithfulEquivalence.lean#L55).

> **Stacks 046N**. Let `(𝒞, J)` be a site, let `p : 𝒳 ⥤ 𝒞` and `q : 𝒴 ⥤ 𝒞` be stacks over `𝒞`
> and let `F : 𝒳 ⥤ 𝒴` be a fully faithful 1-morphism of fibred categories over `𝒞`. Then the
> following are equivalent:
>
> 1. `F` is an equivalence over `𝒞`;
> 2. for every object `U` of `𝒞` and every object `x` of the fibre of `𝒴` over `U` there is a
>    covering sieve of `U` along each member `f` of which `f^* x` is in the essential image of the
>    functor induced by `F` on the fibres over the source of `f`.

```lean
theorem isEquivalenceOver_iff_locallyEssSurjOnFibers
    {p : 𝒳 ⥤ 𝒞} {q : 𝒴 ⥤ 𝒞} {F : 𝒳 ⥤ 𝒴} {J : GrothendieckTopology 𝒞}
    (h₁ : p.IsStack J) (h₂ : q.IsStack J) (hF : IsFibredOneMorphism p q F)
    [F.Full] [F.Faithful] :
    Nonempty (IsEquivalenceOver p q F) ↔ LocallyEssSurjOnFibers h₂.isFibered hF.comp_eq J
```

## Tag 03ZZ, a remark

[Tag 03ZZ](https://stacks.math.columbia.edu/tag/03ZZ) in the Stacks Project.

**`CategoryTheory.Functor.small_fibreRepresentatives`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/FibreRepresentatives.lean, line 102](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/FibreRepresentatives.lean#L102). The attribute's comment: “the cutdown: a full subcategory of 𝒳 whose objects form a set”.

> The objects of the cutdown form a set: they are indexed by the pairs of an object `U` of `𝒮`
> and an object of the small model of `𝒳_U`.

```lean
instance small_fibreRepresentatives :
    ObjectProperty.Small.{max u₁ w} (p.fibreRepresentatives)
```

**`CategoryTheory.Functor.small_fiber_restrict_fibreRepresentatives`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/FibreRepresentatives.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/FibreRepresentatives.lean#L118). The attribute's comment: “the cutdown: each of its fibres is a set”.

> Each fibre of the cutdown is a set at the universe of condition (4): the fibre over `U` is
> covered by the small model of `𝒳_U`.

```lean
instance small_fiber_restrict_fibreRepresentatives (U : 𝒮) :
    Small.{w} ((p.restrict p.fibreRepresentatives).Fiber U)
```

**`CategoryTheory.Functor.isEquivalence_ι_fibreRepresentatives`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/FibreRepresentatives.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/FibreRepresentatives.lean#L140). The attribute's comment: “(b): the inclusion of the cutdown is fully faithful and essentially surjective”.

> **Stacks 03ZZ (b).** The inclusion `𝒳_small ⥤ 𝒳` of the cutdown is fully faithful and
> essentially surjective.

```lean
theorem isEquivalence_ι_fibreRepresentatives : (p.fibreRepresentatives).ι.IsEquivalence
```

**`CategoryTheory.Functor.IsStack.fibreRepresentatives`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Stack/FibreRepresentatives.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Stack/FibreRepresentatives.lean#L145). The attribute's comment: “(a): the restriction of p to the cutdown satisfies the conditions of 026F”.

> **Stacks 03ZZ (a).** If `p : 𝒳 ⥤ 𝒮` satisfies the three conditions of Stacks 026F over the
> site `(𝒮, J)`, then so does its restriction to the cutdown; that is, the cutdown is a stack.

```lean
theorem IsStack.fibreRepresentatives (J : GrothendieckTopology 𝒮) (hp : p.IsStack J) :
    (p.restrict p.fibreRepresentatives).IsStack J
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 8.4, Tag 0268](https://stacks.math.columbia.edu/tag/0268)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
