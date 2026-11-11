---
declaration: section
origin: cited
lean: AlgebraicGeometry.isPushout_opens_ι_of_sup_eq_top, AlgebraicGeometry.existsUnique_comp_ι_eq_of_sup_eq_top, AlgebraicGeometry.opensRange_pushout_inl_sup_opensRange_pushout_inr, AlgebraicGeometry.preimage_opensRange_pushout_inl, AlgebraicGeometry.isPullback_pushout_inl_inr, AlgebraicGeometry.LocallyRingedSpace.GlueData.range_overlap, AlgebraicGeometry.LocallyRingedSpace.GlueData.t_f_eq_restrictOverlapIso_comp, AlgebraicGeometry.LocallyRingedSpace.GlueData.homOutEquiv
statement: formalized
proof: formalized
---

# 26.14 Glueing schemes

Section 26.14 of the Stacks Project, [Tag 01JA](https://stacks.math.columbia.edu/tag/01JA). 5 tags here are carried by 50 declarations of the repository (all in StacksFrontier) and 10 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01JA, the section

[Tag 01JA](https://stacks.math.columbia.edu/tag/01JA) in the Stacks Project.

**`AlgebraicGeometry.isPushout_opens_ι_of_sup_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/OpenImmersionPushout.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/OpenImmersionPushout.lean#L88). The attribute's comment: “the two-chart glueing as a pushout square of schemes”.

> A scheme covered by two opens is glued from them: the square formed by the two inclusions of
> the intersection and the two inclusions into the ambient scheme is a pushout square.

```lean
theorem isPushout_opens_ι_of_sup_eq_top {S : Scheme.{u}} {U V : S.Opens} (h : U ⊔ V = ⊤) :
    IsPushout (S.homOfLE inf_le_left) (S.homOfLE inf_le_right) U.ι V.ι
```

**`AlgebraicGeometry.existsUnique_comp_ι_eq_of_sup_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/OpenImmersionPushout.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/OpenImmersionPushout.lean#L119). The attribute's comment: “the two-chart case of the mapping property for morphisms out of a glueing”.

> The mapping property for morphisms out of a glueing with two charts: if the opens `U, V` of a
> scheme `S` satisfy `U ⊔ V = ⊤`, then a morphism out of `S` is the same thing as a pair of
> morphisms out of `U` and out of `V` agreeing on `U ⊓ V`.

```lean
theorem existsUnique_comp_ι_eq_of_sup_eq_top {S T : Scheme.{u}} {U V : S.Opens}
    (h : U ⊔ V = ⊤) {a : U.toScheme ⟶ T} {b : V.toScheme ⟶ T}
    (w : S.homOfLE inf_le_left ≫ a = S.homOfLE inf_le_right ≫ b) :
    ∃! m : S ⟶ T, U.ι ≫ m = a ∧ V.ι ≫ m = b
```

**`AlgebraicGeometry.opensRange_pushout_inl_sup_opensRange_pushout_inr`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/OpenImmersionPushout.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/OpenImmersionPushout.lean#L136). The attribute's comment: “the two-chart case of part (1): the charts cover the glued scheme”.

> The two charts of the scheme obtained by glueing `X` and `Y` along a span of open immersions
> cover it.

```lean
theorem opensRange_pushout_inl_sup_opensRange_pushout_inr :
    (pushout.inl f g).opensRange ⊔ (pushout.inr f g).opensRange = ⊤
```

**`AlgebraicGeometry.preimage_opensRange_pushout_inl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/OpenImmersionPushout.lean, line 152](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/OpenImmersionPushout.lean#L152). The attribute's comment: “the two-chart case of part (2): the overlap of the two charts”.

> Inside the second chart of the scheme obtained by glueing `X` and `Y` along a span of open
> immersions, the overlap with the first chart is exactly the image of the span's vertex.

```lean
theorem preimage_opensRange_pushout_inl :
    (pushout.inr f g) ⁻¹ᵁ (pushout.inl f g).opensRange = g.opensRange
```

**`AlgebraicGeometry.isPullback_pushout_inl_inr`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/OpenImmersionPushout.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/OpenImmersionPushout.lean#L169). The attribute's comment: “the two-chart case of part (2), as a cartesian square”.

> The pushout square of a span of open immersions of schemes is also cartesian: the span's
> vertex is the intersection of the two charts of the glued scheme.

```lean
theorem isPullback_pushout_inl_inr :
    IsPullback f g (pushout.inl f g) (pushout.inr f g)
```

## Tag 01JB, a lemma

[Tag 01JB](https://stacks.math.columbia.edu/tag/01JB) in the Stacks Project.

**`AlgebraicGeometry.LocallyRingedSpace.GlueData.range_overlap`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean, line 94](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean#L94). The attribute's comment: “part (2): the overlap is the intersection of two charts”.

> The prescribed overlap `V i j`, viewed inside the chart `U i` through `D.f i j`, is exactly
> the part of that chart lying over the chart `U j`: `φ i '' U i j = U i ∩ U j` in the glued
> space, stated as an equality of subsets of `U i`.

```lean
lemma range_overlap (D : LocallyRingedSpace.GlueData.{u}) (i j : D.J) :
    Set.range (D.f i j).base = (D.ι i).base ⁻¹' Set.range (D.ι j).base
```

**`AlgebraicGeometry.LocallyRingedSpace.GlueData.t_f_eq_restrictOverlapIso_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean, line 133](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean#L133). The attribute's comment: “part (3): the transition map is the restriction of φ j⁻¹ ∘ φ i”.

> The transition map is `φ j⁻¹ ∘ φ i` on the overlap: for any morphism `s : U i ∩ U j ⟶ U j`
> with `s ≫ φ j` the inclusion of `U i ∩ U j` (the restriction of `φ j⁻¹` to `U i ∩ U j`), the
> map `φ i j`, read in the chart `U j`, is `s` composed with the restriction isomorphism.

```lean
theorem t_f_eq_restrictOverlapIso_comp (D : LocallyRingedSpace.GlueData.{u}) (i j : D.J)
    (s : pullback (D.ι i) (D.ι j) ⟶ D.U j)
    (hs : s ≫ D.ι j = pullback.fst (D.ι i) (D.ι j) ≫ D.ι i) :
    D.t i j ≫ D.f j i = (D.restrictOverlapIso i j).hom ≫ s
```

**`AlgebraicGeometry.LocallyRingedSpace.GlueData.homOutEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean#L146). The attribute's comment: “the mapping property for morphisms out of the glueing”.

> The mapping property for morphisms *out of* a gluing: a morphism `D.glued ⟶ Y` is the same
> thing as a family of morphisms `D.U i ⟶ Y` agreeing on the prescribed overlaps, the agreement
> being read through the transition maps. The bijection sends a morphism to the family of its
> restrictions `D.ι i ≫ h`.

```lean
noncomputable def homOutEquiv
    (D : LocallyRingedSpace.GlueData.{u}) (Y : LocallyRingedSpace.{u}) :
    (D.glued ⟶ Y) ≃
      { f : ∀ i, D.U i ⟶ Y //
          ∀ i j, D.f i j ≫ f i = D.t i j ≫ D.f j i ≫ f j }
```

**`AlgebraicGeometry.LocallyRingedSpace.GlueData.hom_pullbackCharts_jointlySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean, line 173](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean#L173). The attribute's comment: “canonical inverse-image cover”.

> The pullbacks of the canonical charts along a morphism into the glued space jointly cover its
> source.

```lean
theorem hom_pullbackCharts_jointlySurjective (D : LocallyRingedSpace.GlueData.{u})
    {Y : LocallyRingedSpace.{u}} (g : Y ⟶ D.glued) (y : Y) :
    ∃ (i : D.J) (x : pullback (C := LocallyRingedSpace) g (D.ι i)),
      (pullback.fst g (D.ι i)).base x = y
```

**`AlgebraicGeometry.LocallyRingedSpace.GlueData.hom_pullbackCharts_preimage_overlap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean#L183). The attribute's comment: “inverse images of overlaps”.

> On the inverse-image chart indexed by `i`, the inverse image of `V i j` is exactly its
> intersection with the chart indexed by `j`.

```lean
theorem hom_pullbackCharts_preimage_overlap (D : LocallyRingedSpace.GlueData.{u})
    {Y : LocallyRingedSpace.{u}} (g : Y ⟶ D.glued) (i j : D.J) :
    (pullback.snd g (D.ι i)).base ⁻¹' Set.range (D.f i j).base =
      Set.range
        (pullback.fst (pullback.fst g (D.ι i))
          (pullback.fst g (D.ι j))).base
```

**`AlgebraicGeometry.LocallyRingedSpace.GlueData.hom_pullbackCharts_transition`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean#L202). The attribute's comment: “transition compatibility for morphisms into the gluing”.

> The local morphisms on the inverse-image charts are related on intersections by the
> prescribed transition map.

```lean
theorem hom_pullbackCharts_transition (D : LocallyRingedSpace.GlueData.{u})
    {Y : LocallyRingedSpace.{u}} (g : Y ⟶ D.glued) (i j : D.J) :
    ∃! k : pullback (pullback.fst g (D.ι i)) (pullback.fst g (D.ι j)) ⟶ D.V (i, j),
      k ≫ D.f i j =
          pullback.fst (pullback.fst g (D.ι i)) (pullback.fst g (D.ι j)) ≫
            pullback.snd g (D.ι i) ∧
        k ≫ D.t i j ≫ D.f j i =
          pullback.snd (pullback.fst g (D.ι i)) (pullback.fst g (D.ι j)) ≫
            pullback.snd g (D.ι j)
```

**`AlgebraicGeometry.LocallyRingedSpace.GlueData.existsUnique_hom_of_openCover`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/MorphismsIntoGluing/GluingReconstruction.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/MorphismsIntoGluing/GluingReconstruction.lean#L268). The attribute's comment: “morphisms of locally ringed spaces glue over an open covering of the source”.

> Morphisms of locally ringed spaces glue over an open covering of the source: a family of
> morphisms out of the members of the covering which agree on the pairwise overlaps comes from a
> unique morphism out of the covered space.
>
> This is the locally ringed space counterpart of `AlgebraicGeometry.Scheme.Cover.glueMorphisms`,
> and the reason it is available here is that the covered space is the gluing of its own covering
> (`openCoverFromGlued_isIso`), so the morphism is obtained from the universal property of the
> multicoequalizer.

```lean
theorem existsUnique_hom_of_openCover
    {I : Type u} {Y Z : LocallyRingedSpace.{u}}
    {V : I → LocallyRingedSpace.{u}} (v : ∀ i, V i ⟶ Y)
    [∀ i, LocallyRingedSpace.IsOpenImmersion (v i)]
    (hv : ∀ y : Y, ∃ i x, (v i).base x = y)
    (h : ∀ i, V i ⟶ Z)
    (hcompat : ∀ i j, pullback.fst (v i) (v j) ≫ h i = pullback.snd (v i) (v j) ≫ h j) :
    ∃! f : Y ⟶ Z, ∀ i, v i ≫ f = h i
```

**`AlgebraicGeometry.LocallyRingedSpace.GlueData.existsUnique_hom_to_glued_of_compatibleCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/MorphismsIntoGluing/GluingReconstruction.lean, line 312](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/MorphismsIntoGluing/GluingReconstruction.lean#L312). The attribute's comment: “reconstruction from compatible charts”.

> Compatible morphisms from an open covering of a locally ringed space to the pieces of a
> gluing datum determine a unique morphism to the glued space. The two equations for
> `transitionLift` say that on `V i ×_Y V j` the maps are related by the transition `D.t i j`.

```lean
theorem existsUnique_hom_to_glued_of_compatibleCharts
    (D : LocallyRingedSpace.GlueData.{u}) (Y : LocallyRingedSpace.{u})
    (V : D.J → LocallyRingedSpace.{u}) (v : ∀ i, V i ⟶ Y)
    (v_open : ∀ i, LocallyRingedSpace.IsOpenImmersion (v i))
    (v_jointly_surjective : ∀ y : Y, ∃ (i : D.J) (x : V i), (v i).base x = y)
    (g : ∀ i, V i ⟶ D.U i)
    (transitionLift : ∀ i j, pullback (v i) (v j) ⟶ D.V (i, j))
    (transitionLift_f : ∀ i j,
      transitionLift i j ≫ D.f i j = pullback.fst (v i) (v j) ≫ g i)
    (transitionLift_t_f : ∀ i j,
      transitionLift i j ≫ D.t i j ≫ D.f j i = pullback.snd (v i) (v j) ≫ g j) :
    ∃! f : Y ⟶ D.glued, ∀ i, v i ≫ f = g i ≫ D.ι i
```

**`AlgebraicGeometry.LocallyRingedSpace.GlueData.hom_chartDatumOfHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/MorphismsIntoGluing/GluingReconstruction.lean, line 418](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/MorphismsIntoGluing/GluingReconstruction.lean#L418). The attribute's comment: “the mapping property for morphisms into the glueing”.

> The mapping property for morphisms *into* a glueing: a morphism `g : Y ⟶ D.glued` is
> recovered from the descent datum it induces, so that passing from a morphism to its chart datum
> and back is the identity. Combined with
> `AlgebraicGeometry.LocallyRingedSpace.GlueData.existsUnique_hom_to_glued`, which says that every
> chart datum determines a unique morphism, this identifies `Mor(Y, D.glued)` with the set of
> descent data arising from morphisms.

```lean
theorem hom_chartDatumOfHom (D : LocallyRingedSpace.GlueData.{u})
    {Y : LocallyRingedSpace.{u}} (g : Y ⟶ D.glued) :
    ∀ f : Y ⟶ D.glued,
      (∀ i, (D.chartDatumOfHom g).v i ≫ f = (D.chartDatumOfHom g).g i ≫ D.ι i) → f = g
```

**`AlgebraicGeometry.LocallyRingedSpace.GlueData.ChartDatum.chartIso_hom_fst_and_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/MorphismsIntoGluing/GluingReconstruction.lean, line 499](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/MorphismsIntoGluing/GluingReconstruction.lean#L499). The attribute's comment: “a descent datum is its own inverse-image covering”.

> The other half of the round trip for morphisms *into* a glueing: a descent datum is carried
> isomorphically, chart by chart and compatibly with both the covering maps and the local
> morphisms, onto the descent datum induced by the morphism it determines — whose charts, covering
> maps and local morphisms are `pullback f (D.ι i)`, `pullback.fst f (D.ι i)` and
> `pullback.snd f (D.ι i)` by `chartDatumOfHom_V`, `chartDatumOfHom_v` and `chartDatumOfHom_g`.
> Together with `AlgebraicGeometry.LocallyRingedSpace.GlueData.hom_chartDatumOfHom` this identifies
> `Mor(Y, D.glued)` with the descent data of the statement.

```lean
theorem ChartDatum.chartIso_hom_fst_and_snd {D : LocallyRingedSpace.GlueData.{u}}
    {Y : LocallyRingedSpace.{u}} (C : D.ChartDatum Y) {f : Y ⟶ D.glued}
    (hf : ∀ i, C.v i ≫ f = C.g i ≫ D.ι i) (i : D.J) :
    (C.chartIso hf i).hom ≫ pullback.fst f (D.ι i) = C.v i ∧
      (C.chartIso hf i).hom ≫ pullback.snd f (D.ι i) = C.g i
```

**`AlgebraicGeometry.LocallyRingedSpace.GlueData.homIntoEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/MorphismsIntoGluing/MappingProperty.lean, line 273](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/MorphismsIntoGluing/MappingProperty.lean#L273). The attribute's comment: “Mor(Y, X) is the set of descent data on an open covering of Y”.

> The mapping property for morphisms *into* a gluing, as a bijection: a morphism `Y ⟶ D.glued` is
> the same thing as a descent datum on `Y`, namely an open covering of `Y` together with compatible
> morphisms from its members to the pieces of the gluing datum. The bijection sends `f` to the
> covering by the inverse images `f ⁻¹' (U i)` and the factorisations of `f` through the charts.
> This is the counterpart for morphisms into the gluing of
> `AlgebraicGeometry.LocallyRingedSpace.GlueData.homOutEquiv`.

```lean
noncomputable def homIntoEquiv (D : LocallyRingedSpace.GlueData.{u})
    (Y : LocallyRingedSpace.{u}) : (Y ⟶ D.glued) ≃ D.ChartDatumOpens Y
```

Declarations registered for the tag:

- [`CategoryTheory.GlueData.glued`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GlueData.glued#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean#L55) (StacksFrontier).
- [`CategoryTheory.GlueData.ι`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GlueData.ι#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean#L56) (StacksFrontier).
- [`CategoryTheory.GlueData.glue_condition`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.GlueData.glue_condition#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean, line 57](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean#L57) (StacksFrontier).
- [`LocallyRingedSpace.GlueData.ι_isOpenImmersion`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LocallyRingedSpace.GlueData.ι_isOpenImmersion#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean#L58) (StacksFrontier).
- [`LocallyRingedSpace.GlueData.ι_jointly_surjective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LocallyRingedSpace.GlueData.ι_jointly_surjective#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean#L59) (StacksFrontier).
- [`LocallyRingedSpace.GlueData.vPullbackConeIsLimit`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LocallyRingedSpace.GlueData.vPullbackConeIsLimit#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean#L60) (StacksFrontier).
- [`LocallyRingedSpace.IsOpenImmersion.pullback_fst_of_right`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=LocallyRingedSpace.IsOpenImmersion.pullback_fst_of_right#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean, line 61](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/LocallyRingedSpaces.lean#L61) (StacksFrontier).

## Tag 01JC, a lemma

[Tag 01JC](https://stacks.math.columbia.edu/tag/01JC) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.GlueData.glued`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.GlueData.glued#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L318) (StacksFrontier): “the glued scheme”. References: EGA I (2.3.1); EGA IV (20.2.16), “more general”; SGA 3 XV (5.5), “more general”; SGA 6 II (AppI.1.2), “more general”.
- [`AlgebraicGeometry.Scheme.GlueData.isoLocallyRingedSpace`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.Scheme.GlueData.isoLocallyRingedSpace#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch26.lean, line 319](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/MathlibRegistrations/Ch26.lean#L319) (StacksFrontier): “its locally ringed space is the gluing of locally ringed spaces of Stacks 01JB”. References: EGA I (2.3.1).

## Tag 01JD, an example

[Tag 01JD](https://stacks.math.columbia.edu/tag/01JD) in the Stacks Project.

**`AlgebraicGeometry.affineSpaceWithDoubledZero`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOrigin.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOrigin.lean#L105). The attribute's comment: “doubled\_zero\_construction”. References: EGA I (5.5.11), “doubled origin constr.”.

> Affine `n`-space over `k` with its origin doubled, obtained by gluing two copies along the
> complements of their origins via the coordinate identification.

```lean
noncomputable abbrev affineSpaceWithDoubledZero (k : Type u) [Field k] (n : ℕ) :
    Scheme.{u}
```

**`AlgebraicGeometry.coordinateMorphismData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOrigin.lean, line 125](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOrigin.lean#L125). The attribute's comment: “coordinate\_morphism”. References: EGA I (5.5.11), “morphism to Spec k[t]”; SGA 6 II (2.2.7.2), “more general”.

> The coordinate maps on the two charts of affine space with doubled origin glue to a scheme
> morphism to affine space, restricting to the identity on each chart.

```lean
noncomputable def coordinateMorphismData (k : Type u) [Field k] (n : ℕ) :
    { f : affineSpaceWithDoubledZero k n ⟶
        Spec (.of (MvPolynomial (Fin n) k)) //
      ∀ i : Fin 2,
        chartInclusion k n i ≫ f = 𝟙 _ }
```

**`AlgebraicGeometry.coordinateMorphism_map_origin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOrigin.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOrigin.lean#L161). The attribute's comment: “origins\_map\_to\_origin”. References: EGA I (5.5.11), “two origins over 0”.

> The coordinate morphism maps the origin of each affine chart to the origin of affine
> space.

```lean
theorem coordinateMorphism_map_origin (k : Type u) [Field k] (n : ℕ)
    (i : Fin 2) :
    coordinateMorphism k n
        (chartInclusion k n i
          (affineOrigin k n)) = affineOrigin k n
```

**`AlgebraicGeometry.intersection_iso_puncturedAffinePlane`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOriginIntersection.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOriginIntersection.lean#L153). The attribute's comment: “non\_affine\_intersection”.

> In dimension two, the overlap of the two affine charts of the doubled-origin scheme is the
> punctured affine plane.

```lean
theorem intersection_iso_puncturedAffinePlane (S : PuncturedAffinePlane.{u}) :
    Nonempty (((chartInclusion S.k 2 0).opensRange ⊓
      (chartInclusion S.k 2 1).opensRange).toScheme ≅ S.puncturedScheme)
```

**`AlgebraicGeometry.not_isAffineOpen_chartIntersection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOriginIntersection.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOriginIntersection.lean#L162). The attribute's comment: “non\_affine\_intersection”.

> For dimension greater than one, the two affine charts of affine space with doubled origin have
> a non-affine intersection.

```lean
theorem not_isAffineOpen_chartIntersection (k : Type u) [Field k] (n : ℕ)
    (hn : 1 < n) :
    ¬ IsAffineOpen ((chartInclusion k n 0).opensRange ⊓
      (chartInclusion k n 1).opensRange)
```

**`AlgebraicGeometry.exists_affineOpens_nonaffine_inf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOriginIntersection.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOriginIntersection.lean#L174). The attribute's comment: “non\_affine\_intersection”.

> The intersection of two affine opens in a scheme need not be affine.

```lean
theorem exists_affineOpens_nonaffine_inf :
    ∃ (X : Scheme.{u}) (U V : X.Opens),
      IsAffineOpen U ∧ IsAffineOpen V ∧ ¬ IsAffineOpen (U ⊓ V)
```

**`AlgebraicGeometry.infinite_irreducibleClosed_closures`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOriginPoints.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOriginPoints.lean#L132). The attribute's comment: “many\_irreducible\_closed”.

> In dimension greater than one, infinitely many irreducible closed subsets of affine space with
> doubled origin are closures of nonclosed points in its first affine chart.

```lean
theorem infinite_irreducibleClosed_closures (k : Type u) [Field k] (n : ℕ) (hn : 1 < n) :
    Set.Infinite
      { T : Set (affineSpaceWithDoubledZero k n) |
        IsClosed T ∧ IsIrreducible T ∧
          ∃ x : Spec (.of (MvPolynomial (Fin n) k)),
            ¬ IsClosed ({x} : Set (Spec (.of (MvPolynomial (Fin n) k)))) ∧
              T = closure ({(chartInclusion k n 0).base x} :
                Set (affineSpaceWithDoubledZero k n)) }
```

**`AlgebraicGeometry.mem_origin_iff_mem_origin`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOriginPoints.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOriginPoints.lean#L264). The attribute's comment: “origins\_in\_closed\_subset”.

> Apart from the two singleton origins, an irreducible closed subset of affine space with
> the origin doubled contains either both origins or neither.

```lean
theorem mem_origin_iff_mem_origin (k : Type u) [Field k] (n : ℕ)
    (T : Set (affineSpaceWithDoubledZero k n))
    (hT : IsIrreducible T) (hT_closed : IsClosed T)
    (hT₀ : T ≠ {chartInclusion k n 0 (affineOrigin k n)})
    (hT₁ : T ≠ {chartInclusion k n 1 (affineOrigin k n)}) :
    (chartInclusion k n 0 (affineOrigin k n) ∈ T ↔
      chartInclusion k n 1 (affineOrigin k n) ∈ T)
```

**`AlgebraicGeometry.isIso_coordinateMorphism_globalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOriginSections.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOriginSections.lean#L146). The attribute's comment: “global\_sections”. References: EGA I (5.5.11), “more general”; SGA 6 II (2.2.7.2), “more general”.

> In positive dimension, every global function on affine space with doubled origin is induced
> uniquely by a polynomial via the coordinate morphism.

```lean
theorem isIso_coordinateMorphism_globalSections (k : Type u) [Field k]
    (n : ℕ) (hn : 0 < n) :
    IsIso ((Scheme.ΓSpecIso (.of (MvPolynomial (Fin n) k))).inv ≫
      (coordinateMorphism k n).appTop)
```

**`AlgebraicGeometry.not_isAffine_affineSpaceWithDoubledZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOriginSections.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOriginSections.lean#L176). The attribute's comment: “not\_affine”.

> Affine space of positive dimension with its origin doubled is not affine.

```lean
theorem not_isAffine_affineSpaceWithDoubledZero (k : Type u) [Field k]
    (n : ℕ) (hn : 0 < n) :
    ¬ IsAffine (affineSpaceWithDoubledZero k n)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.isAffineOpen_opensRange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isAffineOpen_opensRange#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOrigin.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/DoubledOrigin.lean#L58) (StacksFrontier): “affine\_open\_charts”.

## Tag 01JE, an example

[Tag 01JE](https://stacks.math.columbia.edu/tag/01JE) in the Stacks Project.

**`AlgebraicGeometry.projectiveLineInversionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLine.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLine.lean#L83). The attribute's comment: “projective\_line\_gluing”. References: EGA I (2.3.2), “partial”.

> The isomorphism `φ₁₂` of the gluing datum: the automorphism of the punctured affine line
> induced by `T ↦ T⁻¹`, which is the identification `y = 1/x` of the two coordinates on the
> overlap.

```lean
noncomputable def projectiveLineInversionIso :
    Spec (.of (LaurentPolynomial k)) ≅ Spec (.of (LaurentPolynomial k))
```

**`AlgebraicGeometry.projectiveLineGluingData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLine.lean, line 126](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLine.lean#L126). The attribute's comment: “projective\_line\_gluing”.

> The gluing datum for the projective line: two copies of `Spec k[X]`, glued along
> `D(X) = Spec k[T,T⁻¹]` by inversion.

```lean
noncomputable def projectiveLineGluingData : Scheme.GlueData.{u}
```

**`AlgebraicGeometry.projectiveLine`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLine.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLine.lean#L136). The attribute's comment: “projective\_line\_gluing”. References: EGA I (2.3.2), “gluing construction”.

> The projective line over `k`, constructed by gluing its two standard affine charts.

```lean
noncomputable abbrev projectiveLine : Scheme.{u}
```

**`AlgebraicGeometry.projectiveLineZero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLine.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLine.lean#L216). The attribute's comment: “projective\_line\_gluing”.

> The point `0` of the projective line, namely the point `(X)` in the `x`-chart.

```lean
def projectiveLineZero [IsDomain k] : projectiveLine k
```

**`AlgebraicGeometry.projectiveLineInfinity`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLine.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLine.lean#L221). The attribute's comment: “projective\_line\_gluing”. References: EGA II (7.4.14).

> The point `∞` of the projective line, namely the point `(X)` in the `y`-chart.

```lean
def projectiveLineInfinity [IsDomain k] : projectiveLine k
```

**`AlgebraicGeometry.affineLineOne`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean#L162). The attribute's comment: “projective\_line\_one”.

> The point `1` of an affine-line chart, represented by the prime ideal `(X - 1)`.

```lean
def affineLineOne : Spec (.of (Polynomial k))
```

**`AlgebraicGeometry.projectiveLineOne`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean, line 185](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean#L185). The attribute's comment: “projective\_line\_one”.

> The point `1` of the projective line, namely the point `(x - 1)` in the `x`-chart.

```lean
def projectiveLineOne : projectiveLine k
```

**`AlgebraicGeometry.projectiveLineYChart_affineLineOne`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean#L190). The attribute's comment: “projective\_line\_one”.

> The point `1` is *also* the point `(y - 1)` of the second chart.

```lean
theorem projectiveLineYChart_affineLineOne :
    projectiveLineYChart k (affineLineOne k) = projectiveLineOne k
```

**`AlgebraicGeometry.projectiveLineSChart`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean, line 1075](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean#L1075). The attribute's comment: “projective\_line\_affine\_open\_through\_zero\_and\_infinity”.

> The third chart of the projective line: the affine line with coordinate
> `s = 1/(x-1) = y/(1-y)`, mapping onto the complement of the point `1`.

```lean
def projectiveLineSChart : Spec (.of (Polynomial k)) ⟶ projectiveLine k
```

**`AlgebraicGeometry.projectiveLineSXPiece_comp_projectiveLineSChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean, line 1082](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean#L1082). The attribute's comment: “projective\_line\_affine\_open\_coordinate\_ring”.

> On `D(x-1) ⊂ X₁` the third chart is the inclusion of that open into the first chart;
> equivalently, `s` restricts to `1/(x-1)` there.

```lean
theorem projectiveLineSXPiece_comp_projectiveLineSChart :
    projectiveLineSXPiece k ≫ projectiveLineSChart k =
      Spec.map (CommRingCat.ofHom (algebraMap (Polynomial k) (affineLineAwayOne k))) ≫
        projectiveLineXChart k
```

**`AlgebraicGeometry.projectiveLineSYPiece_comp_projectiveLineSChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean, line 1091](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean#L1091). The attribute's comment: “projective\_line\_affine\_open\_coordinate\_ring”.

> On `D(y-1) ⊂ X₂` the third chart is the inclusion of that open into the second chart;
> equivalently, `s` restricts to `y/(1-y)` there.

```lean
theorem projectiveLineSYPiece_comp_projectiveLineSChart :
    projectiveLineSYPiece k ≫ projectiveLineSChart k =
      Spec.map (CommRingCat.ofHom (algebraMap (Polynomial k) (affineLineAwayOne k))) ≫
        projectiveLineYChart k
```

**`AlgebraicGeometry.range_projectiveLineSChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean, line 1345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean#L1345). The attribute's comment: “projective\_line\_affine\_open\_through\_zero\_and\_infinity”.

> The image of the third chart is exactly the complement of the point `1`: `U = ℙ¹ \ {1}`.

```lean
theorem range_projectiveLineSChart :
    Set.range (projectiveLineSChart k).base = {projectiveLineOne k}ᶜ
```

**`AlgebraicGeometry.isAffineOpen_projectiveLineSChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean, line 1376](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean#L1376). The attribute's comment: “projective\_line\_affine\_open\_through\_zero\_and\_infinity”.

> `U = ℙ¹ \ {1}` is an affine open.

```lean
theorem isAffineOpen_projectiveLineSChart :
    IsAffineOpen (projectiveLineSChart k).opensRange
```

**`AlgebraicGeometry.projectiveLineZero_mem_opensRange_projectiveLineSChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean, line 1382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean#L1382). The attribute's comment: “projective\_line\_affine\_open\_through\_zero\_and\_infinity”.

> The point `0` lies in `U = ℙ¹ \ {1}`.

```lean
theorem projectiveLineZero_mem_opensRange_projectiveLineSChart :
    projectiveLineZero k ∈ (projectiveLineSChart k).opensRange
```

**`AlgebraicGeometry.projectiveLineInfinity_mem_opensRange_projectiveLineSChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean, line 1393](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean#L1393). The attribute's comment: “projective\_line\_affine\_open\_through\_zero\_and\_infinity”.

> The point `∞` lies in `U = ℙ¹ \ {1}`.

```lean
theorem projectiveLineInfinity_mem_opensRange_projectiveLineSChart :
    projectiveLineInfinity k ∈ (projectiveLineSChart k).opensRange
```

**`AlgebraicGeometry.projectiveLineSChartIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean, line 1408](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean#L1408). The attribute's comment: “projective\_line\_affine\_open\_coordinate\_ring”.

> `U = ℙ¹ \ {1}` is isomorphic to `Spec k[s]`, and so `Γ(U, O_U) = k[s]`.

```lean
def projectiveLineSChartIso :
    Spec (.of (Polynomial k)) ≅ ((projectiveLineSChart k).opensRange).toScheme
```

**`AlgebraicGeometry.projectiveLineSChartSectionsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean, line 1422](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineAffineOpen.lean#L1422). The attribute's comment: “projective\_line\_affine\_open\_coordinate\_ring”.

> `Γ(U, O_U)` is the polynomial ring `k[s]`, for the coordinate `s = 1/(x-1) = y/(1-y)` of
> `AlgebraicGeometry.affineLineSOnXChart` and `AlgebraicGeometry.affineLineSOnYChart`.

```lean
def projectiveLineSChartSectionsIso :
    CommRingCat.of (Polynomial k) ≅ Γ(((projectiveLineSChart k).opensRange).toScheme, ⊤)
```

**`AlgebraicGeometry.mem_range_projectiveLinePuncturedChart_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLinePoints.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLinePoints.lean#L66). The attribute's comment: “projective\_line\_overlap”.

> The overlap `U₁₂` of the two charts of the projective line, seen in the first chart, is
> `D(x)`, the locus where the coordinate is invertible.

```lean
theorem mem_range_projectiveLinePuncturedChart_iff (y : Spec (.of (Polynomial k))) :
    y ∈ Set.range (projectiveLinePuncturedChart k).base ↔
      (Polynomial.X : Polynomial k) ∉ y.asIdeal
```

**`AlgebraicGeometry.mem_range_projectiveLineOverlapYInclusion_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLinePoints.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLinePoints.lean#L80). The attribute's comment: “projective\_line\_overlap”.

> The overlap `U₂₁` of the two charts of the projective line, seen in the second chart, is
> `D(y)`, the locus where the coordinate of that chart is invertible.

```lean
theorem mem_range_projectiveLineOverlapYInclusion_iff (y : Spec (.of (Polynomial k))) :
    y ∈ Set.range (projectiveLineOverlapYInclusion k).base ↔
      (Polynomial.X : Polynomial k) ∉ y.asIdeal
```

**`AlgebraicGeometry.eq_affineLineOrigin_of_X_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLinePoints.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLinePoints.lean#L106). The attribute's comment: “projective\_line\_overlap”.

> The complement of the overlap in a chart is the single point `0` of that chart: the only
> point of the affine line over a field at which the coordinate vanishes is the origin.

```lean
theorem eq_affineLineOrigin_of_X_mem (y : Spec (.of (Polynomial k)))
    (hy : (Polynomial.X : Polynomial k) ∈ y.asIdeal) : y = affineLineOrigin k
```

**`AlgebraicGeometry.projectiveLineZero_ne_projectiveLineInfinity`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLinePoints.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLinePoints.lean#L213). The attribute's comment: “projective\_line\_gluing”.

> The points `0` and `∞` of the projective line are distinct.

```lean
theorem projectiveLineZero_ne_projectiveLineInfinity (k : Type u) [Field k] :
    projectiveLineZero k ≠ projectiveLineInfinity k
```

**`AlgebraicGeometry.infinite_projectiveLine`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLinePoints.lean, line 262](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLinePoints.lean#L262). The attribute's comment: “projective\_line\_infinite”.

> The projective line over a field is infinite.

```lean
instance infinite_projectiveLine (k : Type u) [Field k] : Infinite (projectiveLine k)
```

**`AlgebraicGeometry.isIso_constantsToGlobalSections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineSections.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineSections.lean#L155). The attribute's comment: “projective\_line\_global\_sections”. References: EGA I (2.3.2), “Γ(X,O\_X) ≅ K”.

> The canonical map from `k` to the global sections of the structure sheaf
> on the projective line over `k` is an isomorphism.

```lean
theorem isIso_constantsToGlobalSections (k : Type u) [CommRing k] :
    IsIso ((Scheme.ΓSpecIso (.of k)).inv ≫
      (projectiveLine k ↘ Spec (.of k)).appTop)
```

**`AlgebraicGeometry.not_isAffine_projectiveLine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineSections.lean, line 212](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Scheme/Glueing/ProjectiveLineSections.lean#L212). The attribute's comment: “projective\_line\_not\_affine”. References: EGA I (2.3.2), “X not affine”.

> The projective line over a field is not affine.

```lean
theorem not_isAffine_projectiveLine (k : Type u) [Field k] :
    ¬ IsAffine (projectiveLine k)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 26.14, Tag 01JA](https://stacks.math.columbia.edu/tag/01JA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
