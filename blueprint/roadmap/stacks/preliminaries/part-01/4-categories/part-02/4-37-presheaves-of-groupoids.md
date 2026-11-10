---
declaration: section
origin: cited
lean: CategoryTheory.isFiberedInGroupoids_presheafOfGroupoids, CategoryTheory.Functor.IsSplitFiberedInGroupoids, CategoryTheory.Functor.exists_isFibredEquivalenceOver_presheafOfGroupoids
statement: formalized
proof: formalized
---

# 4.37 Presheaves of groupoids

Section 4.37 of the Stacks Project, [Tag 0048](https://stacks.math.columbia.edu/tag/0048). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0049, an example

[Tag 0049](https://stacks.math.columbia.edu/tag/0049) in the Stacks Project.

**`CategoryTheory.isFiberedInGroupoids_presheafOfGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/OfPresheaf.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/OfPresheaf.lean#L100). References: SGA 4 VI (6.1.3), “strict, groupoid fibers”; SGA 7 VI (1.1(a)), “groupoid-valued F”.

> **Stacks 0049.**
> The category `𝒮_F` attached to a presheaf of groupoids `F : 𝒞ᵒᵖ ⥤ Grpd` is fibred in groupoids
> over `𝒞`: every morphism of `𝒞` lifts, and every fill-in problem has a unique solution.

```lean
theorem isFiberedInGroupoids_presheafOfGroupoids :
    (presheafOfGroupoids F).p.IsFiberedInGroupoids
```

## Tag 04TL, a definition

[Tag 04TL](https://stacks.math.columbia.edu/tag/04TL) in the Stacks Project.

**`CategoryTheory.Functor.IsSplitFiberedInGroupoids`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedInGroupoids/Split.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedInGroupoids/Split.lean#L89).

> **Stacks 04TL.**
> A *split category fibred in groupoids* over `𝒞` is a category fibred in groupoids `p : 𝒮 ⥤ 𝒞`
> that is isomorphic over `𝒞` to the category `𝒮_F` attached to some presheaf of groupoids
> `F : 𝒞ᵒᵖ ⥤ Grpd` (Stacks 0049). The source is explicit that isomorphism over `𝒞`, and not merely
> equivalence over `𝒞`, is meant.

```lean
def Functor.IsSplitFiberedInGroupoids (p : 𝒮 ⥤ 𝒞) : Prop
```

## Tag 02XY, a lemma

[Tag 02XY](https://stacks.math.columbia.edu/tag/02XY) in the Stacks Project.

**`CategoryTheory.Functor.exists_isFibredEquivalenceOver_presheafOfGroupoids`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/FiberedCategory/Strictification.lean, line 955](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/FiberedCategory/Strictification.lean#L955).

> **Stacks 02XY.**
> Every category fibred in groupoids `p : 𝒳 ⥤ 𝒞` is equivalent, in the 2-category of fibred
> categories over `𝒞`, to the category `𝒮_F` (Stacks 0049,
> `CategoryTheory.presheafOfGroupoids`) attached to a contravariant functor
> `F : 𝒞 ⥤ Groupoids`; in other words, every category fibred in groupoids is equivalent to a split
> one.

```lean
theorem exists_isFibredEquivalenceOver_presheafOfGroupoids (p : 𝒳 ⥤ 𝒞)
    (hp : p.IsFiberedInGroupoids) :
    ∃ (F : 𝒞ᵒᵖ ⥤ Grpd.{v₂, max u₁ u₂ v₁}) (Φ : 𝒳 ⥤ (presheafOfGroupoids F).obj),
      IsFibredEquivalenceOver p (presheafOfGroupoids F).p Φ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.37, Tag 0048](https://stacks.math.columbia.edu/tag/0048)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
