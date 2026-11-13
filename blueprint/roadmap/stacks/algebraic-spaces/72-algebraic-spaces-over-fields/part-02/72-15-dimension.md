---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.dimension_le_of_isIntegralHom, AlgebraicGeometry.Space.dimension_eq_of_isIntegralHom_of_isSurjective, AlgebraicGeometry.Space.dimension_le_dimension_add_transcendenceDegree, AlgebraicGeometry.Space.dimension_eq_dimension_add_transcendenceDegree
statement: formalized
proof: formalized
---

# 72.15 Dimension

Section 72.15 of the Stacks Project, [Tag 0EDA](https://stacks.math.columbia.edu/tag/0EDA). 2 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EDB, a lemma

[Tag 0EDB](https://stacks.math.columbia.edu/tag/0EDB) in the Stacks Project.

**`AlgebraicGeometry.Space.dimension_le_of_isIntegralHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionIntegralMorphism.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DimensionIntegralMorphism.lean#L110). The attribute's comment: “dimension inequality”.

> An integral morphism of algebraic spaces over `S` does not increase the dimension.

```lean
theorem dimension_le_of_isIntegralHom (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsIntegralHom B S hS f) :
    dimension B S hS X hX ≤ dimension B S hS Y hY
```

**`AlgebraicGeometry.Space.dimension_eq_of_isIntegralHom_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionIntegralMorphism.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DimensionIntegralMorphism.lean#L120). The attribute's comment: “surjective case”.

> A surjective integral morphism of algebraic spaces over `S` preserves the dimension.

```lean
theorem dimension_eq_of_isIntegralHom_of_isSurjective (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsIntegralHom B S hS f)
    (hsurj : IsSurjective B S hS f) :
    dimension B S hS X hX = dimension B S hS Y hY
```

## Tag 0EDC, a lemma

[Tag 0EDC](https://stacks.math.columbia.edu/tag/0EDC) in the Stacks Project.

**`AlgebraicGeometry.Space.dimension_le_dimension_add_transcendenceDegree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralDominantMorphism.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralDominantMorphism.lean#L166). The attribute's comment: “the dimension inequality”.

> **Stacks 0EDC, the dimension inequality.** Let `f : X ⟶ Y` be a dominant morphism locally
> of finite type of integral algebraic spaces over `S` with `Y` locally Noetherian, and let `x`
> and `y` be generic points of `|X|` and `|Y|`. If the transcendence degree of `f` at `x` is
> `r`, then `dim X ≤ dim Y + r`.

```lean
theorem dimension_le_dimension_add_transcendenceDegree
    (s : IntegralDominantMorphismSituation B S hS) (r : ℕ∞)
    (hr : HasTranscendenceDegreeAt B S hS s.hom s.sourcePoint r) :
    dimension B S hS s.source s.isAlgebraicSpace_source ≤
      dimension B S hS s.target s.isAlgebraicSpace_target + (r : WithBot ℕ∞)
```

**`AlgebraicGeometry.Space.dimension_eq_dimension_add_transcendenceDegree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IntegralDominantMorphism.lean, line 417](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IntegralDominantMorphism.lean#L417). The attribute's comment: “equality for a proper morphism”.

> **Stacks 0EDC, equality for a proper morphism.** Let `f : X ⟶ Y` be a dominant morphism
> locally of finite type of integral algebraic spaces over `S` with `Y` locally Noetherian, and
> let `x` and `y` be generic points of `|X|` and `|Y|`. If `f` is proper and the transcendence
> degree of `f` at `x` is `r`, then `dim X = dim Y + r`.
>
> The inequality `≤` is `AlgebraicGeometry.Space.dimension_le_dimension_add_transcendenceDegree`.
> For the reverse inequality both dimensions are read on one commuting pair of surjective étale
> scheme charts `U → X` and `V → Y` (Stacks 0A4H and Stacks 02X1), so that each becomes a
> topological Krull dimension and a bound on it is a chain of specializations. A chain of length
> `d` in `V` gives one of length at least `d` in `|Y|` ending at `y`, since two points of an
> étale chart with the same image, one a specialization of the other, are equal (Stacks 03K5);
> properness makes `|f|` closed, so that chain lifts to `|X|` from any point above `y` (Stacks
> 0066). Below such a point
> there are `r` further nontrivial specializations: the fibre of `U → V` through the chart point
> above `x` has dimension at least the transcendence degree there by the dimension formula of
> Stacks 02FX, and the resulting chain lies over `y`. The concatenation is a chain of length
> `d + r` in `|X|`, and it lifts to the chart `U` by Stacks 03IL.

```lean
theorem dimension_eq_dimension_add_transcendenceDegree
    (s : IntegralDominantMorphismSituation B S hS) (hproper : IsProper B S hS s.hom) (r : ℕ∞)
    (hr : HasTranscendenceDegreeAt B S hS s.hom s.sourcePoint r) :
    dimension B S hS s.source s.isAlgebraicSpace_source =
      dimension B S hS s.target s.isAlgebraicSpace_target + (r : WithBot ℕ∞)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 72.15, Tag 0EDA](https://stacks.math.columbia.edu/tag/0EDA)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
