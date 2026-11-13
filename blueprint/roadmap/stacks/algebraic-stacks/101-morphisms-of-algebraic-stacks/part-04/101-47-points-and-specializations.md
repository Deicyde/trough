---
declaration: section
origin: cited
lean: AlgebraicGeometry.Stack.exists_specializes_spacePointMap_eq
statement: formalized
proof: formalized
---

# 101.47 Points and specializations

Section 101.47 of the Stacks Project, [Tag 0GVY](https://stacks.math.columbia.edu/tag/0GVY). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GVZ, a lemma

[Tag 0GVZ](https://stacks.math.columbia.edu/tag/0GVZ) in the Stacks Project.

**`AlgebraicGeometry.Stack.exists_specializes_spacePointMap_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Stacks/SpecializationSmoothChart.lean, line 542](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Stacks/SpecializationSmoothChart.lean#L542).

> **Stacks 0GVZ.** Let `𝒳` be an algebraic stack over `S`, let `f : U ⟶ 𝒳` be a smooth
> 1-morphism from an algebraic space `U` over `S`, let `x' ⤳ x` be a specialization of points of
> `|𝒳|` and let `u` be a point of `|U|` with `f(u) = x`. If the point `x'` admits a quasi-compact
> field-valued representative — one of the equivalent conditions of **Stacks 0DTK** for the pair
> `(𝒳, x')` — then there is a specialization `u' ⤳ u` in `|U|` with `f(u') = x'`.
>
> Smoothness of `f` enters twice. It makes `|U| ⟶ |𝒳|` an open map (**Stacks 06R7**), which is
> what puts `u` in the closure of the fibre of `|U| ⟶ |𝒳|` over `x'`: an open neighbourhood of `u`
> missing that fibre would have open image containing `x` but not `x'`. And it is what makes the
> base change of the 1-morphism `Spec k ⟶ 𝒳` of the representative an algebraic space over the
> affine chart, so that the fibre is the image, on points, of an affine scheme quasi-compact over
> the chart; **Stacks 02JQ** then produces the specialization inside that fibre.

```lean
theorem exists_specializes_spacePointMap_eq
    (𝒳 : CatFiberedInGroupoids.{u, u, u + 1, u + 1} (BigFppfOver B S hS))
    (h𝒳 : IsAlgebraicStack.{u, w} B S hS 𝒳.val)
    (U : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hU : IsAlgebraicSpace B S hS U)
    (f : fibredCategory B S hS U ⟶ 𝒳)
    (hf : HasPropertyOnSomeSmoothDiagram B S hS
      (fun _ _ h => Space.IsSmooth B S hS h) f)
    {x x' : points B S hS 𝒳.val 𝒳.property} (hxx' : x' ⤳ x)
    (hx' : ∃ p : FieldValuedPoint B S hS 𝒳.val,
      pointClass B S hS 𝒳.val 𝒳.property p = x' ∧
        IsQuasiCompactFieldValuedPoint B S hS 𝒳 p)
    (u : Space.points B S hS U) (hu : spacePointMap B S hS U 𝒳 f.hom u = x) :
    ∃ u' : Space.points B S hS U, u' ⤳ u ∧
      spacePointMap B S hS U 𝒳 f.hom u' = x'
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 101.47, Tag 0GVY](https://stacks.math.columbia.edu/tag/0GVY)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
