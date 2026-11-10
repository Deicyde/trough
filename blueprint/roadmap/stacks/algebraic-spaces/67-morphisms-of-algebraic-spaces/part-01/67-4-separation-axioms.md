---
declaration: section
origin: cited
lean: AlgebraicGeometry.relativelyRepresentable_pullbackDiagonal, AlgebraicGeometry.Space.IsSeparated, AlgebraicGeometry.Space.IsLocallySeparated, AlgebraicGeometry.Space.IsQuasiSeparated, AlgebraicGeometry.Space.separationProperties_of_relativelyRepresentable, AlgebraicGeometry.presheaf_locallyOfFiniteType_pullbackDiagonal, AlgebraicGeometry.presheaf_monomorphisms_pullbackDiagonal, AlgebraicGeometry.presheaf_isSeparated_pullbackDiagonal
statement: formalized
proof: formalized
---

# 67.4 Separation axioms

Section 67.4 of the Stacks Project, [Tag 03HJ](https://stacks.math.columbia.edu/tag/03HJ). 14 tags here are carried by 55 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03HJ, the section

[Tag 03HJ](https://stacks.math.columbia.edu/tag/03HJ) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.relativelyRepresentable_pullbackDiagonal`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDiagonal.lean#L96), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxiomsSection.lean, line 33](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxiomsSection.lean#L33) (StacksFrontier): “the relative diagonal is representable”.
- [`AlgebraicGeometry.Space.IsSeparated`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean#L274), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxiomsSection.lean, line 35](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxiomsSection.lean#L35) (StacksFrontier): “separated morphisms”.
- [`AlgebraicGeometry.Space.IsLocallySeparated`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean#L280), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxiomsSection.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxiomsSection.lean#L36) (StacksFrontier): “locally separated morphisms”.
- [`AlgebraicGeometry.Space.IsQuasiSeparated`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean#L286), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxiomsSection.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxiomsSection.lean#L37) (StacksFrontier): “quasi-separated morphisms”.
- [`AlgebraicGeometry.Space.separationProperties_of_relativelyRepresentable`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RepresentableSeparationMatch.lean#L68), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxiomsSection.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxiomsSection.lean#L38) (StacksFrontier): “agreement with the notions for representable morphisms”.

## Tag 03HK, a lemma

[Tag 03HK](https://stacks.math.columbia.edu/tag/03HK) in the Stacks Project.

**`AlgebraicGeometry.relativelyRepresentable_pullbackDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDiagonal.lean, line 96](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDiagonal.lean#L96). The attribute's comment: “part (1)”.

> **Stacks 03HK, part (1).** The relative diagonal of a morphism out of an algebraic space
> over `S` is relatively representable. The target need not be an algebraic space: the relative
> diagonal is a base change of the absolute diagonal of the source, which is representable by
> the second defining clause of `AlgebraicGeometry.IsAlgebraicSpace`.

```lean
theorem relativelyRepresentable_pullbackDiagonal (f : F ⟶ G)
    (hF : IsAlgebraicSpace B S hS F) :
    yoneda.relativelyRepresentable (pullback.diagonal f)
```

**`AlgebraicGeometry.presheaf_locallyOfFiniteType_pullbackDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDiagonalProperties.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDiagonalProperties.lean#L53). The attribute's comment: “part (2)”.

> **Stacks 03HK, part (2).** The relative diagonal of a morphism out of an algebraic space
> over `S` is locally of finite type.

```lean
theorem presheaf_locallyOfFiniteType_pullbackDiagonal (f : F ⟶ G)
    (hF : IsAlgebraicSpace B S hS F) :
    (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@LocallyOfFiniteType.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS))) (pullback.diagonal f)
```

**`AlgebraicGeometry.presheaf_monomorphisms_pullbackDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDiagonalProperties.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDiagonalProperties.lean#L64). The attribute's comment: “part (3)”.

> **Stacks 03HK, part (3).** Every represented base change of the relative diagonal of a
> morphism out of an algebraic space over `S` is a monomorphism of schemes.

```lean
theorem presheaf_monomorphisms_pullbackDiagonal (f : F ⟶ G)
    (hF : IsAlgebraicSpace B S hS F) :
    (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (MorphismProperty.monomorphisms Scheme.{u})
      (BigFppfOver.toScheme B S hS))) (pullback.diagonal f)
```

**`AlgebraicGeometry.presheaf_isSeparated_pullbackDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDiagonalProperties.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDiagonalProperties.lean#L75). The attribute's comment: “part (4)”.

> **Stacks 03HK, part (4).** The relative diagonal of a morphism out of an algebraic space
> over `S` is separated.

```lean
theorem presheaf_isSeparated_pullbackDiagonal (f : F ⟶ G)
    (hF : IsAlgebraicSpace B S hS F) :
    (MorphismProperty.presheaf (MorphismProperty.inverseImage
      (@IsSeparated.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS))) (pullback.diagonal f)
```

**`AlgebraicGeometry.presheaf_locallyQuasiFinite_pullbackDiagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDiagonalProperties.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDiagonalProperties.lean#L86). The attribute's comment: “part (5)”.

> **Stacks 03HK, part (5).** The relative diagonal of a morphism out of an algebraic space
> over `S` is locally quasi-finite.

```lean
theorem presheaf_locallyQuasiFinite_pullbackDiagonal (f : F ⟶ G)
    (hF : IsAlgebraicSpace B S hS F) :
    (MorphismProperty.presheaf (MorphismProperty.inverseImage
      ((@LocallyOfFiniteType.{u} : MorphismProperty Scheme.{u}) ⊓
        (@LocallyQuasiFinite.{u} : MorphismProperty Scheme.{u}))
      (BigFppfOver.toScheme B S hS))) (pullback.diagonal f)
```

**`AlgebraicGeometry.Space.monomorphisms_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedDiagonal.lean, line 192](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedDiagonal.lean#L192). The attribute's comment: “representable and a monomorphism”.

> **Stacks 03HK, representability and the monomorphism condition.** The relative diagonal of
> a morphism of algebraic spaces over `S` is representable and a monomorphism after every
> represented base change.
>
> It is the base change of the absolute diagonal of the source along `X ×_Y X ⟶ X ⨯ X`
> (`AlgebraicGeometry.isPullback_pullbackDiagonal_diag`), and for the absolute diagonal this is
> part (2) of [Stacks Project, Tag 02X4]. Algebraicity of the target is not needed.

```lean
theorem monomorphisms_diagonal (hX : IsAlgebraicSpace B S hS X) (f : X ⟶ Y) :
    (MorphismProperty.inverseImage (MorphismProperty.monomorphisms Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf (pullback.diagonal f)
```

**`AlgebraicGeometry.Space.locallyOfFiniteType_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedDiagonal.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedDiagonal.lean#L203). The attribute's comment: “locally of finite type”.

> **Stacks 03HK, local finite type.** Every represented base change of the relative diagonal
> of a morphism of algebraic spaces over `S` is a morphism of schemes which is locally of finite
> type. This is part (1) of [Stacks Project, Tag 02X4] transported along
> `AlgebraicGeometry.isPullback_pullbackDiagonal_diag`.

```lean
theorem locallyOfFiniteType_diagonal (hX : IsAlgebraicSpace B S hS X) (f : X ⟶ Y) :
    (MorphismProperty.inverseImage
      (@AlgebraicGeometry.LocallyOfFiniteType.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf (pullback.diagonal f)
```

**`AlgebraicGeometry.Space.isSeparated_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedDiagonal.lean, line 215](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedDiagonal.lean#L215). The attribute's comment: “separated”.

> **Stacks 03HK, separatedness.** Every represented base change of the relative diagonal of a
> morphism of algebraic spaces over `S` is a separated morphism of schemes. This is part (3) of
> [Stacks Project, Tag 02X4] transported along
> `AlgebraicGeometry.isPullback_pullbackDiagonal_diag`.

```lean
theorem isSeparated_diagonal (hX : IsAlgebraicSpace B S hS X) (f : X ⟶ Y) :
    (MorphismProperty.inverseImage
      (@_root_.AlgebraicGeometry.IsSeparated.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).presheaf (pullback.diagonal f)
```

**`AlgebraicGeometry.Space.locallyQuasiFinite_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedDiagonal.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UnramifiedDiagonal.lean#L227). The attribute's comment: “locally quasi-finite”.

> **Stacks 03HK, local quasi-finiteness.** Every represented base change of the relative
> diagonal of a morphism of algebraic spaces over `S` is a morphism of schemes which is locally
> of finite type and locally quasi-finite. This is part (4) of [Stacks Project, Tag 02X4]
> transported along `AlgebraicGeometry.isPullback_pullbackDiagonal_diag`.

```lean
theorem locallyQuasiFinite_diagonal (hX : IsAlgebraicSpace B S hS X) (f : X ⟶ Y) :
    (MorphismProperty.inverseImage
      ((@AlgebraicGeometry.LocallyOfFiniteType.{u} : MorphismProperty Scheme.{u}) ⊓
        (@AlgebraicGeometry.LocallyQuasiFinite.{u} : MorphismProperty Scheme.{u}))
      (BigFppfOver.toScheme B S hS)).presheaf (pullback.diagonal f)
```

## Tag 03HL, a definition

[Tag 03HL](https://stacks.math.columbia.edu/tag/03HL) in the Stacks Project.

**`AlgebraicGeometry.Space.IsSeparated`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean, line 274](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean#L274). The attribute's comment: “part (1): separated”. References: EGA I (5.4.1).

> **Stacks 03HL, part (1).** A morphism of algebraic spaces over `S` is *separated* when
> its relative diagonal is a closed immersion.

```lean
abbrev IsSeparated (f : F ⟶ G) : Prop
```

**`AlgebraicGeometry.Space.IsLocallySeparated`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean#L280). The attribute's comment: “part (2): locally separated”.

> **Stacks 03HL, part (2).** A morphism of algebraic spaces over `S` is *locally
> separated* when its relative diagonal is an immersion.

```lean
abbrev IsLocallySeparated (f : F ⟶ G) : Prop
```

**`AlgebraicGeometry.Space.IsQuasiSeparated`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean, line 286](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms.lean#L286). The attribute's comment: “part (3): quasi-separated”. References: EGA IV (1.2.1); SGA 4 VI (1.7), “quasi-separated”.

> **Stacks 03HL, part (3).** A morphism of algebraic spaces over `S` is
> *quasi-separated* when its relative diagonal is quasi-compact.

```lean
abbrev IsQuasiSeparated (f : F ⟶ G) : Prop
```

## Tag 03KK, a lemma

[Tag 03KK](https://stacks.math.columbia.edu/tag/03KK) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallySeparated_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedVariants.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedVariants.lean#L65). The attribute's comment: “locally separated”.

> A separated morphism of algebraic spaces over `S` is locally separated.

```lean
theorem isLocallySeparated_of_isSeparated
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : F ⟶ G} (hf : IsSeparated B S hS f) :
    IsLocallySeparated B S hS f
```

**`AlgebraicGeometry.Space.isQuasiSeparated_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedVariants.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedVariants.lean#L72). The attribute's comment: “quasi-separated”.

> A separated morphism of algebraic spaces over `S` is quasi-separated.

```lean
theorem isQuasiSeparated_of_isSeparated
    {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : F ⟶ G} (hf : IsSeparated B S hS f) :
    IsQuasiSeparated B S hS f
```

## Tag 03KL, a lemma

[Tag 03KL](https://stacks.math.columbia.edu/tag/03KL) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiSeparated_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationBaseChange.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FinitePresentationBaseChange.lean#L63). The attribute's comment: “quasi_separated_base_change”. References: SGA 4 VI (1.9.1), “(ii), special case”.

> A base change of a quasi-separated morphism of algebraic spaces over `S` is quasi-separated.

```lean
theorem isQuasiSeparated_pullback {X Y Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : X ⟶ Y) (g : Y' ⟶ Y) (hf : IsQuasiSeparated B S hS f) :
    IsQuasiSeparated B S hS (pullback.snd f g)
```

**`AlgebraicGeometry.Space.isSeparated_pullbackSnd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedTfae.lean, line 666](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedTfae.lean#L666). The attribute's comment: “separated_base_change”.

> A separated morphism stays separated after any base change.

```lean
theorem isSeparated_pullbackSnd {Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : X ⟶ Y} (g : Z ⟶ Y)
    (h : IsSeparated B S hS f) : IsSeparated B S hS (pullback.snd f g)
```

**`AlgebraicGeometry.Space.isSeparated_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparationMorphismProperties.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparationMorphismProperties.lean#L82). The attribute's comment: “separated_base_change”.

> A base change of a separated morphism of algebraic spaces over `S` is separated.

```lean
theorem isSeparated_pullback {X Y Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : X ⟶ Y) (g : Y' ⟶ Y) (hf : IsSeparated B S hS f) :
    IsSeparated B S hS (pullback.snd f g)
```

**`AlgebraicGeometry.Space.isLocallySeparated_pullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparationMorphismProperties.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparationMorphismProperties.lean#L92). The attribute's comment: “locally_separated_base_change”.

> A base change of a locally separated morphism of algebraic spaces over `S` is locally
> separated.

```lean
theorem isLocallySeparated_pullback {X Y Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (f : X ⟶ Y) (g : Y' ⟶ Y) (hf : IsLocallySeparated B S hS f) :
    IsLocallySeparated B S hS (pullback.snd f g)
```

## Tag 03KN, a lemma

[Tag 03KN](https://stacks.math.columbia.edu/tag/03KN) in the Stacks Project.

**`AlgebraicGeometry.Space.isLocallyOfFiniteType_mapDesc'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartBridge.lean, line 167](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartBridge.lean#L167). The attribute's comment: “part (1): locally of finite type”.

> **Stacks 03KN, part (1).** The comparison `X ×[Z] Y ⟶ X ×[T] Y` is locally of finite type in
> the sense of Stacks 03XF. This is
> `AlgebraicGeometry.Space.isLocallyOfFiniteType_mapDesc` with its hypothesis discharged.

```lean
theorem isLocallyOfFiniteType_mapDesc' (f : X ⟶ Z) (g : Y ⟶ Z) (h : Z ⟶ T)
    (hZ : IsAlgebraicSpace B S hS Z) :
    IsLocallyOfFiniteType B S hS (pullback.mapDesc f g h)
```

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_mapDesc'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartBridge.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/EtaleChartBridge.lean#L177). The attribute's comment: “part (1): locally quasi-finite”.

> **Stacks 03KN, part (1).** The comparison `X ×[Z] Y ⟶ X ×[T] Y` is locally quasi-finite in
> the sense of Stacks 03XJ. This is
> `AlgebraicGeometry.Space.isLocallyQuasiFinite_mapDesc` with its hypothesis discharged.

```lean
theorem isLocallyQuasiFinite_mapDesc' (f : X ⟶ Z) (g : Y ⟶ Z) (h : Z ⟶ T)
    (hZ : IsAlgebraicSpace B S hS Z) :
    IsLocallyQuasiFinite B S hS (pullback.mapDesc f g h)
```

**`CategoryTheory.Limits.pullback.mono_mapDesc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MapDescent.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/MapDescent.lean#L60). The attribute's comment: “part (1): monomorphism”.

> The canonical comparison `X ×[Z] Y ⟶ X ×[T] Y` induced by a morphism `Z ⟶ T` is a
> monomorphism.

```lean
instance pullback.mono_mapDesc {X Y Z T : C} (f : X ⟶ Z) (g : Y ⟶ Z) (i : Z ⟶ T)
    [HasPullback f g] [HasPullback (f ≫ i) (g ≫ i)] :
    Mono (pullback.mapDesc f g i)
```

**`AlgebraicGeometry.Space.relativelyRepresentable_mapDesc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MapDescent.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/MapDescent.lean#L162). The attribute's comment: “part (1): representable”.

> The comparison of fibre products is representable.

```lean
theorem relativelyRepresentable_mapDesc (f : X ⟶ Z) (g : Y ⟶ Z) (h : Z ⟶ T)
    (hZ : IsAlgebraicSpace B S hS Z) :
    yoneda.relativelyRepresentable (pullback.mapDesc f g h)
```

**`AlgebraicGeometry.Space.isSeparated_mapDesc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MapDescent.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/MapDescent.lean#L171). The attribute's comment: “part (1): separated”.

> The comparison of fibre products is separated.

```lean
theorem isSeparated_mapDesc (f : X ⟶ Z) (g : Y ⟶ Z) (h : Z ⟶ T) :
    IsSeparated B S hS (pullback.mapDesc f g h)
```

**`AlgebraicGeometry.Space.isImmersion_mapDesc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MapDescent.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/MapDescent.lean#L180). The attribute's comment: “part (2)”. References: EGA I (5.3.10).

> The comparison of fibre products is an immersion when `h : Z ⟶ T` is locally separated.

```lean
theorem isImmersion_mapDesc (f : X ⟶ Z) (g : Y ⟶ Z) (h : Z ⟶ T)
    (hh : IsLocallySeparated B S hS h) :
    IsImmersion B S hS (pullback.mapDesc f g h)
```

**`AlgebraicGeometry.Space.isClosedImmersion_mapDesc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MapDescent.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/MapDescent.lean#L187). The attribute's comment: “part (3)”. References: EGA I (5.4.2).

> The comparison of fibre products is a closed immersion when `h : Z ⟶ T` is separated.

```lean
theorem isClosedImmersion_mapDesc (f : X ⟶ Z) (g : Y ⟶ Z) (h : Z ⟶ T)
    (hh : IsSeparated B S hS h) :
    IsClosedImmersion B S hS (pullback.mapDesc f g h)
```

**`AlgebraicGeometry.Space.isQuasiCompact_mapDesc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/MapDescent.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/MapDescent.lean#L194). The attribute's comment: “part (4)”.

> The comparison of fibre products is quasi-compact when `h : Z ⟶ T` is quasi-separated.

```lean
theorem isQuasiCompact_mapDesc (f : X ⟶ Z) (g : Y ⟶ Z) (h : Z ⟶ T)
    (hh : IsQuasiSeparated B S hS h) :
    IsQuasiCompact B S hS (pullback.mapDesc f g h)
```

## Tag 03KO, a lemma

[Tag 03KO](https://stacks.math.columbia.edu/tag/03KO) in the Stacks Project.

**`AlgebraicGeometry.Space.separationProperties_graph`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/GraphSeparationProperties.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/GraphSeparationProperties.lean#L54).

> **Stacks 03KO.** Let `Z` be an algebraic space over the scheme `S` and let `f : X ⟶ Y` be
> a morphism of algebraic spaces over `Z`.  For the graph `i : X ⟶ X ×[Z] Y` of `f`:
>
> 1. `i` is representable, locally of finite type, locally quasi-finite, separated and a
>    monomorphism;
> 2. if `Y ⟶ Z` is locally separated then `i` is an immersion;
> 3. if `Y ⟶ Z` is separated then `i` is a closed immersion; and
> 4. if `Y ⟶ Z` is quasi-separated then `i` is quasi-compact.
>
> The graph is a section of the first projection of `X ×[Z] Y`, and all four parts are the
> corresponding parts of Stacks 03KP for that section; parts (2), (3) and (4) use in addition
> that the first projection inherits the relevant separation property from `Y ⟶ Z` as a base
> change of it.

```lean
theorem separationProperties_graph {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (g : Y ⟶ Z) (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) :
    (yoneda.relativelyRepresentable (graph B S hS f g) ∧
        IsLocallyOfFiniteType B S hS (graph B S hS f g) ∧
        IsLocallyQuasiFinite B S hS (graph B S hS f g) ∧
        IsSeparated B S hS (graph B S hS f g) ∧
        Mono (graph B S hS f g)) ∧
      (IsLocallySeparated B S hS g → IsImmersion B S hS (graph B S hS f g)) ∧
      (IsSeparated B S hS g → IsClosedImmersion B S hS (graph B S hS f g)) ∧
      (IsQuasiSeparated B S hS g → IsQuasiCompact B S hS (graph B S hS f g))
```

## Tag 03KP, a lemma

[Tag 03KP](https://stacks.math.columbia.edu/tag/03KP) in the Stacks Project.

**`AlgebraicGeometry.Space.mono_of_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedCriteria.lean, line 340](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedCriteria.lean#L340). The attribute's comment: “part (1): monomorphism”.

> **Stacks 03KP, part (1).** A section of a morphism of algebraic spaces over `S` is a
> monomorphism, being a split monomorphism.

```lean
theorem mono_of_section (p : P ⟶ V) (s : V ⟶ P) (hs : s ≫ p = 𝟙 V) : Mono s
```

**`AlgebraicGeometry.Space.isSeparated_of_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedCriteria.lean, line 347](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedCriteria.lean#L347). The attribute's comment: “part (1): separated”.

> **Stacks 03KP, part (1).** A section of a morphism of algebraic spaces over `S` is
> separated.

```lean
theorem isSeparated_of_section (p : P ⟶ V) (s : V ⟶ P) (hs : s ≫ p = 𝟙 V) :
    IsSeparated B S hS s
```

**`AlgebraicGeometry.Space.relativelyRepresentable_of_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedCriteria.lean, line 377](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedCriteria.lean#L377). The attribute's comment: “part (1): representable”.

> **Stacks 03KP, part (1).** A section of a morphism of algebraic spaces over `S` with
> algebraic total space is representable.

```lean
theorem relativelyRepresentable_of_section (p : P ⟶ V)
    (hP : IsAlgebraicSpace B S hS P) (s : V ⟶ P) (hs : s ≫ p = 𝟙 V) :
    yoneda.relativelyRepresentable s
```

**`AlgebraicGeometry.Space.isLocallyOfFiniteType_of_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedCriteria.lean, line 385](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedCriteria.lean#L385). The attribute's comment: “part (1): locally of finite type”.

> **Stacks 03KP, part (1).** A section of a morphism of algebraic spaces over `S` with
> algebraic total space is locally of finite type in the sense of Stacks 03XF.

```lean
theorem isLocallyOfFiniteType_of_section (p : P ⟶ V)
    (hP : IsAlgebraicSpace B S hS P) (s : V ⟶ P) (hs : s ≫ p = 𝟙 V) :
    IsLocallyOfFiniteType B S hS s
```

**`AlgebraicGeometry.Space.isLocallyQuasiFinite_of_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedCriteria.lean, line 394](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedCriteria.lean#L394). The attribute's comment: “part (1): locally quasi-finite”.

> **Stacks 03KP, part (1).** A section of a morphism of algebraic spaces over `S` with
> algebraic total space is locally quasi-finite in the sense of Stacks 03XJ.

```lean
theorem isLocallyQuasiFinite_of_section (p : P ⟶ V)
    (hP : IsAlgebraicSpace B S hS P) (s : V ⟶ P) (hs : s ≫ p = 𝟙 V) :
    IsLocallyQuasiFinite B S hS s
```

**`AlgebraicGeometry.Space.isImmersion_of_isLocallySeparated_of_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedCriteria.lean, line 403](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedCriteria.lean#L403). The attribute's comment: “part (2)”.

> **Stacks 03KP, part (2).** A section of a locally separated morphism of algebraic spaces
> over `S` is an immersion.

```lean
theorem isImmersion_of_isLocallySeparated_of_section (p : P ⟶ V)
    (hp : IsLocallySeparated B S hS p) (s : V ⟶ P) (hs : s ≫ p = 𝟙 V) :
    IsImmersion B S hS s
```

**`AlgebraicGeometry.Space.isClosedImmersion_of_isSeparated_of_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedCriteria.lean, line 412](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedCriteria.lean#L412). The attribute's comment: “part (3)”. References: SGA 3 VIB (5.6.3), “more general”.

> **Stacks 03KP, part (3).** A section of a separated morphism of algebraic spaces over `S`
> is a closed immersion.

```lean
theorem isClosedImmersion_of_isSeparated_of_section (p : P ⟶ V)
    (hp : IsSeparated B S hS p) (s : V ⟶ P) (hs : s ≫ p = 𝟙 V) :
    IsClosedImmersion B S hS s
```

**`AlgebraicGeometry.Space.isQuasiCompact_of_isQuasiSeparated_of_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedCriteria.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedCriteria.lean#L421). The attribute's comment: “part (4)”.

> **Stacks 03KP, part (4).** A section of a quasi-separated morphism of algebraic spaces over
> `S` is quasi-compact.

```lean
theorem isQuasiCompact_of_isQuasiSeparated_of_section (p : P ⟶ V)
    (hp : IsQuasiSeparated B S hS p) (s : V ⟶ P) (hs : s ≫ p = 𝟙 V) :
    IsQuasiCompact B S hS s
```

## Tag 03KQ, a lemma

[Tag 03KQ](https://stacks.math.columbia.edu/tag/03KQ) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiSeparated_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxioms.lean, line 86](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxioms.lean#L86). The attribute's comment: “quasi-separated”.

> The composite of two quasi-separated morphisms of algebraic spaces over `S` is
> quasi-separated.

```lean
theorem isQuasiSeparated_comp (hF : IsAlgebraicSpace B S hS F) (hG : IsAlgebraicSpace B S hS G)
    (p : F ⟶ G) (q : G ⟶ H) (hp : IsQuasiSeparated B S hS p)
    (hq : IsQuasiSeparated B S hS q) : IsQuasiSeparated B S hS (p ≫ q)
```

**`AlgebraicGeometry.Space.isSeparated_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedTfae.lean, line 1074](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedTfae.lean#L1074). The attribute's comment: “separated”.

> Separatedness of morphisms of algebraic spaces is stable under composition.

```lean
theorem isSeparated_comp {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (p : F ⟶ G) (q : G ⟶ H)
    (hp : IsSeparated B S hS p) (hq : IsSeparated B S hS q) :
    IsSeparated B S hS (p ≫ q)
```

**`AlgebraicGeometry.Space.isLocallySeparated_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedTfae.lean, line 1156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedTfae.lean#L1156). The attribute's comment: “locally separated”.

> Local separatedness of morphisms of algebraic spaces is stable under composition.

```lean
theorem isLocallySeparated_comp {F G H : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (p : F ⟶ G) (q : G ⟶ H)
    (hp : IsLocallySeparated B S hS p) (hq : IsLocallySeparated B S hS q) :
    IsLocallySeparated B S hS (p ≫ q)
```

## Tag 04ZH, a lemma

[Tag 04ZH](https://stacks.math.columbia.edu/tag/04ZH) in the Stacks Project.

**`AlgebraicGeometry.Space.isSeparatedOver_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxioms.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxioms.lean#L107). The attribute's comment: “part (4)”.

> If `G` is separated over `S` and `f : F ⟶ G` is separated,
> then `F` is separated over `S`.

```lean
theorem isSeparatedOver_of_isSeparated {f : F ⟶ G} (hG : IsSeparatedOver B S hS G)
    (hf : IsSeparated B S hS f) : IsSeparatedOver B S hS F
```

**`AlgebraicGeometry.Space.isLocallySeparatedOver_of_isLocallySeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxioms.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxioms.lean#L119). The attribute's comment: “part (6)”.

> If `G` is locally separated over `S` and `f : F ⟶ G` is
> locally separated, then `F` is locally separated over `S`.

```lean
theorem isLocallySeparatedOver_of_isLocallySeparated {f : F ⟶ G}
    (hG : IsLocallySeparatedOver B S hS G) (hf : IsLocallySeparated B S hS f) :
    IsLocallySeparatedOver B S hS F
```

**`AlgebraicGeometry.Space.isQuasiSeparatedOver_of_isQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxioms.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxioms.lean#L145). The attribute's comment: “part (5)”.

> If `G` is quasi-separated over `S` and `f : F ⟶ G` is quasi-separated, then `F` is
> quasi-separated over `S`.

```lean
theorem isQuasiSeparatedOver_of_isQuasiSeparated (hF : IsAlgebraicSpace B S hS F) {f : F ⟶ G}
    (hG : IsQuasiSeparatedOver B S hS G) (hf : IsQuasiSeparated B S hS f) :
    IsQuasiSeparatedOver B S hS F
```

**`AlgebraicGeometry.Space.isAbsolutelySeparated_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxioms.lean, line 157](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxioms.lean#L157). The attribute's comment: “part (1)”.

> If `G` is separated and `f : F ⟶ G` is separated, then `F` is separated.

```lean
theorem isAbsolutelySeparated_of_isSeparated {f : F ⟶ G}
    (hG : IsAbsolutelySeparated B S hS hZ G) (hf : IsSeparated B S hS f) :
    IsAbsolutelySeparated B S hS hZ F
```

**`AlgebraicGeometry.Space.isAbsolutelyLocallySeparated_of_isLocallySeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxioms.lean, line 166](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxioms.lean#L166). The attribute's comment: “part (3)”.

> If `G` is locally separated and `f : F ⟶ G` is locally
> separated, then `F` is locally separated.

```lean
theorem isAbsolutelyLocallySeparated_of_isLocallySeparated {f : F ⟶ G}
    (hG : IsAbsolutelyLocallySeparated B S hS hZ G) (hf : IsLocallySeparated B S hS f) :
    IsAbsolutelyLocallySeparated B S hS hZ F
```

**`AlgebraicGeometry.Space.isAbsolutelyQuasiSeparated_of_isQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxioms.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxioms.lean#L175). The attribute's comment: “part (2)”.

> If `G` is quasi-separated and `f : F ⟶ G` is quasi-separated, then `F` is
> quasi-separated.

```lean
theorem isAbsolutelyQuasiSeparated_of_isQuasiSeparated (hF : IsAlgebraicSpace B S hS F)
    {f : F ⟶ G} (hG : IsAbsolutelyQuasiSeparated B S hS hZ G)
    (hf : IsQuasiSeparated B S hS f) : IsAbsolutelyQuasiSeparated B S hS hZ F
```

## Tag 03KR, a lemma

[Tag 03KR](https://stacks.math.columbia.edu/tag/03KR) in the Stacks Project.

**`AlgebraicGeometry.Space.separationAxioms_of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparationAxiomsCancellation.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparationAxiomsCancellation.lean#L74).

> **Stacks 03KR.** Let `S` be a scheme contained in the big fppf site `B` and let
> `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of algebraic spaces over `S`. Then:
>
> 1. if `f ≫ g` is separated, so is `f`;
> 2. if `f ≫ g` is locally separated, so is `f`; and
> 3. if `f ≫ g` is quasi-separated, so is `f`.
>
> Each of the three separation axioms is a condition on the relative diagonal which is stable
> under base change, and the relative diagonal of `f` is a base change of that of `f ≫ g` along
> the comparison map `X ×_Y X ⟶ X ×_Z X`.

```lean
theorem separationAxioms_of_comp (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y) (g : Y ⟶ Z) :
    (IsSeparated B S hS (f ≫ g) → IsSeparated B S hS f) ∧
      (IsLocallySeparated B S hS (f ≫ g) → IsLocallySeparated B S hS f) ∧
      (IsQuasiSeparated B S hS (f ≫ g) → IsQuasiSeparated B S hS f)
```

## Tag 04ZI, a lemma

[Tag 04ZI](https://stacks.math.columbia.edu/tag/04ZI) in the Stacks Project.

**`AlgebraicGeometry.Space.isSeparatedOver_of_isAbsolutelySeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxioms.lean, line 186](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxioms.lean#L186). The attribute's comment: “part (1)”.

> A separated algebraic space over `S` is separated over `S`, that is, an algebraic space
> which is separated over the terminal scheme is separated over its own base scheme.

```lean
theorem isSeparatedOver_of_isAbsolutelySeparated (hF : IsAlgebraicSpace B S hS F)
    (h : IsAbsolutelySeparated B S hS hZ F) : IsSeparatedOver B S hS F
```

**`AlgebraicGeometry.Space.isLocallySeparatedOver_of_isAbsolutelyLocallySeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxioms.lean, line 197](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxioms.lean#L197). The attribute's comment: “part (2)”.

> A locally separated algebraic space is locally separated over
> its base scheme.

```lean
theorem isLocallySeparatedOver_of_isAbsolutelyLocallySeparated (hF : IsAlgebraicSpace B S hS F)
    (h : IsAbsolutelyLocallySeparated B S hS hZ F) : IsLocallySeparatedOver B S hS F
```

**`AlgebraicGeometry.Space.isQuasiSeparatedOver_of_isAbsolutelyQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxioms.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxioms.lean#L208). The attribute's comment: “part (3)”.

> A quasi-separated algebraic space is quasi-separated over its
> base scheme.

```lean
theorem isQuasiSeparatedOver_of_isAbsolutelyQuasiSeparated (hF : IsAlgebraicSpace B S hS F)
    (h : IsAbsolutelyQuasiSeparated B S hS hZ F) : IsQuasiSeparatedOver B S hS F
```

**`AlgebraicGeometry.Space.isQuasiSeparated_of_isQuasiSeparatedOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxioms.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparationAxioms.lean#L220). The attribute's comment: “part (6)”.

> Every morphism out of an algebraic space which is quasi-separated over `S` is
> quasi-separated.

```lean
theorem isQuasiSeparated_of_isQuasiSeparatedOver (hF : IsQuasiSeparatedOver B S hS F)
    (p : F ⟶ G) : IsQuasiSeparated B S hS p
```

**`AlgebraicGeometry.Space.isSeparated_of_isSeparatedOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedTfae.lean, line 1088](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedTfae.lean#L1088). The attribute's comment: “part (4)”.

> Every morphism out of an algebraic space which is separated over `S` is separated.

```lean
theorem isSeparated_of_isSeparatedOver {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsSeparatedOver B S hS F) (p : F ⟶ G) : IsSeparated B S hS p
```

**`AlgebraicGeometry.Space.isLocallySeparated_of_isLocallySeparatedOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedTfae.lean, line 1171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedTfae.lean#L1171). The attribute's comment: “part (5)”.

> Every morphism out of an algebraic space which is locally separated over `S` is locally
> separated.

```lean
theorem isLocallySeparated_of_isLocallySeparatedOver {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hF : IsLocallySeparatedOver B S hS F) (p : F ⟶ G) : IsLocallySeparated B S hS p
```

## Tag 03KM, a lemma

[Tag 03KM](https://stacks.math.columbia.edu/tag/03KM) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiSeparated_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiSeparatedTfae.lean, line 527](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/QuasiSeparatedTfae.lean#L527). The attribute's comment: “quasi-separated”.

> For a morphism `f : X ⟶ Y` of algebraic spaces over a
> scheme `S` the following six conditions are equivalent: `f` is quasi-separated; the base change of
> `f` along every morphism from a representable presheaf is quasi-separated; the same for the test
> objects with affine underlying scheme; for every affine test object the fibre product is a
> quasi-separated algebraic space, that is quasi-separated over the terminal scheme; there is a
> surjective étale scheme chart of the target along which the base change of `f` is quasi-separated;
> and there is a Zariski covering of the target over whose members the base changes of `f` are
> quasi-separated.

```lean
theorem isQuasiSeparated_tfae (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) :
    List.TFAE [
      IsQuasiSeparated B S hS f,
      (∀ (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y),
        IsQuasiSeparated B S hS (pullback.snd f g)),
      (∀ (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y),
        IsAffine ((BigFppfOver.toScheme B S hS).obj T) →
          IsQuasiSeparated B S hS (pullback.snd f g)),
      (∀ (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y),
        IsAffine ((BigFppfOver.toScheme B S hS).obj T) →
          IsAbsolutelyQuasiSeparated B S hS hZ (pullback f g)),
      (∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
        (MorphismProperty.presheaf (MorphismProperty.inverseImage
          (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS))) g ∧
        (MorphismProperty.presheaf (MorphismProperty.inverseImage
          (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS))) g ∧
        IsQuasiSeparated B S hS (pullback.snd f g)),
      (∃ (I : Type u) (U : I → Subfunctor Y),
        IsZariskiCover B S hS I U ∧
        ∀ i, IsQuasiSeparated B S hS (pullback.snd f (U i).ι))
    ]
```

**`AlgebraicGeometry.Space.isSeparated_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedTfae.lean, line 1360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedTfae.lean#L1360). The attribute's comment: “separated”.

> For a morphism `f : X ⟶ Y` of algebraic spaces over a scheme `S` the following are equivalent:
> `f` is separated; the base change of `f` along every morphism from a representable presheaf is
> separated; the same for the test objects with affine underlying scheme; for every affine test
> object the fibre product is a separated algebraic space over the terminal scheme; there is a
> surjective étale scheme chart of the target along which the base change of `f` is separated; and
> there is a Zariski covering of the target over whose members the base changes of `f` are
> separated.

```lean
theorem isSeparated_tfae (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) :
    List.TFAE [
      IsSeparated B S hS f,
      (∀ (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y),
        IsSeparated B S hS (pullback.snd f g)),
      (∀ (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y),
        IsAffine ((BigFppfOver.toScheme B S hS).obj T) →
          IsSeparated B S hS (pullback.snd f g)),
      (∀ (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y),
        IsAffine ((BigFppfOver.toScheme B S hS).obj T) →
          IsAbsolutelySeparated B S hS hZ (pullback f g)),
      (∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
        (MorphismProperty.presheaf (MorphismProperty.inverseImage
          (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS))) g ∧
        (MorphismProperty.presheaf (MorphismProperty.inverseImage
          (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS))) g ∧
        IsSeparated B S hS (pullback.snd f g)),
      (∃ (I : Type u) (U : I → Subfunctor Y),
        IsZariskiCover B S hS I U ∧
        ∀ i, IsSeparated B S hS (pullback.snd f (U i).ι))
    ]
```

**`AlgebraicGeometry.Space.isLocallySeparated_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparatedTfae.lean, line 1407](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparatedTfae.lean#L1407). The attribute's comment: “locally separated”.

> For a morphism `f : X ⟶ Y` of algebraic spaces over a scheme `S` the following are equivalent:
> `f` is locally separated; the base change of `f` along every morphism from a representable presheaf
> is locally separated; the same for the test objects with affine underlying scheme; for every affine
> test object the fibre product is a locally separated algebraic space over the terminal scheme;
> there is a surjective étale scheme chart of the target along which the base change of `f` is
> locally separated; and there is a Zariski covering of the target over whose members the base
> changes of `f` are locally separated.

```lean
theorem isLocallySeparated_tfae (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    List.TFAE [
      IsLocallySeparated B S hS f,
      (∀ (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y),
        IsLocallySeparated B S hS (pullback.snd f g)),
      (∀ (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y),
        IsAffine ((BigFppfOver.toScheme B S hS).obj T) →
          IsLocallySeparated B S hS (pullback.snd f g)),
      (∀ (T : BigFppfOver B S hS) (g : yoneda.obj T ⟶ Y),
        IsAffine ((BigFppfOver.toScheme B S hS).obj T) →
          IsAbsolutelyLocallySeparated B S hS hZ (pullback f g)),
      (∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
        (MorphismProperty.presheaf (MorphismProperty.inverseImage
          (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS))) g ∧
        (MorphismProperty.presheaf (MorphismProperty.inverseImage
          (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS))) g ∧
        IsLocallySeparated B S hS (pullback.snd f g)),
      (∃ (I : Type u) (U : I → Subfunctor Y),
        IsZariskiCover B S hS I U ∧
        ∀ i, IsLocallySeparated B S hS (pullback.snd f (U i).ι))
    ]
```

## Tag 03KY, a lemma

[Tag 03KY](https://stacks.math.columbia.edu/tag/03KY) in the Stacks Project.

**`AlgebraicGeometry.Space.separationProperties_of_relativelyRepresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RepresentableSeparationMatch.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RepresentableSeparationMatch.lean#L68).

> **Stacks 03KY.** Let `S` be a scheme and let `f : X ⟶ Y` be a representable morphism of
> algebraic spaces over `S`.  Then:
>
> 1. `f` is locally separated; and
> 2. `f` is separated in the sense of Stacks 03HL if and only if it is separated in the sense
>    of Stacks 03HA, that is, if and only if every represented base change of `f` is a
>    separated morphism of schemes, and likewise for quasi-separatedness.
>
> In particular, a morphism `m` of schemes over `S` is (quasi-)separated in the sense of
> Stacks 03HL, as the morphism of algebraic spaces `yoneda.map m`, if and only if it is
> (quasi-)separated as a morphism of schemes.
>
> Part (1) holds because the relative diagonal of a morphism of schemes is an immersion, by
> Stacks 01KJ, and local separatedness of a morphism with algebraic source is tested on its
> represented base changes, by Stacks 03KM, each of which is the Yoneda image of a morphism of
> the site.  Part (2) is the equivalence of conditions (1) and (2) of Stacks 03KM for
> separatedness and for quasi-separatedness, taken together with the fact that separatedness
> and quasi-separatedness of the Yoneda image of a morphism of the site are those properties of
> the underlying morphism of schemes; that last fact, stated for every morphism of the site, is
> also the concluding assertion.

```lean
theorem separationProperties_of_relativelyRepresentable
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y) (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (hf : yoneda.relativelyRepresentable f) :
    IsLocallySeparated B S hS f ∧
      (IsSeparated B S hS f ↔
          (MorphismProperty.presheaf (MorphismProperty.inverseImage
            (@_root_.AlgebraicGeometry.IsSeparated.{u} : MorphismProperty Scheme.{u})
            (BigFppfOver.toScheme B S hS))) f) ∧
      (IsQuasiSeparated B S hS f ↔
          (MorphismProperty.presheaf (MorphismProperty.inverseImage
            (@_root_.AlgebraicGeometry.QuasiSeparated.{u} : MorphismProperty Scheme.{u})
            (BigFppfOver.toScheme B S hS))) f) ∧
      ∀ (a b : BigFppfOver B S hS) (m : a ⟶ b),
        (IsSeparated B S hS (yoneda.map m) ↔
            _root_.AlgebraicGeometry.IsSeparated ((BigFppfOver.toScheme B S hS).map m)) ∧
          (IsQuasiSeparated B S hS (yoneda.map m) ↔
            _root_.AlgebraicGeometry.QuasiSeparated ((BigFppfOver.toScheme B S hS).map m))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.4, Tag 03HJ](https://stacks.math.columbia.edu/tag/03HJ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
