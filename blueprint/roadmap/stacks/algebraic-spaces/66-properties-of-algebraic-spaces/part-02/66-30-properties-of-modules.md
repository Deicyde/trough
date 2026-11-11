---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isFinitePresentationOnSite_iff_isFinitePresentationOnCharts, AlgebraicGeometry.Space.isFiniteTypeOnSite_of_epi
statement: formalized
proof: formalized
---

# 66.30 Properties of modules

Section 66.30 of the Stacks Project, [Tag 05VR](https://stacks.math.columbia.edu/tag/05VR). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05VR, the section

[Tag 05VR](https://stacks.math.columbia.edu/tag/05VR) in the Stacks Project.

**`AlgebraicGeometry.Space.isFinitePresentationOnSite_iff_isFinitePresentationOnCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationOnSiteAffineCharts.lean, line 269](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationOnSiteAffineCharts.lean#L269). The attribute's comment: “of finite presentation: for a quasi-coherent module on an algebraic space, finite presentation on the small etale site is finite presentation of its restriction to every etale scheme chart, read on the Zariski site of the chart (items (2) and (4) of the section)”.

> **For a quasi-coherent module, finite presentation on the small étale site is finite
> presentation on the étale scheme charts.**  This is the property "of finite presentation" of the
> section of Stacks 05VR on properties of modules on an algebraic space: it may be read on the
> small étale site, or on every étale scheme chart, where for a quasi-coherent module it is the
> property of the corresponding module on the scheme (the scheme case being Stacks 05VG).

```lean
theorem isFinitePresentationOnSite_iff_isFinitePresentationOnCharts
    (M : Modules.{u, u} B S hS X.1 X.2) (hqc : M.IsQuasicoherentOnSite) :
    SheafOfModules.IsFinitePresentationOnSite M ↔ IsFinitePresentationOnCharts B S hS X.2 M
```

**`AlgebraicGeometry.Space.isFiniteTypeOnSite_of_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ModuleFiniteTypeQuotient.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ModuleFiniteTypeQuotient.lean#L94). The attribute's comment: “finite type, quotients”.

> **Properties of Spaces, Section 66.30, the finite type clause for a quotient.**  A quotient
> of an `𝒪_X`-module of finite type on the small étale site of an algebraic space `X` is again of
> finite type.
>
> On each member of a covering witnessing finite type for the source, the restricted epimorphism
> composes with the finite coproduct presenting the source to present the target.

```lean
theorem isFiniteTypeOnSite_of_epi {M N : Modules.{u, u} B S hS X hX} (p : M ⟶ N) [Epi p]
    (hM : SheafOfModules.IsFiniteTypeOnSite M) :
    SheafOfModules.IsFiniteTypeOnSite N
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.30, Tag 05VR](https://stacks.math.columbia.edu/tag/05VR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
