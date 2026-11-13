---
declaration: section
origin: cited
lean: CategoryTheory.Functor.IsCofiltered, CategoryTheory.Functor.isCofiltered_id_iff
statement: formalized
proof: formalized
---

# 4.20 Cofiltered limits

Section 4.20 of the Stacks Project, [Tag 04AY](https://stacks.math.columbia.edu/tag/04AY). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04AZ, a definition

[Tag 04AZ](https://stacks.math.columbia.edu/tag/04AZ) in the Stacks Project.

**`CategoryTheory.Functor.IsCofiltered`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Filtered/Cofiltered.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Filtered/Cofiltered.lean#L41). References: SGA 4 I (2.7), “cofiltered”.

> **Stacks 04AZ.** A diagram `M : I ⥤ C` is *cofiltered* (or *codirected*) if
> `I` is nonempty, every pair of objects of `I` admits morphisms from a common
> object, and every pair of parallel morphisms of `I` is equalized, after applying
> `M`, by precomposition with a further morphism.

```lean
structure Functor.IsCofiltered {I : Type u₁} [Category.{v₁} I] {C : Type u₂} [Category.{v₂} C]
    (M : I ⥤ C) : Prop
```

**`CategoryTheory.Functor.isCofiltered_id_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Filtered/Cofiltered.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Filtered/Cofiltered.lean#L59).

> **Stacks 04AZ.** An index category `I` is cofiltered in the sense of Stacks —
> the identity diagram `𝟭 I` is a cofiltered diagram — exactly when it is
> cofiltered in the sense of Mathlib's `CategoryTheory.IsCofiltered`. Since
> `(𝟭 I).map f = f`, condition (3) for `𝟭 I` reads `c ≫ a = c ≫ b` in `I`, so both
> directions are a repackaging of the same data.

```lean
theorem Functor.isCofiltered_id_iff (I : Type u₁) [Category.{v₁} I] :
    (𝟭 I).IsCofiltered ↔ _root_.CategoryTheory.IsCofiltered I
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.20, Tag 04AY](https://stacks.math.columbia.edu/tag/04AY)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
