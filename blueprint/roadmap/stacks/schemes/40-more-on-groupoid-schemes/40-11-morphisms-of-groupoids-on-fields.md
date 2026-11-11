---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupoidMorphismOverFieldSituation, AlgebraicGeometry.isClosed_range_mapArrows_of_isOpen, AlgebraicGeometry.comp_mapsTo_closure_range_mapArrows, AlgebraicGeometry.GroupoidScheme.reducedClosureImage, AlgebraicGeometry.GroupoidScheme.reducedClosureGroupoid_objects, AlgebraicGeometry.GroupoidScheme.reducedClosureGroupoid_arrows, AlgebraicGeometry.GroupoidScheme.reducedClosureInclusion_mapObjects, AlgebraicGeometry.GroupoidScheme.reducedClosureInclusion_mapArrows_left
statement: formalized
proof: formalized
---

# 40.11 Morphisms of groupoids on fields

Section 40.11 of the Stacks Project, [Tag 04Q4](https://stacks.math.columbia.edu/tag/04Q4). 9 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04Q5, a situation

[Tag 04Q5](https://stacks.math.columbia.edu/tag/04Q5) in the Stacks Project.

**`AlgebraicGeometry.GroupoidMorphismOverFieldSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/Situation.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/Situation.lean#L56).

> The standing data of Situation 04Q5: two groupoid schemes over a base scheme sharing a
> scheme of objects which is the spectrum of a field, and a morphism between them whose
> component on objects is the identity.

```lean
structure GroupoidMorphismOverFieldSituation
```

## Tag 04Q6, a lemma

[Tag 04Q6](https://stacks.math.columbia.edu/tag/04Q6) in the Stacks Project.

**`AlgebraicGeometry.isClosed_range_mapArrows_of_isOpen`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/OpenImageOverField.lean, line 228](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/OpenImageOverField.lean#L228).

> **Stacks Project, Tag 04Q6.** If a morphism of groupoid schemes whose common object
> scheme is the spectrum of a field has open image on arrows, then that image is closed.

```lean
public lemma isClosed_range_mapArrows_of_isOpen
    {S : Scheme.{u}} {k : Type u} [Field k]
    {G₁ G₂ : GroupoidScheme S} (F : GroupoidScheme.Hom G₁ G₂)
    (hobjects : G₁.objects = G₂.objects)
    (hfield : G₁.objects.left = Spec (.of k))
    (hmapObjects : F.mapObjects = eqToHom hobjects)
    (hopen : IsOpen (Set.range F.mapArrows.left.base)) :
    IsClosed (Set.range F.mapArrows.left.base)
```

## Tag 04Q7, a lemma

[Tag 04Q7](https://stacks.math.columbia.edu/tag/04Q7) in the Stacks Project.

**`AlgebraicGeometry.comp_mapsTo_closure_range_mapArrows`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/ImageClosure.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/ImageClosure.lean#L66).

> **Stacks Project, Tag 04Q7.** For a morphism of groupoid schemes over a field which is the
> identity on the common scheme of objects, the closure of the image on arrows is stable under
> composition.

```lean
theorem comp_mapsTo_closure_range_mapArrows {S : Scheme.{u}} {k : Type u} [Field k]
    {G₁ G₂ : GroupoidScheme S} (F : GroupoidScheme.Hom G₁ G₂)
    (hobjects : G₁.objects = G₂.objects) (hfield : G₁.objects.left = Spec (.of k))
    (hmapObjects : F.mapObjects = eqToHom hobjects) :
    Set.MapsTo G₂.comp.left.base
      ((pullback.fst G₂.source G₂.target).left.base ⁻¹'
          closure (Set.range F.mapArrows.left.base) ∩
        (pullback.snd G₂.source G₂.target).left.base ⁻¹'
          closure (Set.range F.mapArrows.left.base))
      (closure (Set.range F.mapArrows.left.base))
```

## Tag 04Q8, a lemma

[Tag 04Q8](https://stacks.math.columbia.edu/tag/04Q8) in the Stacks Project.

**`AlgebraicGeometry.GroupoidScheme.reducedClosureImage`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/ReducedClosureGroupoid.lean, line 476](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/ReducedClosureGroupoid.lean#L476). The attribute's comment: “construction”. References: SGA 3 VIA (0.2), “special case”.

> **Stacks Project, Tag 04Q8.** The reduced closure of the image on arrows of a morphism of
> groupoid schemes over a perfect field which is the identity on objects carries a groupoid
> structure for which the closed immersion into the target is a morphism of groupoid schemes.

```lean
noncomputable def reducedClosureImage {k : Type u} [Field k] [PerfectField k]
    (F : GroupoidScheme.Hom G₁ G₂) (hobjects : G₁.objects = G₂.objects)
    (hfield : G₁.objects.left = Spec (.of k))
    (hmapObjects : F.mapObjects = eqToHom hobjects) : ReducedClosureImage F
```

**`AlgebraicGeometry.GroupoidScheme.reducedClosureGroupoid_objects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/ReducedClosureGroupoid.lean, line 500](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/ReducedClosureGroupoid.lean#L500). The attribute's comment: “object scheme”.

> **Stacks Project, Tag 04Q8.** The reduced-closure groupoid has the same scheme of objects
> as the target groupoid.

```lean
theorem reducedClosureGroupoid_objects {k : Type u} [Field k] [PerfectField k]
    (F : GroupoidScheme.Hom G₁ G₂) (hobjects : G₁.objects = G₂.objects)
    (hfield : G₁.objects.left = Spec (.of k))
    (hmapObjects : F.mapObjects = eqToHom hobjects) :
    (reducedClosureGroupoid F hobjects hfield hmapObjects).objects = G₂.objects
```

**`AlgebraicGeometry.GroupoidScheme.reducedClosureGroupoid_arrows`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/ReducedClosureGroupoid.lean, line 510](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/ReducedClosureGroupoid.lean#L510). The attribute's comment: “arrow scheme”.

> **Stacks Project, Tag 04Q8.** The scheme of arrows of the reduced-closure groupoid is the
> reduced closure of the image on arrows.

```lean
theorem reducedClosureGroupoid_arrows {k : Type u} [Field k] [PerfectField k]
    (F : GroupoidScheme.Hom G₁ G₂) (hobjects : G₁.objects = G₂.objects)
    (hfield : G₁.objects.left = Spec (.of k))
    (hmapObjects : F.mapObjects = eqToHom hobjects) :
    (reducedClosureGroupoid F hobjects hfield hmapObjects).arrows = reducedClosureArrows F
```

**`AlgebraicGeometry.GroupoidScheme.reducedClosureInclusion_mapObjects`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/ReducedClosureGroupoid.lean, line 520](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/ReducedClosureGroupoid.lean#L520). The attribute's comment: “inclusion on objects”.

> **Stacks Project, Tag 04Q8.** The canonical morphism from the reduced-closure groupoid is
> the identity on objects.

```lean
theorem reducedClosureInclusion_mapObjects {k : Type u} [Field k] [PerfectField k]
    (F : GroupoidScheme.Hom G₁ G₂) (hobjects : G₁.objects = G₂.objects)
    (hfield : G₁.objects.left = Spec (.of k))
    (hmapObjects : F.mapObjects = eqToHom hobjects) :
    (reducedClosureInclusion F hobjects hfield hmapObjects).mapObjects =
      eqToHom (reducedClosureGroupoid_objects F hobjects hfield hmapObjects)
```

**`AlgebraicGeometry.GroupoidScheme.reducedClosureInclusion_mapArrows_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/ReducedClosureGroupoid.lean, line 542](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/ReducedClosureGroupoid.lean#L542). The attribute's comment: “inclusion on arrows”.

> **Stacks Project, Tag 04Q8.** On arrows the canonical morphism from the reduced-closure
> groupoid is the closed immersion of the reduced closure of the image.

```lean
theorem reducedClosureInclusion_mapArrows_left {k : Type u} [Field k] [PerfectField k]
    (F : GroupoidScheme.Hom G₁ G₂) (hobjects : G₁.objects = G₂.objects)
    (hfield : G₁.objects.left = Spec (.of k))
    (hmapObjects : F.mapObjects = eqToHom hobjects) :
    (reducedClosureInclusion F hobjects hfield hmapObjects).mapArrows.left =
      eqToHom (congrArg Over.left
        (reducedClosureGroupoid_arrows F hobjects hfield hmapObjects)) ≫
        (reducedClosureArrowImage F).subschemeι
```

## Tag 04Q9, a lemma

[Tag 04Q9](https://stacks.math.columbia.edu/tag/04Q9) in the Stacks Project.

**`AlgebraicGeometry.isClosed_range_mapArrows_of_isLocallyClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/LocallyClosedImage.lean, line 391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/LocallyClosedImage.lean#L391).

> **Stacks Project, Tag 04Q9.** The image on arrows of a morphism of groupoid schemes over a
> field which is the identity on their common scheme of objects is closed as soon as it is
> locally closed.

```lean
theorem isClosed_range_mapArrows_of_isLocallyClosed {k : Type u} [Field k]
    (F : GroupoidScheme.Hom G₁ G₂) (hobjects : G₁.objects = G₂.objects)
    (hfield : G₁.objects.left = Spec (.of k))
    (hmapObjects : F.mapObjects = eqToHom hobjects)
    (h : IsLocallyClosed (Set.range F.mapArrows.left.base)) :
    IsClosed (Set.range F.mapArrows.left.base)
```

## Tag 04QA, a lemma

[Tag 04QA](https://stacks.math.columbia.edu/tag/04QA) in the Stacks Project.

**`AlgebraicGeometry.exists_groupoidScheme_image`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/ArrowImageOverField.lean, line 627](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/Slicing/ArrowImageOverField.lean#L627).

> **Stacks Project, Tag 04QA.** The scheme-theoretic image of a quasi-compact
> arrow map of groupoid schemes over a field has the restricted groupoid structure.

```lean
public theorem exists_groupoidScheme_image
    {S : Scheme.{u}} {k : Type u} [Field k]
    {G₁ G₂ : GroupoidScheme S} (F : GroupoidScheme.Hom G₁ G₂)
    (hobjects : G₁.objects = G₂.objects)
    (hfield : G₁.objects.left = Spec (.of k))
    (hmapObjects : F.mapObjects = eqToHom hobjects)
    [QuasiCompact F.mapArrows.left] :
    ∃ (H : GroupoidScheme S) (j : GroupoidScheme.Hom H G₂)
      (hHobjects : H.objects = G₂.objects)
      (hHarrows : H.arrows = Over.mk
        (F.mapArrows.left.imageι ≫ G₂.arrows.hom)),
        (j.mapObjects = eqToHom hHobjects) ∧
        (j.mapArrows.left =
          eqToHom (congrArg Over.left hHarrows) ≫ F.mapArrows.left.imageι)
```

## Tag 04QB, a lemma

[Tag 04QB](https://stacks.math.columbia.edu/tag/04QB) in the Stacks Project.

**`AlgebraicGeometry.comp_mapsTo_closure_range_groupoidPreRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/ClosureComposition.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/ClosureComposition.lean#L71).

> **Stacks Project, Tag 04QB.** Let `(U, R, s, t, c)` be a groupoid scheme over `S` with `U`
> the spectrum of a field, and let `Z` be the closure of the image of `j = (t, s)` in `U ×_S U`.
> Then `pr₀₂` maps `Z ×_{pr₁, U, pr₀} Z` into `Z`.

```lean
theorem comp_mapsTo_closure_range_groupoidPreRelation :
    Set.MapsTo
      (prod.lift
        (pullback.fst (prod.snd : G.objects ⨯ G.objects ⟶ G.objects) prod.fst ≫ prod.fst)
        (pullback.snd (prod.snd : G.objects ⨯ G.objects ⟶ G.objects) prod.fst
          ≫ prod.snd)).left.base
      ((pullback.fst (prod.snd : G.objects ⨯ G.objects ⟶ G.objects) prod.fst).left.base ⁻¹'
          closure (Set.range (groupoidPreRelation G).left.base) ∩
        (pullback.snd (prod.snd : G.objects ⨯ G.objects ⟶ G.objects) prod.fst).left.base ⁻¹'
          closure (Set.range (groupoidPreRelation G).left.base))
      (closure (Set.range (groupoidPreRelation G).left.base))
```

## Tag 04QC, a lemma

[Tag 04QC](https://stacks.math.columbia.edu/tag/04QC) in the Stacks Project.

**`AlgebraicGeometry.reducedClosureGroupoidPreRelation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/ClosureComposition.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/ClosureComposition.lean#L89).

> **Stacks Project, Tag 04QC.** For a groupoid scheme `(U, R, s, t, c)` over `S` with `U` the
> spectrum of a perfect field, the reduced closed subscheme `Z` of `U ×_S U` supported on the
> closure of the image of `j = (t, s)` is the scheme of arrows of a groupoid scheme on `U` whose
> structure maps are the restrictions of `pr₁`, `pr₀` and `pr₀₂`.

```lean
noncomputable def reducedClosureGroupoidPreRelation [PerfectField k] :
    GroupoidScheme.ReducedClosureImage (groupoidPreRelationHom G)
```

## Tag 04QD, a lemma

[Tag 04QD](https://stacks.math.columbia.edu/tag/04QD) in the Stacks Project.

**`AlgebraicGeometry.exists_groupoidScheme_image_groupoidPreRelation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/ClosureComposition.lean, line 117](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Groupoids/OverField/Morphisms/ClosureComposition.lean#L117).

> **Stacks Project, Tag 04QD.** For a groupoid scheme `(U, R, s, t, c)` over `S` with `U` the
> spectrum of a field and `R` quasi-compact, the scheme-theoretic image of `j = (t, s)` in
> `U ×_S U` is the scheme of arrows of a groupoid scheme on `U` whose structure maps are the
> restrictions of `pr₁`, `pr₀` and `pr₀₂`.

```lean
theorem exists_groupoidScheme_image_groupoidPreRelation [CompactSpace G.arrows.left] :
    ∃ (H : GroupoidScheme S) (ι : GroupoidScheme.Hom H (prodPairGroupoid G.objects))
      (hHobjects : H.objects = G.objects)
      (hHarrows : H.arrows = Over.mk ((groupoidPreRelation G).left.imageι ≫
        (G.objects ⨯ G.objects).hom)),
        (ι.mapObjects = eqToHom hHobjects) ∧
        (ι.mapArrows.left =
          eqToHom (congrArg Over.left hHarrows) ≫ (groupoidPreRelation G).left.imageι)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 40.11, Tag 04Q4](https://stacks.math.columbia.edu/tag/04Q4)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
