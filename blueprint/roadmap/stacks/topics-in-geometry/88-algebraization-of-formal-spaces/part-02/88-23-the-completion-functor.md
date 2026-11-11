---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.isLocallyOfFiniteType_completionSheafMap, AlgebraicGeometry.FormalSpace.isEtale_completionSheafMap, AlgebraicGeometry.FormalSpace.isClosedImmersion_completionSheafMap, AlgebraicGeometry.FormalSpace.isProper_completionSheafMap, AlgebraicGeometry.FormalSpace.isQuasiCompact_completionSheafMap, AlgebraicGeometry.Space.isPullback_completionSheafPullback, AlgebraicGeometry.Space.completionSheafDiagonal_comp_completionSheafInclusion, AlgebraicGeometry.Space.completionSheafDiagonal_eq_completionSheafMap_diagonal
statement: formalized
proof: formalized
---

# 88.23 The completion functor

Section 88.23 of the Stacks Project, [Tag 0GDB](https://stacks.math.columbia.edu/tag/0GDB). 11 tags here are carried by 17 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0AQ9, a lemma

[Tag 0AQ9](https://stacks.math.columbia.edu/tag/0AQ9) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isLocallyOfFiniteType_completionSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionLocallyFiniteType.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionLocallyFiniteType.lean#L114).

> **Stacks 0AQ9.** Let `f : X' ⟶ X` be a morphism of algebraic spaces over `S` and let `T`
> be a set of points of `X`. If `f` is locally of finite type, then the induced morphism of
> completions `X'_{/|f|⁻¹ T} ⟶ X_{/T}` is locally of finite type.

```lean
theorem isLocallyOfFiniteType_completionSheafMap
    {X' X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (f : X' ⟶ X) (T : Set (Space.points B S hS X))
    (hf : Space.IsLocallyOfFiniteType B S hS f) :
    IsLocallyOfFiniteType B S hS (Space.completionSheafMap B S hS f T)
```

## Tag 0GI0, a lemma

[Tag 0GI0](https://stacks.math.columbia.edu/tag/0GI0) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isEtale_completionSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionEtale.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionEtale.lean#L208).

> Let `f : X' ⟶ X` be a morphism of algebraic spaces over `S` and let `T` be a set of points
> of `X`. If `f` is étale, then the induced morphism of completions `X'_{/|f|⁻¹ T} ⟶ X_{/T}` is
> étale: it is representable by algebraic spaces and each of its base changes along a
> scheme-valued point of its target is étale.

```lean
theorem isEtale_completionSheafMap
    {X' X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (f : X' ⟶ X) (T : Set (Space.points B S hS X))
    (hf : Space.IsEtale B S hS f) :
    ∃ hrep : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS
        (Space.completionSheafMap B S hS f T).hom,
      Space.HasPropertyULift.{u + 1} B S hS
        (fun ⦃A C : Space.AlgebraicSpacesULift.{u + 1} B S hS⦄ (g : A ⟶ C) ↦
          Space.IsEtaleULift.{u + 1} B S hS g.hom)
        (Space.completionSheafMap B S hS f T).hom hrep
```

## Tag 0GDC, a lemma

[Tag 0GDC](https://stacks.math.columbia.edu/tag/0GDC) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isClosedImmersion_completionSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionClosedImmersion.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionClosedImmersion.lean#L98).

> **Stacks 0GDC.** Let `f : X' ⟶ X` be a morphism of algebraic spaces over `S` and let `T`
> be a set of points of `X`. If `f` is a closed immersion, then the induced morphism of
> completions `X'_{/|f|⁻¹ T} ⟶ X_{/T}` is a closed immersion of formal algebraic spaces: it is
> representable by algebraic spaces and each of its base changes along a scheme-valued point of
> its target is a closed immersion.

```lean
theorem isClosedImmersion_completionSheafMap
    {X' X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (f : X' ⟶ X) (T : Set (Space.points B S hS X))
    (hf : Space.IsClosedImmersion B S hS f) :
    IsClosedImmersion B S hS (Space.completionSheafMap B S hS f T)
```

## Tag 0GDD, a lemma

[Tag 0GDD](https://stacks.math.columbia.edu/tag/0GDD) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isProper_completionSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionProper.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionProper.lean#L282).

> Let `f : X' ⟶ X` be a morphism of algebraic spaces over `S` and let `T` be a set of points
> of `X`. If `f` is proper, then the induced morphism of completions
> `X'_{/|f|⁻¹ T} ⟶ X_{/T}` is proper.

```lean
theorem isProper_completionSheafMap
    {X' X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (f : X' ⟶ X) (T : Set (Space.points B S hS X))
    (hf : Space.IsProper B S hS f) :
    IsProper B S hS (Space.completionSheafMap B S hS f T)
```

## Tag 0GDE, a lemma

[Tag 0GDE](https://stacks.math.columbia.edu/tag/0GDE) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isQuasiCompact_completionSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionQuasiCompact.lean, line 146](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionQuasiCompact.lean#L146). The attribute's comment: “quasi-compactness of `f_{/T}` in the form of Bootstrap, Definition 03XZ: `f_{/T}` is representable by algebraic spaces and each of its base changes along a scheme-valued point of its target is a quasi-compact morphism of algebraic spaces. For a morphism representable by algebraic spaces this is the quasi-compactness of Stacks 0AJC by Stacks 0AM2, whose proof needs the agreement of the two notions of a quasi-compact space on an algebraic space, `QuasiCompactSpaceAgreesOnAlgebraicSpaces`, which this library does not carry; `isQuasiCompact_completionSheafMap_of_agreesOnAlgebraicSpaces` is the conclusion in the form of Stacks 0AJC granted that agreement”.

> **Stacks 0GDE.** Let `f : X' ⟶ X` be a morphism of algebraic spaces over `S` and let `T`
> be a set of points of `X`. If `f` is quasi-compact, then the induced morphism of completions
> `f_{/T} : X'_{/|f|⁻¹ T} ⟶ X_{/T}` is quasi-compact: it is representable by algebraic spaces
> and each of its base changes along a scheme-valued point of its target is a quasi-compact
> morphism of algebraic spaces.

```lean
theorem isQuasiCompact_completionSheafMap
    {X' X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (f : X' ⟶ X) (T : Set (Space.points B S hS X))
    (hf : Space.IsQuasiCompact B S hS f) :
    ∃ hrep : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS
        (Space.completionSheafMap B S hS f T).hom,
      Space.HasPropertyULift.{u + 1} B S hS
        (Space.quasiCompactPropertyULift.{u + 1} B S hS)
        (Space.completionSheafMap B S hS f T).hom hrep
```

## Tag 0GDF, a remark

[Tag 0GDF](https://stacks.math.columbia.edu/tag/0GDF) in the Stacks Project.

**`AlgebraicGeometry.Space.isPullback_completionSheafPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionDiagonal.lean, line 248](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionDiagonal.lean#L248). The attribute's comment: “fibre product of completions”.

> **Stacks 0GDF.** The completion of a fibre product is the fibre product of the
> completions: for morphisms `f : X' ⟶ X` and `g : Y ⟶ X` of presheaves on the big fppf site of
> `S` and a set `T` of points of `X`, the square formed by `(X' ×_X Y)_{/T''}`, the two
> completions `X'_{/T'}` and `Y_{/T₂}` and `X_{/T}` is cartesian, so that
> `X'_{/T'} ×_{X_{/T}} Y_{/T₂} = (X' ×_X Y)_{/T''}` as subobjects of the ambient sheaf of
> `X' ×_X Y`.

```lean
theorem isPullback_completionSheafPullback (f : X' ⟶ X) (g : Y ⟶ X)
    (T : Set (points B S hS X)) :
    IsPullback (completionSheafPullbackFst B S hS f g T)
      (completionSheafPullbackSnd B S hS f g T)
      (completionSheafMap B S hS f T) (completionSheafMap B S hS g T)
```

**`AlgebraicGeometry.Space.completionSheafDiagonal_comp_completionSheafInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionDiagonal.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionDiagonal.lean#L300). The attribute's comment: “diagonals agree over the fibre product”.

> **Stacks 0GDF.** The diagonal of the completed morphism is the diagonal of the original
> morphism, read inside the ambient sheaf of `X' ×_X X'`: this is the equality
> `Δ_{f_{/T}} = (Δ_f)_{/T''}` of morphisms of subobjects of `X' ×_X X'`, the inclusion of a
> completion into the ambient sheaf being a monomorphism.

```lean
theorem completionSheafDiagonal_comp_completionSheafInclusion (f : X' ⟶ X)
    (T : Set (points B S hS X)) :
    completionSheafDiagonal B S hS f T ≫
        completionSheafInclusion B S hS (pullback f f) (pullbackPoints B S hS f f T) =
      completionSheafInclusion B S hS X' (pointsMap B S hS X' f ⁻¹' T) ≫
        sheafifiedULiftMap B S hS (pullback.diagonal f)
```

**`AlgebraicGeometry.Space.completionSheafDiagonal_eq_completionSheafMap_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionDiagonal.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionDiagonal.lean#L337). The attribute's comment: “equality of diagonals”.

> **Stacks 0GDF.** The diagonal of the completed morphism is the completion of the diagonal:
> `Δ_{f_{/T}} = (Δ_f)_{/T''}` as morphisms `X'_{/T'} ⟶ (X' ×_X X')_{/T''}`. The `eqToHom`
> transports the source of `(Δ_f)_{/T''}`, the completion of `X'` along the inverse image of
> `T''` under the diagonal, to the completion of `X'` along `T'`; the two sets of points are
> equal by `AlgebraicGeometry.Space.pointsMap_diagonal_preimage_pullbackPoints`.

```lean
theorem completionSheafDiagonal_eq_completionSheafMap_diagonal (f : X' ⟶ X)
    (T : Set (points B S hS X)) :
    completionSheafDiagonal B S hS f T =
      eqToHom (congrArg (completionSheaf B S hS X')
          (pointsMap_diagonal_preimage_pullbackPoints B S hS f T).symm) ≫
        completionSheafMap B S hS (pullback.diagonal f) (pullbackPoints B S hS f f T)
```

## Tag 0GDG, a lemma

[Tag 0GDG](https://stacks.math.columbia.edu/tag/0GDG) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isSeparatedMorphism_completionSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSeparated.lean, line 130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSeparated.lean#L130). The attribute's comment: “separated: the completion of a separated morphism of algebraic spaces along a set of points of its target is a separated morphism of formal algebraic spaces, separatedness of the completion read as the separatedness axiom of Stacks 0ARN”.

> **Stacks 0GDG, the separatedness clause.** Let `f : X' ⟶ X` be a morphism of algebraic
> spaces over `S` and let `T` be a set of points of `X`. If `f` is separated, then the induced
> morphism of completions `f_{/T} : X'_{/|f|⁻¹ T} ⟶ X_{/T}` is separated: its relative diagonal
> is the completion of the relative diagonal of `f`, which is a closed immersion by Stacks
> 0GDC.

```lean
theorem isSeparatedMorphism_completionSheafMap
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (f : X' ⟶ X) (T : Set (Space.points B S hS X))
    (hf : Space.IsSeparated B S hS f) :
    IsSeparatedMorphism B S hS (Space.completionSheafMap B S hS f T)
```

**`AlgebraicGeometry.FormalSpace.isQuasiSeparatedMorphism_completionSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSeparated.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionSeparated.lean#L162). The attribute's comment: “quasi-separated: the completion of a quasi-separated morphism of algebraic spaces along a set of points of its target has quasi-compact relative diagonal. Quasi-compactness of the diagonal is read as `IsQuasiSeparatedMorphism`, that is, as `Space.IsQuasiCompactULift`: every base change of the diagonal along a morphism from a quasi-compact algebraic space has quasi-compact source. The implementation notes of `StacksFrontier.AlgebraicGeometry.FormalSpace.SeparatedMorphism` record that condition as a priori stronger than the source's quasi-compactness of a morphism of formal algebraic spaces, so the conclusion delivered is a priori stronger than the source's; the hypothesis is the source's quasi-separatedness of Stacks 03HL, part (3)”.

> **Stacks 0GDG, the quasi-separatedness clause.** Let `f : X' ⟶ X` be a morphism of algebraic
> spaces over `S` and let `T` be a set of points of `X`. If `f` is quasi-separated, then the
> induced morphism of completions `f_{/T} : X'_{/|f|⁻¹ T} ⟶ X_{/T}` has quasi-compact relative
> diagonal: that relative diagonal is the completion of the relative diagonal of `f`, which is
> quasi-compact by Stacks 0GDE.

```lean
theorem isQuasiSeparatedMorphism_completionSheafMap
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (f : X' ⟶ X) (T : Set (Space.points B S hS X))
    (hf : Space.IsQuasiSeparated B S hS f) :
    IsQuasiSeparatedMorphism B S hS (Space.completionSheafMap B S hS f T)
```

## Tag 0GDH, a lemma

[Tag 0GDH](https://stacks.math.columbia.edu/tag/0GDH) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigSmooth_completionSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionRigEtale.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionRigEtale.lean#L307). The attribute's comment: “the affine case, which is part (1) of Stacks 0GAK (`Rig.isRigSmooth_adicCompletionObj_of_smoothAwayFrom`), applied through the reduction to the affine case carried as the hypothesis `hred`: granted the three hypotheses of the lemma it produces, for each affine representable étale square over `f_{/T}`, the Noetherian ring `A₀`, the ideal `I₀` and the finite type `A₀`-algebra `C₀` smooth over `Spec A₀` minus `V(I₀)` of the source's proof, together with the comparison of rig-smoothness of `C₀` completed with rig-smoothness of the arrow of `WAdm^{Noeth}` presenting the square. The source assembles that reduction from Properties of Spaces, Lemma 03FX, the cartesian completion squares of Stacks 0APV, the identification of a chart of the completion with a formal spectrum in the proof of Stacks 0AQ1, and the étale locality of local finite type, of smoothness and of local Noetherianity, none of which this library carries in that combination”.

> **Stacks 0GDH.** In the situation of Stacks 0GDB, if `X` is locally Noetherian, `f` is
> locally of finite type and `U' → U` is smooth, then `f_{/T}` is rig-smooth.
>
> Granted the reduction to the affine case, the lemma is part (1) of Stacks 0GAK applied to the
> affine data that reduction produces, exactly as in the source.

```lean
theorem isRigSmooth_completionSheafMap {X' X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X' ⟶ X)
    (T : Set (Space.points B S hS X))
    (hX : Space.IsLocallyNoetherian B S hS X)
    (hf : Space.IsLocallyOfFiniteType B S hS f)
    (hsm : Space.IsSmooth B S hS (Space.openComplementRestriction B S hS f T))
    (hred : ChartSquareReducesToSmoothAwayFrom B S hS f T) :
    IsRigSmooth B S hS (Space.completionSheafMap B S hS f T)
```

**`AlgebraicGeometry.FormalSpace.isRigSmooth_completionSheafMap_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionRigSmoothCover.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionRigSmoothCover.lean#L329).

> **Stacks 0GDH.** Let `f : X' ⟶ X` be a morphism of algebraic spaces over `S`, let
> `T ⊆ |X|` be closed, and let `U ⊆ X` be the open complement of `T` and `U' = f⁻¹U` (the
> situation of Stacks 0GDB). If `X` is locally Noetherian, `f` is locally of finite type and
> `U' → U` is smooth, then the completion `f_{/T} : X'_{/T'} ⟶ X_{/T}` is rig-smooth.
>
> The proof is the source's: compatible étale atlases of `X` and `X'` by spectra of rings
> (Properties of Spaces, Lemma 03FX; `exists_compatible_affineOver_atlases`), condition (4) of
> Stacks 0GCQ for `f_{/T}` from them
> (`correspondsToNoetherianMapAfterSourceCover_isRigSmoothArrow_completionSheafMap`: the reduction
> to the affine case and the affine case by Stacks 0GAK and Stacks 0GAM), and the implication
> (4) ⟹ (1) of Stacks 0GCQ.

```lean
theorem isRigSmooth_completionSheafMap_of_isLocallyNoetherian
    {X' X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX' : IsAlgebraicSpace B S hS X')
    (hX : IsAlgebraicSpace B S hS X) (f : X' ⟶ X) (T : Set (Space.points B S hS X))
    (hT : @IsClosed _ (Space.pointTopology B S hS X) T)
    (hXN : Space.IsLocallyNoetherian B S hS X)
    (hf : Space.IsLocallyOfFiniteType B S hS f)
    (hsm : Space.IsSmooth B S hS (Space.openComplementRestriction B S hS f T)) :
    IsRigSmooth B S hS (Space.completionSheafMap B S hS f T)
```

## Tag 0AR2, a lemma

[Tag 0AR2](https://stacks.math.columbia.edu/tag/0AR2) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigEtale_completionSheafMap_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionAtlasCompatible.lean, line 386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionAtlasCompatible.lean#L386).

> **Stacks 0AR2.** Let `f : X' ⟶ X` be a morphism of algebraic spaces over `S`, let
> `T ⊆ |X|` be closed, and let `U ⊆ X` be the open complement of `T` and `U' = f⁻¹U` (the
> situation of Stacks 0GDB). If `X` is locally Noetherian, `f` is locally of finite type and
> `U' → U` is étale, then the completion `f_{/T} : X'_{/T'} ⟶ X_{/T}` is rig-étale.
>
> The proof is the source's: compatible étale atlases of `X` and `X'` by spectra of rings
> (Properties of Spaces, Lemma 03FX; `exists_compatible_affineOver_atlases`), condition (4) of
> Stacks 0GCZ for `f_{/T}` from them (`correspondsToRigEtaleMapAfterSourceCover_completionSheafMap`:
> the reduction to the affine case and the affine case by part (1) of Stacks 0ALQ), and the
> implication (4) ⟹ (1) of Stacks 0GCZ.

```lean
theorem isRigEtale_completionSheafMap_of_isLocallyNoetherian
    {X' X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX' : IsAlgebraicSpace B S hS X')
    (hX : IsAlgebraicSpace B S hS X) (f : X' ⟶ X) (T : Set (Space.points B S hS X))
    (hT : @IsClosed _ (Space.pointTopology B S hS X) T)
    (hXN : Space.IsLocallyNoetherian B S hS X)
    (hf : Space.IsLocallyOfFiniteType B S hS f)
    (het : Space.IsEtale B S hS (Space.openComplementRestriction B S hS f T)) :
    IsRigEtale B S hS (Space.completionSheafMap B S hS f T)
```

**`AlgebraicGeometry.FormalSpace.isRigEtale_completionSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionRigEtale.lean, line 339](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionRigEtale.lean#L339). The attribute's comment: “the affine case, which is part (1) of Stacks 0ALQ (`Rig.isRigEtale_adicCompletionObj_of_isEtaleOutside`), applied through the reduction to the affine case carried as the hypothesis `hred`: granted the three hypotheses of the lemma it produces, for each affine representable étale square over `f_{/T}`, the Noetherian ring `A₀`, the ideal `I₀` and the finite type `A₀`-algebra `C₀` étale over `Spec A₀` minus `V(I₀)` of the source's proof, together with the comparison of rig-étaleness of `C₀` completed with rig-étaleness of the arrow of `WAdm^{Noeth}` presenting the square. This is the substitution of Lemmas 0ALQ and 0GCZ for Lemmas 0GAK and 0GCQ that the source's proof prescribes; the reduction itself is assembled in the source from Properties of Spaces, Lemma 03FX, the cartesian completion squares of Stacks 0APV, the identification of a chart of the completion with a formal spectrum in the proof of Stacks 0AQ1, and the étale locality of local finite type, of étaleness and of local Noetherianity, none of which this library carries in that combination”.

> **Stacks 0AR2.** In the situation of Stacks 0GDB, if `X` is locally Noetherian, `f` is
> locally of finite type and `U' → U` is étale, then `f_{/T}` is rig-étale.
>
> Granted the reduction to the affine case, the lemma is part (1) of Stacks 0ALQ applied to the
> affine data that reduction produces; this is the proof of Stacks 0GDH with Lemmas 0GAK and
> 0GCQ replaced by Lemmas 0ALQ and 0GCZ, as the source says.

```lean
theorem isRigEtale_completionSheafMap {X' X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X' ⟶ X)
    (T : Set (Space.points B S hS X))
    (hX : Space.IsLocallyNoetherian B S hS X)
    (hf : Space.IsLocallyOfFiniteType B S hS f)
    (het : Space.IsEtale B S hS (Space.openComplementRestriction B S hS f T))
    (hred : ChartSquareReducesToIsEtaleOutside B S hS f T) :
    IsRigEtale B S hS (Space.completionSheafMap B S hS f T)
```

**`AlgebraicGeometry.FormalSpace.isRigEtale_completionSheafMap_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionRigEtaleCharts.lean, line 692](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionRigEtaleCharts.lean#L692).

> **Stacks 0AR2.** Let `f : X' ⟶ X` be a morphism of algebraic spaces over `S`, let `T ⊆ |X|`
> be closed and let `U' ⟶ U` be the restriction of `f` to the open complements of `T' = |f|⁻¹T`
> and `T`. If `X` is locally Noetherian, `f` is locally of finite type and `U' ⟶ U` is étale, then
> `f_{/T} : X'_{/T'} ⟶ X_{/T}` is rig-étale.
>
> The proof is the source's, through condition (4) of Stacks 0GCZ. Cover `X` by affine étale
> charts `Spec A_k ⟶ X` (`exists_affine_etale_charts`) and each `Spec A_k ×_X X'` by affine étale
> charts `Spec C_kl`; the completions `(Spec C_kl)_{/T}` cover `X'_{/T'}` (Stacks 0APV), each
> factors through the chart `(Spec A_k)_{/T}` of `X_{/T}` by the completion of
> `Spec C_kl ⟶ Spec A_k`, and that completion corresponds to a rig-étale map by the affine case
> (`correspondsToRigEtaleMap_completionSheafMap_of_etaleAt`, which is part (1) of Stacks 0ALQ):
> the chart map `Spec C_kl ⟶ Spec A_k` is locally of finite type, `A_k` is Noetherian, and the
> chart map is étale over the complement of `T` because `U' ⟶ U` is.

```lean
theorem isRigEtale_completionSheafMap_of_isEtale {X' X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X) (f : X' ⟶ X)
    (T : Set (Space.points B S hS X)) (hT : IsClosed T)
    (hXN : Space.IsLocallyNoetherian B S hS X) (hf : Space.IsLocallyOfFiniteType B S hS f)
    (het : Space.IsEtale B S hS (Space.openComplementRestriction B S hS f T)) :
    IsRigEtale B S hS (Space.completionSheafMap B S hS f T)
```

## Tag 0AQW, a lemma

[Tag 0AQW](https://stacks.math.columbia.edu/tag/0AQW) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigSurjective_completionSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/ProperValuativeLifting.lean, line 789](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/ProperValuativeLifting.lean#L789).

> **Stacks 0AQW.** In the situation of Stacks 0GDB, let `f : X' ⟶ X` be a proper morphism of
> algebraic spaces over `S`, let `T` be a closed set of points of `X`, and let the restriction
> `U' ⟶ U` of `f` to the open complements of `T` and of `T' = |f|⁻¹ T` be surjective. Then the
> morphism of completions `f_{/T} : X'_{/T'} ⟶ X_{/T}` is rig-surjective.
>
> An adic morphism `p : Spf R ⟶ X_{/T}` out of a complete discrete valuation ring `R` algebraizes
> by Stacks 0GBU to a morphism `Spec R ⟶ X` whose fibre over `T` is the closed point, so its
> generic point lies over `U`. The valuative step
> `AlgebraicGeometry.Space.exists_isExtension_lift_of_isProper_of_isSurjective` (Stacks 00PH,
> 0A40 and 0AP1) produces an extension `R ⊂ R'` of complete discrete valuation rings and a point
> `Spec R' ⟶ X'` over `Spec R' ⟶ Spec R ⟶ X`. Restricted to `Spf R'` and paired with
> `Spf R' ⟶ Spf R ⟶ X_{/T}`, it lands in `X'_{/T'}` because the completion square of Stacks 0APV
> is cartesian, and this is the lift.
>
> The source also assumes `X` locally Noetherian, so that `f_{/T}` is a morphism of locally
> Noetherian formal algebraic spaces and the algebraization of Stacks 0GBU is available as stated;
> neither use is needed here, and the statement is proved without that hypothesis.

```lean
theorem isRigSurjective_completionSheafMap {X' X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (f : X' ⟶ X) (T : Set (Space.points B S hS X))
    (hT : @IsClosed _ (Space.pointTopology B S hS X) T) (hf : Space.IsProper B S hS f)
    (hsurj : Space.IsSurjective B S hS
      ((Space.openSubspaceOfPoints B S hS X Tᶜ).fromPreimage f)) :
    IsRigSurjective B S hS (Space.completionSheafMap B S hS f T)
```

## Tag 0GDI, a lemma

[Tag 0GDI](https://stacks.math.columbia.edu/tag/0GDI) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigSurjective_diagonal_completionSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionDiagonalRigSurjective.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/FormalSpace/CompletionDiagonalRigSurjective.lean#L170).

> **Stacks 0GDI.** In the situation of Stacks 0GDB, let `f : X' ⟶ X` be a separated morphism
> of algebraic spaces over `S`, let `T` be a closed set of points of `X`, and let the restriction
> `U' ⟶ U` of `f` to the open complements of `T` and of `T' = |f|⁻¹ T` be a monomorphism. Then
> the diagonal `Δ_{f_{/T}} : X'_{/T'} ⟶ X'_{/T'} ×_{X_{/T}} X'_{/T'}` of the completed morphism
> is rig-surjective.
>
> By Stacks 0GDF it is the completion of `Δ_f : X' ⟶ X' ×_X X'` along the set of points over
> `T`, up to isomorphisms; `Δ_f` is a closed immersion, hence proper, and is surjective over the
> complement of `T`, so Stacks 0AQW applies. The source's hypotheses that `X` be locally
> Noetherian and `f` locally of finite type are not needed.

```lean
theorem isRigSurjective_diagonal_completionSheafMap {X' X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX' : IsAlgebraicSpace B S hS X') (hX : IsAlgebraicSpace B S hS X)
    (f : X' ⟶ X) (T : Set (Space.points B S hS X))
    (hT : @IsClosed _ (Space.pointTopology B S hS X) T) (hf : Space.IsSeparated B S hS f)
    (hmono : Mono ((Space.openSubspaceOfPoints B S hS X Tᶜ).fromPreimage f)) :
    IsRigSurjective B S hS (pullback.diagonal (Space.completionSheafMap B S hS f T))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.23, Tag 0GDB](https://stacks.math.columbia.edu/tag/0GDB)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
