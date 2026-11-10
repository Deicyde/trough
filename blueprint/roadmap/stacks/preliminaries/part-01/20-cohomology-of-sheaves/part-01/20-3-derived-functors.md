---
declaration: section
origin: cited
lean: CategoryTheory.Functor.rightDerivedPlus, Stacks.RingedSpaceCohomology.derivedSections, AlgebraicGeometry.RingedSpace.derivedPushforwardPlus
statement: formalized
proof: formalized
---

# 20.3 Derived functors

Section 20.3 of the Stacks Project, [Tag 0716](https://stacks.math.columbia.edu/tag/0716). 3 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05U4, an equation

[Tag 05U4](https://stacks.math.columbia.edu/tag/05U4) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.rightDerivedPlus`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/RightDerivedFunctorInjective/Exactness.lean#L379), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Cohomology/DerivedFunctors/HigherRightDerivedFunctors.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/DerivedFunctors/HigherRightDerivedFunctors.lean#L38) (StacksFrontier).

## Tag 0717, an equation

[Tag 0717](https://stacks.math.columbia.edu/tag/0717) in the Stacks Project.

**`Stacks.RingedSpaceCohomology.derivedSections`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/RingedSpaceCohomology/DerivedSections.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/RingedSpaceCohomology/DerivedSections.lean#L55). The attribute's comment: “RΓ(U, -) : D⁺(X) → D⁺(𝒪\_X(U))”.

> **The derived sections functor over an open of a ringed space**,
> `RΓ(U, -) : D⁺(O) ⥤ D⁺(O(U))`: the right derived functor, on bounded below derived categories,
> of the sections functor `Γ(U, -) = SheafOfModules.evaluation O (op U)` from sheaves of
> `O`-modules to modules over the ring `O(U)` of sections of `O` over `U`. It is computed by
> injective resolutions, sheaves of `O`-modules having enough injectives.

```lean
abbrev derivedSections (U : Opens X) [HasDerivedCategory (SheafOfModules.{u} O)]
    [HasDerivedCategory (ModuleCat.{u} (O.obj.obj (op U)))] :
    DerivedCategory.Plus (SheafOfModules.{u} O) ⥤
      DerivedCategory.Plus (ModuleCat.{u} (O.obj.obj (op U)))
```

## Tag 0718, an equation

[Tag 0718](https://stacks.math.columbia.edu/tag/0718) in the Stacks Project.

**`AlgebraicGeometry.RingedSpace.derivedPushforwardPlus`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/RingedSpaceCohomology/DerivedPushforward.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/RingedSpaceCohomology/DerivedPushforward.lean#L59). The attribute's comment: “derived pushforward `Rf_* : D⁺(X) → D⁺(Y)`”.

> The derived pushforward `Rf_* : D⁺(𝒪_X) ⥤ D⁺(𝒪_Y)` along a morphism of ringed spaces
> `f : X ⟶ Y`: the right derived functor of the pushforward `f_* : Mod(𝒪_X) ⥤ Mod(𝒪_Y)` on
> bounded below derived categories, which exists because `Mod(𝒪_X)` has enough injectives.

```lean
abbrev derivedPushforwardPlus :
    DerivedCategory.Plus (SheafOfModules.{u} (structureSheafRing X)) ⥤
      DerivedCategory.Plus (SheafOfModules.{u} (structureSheafRing Y))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 20.3, Tag 0716](https://stacks.math.columbia.edu/tag/0716)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
