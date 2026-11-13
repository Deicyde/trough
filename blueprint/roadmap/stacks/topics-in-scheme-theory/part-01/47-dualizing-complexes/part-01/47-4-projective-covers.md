---
declaration: section
origin: cited
lean: Module.IsProjectiveCover, Module.isProjectiveCover_unique, Module.exists_projectiveCover_of_finite
statement: formalized
proof: formalized
---

# 47.4 Projective covers

Section 47.4 of the Stacks Project, [Tag 08XX](https://stacks.math.columbia.edu/tag/08XX). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08XY, a definition

[Tag 08XY](https://stacks.math.columbia.edu/tag/08XY) in the Stacks Project.

**`Module.IsProjectiveCover`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/ProjectiveCover.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/ProjectiveCover.lean#L63).

> A morphism is a projective cover if its source is projective and it is an essential
> epimorphism.

```lean
abbrev IsProjectiveCover {P M : C} (f : P ⟶ M) : Prop
```

## Tag 08XZ, a lemma

[Tag 08XZ](https://stacks.math.columbia.edu/tag/08XZ) in the Stacks Project.

**`Module.isProjectiveCover_unique`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/ProjectiveCover.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/ProjectiveCover.lean#L70).

> Two projective covers of the same object are isomorphic over that object.

```lean
lemma isProjectiveCover_unique {C : Type u} [Category.{v} C] [Abelian C] {P P' M : C}
    (f : P ⟶ M) (g : P' ⟶ M) (hf : IsProjectiveCover f) (hg : IsProjectiveCover g) :
    ∃ e : P ≅ P', e.hom ≫ g = f
```

## Tag 08Y0, a lemma

[Tag 08Y0](https://stacks.math.columbia.edu/tag/08Y0) in the Stacks Project.

**`Module.exists_projectiveCover_of_finite`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Module/ProjectiveCover.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/ProjectiveCover.lean#L132).

> A finite module over a local ring has a projective cover.

```lean
lemma exists_projectiveCover_of_finite
    (R : Type u) [CommRing R] [IsLocalRing R]
    (M : Type v) [AddCommGroup M] [Module R M] [Module.Finite R M] :
    ∃ (P : ModuleCat.{max u v} R)
      (f : P ⟶ ModuleCat.of R (Shrink.{max u v} M)),
      IsProjectiveCover f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 47.4, Tag 08XX](https://stacks.math.columbia.edu/tag/08XX)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
