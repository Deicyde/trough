---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isRepresentable_of_isAbsolutelyQuasiSeparated_of_dimension_eq_zero, AlgebraicGeometry.Space.isSeparatedSchemeWithAffineQuasiCompactOpens_of_isAbsolutelyQuasiSeparated_of_dimension_eq_zero, AlgebraicGeometry.Space.isSeparatedSchemeWithAffineQuasiCompactOpens_of_isNoetherian_of_dimension_eq_zero, AlgebraicGeometry.Space.isRepresentable_of_isNoetherian_of_dimension_eq_zero, AlgebraicGeometry.Space.isSeparatedSchemeWithAffineQuasiCompactOpens_of_isLocallyOfFiniteType_over_field, AlgebraicGeometry.Space.isRepresentable_of_isLocallyOfFiniteType_over_field, AlgebraicGeometry.Space.tfae_localRingDimension_eq_zero_and_exists_isRepresentable_isOpenSubspace, AlgebraicGeometry.Space.exists_isRepresentable_isOpenSubspace_mem_range_of_mem_genericPoints
statement: formalized
proof: formalized
---

# 72.9 Schematic locus

Section 72.9 of the Stacks Project, [Tag 06LY](https://stacks.math.columbia.edu/tag/06LY). 4 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 06LZ, a lemma

[Tag 06LZ](https://stacks.math.columbia.edu/tag/06LZ) in the Stacks Project.

**`AlgebraicGeometry.Space.isRepresentable_of_isAbsolutelyQuasiSeparated_of_dimension_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroSeparatedScheme.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroSeparatedScheme.lean#L128). The attribute's comment: “case (1): X is a scheme”.

> A quasi-separated algebraic space of dimension zero over `S` is representable.

```lean
theorem isRepresentable_of_isAbsolutelyQuasiSeparated_of_dimension_eq_zero
    (hX : IsAlgebraicSpace B S hS X) (hqs : IsAbsolutelyQuasiSeparated B S hS hZ X)
    (hdim : dimension B S hS X hX = 0) : X.IsRepresentable
```

**`AlgebraicGeometry.Space.isSeparatedSchemeWithAffineQuasiCompactOpens_of_isAbsolutelyQuasiSeparated_of_dimension_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroSeparatedScheme.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroSeparatedScheme.lean#L199). The attribute's comment: “case (1)”.

> A quasi-separated algebraic space of dimension zero over `S` is a separated scheme, and every
> quasi-compact open of it is affine.

```lean
theorem
    isSeparatedSchemeWithAffineQuasiCompactOpens_of_isAbsolutelyQuasiSeparated_of_dimension_eq_zero
    (hX : IsAlgebraicSpace B S hS X) (hqs : IsAbsolutelyQuasiSeparated B S hS hZ X)
    (hdim : dimension B S hS X hX = 0) :
    IsSeparatedSchemeWithAffineQuasiCompactOpens B S hS X
```

**`AlgebraicGeometry.Space.isSeparatedSchemeWithAffineQuasiCompactOpens_of_isNoetherian_of_dimension_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroSeparatedScheme.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroSeparatedScheme.lean#L217). The attribute's comment: “case (3)”.

> A Noetherian algebraic space of dimension zero over `S` is a separated scheme, and every
> quasi-compact open of it is affine.

```lean
theorem isSeparatedSchemeWithAffineQuasiCompactOpens_of_isNoetherian_of_dimension_eq_zero
    (hX : IsAlgebraicSpace B S hS X) (hnoeth : IsNoetherian B S hS hZ X)
    (hdim : dimension B S hS X hX = 0) :
    IsSeparatedSchemeWithAffineQuasiCompactOpens B S hS X
```

**`AlgebraicGeometry.Space.isRepresentable_of_isNoetherian_of_dimension_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroSeparatedScheme.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroSeparatedScheme.lean#L226). The attribute's comment: “case (3): X is a scheme”.

> A Noetherian algebraic space of dimension zero over `S` is representable.

```lean
theorem isRepresentable_of_isNoetherian_of_dimension_eq_zero
    (hX : IsAlgebraicSpace B S hS X) (hnoeth : IsNoetherian B S hS hZ X)
    (hdim : dimension B S hS X hX = 0) : X.IsRepresentable
```

**`AlgebraicGeometry.Space.isSeparatedSchemeWithAffineQuasiCompactOpens_of_isLocallyOfFiniteType_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroSeparatedScheme.lean, line 412](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroSeparatedScheme.lean#L412). The attribute's comment: “case (2)”.

> An algebraic space over `S` of dimension zero which is locally of finite type over a field `k`
> is a separated scheme, and every quasi-compact open of it is affine.

```lean
theorem isSeparatedSchemeWithAffineQuasiCompactOpens_of_isLocallyOfFiniteType_over_field
    (hX : IsAlgebraicSpace B S hS X) {k : Type u} [Field k]
    {K : BigFppfOver B (⊤_ Scheme.{u}) hZ}
    (eK : (BigFppfOver.toScheme B (⊤_ Scheme.{u}) hZ).obj K ≅ Spec (.of k))
    {f : viewOverIntegers B S hS hZ X ⟶ yoneda.obj K}
    (hf : IsLocallyOfFiniteType B (⊤_ Scheme.{u}) hZ f)
    (hdim : dimension B S hS X hX = 0) :
    IsSeparatedSchemeWithAffineQuasiCompactOpens B S hS X
```

**`AlgebraicGeometry.Space.isRepresentable_of_isLocallyOfFiniteType_over_field`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroSeparatedScheme.lean, line 427](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/DimensionZeroSeparatedScheme.lean#L427). The attribute's comment: “case (2): X is a scheme”.

> An algebraic space over `S` of dimension zero which is locally of finite type over a field is
> representable.

```lean
theorem isRepresentable_of_isLocallyOfFiniteType_over_field (hX : IsAlgebraicSpace B S hS X)
    {k : Type u} [Field k] {K : BigFppfOver B (⊤_ Scheme.{u}) hZ}
    (eK : (BigFppfOver.toScheme B (⊤_ Scheme.{u}) hZ).obj K ≅ Spec (.of k))
    {f : viewOverIntegers B S hS hZ X ⟶ yoneda.obj K}
    (hf : IsLocallyOfFiniteType B (⊤_ Scheme.{u}) hZ f)
    (hdim : dimension B S hS X hX = 0) : X.IsRepresentable
```

## Tag 0ADC, a lemma

[Tag 0ADC](https://stacks.math.columbia.edu/tag/0ADC) in the Stacks Project.

**`AlgebraicGeometry.Space.tfae_localRingDimension_eq_zero_and_exists_isRepresentable_isOpenSubspace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiSeparatedSchematicLocusCodimensionZero.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiSeparatedSchematicLocusCodimensionZero.lean#L174).

> Let `x` be a point of a quasi-separated algebraic space over `S`. The
> following are equivalent:
> 1. `x` is a point of codimension `0` on the space, that is, by Tag 04NA, the dimension of the
>    local ring there is `0`;
> 2. the local ring of the space at `x` has dimension `0`, in the chart-wise form of Tag 0BAM:
>    every étale scheme chart has a local ring of Krull dimension `0` at each point above `x`;
> 3. `x` is a generic point of an irreducible component of the space of points.
>
> If these hold, then some open subspace of the space containing `x` is a scheme.

```lean
theorem tfae_localRingDimension_eq_zero_and_exists_isRepresentable_isOpenSubspace
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    (hqs : IsAbsolutelyQuasiSeparated B S hS hZ F) (x : points B S hS F) :
    [localRingDimension B S hS x = 0, AllChartsLocalRingDimension B S hS x 0,
        x ∈ genericPoints (points B S hS F)].TFAE ∧
      (localRingDimension B S hS x = 0 →
        ∃ G : Subfunctor F, IsOpenSubspace B S hS G ∧ G.toFunctor.IsRepresentable ∧
          x ∈ Set.range (pointsMap B S hS G.toFunctor G.ι))
```

**`AlgebraicGeometry.Space.exists_isRepresentable_isOpenSubspace_mem_range_of_mem_genericPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiLocallyQuasiSeparatedCodimensionZero.lean, line 309](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiLocallyQuasiSeparatedCodimensionZero.lean#L309). The attribute's comment: “the final statement”.

> **Stacks 0ADC, the final statement.** A generic point of an irreducible component of the
> space of points of a quasi-separated algebraic space over `S` lies in an open subspace which
> is a scheme, namely in the schematic locus of Tag 03JH.
>
> The equivalence of the tag's conditions (1), (2) and (3) is
> `AlgebraicGeometry.Space.localRingDimension_eq_zero_iff_mem_genericPoints_of_quasiSeparated`;
> the codimension-zero clause of Tag 06NH which carries such a generic point into the schematic
> locus is `codimensionZero_mem_schematicLocus_of_isZariskiLocallyQuasiSeparated` above.

```lean
theorem exists_isRepresentable_isOpenSubspace_mem_range_of_mem_genericPoints
    (hZ : B.Contains (⊤_ Scheme.{u}))
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    (hqs : IsAbsolutelyQuasiSeparated B S hS hZ F)
    (x : points B S hS F) (hx : x ∈ genericPoints (points B S hS F)) :
    ∃ G : Subfunctor F, IsOpenSubspace B S hS G ∧ G.toFunctor.IsRepresentable ∧
      x ∈ Set.range (pointsMap B S hS G.toFunctor G.ι)
```

**`AlgebraicGeometry.Space.localRingDimension_eq_zero_iff_mem_genericPoints_of_quasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ZariskiLocallyQuasiSeparatedSchematicLocus.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ZariskiLocallyQuasiSeparatedSchematicLocus.lean#L137). The attribute's comment: “the equivalence of conditions (1), (2) and (3)”.

> A point of a quasi-separated algebraic space over `S` has a local ring of dimension zero —
> equivalently, is a point of codimension `0` — exactly when it is a generic point of an
> irreducible component of the space of points.

```lean
theorem localRingDimension_eq_zero_iff_mem_genericPoints_of_quasiSeparated
    (F : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (hF : IsAlgebraicSpace B S hS F)
    (hqs : IsAbsolutelyQuasiSeparated B S hS hZ F) (x : points B S hS F) :
    localRingDimension B S hS x = 0 ↔ x ∈ genericPoints (points B S hS F)
```

## Tag 0ADD, a lemma

[Tag 0ADD](https://stacks.math.columbia.edu/tag/0ADD) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isOpenSubspace_isRepresentable_of_localRingDimension_le_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CodimensionOneSchematicLocus.lean, line 341](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CodimensionOneSchematicLocus.lean#L341).

> **Stacks 0ADD.** Let `X` be an algebraic space over `S` which is separated and locally
> Noetherian, and let `x ∈ |X|` be a point whose local ring has dimension at most one
> (Stacks 04NA). Then there is an open subspace of `X` containing `x` which is a scheme, that
> is, whose functor of points is representable.
>
> An affine étale chart `V ⟶ X` through `x` has open image `Z₀`, which is quasi-compact,
> separated and locally Noetherian; `V` is immersed over `Z₀` in a proper representable morphism,
> the fibres of `V ⟶ Z₀` at field-valued points have bounded degree, and
> `AlgebraicGeometry.Space.exists_isOpenSubspace_isRepresentable_of_chart_rank_le` applies.

```lean
theorem exists_isOpenSubspace_isRepresentable_of_localRingDimension_le_one
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hsep : IsAbsolutelySeparated B S hS B.contains_terminal X)
    (hnoeth : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (x : points B S hS X) (hdim : localRingDimension B S hS x ≤ 1) :
    ∃ G : Subfunctor X, IsOpenSubspace B S hS G ∧ G.toFunctor.IsRepresentable ∧
      x ∈ Set.range (pointsMap B S hS G.toFunctor G.ι)
```

## Tag 0ADE, a remark

[Tag 0ADE](https://stacks.math.columbia.edu/tag/0ADE) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isOpenSubspace_isRepresentable_of_localRingDimension_le_one_of_fittingBlowups`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CodimensionOneSchematicLocusByFlattening.lean, line 424](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CodimensionOneSchematicLocusByFlattening.lean#L424). The attribute's comment: “Lemma 0ADD proved along the route of the remark, avoiding Stacks 0ABI”.

> **Stacks 0ADE.**  Let `X` be an algebraic space over `S` which is separated and locally
> Noetherian, and let `x ∈ |X|` be a point whose local ring has dimension at most one
> (Stacks 04NA).  Then there is an open subspace of `X` containing `x` which is a scheme, that is,
> whose functor of points is representable; the route of the remark makes it an affine scheme,
> which is recorded as well.
>
> This is the statement of Stacks 0ADD, proved along the route of the remark Stacks 0ADE, which
> avoids More on Groupoids, Lemma 0ABI: the finite surjective cover by a scheme near `x` comes
> from the induction on the degree of an affine étale chart through `x`
> (`exists_isOpenSubspace_isRepresentable_of_chart_rank_le_of_fittingBlowups`), and the
> remark's Steps 1 to 5 — reduction, flattening by blowing up Fitting ideals (Stacks 0D0Q), the
> finite flat quotient of Stacks 07S6 with Stacks 09NN, the affine open with saturated principal
> trace via Stacks 0ADC and 09NN, and Stacks 07VP — turn it into an open subspace which is a scheme.

```lean
theorem exists_isOpenSubspace_isRepresentable_of_localRingDimension_le_one_of_fittingBlowups
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hsep : IsAbsolutelySeparated B S hS B.contains_terminal X)
    (hnoeth : HasEtaleLocalProperty B S hS X (fun T : Scheme.{u} => IsLocallyNoetherian T))
    (x : points B S hS X) (hdim : localRingDimension B S hS x ≤ 1) :
    ∃ G : Subfunctor X, IsOpenSubspace B S hS G ∧ G.toFunctor.IsRepresentable ∧
      IsAffineSpace B S hS G.toFunctor ∧ x ∈ Set.range (pointsMap B S hS G.toFunctor G.ι)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 72.9, Tag 06LY](https://stacks.math.columbia.edu/tag/06LY)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
