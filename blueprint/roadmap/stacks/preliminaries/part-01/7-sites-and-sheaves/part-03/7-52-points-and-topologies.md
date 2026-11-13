---
declaration: section
origin: cited
lean: CategoryTheory.GrothendieckTopology.IsPointOfTopology
statement: formalized
proof: formalized
---

# 7.52 Points and topologies

Section 7.52 of the Stacks Project, [Tag 00ZS](https://stacks.math.columbia.edu/tag/00ZS). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 00ZT, a definition

[Tag 00ZT](https://stacks.math.columbia.edu/tag/00ZT) in the Stacks Project.

**`CategoryTheory.GrothendieckTopology.IsPointOfTopology`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/OfTopology.lean, line 98](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Point/OfTopology.lean#L98). The attribute's comment: “Stacks' definition of a point of a topology, on `u : C ⥤ Type w` with the stalk taken as the colimit over the category of elements of `u`; a Mathlib point gives one, see `GrothendieckTopology.Point.isPointOfTopology`.”.

> **Stacks 00ZT.** A *point of the topology* `J` on `C` is a functor `u : C ⥤ Type w` such
> that
>
> 1. for every covering sieve `S` on `U`, the map `S_p → (h_U)_p` induced on stalks by the
>    inclusion `S ⟶ h_U` is surjective;
> 2. the stalk functor `Sh(C) ⥤ Sets`, `F ↦ F_p`, on sheaves of sets `Type w`, is exact: it
>    commutes with finite limits and with finite colimits (Stacks 0034).
>
> The stalk is `Functor.pointStalk u`, the colimit over the neighbourhoods of `p = u`.

```lean
structure IsPointOfTopology (u : C ⥤ Type w) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 7.52, Tag 00ZS](https://stacks.math.columbia.edu/tag/00ZS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
