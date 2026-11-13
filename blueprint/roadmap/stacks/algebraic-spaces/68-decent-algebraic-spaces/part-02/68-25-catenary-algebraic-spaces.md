---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.IsCatenary, AlgebraicGeometry.Space.inducedDimensionValue_isDimensionFunction, AlgebraicGeometry.Space.isCatenary_of_isDecentSpace, AlgebraicGeometry.Space.IsUniversallyCatenary, AlgebraicGeometry.Space.isUniversallyCatenary_of_isLocallyOfFiniteType, AlgebraicGeometry.Space.exists_dimensionFunction_of_isFinite
statement: formalized
proof: formalized
---

# 68.25 Catenary algebraic spaces

Section 68.25 of the Stacks Project, [Tag 0ED3](https://stacks.math.columbia.edu/tag/0ED3). 6 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0ED4, a definition

[Tag 0ED4](https://stacks.math.columbia.edu/tag/0ED4) in the Stacks Project.

**`AlgebraicGeometry.Space.IsCatenary`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Catenary.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Catenary.lean#L112).

> **Stacks 0ED4.** An algebraic space is catenary when its space of points, with the
> topology of Tag 03BX, is a catenary topological space.

```lean
abbrev IsCatenary (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u)
    (_hX : IsAlgebraicSpace B S hS X) : Prop
```

## Tag 0ED5, a lemma

[Tag 0ED5](https://stacks.math.columbia.edu/tag/0ED5) in the Stacks Project.

**`AlgebraicGeometry.Space.inducedDimensionValue_isDimensionFunction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Catenary.lean, line 192](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Catenary.lean#L192). The attribute's comment: “with decency read as condition (alpha) of Stacks 03JX”. References: SGA 6 X (1.5), “(1.5.2) is a dim. fn”.

> **Stacks 0ED5.** Let `T` be an object of the big fppf site over `S` whose underlying
> scheme is locally Noetherian and universally catenary, and let `δ` be a dimension function on
> that scheme. Let `X` be an algebraic space over `S`, locally of finite type over `T`, above
> every point of which every étale chart by an affine scheme has a finite fibre. Then the
> function sending a point `x` of `X` to the value of `δ` at the image of `x` plus the relative
> transcendence degree of `x` over that image is a dimension function on the points of `X`.
>
> The finiteness hypothesis is condition `(α)` of Stacks 03JX, which is weaker than the
> condition (1) of Stacks 03JV through which Stacks 03I8 defines a decent algebraic space, and
> which is all that the argument uses. Taking for `T` the terminal object
> `Over.mk (𝟙 (B.obj hS))`, whose underlying scheme is `S`, gives the statement for the
> structure morphism of `X`.

```lean
theorem inducedDimensionValue_isDimensionFunction
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {T : BigFppfOver B S hS}
    [IsLocallyNoetherian ((BigFppfOver.toScheme B S hS).obj T)]
    (hcat : Scheme.IsUniversallyCatenary ((BigFppfOver.toScheme B S hS).obj T))
    (δ : TopologicalSpace.DimensionFunction ((BigFppfOver.toScheme B S hS).obj T))
    (hX : IsAlgebraicSpace B S hS X)
    (hfib : HasFiniteChartFibersAtEveryPoint B S hS X)
    (f : X ⟶ yoneda.obj T) (hf : IsLocallyOfFiniteType B S hS f) :
    ∃ d : TopologicalSpace.DimensionFunction (points B S hS X), ∀ x : points B S hS X,
      d x = inducedDimensionValue B S hS
        (fun y ↦ δ (pointsToScheme B S hS T y)) f x
```

## Tag 0ED6, a lemma

[Tag 0ED6](https://stacks.math.columbia.edu/tag/0ED6) in the Stacks Project.

**`AlgebraicGeometry.Space.isCatenary_of_isDecentSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/Catenary.lean, line 182](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Decent/Catenary.lean#L182).

> **Stacks 0ED6.** A decent algebraic space over `S` which is locally of finite type over an
> object of the site whose scheme is locally Noetherian and universally catenary is catenary.

```lean
theorem isCatenary_of_isDecentSpace {T : BigFppfOver B S hS}
    [IsLocallyNoetherian ((BigFppfOver.toScheme B S hS).obj T)]
    (hcat : Scheme.IsUniversallyCatenary ((BigFppfOver.toScheme B S hS).obj T))
    (hX : IsAlgebraicSpace B S hS X) (hdec : IsDecentSpace B S hS X)
    (f : X ⟶ yoneda.obj T) (hf : IsLocallyOfFiniteType B S hS f) :
    IsCatenary B S hS X hX
```

## Tag 0ED7, a definition

[Tag 0ED7](https://stacks.math.columbia.edu/tag/0ED7) in the Stacks Project.

**`AlgebraicGeometry.Space.IsUniversallyCatenary`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Catenary.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Catenary.lean#L119).

> **Stacks 0ED7.** An algebraic space is universally catenary when every decent algebraic
> space locally of finite type over it is catenary.

```lean
abbrev IsUniversallyCatenary (X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) : Prop
```

## Tag 0ED8, a lemma

[Tag 0ED8](https://stacks.math.columbia.edu/tag/0ED8) in the Stacks Project.

**`AlgebraicGeometry.Space.isUniversallyCatenary_of_isLocallyOfFiniteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Catenary.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Catenary.lean#L132).

> **Stacks 0ED8.** An algebraic space locally of finite type over a universally catenary
> algebraic space is universally catenary.
>
> Universal catenarity of the target already quantifies over all decent algebraic spaces
> locally of finite type over it, so the source needs no decency or local Noetherianity
> hypothesis: a decent space locally of finite type over the source is locally of finite type
> over the target by Stacks 03XG.

```lean
theorem isUniversallyCatenary_of_isLocallyOfFiniteType
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (hXcat : IsUniversallyCatenary B S hS X) (f : Y ⟶ X)
    (hf : IsLocallyOfFiniteType B S hS f) :
    IsUniversallyCatenary B S hS Y
```

## Tag 0ED9, a lemma

[Tag 0ED9](https://stacks.math.columbia.edu/tag/0ED9) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_dimensionFunction_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionFunction.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DimensionFunction.lean#L133). The attribute's comment: “decency and local Noetherianity not needed”.

> Let `q : Z ⟶ X` be a surjective finite morphism of algebraic spaces and let `δ` be a function
> on the points of `X`. If the pullback of `δ` along the map on points of `q` is a dimension
> function, then `δ` is a dimension function.

```lean
theorem exists_dimensionFunction_of_isFinite
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hZ : IsAlgebraicSpace B S hS Z) (q : Z ⟶ X) (hqfin : IsFinite B S hS q)
    (hqsurj : IsSurjective B S hS q) (δ : points B S hS X → ℤ)
    (hd : ∃ d : DimensionFunction (points B S hS Z), ∀ z : points B S hS Z,
      d z = δ (pointsMap B S hS Z q z)) :
    ∃ d : DimensionFunction (points B S hS X), ∀ x : points B S hS X, d x = δ x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 68.25, Tag 0ED3](https://stacks.math.columbia.edu/tag/0ED3)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
