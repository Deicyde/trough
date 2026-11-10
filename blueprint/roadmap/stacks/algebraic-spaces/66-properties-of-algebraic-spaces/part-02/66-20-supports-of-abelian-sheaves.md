---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.existsUnique_openSubspace_of_subterminalSheaf, AlgebraicGeometry.Space.SpacesEtale.largestOpenZeroSubspace, AlgebraicGeometry.Space.SpacesEtale.largestOpenZeroSubspace_restrict_iff, AlgebraicGeometry.Space.SpacesEtale.restrict_largestOpenZeroSubspace_eq_zero, AlgebraicGeometry.Space.SpacesEtale.largestOpenZeroSubspace_maximal, AlgebraicGeometry.Space.SpacesEtale.germ_eq_zero_iff_mem_largestOpenZeroSubspace, AlgebraicGeometry.Space.SpacesEtale.exists_largestOpenZeroSubspace, AlgebraicGeometry.Space.supportOfSection
statement: formalized
proof: formalized
---

# 66.20 Supports of abelian sheaves

Section 66.20 of the Stacks Project, [Tag 04K7](https://stacks.math.columbia.edu/tag/04K7). 5 tags here are carried by 18 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04K8, a lemma

[Tag 04K8](https://stacks.math.columbia.edu/tag/04K8) in the Stacks Project.

**`AlgebraicGeometry.Space.existsUnique_openSubspace_of_subterminalSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleSubterminalSheaf.lean, line 245](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleSubterminalSheaf.lean#L245).

> **Stacks 04K8.** Every subsheaf of the terminal sheaf on the spaces-étale site of an
> algebraic space is the sheaf of a unique open subspace.

```lean
theorem existsUnique_openSubspace_of_subterminalSheaf
    (F : Subfunctor (spacesEtaleTerminalSheaf B S hS X))
    (hF : Presheaf.IsSheaf (SpacesEtale.topology B S hS X) F.toFunctor) :
    ∃! W : {W : Subfunctor X.1 // IsOpenSubspace B S hS W},
      F = openSubspaceSheaf B S hS X W
```

## Tag 04K9, a lemma

[Tag 04K9](https://stacks.math.columbia.edu/tag/04K9) in the Stacks Project.

**`AlgebraicGeometry.Space.SpacesEtale.largestOpenZeroSubspace`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleZeroLocus.lean, line 271](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleZeroLocus.lean#L271). The attribute's comment: “part (1): the open subspace”.

> **Stacks 04K9, part (1).** The largest open subspace of the algebraic space underlying an
> object `U` of the spaces-étale site of `X` on which a section of an abelian sheaf over `U`
> vanishes: the open subspace whose point set is the zero images of the section.

```lean
noncomputable def largestOpenZeroSubspace
    (F : Sheaf (topology B S hS X) AddCommGrpCat.{v})
    (U : SpacesEtale B S hS X) (σ : F.obj.obj (op U)) :
    {W : Subfunctor (underlying B S hS X U).1 // IsOpenSubspace B S hS W}
```

**`AlgebraicGeometry.Space.SpacesEtale.largestOpenZeroSubspace_restrict_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleZeroLocus.lean, line 295](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleZeroLocus.lean#L295). The attribute's comment: “part (2): the pullback criterion”.

> **Stacks 04K9, part (2).** A section restricts to zero on an object of the spaces-étale
> site over `U` exactly when the image of the points of that object lies in the largest open
> zero subspace.

```lean
theorem largestOpenZeroSubspace_restrict_iff
    (F : Sheaf (topology B S hS X) AddCommGrpCat.{v})
    (U : SpacesEtale B S hS X) (σ : F.obj.obj (op U))
    (V : SpacesEtale B S hS X) (f : V ⟶ U) :
    F.obj.map f.op σ = 0 ↔
      ImageInOpen B S hS X
        (openPoints B S hS X U (largestOpenZeroSubspace B S hS X F U σ)) f
```

**`AlgebraicGeometry.Space.SpacesEtale.restrict_largestOpenZeroSubspace_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleZeroLocus.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleZeroLocus.lean#L308). The attribute's comment: “part (1): the section vanishes on the open subspace”.

> **Stacks 04K9, part (1).** A section vanishes on its largest open zero subspace.

```lean
theorem restrict_largestOpenZeroSubspace_eq_zero
    (F : Sheaf (topology B S hS X) AddCommGrpCat.{v})
    (U : SpacesEtale B S hS X) (σ : F.obj.obj (op U)) :
    F.obj.map (openSubspaceInclusion B S hS X U
      (largestOpenZeroSubspace B S hS X F U σ)).op σ = 0
```

**`AlgebraicGeometry.Space.SpacesEtale.largestOpenZeroSubspace_maximal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleZeroLocus.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleZeroLocus.lean#L320). The attribute's comment: “part (1): maximality”.

> **Stacks 04K9, part (1).** Every open subspace on which a section vanishes is contained in
> its largest open zero subspace.

```lean
theorem largestOpenZeroSubspace_maximal
    (F : Sheaf (topology B S hS X) AddCommGrpCat.{v})
    (U : SpacesEtale B S hS X) (σ : F.obj.obj (op U))
    (W : {W : Subfunctor (underlying B S hS X U).1 // IsOpenSubspace B S hS W})
    (hW : F.obj.map (openSubspaceInclusion B S hS X U W).op σ = 0) :
    W.1 ≤ (largestOpenZeroSubspace B S hS X F U σ).1
```

**`AlgebraicGeometry.Space.SpacesEtale.germ_eq_zero_iff_mem_largestOpenZeroSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleZeroLocus.lean, line 358](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleZeroLocus.lean#L358). The attribute's comment: “part (3): the geometric-point criterion”. References: SGA 2 XIV (1.8.2.1), “abelian, geom. point”.

> **Stacks 04K9, part (3).** The germ of a section at a geometric point of the algebraic
> space underlying an object `U` of the spaces-étale site of `X` vanishes in the spaces-étale
> stalk at the image of that point in `X` exactly when the point lies in the largest open zero
> subspace of the section.
>
> The colimit defining the stalk is filtered, so the germ vanishes exactly when the section
> already vanishes on some étale neighbourhood refining `U`; one direction is then the
> restriction criterion applied to such a refinement, and the other is the restriction
> criterion applied to the largest open zero subspace itself, which the field-valued point
> factors through by Tag 03IE.

```lean
theorem germ_eq_zero_iff_mem_largestOpenZeroSubspace
    (F : Sheaf (topology B S hS X) AddCommGrpCat.{v})
    (U : SpacesEtale B S hS X) (σ : F.obj.obj (op U))
    (p : GeometricPoint B S hS (underlying B S hS X U).1) :
    (spacesNeighborhoodSections (imageGeometricPoint B S hS X U p)
        (F.obj ⋙ forget AddCommGrpCat.{v})).ιColimitType
      (op (neighborhoodOfGeometricPoint B S hS X U p)) σ =
    (spacesNeighborhoodSections (imageGeometricPoint B S hS X U p)
        (F.obj ⋙ forget AddCommGrpCat.{v})).ιColimitType
      (op (neighborhoodOfGeometricPoint B S hS X U p)) (0 : F.obj.obj (op U)) ↔
      p.image ∈ openPoints B S hS X U (largestOpenZeroSubspace B S hS X F U σ)
```

**`AlgebraicGeometry.Space.SpacesEtale.exists_largestOpenZeroSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleZeroLocus.lean, line 448](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SpacesEtaleZeroLocus.lean#L448). References: SGA 2 XIV (1.8.2.1), “abelian, spaces”.

> **Stacks 04K9.** A section `σ` of an abelian sheaf on the spaces-étale site of an
> algebraic space `X`, over an object `U` of that site, has an open subspace `W` of the
> algebraic space underlying `U` such that: `σ` vanishes on `W` and `W` contains every open
> subspace on which `σ` vanishes; `σ` restricts to zero on an object of the site over `U`
> exactly when the image of its points lies in `W`; and the germ of `σ` at a geometric point of
> `U` vanishes in the spaces-étale stalk at its image in `X` exactly when that point lies in
> `W`.

```lean
theorem exists_largestOpenZeroSubspace
    (F : Sheaf (topology B S hS X) AddCommGrpCat.{v})
    (U : SpacesEtale B S hS X) (σ : F.obj.obj (op U)) :
    ∃ W : {W : Subfunctor (underlying B S hS X U).1 // IsOpenSubspace B S hS W},
      F.obj.map (openSubspaceInclusion B S hS X U W).op σ = 0 ∧
      (∀ W' : {W : Subfunctor (underlying B S hS X U).1 // IsOpenSubspace B S hS W},
        F.obj.map (openSubspaceInclusion B S hS X U W').op σ = 0 → W'.1 ≤ W.1) ∧
      (∀ (V : SpacesEtale B S hS X) (f : V ⟶ U),
        F.obj.map f.op σ = 0 ↔ ImageInOpen B S hS X (openPoints B S hS X U W) f) ∧
      (∀ p : GeometricPoint B S hS (underlying B S hS X U).1,
        (spacesNeighborhoodSections (imageGeometricPoint B S hS X U p)
            (F.obj ⋙ forget AddCommGrpCat.{v})).ιColimitType
          (op (neighborhoodOfGeometricPoint B S hS X U p)) σ =
        (spacesNeighborhoodSections (imageGeometricPoint B S hS X U p)
            (F.obj ⋙ forget AddCommGrpCat.{v})).ιColimitType
          (op (neighborhoodOfGeometricPoint B S hS X U p)) (0 : F.obj.obj (op U)) ↔
          p.image ∈ openPoints B S hS X U W)
```

## Tag 04KA, a definition

[Tag 04KA](https://stacks.math.columbia.edu/tag/04KA) in the Stacks Project.

**`AlgebraicGeometry.Space.supportOfSection`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafSupport.lean, line 418](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafSupport.lean#L418). The attribute's comment: “support of a section”. References: SGA 4 VIII (6.6), “support of a section”.

> The *support* of a section of an abelian sheaf on the small étale site of an algebraic
> space over an étale chart: the complement of the largest open on which the section restricts
> to zero.

```lean
abbrev supportOfSection (F : Sheaf (SmallEtale.topology B S hS X) AddCommGrpCat.{v})
    (U : SmallEtale B S hS X) (σ : F.obj.obj (op U)) :
    Set (points B S hS (yoneda.obj ((SmallEtale.toOver B S hS X).obj U)))
```

**`AlgebraicGeometry.Space.supportOfSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafSupport.lean, line 626](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafSupport.lean#L626). The attribute's comment: “support of a sheaf”. References: SGA 4 VIII (6.6), “support of a sheaf”.

> The *support* of an abelian sheaf on the small étale site of an algebraic space: the set
> of points at which the stalk at some geometric point lying over that point is nonzero, that is,
> at which the set-valued stalk is not a subsingleton.

```lean
def supportOfSheaf (F : Sheaf (SmallEtale.topology B S hS X) AddCommGrpCat.{v}) :
    Set (points B S hS X)
```

## Tag 04KB, a lemma

[Tag 04KB](https://stacks.math.columbia.edu/tag/04KB) in the Stacks Project.

**`AlgebraicGeometry.Space.isClosed_supportOfSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafSupport.lean, line 436](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafSupport.lean#L436). The attribute's comment: “closed\_section\_support”.

> The support of a section is closed.

```lean
theorem isClosed_supportOfSection
    (F : Sheaf (SmallEtale.topology B S hS X) AddCommGrpCat.{v})
    (U : SmallEtale B S hS X) (σ : F.obj.obj (op U)) :
    IsClosed (supportOfSection B S hS X F U σ)
```

**`AlgebraicGeometry.Space.supportOfSection_add_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafSupport.lean, line 494](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafSupport.lean#L494). The attribute's comment: “support\_sum”.

> The support of a sum is contained in the union of the supports.

```lean
theorem supportOfSection_add_subset
    (F : Sheaf (SmallEtale.topology B S hS X) AddCommGrpCat.{v})
    (U : SmallEtale B S hS X) (σ τ : F.obj.obj (op U)) :
    supportOfSection B S hS X F U (σ + τ) ⊆
      supportOfSection B S hS X F U σ ∪ supportOfSection B S hS X F U τ
```

**`AlgebraicGeometry.Space.supportOfSection_map_subset`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafSupport.lean, line 521](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafSupport.lean#L521). The attribute's comment: “support\_image\_section”.

> A morphism of abelian sheaves cannot enlarge the support of a section: the support of the
> image of `σ` under `φ` is contained in the support of `σ`.

```lean
theorem supportOfSection_map_subset
    {F G : Sheaf (SmallEtale.topology B S hS X) AddCommGrpCat.{v}} (φ : F ⟶ G)
    (U : SmallEtale B S hS X) (σ : F.obj.obj (op U)) :
    supportOfSection B S hS X G U (φ.hom.app (op U) σ) ⊆
      supportOfSection B S hS X F U σ
```

**`AlgebraicGeometry.Space.supportOfSheaf_subset_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafSupport.lean, line 644](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafSupport.lean#L644). The attribute's comment: “support\_injection”.

> The support of an abelian subsheaf is contained in the support of the ambient sheaf: a
> monomorphism `f : F ⟶ G` of abelian sheaves on the small étale site cannot enlarge the support
> of its source.

```lean
theorem supportOfSheaf_subset_of_mono (hX : IsAlgebraicSpace B S hS X)
    {F G : Sheaf (SmallEtale.topology B S hS X) AddCommGrpCat.{v}} (f : F ⟶ G) [Mono f] :
    supportOfSheaf B S hS X F ⊆ supportOfSheaf B S hS X G
```

**`AlgebraicGeometry.Space.supportOfSheaf_subset_of_injective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafSupportProperties.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafSupportProperties.lean#L161). The attribute's comment: “part (6): support along an injection”.

> **Stacks 04KB, part (6).** If a map of abelian sheaves on the small étale site of an
> algebraic space is injective on sections over every étale chart, then the support of its source
> is contained in the support of its target.
>
> Such a map is injective on every geometric stalk by Stacks 04K5, and an injection into a
> subsingleton has subsingleton source.
>
> The hypothesis is the sectionwise one, which is what a splitting of sheaves supplies.
> `AlgebraicGeometry.Space.supportOfSheaf_subset_of_mono` draws the same conclusion from a `Mono`
> instance in the sheaf category; neither hypothesis is the other, the passage between them being
> full faithfulness of `CategoryTheory.sheafToPresheaf` together with
> `CategoryTheory.NatTrans.mono_iff_mono_app`, so both forms are stated.

```lean
theorem supportOfSheaf_subset_of_injective (hX : IsAlgebraicSpace B S hS X)
    {F G : Sheaf (SmallEtale.topology B S hS X) AddCommGrpCat.{v}} (φ : F ⟶ G)
    (hφ : ∀ U : SmallEtale B S hS X, Function.Injective (φ.hom.app (op U))) :
    supportOfSheaf B S hS X F ⊆ supportOfSheaf B S hS X G
```

**`AlgebraicGeometry.Space.supportOfSheaf_eq_iUnion_image_supportOfSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafSupportSections.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafSupportSections.lean#L257). The attribute's comment: “sheaf\_support\_sections”.

> **Stacks 04KB, part (4).** The support of an abelian sheaf on the small étale site of an
> algebraic space is the union, over all étale charts and all sections on them, of the images of
> the supports of those sections.
>
> A point of the support carries a geometric point with a nonzero stalk, hence a neighbourhood
> and a section whose germ there is nonzero, and that section has the point of the chart in its
> support. Conversely a point in the support of a section is the image of a geometric point of
> the chart, whose germ there is then nonzero.

```lean
theorem supportOfSheaf_eq_iUnion_image_supportOfSection
    (F : Sheaf (SmallEtale.topology B S hS X) AddCommGrpCat.{v}) :
    supportOfSheaf B S hS X F =
      ⋃ U : SmallEtale B S hS X, ⋃ σ : F.obj.obj (op U),
        pointsMap B S hS (yoneda.obj ((SmallEtale.toOver B S hS X).obj U)) U.obj.hom ''
          supportOfSection B S hS X F U σ
```

**`AlgebraicGeometry.Space.supportOfSheaf_eq_iUnion_image_supportOfSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafSupportSections.lean, line 257](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafSupportSections.lean#L257). The attribute's comment: “part (4): the support of a sheaf is the union of the section supports”.

> **Stacks 04KB, part (4).** The support of an abelian sheaf on the small étale site of an
> algebraic space is the union, over all étale charts and all sections on them, of the images of
> the supports of those sections.
>
> A point of the support carries a geometric point with a nonzero stalk, hence a neighbourhood
> and a section whose germ there is nonzero, and that section has the point of the chart in its
> support. Conversely a point in the support of a section is the image of a geometric point of
> the chart, whose germ there is then nonzero.

```lean
theorem supportOfSheaf_eq_iUnion_image_supportOfSection
    (F : Sheaf (SmallEtale.topology B S hS X) AddCommGrpCat.{v}) :
    supportOfSheaf B S hS X F =
      ⋃ U : SmallEtale B S hS X, ⋃ σ : F.obj.obj (op U),
        pointsMap B S hS (yoneda.obj ((SmallEtale.toOver B S hS X).obj U)) U.obj.hom ''
          supportOfSection B S hS X F U σ
```

**`AlgebraicGeometry.Space.supportOfSheaf_subset_of_isLocallySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafSupportSections.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafSupportSections.lean#L300). The attribute's comment: “part (5): support along a surjection”.

> **Stacks 04KB.** A surjection of abelian sheaves on the small étale site of an algebraic
> space does not enlarge the support: the support of the target is contained in the support of
> the source.
>
> A surjection of sheaves is surjective on every geometric stalk by Stacks 04K5, so a point at
> which the stalk of the source is a subsingleton is one at which the stalk of the target is one
> too.

```lean
theorem supportOfSheaf_subset_of_isLocallySurjective
    {F G : Sheaf (SmallEtale.topology B S hS X) AddCommGrpCat.{v}} (a : F ⟶ G)
    [Sheaf.IsLocallySurjective a] :
    supportOfSheaf B S hS X G ⊆ supportOfSheaf B S hS X F
```

## Tag 04KC, a lemma

[Tag 04KC](https://stacks.math.columbia.edu/tag/04KC) in the Stacks Project.

**`AlgebraicGeometry.Space.isClosed_supportOfSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafSupportProperties.lean, line 303](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafSupportProperties.lean#L303).

> **Stacks 04KC.** The support of a sheaf of rings on the small étale site of an algebraic
> space is closed.
>
> The support is the set of points of the space at which the stalk of the underlying abelian
> sheaf at some geometric point is nonzero; for a sheaf of rings that is the set of points at
> which the ring of germs is not the zero ring, since a ring vanishes exactly when its unit
> does. Its complement is exhibited as the image of the maximal open zero locus of the unit
> section of a surjective étale atlas, which is open because an étale chart is open on points
> by clause (3) of Stacks 03BX.

```lean
theorem isClosed_supportOfSheaf (hX : IsAlgebraicSpace B S hS X) :
    IsClosed (supportOfSheaf B S hS X (toAddCommGrp B S hS X R))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.20, Tag 04K7](https://stacks.math.columbia.edu/tag/04K7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
