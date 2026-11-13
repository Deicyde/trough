---
declaration: section
origin: cited
lean: AlgebraicGeometry.MorphismOfGerms.IsEtaleLocalOnSourceAndTarget, AlgebraicGeometry.MorphismOfGerms.hasRepresentativeWithProperty_isEtaleLocalOnSourceAndTarget, AlgebraicGeometry.IsEtaleLocalOnSourceAndTarget.iff_forall_hasRepresentativeWithProperty, AlgebraicGeometry.MorphismOfGerms.isEtaleLocalOnSourceAndTarget_isFlat, AlgebraicGeometry.etale_fiberMap, AlgebraicGeometry.fiberLocalRingDimension_isEtaleLocalOnSourceAndTarget, AlgebraicGeometry.MorphismOfGerms.residueFieldTranscendenceDegree_isEtaleLocalOnSourceAndTarget, AlgebraicGeometry.fiberDimensionAt_isEtaleLocalOnSourceAndTarget
statement: formalized
proof: formalized
---

# 35.33 Properties of morphisms of germs local on source-and-target

Section 35.33 of the Stacks Project, [Tag 04R5](https://stacks.math.columbia.edu/tag/04R5). 8 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04NB, a definition

[Tag 04NB](https://stacks.math.columbia.edu/tag/04NB) in the Stacks Project.

**`AlgebraicGeometry.MorphismOfGerms.IsEtaleLocalOnSourceAndTarget`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germ/Local.lean, line 66](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Germ/Local.lean#L66).

> A property of morphisms of germs of schemes is étale local on the source and target if it
> is invariant under commutative squares with étale vertical arrows.

```lean
structure MorphismOfGerms.IsEtaleLocalOnSourceAndTarget
    (Q : ∀ {X Y : GermOfScheme.{u}}, MorphismOfGerms X Y → Prop) : Prop
```

## Tag 04R6, a lemma

[Tag 04R6](https://stacks.math.columbia.edu/tag/04R6) in the Stacks Project.

**`AlgebraicGeometry.MorphismOfGerms.hasRepresentativeWithProperty_isEtaleLocalOnSourceAndTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germ/InducedProperty.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Germ/InducedProperty.lean#L108).

> Étale locality on the source and target of a property of morphisms of schemes passes to
> the property it induces on morphisms of germs.

```lean
theorem hasRepresentativeWithProperty_isEtaleLocalOnSourceAndTarget
    (P : MorphismProperty Scheme.{u})
    (hP : AlgebraicGeometry.IsEtaleLocalOnSourceAndTarget P) :
    IsEtaleLocalOnSourceAndTarget (HasRepresentativeWithProperty P)
```

## Tag 04R7, a lemma

[Tag 04R7](https://stacks.math.columbia.edu/tag/04R7) in the Stacks Project.

**`AlgebraicGeometry.IsEtaleLocalOnSourceAndTarget.iff_forall_hasRepresentativeWithProperty`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germ/EtaleLocalCriterion.lean, line 53](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Germ/EtaleLocalCriterion.lean#L53).

> A property of morphisms of schemes which is étale local on the source and target holds for
> a morphism exactly when the associated property of morphisms of germs holds for every induced
> morphism of germs.

```lean
theorem IsEtaleLocalOnSourceAndTarget.iff_forall_hasRepresentativeWithProperty
    (P : MorphismProperty Scheme.{u}) (hP : IsEtaleLocalOnSourceAndTarget P)
    {X Y : Scheme.{u}} (f : X ⟶ Y) :
    P f ↔ ∀ x : X, MorphismOfGerms.HasRepresentativeWithProperty P
      (MorphismOfGerms.ofSchemeHom f x)
```

## Tag 04ND, a lemma

[Tag 04ND](https://stacks.math.columbia.edu/tag/04ND) in the Stacks Project.

**`AlgebraicGeometry.MorphismOfGerms.isEtaleLocalOnSourceAndTarget_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/GermSourceAndTarget/Flat.lean, line 461](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/GermSourceAndTarget/Flat.lean#L461).

> Flatness of the map on local rings of a morphism of germs is étale local on
> both source and target.

```lean
theorem isEtaleLocalOnSourceAndTarget_isFlat :
    IsEtaleLocalOnSourceAndTarget (@IsFlat.{u})
```

## Tag 04NI, a lemma

[Tag 04NI](https://stacks.math.columbia.edu/tag/04NI) in the Stacks Project.

**`AlgebraicGeometry.etale_fiberMap`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Fiber.lean, line 164](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/EtaleLocal/Fiber.lean#L164).

> **Stacks Project, Tag 04NI.** The morphism between corresponding fibres in
> a commutative square with étale vertical arrows is étale.

```lean
public lemma etale_fiberMap (f' : U' ⟶ V') (g' : U' ⟶ U)
    (g : V' ⟶ V) (f : U ⟶ V) (h : g' ≫ f = f' ≫ g) (v' : V')
    [Etale g'] [Etale g] : Etale (fiberMap f' g' g f h v')
```

## Tag 04NJ, a lemma

[Tag 04NJ](https://stacks.math.columbia.edu/tag/04NJ) in the Stacks Project.

**`AlgebraicGeometry.fiberLocalRingDimension_isEtaleLocalOnSourceAndTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germs/FiberLocalRingDimension.lean, line 282](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Germs/FiberLocalRingDimension.lean#L282).

> The dimension of the local ring of the fibre of a morphism of germs at its distinguished
> point is étale local on the source and target germs.

```lean
public theorem fiberLocalRingDimension_isEtaleLocalOnSourceAndTarget (d : ℕ∞) :
    MorphismOfGerms.IsEtaleLocalOnSourceAndTarget
      (@HasFiberLocalRingDimension.{u} d)
```

## Tag 04NK, a lemma

[Tag 04NK](https://stacks.math.columbia.edu/tag/04NK) in the Stacks Project.

**`AlgebraicGeometry.MorphismOfGerms.residueFieldTranscendenceDegree_isEtaleLocalOnSourceAndTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germ/TranscendenceDegree.lean, line 563](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Germ/TranscendenceDegree.lean#L563).

> **Stacks Project, Tag 04NK.** Residue-field transcendence degree at a
> point is étale local on the source and target of a morphism of germs.

```lean
public theorem residueFieldTranscendenceDegree_isEtaleLocalOnSourceAndTarget
    (r : ℕ∞) :
    IsEtaleLocalOnSourceAndTarget
      (@HasResidueFieldTranscendenceDegree.{u} r)
```

## Tag 04NL, a lemma

[Tag 04NL](https://stacks.math.columbia.edu/tag/04NL) in the Stacks Project.

**`AlgebraicGeometry.fiberDimensionAt_isEtaleLocalOnSourceAndTarget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/Germs/FiberDimension.lean, line 185](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Descent/Germs/FiberDimension.lean#L185).

> **Stacks Project, Tag 04NL.** Dimension at a point of a fibre is étale
> local on the source and target of a morphism of germs.

```lean
public theorem fiberDimensionAt_isEtaleLocalOnSourceAndTarget (d : ℕ∞) :
    MorphismOfGerms.IsEtaleLocalOnSourceAndTarget (@HasFiberDimensionAt.{u} d)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 35.33, Tag 04R5](https://stacks.math.columbia.edu/tag/04R5)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
