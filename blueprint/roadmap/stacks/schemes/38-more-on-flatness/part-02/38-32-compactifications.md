---
declaration: section
origin: cited
lean: AlgebraicGeometry.CategoryOfCompactifications.isCofiltered_category, AlgebraicGeometry.CategoryOfCompactifications.initial_ι_hasDenseInterior, AlgebraicGeometry.preimage_range_immersion_eq, AlgebraicGeometry.CategoryOfCompactifications.isCofiltered, AlgebraicGeometry.CategoryOfCompactifications.denseCompactification_initial, AlgebraicGeometry.exists_quasiCompact_compactification_over, AlgebraicGeometry.interiorIsomorphisms_hasRightCalculusOfFractions, AlgebraicGeometry.localizedInteriorEquivalence
statement: formalized
proof: formalized
---

# 38.32 Compactifications

Section 38.32 of the Stacks Project, [Tag 0ATT](https://stacks.math.columbia.edu/tag/0ATT). 4 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0ATU, a lemma

[Tag 0ATU](https://stacks.math.columbia.edu/tag/0ATU) in the Stacks Project.

**`AlgebraicGeometry.CategoryOfCompactifications.isCofiltered_category`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Compactification/DenseInterior.lean, line 267](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Compactification/DenseInterior.lean#L267). The attribute's comment: “part (a)”.

> The category of compactifications of a scheme over a quasi-compact, quasi-separated base is
> cofiltered.

```lean
theorem isCofiltered_category : IsCofiltered D.category
```

**`AlgebraicGeometry.CategoryOfCompactifications.initial_ι_hasDenseInterior`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Compactification/DenseInterior.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Compactification/DenseInterior.lean#L283). The attribute's comment: “part (b)”.

> The full subcategory of compactifications whose interior is dense and scheme-theoretically
> dense is initial.

```lean
theorem initial_ι_hasDenseInterior : (HasDenseInterior D.X).ι.Initial
```

**`AlgebraicGeometry.preimage_range_immersion_eq`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/Compactifications.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/Compactifications.lean#L140). The attribute's comment: “preimage\_of\_interior”.

> **Stacks Project, Tag 0ATU.** For a morphism between compactifications whose source
> interior is dense, the inverse image of the target interior is exactly the source
> interior.

```lean
lemma preimage_range_immersion_eq
    (D : CategoryOfCompactifications.{u}) (j' j : D.category) (f : j' ⟶ j)
    (hdense : DenseRange j'.immersion.base) :
    (CompactificationOf.Hom.map f).base ⁻¹'
      Set.range j.immersion.base = Set.range j'.immersion.base
```

**`AlgebraicGeometry.CategoryOfCompactifications.isCofiltered`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/CompactificationsCofiltered.lean, line 167](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/CompactificationsCofiltered.lean#L167). The attribute's comment: “cofiltered”.

> **Stacks Project, Tag 0ATU.** The category of compactifications of a scheme over a
> quasi-compact and quasi-separated base is cofiltered.

```lean
instance isCofiltered : IsCofiltered D.category
```

**`AlgebraicGeometry.CategoryOfCompactifications.denseCompactification_initial`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/CompactificationsCofiltered.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/CompactificationsCofiltered.lean#L195). The attribute's comment: “dense\_compactifications\_initial”.

> **Stacks Project, Tag 0ATU.** The compactifications in which the image of `X` is dense and
> scheme-theoretically dense form an initial full subcategory of the category of all
> compactifications.

```lean
instance denseCompactification_initial :
    (ObjectProperty.ι (IsDenseCompactification D : ObjectProperty D.category)).Initial
```

## Tag 0A9Z, a lemma

[Tag 0A9Z](https://stacks.math.columbia.edu/tag/0A9Z) in the Stacks Project.

**`AlgebraicGeometry.exists_quasiCompact_compactification_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Compactification/OverIntermediate.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Compactification/OverIntermediate.lean#L47). References: SGA 4 XVII (3.2.2), “(v)”.

> A compactifiable `S`-scheme is also compactifiable over a separated finite-type `S`-scheme
> through which its structure morphism factors.

```lean
theorem exists_quasiCompact_compactification_over
    {X Y S : Scheme.{u}} (f : X ⟶ Y) (g : Y ⟶ S)
    [CompactSpace S] [QuasiSeparatedSpace S]
    [IsSeparated g] [LocallyOfFiniteType g] [QuasiCompact g]
    (hX : ∃ j : CompactificationOf (Over.mk (f ≫ g)),
      QuasiCompact j.immersion) :
    ∃ j : CompactificationOf (Over.mk f),
      QuasiCompact j.immersion
```

## Tag 0ATV, a lemma

[Tag 0ATV](https://stacks.math.columbia.edu/tag/0ATV) in the Stacks Project.

**`AlgebraicGeometry.interiorIsomorphisms_hasRightCalculusOfFractions`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/CompactificationFractions.lean, line 365](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/CompactificationFractions.lean#L365).

> **Stacks Project, Tag 0ATV.** Morphisms of compactifications inducing an isomorphism on
> the open subschemes form a right multiplicative system.

```lean
instance interiorIsomorphisms_hasRightCalculusOfFractions (S : Scheme.{u}) :
    (interiorIsomorphisms S).HasRightCalculusOfFractions
```

## Tag 0ATW, a lemma

[Tag 0ATW](https://stacks.math.columbia.edu/tag/0ATW) in the Stacks Project.

**`AlgebraicGeometry.localizedInteriorEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Compactification/LocalizationEquivalence.lean, line 390](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Compactification/LocalizationEquivalence.lean#L390). The attribute's comment: “the equivalence”.

> **Stacks Project, Tag 0ATW.** The equivalence induced by forgetting the ambient proper
> scheme after localizing compactifications at interior isomorphisms.

```lean
noncomputable def localizedInteriorEquivalence (S : Scheme.{u})
    [CompactSpace S] [QuasiSeparatedSpace S] :
    (interiorIsomorphisms S).Localization ≌ Compactifyable S
```

**`AlgebraicGeometry.localizedInteriorEquivalenceCompQ`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Compactification/LocalizationEquivalence.lean, line 404](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Compactification/LocalizationEquivalence.lean#L404). The attribute's comment: “the forgetful functor”.

> **Stacks Project, Tag 0ATW.** The equivalence extends the forgetful functor from
> compactifications, up to a canonical natural isomorphism.

```lean
noncomputable def localizedInteriorEquivalenceCompQ (S : Scheme.{u})
    [CompactSpace S] [QuasiSeparatedSpace S] :
    (interiorIsomorphisms S).Q ⋙
        (localizedInteriorEquivalence S).functor ≅ compactificationInterior S
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.32, Tag 0ATT](https://stacks.math.columbia.edu/tag/0ATT)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
