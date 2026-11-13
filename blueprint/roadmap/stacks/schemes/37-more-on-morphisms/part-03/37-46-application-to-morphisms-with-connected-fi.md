---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_compactOpen_geometricallyConnected_fibers, AlgebraicGeometry.exists_etaleNeighborhood_geometricallyConnected, AlgebraicGeometry.exists_etaleCover_factors_geometricallyConnected, AlgebraicGeometry.exists_etaleNeighborhood_geometricallyIntegral
statement: formalized
proof: formalized
---

# 37.46 Application to morphisms with connected fibres

Section 37.46 of the Stacks Project, [Tag 057H](https://stacks.math.columbia.edu/tag/057H). 4 tags here are carried by 4 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 057I, a lemma

[Tag 057I](https://stacks.math.columbia.edu/tag/057I) in the Stacks Project.

**`AlgebraicGeometry.exists_compactOpen_geometricallyConnected_fibers`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/ShrinkingConsequences.lean, line 123](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/ShrinkingConsequences.lean#L123).

> **Stacks Project, Tag 057I.** A geometrically connected fibre in a flat, finitely presented
> family with geometrically reduced fibres and a nonempty finite locally free multisection has a
> quasi-compact open neighbourhood in the source whose nonempty fibres are geometrically
> connected.

```lean
theorem exists_compactOpen_geometricallyConnected_fibers : Statement057I.{u}
```

## Tag 055W, a lemma

[Tag 055W](https://stacks.math.columbia.edu/tag/055W) in the Stacks Project.

**`AlgebraicGeometry.exists_etaleNeighborhood_geometricallyConnected`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/ShrinkingConsequences.lean, line 131](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/ShrinkingConsequences.lean#L131).

> **Stacks Project, Tag 055W.** A geometrically connected open in a fibre of a flat, finitely
> presented morphism with geometrically reduced fibres spreads, after an affine elementary étale
> base change, to a quasi-compact open with geometrically connected fibres.

```lean
theorem exists_etaleNeighborhood_geometricallyConnected : Statement055W.{u}
```

## Tag 0EY5, a lemma

[Tag 0EY5](https://stacks.math.columbia.edu/tag/0EY5) in the Stacks Project.

**`AlgebraicGeometry.exists_etaleCover_factors_geometricallyConnected`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ConnectedFibreCover.lean, line 625](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ConnectedFibreCover.lean#L625).

> **Stacks Project, Tag 0EY5.** A flat morphism locally of finite presentation with
> geometrically reduced fibres admits an étale covering of its source each member of which
> factors through an étale morphism to the base, the first factor being flat of finite
> presentation with geometrically connected and geometrically reduced fibres.

```lean
theorem exists_etaleCover_factors_geometricallyConnected
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFinitePresentation f] [Flat f]
    [GeometricallyReduced f] :
    ∃ 𝒰 : X.Cover.{u} Scheme.etalePrecoverage, ∀ i : 𝒰.I₀,
      ∃ (Sᵢ : Scheme.{u}) (h : Sᵢ ⟶ S) (g : 𝒰.X i ⟶ Sᵢ),
        Etale h ∧ Flat g ∧ FinitePresentation g ∧
          GeometricallyConnected g ∧ GeometricallyReduced g ∧
            g ≫ h = 𝒰.f i ≫ f
```

## Tag 057J, a lemma

[Tag 057J](https://stacks.math.columbia.edu/tag/057J) in the Stacks Project.

**`AlgebraicGeometry.exists_etaleNeighborhood_geometricallyIntegral`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/ShrinkingConsequences.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/ShrinkingConsequences.lean#L139).

> **Stacks Project, Tag 057J.** A geometrically irreducible open in a fibre of a normal,
> finitely presented morphism spreads, after an affine elementary étale base change, to a
> quasi-compact open with geometrically integral fibres.

```lean
theorem exists_etaleNeighborhood_geometricallyIntegral : Statement057J.{u}
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.46, Tag 057H](https://stacks.math.columbia.edu/tag/057H)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
