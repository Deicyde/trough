---
declaration: section
origin: cited
lean: CategoryTheory.Sheaf.isRightAdjoint_of_isCorepresentable_sections
statement: formalized
proof: formalized
---

# 7.24 Existence of lower shriek

Section 7.24 of the Stacks Project, [Tag 09YW](https://stacks.math.columbia.edu/tag/09YW). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09YX, a lemma

[Tag 09YX](https://stacks.math.columbia.edu/tag/09YX) in the Stacks Project.

**`CategoryTheory.Sheaf.isRightAdjoint_of_isCorepresentable_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Localization/ExistenceOfLowerShriek.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Localization/ExistenceOfLowerShriek.lean#L320). The attribute's comment: “Existence of lower shriek: the inverse image of a morphism of topoi has a left adjoint as soon as it is corepresentable on sections over a family of objects covering everything.”.

> **Stacks 09YX.** Let `C`, `D` be sites and let `finv : Sh(C) ⥤ Sh(D)` be a functor between
> their topoi of sheaves of sets — for instance the inverse image `f⁻¹` of a morphism of topoi
> `f : Sh(D) → Sh(C)`. Let `E` be a subset of the objects of `D` such that
>
> 1. for every `V ∈ E` there is a sheaf `G` on `C` with `finv F (V) = Mor_{Sh(C)}(G, F)`
>    functorially in `F`, i.e. the functor `F ↦ finv F (V)` is corepresentable, and
> 2. every object of `D` has a covering by objects of `E`, i.e. the inclusion of the full
>    subcategory on `E` is cover dense.
>
> Then `finv` has a left adjoint `f_!`.

```lean
public theorem isRightAdjoint_of_isCorepresentable_sections {C : Type u} [Category.{v} C]
    {D : Type u} [Category.{v} D] {J : GrothendieckTopology C} {K : GrothendieckTopology D}
    (finv : Sheaf J (Type max u v) ⥤ Sheaf K (Type max u v)) (E : ObjectProperty D)
    [E.ι.IsCoverDense K]
    (hE : ∀ V : D, E V → (finv ⋙ (sheafSections K (Type max u v)).obj (op V)).IsCorepresentable) :
    finv.IsRightAdjoint
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.24, Tag 09YW](https://stacks.math.columbia.edu/tag/09YW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
