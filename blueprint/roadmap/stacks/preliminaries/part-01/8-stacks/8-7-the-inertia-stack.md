---
declaration: section
origin: cited
lean: CategoryTheory.RelativeInertia.isStack, CategoryTheory.RelativeInertia.isStack_and_fiber_isGroupoid, CategoryTheory.RelativeInertia.isStackInSetoids, CategoryTheory.RelativeInertia.π_isEquivalence_iff, CategoryTheory.RelativeInertia.π_comp_neutralSection_eq_id
statement: formalized
proof: formalized
---

# 8.7 The inertia stack

Section 8.7 of the Stacks Project, [Tag 036X](https://stacks.math.columbia.edu/tag/036X). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 036Y, a lemma

[Tag 036Y](https://stacks.math.columbia.edu/tag/036Y) in the Stacks Project.

**`CategoryTheory.RelativeInertia.isStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/Inertia.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/Inertia.lean#L140). The attribute's comment: “(1)”.

> The relative inertia `I_{𝒮/𝒮'}` of a 1-morphism `F` of stacks over the site `(𝒞, J)`, with its
> structure functor `π ⋙ p`, is a stack over `𝒞`; taking `F = p` and `p' = 𝟭 𝒞`, so is the absolute
> inertia `I_𝒮`.
>
> Only the fibredness half of the conclusion is proved, from Stacks 034H (2); the descent of
> morphisms and the effectivity of descent for the inertia are the hypotheses `hmor` and
> `heff`.

```lean
theorem isStack (hp : p.IsStack J) (_hp' : p'.IsStack J) (hF : p.IsFibredOneMorphism p' F)
    (hmor : haveI : (RelativeInertia.π F ⋙ p).IsFibered :=
        RelativeInertia.isFibered F p p' hp.isFibered hF
      ∀ (U : 𝒞) (x y : (RelativeInertia.π F ⋙ p).Fiber U),
        Functor.IsMorSheaf (RelativeInertia.π F ⋙ p) J U x y)
    (heff : haveI : (RelativeInertia.π F ⋙ p).IsFibered :=
        RelativeInertia.isFibered F p p' hp.isFibered hF
      Functor.HasEffectiveDescent (RelativeInertia.π F ⋙ p) J) :
    Functor.IsStack (RelativeInertia.π F ⋙ p) J
```

**`CategoryTheory.RelativeInertia.isStack_and_fiber_isGroupoid`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/Inertia.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/Inertia.lean#L160). The attribute's comment: “(2)”.

> If `𝒮` and `𝒮'` are stacks in groupoids over the site `(𝒞, J)`, then so is the relative inertia
> `I_{𝒮/𝒮'}`; taking `F = p` and `p' = 𝟭 𝒞`, so is the absolute inertia `I_𝒮`.
>
> Being a stack in groupoids is written out as being a stack with groupoid fibres; the stack
> condition on the inertia is the hypothesis `hst`, which is part (1), and what is proved here is
> the remaining content, that the fibres of the inertia are groupoids.

```lean
theorem isStack_and_fiber_isGroupoid (_hp : p.IsStack J) (hgp : ∀ U, IsGroupoid (p.Fiber U))
    (_hp' : p'.IsStack J) (_hgp' : ∀ U, IsGroupoid (p'.Fiber U))
    (hst : Functor.IsStack (RelativeInertia.π F ⋙ p) J) :
    Functor.IsStack (RelativeInertia.π F ⋙ p) J ∧
      ∀ U, IsGroupoid ((RelativeInertia.π F ⋙ p).Fiber U)
```

**`CategoryTheory.RelativeInertia.isStackInSetoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/Inertia.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/Inertia.lean#L173). The attribute's comment: “(3)”.

> If `𝒮` and `𝒮'` are stacks in setoids over the site `(𝒞, J)`, then so is the relative inertia
> `I_{𝒮/𝒮'}`; taking `F = p` and `p' = 𝟭 𝒞`, so is the absolute inertia `I_𝒮`.
>
> The stack condition on the inertia is the hypothesis `hst`, which is part (1); what is proved
> here is the remaining content, that the fibres of the inertia are setoids.

```lean
theorem isStackInSetoids (hp : p.IsStackInSetoids J) (_hp' : p'.IsStackInSetoids J)
    (hst : Functor.IsStack (RelativeInertia.π F ⋙ p) J) :
    (RelativeInertia.π F ⋙ p).IsStackInSetoids J
```

## Tag 04ZM, a lemma

[Tag 04ZM](https://stacks.math.columbia.edu/tag/04ZM) in the Stacks Project.

**`CategoryTheory.RelativeInertia.π_isEquivalence_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/Inertia.lean, line 189](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/Inertia.lean#L189).

> Let `(𝒞, J)` be a site and let `𝒮` be a stack in groupoids over `𝒞`, written out as a stack
> with groupoid fibres. The forgetful 1-morphism `π : I_𝒮 ⥤ 𝒮` of the absolute inertia is an
> equivalence if and only if `𝒮` is a stack in setoids.

```lean
theorem π_isEquivalence_iff (hp : p.IsStack J) (hg : ∀ U, IsGroupoid (p.Fiber U)) :
    (RelativeInertia.π p).IsEquivalence ↔ p.IsStackInSetoids J
```

**`CategoryTheory.RelativeInertia.π_comp_neutralSection_eq_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/Inertia.lean, line 204](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/Inertia.lean#L204).

> For a stack in setoids the neutral section `x ↦ (x, 𝟙)` is a strict two-sided inverse of `π`,
> so `π` is an isomorphism of categories over `𝒞` and in particular an equivalence in the 2-category
> of stacks over `𝒞`, not merely an equivalence of categories.

```lean
theorem π_comp_neutralSection_eq_id (h : p.IsStackInSetoids J) :
    RelativeInertia.π p ⋙ RelativeInertia.neutralSection p = 𝟭 (AbsoluteInertia p)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 8.7, Tag 036X](https://stacks.math.columbia.edu/tag/036X)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
