---
declaration: section
origin: cited
lean: Stacks.Chow.isRelativeCycle_compFamily, Stacks.Chow.compFamily_familyAssociatedToSelf
statement: formalized
proof: formalized
---

# 62.15 Composition of relative cycles

Section 62.15 of the Stacks Project, [Tag 0H6Q](https://stacks.math.columbia.edu/tag/0H6Q). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0H6R, a lemma

[Tag 0H6R](https://stacks.math.columbia.edu/tag/0H6R) in the Stacks Project.

**`Stacks.Chow.isRelativeCycle_compFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/CompositionRelativeCyclesGeneral.lean, line 210](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/CompositionRelativeCyclesGeneral.lean#L210).

> **Stacks Project, Lemma 0H6R.** Let `X --f--> Y --g--> S` be morphisms of schemes, both
> locally of finite type, with `S` locally Noetherian, and let `r, e ≥ 0`. If `α` is a relative
> `r`-cycle on `X/Y` and `β` is a relative `e`-cycle on `Y/S`, then the composition `α ∘ β` is a
> relative `(r + e)`-cycle on `X/S`.
>
> `Y` is locally Noetherian because it is locally of finite type over the locally Noetherian
> scheme `S`, which is what makes the hypothesis on `α` meaningful.

```lean
theorem isRelativeCycle_compFamily {X Y S : Scheme.{u}} (f : X ⟶ Y) [LocallyOfFiniteType f]
    (g : Y ⟶ S) [LocallyOfFiniteType g] [IsLocallyNoetherian S] (r e : ℕ)
    (α : FamilyOfCycles f r) (β : FamilyOfCycles g e) :
    letI : IsLocallyNoetherian Y := LocallyOfFiniteType.isLocallyNoetherian g
    IsRelativeCycle f r α → IsRelativeCycle g e β →
      IsRelativeCycle (f ≫ g) (r + e) (compFamily f g r e α β)
```

## Tag 0H6S, a lemma

[Tag 0H6S](https://stacks.math.columbia.edu/tag/0H6S) in the Stacks Project.

**`Stacks.Chow.compFamily_familyAssociatedToSelf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedSubschemeComposition.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Chow/RelativeCycles/ClosedSubschemeComposition.lean#L240).

> **Stacks Project, Tag 0H6S.** Let `f : X ⟶ Y` and `g : Y ⟶ S` be morphisms of schemes, both
> locally of finite type and flat, of relative dimension `r` resp. `e`. Then the composition
> `[X/X/Y]_r ∘ [Y/Y/S]_e` of the families of cycles on fibres attached to the closed subschemes
> `X ⊆ X` and `Y ⊆ Y` (Example 0H4S) is the family `[X/X/S]_{r + e}`. The equality is one of
> families of cycles on fibres, so the local Noetherian hypothesis on `S`, needed only to speak of
> the group `z(X/S, r + e)` containing them, is not used.

```lean
theorem compFamily_familyAssociatedToSelf {X Y S : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] [Flat f] (g : Y ⟶ S) [LocallyOfFiniteType g] [Flat g] (r e : ℕ)
    (hf : AlgebraicGeometry.RelativeDimension f r)
    (hg : AlgebraicGeometry.RelativeDimension g e) :
    compFamily f g r e (familyAssociatedToClosedSubscheme f (𝟙 X) r)
        (familyAssociatedToClosedSubscheme g (𝟙 Y) e) =
      familyAssociatedToClosedSubscheme (f ≫ g) (𝟙 X) (r + e)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 62.15, Tag 0H6Q](https://stacks.math.columbia.edu/tag/0H6Q)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
