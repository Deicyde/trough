---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.schematicLocus, AlgebraicGeometry.Space.exists_isGreatest_isOpenSubspace_isRepresentable, AlgebraicGeometry.Space.denseRange_schematicLocus_of_isZariskiLocallyQuasiSeparatedOver, AlgebraicGeometry.Space.isOpenSubspace_and_isRepresentable_schematicLocus_of_isAlgebraicSpace, AlgebraicGeometry.Space.mem_range_pointsMap_schematicLocus_iff, AlgebraicGeometry.Space.le_schematicLocus, AlgebraicGeometry.Space.codimensionZero_mem_schematicLocus, AlgebraicGeometry.Space.denseRange_schematicLocus
statement: formalized
proof: formalized
---

# 66.13 The schematic locus

Section 66.13 of the Stacks Project, [Tag 03JG](https://stacks.math.columbia.edu/tag/03JG). 4 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03JG, the section

[Tag 03JG](https://stacks.math.columbia.edu/tag/03JG) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.schematicLocus`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/OpenSubspace.lean#L41), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/SchematicLocusSection.lean, line 31](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SchematicLocusSection.lean#L31) (StacksFrontier): “the schematic locus”.
- [`AlgebraicGeometry.Space.exists_isGreatest_isOpenSubspace_isRepresentable`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DenseSchematicLocusEquivalence.lean#L91), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/SchematicLocusSection.lean, line 32](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SchematicLocusSection.lean#L32) (StacksFrontier): “a largest open subspace which is a scheme”.
- [`AlgebraicGeometry.Space.denseRange_schematicLocus_of_isZariskiLocallyQuasiSeparatedOver`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiLocallyQuasiSeparatedSchematicLocus.lean#L85), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/SchematicLocusSection.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SchematicLocusSection.lean#L34) (StacksFrontier): “density of the schematic locus for quasi-separated spaces”.

## Tag 03JH, a lemma

[Tag 03JH](https://stacks.math.columbia.edu/tag/03JH) in the Stacks Project.

**`AlgebraicGeometry.Space.isOpenSubspace_and_isRepresentable_schematicLocus_of_isAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DenseSchematicLocusEquivalence.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DenseSchematicLocusEquivalence.lean#L67). The attribute's comment: “openness and representability”.

> The schematic locus of an algebraic space over `S` is an open subspace and is
> representable.

```lean
theorem isOpenSubspace_and_isRepresentable_schematicLocus_of_isAlgebraicSpace
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X) :
    IsOpenSubspace B S hS (schematicLocus B S hS X) ∧
      (schematicLocus B S hS X).toFunctor.IsRepresentable
```

**`AlgebraicGeometry.Space.exists_isGreatest_isOpenSubspace_isRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DenseSchematicLocusEquivalence.lean, line 91](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DenseSchematicLocusEquivalence.lean#L91).

> An algebraic space `X` over a scheme `S` has a largest open subspace which is a scheme: the
> set of open subspaces of `X` that are represented by a scheme over `S` has a greatest element.

```lean
theorem exists_isGreatest_isOpenSubspace_isRepresentable
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X) :
    ∃ X' : Subfunctor X, IsGreatest
      {G : Subfunctor X | IsOpenSubspace B S hS G ∧ G.toFunctor.IsRepresentable} X'
```

**`AlgebraicGeometry.Space.mem_range_pointsMap_schematicLocus_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeSchematicLocus.lean, line 196](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeSchematicLocus.lean#L196). The attribute's comment: “points of the schematic locus”.

> A point of a presheaf lies in the point set of the schematic locus of Tag 03JH exactly
> when it lies in the point set of one representable open subspace.
>
> The schematic locus is the supremum of the representable open subspaces, and the supremum of
> subfunctors is the object-wise union, so a field-valued point of it takes its value in one
> member of the family.

```lean
theorem mem_range_pointsMap_schematicLocus_iff
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (y : points B S hS F) :
    y ∈ Set.range (pointsMap B S hS (schematicLocus B S hS F).toFunctor
        (schematicLocus B S hS F).ι) ↔
      ∃ G : Subfunctor F, IsOpenSubspace B S hS G ∧ G.toFunctor.IsRepresentable ∧
        y ∈ Set.range (pointsMap B S hS G.toFunctor G.ι)
```

**`AlgebraicGeometry.Space.schematicLocus`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/OpenSubspace.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/OpenSubspace.lean#L41). The attribute's comment: “schematic locus”.

> The schematic locus of `F`: the union of all open subspaces of `F` which are represented
> by a scheme over `S`.

```lean
def schematicLocus (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) : Subfunctor F
```

**`AlgebraicGeometry.Space.le_schematicLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/OpenSubspace.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/OpenSubspace.lean#L47). The attribute's comment: “maximality”.

> Every open subspace which is represented by a scheme over `S` is contained in the
> schematic locus.

```lean
theorem le_schematicLocus (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (G : Subfunctor F)
    (hG : IsOpenSubspace B S hS G) (hGrep : G.toFunctor.IsRepresentable) :
    G ≤ schematicLocus B S hS F
```

## Tag 0BAS, a lemma

[Tag 0BAS](https://stacks.math.columbia.edu/tag/0BAS) in the Stacks Project.

**`AlgebraicGeometry.Space.codimensionZero_mem_schematicLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteEtaleSchematicLocus.lean, line 341](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteEtaleSchematicLocus.lean#L341). The attribute's comment: “codimension-zero points”.

> **Stacks 0BAS, codimension-zero points.** If an algebraic space over `S` admits a finite,
> étale, surjective morphism from an object of the site whose underlying scheme is
> quasi-separated, then every point of codimension zero lies in the schematic locus of
> Tag 03JH.

```lean
theorem codimensionZero_mem_schematicLocus (hF : IsAlgebraicSpace B S hS F)
    (hcover : ∃ (U : BigFppfOver B S hS) (q : yoneda.obj U ⟶ F),
      QuasiSeparatedSpace ((BigFppfOver.toScheme B S hS).obj U) ∧
      IsFinite B S hS q ∧ IsEtale B S hS q ∧ IsSurjective B S hS q)
    (x : points B S hS F) (hx : localRingDimension B S hS x = 0) :
    x ∈ Set.range (pointsMap B S hS (schematicLocus B S hS F).toFunctor
      (schematicLocus B S hS F).ι)
```

**`AlgebraicGeometry.Space.denseRange_schematicLocus`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteEtaleSchematicLocus.lean, line 357](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FiniteEtaleSchematicLocus.lean#L357). The attribute's comment: “density”.

> **Stacks 0BAS, density.** If an algebraic space over `S` admits a finite, étale, surjective
> morphism from an object of the site whose underlying scheme is quasi-separated, then the
> schematic locus of Tag 03JH is dense in its space of points.

```lean
theorem denseRange_schematicLocus (hF : IsAlgebraicSpace B S hS F)
    (hcover : ∃ (U : BigFppfOver B S hS) (q : yoneda.obj U ⟶ F),
      QuasiSeparatedSpace ((BigFppfOver.toScheme B S hS).obj U) ∧
      IsFinite B S hS q ∧ IsEtale B S hS q ∧ IsSurjective B S hS q) :
    DenseRange (pointsMap B S hS (schematicLocus B S hS F).toFunctor
      (schematicLocus B S hS F).ι)
```

## Tag 06NH, a proposition

[Tag 06NH](https://stacks.math.columbia.edu/tag/06NH) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_denseRange_isRepresentable_isOpenSubspace_codimensionZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiLocallyQuasiSeparatedCodimensionZero.lean, line 287](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiLocallyQuasiSeparatedCodimensionZero.lean#L287).

> **Stacks 06NH.** A Zariski locally quasi-separated algebraic space over `S` — for instance
> a quasi-separated one — has a dense open subspace which is a scheme, and every point of
> codimension `0` of the space lies in that subspace. The subspace is the schematic locus of
> Tag 03JH.
>
> Zariski local quasi-separatedness is the absolute notion of Tag 03BS part (4), as in the
> source; by Tag 03W7 it is equivalent to the notion over `S`, which is how the proof uses it. The
> containment `hZ` of the terminal scheme in the site is the argument of that absolute notion; it
> holds in every big fppf site, by `AlgebraicGeometry.BigFppfSite.contains_terminal`.

```lean
theorem exists_denseRange_isRepresentable_isOpenSubspace_codimensionZero
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    (hqs : IsAbsolutelyZariskiLocallyQuasiSeparated B S hS hZ F) :
    ∃ G : Subfunctor F, IsOpenSubspace B S hS G ∧ G.toFunctor.IsRepresentable ∧
      DenseRange (pointsMap B S hS G.toFunctor G.ι) ∧
      ∀ x : points B S hS F, localRingDimension B S hS x = 0 →
        x ∈ Set.range (pointsMap B S hS G.toFunctor G.ι)
```

**`AlgebraicGeometry.Space.denseRange_schematicLocus_of_isZariskiLocallyQuasiSeparatedOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiLocallyQuasiSeparatedSchematicLocus.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiLocallyQuasiSeparatedSchematicLocus.lean#L85). The attribute's comment: “density”.

> The schematic locus of a Zariski locally quasi-separated algebraic space over `S` is dense
> in its space of points; so that space has a dense open subspace which is a scheme.

```lean
theorem denseRange_schematicLocus_of_isZariskiLocallyQuasiSeparatedOver
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    (hqs : IsZariskiLocallyQuasiSeparatedOver B S hS F) :
    DenseRange (pointsMap B S hS (schematicLocus B S hS F).toFunctor
      (schematicLocus B S hS F).ι)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 66.13, Tag 03JG](https://stacks.math.columbia.edu/tag/03JG)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
