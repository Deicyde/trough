---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.presheaf_of_isFiniteLocallyFree, AlgebraicGeometry.Space.presheaf_iff_isFiniteLocallyFree_iff_chartComparison, AlgebraicGeometry.Space.presheaf_iff_isFiniteLocallyFree, AlgebraicGeometry.Space.isFiniteLocallyFree_presheaf_iff_isFiniteLocallyFree, AlgebraicGeometry.Space.IsFiniteLocallyFree, AlgebraicGeometry.Space.IsFiniteLocallyFreeOfRank, AlgebraicGeometry.Space.isFiniteLocallyFree_iff_exists_etaleChart, AlgebraicGeometry.Space.isFiniteLocallyFree_iff_exists_zariskiCover
statement: formalized
proof: formalized
---

# 67.46 Finite locally free morphisms

Section 67.46 of the Stacks Project, [Tag 03ZT](https://stacks.math.columbia.edu/tag/03ZT). 6 tags here are carried by 17 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03ZU, a lemma

[Tag 03ZU](https://stacks.math.columbia.edu/tag/03ZU) in the Stacks Project.

**`AlgebraicGeometry.Space.presheaf_of_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChartComparisonAssembly.lean, line 255](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ChartComparisonAssembly.lean#L255). The attribute's comment: “the only if direction: finite locally free in the sense of 03ZV implies every represented base change is a finite locally free morphism of schemes”.

> **Stacks 03ZU, the "only if" direction.**  A representable morphism `f : X ⟶ Y` of algebraic
> spaces over `S` which is finite locally free in the sense of Stacks 03ZV — affine with `f_*𝒪_X`
> a finite locally free `𝒪_Y`-module — is finite locally free in the sense of Section 03HA: every
> represented base change of `f` is a finite locally free morphism of schemes.
>
> This is `AlgebraicGeometry.Space.presheaf_of_isFiniteLocallyFree_of_chartComparison_at` with its
> hypothesis `hcross` discharged by
> `AlgebraicGeometry.Space.isFiniteLocallyFree_baseChangeChartHom_of_isFiniteLocallyFreeOnSite`,
> at an étale chart whose structure morphism is surjective on points; one exists by
> `AlgebraicGeometry.Space.exists_surjective_smallEtale_chart`.  The affineness that the chart
> comparison consumes is the first conjunct of Stacks 03ZV, so nothing is assumed beyond it.

```lean
theorem presheaf_of_isFiniteLocallyFree (f : X ⟶ Y)
    (hrep : yoneda.relativelyRepresentable f.hom) (h : IsFiniteLocallyFree B S hS f) :
    (MorphismProperty.inverseImage
      (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f.hom
```

**`AlgebraicGeometry.Space.presheaf_iff_isFiniteLocallyFree_iff_chartComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeRepresentable.lean, line 256](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeRepresentable.lean#L256). The attribute's comment: “the reduction of the biconditional to the chart comparison: proved unconditionally, that f is finite locally free in the sense of Section 03HA if and only if it is affine with finite locally free pushforward, holds exactly when the chart comparison holds at a surjective etale chart. The biconditional itself is AlgebraicGeometry.Space .presheaf\_iff\_isFiniteLocallyFree, which discharges that chart comparison”.

> **The equivalence of Stacks 03ZU for a morphism is equivalent to the chart comparison for
> that morphism.** For a representable `f : X ⟶ Y` and an étale chart `V` of `Y` whose structure
> morphism is surjective on points, the assertion of Stacks 03ZU for `f` holds exactly when the
> scheme-level finite local freeness of the base change of `f` over `V` agrees with affineness of
> `f` together with finite local freeness of the restriction of `f_*𝒪_X` to the slice at `V`.
>
> This statement carries no hypothesis.  It says that the chart comparison is not merely one
> sufficient input for Stacks 03ZU but is equivalent to it, so that nothing is lost by reducing
> the tag to a statement at a single chart.  Affineness appears on the right-hand side because
> the module conjunct alone does not bound the morphism; it cannot be dropped, as the
> implementation notes record.
>
> Its `@[stacks 03ZU]` attribute is clause-labelled for the reduction alone: it is an equivalence
> between Stacks 03ZU and a chart statement, not Stacks 03ZU.  The chart statement is proved, and
> with it the biconditional, in
> `StacksFrontier.AlgebraicGeometry.Spaces.FiniteLocallyFreeRepresentableChart`.

```lean
theorem presheaf_iff_isFiniteLocallyFree_iff_chartComparison (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f.hom)
    (V : (smallEtaleRingedSite B S hS Y.1 Y.2).C) (hV : IsSurjective B S hS V.1.hom) :
    (((MorphismProperty.inverseImage
          (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf f.hom ↔
        IsFiniteLocallyFree B S hS f) ↔
      (Stacks.Morphisms.IsFiniteLocallyFree
          ((BigFppfOver.toScheme B S hS).map (hf.snd V.1.hom)) ↔
        (IsAffineHom B S hS f.hom ∧
          SheafOfModules.IsFiniteLocallyFreeOnSite
            (R := (Stacks.SheafOfModules.Tensor.ringSheaf
              (smallEtaleRingedSite B S hS Y.1 Y.2).O).over V)
            ((pushforwardStructureModule B S hS f).over V))))
```

**`AlgebraicGeometry.Space.presheaf_iff_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeRepresentableChart.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeRepresentableChart.lean#L136).

> Let `S` be a scheme and let `f : X ⟶ Y` be a representable morphism of algebraic spaces over
> `S`.  Then `f` is finite locally free in the sense of Section 03HA — every represented base change
> of `f` is a finite locally free morphism of schemes — if and only if `f` is affine and the sheaf
> `f_*𝒪_X` is a finite locally free `𝒪_Y`-module, which is the definition of Stacks 03ZV,
> `AlgebraicGeometry.Space.IsFiniteLocallyFree`.

```lean
theorem presheaf_iff_isFiniteLocallyFree (f : X ⟶ Y)
    (hf : yoneda.relativelyRepresentable f.hom) :
    (MorphismProperty.inverseImage
        (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf f.hom ↔
      IsFiniteLocallyFree B S hS f
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.isFiniteLocallyFree_presheaf_iff_isFiniteLocallyFree`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeCondition2.lean#L125), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeRepresentableIff.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeRepresentableIff.lean#L167) (StacksFrontier).

## Tag 03ZV, a definition

[Tag 03ZV](https://stacks.math.columbia.edu/tag/03ZV) in the Stacks Project.

**`AlgebraicGeometry.Space.IsFiniteLocallyFree`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFree.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFree.lean#L88). The attribute's comment: “finite locally free”.

> **Stacks 03ZV.** A morphism of algebraic spaces is *finite locally free* when it is
> affine and the direct image of the structure sheaf of its source is a finite locally free
> module on the small étale ringed site of its target.

```lean
noncomputable abbrev IsFiniteLocallyFree (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.Space.IsFiniteLocallyFreeOfRank`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFree.lean, line 95](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFree.lean#L95). The attribute's comment: “rank or degree”.

> **Stacks 03ZV.** A finite locally free morphism of algebraic spaces has *rank* (or
> *degree*) `r` when the direct image of the structure sheaf of its source has rank `r`.

```lean
noncomputable abbrev IsFiniteLocallyFreeOfRank (f : X ⟶ Y) (r : ℕ) : Prop
```

## Tag 03ZW, a lemma

[Tag 03ZW](https://stacks.math.columbia.edu/tag/03ZW) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiniteLocallyFree_presheaf_iff_isFiniteLocallyFree`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeCondition2.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeCondition2.lean#L125). The attribute's comment: “conditions (1) and (2)”.

> **Stacks 03ZW, conditions (1) and (2).** A morphism of algebraic spaces over `S` is
> representable with every represented base change a finite locally free morphism of schemes
> exactly when it is finite locally free in the sense of Stacks 03ZV.
>
> No representability hypothesis is imposed, which is what distinguishes this from Stacks 03ZU,
> `AlgebraicGeometry.Space.presheaf_iff_isFiniteLocallyFree`: from condition (1) representability
> is `CategoryTheory.MorphismProperty.relative.rep`, and from condition (2) it is
> `AlgebraicGeometry.Space.relativelyRepresentable_of_isFiniteLocallyFree`.

```lean
theorem isFiniteLocallyFree_presheaf_iff_isFiniteLocallyFree (f : X ⟶ Y) :
    (MorphismProperty.inverseImage
        (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf f.hom ↔
      IsFiniteLocallyFree B S hS f
```

**`AlgebraicGeometry.Space.isFiniteLocallyFree_iff_exists_etaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeCondition2.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeCondition2.lean#L143). The attribute's comment: “conditions (2) and (3)”.

> **Stacks 03ZW, conditions (2) and (3).** A morphism of algebraic spaces over `S` is finite
> locally free in the sense of Stacks 03ZV exactly when there is one surjective étale morphism from
> a representable presheaf onto its target along which its base change is representable and finite
> locally free.
>
> This is `AlgebraicGeometry.Space.isFiniteLocallyFree_presheaf_iff_isFiniteLocallyFree` composed
> with `AlgebraicGeometry.Space.isFiniteLocallyFree_presheaf_iff_exists_etaleChart`, conditions (1)
> and (3).

```lean
theorem isFiniteLocallyFree_iff_exists_etaleChart (f : X ⟶ Y) :
    IsFiniteLocallyFree B S hS f ↔
      ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y.1),
        (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf g ∧
        (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf g ∧
        (MorphismProperty.inverseImage
          (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf (pullback.snd f.hom g)
```

**`AlgebraicGeometry.Space.isFiniteLocallyFree_iff_exists_zariskiCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeCondition2.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeCondition2.lean#L164). The attribute's comment: “conditions (2) and (4)”.

> **Stacks 03ZW, conditions (2) and (4).** A morphism of algebraic spaces over `S` is finite
> locally free in the sense of Stacks 03ZV exactly when there is a Zariski covering `Y = ⋃ Yᵢ` of
> its target such that each `f⁻¹(Yᵢ) ⟶ Yᵢ` is representable and finite locally free.
>
> This is `AlgebraicGeometry.Space.isFiniteLocallyFree_presheaf_iff_isFiniteLocallyFree` composed
> with `AlgebraicGeometry.Space.isFiniteLocallyFree_presheaf_iff_exists_zariskiCover`, conditions
> (1) and (4).

```lean
theorem isFiniteLocallyFree_iff_exists_zariskiCover (f : X ⟶ Y) :
    IsFiniteLocallyFree B S hS f ↔
      ∃ (I : Type u) (U : I → Subfunctor Y.1),
        IsZariskiCover B S hS I U ∧
        ∀ i, (MorphismProperty.inverseImage
          (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf (pullback.snd f.hom (U i).ι)
```

**`AlgebraicGeometry.Space.isFiniteLocallyFree_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeCondition2.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeCondition2.lean#L193).

> **Stacks 03ZW.** For a morphism `f : X ⟶ Y` of algebraic spaces over `S` the following are
> equivalent:
>
> 1. `f` is representable and finite locally free, i.e. every represented base change of `f` is a
>    finite locally free morphism of schemes;
> 2. `f` is finite locally free in the sense of Stacks 03ZV: affine, with `f_*𝒪_X` a finite
>    locally free `𝒪_Y`-module;
> 3. there exists a scheme `V` and a surjective étale morphism `V ⟶ Y` such that
>    `V ×_Y X ⟶ V` is (representable and) finite locally free;
> 4. there exists a Zariski covering `Y = ⋃ Yᵢ` such that each `f⁻¹(Yᵢ) ⟶ Yᵢ` is (representable
>    and) finite locally free.
>
> Assembled from the pairwise equivalences
> `AlgebraicGeometry.Space.isFiniteLocallyFree_presheaf_iff_isFiniteLocallyFree`,
> `AlgebraicGeometry.Space.isFiniteLocallyFree_iff_exists_etaleChart` and
> `AlgebraicGeometry.Space.isFiniteLocallyFree_iff_exists_zariskiCover`.

```lean
theorem isFiniteLocallyFree_tfae (f : X ⟶ Y) :
    List.TFAE
      [(MorphismProperty.inverseImage
          (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf f.hom,
        IsFiniteLocallyFree B S hS f,
        ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y.1),
          (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
            (BigFppfOver.toScheme B S hS)).presheaf g ∧
          (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
            (BigFppfOver.toScheme B S hS)).presheaf g ∧
          (MorphismProperty.inverseImage
            (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
            (BigFppfOver.toScheme B S hS)).presheaf (pullback.snd f.hom g),
        ∃ (I : Type u) (U : I → Subfunctor Y.1),
          IsZariskiCover B S hS I U ∧
          ∀ i, (MorphismProperty.inverseImage
            (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
            (BigFppfOver.toScheme B S hS)).presheaf (pullback.snd f.hom (U i).ι)]
```

**`AlgebraicGeometry.Space.isFiniteLocallyFree_presheaf_iff_exists_etaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeEtaleLocal.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeEtaleLocal.lean#L292). The attribute's comment: “conditions (1) and (3)”.

> **Stacks 03ZW, conditions (1) and (3).** A morphism of algebraic spaces over `S` is
> representable and finite locally free exactly when there is one surjective étale morphism from a
> representable presheaf onto its target along which its base change is representable and finite
> locally free.

```lean
theorem isFiniteLocallyFree_presheaf_iff_exists_etaleChart
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    (MorphismProperty.inverseImage
        (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf f ↔
      ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
        (MorphismProperty.inverseImage (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf g ∧
        (MorphismProperty.inverseImage (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf g ∧
        (MorphismProperty.inverseImage
          (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf (pullback.snd f g)
```

**`AlgebraicGeometry.Space.isFiniteLocallyFree_presheaf_iff_exists_zariskiCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeZariskiCover.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeZariskiCover.lean#L64). The attribute's comment: “conditions (1) and (4)”.

> **Stacks 03ZW, conditions (1) and (4).** A morphism of algebraic spaces over `S` is
> representable and finite locally free exactly when there is a Zariski covering `Y = ⋃ Yᵢ` of its
> target such that each `f⁻¹(Yᵢ) ⟶ Yᵢ` is.
>
> This is the equivalence the source obtains from the fact that being finite locally free is
> Zariski local on the target, which it notes is a weakening of the fpqc locality established
> along the way to conditions (1) and (3).  Here it is
> `AlgebraicGeometry.Space.presheaf_tfae` — Stacks 03M4 for an arbitrary property of scheme
> morphisms Zariski local at the target — instantiated at finite local freeness: the restriction
> `f⁻¹(Yᵢ) ⟶ Yᵢ` is read, as the source reads it, as the base change of `f` along the inclusion of
> the open subspace `Yᵢ`, and both sides are read in the representable sense of condition (1).

```lean
theorem isFiniteLocallyFree_presheaf_iff_exists_zariskiCover
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    (MorphismProperty.inverseImage
        (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf f ↔
      ∃ (I : Type u) (U : I → Subfunctor Y),
        IsZariskiCover B S hS I U ∧
        ∀ i, (MorphismProperty.inverseImage
          (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS)).presheaf (pullback.snd f (U i).ι)
```

## Tag 03ZX, a lemma

[Tag 03ZX](https://stacks.math.columbia.edu/tag/03ZX) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiniteLocallyFree_presheaf_isStableUnderComposition`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeComp.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeComp.lean#L70). The attribute's comment: “stability under composition”.

> Being representable and finite locally free is a composition-stable class of morphisms of
> presheaves on the big fppf site of `S`.

```lean
instance isFiniteLocallyFree_presheaf_isStableUnderComposition :
    (MorphismProperty.inverseImage
      (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf.IsStableUnderComposition
```

**`AlgebraicGeometry.Space.isFiniteLocallyFree_presheaf_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeComp.lean, line 79](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeComp.lean#L79).

> The composition of representable finite locally free morphisms of algebraic spaces over `S`
> is representable and finite locally free.

```lean
theorem isFiniteLocallyFree_presheaf_comp
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : (MorphismProperty.inverseImage
      (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f)
    (hg : (MorphismProperty.inverseImage
      (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf g) :
    (MorphismProperty.inverseImage
      (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf (f ≫ g)
```

## Tag 03ZY, a lemma

[Tag 03ZY](https://stacks.math.columbia.edu/tag/03ZY) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiniteLocallyFree_presheaf_isStableUnderBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeBaseChange.lean, line 110](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeBaseChange.lean#L110). The attribute's comment: “stability under base change”.

> **Stacks 03ZY.** Being representable and finite locally free is a base-change stable class
> of morphisms of presheaves on the big fppf site of `S`.

```lean
instance isFiniteLocallyFree_presheaf_isStableUnderBaseChange :
    (MorphismProperty.inverseImage
      (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf.IsStableUnderBaseChange
```

**`AlgebraicGeometry.Space.isFiniteLocallyFree_presheaf_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeBaseChange.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeBaseChange.lean#L120).

> **Stacks 03ZY.** A base change of a representable finite locally free morphism of algebraic
> spaces over `S` is representable and finite locally free: if `f'` sits in a Cartesian square
> over `f`, then `f'` is finite locally free as soon as `f` is.

```lean
theorem isFiniteLocallyFree_presheaf_of_isPullback
    {X Y X' Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {f : X ⟶ Y} {g : Y' ⟶ Y} {k : X' ⟶ X} {f' : X' ⟶ Y'} (sq : IsPullback k f' f g)
    (hf : (MorphismProperty.inverseImage
      (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f) :
    (MorphismProperty.inverseImage
      (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf f'
```

## Tag 0416, a lemma

[Tag 0416](https://stacks.math.columbia.edu/tag/0416) in the Stacks Project.

**`AlgebraicGeometry.Space.isFiniteLocallyFree_presheaf_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeFiniteFlat.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeFiniteFlat.lean#L174). The attribute's comment: “conditions (1) and (2), finite local freeness in the representable sense”.

> **Stacks 0416, conditions (1) and (2).** A morphism of algebraic spaces over `S` is
> representable and finite locally free exactly when it is finite, flat and locally of finite
> presentation.
>
> Both sides are conditions on the represented base changes of the morphism, so this is the
> scheme-level equivalence Stacks 02KB applied to one represented base change at a time.

```lean
theorem isFiniteLocallyFree_presheaf_iff (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    (MorphismProperty.inverseImage
        (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf f ↔
      IsFinite B S hS f ∧ IsFlat B S hS f ∧ IsLocallyOfFinitePresentation B S hS f
```

**`AlgebraicGeometry.Space.isFiniteLocallyFree_presheaf_iff_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeFiniteFlat.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FiniteLocallyFreeFiniteFlat.lean#L206). The attribute's comment: “condition (3) over a locally Noetherian target”.

> **Stacks 0416, condition (3).** A morphism of algebraic spaces over `S` with locally
> Noetherian target is representable and finite locally free exactly when it is finite and flat.
>
> A finite morphism is locally of finite type, hence locally of finite presentation over a locally
> Noetherian target by Stacks 06G4, part (1), so the finite presentation condition of conditions
> (1) and (2) is automatic.

```lean
theorem isFiniteLocallyFree_presheaf_iff_of_isLocallyNoetherian
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hN : HasEtaleLocalProperty B S hS Y (fun T : Scheme.{u} => IsLocallyNoetherian T)) :
    (MorphismProperty.inverseImage
        (@Stacks.Morphisms.IsFiniteLocallyFree.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS)).presheaf f ↔
      IsFinite B S hS f ∧ IsFlat B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.46, Tag 03ZT](https://stacks.math.columbia.edu/tag/03ZT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
