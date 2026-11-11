---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isAlgebraicSpace_of_isRepresentableByAlgebraicSpaces_surjective_etale, AlgebraicGeometry.Space.isAlgebraicSpace_of_isRepresentableByAlgebraicSpaces_diag
statement: formalized
proof: formalized
---

# 80.6 Bootstrap

Section 80.6 of the Stacks Project, [Tag 03XV](https://stacks.math.columbia.edu/tag/03XV). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03Y3, a theorem

[Tag 03Y3](https://stacks.math.columbia.edu/tag/03Y3) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpace_of_isRepresentableByAlgebraicSpaces_surjective_etale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BootstrapEtaleSurjective.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BootstrapEtaleSurjective.lean#L252). The attribute's comment: “conditions (a) and (b)”.

> **Stacks 03Y3, conditions (a) and (b).** Let `F` be an fppf sheaf on the big fppf site of
> a scheme `S` admitting a morphism `f : X ⟶ F` from an algebraic space over `S` which is
> representable by algebraic spaces, surjective and étale. Then `F` is an algebraic space over `S`.
>
> The chart of `F` is the composite of a chart of `X` with `f`, which is representable by
> algebraic spaces by **Stacks 03Y1** and therefore by objects of the site; the diagonal is the
> only clause of **Stacks 025Y** needing effective fppf descent, which is supplied by
> `isEffectiveDescentAlongCoveringSieve_monomorphisms_inf_lft`.

```lean
theorem isAlgebraicSpace_of_isRepresentableByAlgebraicSpaces_surjective_etale
    {F X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : Presheaf.IsSheaf (BigFppfOver.topology B S hS) F)
    (hX : IsAlgebraicSpace B S hS X) (f : X ⟶ F)
    (hf : IsRepresentableByAlgebraicSpaces B S hS f)
    (hfSurj : HasProperty B S hS (surjectiveMorphismProperty B S hS) f hf)
    (hfEtale : HasProperty B S hS (etaleMorphisms B S hS) f hf) :
    IsAlgebraicSpace B S hS F
```

**`AlgebraicGeometry.Space.isAlgebraicSpace_of_isRepresentableByAlgebraicSpaces_diag`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/BootstrapEtaleSurjective.lean, line 356](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/BootstrapEtaleSurjective.lean#L356). The attribute's comment: “conditions (1), (2) and (3)”.

> **Stacks 03Y3, conditions (1), (2) and (3).** Let `F` be an fppf sheaf on the big fppf
> site of a scheme `S` whose diagonal is representable by algebraic spaces and which admits a
> surjective étale morphism from an algebraic space over `S`. Then `F` is an algebraic space over
> `S`.
>
> Condition (2) makes the morphism of condition (3) representable by algebraic spaces by **Stacks
> 03Y2**, so the hypotheses (a) and (b) hold and the previous theorem applies.

```lean
theorem isAlgebraicSpace_of_isRepresentableByAlgebraicSpaces_diag
    {F X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : Presheaf.IsSheaf (BigFppfOver.topology B S hS) F)
    (hdiag : IsRepresentableByAlgebraicSpaces B S hS (diag F))
    (hX : IsAlgebraicSpace B S hS X) (f : X ⟶ F)
    (hfSurj : HasProperty B S hS (surjectiveMorphismProperty B S hS) f
      (isRepresentableByAlgebraicSpaces_of_diagonal B S hS hdiag hX f))
    (hfEtale : HasProperty B S hS (etaleMorphisms B S hS) f
      (isRepresentableByAlgebraicSpaces_of_diagonal B S hS hdiag hX f)) :
    IsAlgebraicSpace B S hS F
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 80.6, Tag 03XV](https://stacks.math.columbia.edu/tag/03XV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
