---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_iff_isStackInSetoids, AlgebraicGeometry.Stack.isDeligneMumfordStack_of_isRepresentableByAlgebraicSpace, AlgebraicGeometry.Stack.isDeligneMumfordStack_fibredCategory, CategoryTheory.RelativeInertia.π_isEquivalence_iff, AlgebraicGeometry.Stack.isDeligneMumfordStack_schemeFibredCategory, AlgebraicGeometry.Stack.isDeligneMumfordStack_and_isStackInSetoids_of_isRepresentableByAlgebraicSpace, AlgebraicGeometry.Stack.isDeligneMumfordStack_and_inertiaProjection_isEquivalence_of_isRepresentableByAlgebraicSpace, AlgebraicGeometry.Stack.isStackInSetoids_iff_inertiaProjection_isEquivalence_of_isDeligneMumfordStack
statement: formalized
proof: formalized
---

# 94.13 Algebraic stacks and algebraic spaces

Section 94.13 of the Stacks Project, [Tag 03YR](https://stacks.math.columbia.edu/tag/03YR). 4 tags here are carried by 13 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03YR, the section

[Tag 03YR](https://stacks.math.columbia.edu/tag/03YR) in the Stacks Project.

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_iff_isStackInSetoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStacksAndSpaces.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStacksAndSpaces.lean#L50). The attribute's comment: “the main result: an algebraic stack is an algebraic space exactly when its fibre categories are setoids”.

> An algebraic stack over `S` is representable by an algebraic space if and only if it is a
> stack in setoids, that is, objects of its fibre categories have no nontrivial automorphisms.

```lean
theorem isRepresentableByAlgebraicSpace_iff_isStackInSetoids
    (halg : IsAlgebraicStack.{u, w} B S hS 𝒳.val) :
    IsRepresentableByAlgebraicSpace B S hS 𝒳 ↔
      𝒳.val.p.IsStackInSetoids (BigFppfOver.topology B S hS)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Stack.isDeligneMumfordStack_of_isRepresentableByAlgebraicSpace`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RepresentableDeligneMumford.lean#L223), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStacksAndSpaces.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStacksAndSpaces.lean#L59) (StacksFrontier): “representable by an algebraic space implies Deligne-Mumford”.
- [`AlgebraicGeometry.Stack.isDeligneMumfordStack_fibredCategory`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicSpaceStackPresentation.lean#L313), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStacksAndSpaces.lean, line 61](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStacksAndSpaces.lean#L61) (StacksFrontier): “the category associated with an algebraic space is Deligne-Mumford”.
- [`CategoryTheory.RelativeInertia.π_isEquivalence_iff`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/Inertia.lean#L190), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStacksAndSpaces.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStacksAndSpaces.lean#L63) (StacksFrontier): “trivial inertia: the inertia criterion”.

## Tag 03YS, a lemma

[Tag 03YS](https://stacks.math.columbia.edu/tag/03YS) in the Stacks Project.

**`AlgebraicGeometry.Stack.isDeligneMumfordStack_fibredCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicSpaceStackPresentation.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicSpaceStackPresentation.lean#L313). The attribute's comment: “part (2)”.

> **Stacks 03YS, part (2).** The category of elements of an algebraic space `F` over `S`, read
> as a category fibred in groupoids over the big fppf site of `S`, is a Deligne-Mumford stack.
>
> It is an algebraic stack by `AlgebraicGeometry.Stack.isAlgebraicStack_fibredCategory`, and the
> same scheme atlas of `F` presents it étale-ly: the atlas of Stacks 025Y is surjective and étale,
> and `AlgebraicGeometry.Stack.prop_presentationBasedFunctor` carries both properties to the
> induced 1-morphism.

```lean
theorem isDeligneMumfordStack_fibredCategory (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (hF : IsAlgebraicSpace B S hS F) :
    IsDeligneMumfordStack.{u, w} B S hS (fibredCategory B S hS F).val
```

**`AlgebraicGeometry.Stack.isDeligneMumfordStack_of_isRepresentableByAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RepresentableDeligneMumford.lean, line 223](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RepresentableDeligneMumford.lean#L223). The attribute's comment: “part (1)”.

> **Stacks 03YS, part (1).** A category fibred in groupoids over the big fppf site of `S`
> which is representable by an algebraic space over `S` is a Deligne-Mumford stack.
>
> It is an algebraic stack by
> `AlgebraicGeometry.Stack.isAlgebraicStack_of_isRepresentableByAlgebraicSpace`, and the
> surjective étale scheme atlas of Stacks 025Y for the representing algebraic space presents it
> étale-ly, again by `AlgebraicGeometry.Stack.prop_transportedPresentation`.

```lean
theorem isDeligneMumfordStack_of_isRepresentableByAlgebraicSpace
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (h𝒳 : IsRepresentableByAlgebraicSpace B S hS 𝒳) :
    IsDeligneMumfordStack.{u, w} B S hS 𝒳.val
```

**`AlgebraicGeometry.Stack.isDeligneMumfordStack_schemeFibredCategory`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SchemeStack.lean, line 221](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SchemeStack.lean#L221). The attribute's comment: “part (3)”.

> **Stacks 03YS, part (3).** The big fppf site of a scheme `X` over `S`, read as a category
> fibred in groupoids over the big fppf site of `S`, is a Deligne-Mumford stack.
>
> It is an algebraic stack by
> `AlgebraicGeometry.Stack.isAlgebraicStack_schemeFibredCategory`, and the same identity
> 1-morphism presents it étale-ly, since the identity of `yoneda.obj X` is surjective and
> étale.

```lean
theorem isDeligneMumfordStack_schemeFibredCategory (X : BigFppfOver B S hS) :
    IsDeligneMumfordStack.{u, w} B S hS (schemeFibredCategory B S hS X).val
```

## Tag 045H, a lemma

[Tag 045H](https://stacks.math.columbia.edu/tag/045H) in the Stacks Project.

**`AlgebraicGeometry.Stack.isDeligneMumfordStack_and_isStackInSetoids_of_isRepresentableByAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordStackInSetoids.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordStackInSetoids.lean#L123). The attribute's comment: “the implication (3) ⟹ (1)”.

> **Stacks 045H, the implication (3) ⟹ (1).** A category fibred in groupoids over the big fppf
> site of `S` which is representable by an algebraic space over `S` is a Deligne-Mumford stack and
> a stack in setoids for the fppf topology.
>
> The first conjunct is Stacks 03YS part (1) and the second is the implication (3) ⟹ (1) of Stacks
> 04SZ; neither uses algebraicity as a hypothesis, so none is assumed.

```lean
theorem isDeligneMumfordStack_and_isStackInSetoids_of_isRepresentableByAlgebraicSpace
    (h : IsRepresentableByAlgebraicSpace B S hS 𝒳) :
    IsDeligneMumfordStack.{u, w} B S hS 𝒳.val ∧
      𝒳.val.p.IsStackInSetoids (BigFppfOver.topology B S hS)
```

**`AlgebraicGeometry.Stack.isDeligneMumfordStack_and_inertiaProjection_isEquivalence_of_isRepresentableByAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordStackInSetoids.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordStackInSetoids.lean#L137). The attribute's comment: “the implication (3) ⟹ (2)”.

> **Stacks 045H, the implication (3) ⟹ (2).** A category fibred in groupoids over the big fppf
> site of `S` which is representable by an algebraic space over `S` is a Deligne-Mumford stack
> whose canonical projection from the inertia category is an equivalence.
>
> This is the implication (3) ⟹ (1) with its second conjunct passed through Stacks 04ZM, which is
> the implication (3) ⟹ (2) of Stacks 04SZ.

```lean
theorem isDeligneMumfordStack_and_inertiaProjection_isEquivalence_of_isRepresentableByAlgebraicSpace
    (h : IsRepresentableByAlgebraicSpace B S hS 𝒳) :
    IsDeligneMumfordStack.{u, w} B S hS 𝒳.val ∧
      (RelativeInertia.π 𝒳.val.p :
        AbsoluteInertia 𝒳.val.p ⥤ 𝒳.val.obj).IsEquivalence
```

**`AlgebraicGeometry.Stack.isStackInSetoids_iff_inertiaProjection_isEquivalence_of_isDeligneMumfordStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordStackInSetoids.lean, line 154](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordStackInSetoids.lean#L154). The attribute's comment: “the equivalence of parts (1) and (2)”.

> **Stacks 045H, the equivalence of parts (1) and (2).** A Deligne-Mumford stack over the big
> fppf site of `S` is a stack in setoids if and only if the canonical projection from its inertia
> category is an equivalence.
>
> The Deligne-Mumford condition contains the algebraic-stack condition, which supplies the stack
> hypothesis of Stacks 04ZM through
> `AlgebraicGeometry.Stack.isStackInSetoids_iff_inertiaProjection_isEquivalence_of_isAlgebraicStack`;
> the Deligne-Mumford conjunct is then common to both sides.

```lean
theorem isStackInSetoids_iff_inertiaProjection_isEquivalence_of_isDeligneMumfordStack
    (h𝒳 : IsDeligneMumfordStack.{u, w} B S hS 𝒳.val) :
    𝒳.val.p.IsStackInSetoids (BigFppfOver.topology B S hS) ↔
      (RelativeInertia.π 𝒳.val.p :
        AbsoluteInertia 𝒳.val.p ⥤ 𝒳.val.obj).IsEquivalence
```

**`AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_of_isDeligneMumfordStack_isStackInSetoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordStackInSetoids.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordStackInSetoids.lean#L234). The attribute's comment: “the implication (1) ⟹ (3)”.

> **Stacks 045H, the implication (1) ⟹ (3).** A Deligne-Mumford stack over the big fppf site
> of `S` which is a stack in setoids for the fppf topology is representable by an algebraic space
> over `S`.
>
> The surjective étale presentation by a scheme that the Deligne-Mumford condition provides is the
> presentation the étale engine consumes, and the fibres of an algebraic stack are essentially
> small.

```lean
theorem isRepresentableByAlgebraicSpace_of_isDeligneMumfordStack_isStackInSetoids
    (h𝒳 : IsDeligneMumfordStack.{u, w} B S hS 𝒳.val)
    (hset : 𝒳.val.p.IsStackInSetoids (BigFppfOver.topology B S hS)) :
    IsRepresentableByAlgebraicSpace B S hS 𝒳
```

**`AlgebraicGeometry.Stack.isDeligneMumfordStack_isStackInSetoids_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordStackInSetoids.lean, line 255](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordStackInSetoids.lean#L255). The attribute's comment: “the equivalence of all three parts”.

> **Stacks 045H.** For a category fibred in groupoids over the big fppf site of `S` the
> following are equivalent: it is a Deligne-Mumford stack and a stack in setoids for the fppf
> topology; it is a Deligne-Mumford stack whose canonical projection from the inertia is an
> equivalence; it is representable by an algebraic space over `S`.
>
> No algebraicity hypothesis is assumed: algebraicity is part of the Deligne-Mumford condition of
> the first two parts, and the third implies it by Stacks 03YS part (1).

```lean
theorem isDeligneMumfordStack_isStackInSetoids_tfae :
    List.TFAE
      [IsDeligneMumfordStack.{u, w} B S hS 𝒳.val ∧
          𝒳.val.p.IsStackInSetoids (BigFppfOver.topology B S hS),
        IsDeligneMumfordStack.{u, w} B S hS 𝒳.val ∧
          (RelativeInertia.π 𝒳.val.p :
            AbsoluteInertia 𝒳.val.p ⥤ 𝒳.val.obj).IsEquivalence,
        IsRepresentableByAlgebraicSpace B S hS 𝒳]
```

Declarations registered for the tag:

- [`CategoryTheory.RelativeInertia.π_isEquivalence_iff`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/Inertia.lean#L190), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordStackInSetoids.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordStackInSetoids.lean#L108) (StacksFrontier): “parts (1) and (2), the general inertia criterion”.
- [`CategoryTheory.RelativeInertia.π_comp_neutralSection_eq_id`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/Inertia.lean#L205), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordStackInSetoids.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/DeligneMumfordStackInSetoids.lean#L110) (StacksFrontier): “inverse over the base in part (2)”.

## Tag 04SZ, a proposition

[Tag 04SZ](https://stacks.math.columbia.edu/tag/04SZ) in the Stacks Project.

**`AlgebraicGeometry.Stack.isStackInSetoids_iff_inertiaProjection_isEquivalence_of_isAlgebraicStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStackIsStack.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/AlgebraicStackIsStack.lean#L55). The attribute's comment: “parts (1) and (2)”.

> An algebraic stack over the big fppf site of `S` is a stack in setoids if and only if the
> canonical projection from its inertia category is an equivalence.

```lean
theorem isStackInSetoids_iff_inertiaProjection_isEquivalence_of_isAlgebraicStack
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val) :
    𝒳.val.p.IsStackInSetoids (BigFppfOver.topology B S hS) ↔
      (RelativeInertia.π 𝒳.val.p :
        AbsoluteInertia 𝒳.val.p ⥤ 𝒳.val.obj).IsEquivalence
```

**`AlgebraicGeometry.Stack.isStackInSetoids_of_isRepresentableByAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RepresentableStackInSetoids.lean, line 89](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RepresentableStackInSetoids.lean#L89). The attribute's comment: “the implication (3) ⟹ (1)”.

> **Stacks 04SZ**, the implication (3) ⟹ (1). A category fibred in groupoids over the big fppf
> site of `S` which is representable by an algebraic space over `S` is a stack in setoids for the
> fppf topology.
>
> The representing presheaf is an fppf sheaf, so the category of its elements is a stack in sets,
> and the equivalence over the site that representability provides carries that back to `𝒳`. No
> part of the algebraic-stack condition is used.

```lean
theorem isStackInSetoids_of_isRepresentableByAlgebraicSpace
    (h : IsRepresentableByAlgebraicSpace B S hS 𝒳) :
    𝒳.val.p.IsStackInSetoids (BigFppfOver.topology B S hS)
```

**`AlgebraicGeometry.Stack.isEquivalence_inertiaProjection_of_isRepresentableByAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/RepresentableStackInSetoids.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/RepresentableStackInSetoids.lean#L127). The attribute's comment: “the implication (3) ⟹ (2)”.

> **Stacks 04SZ**, the implication (3) ⟹ (2). For a category fibred in groupoids over the big
> fppf site of `S` which is representable by an algebraic space over `S`, the canonical projection
> from its inertia category is an equivalence.
>
> This is the implication (3) ⟹ (1) composed with Stacks 04ZM.

```lean
theorem isEquivalence_inertiaProjection_of_isRepresentableByAlgebraicSpace
    (h : IsRepresentableByAlgebraicSpace B S hS 𝒳) :
    (RelativeInertia.π 𝒳.val.p :
      AbsoluteInertia 𝒳.val.p ⥤ 𝒳.val.obj).IsEquivalence
```

**`AlgebraicGeometry.Stack.isStackInSetoids_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/StackInSetoidsRepresentableBySpace.lean, line 229](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/StackInSetoidsRepresentableBySpace.lean#L229).

> **Stacks 04SZ.** For an algebraic stack `𝒳` over the big fppf site of `S` the following are
> equivalent:
>
> 1. `𝒳` is a stack in setoids;
> 2. the canonical 1-morphism `I_𝒳 ⟶ 𝒳` from the inertia is an equivalence;
> 3. `𝒳` is representable by an algebraic space.
>
> The equivalence (1) ⟺ (2) is
> `AlgebraicGeometry.Stack.isStackInSetoids_iff_inertiaProjection_isEquivalence_of_isAlgebraicStack`,
> the implication (3) ⟹ (1) is
> `AlgebraicGeometry.Stack.isStackInSetoids_of_isRepresentableByAlgebraicSpace`, and the
> implication (1) ⟹ (3) is
> `AlgebraicGeometry.Stack.isRepresentableByAlgebraicSpace_of_isStackInSetoids`.

```lean
theorem isStackInSetoids_tfae (halg : IsAlgebraicStack.{u, w} B S hS 𝒳.val) :
    List.TFAE
      [𝒳.val.p.IsStackInSetoids (BigFppfOver.topology B S hS),
        (RelativeInertia.π 𝒳.val.p : AbsoluteInertia 𝒳.val.p ⥤ 𝒳.val.obj).IsEquivalence,
        IsRepresentableByAlgebraicSpace B S hS 𝒳]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 94.13, Tag 03YR](https://stacks.math.columbia.edu/tag/03YR)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
