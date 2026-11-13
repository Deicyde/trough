---
declaration: section
origin: cited
lean: AlgebraicGeometry.SheafOfModules.OnSpace.IsInvertible, AlgebraicGeometry.SheafOfModules.OnSpace.IsTrivial, Module.Invertible, Module.IsTrivialInvertibleModule
statement: formalized
proof: formalized
---

# 111.40 Invertible sheaves

Section 111.40 of the Stacks Project, [Tag 02AC](https://stacks.math.columbia.edu/tag/02AC). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 02AD, a definition

[Tag 02AD](https://stacks.math.columbia.edu/tag/02AD) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.OnSpace.IsInvertible`**, a class in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/InvertibleSheaves.lean, line 58](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/InvertibleSheaves.lean#L58). The attribute's comment: “invertible sheaves”. References: EGA 0 (5.4.1), “invertible”.

> A sheaf of modules is invertible if every point has an open neighbourhood on which it is
> isomorphic to the structure sheaf.

```lean
class IsInvertible {X : TopCat.{u}}
    {R : Sheaf (Opens.grothendieckTopology X) RingCat.{v}}
    (L : _root_.SheafOfModules.{v} R) : Prop
```

**`AlgebraicGeometry.SheafOfModules.OnSpace.IsTrivial`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/Morphisms/InvertibleSheaves.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/Morphisms/InvertibleSheaves.lean#L68). The attribute's comment: “trivial sheaves”.

> A sheaf of modules is trivial if it is globally isomorphic to the structure sheaf.

```lean
abbrev IsTrivial {X : TopCat.{u}}
    {R : Sheaf (Opens.grothendieckTopology X) RingCat.{v}}
    (L : _root_.SheafOfModules.{v} R) : Prop
```

## Tag 02AG, a definition

[Tag 02AG](https://stacks.math.columbia.edu/tag/02AG) in the Stacks Project.

Declarations registered for the tag:

- [`Module.Invertible`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Invertible#doc) registered with `add_to_stacks` in [StacksFrontier/Exercises/InvertibleModule.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Exercises/InvertibleModule.lean#L24) (StacksFrontier): “invertible modules”.
- [`Module.IsTrivialInvertibleModule`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Module/Projective/Invertible.lean#L68), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Exercises/InvertibleModule.lean, line 25](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Exercises/InvertibleModule.lean#L25) (StacksFrontier): “trivial modules”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 111.40, Tag 02AC](https://stacks.math.columbia.edu/tag/02AC)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
