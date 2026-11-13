---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.meromorphicFunctionSheaf, AlgebraicGeometry.Space.MeromorphicFunction, AlgebraicGeometry.Space.isRegularSection_iff_mem_nonZeroDivisors, AlgebraicGeometry.Space.meromorphicSectionSheaf, AlgebraicGeometry.Space.MeromorphicSection, AlgebraicGeometry.Space.isFractionRing_meromorphicFunctionSheaf_obj, AlgebraicGeometry.Space.isQuasicoherent_meromorphicAlgebraSheaf, AlgebraicGeometry.Space.regularSectionsStalk_eq_nonZeroDivisors
statement: formalized
proof: formalized
---

# 71.10 Meromorphic functions and sections

Section 71.10 of the Stacks Project, [Tag 0EN2](https://stacks.math.columbia.edu/tag/0EN2). 11 tags here are carried by 32 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0EN3, a definition

[Tag 0EN3](https://stacks.math.columbia.edu/tag/0EN3) in the Stacks Project.

**`AlgebraicGeometry.Space.meromorphicFunctionSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicFunctions.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicFunctions.lean#L214). The attribute's comment: “the sheaf of meromorphic functions”.

> **Stacks 0EN3.** The *sheaf of meromorphic functions* `𝒦_F` on the algebraic space `F`: the
> sheaf on the small étale site of `F` associated to the presheaf of sectionwise localizations
> `U ↦ 𝒮_F(U)⁻¹ 𝒪_F(U)`.

```lean
noncomputable def meromorphicFunctionSheaf (hF : IsAlgebraicSpace B S hS F) :
    Sheaf (SmallEtale.topology B S hS F) CommRingCat.{u}
```

**`AlgebraicGeometry.Space.MeromorphicFunction`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicFunctions.lean, line 227](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicFunctions.lean#L227). The attribute's comment: “meromorphic functions”.

> **Stacks 0EN3.** A *meromorphic function* on the algebraic space `F` is a global section of
> its sheaf of meromorphic functions `𝒦_F`.

```lean
abbrev MeromorphicFunction (hF : IsAlgebraicSpace B S hS F)
```

## Tag 0EN4, a lemma

[Tag 0EN4](https://stacks.math.columbia.edu/tag/0EN4) in the Stacks Project.

**`AlgebraicGeometry.Space.isRegularSection_iff_mem_nonZeroDivisors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicFunctions.lean, line 336](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicFunctions.lean#L336).

> **Stacks 0EN4.** Over an affine étale chart `U` of the algebraic space `F` the regular
> sections of `𝒪_F` are exactly the nonzerodivisors of the ring of sections `𝒪_F(U)`.

```lean
theorem isRegularSection_iff_mem_nonZeroDivisors (U : SmallEtale B S hS F)
    (hU : IsAffine (smallEtaleScheme B S hS F U))
    (s : (structurePresheaf B S hS F).obj (op U)) :
    IsRegularSection B S hS F U s ↔ s ∈ ((structurePresheaf B S hS F).obj (op U))⁰
```

## Tag 0EN5, a definition

[Tag 0EN5](https://stacks.math.columbia.edu/tag/0EN5) in the Stacks Project.

**`AlgebraicGeometry.Space.meromorphicSectionSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicSections.lean, line 148](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicSections.lean#L148). The attribute's comment: “part (1)”.

> The sheaf `𝒦_F(M)` of *meromorphic sections* of a sheaf of `𝒪_F`-modules `M`: the extension
> of scalars of `M` along `𝒪_F ⟶ 𝒦_F`, sheafified.

```lean
noncomputable abbrev meromorphicSectionSheaf (hF : IsAlgebraicSpace B S hS F)
    (M : Modules.{u, max u z} B S hS F hF) :
    SheafOfModules.{max (u + 1) z}
      (Stacks.SheafOfModules.Tensor.ringSheaf (meromorphicRingedSite B S hS F hF).O)
```

**`AlgebraicGeometry.Space.MeromorphicSection`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicSections.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicSections.lean#L161). The attribute's comment: “part (2)”.

> A *meromorphic section* of a sheaf of `𝒪_F`-modules `M` is a global section of the sheaf
> `𝒦_F(M)` of meromorphic sections of `M`.

```lean
noncomputable abbrev MeromorphicSection (hF : IsAlgebraicSpace B S hS F)
    (M : Modules.{u, max u z} B S hS F hF) : Type _
```

## Tag 0EN6, a lemma

[Tag 0EN6](https://stacks.math.columbia.edu/tag/0EN6) in the Stacks Project.

**`AlgebraicGeometry.Space.isFractionRing_meromorphicFunctionSheaf_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicQuasicoherent.lean, line 342](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicQuasicoherent.lean#L342). The attribute's comment: “part (2): over an affine object of the small étale site the ring of meromorphic functions is the total ring of fractions of the ring of sections”.

> For an affine object `U` of the small étale site of an algebraic
> space `X` satisfying hypotheses (a) and (b), the ring `𝒦_X(U)` of meromorphic functions over `U`
> is the total ring of fractions of `𝒪_X(U)`.

```lean
theorem isFractionRing_meromorphicFunctionSheaf_obj
    (hwa : ∀ z ∈ weaklyAssociatedPointsOfSpace B S hS X, localRingDimension B S hS z = 0)
    (hfin : HasLocallyFiniteIrreducibleComponents B S hS X.1)
    (U : SmallEtale B S hS X.1) (hU : IsAffine (smallEtaleScheme B S hS X.1 U)) :
    letI : Algebra ((structurePresheaf B S hS X.1).obj (op U))
        ((meromorphicFunctionSheaf B S hS X.1 X.2).obj.obj (op U)) :=
      ((toMeromorphicFunctionSheaf B S hS X.1 X.2).hom.app (op U)).hom.toAlgebra
    IsFractionRing ((structurePresheaf B S hS X.1).obj (op U))
      ((meromorphicFunctionSheaf B S hS X.1 X.2).obj.obj (op U))
```

**`AlgebraicGeometry.Space.isQuasicoherent_meromorphicAlgebraSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicQuasicoherent.lean, line 388](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicQuasicoherent.lean#L388). The attribute's comment: “part (1): the sheaf of meromorphic functions is a quasi-coherent sheaf of algebras”.

> For an algebraic space `X` satisfying hypotheses (a) and (b), the
> sheaf of meromorphic functions `𝒦_X` is a quasi-coherent sheaf of `𝒪_X`-algebras.

```lean
theorem isQuasicoherent_meromorphicAlgebraSheaf
    (hwa : ∀ z ∈ weaklyAssociatedPointsOfSpace B S hS X, localRingDimension B S hS z = 0)
    (hfin : HasLocallyFiniteIrreducibleComponents B S hS X.1) :
    (meromorphicAlgebraSheaf B S hS X).IsQuasicoherent
```

**`AlgebraicGeometry.Space.regularSectionsStalk_eq_nonZeroDivisors`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicStalks.lean, line 408](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicStalks.lean#L408). The attribute's comment: “part (3): for a geometric point the germs of regular sections are exactly the nonzerodivisors of the étale local ring”.

> **Stacks 0EN6, part (3).** Let `X` be an algebraic space over a scheme `S` such that every
> weakly associated point of `X` is a point of codimension `0` and every quasi-compact open of
> every étale scheme chart of `X` has finitely many irreducible components (the condition of
> Stacks 0BB1).  Then for every geometric point `x̄` of `X` the set `𝒮_x̄` of germs of regular
> sections is exactly the set of nonzerodivisors of the étale local ring `𝒪_{X, x̄}`.

```lean
theorem regularSectionsStalk_eq_nonZeroDivisors (X : AlgebraicSpaces B S hS)
    (hwa : ∀ z ∈ weaklyAssociatedPointsOfSpace B S hS X, localRingDimension B S hS z = 0)
    (hfin : HasLocallyFiniteIrreducibleComponents B S hS X.1)
    (x : GeometricPoint B S hS X.1) :
    regularSectionsStalk x = (etaleLocalRing B S hS X.1 x)⁰
```

**`AlgebraicGeometry.Space.isFractionRing_meromorphicStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicStalks.lean, line 608](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicStalks.lean#L608). The attribute's comment: “part (4): for a geometric point the stalk of the sheaf of meromorphic functions is the total ring of fractions of the étale local ring”.

> **Stacks 0EN6, part (4).** Let `X` be an algebraic space over a scheme `S` such that every
> weakly associated point of `X` is a point of codimension `0` and every quasi-compact open of
> every étale scheme chart of `X` has finitely many irreducible components (the condition of
> Stacks 0BB1).  Then for every geometric point `x̄` of `X` the stalk `𝒦_{X, x̄}` of the sheaf of
> meromorphic functions is the total ring of fractions of the étale local ring `𝒪_{X, x̄}`.
>
> The stalk of `𝒦_X` is the stalk of the presheaf of sectionwise localizations, which is the
> localization of `𝒪_{X, x̄}` at `𝒮_x̄`; by part (3) that multiplicative subset is exactly the
> set of nonzerodivisors of `𝒪_{X, x̄}`.

```lean
theorem isFractionRing_meromorphicStalk
    (hwa : ∀ z ∈ weaklyAssociatedPointsOfSpace B S hS X, localRingDimension B S hS z = 0)
    (hfin : HasLocallyFiniteIrreducibleComponents B S hS X.1) :
    letI : Algebra (etaleLocalRing B S hS X.1 x) (meromorphicStalk B S hS X x) :=
      (toMeromorphicStalk B S hS X x).toAlgebra
    IsFractionRing (etaleLocalRing B S hS X.1 x) (meromorphicStalk B S hS X x)
```

## Tag 0EN7, a lemma

[Tag 0EN7](https://stacks.math.columbia.edu/tag/0EN7) in the Stacks Project.

**`AlgebraicGeometry.Space.nonempty_meromorphicFunctionSheaf_iso_representedMeromorphicAlgebra`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicRepresentableComparison.lean, line 373](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicRepresentableComparison.lean#L373).

> **Stacks 0EN7.**  Let `X` be an algebraic space over `S` all of whose weakly associated
> points are points of codimension `0` and which satisfies the condition of Stacks 0BB1, and let
> `X` be representable by a scheme `X₀`.  Then the sheaf of meromorphic functions `𝒦_X` is, as a
> sheaf of `𝒪_X`-algebras, the algebra on the small étale site of `X` associated to the
> quasi-coherent algebra `𝒦_{X₀}` of meromorphic functions on `X₀`.

```lean
public theorem nonempty_meromorphicFunctionSheaf_iso_representedMeromorphicAlgebra
    (codimZero : ∀ z ∈ weaklyAssociatedPointsOfSpace B S hS X, localRingDimension B S hS z = 0)
    (finiteComponents : HasLocallyFiniteIrreducibleComponents B S hS X.1)
    (i : X.1 ≅ yoneda.obj T) :
    Nonempty (Under.mk (toMeromorphicFunctionSheaf B S hS X.1 X.2).hom ≅
      representedMeromorphicAlgebra B S hS X T codimZero finiteComponents i)
```

## Tag 0EN8, a definition

[Tag 0EN8](https://stacks.math.columbia.edu/tag/0EN8) in the Stacks Project.

**`AlgebraicGeometry.Space.PullbacksMeromorphicSections`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicPullback.lean, line 145](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicPullback.lean#L145).

> **Stacks 0EN8.** *Pullbacks of meromorphic functions are defined for `f : X ⟶ Y`* when, for
> every commuting square of an étale chart `U` of `X` over an étale chart `V` of `Y`, the pullback
> `f^♯` along the underlying morphism of schemes carries every regular section of `𝒪_Y` over `V`
> to a regular section of `𝒪_X` over `U`.

```lean
abbrev PullbacksMeromorphicSections {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y) : Prop
```

## Tag 0EN9, a lemma

[Tag 0EN9](https://stacks.math.columbia.edu/tag/0EN9) in the Stacks Project.

**`AlgebraicGeometry.Space.pullbacksMeromorphicSections_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicPullback.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicPullback.lean#L156). The attribute's comment: “part (2): flat”. References: EGA IV (20.3.13), “flat: pullback defined”.

> **Stacks 0EN9, part (2).** Pullbacks of meromorphic functions are defined along a flat
> morphism `f : X ⟶ Y`: the morphism of schemes underlying a commuting square of étale charts of
> `f` is flat, and pullbacks of meromorphic functions are defined along a flat morphism of
> schemes.

```lean
theorem pullbacksMeromorphicSections_of_flat {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hf : IsFlat B S hS f) : PullbacksMeromorphicSections B S hS f
```

**`AlgebraicGeometry.Space.pullbacksMeromorphicSections_of_mapsTo_codimensionZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicPullbackWeaklyAssociated.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicPullbackWeaklyAssociated.lean#L70). The attribute's comment: “part (1): weakly associated points of X mapped to codimension-zero points of Y”.

> **Stacks 0EN9, part (1).** Pullbacks of meromorphic functions are defined along a morphism
> `f : X ⟶ Y` of algebraic spaces carrying every weakly associated point of `X` to a point of
> codimension `0` of `Y`.
>
> Over a commuting square of étale scheme charts the claim is the scheme-level criterion of
> Stacks 02OU: a weakly associated point of the chart of `X` lies over a weakly associated point
> of `X`, which is carried to a point of codimension `0` of `Y`, and such a point is a generic
> point of an irreducible component on the chart of `Y` above it.

```lean
theorem pullbacksMeromorphicSections_of_mapsTo_codimensionZero
    {X Y : AlgebraicSpaces B S hS} (f : X.1 ⟶ Y.1)
    (hf : ∀ x ∈ weaklyAssociatedPointsOfSpace B S hS X,
      localRingDimension B S hS (pointsMap B S hS X.1 f x) = 0) :
    PullbacksMeromorphicSections B S hS f
```

## Tag 0ENA, a lemma

[Tag 0ENA](https://stacks.math.columbia.edu/tag/0ENA) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_codimensionZeroPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CodimensionZeroSchematicLocus.lean, line 361](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CodimensionZeroSchematicLocus.lean#L361). The attribute's comment: “the assertion of the statement that the construction makes sense: the set of codimension-zero points is contained in the schematic locus, so that the local rings and the morphisms j\_η are defined”.

> **Stacks 0ENA, the assertion that the construction makes sense.** Let `X` be an algebraic
> space over a scheme `S` satisfying hypotheses (b) and (c) of Stacks 0ENA — the equivalent
> conditions of Stacks 0BB1, and representability of every codimension-zero point by a
> monomorphism from the spectrum of a field.  Then `X` has a dense open subspace which is a
> scheme and whose point set contains the whole of `X⁰`.
>
> Consequently the local rings `𝒪_{X, η}` and the canonical morphisms
> `j_η : Spec(𝒪_{X, η}) ⟶ X` for `η ∈ X⁰` are defined; they are
> `AlgebraicGeometry.Space.CodimensionZeroPresentation.stalk` and
> `AlgebraicGeometry.Space.CodimensionZeroPresentation.fromSpecStalk`.

```lean
theorem exists_codimensionZeroPresentation
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hfin : HasLocallyFiniteIrreducibleComponents B S hS X)
    (hmono : HasMonomorphicCodimensionZeroPoints B S hS X) :
    Nonempty (CodimensionZeroPresentation B S hS X)
```

**`AlgebraicGeometry.Space.codimensionZero_mem_schematicLocus_of_hasLocallyFiniteIrreducibleComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/CodimensionZeroSchematicLocus.lean, line 387](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/CodimensionZeroSchematicLocus.lean#L387). The attribute's comment: “the assertion of the statement that the construction makes sense, read on the schematic locus of Tag 03JH”.

> **Stacks 0ENA, the assertion that the construction makes sense**, stated with the
> schematic locus of Stacks 03JH: under hypotheses (b) and (c) of Stacks 0ENA every point of
> codimension `0` of `X` lies in the schematic locus.
>
> The dense open subspace of `AlgebraicGeometry.Space.exists_codimensionZeroPresentation` is a
> representable open subspace, hence contained in the schematic locus.

```lean
theorem codimensionZero_mem_schematicLocus_of_hasLocallyFiniteIrreducibleComponents
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hfin : HasLocallyFiniteIrreducibleComponents B S hS X)
    (hmono : HasMonomorphicCodimensionZeroPoints B S hS X)
    (x : points B S hS X) (hx : localRingDimension B S hS x = 0) :
    x ∈ Set.range (pointsMap B S hS (schematicLocus B S hS X).toFunctor
      (schematicLocus B S hS X).ι)
```

**`AlgebraicGeometry.Space.CodimensionZeroPresentation.exists_codimensionZeroPresentation_isIso_genericPointComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicCodimensionZeroProduct.lean, line 373](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicCodimensionZeroProduct.lean#L373). The attribute's comment: “the first conclusion: the sheaf of meromorphic functions is the direct sum, and equally the product, over the codimension-zero points of the direct images of the local rings there, through the canonical comparisons”.

> **Stacks 0ENA, the first conclusion.** Let `X` be an algebraic space over a scheme `S` such
> that
>
> * (a) every weakly associated point of `X` is a point of codimension `0`,
> * (b) every quasi-compact open of every étale scheme chart of `X` has finitely many irreducible
>   components, the condition of Stacks 0BB1, and
> * (c) every point of codimension `0` of `X` is represented by a monomorphism from the spectrum
>   of a field.
>
> Then the local rings `𝒪_{X, η}` at the points `η ∈ X⁰` of codimension `0` and the canonical
> morphisms `j_η : Spec(𝒪_{X, η}) ⟶ X` are defined — this is the presentation `P` of the
> schematic locus whose existence is `AlgebraicGeometry.Space.exists_codimensionZeroPresentation`
> — and the sheaf of meromorphic functions `𝒦_X` is both the direct sum and the product over `X⁰`
> of the direct images `j_{η, *}𝒪_{X, η}`:
>
> `𝒦_X = ⨁_{η ∈ X⁰} j_{η, *}𝒪_{X, η} = ∏_{η ∈ X⁰} j_{η, *}𝒪_{X, η}`.
>
> The two identifications are the canonical comparisons: the one into the product has components
> the canonical maps `𝒦_X ⟶ j_{η, *}𝒪_{X, η}` of
> `AlgebraicGeometry.Space.CodimensionZeroPresentation.genericPointComparison`, and the one out of
> the direct sum is `CategoryTheory.Limits.sigmaPiComparison`, the identity on the diagonal and
> zero off it.

```lean
theorem exists_codimensionZeroPresentation_isIso_genericPointComparison
    (hwa : ∀ z ∈ weaklyAssociatedPointsOfSpace B S hS X, localRingDimension B S hS z = 0)
    (hfin : HasLocallyFiniteIrreducibleComponents B S hS X.1)
    (hmono : HasMonomorphicCodimensionZeroPoints B S hS X.1) :
    ∃ P : CodimensionZeroPresentation B S hS X.1,
      IsIso P.genericPointModuleComparisonPi ∧
        letI : DecidableEq (CodimensionZeroPoints B S hS X.1) := Classical.decEq _
        letI := P.hasCoproduct_genericPointModule
        IsIso (sigmaPiComparison fun η : CodimensionZeroPoints B S hS X.1 =>
          P.genericPointModule η.2)
```

**`AlgebraicGeometry.Space.CodimensionZeroPresentation.exists_codimensionZeroPresentation_isIso_meromorphicSectionComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicCodimensionZeroSectionProduct.lean, line 380](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicCodimensionZeroSectionProduct.lean#L380). The attribute's comment: “the second conclusion: for every quasi-coherent module the sheaf of its meromorphic sections is the direct sum, and equally the product, over the codimension-zero points of the direct images of its inverse images there, through the canonical comparisons”.

> **Stacks 0ENA, the second conclusion.** Let `X` be an algebraic space over a scheme `S` such
> that
>
> * (a) every weakly associated point of `X` is a point of codimension `0`,
> * (b) every quasi-compact open of every étale scheme chart of `X` has finitely many irreducible
>   components, the condition of Stacks 0BB1, and
> * (c) every point of codimension `0` of `X` is represented by a monomorphism from the spectrum
>   of a field.
>
> Then the local rings `𝒪_{X, η}` at the points `η ∈ X⁰` of codimension `0` and the canonical
> morphisms `j_η : Spec(𝒪_{X, η}) ⟶ X` are defined — this is the presentation `P` of the
> schematic locus whose existence is `AlgebraicGeometry.Space.exists_codimensionZeroPresentation`
> — and for every quasi-coherent `𝒪_X`-module `F` the sheaf `𝒦_X(F)` of meromorphic sections of
> `F` is both the direct sum and the product over `X⁰` of the direct images `j_{η, *}j_η^*F` of the
> inverse images of `F`:
>
> `𝒦_X(F) = ⨁_{η ∈ X⁰} j_{η, *}j_η^*F = ∏_{η ∈ X⁰} j_{η, *}j_η^*F`.
>
> The two identifications are the canonical comparisons: the one into the product is
> `AlgebraicGeometry.Space.CodimensionZeroPresentation.meromorphicSectionGenericPointComparisonPi`,
> the transpose across sheafification of the family `a ⊗ s ↦ a · s|_{U ×_X Spec(𝒪_{X, η})}`, and
> the one out of the direct sum is `CategoryTheory.Limits.sigmaPiComparison`, the identity on the
> diagonal and zero off it.

```lean
theorem exists_codimensionZeroPresentation_isIso_meromorphicSectionComparison
    (hwa : ∀ z ∈ weaklyAssociatedPointsOfSpace B S hS X, localRingDimension B S hS z = 0)
    (hfin : HasLocallyFiniteIrreducibleComponents B S hS X.1)
    (hmono : HasMonomorphicCodimensionZeroPoints B S hS X.1) :
    ∃ P : CodimensionZeroPresentation B S hS X.1,
      ∀ F : Modules.{u, u} B S hS X.1 X.2, F.IsQuasicoherentOnSite →
        IsIso (P.meromorphicSectionGenericPointComparisonPi F) ∧
          letI : DecidableEq (CodimensionZeroPoints B S hS X.1) := Classical.decEq _
          letI := P.hasCoproduct_genericPointMeromorphicModule F
          IsIso (sigmaPiComparison fun η : CodimensionZeroPoints B S hS X.1 =>
            SheafOfModules.uliftObj.{_, _, _, _, u + 1}
              (P.genericPointMeromorphicModule η.2 F))
```

**`AlgebraicGeometry.Space.exists_ringEquiv_rationalFunctions_meromorphicFunction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SpaceRationalFunctionsMeromorphic.lean, line 475](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SpaceRationalFunctionsMeromorphic.lean#L475). The attribute's comment: “the third conclusion: the ring of rational functions of the space is its ring of meromorphic functions, R(X) = Γ(X, 𝒦\_X), through the comparison that reads a rational function regular on a dense open subspace as a meromorphic function on every étale chart lying in that subspace”. References: EGA IV (20.1.13), “Algebraic clause only”.

> **Stacks 0ENA, the third conclusion.**  Let `X` be an algebraic space over a scheme `S`
> such that (a) every weakly associated point of `X` has codimension `0`, (b) the irreducible
> components of `X` are locally finite, and (c) every codimension-zero point of `X` is
> representable by a monomorphism from the spectrum of a field.  Then the ring `R(X)` of rational
> functions of `X` — the classes, modulo agreement on a dense open subspace, of morphisms to the
> relative affine line defined on a dense open subspace, of Stacks 0EMP — is the ring
> `Γ(X, 𝒦_X)` of meromorphic functions on `X`, the global sections of the sheaf of meromorphic
> functions of Stacks 0EN3.
>
> The comparison is the canonical one: a rational function represented by a morphism `ν` regular
> on a dense open subspace `W` is sent to the meromorphic function whose value at an étale chart
> `U` lying in `W` is the image in `𝒦_X(U)` of the coordinate of `ν` at `U`, and the displayed
> equation says exactly that.  It is a ring homomorphism by
> `AlgebraicGeometry.Space.rationalToMeromorphicRingHom`, injective by
> `AlgebraicGeometry.Space.injective_rationalToMeromorphic` and surjective by
> `AlgebraicGeometry.Space.surjective_rationalToMeromorphic`.

```lean
theorem exists_ringEquiv_rationalFunctions_meromorphicFunction
    (hwa : ∀ z ∈ weaklyAssociatedPointsOfSpace B S hS X, localRingDimension B S hS z = 0)
    (hfin : HasLocallyFiniteIrreducibleComponents B S hS X.1)
    (hmono : HasMonomorphicCodimensionZeroPoints B S hS X.1) :
    ∃ e : rationalFunctions B S hS X.2 ≃+* MeromorphicFunction B S hS X.1 X.2,
      ∀ (f : PartialMap B S hS X.2 (affineLineFunctor B S hS))
        (U : SmallEtale B S hS X.1) (τ : yoneda.obj U.obj.left ⟶ f.domain.toFunctor),
        τ ≫ f.domain.ι = U.1.hom →
        (e (PartialMap.toRationalMap B S hS f)).val (op U) =
          ((toMeromorphicFunctionSheaf B S hS X.1 X.2).hom.app (op U)).hom
            (affineLineCoordinate B S hS (op U.obj.left)
              (f.hom.app (op U.obj.left) (yonedaEquiv τ)))
```

## Tag 0ENB, a definition

[Tag 0ENB](https://stacks.math.columbia.edu/tag/0ENB) in the Stacks Project.

**`AlgebraicGeometry.Space.IsRegularMeromorphicSection`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicSections.lean, line 168](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicSections.lean#L168). References: EGA IV (20.1.8), “regular section defn”.

> A meromorphic section `s` of a sheaf of `𝒪_F`-modules `L` is *regular* when the induced map
> `𝒦_F ⟶ 𝒦_F(L)`, multiplication by `s`, is injective; this is tested on every étale chart of `F`.

```lean
noncomputable abbrev IsRegularMeromorphicSection (hF : IsAlgebraicSpace B S hS F)
    (L : Modules.{u, max u z} B S hS F hF)
    (s : MeromorphicSection.{u, z} B S hS F hF L) : Prop
```

## Tag 0ENC, a lemma

[Tag 0ENC](https://stacks.math.columbia.edu/tag/0ENC) in the Stacks Project.

**`AlgebraicGeometry.Space.isRegularMeromorphicSection_pullbackMeromorphicSectionOfGood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardOfDivisorPullback.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Chow/ProperPushforwardOfDivisorPullback.lean#L149). The attribute's comment: “part (2) in the vocabulary of this chapter: the pullback f^*s of a regular meromorphic section of an invertible sheaf on a good algebraic space is regular”.

> **Stacks 0ENC, part (2), in this chapter's vocabulary.** The pullback `f^*s` of a nonzero —
> that is, regular — meromorphic section of an invertible `𝒪_Y`-module `ℒ` is again a nonzero
> meromorphic section, now of `f^*ℒ`.

```lean
theorem isRegularMeromorphicSection_pullbackMeromorphicSectionOfGood
    (hL : IsInvertibleSheaf D sY hY L)
    (hσ : IsRegularMeromorphicSection.{u, u} D.site D.base D.base_mem Y hY.1 L σ) :
    IsRegularMeromorphicSection.{u, u} D.site D.base D.base_mem X hX.1
      (pullbackSheaf D sY hY sX hX (spaceMorphismOfGood D sX hX sY hY (f := f)) L)
      (pullbackMeromorphicSectionOfGood D sX hX sY hY L σ hPull)
```

**`AlgebraicGeometry.Space.chartMeromorphicFunctionPullback`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicFunctionsChartPullback.lean, line 140](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicFunctionsChartPullback.lean#L140). The attribute's comment: “part (1), chartwise on the SHEAVES of meromorphic functions: the fraction rule a/b ↦ f♯a/f♯b over an étale chart diagram as a homomorphism 𝒦\_Y(V) ⟶ 𝒦\_X(U), where AlgebraicGeometry.Space.chartPullbackMeromorphicFunctions is the same rule on the presheaves of sectionwise localizations. This is the coefficient rule for part (1) read through the second of the two descriptions of 𝒦(F) in Stacks 0EN5, the sheafification of F ⊗\_𝒪 𝒦, which is the one AlgebraicGeometry.Space.MeromorphicSection and hence part (2) use. The global map Γ(Y, 𝒦\_Y(F)) ⟶ Γ(X, 𝒦\_X(f^*F)) of part (1) is asserted for the first description by AlgebraicGeometry.Space.pullbackSheafifiedRegularSections, and for the second by AlgebraicGeometry.Space.pullbackMeromorphicSection, which is built over this rule. Part (2) is proved for an invertible module by AlgebraicGeometry.Space.isRegularMeromorphicSection\_pullbackMeromorphicSection, over that same description, and is not asserted here”.

> **The chartwise pullback of meromorphic functions on the sheaves.**  Over a commuting square
> of étale charts `U` of `X` above `V` of `Y` the comparison `𝒦_Y ⟶ f_*𝒦_X` projects to a
> homomorphism of commutative rings `𝒦_Y(V) ⟶ 𝒦_X(U)`.

```lean
noncomputable def chartMeromorphicFunctionPullback (d : ChartDiagram B S hS X.1 Y.1 f.hom) :
    (meromorphicFunctionSheaf B S hS Y.1 Y.2).obj.obj (op d.V) →+*
      (meromorphicFunctionSheaf B S hS X.1 X.2).obj.obj (op d.U)
```

**`AlgebraicGeometry.Space.chartPullbackMeromorphicFunctions`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicPullback.lean, line 238](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicPullback.lean#L238). The attribute's comment: “part (1), chartwise: the local fraction rule a/b ↦ f♯a/f♯b over an étale chart diagram, on the presheaf of sectionwise localizations. The global map Γ(Y, 𝒦\_Y(F)) ⟶ Γ(X, 𝒦\_X(f^*F)) of part (1) is asserted for ONE of the two spellings of 𝒦(F): AlgebraicGeometry.Space.pullbackSheafifiedRegularSections gives it with 𝒦(F) read as the first description in Stacks 0EN5, the sheafification of the presheaf of sectionwise localizations. It is asserted for AlgebraicGeometry.Space.MeromorphicSection, which realizes Stacks 0EN5 through the other description there, the sheafification of F ⊗\_𝒪 𝒦, by AlgebraicGeometry.Space.pullbackMeromorphicSection. Stacks 0EMD, which identifies the two descriptions, is not proved and neither map uses it. Part (2), stated through AlgebraicGeometry.Space.IsRegularMeromorphicSection, is not asserted here; it is proved for an invertible module by AlgebraicGeometry.Space.isRegularMeromorphicSection\_pullbackMeromorphicSection. Erratum: part (2) as printed reads 'invertible 𝒪\_X-module', but pulling back along f : X ⟶ Y needs an 𝒪\_Y-module, which is what the scheme-level form of the lemma, 02OY, says”.

> **The local fraction rule `a/b ↦ f^♯a/f^♯b`.**  When pullbacks of meromorphic functions
> are defined for `f`, the pullback along a chart diagram carries the sectionwise localization
> `𝒮_Y(V)⁻¹𝒪_Y(V)` into `𝒮_X(U)⁻¹𝒪_X(U)`: a denominator regular over `V` pulls back to one
> regular over `U`, so the universal property of the localization applies.

```lean
noncomputable def chartPullbackMeromorphicFunctions
    (hf : PullbacksMeromorphicSections B S hS f) (d : ChartDiagram B S hS X Y f) :
    (regularSectionsSubpresheaf B S hS Y hY).localizationPresheaf.obj (op d.V) →+*
      (regularSectionsSubpresheaf B S hS X hX).localizationPresheaf.obj (op d.U)
```

**`AlgebraicGeometry.Space.fmapMeromorphicFunctions`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicPullback.lean, line 328](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicPullback.lean#L328). The attribute's comment: “part (1), chartwise: the fraction rule is canonical, being an f-map of Stacks 03G3 on the presheaves of sectionwise localizations. The global pullback map of part (1) is asserted for the sheafification of those presheaves, the first of the two descriptions of 𝒦 in Stacks 0EN5, by AlgebraicGeometry.Space.pullbackSheafifiedRegularSections, and for the second, AlgebraicGeometry.Space.MeromorphicSection, by AlgebraicGeometry.Space.pullbackMeromorphicSection. Part (2) is not asserted here; it is proved for an invertible module by AlgebraicGeometry.Space.isRegularMeromorphicSection\_pullbackMeromorphicSection”.

> The chartwise fraction rules assemble into an `f`-map of presheaves of sets from the
> sectionwise localization `𝒮_Y⁻¹𝒪_Y` to `𝒮_X⁻¹𝒪_X`, in the sense of Stacks 03G3: pullback of
> meromorphic functions is compatible with étale restriction of both charts of a diagram.

```lean
noncomputable def fmapMeromorphicFunctions (hf : PullbacksMeromorphicSections B S hS f) :
    FMap B S hS X Y f
      ((regularSectionsSubpresheaf B S hS X hX).localizationPresheaf ⋙
        CategoryTheory.forget CommRingCat.{u})
      ((regularSectionsSubpresheaf B S hS Y hY).localizationPresheaf ⋙
        CategoryTheory.forget CommRingCat.{u})
```

**`AlgebraicGeometry.Space.pullbackSheafifiedRegularSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicPullbackGlobalSections.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicPullbackGlobalSections.lean#L150). The attribute's comment: “part (1), for the first of the two descriptions of the sheaf of meromorphic sections in Stacks 0EN5: the global map Γ(Y, 𝒦\_Y(F)) ⟶ Γ(X, 𝒦\_X(f^*F)) with 𝒦(F) taken to be the sheafification of the presheaf of sectionwise localizations U ↦ 𝒮(U)⁻¹F(U). The same map for AlgebraicGeometry.Space.MeromorphicSection, which realizes Stacks 0EN5 through the other description there, the sheafification of the extension of scalars F ⊗\_𝒪 𝒦, is AlgebraicGeometry.Space.pullbackMeromorphicSection. Stacks 0EMD, which identifies the two descriptions, is not proved and neither map uses it. Additivity of the map is not asserted, and neither is part (2), which is stated through AlgebraicGeometry.Space.IsRegularMeromorphicSection and proved for an invertible module by AlgebraicGeometry.Space.isRegularMeromorphicSection\_pullbackMeromorphicSection”.

> **Stacks 0ENC, part (1), for the sheafification of the sectionwise localizations.**  When
> pullbacks of meromorphic functions are defined for `f`, there is a canonical map on global
> sections
>
> `Γ(Y, 𝒦_Y(M)) ⟶ Γ(X, 𝒦_X(f^*M))`
>
> with the sheaf of meromorphic sections taken as Stacks 0EN5 describes it, the sheafification of
> the presheaf of sectionwise localizations `U ↦ 𝒮(U)⁻¹M(U)`.
>
> It is the chartwise fraction rule `m/b ↦ (f^*m)/(f^♯b)` of
> `AlgebraicGeometry.Space.chartPullbackMeromorphicSections`, carried along three identifications:
> the descent of Stacks 03G4 for a presheaf of sections on the target
> (`AlgebraicGeometry.Space.meromorphicSectionsDescendedHom`), the extension of a morphism into a
> sheaf over the sheafification of its source
> (`AlgebraicGeometry.Space.sheafifyForgetHomEquiv`), and the identification of the global
> sections of a direct image with those of the sheaf
> (`AlgebraicGeometry.Space.equivSectionsSpacesDirectImage`).
>
> Only the additive structure of the sectionwise localizations is used, so the map is produced on
> the underlying sets; it is a map of sets of global sections and is not here asserted to be
> additive.

```lean
noncomputable def pullbackSheafifiedRegularSections
    (hf : PullbacksMeromorphicSections B S hS f.hom) :
    (regularSectionsLocalizationModuleSheafSet B S hS Y.1 Y.2 M).obj.sections →
      (regularSectionsLocalizationModuleSheafSet B S hS X.1 X.2
        ((modulePullback B S hS f).obj M)).obj.sections
```

**`AlgebraicGeometry.Space.chartPullbackMeromorphicSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicPullbackModule.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicPullbackModule.lean#L202). The attribute's comment: “part (1), chartwise for an arbitrary sheaf of 𝒪\_Y-modules F: the local fraction rule m/b ↦ (f^*m)/(f♯b) on the sectionwise localizations over an étale chart diagram. This generalizes the structure-sheaf case AlgebraicGeometry.Space.chartPullbackMeromorphicFunctions from F = 𝒪\_Y to an arbitrary F. The global map Γ(Y, 𝒦\_Y(F)) ⟶ Γ(X, 𝒦\_X(f^*F)) of part (1) is asserted for ONE of the two spellings of 𝒦(F): AlgebraicGeometry.Space.pullbackSheafifiedRegularSections gives it with 𝒦(F) read as the first description in Stacks 0EN5, the sheafification of this presheaf of sectionwise localizations, and AlgebraicGeometry.Space.pullbackMeromorphicSection gives it for the other description there, the sheafification of F ⊗\_𝒪 𝒦, which is the one AlgebraicGeometry.Space.MeromorphicSection uses. Stacks 0EMD, which identifies the two descriptions, is not proved and neither map uses it. Part (2), stated through AlgebraicGeometry.Space.IsRegularMeromorphicSection, is not asserted here; it is proved for an invertible module by AlgebraicGeometry.Space.isRegularMeromorphicSection\_pullbackMeromorphicSection”.

> **The local fraction rule `m/b ↦ (f^*m)/(f^♯b)`.**  When pullbacks of meromorphic functions
> are defined for `f`, the pullback along a chart diagram carries the sectionwise localization
> `𝒮_Y(V)⁻¹M(V)` of a sheaf of `𝒪_Y`-modules `M` into `𝒮_X(U)⁻¹(f^*M)(U)`: the numerator is
> pulled back by the chart component of the unit of the Stacks 03D7 adjunction and the
> denominator by the fraction rule on the structure sheaf, which inverts it.

```lean
noncomputable def chartPullbackMeromorphicSections
    (hf : PullbacksMeromorphicSections B S hS f.hom)
    (d : ChartDiagram B S hS X.1 Y.1 f.hom) :
    (regularSectionsLocalizationModule B S hS Y.1 Y.2 M).obj (op d.V) →+
      (regularSectionsLocalizationModule B S hS X.1 X.2
        ((modulePullback B S hS f).obj M)).obj (op d.U)
```

**`AlgebraicGeometry.Space.fmapMeromorphicSections`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicPullbackModule.lean, line 323](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicPullbackModule.lean#L323). The attribute's comment: “part (1), chartwise for an arbitrary sheaf of 𝒪\_Y-modules F: the fraction rule m/b ↦ (f^*m)/(f♯b) is canonical, being an f-map of Stacks 03G3 from the presheaf of sectionwise localizations of F to that of f^*F. This generalizes the structure-sheaf case AlgebraicGeometry.Space.fmapMeromorphicFunctions from F = 𝒪\_Y to an arbitrary F. It is a statement about the presheaves of sectionwise localizations, not about their sheafifications; the global map Γ(Y, 𝒦\_Y(F)) ⟶ Γ(X, 𝒦\_X(f^*F)) of part (1) that this f-map descends to is AlgebraicGeometry.Space.pullbackSheafifiedRegularSections, which is part (1) with 𝒦(F) read as the first description in Stacks 0EN5, the sheafification of these sectionwise localizations. Part (1) for AlgebraicGeometry.Space.MeromorphicSection, which realizes Stacks 0EN5 through the other description there, the sheafification of F ⊗\_𝒪 𝒦, is AlgebraicGeometry.Space.pullbackMeromorphicSection, built over the same rule taken over the sheaf 𝒦 instead of the presheaf 𝒮⁻¹𝒪. Part (2), stated through AlgebraicGeometry.Space.IsRegularMeromorphicSection, is not asserted here; it is proved for an invertible module by AlgebraicGeometry.Space.isRegularMeromorphicSection\_pullbackMeromorphicSection”.

> The chartwise fraction rules for a sheaf of `𝒪_Y`-modules `M` assemble into an `f`-map of
> presheaves of sets from the sectionwise localization `𝒮_Y⁻¹M` to `𝒮_X⁻¹(f^*M)`, in the sense of
> Stacks 03G3: the rule `m/b ↦ (f^*m)/(f^♯b)` is compatible with étale restriction of both charts
> of a diagram.  This is the module-level form of
> `AlgebraicGeometry.Space.fmapMeromorphicFunctions`, which is the case `M = 𝒪_Y`.

```lean
noncomputable def fmapMeromorphicSections
    (hf : PullbacksMeromorphicSections B S hS f.hom) :
    FMap B S hS X.1 Y.1 f.hom
      ((regularSectionsLocalizationModule B S hS X.1 X.2
          ((modulePullback B S hS f).obj M)).presheaf ⋙
        CategoryTheory.forget AddCommGrpCat.{u})
      ((regularSectionsLocalizationModule B S hS Y.1 Y.2 M).presheaf ⋙
        CategoryTheory.forget AddCommGrpCat.{u})
```

**`AlgebraicGeometry.Space.pullbackMeromorphicSection`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicSectionGlobalPullback.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicSectionGlobalPullback.lean#L200). The attribute's comment: “part (1): the global map Γ(Y, 𝒦\_Y(F)) ⟶ Γ(X, 𝒦\_X(f^*F)) on AlgebraicGeometry.Space.MeromorphicSection, the meromorphic sections of Stacks 0EN5 as the library spells them -- global sections of the sheafification of F ⊗\_𝒪 𝒦. AlgebraicGeometry.Space.pullbackSheafifiedRegularSections is the same map for the other description in Stacks 0EN5, the sheafification of the presheaf of sectionwise localizations. Additivity and semilinearity of this map are AlgebraicGeometry.Space.pullbackMeromorphicSection\_eval\_add and AlgebraicGeometry.Space.pullbackMeromorphicSection\_eval\_smul\_chartDiagram, and global additivity is AlgebraicGeometry.Space.pullbackMeromorphicSection\_add; part (2) for an invertible module is AlgebraicGeometry.Space.isRegularMeromorphicSection\_pullbackMeromorphicSection”.

> **Stacks 0ENC, part (1).**  When pullbacks of meromorphic functions are defined for `f`,
> there is a canonical map on global meromorphic sections
>
> `Γ(Y, 𝒦_Y(M)) ⟶ Γ(X, 𝒦_X(f^*M))`
>
> with `𝒦(M)` the sheaf of meromorphic sections of Stacks 0EN5,
> `AlgebraicGeometry.Space.meromorphicSectionSheaf`, and a meromorphic section a global section of
> it, `AlgebraicGeometry.Space.MeromorphicSection`.
>
> It is the chartwise rule `m ⊗ a ↦ (f^*m) ⊗ (f^♯a)` of
> `AlgebraicGeometry.Space.chartPullbackMeromorphicSectionsSheaf`, carried along three
> identifications: the descent of Stacks 03G4 for a presheaf of sections on the target
> (`AlgebraicGeometry.Space.meromorphicSectionSheafDescendedHom`), the extension of a morphism
> into a sheaf over the sheafification of its source
> (`AlgebraicGeometry.Space.sheafifyForgetHomEquiv`), and the identification of the global
> sections of a direct image with those of the sheaf
> (`AlgebraicGeometry.Space.equivSectionsSpacesDirectImage`).
>
> Only the additive structure of `M ⊗_{𝒪} 𝒦` is used, so the map is produced on the underlying
> sets and nothing in the construction is a map of abelian groups.  That it is nonetheless
> additive and `𝒦`-semilinear is
> `AlgebraicGeometry.Space.pullbackMeromorphicSection_eval_add` and
> `AlgebraicGeometry.Space.pullbackMeromorphicSection_eval_smul_chartDiagram`, proved from its
> values; `AlgebraicGeometry.Space.pullbackMeromorphicSection_add` is global additivity against
> the group structure on global sections.

```lean
noncomputable def pullbackMeromorphicSection :
    MeromorphicSection.{u, u} B S hS Y.1 Y.2 M →
      MeromorphicSection.{u, u} B S hS X.1 X.2 ((modulePullback B S hS f).obj M)
```

**`AlgebraicGeometry.Space.pullbackMeromorphicSection_eval_add`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicSectionGlobalPullbackLinear.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicSectionGlobalPullbackLinear.lean#L297). The attribute's comment: “the algebra of the part (1) map, which its construction leaves unasserted: the global map on meromorphic sections is additive”.

> **The global pullback map of Stacks 0ENC, part (1) is additive.**  Let `w` be a meromorphic
> section of `M` whose value over every étale scheme chart of `Y` is the sum of the values of `s`
> and `s'` there.  Then the value of the pullback of `w` over every étale scheme chart of `X` is
> the sum of the values of the pullbacks of `s` and `s'`.
>
> A meromorphic section is a section of a sheaf of modules, a type carrying no module structure, so
> this is the assertion that the global map of part (1) is additive.
>
> Every chart of `X` is covered by the charts of `X` of affine commuting squares
> (`AlgebraicGeometry.Space.exists_affine_chartDiagram_ofArrows`), over which the identity is
> `AlgebraicGeometry.Space.pullbackMeromorphicSection_eval_add_chartDiagram`.

```lean
theorem pullbackMeromorphicSection_eval_add
    (s s' w : MeromorphicSection.{u, u} B S hS Y.1 Y.2 M)
    (hw : ∀ V : SmallEtale B S hS Y.1, w.eval (op V) = s.eval (op V) + s'.eval (op V))
    (U : SmallEtale B S hS X.1) :
    (pullbackMeromorphicSection B S hS f M hf w).eval (op U) =
      (pullbackMeromorphicSection B S hS f M hf s).eval (op U) +
        (pullbackMeromorphicSection B S hS f M hf s').eval (op U)
```

**`AlgebraicGeometry.Space.pullbackMeromorphicSection_eval_smul_chartDiagram`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicSectionGlobalPullbackLinear.lean, line 334](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicSectionGlobalPullbackLinear.lean#L334). The attribute's comment: “the algebra of the part (1) map, which its construction leaves unasserted: the global map on meromorphic sections is semilinear over the chartwise pullback of meromorphic functions. The coefficient over the chart of X of a commuting square of affine etale charts is the image of the coefficient over its chart of Y under AlgebraicGeometry.Space.chartMeromorphicPullbackHom; a single coefficient over all of X would need the global map on meromorphic functions, which is not available”.

> **The global pullback map of Stacks 0ENC, part (1) is semilinear over the chartwise pullback
> of meromorphic functions.**  Let `d` be a commuting square of affine étale scheme charts, `d.U`
> of `X` above `d.V` of `Y`, let `c` be a meromorphic function on `d.V` and let the meromorphic
> sections `s` and `s'` of `M` satisfy `s|_{d.V} = c · s'|_{d.V}`.  Then over `d.U`
>
> `(f^*s)|_{d.U} = (f^♯c) · (f^*s')|_{d.U}`,
>
> with `f^♯` the chartwise pullback of meromorphic functions
> `AlgebraicGeometry.Space.chartMeromorphicPullbackHom`.
>
> Over a covering family of `d.U` refining the sieve over which `s'` is an honest element of
> `M ⊗_{𝒪_Y} 𝒦_Y` both values are computed by
> `AlgebraicGeometry.Space.pullbackMeromorphicSection_eval_chartDiagram`, and the identity is that
> the chartwise rule carries a coefficient to its pullback.

```lean
theorem pullbackMeromorphicSection_eval_smul_chartDiagram
    (s s' : MeromorphicSection.{u, u} B S hS Y.1 Y.2 M)
    (d : ChartDiagram B S hS X.1 Y.1 f.hom)
    (hU : IsAffine ((BigFppfOver.toScheme B S hS).obj
      ((SmallEtale.toOver B S hS X.1).obj d.U)))
    (hV : IsAffine ((BigFppfOver.toScheme B S hS).obj
      ((SmallEtale.toOver B S hS Y.1).obj d.V)))
    (c : (Stacks.SheafOfModules.Tensor.ringSheaf (meromorphicRingedSite B S hS Y.1 Y.2).O).obj.obj
      (op d.V))
    (hc : s.eval (op d.V) = c • s'.eval (op d.V)) :
    (pullbackMeromorphicSection B S hS f M hf s).eval (op d.U) =
      chartMeromorphicRingedSitePullbackHom B S hS f hf d c •
        (pullbackMeromorphicSection B S hS f M hf s').eval (op d.U)
```

**`AlgebraicGeometry.Space.pullbackMeromorphicSection_sectionsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicSectionGlobalPullbackNatural.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicSectionGlobalPullbackNatural.lean#L194). The attribute's comment: “the algebra of the part (1) map, which its construction leaves unasserted: the global map on meromorphic sections is natural in the module, for the action of the sheaf of meromorphic sections on morphisms of modules”.

> The global pullback of meromorphic sections is natural in the module: for a morphism
> `φ : M ⟶ N` of sheaves of `𝒪_Y`-modules the pullback of the image of a meromorphic section of
> `M` under `𝒦_Y(φ)` is the image of the pullback of that section under `𝒦_X(f^*φ)`.

```lean
theorem pullbackMeromorphicSection_sectionsMap (φ : M ⟶ N)
    (s : MeromorphicSection.{u, u} B S hS Y.1 Y.2 M) :
    pullbackMeromorphicSection B S hS f N hf
        (SheafOfModules.sectionsMap (meromorphicSectionSheafMap B S hS Y.1 Y.2 φ) s) =
      SheafOfModules.sectionsMap
        (meromorphicSectionSheafMap B S hS X.1 X.2 ((modulePullback B S hS f).map φ))
        (pullbackMeromorphicSection B S hS f M hf s)
```

**`AlgebraicGeometry.Space.isRegularMeromorphicSection_pullbackMeromorphicSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicSectionPullbackRegular.lean, line 215](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MeromorphicSectionPullbackRegular.lean#L215). The attribute's comment: “part (2)”.

> Let `f : X ⟶ Y` be a morphism of algebraic spaces for which pullbacks of meromorphic
> functions are defined, let `L` be an invertible `𝒪_Y`-module and let `s` be a regular meromorphic
> section of `L`. Then the pullback `f^*s` is a regular meromorphic section of the invertible
> `𝒪_X`-module `f^*L`.

```lean
theorem isRegularMeromorphicSection_pullbackMeromorphicSection (f : X ⟶ Y)
    (hf : PullbacksMeromorphicSections B S hS f.hom) (L : Modules.{u, u} B S hS Y.1 Y.2)
    (hL : AlgebraicGeometry.SheafOfModules.IsInvertible (structureCommRings B S hS Y)
      (structureRingSheaf B S hS Y).property L)
    (s : MeromorphicSection.{u, u} B S hS Y.1 Y.2 L)
    (hs : IsRegularMeromorphicSection.{u, u} B S hS Y.1 Y.2 L s) :
    IsRegularMeromorphicSection.{u, u} B S hS X.1 X.2 ((modulePullback B S hS f).obj L)
      (pullbackMeromorphicSection B S hS f L hf s)
```

## Tag 0EPQ, a lemma

[Tag 0EPQ](https://stacks.math.columbia.edu/tag/0EPQ) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isRegularMeromorphicSection_of_isTrivialAtCodimensionZeroPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RegularMeromorphicSectionExistence.lean, line 299](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/RegularMeromorphicSectionExistence.lean#L299). The attribute's comment: “every invertible module on an algebraic space satisfying conditions (a), (b) and (c) of Tag 0ENA has a regular meromorphic section”.

> **Stacks 0EPQ.** Let `X` be an algebraic space over a scheme `S` satisfying conditions (a),
> (b) and (c) of Stacks 0ENA — every weakly associated point of `X` has codimension `0`, the
> irreducible components of `X` are locally finite, and every codimension-zero point of `X` is
> representable by a monomorphism from the spectrum of a field.  Then **every invertible
> `𝒪_X`-module `ℒ` has a regular meromorphic section.**
>
> The choice of the generators `s_η ∈ ℒ_η` that the source makes is
> `AlgebraicGeometry.Space.CodimensionZeroPresentation.nonempty_iso_unit_of_isInvertibleModule`
> above, the triviality of an invertible module on the small étale site of `Spec(𝒪_{X, η})`,
> composed with `AlgebraicGeometry.Space.modulePullbackInvertible`.  Those trivialisations give
> `𝒦_X ≅ 𝒦_X(ℒ)` by `CodimensionZeroPresentation.nonempty_uliftUnit_iso_meromorphicSectionSheaf`,
> and an isomorphism `𝒦_X ≅ 𝒦_X(ℒ)` produces a regular meromorphic section by
> `AlgebraicGeometry.Space.exists_isRegularMeromorphicSection_of_nonempty_iso`.  See the
> implementation notes.

```lean
theorem exists_isRegularMeromorphicSection_of_isTrivialAtCodimensionZeroPoints
    {X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hwa : ∀ z ∈ weaklyAssociatedPointsOfSpace B S hS (⟨X, hX⟩ : AlgebraicSpaces B S hS),
      localRingDimension B S hS z = 0)
    (hfin : HasLocallyFiniteIrreducibleComponents B S hS X)
    (hmono : HasMonomorphicCodimensionZeroPoints B S hS X)
    (L : Modules.{u, u} B S hS X hX)
    (hL : IsInvertibleModule (⟨X, hX⟩ : AlgebraicSpaces B S hS) L) :
    ∃ s : MeromorphicSection.{u, u} B S hS X hX L,
      IsRegularMeromorphicSection.{u, u} B S hS X hX L s
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 71.10, Tag 0EN2](https://stacks.math.columbia.edu/tag/0EN2)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
