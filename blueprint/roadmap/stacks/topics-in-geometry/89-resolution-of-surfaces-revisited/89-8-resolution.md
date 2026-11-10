---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsResolutionOfSingularities, AlgebraicGeometry.Space.HasResolutionByNormalizedBlowUps, AlgebraicGeometry.Space.tfae_resolution_of_dimension_eq_two
statement: formalized
proof: formalized
---

# 89.8 Resolution

Section 89.8 of the Stacks Project, [Tag 0BHV](https://stacks.math.columbia.edu/tag/0BHV). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0BHW, a definition

[Tag 0BHW](https://stacks.math.columbia.edu/tag/0BHW) in the Stacks Project.

**`AlgebraicGeometry.Space.IsResolutionOfSingularities`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ResolutionOfSingularities.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ResolutionOfSingularities.lean#L62).

> A *resolution of singularities* of a Noetherian integral algebraic space `Y` over `S` is a
> modification `f : X ⟶ Y` whose source `X` is regular.

```lean
abbrev IsResolutionOfSingularities {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (_hYnoeth : IsNoetherian B S hS hZ Y) (hYint : IsIntegralSpace B S hS Y)
    (_hdecentX : IsDecentSpace B S hS X)
    (_hdecentY : IsDecentSpace B S hS Y) (f : X ⟶ Y) : Prop
```

## Tag 0BHX, a definition

[Tag 0BHX](https://stacks.math.columbia.edu/tag/0BHX) in the Stacks Project.

**`AlgebraicGeometry.Space.HasResolutionByNormalizedBlowUps`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ResolutionByNormalizedBlowUps.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ResolutionByNormalizedBlowUps.lean#L133).

> **Stacks 0BHX.** A two-dimensional Noetherian integral algebraic space `Y` over `S` *has a
> resolution of singularities by normalized blowups* when the normalization of `Y` can be
> followed by finitely many normalizations of blowing ups at closed points, all of them proper
> over `Y`, so as to reach a regular algebraic space.

```lean
abbrev HasResolutionByNormalizedBlowUps (Y : AlgebraicSpaces B S hS)
    (_hYdim : dimension B S hS Y.obj Y.property = 2)
    (_hYnoeth : IsNoetherian B S hS hZ Y.obj)
    (_hYint : IsIntegralSpace B S hS Y.obj) : Prop
```

## Tag 0BHY, a theorem

[Tag 0BHY](https://stacks.math.columbia.edu/tag/0BHY) in the Stacks Project.

**`AlgebraicGeometry.Space.tfae_resolution_of_dimension_eq_two`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SurfaceResolutionTheorem.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SurfaceResolutionTheorem.lean#L64).

> **Stacks 0BHY.** For a two-dimensional integral Noetherian algebraic space `Y` over `S`, the
> following are equivalent: (1) there is an alteration `X ⟶ Y` with `X` regular; (2) `Y` has a
> resolution of singularities; (3) `Y` has a resolution of singularities by normalized blowups;
> (4) the normalization `Y^ν ⟶ Y` is finite, `Y^ν` has finitely many singular points, and the
> completion of the henselian local ring of `Y^ν` at each of them is normal.

```lean
theorem tfae_resolution_of_dimension_eq_two (hZ : B.Contains (⊤_ Scheme.{u}))
    (Y : AlgebraicSpaces B S hS) (hYdim : dimension B S hS Y.obj Y.property = 2)
    (hYnoeth : IsNoetherian B S hS hZ Y.obj) (hYint : IsIntegralSpace B S hS Y.obj) :
    List.TFAE
      [∃ (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (f : X ⟶ Y.obj), IsAlteration B S hS f ∧
          HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsRegular T),
        ∃ (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hX : IsAlgebraicSpace B S hS X)
          (hdecentX : IsDecentSpace B S hS X) (f : X ⟶ Y.obj),
          IsResolutionOfSingularities B S hS hZ hX Y.property hYnoeth hYint hdecentX
            (hYint.isDecentSpace B S hS Y.obj) f,
        HasResolutionByNormalizedBlowUps B S hS hZ Y hYdim hYnoeth hYint,
        ∀ D : NormalizationData B S hS Y.obj,
          D.IsSurfaceResolutionCriterion Y.property (hYint.isDecentSpace B S hS Y.obj)]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 89.8, Tag 0BHV](https://stacks.math.columbia.edu/tag/0BHV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
