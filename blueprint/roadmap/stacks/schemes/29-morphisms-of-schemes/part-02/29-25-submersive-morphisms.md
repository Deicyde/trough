---
declaration: section
origin: cited
lean: AlgebraicGeometry.Submersive, AlgebraicGeometry.UniversallySubmersive, AlgebraicGeometry.Submersive.comp, AlgebraicGeometry.UniversallySubmersive.comp
statement: formalized
proof: formalized
---

# 29.25 Submersive morphisms

Section 29.25 of the Stacks Project, [Tag 040G](https://stacks.math.columbia.edu/tag/040G). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 040H, a definition

[Tag 040H](https://stacks.math.columbia.edu/tag/040H) in the Stacks Project.

**`AlgebraicGeometry.Submersive`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Submersive.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Submersive.lean#L63). The attribute's comment: “part (1): submersive”. References: EGA IV (15.7.8); SGA 1 IX (2.1), “submersive”.

> **Stacks 040H, part (1).** A morphism of schemes is *submersive* when the continuous map of
> underlying topological spaces is a quotient map, that is submersive in the sense of Stacks 0406,
> part (2). This is unrelated to the notion of a submersion of differentiable manifolds.

```lean
def Submersive : MorphismProperty Scheme.{u}
```

**`AlgebraicGeometry.UniversallySubmersive`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Submersive.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Submersive.lean#L71). The attribute's comment: “part (2): universally submersive”. References: EGA IV (15.7.8); SGA 1 IX (2.1), “univ. submersive”.

> **Stacks 040H, part (2).** A morphism of schemes `f : X ⟶ Y` is *universally submersive*
> when the base change `Y' ×_Y X ⟶ Y'` of `f` along every morphism of schemes `Y' ⟶ Y` is
> submersive.

```lean
def UniversallySubmersive : MorphismProperty Scheme.{u}
```

## Tag 0CET, a lemma

[Tag 0CET](https://stacks.math.columbia.edu/tag/0CET) in the Stacks Project.

**`AlgebraicGeometry.Submersive.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Submersive.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Submersive.lean#L95). The attribute's comment: “submersive”.

> **Stacks 0CET, submersive morphisms.** The composition of a pair of submersive morphisms of
> schemes is submersive.

```lean
theorem Submersive.comp {X Y Z : Scheme.{u}} {f : X ⟶ Y} {g : Y ⟶ Z}
    (hf : Submersive f) (hg : Submersive g) : Submersive (f ≫ g)
```

**`AlgebraicGeometry.UniversallySubmersive.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Submersive.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Submersive.lean#L108). The attribute's comment: “universally submersive”.

> **Stacks 0CET, universally submersive morphisms.** The composition of a pair of universally
> submersive morphisms of schemes is universally submersive.

```lean
theorem UniversallySubmersive.comp {X Y Z : Scheme.{u}} {f : X ⟶ Y} {g : Y ⟶ Z}
    (hf : UniversallySubmersive f) (hg : UniversallySubmersive g) :
    UniversallySubmersive (f ≫ g)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.25, Tag 040G](https://stacks.math.columbia.edu/tag/040G)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
