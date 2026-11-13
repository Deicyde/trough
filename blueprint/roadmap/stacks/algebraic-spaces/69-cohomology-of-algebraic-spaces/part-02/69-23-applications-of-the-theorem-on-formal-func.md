---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isFinite_iff_isProper_and_discreteFibres, AlgebraicGeometry.Space.exists_isOpenSubspace_isFinite_pullback_snd_of_finite_geometricFibre
statement: formalized
proof: formalized
---

# 69.23 Applications of the theorem on formal functions

Section 69.23 of the Stacks Project, [Tag 0A4U](https://stacks.math.columbia.edu/tag/0A4U). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0A4V, a lemma

[Tag 0A4V](https://stacks.math.columbia.edu/tag/0A4V) in the Stacks Project.

**`AlgebraicGeometry.Space.isFinite_iff_isProper_and_discreteFibres`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteProperDiscreteFibres.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteProperDiscreteFibres.lean#L65).

> **Stacks 0A4V.** A morphism `f : X ⟶ Y` of algebraic spaces over `S` is finite exactly when
> it is proper and the point space of its fibre over every field-valued point of `Y` is discrete.
>
> The source assumes `Y` locally Noetherian; the equivalence holds for every target, as conditions
> (1) and (3) of Stacks 0A4X.

```lean
theorem isFinite_iff_isProper_and_discreteFibres
    (spaceX : IsAlgebraicSpace B S hS X) (spaceY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    IsFinite B S hS f ↔
      IsProper B S hS f ∧ ∀ p : FieldValuedPoint B S hS Y,
        DiscreteTopology (points B S hS (pullback (yonedaEquiv.symm p.value) f))
```

## Tag 0A4W, a lemma

[Tag 0A4W](https://stacks.math.columbia.edu/tag/0A4W) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isOpenSubspace_isFinite_pullback_snd_of_finite_geometricFibre`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteNearFiniteGeometricFibre.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteNearFiniteGeometricFibre.lean#L80).

> **Stacks 0A4W.** Let `f : X ⟶ Y` be a proper morphism of algebraic spaces over `S` and let
> `ȳ` be a geometric point of `Y` whose geometric fibre `X_ȳ` has finitely many points. Then `ȳ`
> has an open neighbourhood `V ⊆ Y` over which `f` becomes finite, in the sense that the base
> change `f^{-1}(V) ⟶ V` is finite.
>
> The source assumes `Y` locally Noetherian; the conclusion holds for every target. A proper
> morphism is decent, so the finite fibre `X_ȳ` has discrete point space by Stacks 0ACK, hence `f`
> is quasi-finite at every point of `|X|` over the image of `ȳ`, and Stacks 0A4Y applies.

```lean
theorem exists_isOpenSubspace_isFinite_pullback_snd_of_finite_geometricFibre
    (spaceX : IsAlgebraicSpace B S hS X) (spaceY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (proper : IsProper B S hS f) (y : GeometricPoint B S hS Y)
    (finiteFibre : Finite (points B S hS (pullback f (yonedaEquiv.symm y.val.value)))) :
    ∃ V : Subfunctor Y, IsOpenSubspace B S hS V ∧
      y.image ∈ Set.range (pointsMap B S hS V.toFunctor V.ι) ∧
      IsFinite B S hS (pullback.snd f V.ι)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 69.23, Tag 0A4U](https://stacks.math.columbia.edu/tag/0A4U)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
