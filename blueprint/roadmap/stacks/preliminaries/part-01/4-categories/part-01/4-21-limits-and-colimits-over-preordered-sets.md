---
declaration: section
origin: cited
lean: Preorder, PartialOrder, IsDirectedOrder, Preorder.smallCategory, CategoryTheory.isDirected_antisymmetrization, CategoryTheory.pullbackSystemFunctor, CategoryTheory.systemEquivalence, CategoryTheory.inverseSystemEquivalence
statement: formalized
proof: formalized
---

# 4.21 Limits and colimits over preordered sets

Section 4.21 of the Stacks Project, [Tag 002Z](https://stacks.math.columbia.edu/tag/002Z). 6 tags here are carried by 12 declarations of the repository (1 in StacksCore and 11 in StacksFrontier) and 8 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 00D3, a definition

[Tag 00D3](https://stacks.math.columbia.edu/tag/00D3) in the Stacks Project.

Declarations registered for the tag:

- [`Preorder`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Preorder#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/DirectedLimits.lean, line 13](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/DirectedLimits.lean#L13) (StacksCore).
- [`PartialOrder`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PartialOrder#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/DirectedLimits.lean, line 14](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/DirectedLimits.lean#L14) (StacksCore).
- [`IsDirectedOrder`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsDirectedOrder#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/DirectedLimits.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/DirectedLimits.lean#L15) (StacksCore): “Directed sets. Note that unlike stacks, mathlib does not require directed sets to be nonempty.”.

## Tag 0030, a definition

[Tag 0030](https://stacks.math.columbia.edu/tag/0030) in the Stacks Project.

Declarations registered for the tag:

- [`Preorder.smallCategory`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Preorder.smallCategory#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/DirectedLimits.lean, line 18](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/DirectedLimits.lean#L18) (StacksCore): “The instance giving every preordered set the structure of a category. Inductive and inverse systems are just functors out of a poset resp. its opposite with respect to this.”. References: SGA 4 I (8.1.5).

## Tag 0CN1, a remark

[Tag 0CN1](https://stacks.math.columbia.edu/tag/0CN1) in the Stacks Project.

**An instance with no name** in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Category/Preorder.lean, line 17](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Category/Preorder.lean#L17). The attribute's comment: “Every preorder is equivalent to its partial order quotient. In particular, they are equivalent for the purpose of computing limits and colimits.”.

```lean
instance {α : Type*} [Preorder α] :
    (toAntisymmetrization_mono (α := α)).functor.IsEquivalence
```

**`CategoryTheory.isDirected_antisymmetrization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Order/PreorderVsPartialOrder.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Order/PreorderVsPartialOrder.lean#L49). The attribute's comment: “If `I` is directed, so is its partial order quotient.”.

> If `I` is directed, so is its antisymmetrization.

```lean
theorem isDirected_antisymmetrization [IsDirected I (· ≤ ·)] :
    IsDirected (Antisymmetrization I (· ≤ ·)) (· ≤ ·)
```

**`CategoryTheory.pullbackSystemFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Order/PreorderVsPartialOrder.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Order/PreorderVsPartialOrder.lean#L68). The attribute's comment: “The functor from systems over `Ī` to systems over `I`, `N ↦ (N_{π(i)})`.”.

> The pullback of systems over the antisymmetrization `Ī = Antisymmetrization I (· ≤ ·)` to
> systems over `I`, along the quotient functor induced by `toAntisymmetrization`.

```lean
def pullbackSystemFunctor :
    (Antisymmetrization I (· ≤ ·) ⥤ C) ⥤ (I ⥤ C)
```

**`CategoryTheory.systemEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Order/PreorderVsPartialOrder.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Order/PreorderVsPartialOrder.lean#L82). The attribute's comment: “The functor from systems over `Ī` to systems over `I` is an equivalence.”.

> The equivalence between systems over the antisymmetrization of `I` and systems over `I`:
> every system over `I` descends, uniquely up to canonical isomorphism, to a system over the
> antisymmetrization.

```lean
noncomputable def systemEquivalence :
    (Antisymmetrization I (· ≤ ·) ⥤ C) ≌ (I ⥤ C)
```

**`CategoryTheory.inverseSystemEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Order/PreorderVsPartialOrder.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Order/PreorderVsPartialOrder.lean#L94). The attribute's comment: “The analogous equivalence for inverse systems.”.

> The equivalence between inverse systems over the antisymmetrization of `I` and inverse
> systems over `I`.

```lean
noncomputable def inverseSystemEquivalence :
    ((Antisymmetrization I (· ≤ ·))ᵒᵖ ⥤ C) ≌ (Iᵒᵖ ⥤ C)
```

**`CategoryTheory.hasColimit_iff_hasColimit_of_systemEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Order/PreorderVsPartialOrder.lean, line 108](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Order/PreorderVsPartialOrder.lean#L108). The attribute's comment: “Compatibility of the equivalence with colimits of systems.”.

> A system `N` over `Ī` has a colimit if and only if its pullback to `I` has a colimit.

```lean
theorem hasColimit_iff_hasColimit_of_systemEquivalence
    (N : Antisymmetrization I (· ≤ ·) ⥤ C) :
    HasColimit N ↔ HasColimit ((pullbackSystemFunctor I C).obj N)
```

**`CategoryTheory.colimitPullbackSystemIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Order/PreorderVsPartialOrder.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Order/PreorderVsPartialOrder.lean#L115). The attribute's comment: “The colimits of related systems agree.”.

> The colimit of the pullback of a system `N` over `Ī` to `I` is the colimit of `N`.

```lean
noncomputable def colimitPullbackSystemIso (N : Antisymmetrization I (· ≤ ·) ⥤ C)
    [HasColimit N] :
    colimit ((toAntisymmetrization_mono (α := I)).functor ⋙ N) ≅ colimit N
```

**`CategoryTheory.hasLimit_iff_hasLimit_of_inverseSystemEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Order/PreorderVsPartialOrder.lean, line 123](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Order/PreorderVsPartialOrder.lean#L123). The attribute's comment: “Compatibility of the equivalence with limits of inverse systems.”. References: SGA 4 V (8.1.5), “special case”.

> An inverse system `N` over `Ī` has a limit if and only if its pullback to `I` has a limit.

```lean
theorem hasLimit_iff_hasLimit_of_inverseSystemEquivalence
    (N : (Antisymmetrization I (· ≤ ·))ᵒᵖ ⥤ C) :
    HasLimit N ↔ HasLimit ((inverseSystemEquivalence I C).functor.obj N)
```

**`CategoryTheory.limitInverseSystemIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Order/PreorderVsPartialOrder.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Order/PreorderVsPartialOrder.lean#L130). The attribute's comment: “The limits of related inverse systems agree.”.

> The limit of the pullback of an inverse system `N` over `Ī` to `I` is the limit of `N`.

```lean
noncomputable def limitInverseSystemIso (N : (Antisymmetrization I (· ≤ ·))ᵒᵖ ⥤ C)
    [HasLimit N] :
    limit ((toAntisymmetrization_mono (α := I)).functor.op ⋙ N) ≅ limit N
```

Declarations registered for the tag:

- [`Antisymmetrization`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Antisymmetrization#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/DirectedLimits.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/DirectedLimits.lean#L22) (StacksCore): “The partial order quotient of a preorder.”.
- [`preordToPartOrd`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=preordToPartOrd#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/DirectedLimits.lean, line 23](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/DirectedLimits.lean#L23) (StacksCore): “The partial order quotient construction as a functor.”.

## Tag 0031, a definition

[Tag 0031](https://stacks.math.columbia.edu/tag/0031) in the Stacks Project.

Declarations registered for the tag:

- [`IsDirectedOrder`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsDirectedOrder#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/DirectedLimits.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/DirectedLimits.lean#L25) (StacksCore): “A directed system is just a functor out of a nonempty directed order; this should not be bundled.”.

## Tag 09P8, a remark

[Tag 09P8](https://stacks.math.columbia.edu/tag/09P8) in the Stacks Project.

**`CategoryTheory.exists_isTop_and_isIso_colimit_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Filtered/FiniteDirected.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Filtered/FiniteDirected.lean#L79). The attribute's comment: “first half: a colimit over a finite directed set is trivial”.

> **Stacks 09P8**, first half. A finite directed set `I` has a greatest element `i∞`, and
> therefore every colimit over `I` is trivial: the structure map from the value at `i∞` to the
> colimit is an isomorphism.

```lean
theorem exists_isTop_and_isIso_colimit_ι {I : Type u} [Preorder I] [Finite I] [Nonempty I]
    [IsDirectedOrder I] {C : Type*} [Category C] (F : I ⥤ C) [HasColimit F] :
    ∃ i : I, IsTop i ∧ IsIso (colimit.ι F i)
```

**`CategoryTheory.Limits.SingleObj.isColimitRangeCocone`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Filtered/FiniteDirected.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Filtered/FiniteDirected.lean#L143). The attribute's comment: “second half: the colimit over the one-object category on an idempotent”.

> **Stacks 09P8**, second half. Let `e` be a left-absorbing element of a monoid `M`, so in
> particular an idempotent. The colimit of a diagram of sets indexed by the single-object category
> `SingleObj M` is the image of the idempotent `x ↦ e • x`, that is, of the map by which `e` acts.
> For the source's index category — one object with one non-trivial morphism `e` satisfying
> `e = e ∘ e` — take `M = WithZero Unit` and `e = 0`.

```lean
def isColimitRangeCocone (he : ∀ x : M, e * x = e) : IsColimit (rangeCocone F e he)
```

**`CategoryTheory.Limits.SingleObj.not_injective_ι_constDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Filtered/FiniteDirected.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Filtered/FiniteDirected.lean#L198). The attribute's comment: “second half: the colimit need not be trivial”.

> The colimit of `constDiagram X a` is the image of a constant map, a singleton, so its
> structure map is not injective as soon as `X` has an element other than `a`. Together with
> `instIsFilteredSingleObjOfMonoidWithZero` and the `FinCategory` instance on
> `SingleObj (WithZero Unit)`, this is the second assertion of Stacks 09P8: a colimit indexed by a
> *finite filtered* category need not be trivial.

```lean
theorem not_injective_ι_constDiagram {X : Type v} (a : X) (hX : ∃ x : X, x ≠ a) :
    ¬ Function.Injective
      ((rangeCocone (constDiagram X a) 0 fun x => zero_mul x).ι.app
        (star (WithZero Unit)))
```

## Tag 086J, a lemma

[Tag 086J](https://stacks.math.columbia.edu/tag/086J) in the Stacks Project.

Declarations registered for the tag:

- [`nonempty_sections_of_finite_cofiltered_system`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=nonempty_sections_of_finite_cofiltered_system#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/CofilteredSystem.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/CofilteredSystem.lean#L15) (StacksCore). References: SGA 4 I (App.Lemma3), “more general”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.21, Tag 002Z](https://stacks.math.columbia.edu/tag/002Z)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
