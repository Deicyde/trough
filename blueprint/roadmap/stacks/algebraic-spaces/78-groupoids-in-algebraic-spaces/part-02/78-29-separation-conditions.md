---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupoidInAlgebraicSpaces.isIso_arrowToArrowsOverObjects, AlgebraicGeometry.GroupoidInAlgebraicSpaces.isIso_arrowPairsToArrowsOverStabilizer, AlgebraicGeometry.GroupoidInAlgebraicSpaces.diagonal_comp_arrowPairsToArrowsOverStabilizer, AlgebraicGeometry.GroupoidInAlgebraicSpaces.isPullback_stabilizerUnit, AlgebraicGeometry.GroupoidInAlgebraicSpaces.isSeparated_stabilizer_iff_unit_closedImmersion, AlgebraicGeometry.GroupoidInAlgebraicSpaces.isSeparated_sourceTarget_iff_stabilizer, AlgebraicGeometry.GroupoidInAlgebraicSpaces.isLocallySeparated_stabilizer_iff_unit_immersion, AlgebraicGeometry.GroupoidInAlgebraicSpaces.isLocallySeparated_sourceTarget_iff_stabilizer
statement: formalized
proof: formalized
---

# 78.29 Separation conditions

Section 78.29 of the Stacks Project, [Tag 0453](https://stacks.math.columbia.edu/tag/0453). 2 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0454, a lemma

[Tag 0454](https://stacks.math.columbia.edu/tag/0454) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isIso_arrowToArrowsOverObjects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/Diagonal.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/Diagonal.lean#L183). The attribute's comment: “the upper horizontal morphism is an isomorphism”.

> **Stacks 0454.** The upper horizontal morphism `f ↦ (f, s f)` of the diagram is an
> isomorphism, its inverse being the first projection of `R ×_{s, U} U`.

```lean
theorem isIso_arrowToArrowsOverObjects (G : GroupoidInAlgebraicSpaces C S hS B) :
    IsIso (arrowToArrowsOverObjects G)
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isIso_arrowPairsToArrowsOverStabilizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/Diagonal.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/Diagonal.lean#L440). The attribute's comment: “the lower horizontal morphism is an isomorphism”.

> **Stacks 0454.** The lower horizontal morphism `(f, g) ↦ (f, f⁻¹ g)` of the diagram is an
> isomorphism, its inverse being `(f, h) ↦ (f, f h)`.

```lean
theorem isIso_arrowPairsToArrowsOverStabilizer
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    IsIso (arrowPairsToArrowsOverStabilizer G)
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.diagonal_comp_arrowPairsToArrowsOverStabilizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/Diagonal.lean, line 515](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/Diagonal.lean#L515). The attribute's comment: “commutativity of the left hand square”.

> **Stacks 0454.** The left hand square of the diagram commutes: the relative diagonal of
> `j = (t, s)`, followed by `(f, g) ↦ (f, f⁻¹ g)`, is `f ↦ (f, s f)` followed by the unit
> section of the stabilizer.

```lean
theorem diagonal_comp_arrowPairsToArrowsOverStabilizer
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    pullback.diagonal (sourceTarget G).hom ≫ arrowPairsToArrowsOverStabilizer G =
      arrowToArrowsOverObjects G ≫ arrowsOverObjectsUnit G
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isPullback_stabilizerUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/Diagonal.lean, line 541](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/Diagonal.lean#L541). The attribute's comment: “the right hand square is cartesian”.

> **Stacks 0454.** The right hand square of the diagram is cartesian: `R ×_{s, U} S` is the
> base change of the unit section `e : U ⟶ S` of the stabilizer along the projection
> `R ×_{s, U} S ⟶ S`, the base change being `R ×_{s, U} U`.

```lean
theorem isPullback_stabilizerUnit (G : GroupoidInAlgebraicSpaces C S hS B) :
    IsPullback (arrowsOverObjectsToObjects G) (arrowsOverObjectsUnit G)
      (η[stabilizer G]).left (arrowsOverStabilizerToStabilizer G)
```

## Tag 0455, a lemma

[Tag 0455](https://stacks.math.columbia.edu/tag/0455) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isSeparated_stabilizer_iff_unit_closedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/SeparationConditions.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/SeparationConditions.lean#L125). The attribute's comment: “separated\_equivalences”.

> **Stacks 0455.** The structure morphism of the stabilizer of a groupoid in algebraic spaces
> is separated exactly when the unit section of the stabilizer is a closed immersion.

```lean
theorem isSeparated_stabilizer_iff_unit_closedImmersion
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    Space.IsSeparated C S hS (stabilizer G).hom ↔
      Space.IsClosedImmersion C S hS (η[stabilizer G]).left
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isSeparated_sourceTarget_iff_stabilizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/SeparationConditions.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/SeparationConditions.lean#L135). The attribute's comment: “separated\_equivalences”.

> **Stacks 0455.** The source-target morphism of a groupoid in algebraic spaces is separated
> exactly when the structure morphism of its stabilizer is separated.

```lean
theorem isSeparated_sourceTarget_iff_stabilizer (G : GroupoidInAlgebraicSpaces C S hS B) :
    Space.IsSeparated C S hS (sourceTarget G).hom ↔
      Space.IsSeparated C S hS (stabilizer G).hom
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isLocallySeparated_stabilizer_iff_unit_immersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/SeparationConditions.lean, line 147](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/SeparationConditions.lean#L147). The attribute's comment: “locally\_separated\_equivalences”.

> **Stacks 0455.** The structure morphism of the stabilizer of a groupoid in algebraic spaces
> is locally separated exactly when the unit section of the stabilizer is an immersion.

```lean
theorem isLocallySeparated_stabilizer_iff_unit_immersion
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    Space.IsLocallySeparated C S hS (stabilizer G).hom ↔
      Space.IsImmersion C S hS (η[stabilizer G]).left
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isLocallySeparated_sourceTarget_iff_stabilizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/SeparationConditions.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/SeparationConditions.lean#L157). The attribute's comment: “locally\_separated\_equivalences”.

> **Stacks 0455.** The source-target morphism of a groupoid in algebraic spaces is locally
> separated exactly when the structure morphism of its stabilizer is locally separated.

```lean
theorem isLocallySeparated_sourceTarget_iff_stabilizer
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    Space.IsLocallySeparated C S hS (sourceTarget G).hom ↔
      Space.IsLocallySeparated C S hS (stabilizer G).hom
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isQuasiSeparated_stabilizer_iff_unit_quasiCompact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/SeparationConditions.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/SeparationConditions.lean#L171). The attribute's comment: “quasi\_separated\_equivalences”.

> **Stacks 0455.** The structure morphism of the stabilizer of a groupoid in algebraic spaces
> is quasi-separated exactly when the unit section of the stabilizer is quasi-compact.

```lean
theorem isQuasiSeparated_stabilizer_iff_unit_quasiCompact
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    Space.IsQuasiSeparated C S hS (stabilizer G).hom ↔
      Space.IsQuasiCompact C S hS (η[stabilizer G]).left
```

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.isQuasiSeparated_sourceTarget_iff_stabilizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/SeparationConditions.lean, line 181](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/Stabilizer/SeparationConditions.lean#L181). The attribute's comment: “quasi\_separated\_equivalences”.

> **Stacks 0455.** The source-target morphism of a groupoid in algebraic spaces is
> quasi-separated exactly when the structure morphism of its stabilizer is quasi-separated.

```lean
theorem isQuasiSeparated_sourceTarget_iff_stabilizer
    (G : GroupoidInAlgebraicSpaces C S hS B) :
    Space.IsQuasiSeparated C S hS (sourceTarget G).hom ↔
      Space.IsQuasiSeparated C S hS (stabilizer G).hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 78.29, Tag 0453](https://stacks.math.columbia.edu/tag/0453)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
