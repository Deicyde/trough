---
declaration: section
origin: cited
lean: CategoryTheory.RelativeInertia.isStack_of_isStack, CategoryTheory.RelativeInertia.isStack_and_fiber_isGroupoid_of_isStack, CategoryTheory.RelativeInertia.isStackInSetoids_of_isStackInSetoids, CategoryTheory.RelativeInertia.π_isEquivalence_iff, CategoryTheory.RelativeInertia.π_comp_neutralSection_eq_id
statement: formalized
proof: formalized
---

# 8.7 The inertia stack

Section 8.7 of the Stacks Project, [Tag 036X](https://stacks.math.columbia.edu/tag/036X). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 036Y, a lemma

[Tag 036Y](https://stacks.math.columbia.edu/tag/036Y) in the Stacks Project.

**`CategoryTheory.RelativeInertia.isStack_of_isStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/RelativeInertiaIsStack.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/RelativeInertiaIsStack.lean#L175). The attribute's comment: “(1)”.

> Let `(𝒞, J)` be a site, let `p : 𝒳 ⥤ 𝒞` and `p' : 𝒳' ⥤ 𝒞` be stacks and let `F : 𝒳 ⥤ 𝒳'` be
> a 1-morphism of stacks. Then the relative inertia `I_{𝒳/𝒳'}` (structure functor `π ⋙ p`) and the
> inertia `I_𝒳` (structure functor `toBase p`) are stacks over `𝒞`.

```lean
theorem isStack_of_isStack (hp : p.IsStack J) (hp' : p'.IsStack J)
    (hF : p.IsFibredOneMorphism p' F) :
    (RelativeInertia.π F ⋙ p).IsStack J ∧ (RelativeInertia.toBase p).IsStack J
```

**`CategoryTheory.RelativeInertia.isStack_and_fiber_isGroupoid_of_isStack`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/RelativeInertiaIsStack.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/RelativeInertiaIsStack.lean#L185). The attribute's comment: “(2), a stack in groupoids written out as a stack with groupoid fibres”.

> Let `(𝒞, J)` be a site, let `p : 𝒳 ⥤ 𝒞` and `p' : 𝒳' ⥤ 𝒞` be stacks in groupoids and let
> `F : 𝒳 ⥤ 𝒳'` be a 1-morphism of stacks. Then the relative inertia `I_{𝒳/𝒳'}` and the inertia
> `I_𝒳` are stacks in groupoids. A stack in groupoids is spelled out as a stack all of whose fibre
> categories are groupoids.

```lean
theorem isStack_and_fiber_isGroupoid_of_isStack (hp : p.IsStack J)
    (hgp : ∀ U, IsGroupoid (p.Fiber U)) (hp' : p'.IsStack J)
    (_hgp' : ∀ U, IsGroupoid (p'.Fiber U)) (hF : p.IsFibredOneMorphism p' F) :
    ((RelativeInertia.π F ⋙ p).IsStack J ∧
        ∀ U, IsGroupoid ((RelativeInertia.π F ⋙ p).Fiber U)) ∧
      ((RelativeInertia.toBase p).IsStack J ∧
        ∀ U, IsGroupoid ((RelativeInertia.toBase p).Fiber U))
```

**`CategoryTheory.RelativeInertia.isStackInSetoids_of_isStackInSetoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/RelativeInertiaIsStack.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/RelativeInertiaIsStack.lean#L199). The attribute's comment: “(3)”.

> Let `(𝒞, J)` be a site, let `p : 𝒳 ⥤ 𝒞` and `p' : 𝒳' ⥤ 𝒞` be stacks in setoids and let
> `F : 𝒳 ⥤ 𝒳'` be a 1-morphism of stacks. Then the relative inertia `I_{𝒳/𝒳'}` and the inertia
> `I_𝒳` are stacks in setoids.

```lean
theorem isStackInSetoids_of_isStackInSetoids (hp : p.IsStackInSetoids J)
    (hp' : p'.IsStackInSetoids J) (hF : p.IsFibredOneMorphism p' F) :
    (RelativeInertia.π F ⋙ p).IsStackInSetoids J ∧
      (RelativeInertia.toBase p).IsStackInSetoids J
```

## Tag 04ZM, a lemma

[Tag 04ZM](https://stacks.math.columbia.edu/tag/04ZM) in the Stacks Project.

**`CategoryTheory.RelativeInertia.π_isEquivalence_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/Inertia.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/Inertia.lean#L190).

> Let `(𝒞, J)` be a site and let `𝒮` be a stack in groupoids over `𝒞`, written out as a stack
> with groupoid fibres. The forgetful 1-morphism `π : I_𝒮 ⥤ 𝒮` of the absolute inertia is an
> equivalence if and only if `𝒮` is a stack in setoids.

```lean
theorem π_isEquivalence_iff (hp : p.IsStack J) (hg : ∀ U, IsGroupoid (p.Fiber U)) :
    (RelativeInertia.π p).IsEquivalence ↔ p.IsStackInSetoids J
```

**`CategoryTheory.RelativeInertia.π_comp_neutralSection_eq_id`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/Inertia.lean, line 205](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/Inertia.lean#L205).

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
