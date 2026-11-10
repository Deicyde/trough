---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_open_natCard_connectedComponents_fiber_ge, AlgebraicGeometry.geometricallyConnected_fiber_locus_pullback, AlgebraicGeometry.numGeometricConnectedComponents, AlgebraicGeometry.enatCard_connectedComponents_fiberBaseChange, AlgebraicGeometry.numGeometricConnectedComponents_eq_of_isPullback, geometricFiber, AlgebraicGeometry.geometricallyConnectedAfterShrinking, AlgebraicGeometry.exists_open_numGeometricConnectedComponents_eq
statement: formalized
proof: formalized
---

# 37.28 Connected components of fibres

Section 37.28 of the Stacks Project, [Tag 055C](https://stacks.math.columbia.edu/tag/055C). 7 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 055D, a lemma

[Tag 055D](https://stacks.math.columbia.edu/tag/055D) in the Stacks Project.

**`AlgebraicGeometry.exists_open_natCard_connectedComponents_fiber_ge`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FibreConnectedComponents/LowerBound.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FibreConnectedComponents/LowerBound.lean#L208). References: EGA IV (9.7.1), “connected components”.

> **Stacks Project, Tag 055D.** For a finite type morphism to a scheme with a chosen dense
> generic point, the number of connected components of the fibres is at least the number for the
> generic fibre on a nonempty open subset of the base.

```lean
theorem exists_open_natCard_connectedComponents_fiber_ge {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] [QuasiCompact f] (η : Y) (hη : IsGenericPoint η Set.univ) (n : ℕ)
    (hcomp : Nat.card (ConnectedComponents (f.fiber η)) = n) :
    ∃ V : Set Y, IsOpen V ∧ V.Nonempty ∧
      ∀ y ∈ V, n ≤ Nat.card (ConnectedComponents (f.fiber y))
```

## Tag 055E, a lemma

[Tag 055E](https://stacks.math.columbia.edu/tag/055E) in the Stacks Project.

**`AlgebraicGeometry.geometricallyConnected_fiber_locus_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/ConnectedComponents.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/ConnectedComponents.lean#L60).

> **Stacks Project, Tag 055E.** Formation of the locus where the fibres of a scheme morphism
> are geometrically connected commutes with arbitrary base change.

```lean
theorem geometricallyConnected_fiber_locus_pullback
    {X Y Y' : Scheme.{u}} (f : X ⟶ Y) (g : Y' ⟶ Y) :
    {y' : Y' |
        GeometricallyConnected ((pullback.snd f g).fiberToSpecResidueField y')} =
      g ⁻¹' {y : Y | GeometricallyConnected (f.fiberToSpecResidueField y)}
```

## Tag 055F, a lemma

[Tag 055F](https://stacks.math.columbia.edu/tag/055F) in the Stacks Project.

**`AlgebraicGeometry.numGeometricConnectedComponents`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/ConnectedComponents.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/ConnectedComponents.lean#L171). The attribute's comment: “the function”. References: EGA III (4.3.4), “geom. # of components”; EGA IV (15.5.3); EGA IV (4.5.2), “more general”.

> The number of geometric connected components of each fibre of a morphism of schemes.

```lean
def numGeometricConnectedComponents (f : X ⟶ Y) : Y → ℕ∞
```

**`AlgebraicGeometry.enatCard_connectedComponents_fiberBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/ConnectedComponents.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/ConnectedComponents.lean#L178). The attribute's comment: “well-definedness”. References: EGA IV (15.5.3), “more general”.

> Computing the number of connected components after extending a fibre to any separably closed
> extension gives the canonical number of geometric connected components.

```lean
theorem enatCard_connectedComponents_fiberBaseChange (f : X ⟶ Y) (y : Y)
    (K : Type u) [Field K] [Algebra (Y.residueField y) K] [IsSepClosed K] :
    ENat.card (ConnectedComponents (geometricFiber f y K)) =
      numGeometricConnectedComponents f y
```

**`AlgebraicGeometry.numGeometricConnectedComponents_eq_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/ConnectedComponents.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/ConnectedComponents.lean#L202). The attribute's comment: “base change”.

> The number of geometric connected components of fibres is preserved by arbitrary base
> change.

```lean
theorem numGeometricConnectedComponents_eq_of_isPullback
    {X' Y' : Scheme.{u}} (f : X ⟶ Y) (f' : X' ⟶ Y') (i : X' ⟶ X) (g : Y' ⟶ Y)
    (h : IsPullback i f' f g) :
    numGeometricConnectedComponents f' = numGeometricConnectedComponents f ∘ g
```

Declarations registered for the tag:

- [`geometricFiber`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=geometricFiber#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/ConnectedComponents.lean, line 84](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/ConnectedComponents.lean#L84) (StacksFrontier): “geometric fibre”.

## Tag 055G, a lemma

[Tag 055G](https://stacks.math.columbia.edu/tag/055G) in the Stacks Project.

**`AlgebraicGeometry.geometricallyConnectedAfterShrinking`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/ShrinkingConsequences.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/GenericFibre/ShrinkingConsequences.lean#L80).

> **Stacks Project, Tag 055G.** A finite type morphism onto an irreducible base whose fibre
> over the generic point is geometrically connected has geometrically connected fibres over a
> nonempty open subscheme of the base.

```lean
theorem geometricallyConnectedAfterShrinking : GeometricallyConnectedAfterShrinking.{u}
```

## Tag 055H, a lemma

[Tag 055H](https://stacks.math.columbia.edu/tag/055H) in the Stacks Project.

**`AlgebraicGeometry.exists_open_numGeometricConnectedComponents_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FibreConnectedComponents/GenericConstancy.lean, line 701](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FibreConnectedComponents/GenericConstancy.lean#L701).

> **Stacks Project, Tag 055H.** For a finite type morphism of schemes, the number of
> geometric connected components of the fibres is constant on some nonempty open subset of the
> closure of any prescribed point of the base.

```lean
theorem exists_open_numGeometricConnectedComponents_eq {X Y : Scheme.{u}} (f : X ⟶ Y)
    [LocallyOfFiniteType f] [QuasiCompact f] (y : Y) :
    ∃ V : TopologicalSpace.Opens (↑(closure ({y} : Set Y))), Nonempty V ∧
      ∃ n : ℕ∞, ∀ z : V, numGeometricConnectedComponents f z.1.1 = n
```

## Tag 055I, a lemma

[Tag 055I](https://stacks.math.columbia.edu/tag/055I) in the Stacks Project.

**`AlgebraicGeometry.isLocallyConstructible_numGeometricConnectedComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FibreConnectedComponents/Constructible.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FibreConnectedComponents/Constructible.lean#L81). References: EGA IV (9.7.9), “n'(s) (connected)”.

> **Stacks Project, Tag 055I.** Every level set of the number of geometrically connected
> components of the fibres of a morphism of finite presentation is locally constructible.

```lean
theorem isLocallyConstructible_numGeometricConnectedComponents {X Y : Scheme.{u}} (f : X ⟶ Y)
    (hf : AlgebraicGeometry.FinitePresentation f) (n : ℕ∞) :
    IsLocallyConstructible {y : Y | numGeometricConnectedComponents f y = n}
```

## Tag 055J, a lemma

[Tag 055J](https://stacks.math.columbia.edu/tag/055J) in the Stacks Project.

**`AlgebraicGeometry.connectedSpace_fiber_bot_of_isReduced_fiber_closedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/ConnectedGenericFibre.lean, line 234](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/ConnectedGenericFibre.lean#L234). References: EGA IV (15.5.6), “more general”; EGA IV (18.9.7), “special case”.

> **Stacks Project, Tag 055J.** A flat degeneration of a disconnected scheme
> is either disconnected or nonreduced: if a flat scheme over a discrete
> valuation ring is connected and its closed fibre is reduced, then its generic
> fibre is connected.

```lean
theorem connectedSpace_fiber_bot_of_isReduced_fiber_closedPoint
    {R : Type u} [CommRing R] [IsDomain R] [IsDiscreteValuationRing R]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of R)) [Flat f] [ConnectedSpace X]
    [IsReduced (f.fiber (IsLocalRing.closedPoint R))] :
    ConnectedSpace (f.fiber (⟨⊥, inferInstance⟩ : PrimeSpectrum R))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.28, Tag 055C](https://stacks.math.columbia.edu/tag/055C)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
