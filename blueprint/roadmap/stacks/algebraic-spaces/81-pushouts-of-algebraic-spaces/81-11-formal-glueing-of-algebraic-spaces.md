---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.FormalGlueingSituation.formalGlueingFunctor, AlgebraicGeometry.Space.FormalGlueingSituation.affineGlueingFunctor_isEquivalence, AlgebraicGeometry.Space.FormalGlueingSituation.closedGlueingFunctor_isEquivalence, AlgebraicGeometry.Space.FormalGlueingSituation.finiteGlueingFunctor_isEquivalence, AlgebraicGeometry.Space.FormalGlueingSituation.reflectsIsomorphisms_formalGlueingFunctor, AlgebraicGeometry.Space.FormalGlueingSituation.bijective_formalGlueingFunctor_map_of_isSeparated
statement: formalized
proof: formalized
---

# 81.11 Formal glueing of algebraic spaces

Section 81.11 of the Stacks Project, [Tag 0AF2](https://stacks.math.columbia.edu/tag/0AF2). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AF3, an equation

[Tag 0AF3](https://stacks.math.columbia.edu/tag/0AF3) in the Stacks Project.

**`AlgebraicGeometry.Space.FormalGlueingSituation.formalGlueingFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingSpaces.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingSpaces.lean#L158).

> Restriction from algebraic spaces over `X` to their cartesian
> formal-glueing diagrams. The comparison identifies it naturally with
> pullback on each component and the canonical associativity identification
> on the overlap.

```lean
noncomputable def formalGlueingFunctor (D : FormalGlueingSituation B S hS) :
    Σ F : spacesOverX D ⥤ glueingData D,
      F ⋙ (show ObjectProperty
          (Comma (Over.pullback (D.U.fromPreimage D.f))
            (Over.pullback D.V.ι)) from
          fun T ↦ IsIso T.hom ∧
            IsAlgebraicSpace B S hS T.left.left ∧
            IsAlgebraicSpace B S hS T.right.left).ι ≅
        (show ObjectProperty (Over D.X) from
          fun T ↦ IsAlgebraicSpace B S hS T.left).ι ⋙
          restrictionDiagram D
```

## Tag 0AF4, a lemma

[Tag 0AF4](https://stacks.math.columbia.edu/tag/0AF4) in the Stacks Project.

**`AlgebraicGeometry.Space.FormalGlueingSituation.affineGlueingFunctor_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingSpacesRestrictedEquivalences.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingSpacesRestrictedEquivalences.lean#L55). The attribute's comment: “part (1)”.

> **Stacks 0AF4, part (1).**  The functor of Stacks 0AF3 is an equivalence from algebraic
> spaces affine over `X` onto glueing triples whose maps `U' ⟶ U`, `V' ⟶ V` and `Y' ⟶ Y` are
> affine.

```lean
theorem affineGlueingFunctor_isEquivalence (D : FormalGlueingSituation B S hS) :
    (affineGlueingFunctor D).IsEquivalence
```

**`AlgebraicGeometry.Space.FormalGlueingSituation.closedGlueingFunctor_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingSpacesRestrictedEquivalences.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingSpacesRestrictedEquivalences.lean#L62). The attribute's comment: “part (2)”.

> **Stacks 0AF4, part (2).**  The functor of Stacks 0AF3 is an equivalence from closed
> immersions into `X` onto glueing triples whose three maps are closed immersions.

```lean
theorem closedGlueingFunctor_isEquivalence (D : FormalGlueingSituation B S hS) :
    (closedGlueingFunctor D).IsEquivalence
```

**`AlgebraicGeometry.Space.FormalGlueingSituation.finiteGlueingFunctor_isEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingSpacesRestrictedEquivalences.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingSpacesRestrictedEquivalences.lean#L69). The attribute's comment: “part (3)”.

> **Stacks 0AF4, part (3).**  The functor of Stacks 0AF3 is an equivalence from algebraic
> spaces finite over `X` onto glueing triples whose three maps are finite.

```lean
theorem finiteGlueingFunctor_isEquivalence (D : FormalGlueingSituation B S hS) :
    (finiteGlueingFunctor D).IsEquivalence
```

## Tag 0AF5, a lemma

[Tag 0AF5](https://stacks.math.columbia.edu/tag/0AF5) in the Stacks Project.

**`AlgebraicGeometry.Space.FormalGlueingSituation.reflectsIsomorphisms_formalGlueingFunctor`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingSpaces.lean, line 320](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingSpaces.lean#L320).

> **Stacks 0AF5.** The restriction functor from algebraic spaces over `X` to cartesian
> formal-glueing triples reflects isomorphisms: a morphism over `X` whose restrictions to `U` and
> to `Y` are invertible is itself invertible.

```lean
instance reflectsIsomorphisms_formalGlueingFunctor
    (D : FormalGlueingSituation B S hS) :
    (formalGlueingFunctor D).1.ReflectsIsomorphisms
```

## Tag 0AF6, a lemma

[Tag 0AF6](https://stacks.math.columbia.edu/tag/0AF6) in the Stacks Project.

**`AlgebraicGeometry.Space.FormalGlueingSituation.bijective_formalGlueingFunctor_map_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingSpacesSeparatedBijection.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Pushouts/FormalGlueingSpacesSeparatedBijection.lean#L59).

> In a formal glueing situation, the functor of Stacks 0AF3 is bijective on
> morphisms `X'₁ ⟶ X'₂` of algebraic spaces over `X` whenever `X'₂ ⟶ X` is separated.

```lean
theorem bijective_formalGlueingFunctor_map_of_isSeparated (D : FormalGlueingSituation B S hS)
    {X₁ X₂ : spacesOverX D} (hsep : IsSeparated B S hS X₂.obj.hom) :
    Function.Bijective fun a : X₁ ⟶ X₂ ↦ (formalGlueingFunctor D).1.map a
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 81.11, Tag 0AF2](https://stacks.math.columbia.edu/tag/0AF2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
