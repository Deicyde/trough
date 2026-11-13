---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_completionAlong', AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_completionFunctor, AlgebraicGeometry.FormalSpace.completionAlong, AlgebraicGeometry.FormalSpace.isClosed_preimage_pointsMapULift, AlgebraicGeometry.FormalSpace.isPullback_completionAlongMap, AlgebraicGeometry.FormalSpace.isReduction_completionAlong, AlgebraicGeometry.FormalSpace.isCountablyIndexed_completionAlong, AlgebraicGeometry.FormalSpace.isAdicStar_completionAlong
statement: formalized
proof: formalized
---

# 87.37 Recompletion

Section 87.37 of the Stacks Project, [Tag 0GVP](https://stacks.math.columbia.edu/tag/0GVP). 7 tags here are carried by 16 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0GVQ, a lemma

[Tag 0GVQ](https://stacks.math.columbia.edu/tag/0GVQ) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_completionAlong'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionAffineSupplement.lean, line 995](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionAffineSupplement.lean#L995).

> **Stacks 0GVQ.** Let `S` be a scheme, let `X` be an affine formal algebraic space over `S`,
> let `i : X_red ⟶ X` be a reduction of `X` and let `T ⊆ |X_red|` be a closed subset. Then the
> completion `X_{/T}` of `X` along `T` — the fppf sheaf whose sections over an object `U` of the
> big fppf site of `S` are the morphisms `f : U ⟶ X` with `f(|U|) ⊆ T` — is an affine formal
> algebraic space over `S`.
>
> Nothing is assumed beyond the tag's own hypotheses. The affine presentation is
> `exists_affinePresentation_completionSheafULift` and the set-theoretic condition of Stacks 0AIS
> is `satisfiesSetTheoreticCondition_completionSheafULift`.
>
> The two steps the source cites in general form are proved here: that a closed subset of
> `|X_red|` is a closed subset of `|X|` is
> `AlgebraicGeometry.FormalSpace.IsReduction.isClosed_image_pointsMapULift`, and that
> `X_{/T} = colim (X_λ)_{/T}` is
> `AlgebraicGeometry.FormalSpace.completionSheafULiftIsoColimitCompletion`.
>
> The reduction is supplied as data satisfying `AlgebraicGeometry.FormalSpace.IsReduction`
> rather than constructed, since Stacks 0AIN — the existence of a reduction — is not available
> in this library; this is how Stacks 0GVT is stated here as well, and it needs no choice.

```lean
theorem isAffineFormalAlgebraicSpace_completionAlong' {X Xred : FppfSheaf B S hS}
    (hX : IsAffineFormalAlgebraicSpace B S hS X) {i : Xred ⟶ X}
    (hi : IsReduction B S hS X Xred i)
    (T : Set (Space.pointsULift.{u + 1} B S hS Xred.obj))
    (hT : @IsClosed _ (Space.pointTopologyULift.{u + 1} B S hS Xred.obj) T) :
    IsAffineFormalAlgebraicSpace B S hS (completionAlong i T)
```

## Tag 0GVR, a lemma

[Tag 0GVR](https://stacks.math.columbia.edu/tag/0GVR) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_completionFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionFormalAlgebraicSpace.lean, line 316](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionFormalAlgebraicSpace.lean#L316). The attribute's comment: “the functor `X_{/T}` is an fppf sheaf and a formal algebraic space, for any reduction `X_red` of `X` and `T` closed in `|X_red|`; the atlas, the affine case 0GVQ and the set-theoretic condition of 0AIS for `X_{/T}` are all proved here”.

> **Stacks 0GVR.** Let `S` be a scheme, let `X` be a formal algebraic space over `S` and let
> `T ⊆ |X_red|` be a closed subset, for a reduction `i : X_red ⟶ X` of `X`. Then the functor
> `X_{/T}` on the big fppf site of `S` sending `U` to the morphisms `f : U ⟶ X` with
> `f(|U|) ⊆ T` is a formal algebraic space: it is an fppf sheaf, and as such a formal algebraic
> space over `S`. It is the completion `completionAlong i T` of Stacks 0GVS, which is a formal
> algebraic space as well.
>
> The functor is `AlgebraicGeometry.Space.completionSubfunctorULift` of `X` along the image of
> `T` in `|X|`. Nothing is assumed: the sheaf property is
> `AlgebraicGeometry.Space.isSheaf_completionSubfunctorULift`, the atlas of Definition 0AIM is
> `AlgebraicGeometry.FormalSpace.isFormalAlgebraicSpace_completionSheafULift` with its affine
> charts from Stacks 0GVQ, and the set-theoretic condition of Stacks 0AIS is
> `satisfiesSetTheoreticCondition_completionSheafULift_of_satisfiesSetTheoreticCondition`.
> A reduction exists by Stacks 0AIN, and the statement holds for every one.

```lean
theorem isFormalAlgebraicSpace_completionFunctor {X Xred : FppfSheaf B S hS}
    (hX : IsFormalAlgebraicSpace B S hS X) {i : Xred ⟶ X}
    (hi : IsReduction B S hS X Xred i)
    (T : Set (Space.pointsULift.{u + 1} B S hS Xred.obj))
    (hT : @IsClosed _ (Space.pointTopologyULift.{u + 1} B S hS Xred.obj) T) :
    ∃ h : Presheaf.IsSheaf (BigFppfOver.topology B S hS)
        (Space.completionSubfunctorULift B S hS X.obj
          (Space.pointsMapULift.{u + 1} B S hS Xred.obj i.hom '' T)).toFunctor,
      IsFormalAlgebraicSpace B S hS ⟨_, h⟩ ∧
        IsFormalAlgebraicSpace B S hS (completionAlong i T)
```

## Tag 0GVS, a definition

[Tag 0GVS](https://stacks.math.columbia.edu/tag/0GVS) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.FormalSpace.completionAlong`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Recompletion.lean#L337), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionAffine.lean, line 414](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionAffine.lean#L414) (StacksFrontier): “the completion of a formal algebraic space along a closed subset of its reduction, defined for an arbitrary morphism into the space and an arbitrary subset of the points of its source”.

## Tag 0GVT, a lemma

[Tag 0GVT](https://stacks.math.columbia.edu/tag/0GVT) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isClosed_preimage_pointsMapULift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Recompletion.lean, line 352](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Recompletion.lean#L352). The attribute's comment: “the closed subset `T'`”.

> **Stacks 0GVT.** The inverse image `T' = |f_red|⁻¹ T` of a closed subset `T ⊆ |X_red|` is a
> closed subset of `|X'_red|`, since the morphism of reductions is continuous on points.

```lean
theorem isClosed_preimage_pointsMapULift {Xred' Xred : FppfSheaf B S hS}
    (fred : Xred' ⟶ Xred) (T : Set (Space.pointsULift.{u + 1} B S hS Xred.obj)) :
    letI := Space.pointTopologyULift.{u + 1} B S hS Xred.obj
    letI := Space.pointTopologyULift.{u + 1} B S hS Xred'.obj
    IsClosed T →
      IsClosed (Space.pointsMapULift.{u + 1} B S hS Xred'.obj fred.hom ⁻¹' T)
```

**`AlgebraicGeometry.FormalSpace.isPullback_completionAlongMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/Recompletion.lean, line 410](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/Recompletion.lean#L410). The attribute's comment: “the cartesian square”. References: EGA I (10.9.9).

> **Stacks 0GVT.** Let `f : X' ⟶ X` be a morphism of formal algebraic spaces over `S`, let
> `T ⊆ |X_red|` be a closed subset and let `T' = |f_red|⁻¹ T ⊆ |X'_red|`. Then the square formed
> by `X'_{/T'} ⟶ X'`, `X_{/T} ⟶ X`, the morphism of completions and `f` is cartesian.

```lean
theorem isPullback_completionAlongMap {X' X Xred' Xred : FppfSheaf B S hS}
    (_hX' : IsFormalAlgebraicSpace B S hS X') (_hX : IsFormalAlgebraicSpace B S hS X)
    {i' : Xred' ⟶ X'} {i : Xred ⟶ X} (hi' : IsReduction B S hS X' Xred' i')
    (hi : IsReduction B S hS X Xred i) (f : X' ⟶ X)
    (T : Set (Space.pointsULift.{u + 1} B S hS Xred.obj))
    (_hT : @IsClosed _ (Space.pointTopologyULift.{u + 1} B S hS Xred.obj) T) :
    IsPullback
      (completionAlongInclusion i'
        (Space.pointsMapULift.{u + 1} B S hS Xred'.obj (reductionMap hi' hi f).hom ⁻¹' T))
      (completionAlongMap hi' hi f T)
      f
      (completionAlongInclusion i T)
```

## Tag 0GVU, a lemma

[Tag 0GVU](https://stacks.math.columbia.edu/tag/0GVU) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isReduction_completionAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionReduction.lean, line 551](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionReduction.lean#L551). The attribute's comment: “with the reduction of `X` written as the universe lift of an algebraic space over `S`, the form in which the reduced induced closed subspace of Stacks 03IQ is available; that costs no generality, by `Space.exists_uliftFunctor_iso_of_isAlgebraicSpaceULift`”. References: EGA I (10.8.6), “more general”.

> **Stacks 0GVU.** Let `S` be a scheme contained in a big fppf site `B`, let `X` be a formal
> algebraic space over `S` with reduction `i : X_red ⟶ X`, and let `T ⊆ |X_red|` be a closed
> subset. The reduction of the completion `X_{/T}` of `X` along `T` is the reduced induced closed
> subspace `Z` of `X_red` corresponding to `T`: the canonical morphism `Z ⟶ X_{/T}` exhibits `Z`
> as the reduction of the completion.
>
> The conclusion contains the mapping property: every morphism to `X_{/T}` from a reduced
> algebraic space over `S` factors uniquely through `Z`.

```lean
theorem isReduction_completionAlong (_hX : IsFormalAlgebraicSpace B S hS X)
    (hi : IsReduction B S hS X (sheafOfAlgebraicSpace B S hS Xred₀ hXred₀) i)
    (T : Set (Space.points B S hS Xred₀)) (hT : IsClosed T) :
    IsReduction B S hS (completionAlong i (liftedPointSet B S hS hXred₀ T))
      (reducedSubspaceSheaf B S hS hXred₀ T hT)
      (reducedSubspaceToCompletionAlong B S hS hXred₀ T hT)
```

## Tag 0GVV, a lemma

[Tag 0GVV](https://stacks.math.columbia.edu/tag/0GVV) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isCountablyIndexed_completionAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionAffineClausesTypes.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionAffineClausesTypes.lean#L142). The attribute's comment: “clause (3): if `|X_red| \ T` is quasi-compact and `X` is countably indexed then so is `X_{/T}`, countably indexed being `IsCountablyIndexed` (Stacks 0AIJ, StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexed.lean). Carried hypotheses: `hX` is the tag's own countable-indexing hypothesis on `X`, `hi` supplies the reduction as data rather than choosing one from Stacks 0AIN (the convention of the library's Stacks 0GVT and 0GB8), `hT` is the tag's own closedness of `T` in `|X_red|`, `hqc` is the tag's own quasi-compactness of `|X_red| \ T`, stated as compactness of `Tᶜ` for the point topology `Space.pointTopologyULift` since this library has no quasi-compactness predicate for formal algebraic spaces, and `hspf` is the source's own step producing the weakly admissible ring `lim A/J_{m,n}` with a countable fundamental system of neighbourhoods of zero — condition (2) of Stacks 0AN1 — quantified over its own space, reduction and subset. The step from `hspf` to the conclusion is Stacks 0AN1, (2) ⇒ (1) (`isCountablyIndexedAffine_of_hasCountableWeakPresentation`).”.

> Let `S` be a scheme, let `X` be an affine formal algebraic space over `S`, let
> `i : X_red ⟶ X` be a reduction of `X` and let `T ⊆ |X_red|` be closed with `|X_red| \ T`
> quasi-compact. If `X` is countably indexed then so is the completion `X_{/T}` of `X` along `T`.
>
> It takes as hypothesis `hspf : CompletionOfCountablyIndexedIsCountableSpf`.

```lean
theorem isCountablyIndexed_completionAlong {X Xred : FppfSheaf B S hS}
    (hX : IsCountablyIndexed B S hS X) {i : Xred ⟶ X}
    (hi : IsReduction B S hS X Xred i)
    (T : Set (Space.pointsULift.{u + 1} B S hS Xred.obj))
    (hT : @IsClosed _ (Space.pointTopologyULift.{u + 1} B S hS Xred.obj) T)
    (hqc : @IsCompact _ (Space.pointTopologyULift.{u + 1} B S hS Xred.obj) Tᶜ)
    (hspf : CompletionOfCountablyIndexedIsCountableSpf B S hS) :
    IsCountablyIndexed B S hS (completionAlong i T)
```

**`AlgebraicGeometry.FormalSpace.isAdicStar_completionAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionAffineClausesTypes.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionAffineClausesTypes.lean#L190). The attribute's comment: “clause (4): if `|X_red| \ T` is quasi-compact and `X` is adic* then so is `X_{/T}`, adic* being `IsAdicStar` (Stacks 0AID (4), StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/Types.lean). Carried hypotheses: `hX` is the tag's own adic* hypothesis on `X`, `hi` supplies the reduction as data rather than choosing one from Stacks 0AIN (the convention of the library's Stacks 0GVT and 0GB8), `hT` is the tag's own closedness of `T` in `|X_red|`, `hqc` is the tag's own quasi-compactness of `|X_red| \ T`, stated as compactness of `Tᶜ` for the point topology `Space.pointTopologyULift` since this library has no quasi-compactness predicate for formal algebraic spaces, `hideal` is the source's own step identifying `X_{/T}` with the completion of an affine scheme along the finitely generated ideal `J = (f_1,...,f_r) + I`, quantified over its own space, reduction and subset, and `hset` is the set-theoretic condition of Stacks 0AIS on the completion, carried where Stacks 0GVM (`isAffineFormalAlgebraicSpace_colimit`) carries it and needed to transport the conclusion back along the isomorphism. The step from `hideal` to the conclusion is Stacks 0GXX (3) (`isAdicStar_completionAlongIdeal`).”.

> Let `S` be a scheme, let `X` be an affine formal algebraic space over `S`, let
> `i : X_red ⟶ X` be a reduction of `X` and let `T ⊆ |X_red|` be closed with `|X_red| \ T`
> quasi-compact. If `X` is adic\* then so is the completion `X_{/T}` of `X` along `T`.
>
> It takes as hypotheses `hideal : CompletionOfAdicStarIsCompletionAlongFGIdeal` and the
> set-theoretic condition `hset` on `X_{/T}`.

```lean
theorem isAdicStar_completionAlong {X Xred : FppfSheaf B S hS}
    (hX : IsAdicStar B S hS X) {i : Xred ⟶ X}
    (hi : IsReduction B S hS X Xred i)
    (T : Set (Space.pointsULift.{u + 1} B S hS Xred.obj))
    (hT : @IsClosed _ (Space.pointTopologyULift.{u + 1} B S hS Xred.obj) T)
    (hqc : @IsCompact _ (Space.pointTopologyULift.{u + 1} B S hS Xred.obj) Tᶜ)
    (hideal : CompletionOfAdicStarIsCompletionAlongFGIdeal B S hS)
    (hset : SatisfiesSetTheoreticCondition B S hS (completionAlong i T)) :
    IsAdicStar B S hS (completionAlong i T)
```

**`AlgebraicGeometry.FormalSpace.isNoetherian_completionAlong`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionAffineClausesTypes.lean, line 239](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionAffineClausesTypes.lean#L239). The attribute's comment: “clause (5): if `X` is Noetherian then so is `X_{/T}`, Noetherian being `IsNoetherian` (Stacks 0AID (5), StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/Types.lean). Carried hypotheses: `hX` is the tag's own Noetherian hypothesis on `X`, `hi` supplies the reduction as data rather than choosing one from Stacks 0AIN (the convention of the library's Stacks 0GVT and 0GB8), `hT` is the tag's own closedness of `T` in `|X_red|`, `hideal` is the source's own step identifying `X_{/T}` with the completion of a Noetherian affine scheme along an ideal, quantified over its own space, reduction and subset, and `hset` is the set-theoretic condition of Stacks 0AIS on the completion, carried where Stacks 0GVM (`isAffineFormalAlgebraicSpace_colimit`) carries it and needed to transport the conclusion back along the isomorphism. There is deliberately NO quasi-compactness hypothesis: the source notes it is automatic here. The step from `hideal` to the conclusion is Stacks 0GXX (4) (`isNoetherian_completionAlongIdeal`).”.

> Let `S` be a scheme, let `X` be an affine formal algebraic space over `S`, let
> `i : X_red ⟶ X` be a reduction of `X` and let `T ⊆ |X_red|` be closed. If `X` is Noetherian
> then so is the completion `X_{/T}` of `X` along `T`. No quasi-compactness of `|X_red| \ T` is
> assumed.
>
> It takes as hypotheses `hideal : CompletionOfNoetherianIsCompletionAlongNoetherianIdeal` and the
> set-theoretic condition `hset` on `X_{/T}`.

```lean
theorem isNoetherian_completionAlong {X Xred : FppfSheaf B S hS}
    (hX : IsNoetherian B S hS X) {i : Xred ⟶ X}
    (hi : IsReduction B S hS X Xred i)
    (T : Set (Space.pointsULift.{u + 1} B S hS Xred.obj))
    (hT : @IsClosed _ (Space.pointTopologyULift.{u + 1} B S hS Xred.obj) T)
    (hideal : CompletionOfNoetherianIsCompletionAlongNoetherianIdeal B S hS)
    (hset : SatisfiesSetTheoreticCondition B S hS (completionAlong i T)) :
    IsNoetherian B S hS (completionAlong i T)
```

**`AlgebraicGeometry.FormalSpace.isCountablyIndexed_completionAlong'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionAffineClausesTypesSupplement.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionAffineClausesTypesSupplement.lean#L72). The attribute's comment: “clause (3): if `|X_red| \ T` is quasi-compact and `X` is countably indexed then so is `X_{/T}`, countably indexed being `IsCountablyIndexed` (Stacks 0AIJ, StacksFrontier/AlgebraicGeometry/FormalSpace/CountablyIndexed.lean). Carried hypotheses: `hX` is the tag's own countable-indexing hypothesis on `X`, `hi` supplies the reduction as data rather than choosing one from Stacks 0AIN (the convention of Stacks 0GVT and 0GB8), `hT` is the tag's own closedness of `T` in `|X_red|`, `hqc` is the tag's own quasi-compactness of `|X_red| \ T`, stated as compactness of `Tᶜ` for the point topology `Space.pointTopologyULift` since this library has no quasi-compactness predicate for formal algebraic spaces. Nothing else: the source's step producing the weakly admissible ring `lim A/J_{m,n}` with a countable fundamental system of neighbourhoods of zero — condition (2) of Stacks 0AN1 — is not needed at all. The proof goes through condition (1) directly: `isCountablyIndexed_completionSheafULift`, which gets a countable directed presentation of `X_{/T}` from a countable one of `X` and turns it into a sequential one by Stacks 0AII (`isCountablyIndexed_iff_exists_countable_presentation`).”.

> Let `S` be a scheme, let `X` be an affine formal algebraic space over `S`, let
> `i : X_red ⟶ X` be a reduction of `X` and let `T ⊆ |X_red|` be closed with `|X_red| \ T`
> quasi-compact. If `X` is countably indexed then so is the completion `X_{/T}` of `X` along `T`:
> it admits a presentation indexed by `ℕ` by affine schemes along thickenings.

```lean
theorem isCountablyIndexed_completionAlong' {X Xred : FppfSheaf B S hS}
    (hX : IsCountablyIndexed B S hS X) {i : Xred ⟶ X}
    (hi : IsReduction B S hS X Xred i)
    (T : Set (Space.pointsULift.{u + 1} B S hS Xred.obj))
    (hT : @IsClosed _ (Space.pointTopologyULift.{u + 1} B S hS Xred.obj) T)
    (hqc : @IsCompact _ (Space.pointTopologyULift.{u + 1} B S hS Xred.obj) Tᶜ) :
    IsCountablyIndexed B S hS (completionAlong i T)
```

**`AlgebraicGeometry.FormalSpace.isAdicStar_completionAlong'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionAffineClausesTypesSupplement.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionAffineClausesTypesSupplement.lean#L105). The attribute's comment: “clause (4): if `|X_red| \ T` is quasi-compact and `X` is adic* then so is `X_{/T}`, adic* being `IsAdicStar` (Stacks 0AID (4), StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/Types.lean). Carried hypotheses: `hX` is the tag's own adic* hypothesis on `X`, `hi` supplies the reduction as data because Stacks 0AIN is unavailable in this library (the convention of Stacks 0GVT and 0GB8), `hT` is the tag's own closedness of `T` in `|X_red|`, and `hqc` is the tag's own quasi-compactness of `|X_red| \ T`, stated as compactness of `Tᶜ` for the point topology `Space.pointTopologyULift` since this library has no quasi-compactness predicate for formal algebraic spaces. NOTHING ELSE: the source's own step `X_{/T} = Spf (lim A/J^n)` for a finitely generated `J` is PROVED (`exists_fg_quotientSystem_formalSpectrum_iso_completionSheafULift`). Nothing in the chain asks anything of `Spec A` -- no structure morphism to `S` and no site-membership -- exactly as the source asks nothing: the affines of the site cutting out the powers of `J` are quotients of the STAGE rings `A/K`. The set-theoretic condition of Stacks 0AIS is not assumed. The step from `X_{/T} = Spf (lim A/J^n)` to the conclusion is the ring half of Stacks 0GXX (`isAdic_adicCompletion`, `isIdealOfDefinition_map_adicCompletion`, `isWeaklyAdmissible_adicCompletion`) together with clause (2) of this tag (`hasSomeSurjectivePresentation_completionAlong'`).”.

> Let `S` be a scheme, let `X` be an affine formal algebraic space over `S`, let
> `i : X_red ⟶ X` be a reduction of `X` and let `T ⊆ |X_red|` be closed with `|X_red| \ T`
> quasi-compact. If `X` is adic\* then so is the completion `X_{/T}` of `X` along `T`: it is
> presented by an adic topological ring with a finitely generated ideal of definition.

```lean
theorem isAdicStar_completionAlong' {X Xred : FppfSheaf B S hS}
    (hX : IsAdicStar B S hS X) {i : Xred ⟶ X}
    (hi : IsReduction B S hS X Xred i)
    (T : Set (Space.pointsULift.{u + 1} B S hS Xred.obj))
    (hT : @IsClosed _ (Space.pointTopologyULift.{u + 1} B S hS Xred.obj) T)
    (hqc : @IsCompact _ (Space.pointTopologyULift.{u + 1} B S hS Xred.obj) Tᶜ) :
    IsAdicStar B S hS (completionAlong i T)
```

**`AlgebraicGeometry.FormalSpace.isNoetherian_completionAlong'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionAffineClausesTypesSupplement.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionAffineClausesTypesSupplement.lean#L150). The attribute's comment: “clause (5): if `X` is Noetherian then so is `X_{/T}`, Noetherian being `IsNoetherian` (Stacks 0AID (5), StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/Types.lean). Carried hypotheses: `hX` is the tag's own Noetherian hypothesis on `X`, `hi` supplies the reduction as data because Stacks 0AIN is unavailable in this library (the convention of Stacks 0GVT and 0GB8), and `hT` is the tag's own closedness of `T` in `|X_red|`. NOTHING ELSE: the source's own step `X_{/T} = Spf (lim A/J^n)` for a Noetherian `A` is PROVED (`exists_fg_quotientSystem_formalSpectrum_iso_completionSheafULift`). Nothing in the chain asks anything of `Spec A` -- no structure morphism to `S` and no site-membership. There is deliberately NO quasi-compactness hypothesis: it is automatic here, which is `isCompact_of_isNoetherianRing` (the point space of `X` is the prime spectrum of a quotient of the Noetherian presenting ring, hence a Noetherian space). The set-theoretic condition of Stacks 0AIS is not assumed. The step from `X_{/T} = Spf (lim A/J^n)` to the conclusion is Stacks 0316 for the Noetherianness of the adic completion together with the ring half of Stacks 0GXX (`isAdic_adicCompletion`) and clause (2) of this tag (`hasSomeSurjectivePresentation_completionAlong'`).”. References: EGA I (10.8.6), “special case”.

> Let `S` be a scheme, let `X` be an affine formal algebraic space over `S`, let
> `i : X_red ⟶ X` be a reduction of `X` and let `T ⊆ |X_red|` be closed. If `X` is Noetherian
> then so is the completion `X_{/T}` of `X` along `T`: it is presented by a topological ring which
> is both Noetherian and adic.

```lean
theorem isNoetherian_completionAlong' {X Xred : FppfSheaf B S hS}
    (hX : IsNoetherian B S hS X) {i : Xred ⟶ X}
    (hi : IsReduction B S hS X Xred i)
    (T : Set (Space.pointsULift.{u + 1} B S hS Xred.obj))
    (hT : @IsClosed _ (Space.pointTopologyULift.{u + 1} B S hS Xred.obj) T) :
    IsNoetherian B S hS (completionAlong i T)
```

**`AlgebraicGeometry.FormalSpace.hasSomeSurjectivePresentation_completionAlong'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionAffineClausesVariants.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionAffineClausesVariants.lean#L56). The attribute's comment: “clause (2): if `X` is McQuillan so is `X_{/T}`, with McQuillan read as `HasSomeSurjectivePresentation` (condition (4) of Stacks 0AIC, registered for Stacks 0AID at StacksFrontier/AlgebraicGeometry/FormalSpace/Affine/Types.lean). Carried hypotheses: `hX` is the tag's own McQuillan hypothesis on `X`, `hi` supplies the reduction as data because Stacks 0AIN is unavailable in this library (the convention of the library's Stacks 0GVT and 0GB8), and `hT` is the tag's own closedness of `T` in `|X_red|`. Nothing else: the source's step producing condition (2) of Stacks 0AIC for the completion is proved — `hasAffineClosedImmersionCriterion_completionSheafULift`, resting on `completionClosedSubscheme_of_isAffineFormalAlgebraicSpace`; and the set-theoretic condition of Stacks 0AIS on the completion is proved — `satisfiesSetTheoreticCondition_completionSheafULift`. The step from condition (2) to the conclusion is Stacks 0AIC, (2) ⇒ (5) ⇒ (4).”.

> **Clause (2) of Stacks 0GVV.** Let `S` be a scheme, let `X` be a McQuillan affine formal
> algebraic space over `S`, let `i : X_red ⟶ X` be a reduction of `X` and let `T ⊆ |X_red|` be
> closed. Then the completion `X_{/T}` of `X` along `T` is again McQuillan, that is satisfies
> condition (4) of Stacks 0AIC: it is an affine formal algebraic space some presentation of which
> by affine thickenings has all its section-ring projections surjective.
>
> Nothing is assumed beyond the tag's own hypotheses. This is
> `AlgebraicGeometry.FormalSpace.hasSomeSurjectivePresentation_completionSheafULift` in the
> source's spelling `X_{/T}` for a closed subset `T` of the points of a reduction; the source's
> step — write `X = Spf(A)` and observe that `X_{/T} ⟶ X ⟶ Spec(A)` satisfies condition (2) of
> Stacks 0AIC — is
> `AlgebraicGeometry.FormalSpace.hasAffineClosedImmersionCriterion_completionSheafULift`, and the
> geometric content it rests on is
> `AlgebraicGeometry.FormalSpace.completionClosedSubscheme_of_isAffineFormalAlgebraicSpace`: a
> closed immersion of an object of the site into `X_{/T}` is a closed immersion into `X`.

```lean
theorem hasSomeSurjectivePresentation_completionAlong' {X Xred : FppfSheaf B S hS}
    (hX : HasSomeSurjectivePresentation B S hS X) {i : Xred ⟶ X}
    (hi : IsReduction B S hS X Xred i)
    (T : Set (Space.pointsULift.{u + 1} B S hS Xred.obj))
    (hT : @IsClosed _ (Space.pointTopologyULift.{u + 1} B S hS Xred.obj) T) :
    HasSomeSurjectivePresentation B S hS (completionAlong i T)
```

**`AlgebraicGeometry.FormalSpace.completionOfAffineIsAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionAffineSupplement.lean, line 1041](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionAffineSupplement.lean#L1041). The attribute's comment: “clause (1), in the ambient spelling `CompletionOfAffineIsAffine`, quantified over the affine formal algebraic space and over the closed subset of its own points. No hypotheses beyond the tag's own: the set-theoretic condition of Stacks 0AIS on the completions is proved — `satisfiesSetTheoreticCondition_completionSheafULift`; the commutation of completion with directed colimits of fppf sheaves is proved — `completionSheafULiftIsoColimitCompletion`; Stacks 0AIY at the affine stages is `isAffineFormalAlgebraicSpace_completionSheafULift_affineStageSheaf`. No `hred` is needed, the ambient spelling mentioning no reduction. Clause (1) is Stacks 0GVQ, whose registration stays on `isAffineFormalAlgebraicSpace_completionAlong'` above”.

> **Clause (1) of Stacks 0GVV**, in the ambient spelling
> `AlgebraicGeometry.FormalSpace.CompletionOfAffineIsAffine`: the completion of an affine formal
> algebraic space over `S` along a closed set of its points is again an affine formal algebraic
> space, for every such space and every such set at once. It is
> `AlgebraicGeometry.FormalSpace.isAffineFormalAlgebraicSpace_completionAlong'` (Stacks 0GVQ) with
> the reduction removed from the statement: the completion is formed along a closed set of points
> of the space itself, which is what the consumers of clause (1) in this library — the
> base-changed charts of Stacks 0GVR and Stacks 0GVW — supply, and so no `hred` is needed.
>
> Nothing is assumed. The affine presentation is
> `AlgebraicGeometry.FormalSpace.exists_affinePresentation_completionSheafULift` and the
> set-theoretic condition of Stacks 0AIS is
> `AlgebraicGeometry.FormalSpace.satisfiesSetTheoreticCondition_completionSheafULift`.

```lean
theorem completionOfAffineIsAffine : CompletionOfAffineIsAffine' B S hS
```

## Tag 0GVW, a lemma

[Tag 0GVW](https://stacks.math.columbia.edu/tag/0GVW) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isLocallyCountablyIndexed_completionAlong'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionLocalTypes.lean, line 488](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionLocalTypes.lean#L488). The attribute's comment: “clause (1): if the complement of `T` is quasi-compact and `X` is locally countably indexed then so is `X_{/T}` (`IsLocallyCountablyIndexed`, Stacks 0AKY). Binders are exactly the source's data: `T` closed in `|X_red|`, and quasi-compactness (Stacks 03HE, `Space.IsQuasiCompactULift`) of the inclusion of the open subspace `|X_red| \ T` (the subfunctor of sections with point-set image in `Tᶜ`). The set-theoretic condition of 0AIS is proved (0GVR), clause (1) of 0GVV is proved (`completionOfAffineIsAffine`), clause (3) of 0GVV is proved (`isCountablyIndexed_completionAlong'`).”.

> **Clause (1) of Stacks 0GVW.** Let `S` be a scheme, let `X` be a formal algebraic space
> over `S`, let `i : X_red ⟶ X` be a reduction of `X` and let `T ⊆ |X_red|` be closed such that
> the inclusion `|X_red| \ T ⟶ |X_red|` of the open subspace with points `|X_red| \ T` is
> quasi-compact. If `X` is locally countably indexed then so is the completion `X_{/T}` of `X`
> along `T`.
>
> The open subspace `|X_red| \ T` is the subfunctor of the sections of `X_red` with point-set
> image in `Tᶜ`, and the hypothesis `hqc` is quasi-compactness of its inclusion in the sense of
> Stacks 03HE; see the section "The source's quasi-compactness hypothesis" of this file. It is
> transferred to the charts by `complementCompactOnCharts_of_isQuasiCompactULift`, and the
> statement follows from
> `isLocallyCountablyIndexed_completionAlong_of_complementCompactOnCharts`. Nothing else is
> assumed.

```lean
theorem isLocallyCountablyIndexed_completionAlong' {X Xred : FppfSheaf B S hS}
    (hX : IsLocallyCountablyIndexed B S hS X) {i : Xred ⟶ X}
    (hi : IsReduction B S hS X Xred i)
    (T : Set (Space.pointsULift.{u + 1} B S hS Xred.obj))
    (hT : @IsClosed _ (Space.pointTopologyULift.{u + 1} B S hS Xred.obj) T)
    (hqc : Space.IsQuasiCompactULift.{u + 1} B S hS
      (Space.completionSubfunctorULift B S hS Xred.obj Tᶜ).ι) :
    IsLocallyCountablyIndexed B S hS (completionAlong i T)
```

**`AlgebraicGeometry.FormalSpace.isLocallyAdicStar_completionAlong'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionLocalTypes.lean, line 545](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionLocalTypes.lean#L545). The attribute's comment: “clause (2): if the complement of `T` is quasi-compact and `X` is locally adic* then so is `X_{/T}` (`IsLocallyAdicStar`, Stacks 0AKY). Binders are exactly the source's data: `T` closed in `|X_red|`, and quasi-compactness (Stacks 03HE, `Space.IsQuasiCompactULift`) of the inclusion of the open subspace `|X_red| \ T` (the subfunctor of sections with point-set image in `Tᶜ`). The set-theoretic condition of 0AIS is proved (0GVR), clause (4) of 0GVV is proved (`isAdicStar_completionAlong'`).”.

> **Clause (2) of Stacks 0GVW.** Let `S` be a scheme, let `X` be a formal algebraic space
> over `S`, let `i : X_red ⟶ X` be a reduction of `X` and let `T ⊆ |X_red|` be closed such that
> the inclusion `|X_red| \ T ⟶ |X_red|` of the open subspace with points `|X_red| \ T` is
> quasi-compact. If `X` is locally adic\* then so is the completion `X_{/T}` of `X` along `T`.
>
> The hypothesis `hqc` is read as for clause (1), `isLocallyCountablyIndexed_completionAlong'`.
> Nothing else is assumed.

```lean
theorem isLocallyAdicStar_completionAlong' {X Xred : FppfSheaf B S hS}
    (hX : IsLocallyAdicStar B S hS X) {i : Xred ⟶ X}
    (hi : IsReduction B S hS X Xred i)
    (T : Set (Space.pointsULift.{u + 1} B S hS Xred.obj))
    (hT : @IsClosed _ (Space.pointTopologyULift.{u + 1} B S hS Xred.obj) T)
    (hqc : Space.IsQuasiCompactULift.{u + 1} B S hS
      (Space.completionSubfunctorULift B S hS Xred.obj Tᶜ).ι) :
    IsLocallyAdicStar B S hS (completionAlong i T)
```

**`AlgebraicGeometry.FormalSpace.isLocallyNoetherian_completionAlong'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionLocalTypes.lean, line 588](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RecompletionLocalTypes.lean#L588). The attribute's comment: “clause (3): if `X` is locally Noetherian then so is `X_{/T}` (`IsLocallyNoetherian`, Stacks 0AKY); deliberately NO quasi-compactness hypothesis, as in the source. Binders are exactly the source's data: `T` closed in `|X_red|`. The set-theoretic condition of 0AIS is proved (0GVR), clause (5) of 0GVV is proved (`isNoetherian_completionAlong'`).”.

> **Clause (3) of Stacks 0GVW.** Let `S` be a scheme, let `X` be a formal algebraic space
> over `S`, let `i : X_red ⟶ X` be a reduction of `X` and let `T ⊆ |X_red|` be closed. If `X` is
> locally Noetherian then so is the completion `X_{/T}` of `X` along `T`: the completions of the
> charts of `X` along the inverse images of `T` form an atlas as in Definition 0AIM, and each of
> them is a Noetherian affine formal algebraic space by clause (5) of Stacks 0GVV. No
> quasi-compactness hypothesis is needed, the source observing that it holds automatically
> because `|X_red|` is then the spectrum of a Noetherian ring.
>
> Nothing is assumed beyond the source's hypotheses: the set-theoretic condition of Stacks 0AIS
> for `X_{/T}` is `satisfiesSetTheoreticCondition_completionAlong_of_isFormalAlgebraicSpace`
> (Stacks 0GVR), and clause (5) of Stacks 0GVV is
> `AlgebraicGeometry.FormalSpace.isNoetherian_completionAlong'`.

```lean
theorem isLocallyNoetherian_completionAlong' {X Xred : FppfSheaf B S hS}
    (hX : IsLocallyNoetherian B S hS X) {i : Xred ⟶ X}
    (hi : IsReduction B S hS X Xred i)
    (T : Set (Space.pointsULift.{u + 1} B S hS Xred.obj))
    (hT : @IsClosed _ (Space.pointTopologyULift.{u + 1} B S hS Xred.obj) T) :
    IsLocallyNoetherian B S hS (completionAlong i T)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.37, Tag 0GVP](https://stacks.math.columbia.edu/tag/0GVP)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
