---
declaration: section
origin: cited
lean: CategoryTheory.presheafOfCategories, CategoryTheory.PresheafOfCategories.objEquiv, CategoryTheory.PresheafOfCategories.homEquiv, CategoryTheory.PresheafOfCategories.comp_fiber, CategoryTheory.PresheafOfCategories.isFibered, CategoryTheory.Pseudofunctor.CoGrothendieck, CategoryTheory.Pseudofunctor.CoGrothendieck.forget, CategoryTheory.Pseudofunctor.CoGrothendieck.instIsFiberedForget
statement: formalized
proof: formalized
---

# 4.36 Presheaves of categories

Section 4.36 of the Stacks Project, [Tag 02XU](https://stacks.math.columbia.edu/tag/02XU). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier) and 4 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02XV, an example

[Tag 02XV](https://stacks.math.columbia.edu/tag/02XV) in the Stacks Project.

**`CategoryTheory.presheafOfCategories`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/OfPresheaf.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/OfPresheaf.lean#L87).

> **Stacks 02XV.**
> The category `𝒮_F` attached to a presheaf of categories `F : 𝒞ᵒᵖ ⥤ Cat`, together with its
> projection `p_F : 𝒮_F ⥤ 𝒞`, as an object of the 2-category of categories over `𝒞`.

```lean
abbrev presheafOfCategories (F : 𝒞ᵒᵖ ⥤ Cat.{v₂, u₂}) : BasedCategory 𝒞
```

**`CategoryTheory.PresheafOfCategories.objEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/OfPresheaf.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/OfPresheaf.lean#L108).

> **Stacks 02XV.**
> `Ob(𝒮_F) = {(U, x) | U ∈ Ob(𝒞), x ∈ Ob(F(U))}`.

```lean
def objEquiv : ∫ᶜ F.toPseudofunctor' ≃ Σ U : 𝒞, F.obj (op U)
```

**`CategoryTheory.PresheafOfCategories.homEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/OfPresheaf.lean, line 117](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/OfPresheaf.lean#L117).

> **Stacks 02XV.**
> `Mor_{𝒮_F}((V, y), (U, x))` is the disjoint union over `f : V ⟶ U` of `Mor_{F(V)}(y, f^* x)`.

```lean
def homEquiv (X Y : ∫ᶜ F.toPseudofunctor') :
    (X ⟶ Y) ≃ Σ f : X.base ⟶ Y.base, (X.fiber ⟶ (F.map f.op).toFunctor.obj Y.fiber)
```

**`CategoryTheory.PresheafOfCategories.comp_fiber`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/OfPresheaf.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/OfPresheaf.lean#L128).

> **Stacks 02XV.**
> The composition of `𝒮_F` is the source's: the composite of `ψ : z ⟶ g^* y` with `φ : y ⟶ f^* x` is
> `g^*(φ) ∘ ψ`, read as a morphism `z ⟶ (f ∘ g)^* x` through `pullback_comp_obj`.

```lean
lemma comp_fiber {X Y Z : ∫ᶜ F.toPseudofunctor'} (u : X ⟶ Y) (v : Y ⟶ Z) :
    (u ≫ v).fiber = u.fiber ≫ (F.map u.base.op).toFunctor.map v.fiber ≫
      eqToHom (pullback_comp_obj F u.base v.base Z.fiber)
```

**`CategoryTheory.PresheafOfCategories.isFibered`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/OfPresheaf.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/OfPresheaf.lean#L142). References: SGA 4 VI (6.1.3), “strict functor case”.

> **Stacks 02XV.**
> The projection `p_F : 𝒮_F ⥤ 𝒞` is a fibred category.
>
> This bridge is load-bearing: instance resolution does not see Mathlib's
> `CoGrothendieck.instIsFiberedForget` through `BasedCategory.ofFunctor`'s projection, so
> `infer_instance` fails on this goal without it.

```lean
instance isFibered : (presheafOfCategories F).p.IsFibered
```

Declarations registered for the tag:

- [`CategoryTheory.Pseudofunctor.CoGrothendieck`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Pseudofunctor.CoGrothendieck#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FiberedCategory/OfPresheaf.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/OfPresheaf.lean#L70) (StacksFrontier): “the category `𝒮_F`”. References: SGA 4 XVII (2.2.12).
- [`CategoryTheory.Pseudofunctor.CoGrothendieck.forget`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Pseudofunctor.CoGrothendieck.forget#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FiberedCategory/OfPresheaf.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/OfPresheaf.lean#L72) (StacksFrontier): “the projection `p_F`”. References: SGA 4 I (8.3.2), “more general”.
- [`CategoryTheory.Pseudofunctor.CoGrothendieck.instIsFiberedForget`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Pseudofunctor.CoGrothendieck.instIsFiberedForget#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FiberedCategory/OfPresheaf.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/OfPresheaf.lean#L74) (StacksFrontier): “`p_F` is a fibred category”. References: SGA 4 VI (6.1.3), “Fiberedness clause”; SGA 4 VI (7.1.4), “partial”; SGA 4 XVII (2.2.12), “partial”.
- [`CategoryTheory.Pseudofunctor.CoGrothendieck.isStronglyCartesian_homCartesianLift`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Pseudofunctor.CoGrothendieck.isStronglyCartesian_homCartesianLift#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/FiberedCategory/OfPresheaf.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/OfPresheaf.lean#L80) (StacksFrontier): “the strongly cartesian lift of `f`”.

## Tag 02XW, a definition

[Tag 02XW](https://stacks.math.columbia.edu/tag/02XW) in the Stacks Project.

**`CategoryTheory.Functor.IsSplitFibered`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/Split.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/Split.lean#L43).

> **Stacks 02XW.**
> A *split fibred category* over `𝒞` is a fibred category `p : 𝒮 ⥤ 𝒞` that is isomorphic over `𝒞`
> to the fibred category `𝒮_F` attached to some presheaf of categories `F : 𝒞ᵒᵖ ⥤ Cat`
> (Stacks 02XV). The source is explicit that isomorphism over `𝒞`, and not merely equivalence over
> `𝒞`, is meant.

```lean
def Functor.IsSplitFibered (p : 𝒮 ⥤ 𝒞) : Prop
```

## Tag 02XX, a lemma

[Tag 02XX](https://stacks.math.columbia.edu/tag/02XX) in the Stacks Project.

**`CategoryTheory.Functor.isSplitFibered_iff_exists_isSplitCleavage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/Splitting.lean, line 847](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/Splitting.lean#L847).

> **Stacks 02XX**, with the source's condition on a choice of pullbacks replaced by
> `CategoryTheory.Functor.ChoiceOfPullbacks.IsSplitCleavage`: a fibred category is split
> (Stacks 02XW) if and only if some choice of pullbacks (Stacks 02XN) has its two canonical
> comparisons of Stacks 02XN equal to identities, i.e. has *chosen cartesian lifts* strictly
> compatible with identities and composition.
>
> The source states the condition on the pullback *functors*, as `(f ∘ g)^* = g^* ∘ f^*`, and that
> biconditional is false: see the module docstring, and the two counterexamples
> `CategoryTheory.SplittingCounterexample.compatibleWithComp_not_isSplitting` and
> `CategoryTheory.SplitCleavageCounterexample.isSplitting_not_isSplitFibered` in
> `StacksFrontier/CategoryTheory/FiberedCategory/SplittingCounterexample.lean`.

```lean
theorem Functor.isSplitFibered_iff_exists_isSplitCleavage {p : 𝒳 ⥤ 𝒮} :
    p.IsSplitFibered ↔ ∃ c : p.ChoiceOfPullbacks, c.IsSplitCleavage
```

## Tag 004A, a lemma

[Tag 004A](https://stacks.math.columbia.edu/tag/004A) in the Stacks Project.

**`CategoryTheory.Functor.exists_isFibredEquivalenceOver_presheafOfCategories`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/Strictification.lean, line 922](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/FiberedCategory/Strictification.lean#L922).

> **Stacks 004A.**
> Every fibred category `p : 𝒳 ⥤ 𝒞` is equivalent, in the 2-category of fibred categories over `𝒞`,
> to the category `𝒮_F` (Stacks 02XV, `CategoryTheory.presheafOfCategories`) attached to a
> contravariant functor `F : 𝒞 ⥤ Cat`; in other words, every fibred category is equivalent to a
> split one.

```lean
theorem exists_isFibredEquivalenceOver_presheafOfCategories :
    ∃ (F : 𝒞ᵒᵖ ⥤ Cat.{v₂, max u₁ u₂ v₁}) (Φ : 𝒳 ⥤ (presheafOfCategories F).obj),
      IsFibredEquivalenceOver p (presheafOfCategories F).p Φ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.36, Tag 02XU](https://stacks.math.columbia.edu/tag/02XU)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
