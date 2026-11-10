---
declaration: section
origin: cited
lean: AlgebraicGeometry.Scheme.IsAmpleFamily, AlgebraicGeometry.Scheme.Modules.isAffineHom_diagonal_of_affine_nonvanishingOpen_cover
statement: formalized
proof: formalized
---

# 29.12 Families of ample invertible modules

Section 29.12 of the Stacks Project, [Tag 0FXQ](https://stacks.math.columbia.edu/tag/0FXQ). 2 tags here are carried by 1 declaration of the repository (in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FXR, a definition

[Tag 0FXR](https://stacks.math.columbia.edu/tag/0FXR) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.IsAmpleFamily`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyAmpleFamily.lean#L112), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyAmpleFamily.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Perfect/ResolutionPropertyAmpleFamily.lean#L163) (StacksFrontier). References: SGA 6 II (2.2.4).

## Tag 0FXS, a lemma

[Tag 0FXS](https://stacks.math.columbia.edu/tag/0FXS) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.isAffineHom_diagonal_of_affine_nonvanishingOpen_cover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineNonvanishing/AffineDiagonal.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineNonvanishing/AffineDiagonal.lean#L67).

> **Stacks Project, Tag 0FXS.** A cover by affine nonvanishing loci of sections of invertible
> modules implies that the diagonal is affine.

```lean
theorem isAffineHom_diagonal_of_affine_nonvanishingOpen_cover (X : Scheme.{u})
    (h : ∀ x : X, ∃ L : X.Modules,
      ∃ _ : IsInvertible X.presheaf (structureSheafRing X.toRingedSpace).property L,
      ∃ s : L.sections,
        x ∈ nonvanishingOpen (X := X.toRingedSpace) L s ∧
          IsAffineOpen (nonvanishingOpen (X := X.toRingedSpace) L s)) :
    IsAffineHom (pullback.diagonal (terminal.from X))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.12, Tag 0FXQ](https://stacks.math.columbia.edu/tag/0FXQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
