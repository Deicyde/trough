---
declaration: section
origin: cited
lean: IsFinitelyPresentable, CategoryTheory.isFinitelyPresentable_iff_preservesFilteredColimits, CategoryTheory.ObjectProperty.exists_extension_of_preservesFilteredColimits, CategoryTheory.ObjectProperty.existsUnique_iso_of_preservesFilteredColimits
statement: formalized
proof: formalized
---

# 4.26 Categorically compact objects

Section 4.26 of the Stacks Project, [Tag 0FWW](https://stacks.math.columbia.edu/tag/0FWW). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0FWX, a definition

[Tag 0FWX](https://stacks.math.columbia.edu/tag/0FWX) in the Stacks Project.

Declarations registered for the tag:

- [`IsFinitelyPresentable`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsFinitelyPresentable#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/IsFinitelyPresentable.lean, line 15](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/CategoryTheory/IsFinitelyPresentable.lean#L15) (StacksCore).
- [`CategoryTheory.isFinitelyPresentable_iff_preservesFilteredColimits`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.isFinitelyPresentable_iff_preservesFilteredColimits#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Stacks0FWX.lean, line 10](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Stacks0FWX.lean#L10) (StacksFrontier). References: SGA 4 VI (1.24.2); SGA 4 VI (4.10).

## Tag 0FWY, a lemma

[Tag 0FWY](https://stacks.math.columbia.edu/tag/0FWY) in the Stacks Project.

**`CategoryTheory.ObjectProperty.exists_extension_of_preservesFilteredColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/KanExtension/Extend.lean, line 60](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/KanExtension/Extend.lean#L60). References: SGA 4 I (8.7.2), “existence of f̄”; SGA 4 I (8.7.3), “ess. surj. of (8.7.3.1)”.

> **Stacks 0FWY** (existence).
> Let `C` and `D` have `w`-filtered colimits, let `P` be a property of objects of `C` cutting out
> an essentially `w`-small full subcategory of categorically compact objects (Stacks 0FWX), and
> assume every object of `C` is a `w`-filtered colimit of objects satisfying `P`. Then every
> functor `F'` out of that subcategory extends to a functor `C ⥤ D` commuting with filtered
> colimits.

```lean
theorem exists_extension_of_preservesFilteredColimits
    [HasFilteredColimitsOfSize.{w, w} C] [HasFilteredColimitsOfSize.{w, w} D]
    [EssentiallySmall.{w} P.FullSubcategory]
    (hP : P ≤ isFinitelyPresentable.{w} C) (hgen : ∀ X : C, P.ind.{w} X)
    (F' : P.FullSubcategory ⥤ D) :
    ∃ F : C ⥤ D, PreservesFilteredColimitsOfSize.{w, w} F ∧ Nonempty (P.ι ⋙ F ≅ F')
```

**`CategoryTheory.ObjectProperty.existsUnique_iso_of_preservesFilteredColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/KanExtension/Extend.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/KanExtension/Extend.lean#L80). References: SGA 4 I (8.7.2), “uniqueness of f̄”; SGA 4 I (8.7.3), “uniqueness of extension”.

> **Stacks 0FWY** (uniqueness).
> Under the hypotheses of `exists_extension_of_preservesFilteredColimits`, an extension of `F'`
> commuting with filtered colimits is unique up to a unique natural isomorphism compatible with
> the identifications of the restrictions with `F'`.

```lean
theorem existsUnique_iso_of_preservesFilteredColimits
    [HasFilteredColimitsOfSize.{w, w} C] [EssentiallySmall.{w} P.FullSubcategory]
    (hP : P ≤ isFinitelyPresentable.{w} C) (hgen : ∀ X : C, P.ind.{w} X)
    {F' : P.FullSubcategory ⥤ D} (F₁ F₂ : C ⥤ D)
    [PreservesFilteredColimitsOfSize.{w, w} F₁] [PreservesFilteredColimitsOfSize.{w, w} F₂]
    (e₁ : P.ι ⋙ F₁ ≅ F') (e₂ : P.ι ⋙ F₂ ≅ F') :
    ∃! φ : F₁ ≅ F₂, Functor.whiskerLeft P.ι φ.hom = (e₁ ≪≫ e₂.symm).hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.26, Tag 0FWW](https://stacks.math.columbia.edu/tag/0FWW)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
