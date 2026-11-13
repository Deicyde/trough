---
declaration: section
origin: cited
lean: Stacks.Duality.isCompactObject_iff_isPerfect, Stacks.Duality.isCompactObject_eq_isPerfect, Stacks.Duality.PerfectCompact.isCompactObject_iff_isPerfect, AlgebraicGeometry.isCompactObject_iff_isPerfect_spec, AlgebraicGeometry.isPerfect_of_isCompactObject, AlgebraicGeometry.isCompactObject_iff_isPerfect_spec_of_model, Stacks.Duality.QcqsPerfect.isCompactObject_iff_isPerfect, Stacks.Duality.QcqsPerfect.isCompactObject_of_isPerfect
statement: formalized
proof: formalized
---

# 36.17 Compact and perfect objects

Section 36.17 of the Stacks Project, [Tag 09M0](https://stacks.math.columbia.edu/tag/09M0). 5 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 09M1, a proposition

[Tag 09M1](https://stacks.math.columbia.edu/tag/09M1) in the Stacks Project.

**`Stacks.Duality.isCompactObject_iff_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/CompactPerfect.lean, line 661](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/CompactPerfect.lean#L661).

> **[Stacks, Tag 09M1].** On a quasi-compact quasi-separated scheme `X`, an object of
> `D_QCoh(𝒪_X)` is compact if and only if it is a perfect object of `D(𝒪_X)`, in any model of
> `D(𝒪_X)`.

```lean
theorem _root_.Stacks.Duality.isCompactObject_iff_isPerfect {X : Scheme.{u}} [CompactSpace X]
    [QuasiSeparatedSpace X] [h : HasDerivedCategory.{w} X.Modules]
    (K : Stacks.Duality.quasiCoherentDerivedCategory X) :
    IsCompactObject.{u} K ↔ @Stacks.Cohomology.PerfectComplexes.IsPerfect X.toRingedSpace h K.obj
```

**`Stacks.Duality.isCompactObject_eq_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/CompactPerfectTag.lean, line 48](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/CompactPerfectTag.lean#L48).

> **[Stacks, Tag 09M1].** Let `X` be a quasi-compact and quasi-separated scheme. An object of
> `D_QCoh(𝒪_X)` is compact if and only if it is perfect: the compact objects of `D_QCoh(𝒪_X)` are
> exactly those whose underlying object of `D(𝒪_X)` is perfect, in any model of `D(𝒪_X)`.

```lean
theorem isCompactObject_eq_isPerfect (X : Scheme.{u}) [CompactSpace X] [QuasiSeparatedSpace X]
    [h : HasDerivedCategory.{w} X.Modules] :
    (IsCompactObject.{u} : ObjectProperty (quasiCoherentDerivedCategory X)) =
      fun K => @Stacks.Cohomology.PerfectComplexes.IsPerfect X.toRingedSpace h K.obj
```

**`Stacks.Duality.PerfectCompact.isCompactObject_iff_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/PerfectIsCompactCover.lean, line 311](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/PerfectIsCompactCover.lean#L311).

> Let `X` be a quasi-compact and quasi-separated scheme. An object of `D_QCoh(𝒪_X)` is compact
> if and only if it is perfect.

```lean
theorem isCompactObject_iff_isPerfect (X : Scheme.{u}) [CompactSpace X] [QuasiSeparatedSpace X]
    (K : Stacks.Duality.quasiCoherentDerivedCategory X) :
    IsCompactObject.{u} K ↔ RingedSpace.IsPerfect (X := X.toRingedSpace) K.obj
```

**`AlgebraicGeometry.isCompactObject_iff_isPerfect_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/QuasiCoherentDerived/CompactAndPerfect.lean, line 124](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/QuasiCoherentDerived/CompactAndPerfect.lean#L124). The attribute's comment: “the affine case, both directions”.

> **Stacks 09M1 on an affine scheme.** Let `R` be a ring and let `L` be an object of
> `D_QCoh(𝒪_{Spec R})`. Then `L` is a compact object of `D_QCoh(𝒪_{Spec R})` if and only if it is a
> perfect object of `D(𝒪_{Spec R})`.
>
> Writing `L = M̃` for an object `M` of `D(R)`, compactness of `L` is compactness of `M` because
> `M ↦ M̃` is an equivalence ([Stacks, Tag 06Z0], here
> `AlgebraicGeometry.affineTildeQuasicoherent_isEquivalence`), compactness of `M` is perfectness of
> `M` by [Stacks, Tag 07LT], and perfectness of `M` is perfectness of `M̃` by
> [Stacks, Tag 08EB].

```lean
theorem isCompactObject_iff_isPerfect_spec (R : CommRingCat.{u})
    (L : QuasicoherentDerivedCategory (Spec R)) :
    IsCompactObject.{u} L ↔
      Stacks.Cohomology.PerfectComplexes.IsPerfect (X := (Spec R).toRingedSpace) L.obj
```

**`AlgebraicGeometry.isPerfect_of_isCompactObject`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/QuasiCoherentDerived/CompactAndPerfect.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/QuasiCoherentDerived/CompactAndPerfect.lean#L161). The attribute's comment: “compact implies perfect; the affine-local datum, which the source draws from Tag 08DZ (derived direct image along a quasi-compact quasi-separated morphism commutes with direct sums) together with Tag 06Z0, is a hypothesis: that deduction is not carried out here. Tag 08DZ is proved in this repository, as Stacks.Duality.DerivedPushforward.preservesColimitsOfShape\_discrete\_qcqsQuasiCoherentDerivedPushforward, but only at HasDerivedCategory.standard”.

> **Stacks 09M1, the implication from compactness to perfectness.** Let `X` be a scheme and let
> `K` be an object of `D_QCoh(𝒪_X)`. Suppose every point of `X` has an open neighbourhood `U` on
> which `K` is the image, under a functor preserving perfectness, of a compact object of
> `D_QCoh(𝒪_{Spec R})` for some ring `R`. Then `K` is a perfect object of `D(𝒪_X)`.
>
> Compactness of `K` itself enters only through the local models: on a quasi-compact
> quasi-separated scheme the restriction of a compact object of `D_QCoh(𝒪_X)` to an affine open is
> compact there, by [Stacks, Tag 08DZ] and adjunction. The affine case makes the local models
> perfect, and perfectness is local on the space by [Stacks, Tag 08CN].

```lean
theorem isPerfect_of_isCompactObject (X : Scheme.{u}) (K : QuasicoherentDerivedCategory X)
    (hloc : ∀ x : X.toRingedSpace.carrier,
      ∃ (U : Opens X.toRingedSpace.carrier) (_ : x ∈ U) (R : CommRingCat.{u})
        (Φ : DerivedCategory (SheafOfModules.{u} (Spec R).ringCatSheaf) ⥤
          DerivedCategory (StrictlyPerfect.OXMod.{u, u, u}
            (X.toRingedSpace.restrict U.isOpenEmbedding)))
        (L : QuasicoherentDerivedCategory (Spec R)),
        IsCompactObject.{u} L ∧
          (∀ N, Stacks.Cohomology.PerfectComplexes.IsPerfect
              (X := (Spec R).toRingedSpace) N →
            Stacks.Cohomology.PerfectComplexes.IsPerfect
              (X := X.toRingedSpace.restrict U.isOpenEmbedding) (Φ.obj N)) ∧
          Nonempty (Φ.obj L.obj ≅
            (RingedSpace.restrictModules X.toRingedSpace U).mapDerivedCategory.obj K.obj)) :
    Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) K.obj
```

**`AlgebraicGeometry.isCompactObject_iff_isPerfect_spec_of_model`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/QuasiCoherentDerived/CompactAndPerfectLocallySmall.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/QuasiCoherentDerived/CompactAndPerfectLocallySmall.lean#L104). The attribute's comment: “the affine case, both directions, at an arbitrary chosen derived category -- in particular at the locally small AlgebraicGeometry.Scheme.Modules.hasDerivedCategory, at which the companion AlgebraicGeometry.isCompactObject\_iff\_isPerfect\_spec says nothing. The global case is not covered here”.

> **The affine case of [Stacks, Tag 09M1], at an arbitrary chosen derived category.** Let `R` be
> a ring and let `K` be an object of `D_QCoh(𝒪_{Spec R})`, for any chosen model of `D(R)` and any
> chosen model of `D(𝒪_{Spec R})`. Then `K` is a compact object of `D_QCoh(𝒪_{Spec R})`, with the
> direct sums tested over index types in `Type u`, if and only if `K` is a perfect object of
> `D(𝒪_{Spec R})`.
>
> Writing `K = M̃` for an object `M` of `D(R)`, which is possible because `M ↦ M̃` is an equivalence
> ([Stacks, Tag 06Z0]), compactness of `K` is compactness of `M` because compactness at a fixed
> index universe crosses an additive equivalence, compactness of `M` is perfectness of `M` by
> [Stacks, Tag 07LT], and perfectness of `M` is perfectness of `M̃` by [Stacks, Tag 08EB].
>
> This is `AlgebraicGeometry.isCompactObject_iff_isPerfect_spec` with the pin on the standard model
> removed; see the implementation notes for why it cannot be added beside it.

```lean
theorem isCompactObject_iff_isPerfect_spec_of_model
    (K : Stacks.Duality.quasiCoherentDerivedCategory (Spec R)) :
    IsCompactObject.{u} K ↔
      @Stacks.Cohomology.PerfectComplexes.IsPerfect (Spec R).toRingedSpace hS K.obj
```

**`Stacks.Duality.QcqsPerfect.isCompactObject_iff_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/QuasiCoherentDerived/QcqsCompactIsPerfect.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/QuasiCoherentDerived/QcqsCompactIsPerfect.lean#L93). The attribute's comment: “both directions, on a quasi-compact quasi-separated scheme, at the locally small AlgebraicGeometry.Scheme.Modules.hasDerivedCategory”.

> **[Stacks, Tag 09M1].** On a quasi-compact quasi-separated scheme `X`, an object of
> `D_QCoh(𝒪_X)` is compact if and only if it is perfect, at the locally small derived category.

```lean
theorem isCompactObject_iff_isPerfect (X : Scheme.{u}) [CompactSpace X] [QuasiSeparatedSpace X]
    (K : Stacks.Duality.quasiCoherentDerivedCategory X) :
    IsCompactObject.{u} K ↔
      Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) K.obj
```

**`Stacks.Duality.QcqsPerfect.isCompactObject_of_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/QuasiCoherentDerived/QcqsPerfectIsCompact.lean, line 289](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/QuasiCoherentDerived/QcqsPerfectIsCompact.lean#L289). The attribute's comment: “perfect implies compact, on a quasi-compact quasi-separated scheme, at the locally small AlgebraicGeometry.Scheme.Modules.hasDerivedCategory. The opposite implication is not covered here; for it on a general scheme see AlgebraicGeometry.isPerfect\_of\_isCompactObject, and for both on an affine scheme see AlgebraicGeometry.isCompactObject\_iff\_isPerfect\_spec\_of\_model”.

> Let `X` be a quasi-compact quasi-separated scheme and let `K` be an object of `D_QCoh(𝒪_X)`
> which is perfect as an object of `D(𝒪_X)`. Then `K` is a compact object of `D_QCoh(𝒪_X)`, with
> the direct sums tested over index types in the universe of `X`, at the locally small derived
> category `AlgebraicGeometry.Scheme.Modules.hasDerivedCategory`.

```lean
theorem isCompactObject_of_isPerfect (X : Scheme.{u}) [CompactSpace X] [QuasiSeparatedSpace X]
    (K : Stacks.Duality.quasiCoherentDerivedCategory X)
    (hK : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) K.obj) :
    IsCompactObject.{u} K
```

## Tag 0GEF, a remark

[Tag 0GEF](https://stacks.math.columbia.edu/tag/0GEF) in the Stacks Project.

**`Stacks.Duality.PerfectClassicalGenerator.triangEnvelope_eq_perfectObjects_of_isWeakTriangulatedGenerator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/ClassicalGeneratorOfPerfectComplexes.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/ClassicalGeneratorOfPerfectComplexes.lean#L253). The attribute's comment: “for X quasi-compact and quasi-separated and G a perfect object generating D\_QCoh(O\_X), G is a classical generator of D\_perf(O\_X): the triangulated envelope of G is exactly the perfect objects”.

> **Stacks 0GEF**. Let `X` be a quasi-compact and quasi-separated scheme and let `G` be a perfect
> object of `D(𝒪_X)` lying in `D_QCoh(𝒪_X)` and generating it, in the sense that an object of
> `D_QCoh(𝒪_X)` receiving only zero morphisms from the shifts of `G` is zero. Then `G` is a classical
> generator of `D_perf(𝒪_X)`: the smallest strictly full triangulated subcategory of `D_QCoh(𝒪_X)`
> closed under direct summands and containing `G` is exactly the subcategory of perfect objects.

```lean
theorem triangEnvelope_eq_perfectObjects_of_isWeakTriangulatedGenerator
    (X : Scheme.{u}) [CompactSpace X] [QuasiSeparatedSpace X]
    (G : Stacks.Duality.quasiCoherentDerivedCategory X)
    (hG : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) G.obj)
    (hgen : (ObjectProperty.singleton G).IsWeakTriangulatedGenerator) :
    (ObjectProperty.singleton G).triangEnvelope = perfectObjects X
```

## Tag 0A9B, a lemma

[Tag 0A9B](https://stacks.math.columbia.edu/tag/0A9B) in the Stacks Project.

**`Stacks.Duality.Supported.isCompactObject_iff_isPerfect`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/SupportedCompactObject.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/SupportedCompactObject.lean#L218). The attribute's comment: “compactness in `D_{QCoh,T}(𝒪_X)` is perfectness in `D(𝒪_X)`, with nothing carried. Both results the source cites are proved in this library and discharged in the proof: Tag 09M1, that a perfect object of `D_QCoh(𝒪_X)` is a compact object of it, as `AlgebraicGeometry.isCompactObject_of_isPerfect`, and Tag 0A9A, that `D_{QCoh,T}(𝒪_X)` is generated by a perfect object, as `Stacks.Rouquier.exists_isPerfect_isWeakTriangulatedGenerator_supported`. They are discharged at the cost of the source's own hypotheses that `X` be quasi-compact and quasi-separated and that `T` be closed with quasi-compact complement, which are Tag 0A9B's hypotheses too and are used for nothing else. The source's step (d), that a direct summand of a perfect object is perfect, is Tag 08CS and is proved in this library, so it is not a hypothesis. The derived category is the locally small model rather than a binder, Tag 0A9A being available at no other; the two directions at an arbitrary model are `Stacks.Duality.Supported.isCompactObject_of_isPerfect` and, with the generator given, `Stacks.Duality.Supported.isPerfect_of_isCompactObject`”.

> **An object of `D_{QCoh,T}(𝒪_X)` is compact if and only if it is perfect as an object of
> `D(𝒪_X)`**, for `X` quasi-compact and quasi-separated and `T` closed with quasi-compact
> complement. The derived category is taken at the locally small model.

```lean
theorem isCompactObject_iff_isPerfect [CompactSpace X] [QuasiSeparatedSpace X]
    (hT : IsClosed T) (hTc : IsCompact Tᶜ)
    (K : QuasiCoherentSupportedDerivedCategory X T) :
    IsCompactObject.{u} K ↔ IsPerfect (X := X.toRingedSpace) K.obj
```

**`Stacks.Duality.Supported.isCompactObject_iff_isPerfect_of_isClosed`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/SupportedCompactPerfect.lean, line 296](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/SupportedCompactPerfect.lean#L296).

> **[Stacks, Tag 0A9B].** Let `X` be a quasi-compact and quasi-separated scheme and let
> `T ⊆ X` be a closed subset such that `X ∖ T` is quasi-compact. An object of `D_{QCoh,T}(𝒪_X)` is
> compact (in `D_{QCoh,T}(𝒪_X)`) if and only if it is perfect as an object of `D(𝒪_X)`.
>
> Perfect objects are compact in `D_QCoh(𝒪_X)` by [Stacks, Tag 09M1]
> (`Stacks.Duality.PerfectCompact.isCompactObject_of_isPerfect`), hence in the full subcategory
> `D_{QCoh,T}(𝒪_X)`, which is closed under direct sums
> (`Stacks.Duality.Supported.isCompactObject_of_isCompactObject_obj`). Conversely
> `D_{QCoh,T}(𝒪_X)` has a compact perfect generator ([Stacks, Tag 0A9A],
> `Stacks.Duality.Supported.exists_isCompactObject_isPerfect_isWeakTriangulatedGenerator`), so
> every compact object is built from it by shifts, cones, finite direct sums and summands
> ([Stacks, Tag 09SR]), and is perfect
> (`Stacks.Duality.Supported.isPerfect_of_isCompactObject_of_generator`).

```lean
theorem isCompactObject_iff_isPerfect_of_isClosed (hT : IsClosed T) (hTc : IsCompact Tᶜ)
    (K : Stacks.Duality.QuasiCoherentSupportedDerivedCategory X T) :
    IsCompactObject.{u} K ↔
      AlgebraicGeometry.RingedSpace.IsPerfect (X := X.toRingedSpace) K.obj
```

## Tag 0GEG, a remark

[Tag 0GEG](https://stacks.math.columbia.edu/tag/0GEG) in the Stacks Project.

**`Stacks.Duality.SupportedClassicalGenerator.hasCoproducts_and_exists_perfect_generator_and_triangEnvelope_eq_perfectSupported`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/SupportedClassicalGenerator.lean, line 386](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/SupportedClassicalGenerator.lean#L386).

> **[Stacks, Remark 0GEG].** Let `X` be a quasi-compact and quasi-separated scheme and let
> `T ⊆ X` be a closed subset such that `X ∖ T` is quasi-compact. Then
>
> 1. `D_{QCoh,T}(𝒪_X)` has direct sums;
> 2. there is a perfect object `G` of `D_{QCoh,T}(𝒪_X)` which is a generator for
>    `D_{QCoh,T}(𝒪_X)` (by [Stacks, Tag 0A9A]);
> 3. every such `G` is a classical generator for `D_{perf,T}(𝒪_X)`: the smallest strictly full,
>    saturated, triangulated subcategory of `D_{QCoh,T}(𝒪_X)` containing `G` is the subcategory
>    `perfectSupported X T` of objects perfect in `D(𝒪_X)`.
>
> Generators are weak generators in the sense of [Stacks, Tag 09SJ\](3) and the classical
> generation is equality with `CategoryTheory.ObjectProperty.triangEnvelope`. Everything is stated
> at an arbitrary model of the derived category. The direct sums are indexed by the universe of
> `𝒪_X`-modules; the source's argument uses them, with [Stacks, Tag 0A9B] and
> [Stacks, Tag 09SR], at the locally small model, where the morphisms of `D(𝒪_X)` lie in that
> universe too.

```lean
theorem hasCoproducts_and_exists_perfect_generator_and_triangEnvelope_eq_perfectSupported
    (hT : IsClosed T) (hTc : IsCompact (Tᶜ : Set X)) :
    HasCoproducts.{u} (QuasiCoherentSupportedDerivedCategory X T) ∧
      (∃ G : QuasiCoherentSupportedDerivedCategory X T,
        perfectSupported X T G ∧ (ObjectProperty.singleton G).IsWeakTriangulatedGenerator) ∧
      ∀ G : QuasiCoherentSupportedDerivedCategory X T, perfectSupported X T G →
        (ObjectProperty.singleton G).IsWeakTriangulatedGenerator →
          (ObjectProperty.singleton G).triangEnvelope = perfectSupported X T
```

## Tag 0A9C, a lemma

[Tag 0A9C](https://stacks.math.columbia.edu/tag/0A9C) in the Stacks Project.

**`Stacks.Duality.exists_isPerfect_whiskerRight_comp_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/PerfectAnnihilator.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Duality/CompactGeneration/PerfectAnnihilator.lean#L149).

> **[Stacks, Tag 0A9C].** Let `X` be quasi-compact and quasi-separated, `U ⊆ X` a quasi-compact
> open and `α : P ⟶ E` a morphism of `D_QCoh(𝒪_X)` with `E` supported on `X \ U`, where either `P`
> is perfect, or `P` is pseudo-coherent and `E` is bounded below. Then there is a perfect complex
> `I` and a map `u : I ⟶ 𝒪_X` invertible on `U` such that `I ⊗ᴸ P ⟶ P ⟶ E` is zero.

```lean
theorem exists_isPerfect_whiskerRight_comp_eq_zero {X U : Scheme.{u}} [CompactSpace X]
    [QuasiSeparatedSpace X] (j : U ⟶ X) [IsOpenImmersion j] [AlgebraicGeometry.QuasiCompact j]
    {P E : quasiCoherentDerivedCategory X} (α : P ⟶ E)
    (hE : IsZero ((derivedRestrict j).obj E.obj))
    (hP : Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) P.obj ∨
      (AlgebraicGeometry.RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) P.obj ∧
        DerivedCategoryB.IsBoundedBelow E.obj)) :
    ∃ (I : quasiCoherentDerivedCategory X) (u : I ⟶ 𝟙_ (quasiCoherentDerivedCategory X)),
      Stacks.Cohomology.PerfectComplexes.IsPerfect (X := X.toRingedSpace) I.obj ∧
        IsIso ((derivedRestrict j).map ((ObjectProperty.ι _).map u)) ∧
          (u ▷ P) ≫ (λ_ P).hom ≫ α = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 36.17, Tag 09M0](https://stacks.math.columbia.edu/tag/09M0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
