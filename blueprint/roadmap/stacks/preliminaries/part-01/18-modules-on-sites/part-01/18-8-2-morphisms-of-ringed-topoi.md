---
declaration: section
origin: cited
lean: Stacks.Sheaves.RingedToposModules.TwoMorphismOfRingedTopoi, AlgebraicGeometry.RingedToposHom.TwoMorphism
statement: formalized
proof: formalized
---

# 18.8 2-morphisms of ringed topoi

Section 18.8 of the Stacks Project, [Tag 04IB](https://stacks.math.columbia.edu/tag/04IB). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04IC, a definition

[Tag 04IC](https://stacks.math.columbia.edu/tag/04IC) in the Stacks Project.

**`Stacks.Sheaves.RingedToposModules.TwoMorphismOfRingedTopoi`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposTwoMorphism.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposTwoMorphism.lean#L80).

> A 2-morphism of ringed topoi: a natural transformation `f_* ⟶ g_*` of the underlying
> direct-image functors commuting with the two maps from the target structure sheaf.

```lean
structure TwoMorphismOfRingedTopoi (f g : RingedToposHom X Y)
```

**`AlgebraicGeometry.RingedToposHom.TwoMorphism`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposTwoMorphism.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposTwoMorphism.lean#L152). The attribute's comment: “2-morphisms of the canonical two-field morphisms of ringed topoi of 01D3 part (2), which are the ones that compose”.

> **Stacks 04IC for the canonical morphism of ringed topoi.** A 2-morphism between two
> morphisms of ringed topoi `f, g : (Sh(C), O_C) ⟶ (Sh(D), O_D)` in the sense of Stacks 01D3
> part (2): a transformation `t : f_* ⟶ g_*` of the underlying direct image functors — which is
> exactly a `TwoMorphismOfTopoi` of the underlying morphisms of topoi — whose value at the
> structure sheaf of the source carries the structure map of `f` to the structure map of `g`.

```lean
structure TwoMorphism (f g : RingedToposHom A B)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.8, Tag 04IB](https://stacks.math.columbia.edu/tag/04IB)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
