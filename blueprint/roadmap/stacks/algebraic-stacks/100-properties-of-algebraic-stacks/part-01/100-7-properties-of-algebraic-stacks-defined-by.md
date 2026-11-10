---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.exists_scheme_atlas_iff_forall_scheme, AlgebraicGeometry.Stack.exists_scheme_atlas_iff_scheme, AlgebraicGeometry.Stack.exists_scheme_atlas_iff_exists_space_atlas, AlgebraicGeometry.Stack.exists_space_atlas_iff_forall_space, AlgebraicGeometry.Stack.exists_space_atlas_iff_space, AlgebraicGeometry.Stack.HasPropertyOnSomeSchemeAtlas, AlgebraicGeometry.Stack.tfae_germProperty_at_point, AlgebraicGeometry.Stack.germPropertyAtSomeSpaceChart_algebraicSpaceStack_iff
statement: formalized
proof: formalized
---

# 100.7 Properties of algebraic stacks defined by properties of schemes

Section 100.7 of the Stacks Project, [Tag 04YE](https://stacks.math.columbia.edu/tag/04YE). 4 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04YF, a lemma

[Tag 04YF](https://stacks.math.columbia.edu/tag/04YF) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_scheme_atlas_iff_forall_scheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalPropertyAtlasScheme.lean, line 163](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalPropertyAtlasScheme.lean#L163). The attribute's comment: “scheme criteria”.

> **Stacks 04YF, the two scheme criteria.** For a property `P` of schemes local in the smooth
> topology, an algebraic stack over `S` admits some smooth surjective 1-morphism from the algebraic
> stack of a scheme over `S` with `P` exactly when every smooth 1-morphism from the algebraic stack
> of a scheme over `S` has source with `P`.

```lean
theorem exists_scheme_atlas_iff_forall_scheme
    (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    HasPropertyOnSomeSchemeAtlas B S hS P 𝒳 ↔
      HasPropertyOnEverySchemeChart B S hS P 𝒳
```

**`AlgebraicGeometry.Stack.exists_scheme_atlas_iff_scheme`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalPropertyAtlasScheme.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalPropertyAtlasScheme.lean#L205). The attribute's comment: “scheme case”.

> **Stacks 04YF, the scheme case.** On the algebraic stack of a scheme `U` over `S`, the
> existential scheme criterion for a smooth-local property `P` is `P` of the scheme underlying `U`.
>
> One direction is smooth surjective descent along the presentation; the other tests the universal
> criterion, which the identity presentation satisfies, at an arbitrary chart.

```lean
theorem exists_scheme_atlas_iff_scheme
    (U : BigFppfOver B S hS) :
    HasPropertyOnSomeSchemeAtlas B S hS P (schemeStack.{u, w} B S hS U) ↔
      P ((BigFppfOver.toScheme B S hS).obj U)
```

**`AlgebraicGeometry.Stack.exists_scheme_atlas_iff_exists_space_atlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalPropertyAtlasSpace.lean, line 373](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalPropertyAtlasSpace.lean#L373). The attribute's comment: “scheme and space atlases”.

> An algebraic stack over `S` admits a smooth surjective 1-morphism from the algebraic stack of
> a scheme over `S` with `P` exactly when it admits one from the algebraic stack of an algebraic
> space over `S` with the étale-local property `P` of Stacks 03E6.

```lean
theorem exists_scheme_atlas_iff_exists_space_atlas
    (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    HasPropertyOnSomeSchemeAtlas B S hS P 𝒳 ↔
      HasPropertyOnSomeSpaceAtlas B S hS P 𝒳
```

**`AlgebraicGeometry.Stack.exists_space_atlas_iff_forall_space`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalPropertyAtlasSpace.lean, line 396](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalPropertyAtlasSpace.lean#L396). The attribute's comment: “space criteria”.

> An algebraic stack over `S` admits a smooth surjective 1-morphism from the algebraic stack of
> an algebraic space over `S` with the étale-local property `P` exactly when every smooth
> 1-morphism from the algebraic stack of an algebraic space over `S` has source with that
> property.

```lean
theorem exists_space_atlas_iff_forall_space
    (𝒳 : AlgebraicStacks.{u, w} B S hS) :
    HasPropertyOnSomeSpaceAtlas B S hS P 𝒳 ↔
      HasPropertyOnEverySpaceChart B S hS P 𝒳
```

**`AlgebraicGeometry.Stack.exists_space_atlas_iff_space`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalPropertyAtlasSpace.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalPropertyAtlasSpace.lean#L421). The attribute's comment: “algebraic-space case”.

> On the algebraic stack of an algebraic space over `S`, the existential algebraic-space
> criterion for a smooth-local property `P` is the étale-local property `P` of Stacks 03E6 of that
> algebraic space.

```lean
theorem exists_space_atlas_iff_space
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F) :
    HasPropertyOnSomeSpaceAtlas B S hS P (algebraicSpaceStack.{u, w} B S hS F hF) ↔
      Space.HasEtaleLocalProperty B S hS F P
```

## Tag 04YG, a definition

[Tag 04YG](https://stacks.math.columbia.edu/tag/04YG) in the Stacks Project.

**`AlgebraicGeometry.Stack.HasPropertyOnSomeSchemeAtlas`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalPropertyAtlas.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalPropertyAtlas.lean#L96).

> **The existential scheme criterion of Stacks 04YF**, and **Stacks 04YG**: the algebraic
> stack `𝒳` *has property* `P` when it admits a smooth surjective 1-morphism from the algebraic
> stack of a scheme over `S` whose underlying scheme has `P`.
>
> Stacks 04YG defines "`𝒳` has `P`" by any of the four equivalent conditions of Stacks 04YF; this
> is the first of them, and the comparisons of Stacks 04YF identify it with the other three.

```lean
abbrev HasPropertyOnSomeSchemeAtlas (𝒳 : AlgebraicStacks.{u, w} B S hS) : Prop
```

## Tag 04YI, a lemma

[Tag 04YI](https://stacks.math.columbia.edu/tag/04YI) in the Stacks Project.

**`AlgebraicGeometry.Stack.tfae_germProperty_at_point`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalGermAtPoint.lean, line 476](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalGermAtPoint.lean#L476).

> **Stacks 04YI.** Let `𝒳` be an algebraic stack over `S`, let `x` be a point of `𝒳`, and let
> `P` be a smooth-local property of germs of schemes (**Stacks 04N1**). Then the four conditions
> comparing `P` against the smooth charts of `𝒳` through `x` — every scheme chart, some scheme
> chart, every algebraic space chart, some algebraic space chart — are equivalent.

```lean
theorem tfae_germProperty_at_point (hP : GermOfScheme.IsSmoothLocal P) :
    [GermPropertyAtEverySchemeChart B S hS 𝒳 x P,
      GermPropertyAtSomeSchemeChart B S hS 𝒳 x P,
      GermPropertyAtEverySpaceChart B S hS 𝒳 x P,
      GermPropertyAtSomeSpaceChart B S hS 𝒳 x P].TFAE
```

**`AlgebraicGeometry.Stack.germPropertyAtSomeSpaceChart_algebraicSpaceStack_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalGermAtPoint.lean, line 527](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalGermAtPoint.lean#L527). The attribute's comment: “algebraic space case”.

> **Stacks 04YI, the algebraic space addendum.** On the algebraic stack of an algebraic space
> `F` over `S` the four conditions say that `F` has property `P` at the corresponding point of `F`,
> in the sense of **Stacks 04RC**. The chart realizing the existential condition is the identity.

```lean
theorem germPropertyAtSomeSpaceChart_algebraicSpaceStack_iff
    {F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hF : IsAlgebraicSpace B S hS F)
    (z : Space.points B S hS F) (P : GermOfScheme.{u} → Prop)
    (hP : GermOfScheme.IsSmoothLocal P) :
    GermPropertyAtSomeSpaceChart B S hS (algebraicSpaceStack.{u, w} B S hS F hF)
        (spacePointMap B S hS F (fibredCategory B S hS F)
          (BasedFunctor.id (fibredCategory B S hS F).val) z) P ↔
      Space.HasPropertyAtPoint B S hS F z P
```

**`AlgebraicGeometry.Stack.germPropertyAtSomeSpaceChart_yoneda_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalGermAtPoint.lean, line 548](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalGermAtPoint.lean#L548). The attribute's comment: “representable case”.

> **Stacks 04YI, the representable addendum.** On the algebraic stack of a scheme `U` over `S`
> the four conditions say that the germ of `U` at the corresponding scheme point has `P`.

```lean
theorem germPropertyAtSomeSpaceChart_yoneda_iff (U : BigFppfOver B S hS)
    (p : Space.FieldValuedPoint B S hS (yoneda.obj U)) (P : GermOfScheme.{u} → Prop)
    (hP : GermOfScheme.IsSmoothLocal P) :
    GermPropertyAtSomeSpaceChart B S hS
        (algebraicSpaceStack.{u, w} B S hS (yoneda.obj U)
          (isAlgebraicSpace_yoneda B S hS U))
        (spacePointMap B S hS (yoneda.obj U) (fibredCategory B S hS (yoneda.obj U))
          (BasedFunctor.id (fibredCategory B S hS (yoneda.obj U)).val)
          (p.class B S hS (yoneda.obj U))) P ↔
      P ⟨(BigFppfOver.toScheme B S hS).obj U, Space.schemePoint B S hS U p⟩
```

## Tag 04YJ, a definition

[Tag 04YJ](https://stacks.math.columbia.edu/tag/04YJ) in the Stacks Project.

**`AlgebraicGeometry.Stack.HasPropertyAtPoint`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalGermAtPoint.lean, line 578](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Stacks/SmoothLocalGermAtPoint.lean#L578).

> **Stacks 04YJ.** Let `P` be a property of germs of schemes which is smooth local (**Stacks
> 04N1**), let `𝒳` be an algebraic stack over `S` and let `x` be a point of `𝒳` (**Stacks 04XG**).
> Then `𝒳` *has property* `P` *at* `x` when some smooth chart of `𝒳` by an algebraic space has
> property `P` at some point of it lying over `x`, in the sense of **Stacks 04RC**.
>
> The source defines this by any of the four equivalent conditions of **Stacks 04YI**; this is the
> fourth of them, and `AlgebraicGeometry.Stack.tfae_germProperty_at_point` identifies it with the
> other three for a smooth-local `P`, which is what makes the choice immaterial. As for **Stacks
> 04RC**, stating this one condition needs neither that hypothesis nor surjectivity of the chart.
> Its specializations are the two addenda above:
> `AlgebraicGeometry.Stack.germPropertyAtSomeSpaceChart_algebraicSpaceStack_iff` on the algebraic
> stack of an algebraic space and
> `AlgebraicGeometry.Stack.germPropertyAtSomeSpaceChart_yoneda_iff` on that of a scheme.

```lean
abbrev HasPropertyAtPoint : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 100.7, Tag 04YE](https://stacks.math.columbia.edu/tag/04YE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
