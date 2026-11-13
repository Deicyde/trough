---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.HasQuasiCompactDiagonal, AlgebraicGeometry.FormalSpace.IsSeparatedMorphism, AlgebraicGeometry.FormalSpace.HasQuasiCompactDiagonal.of_isPullback, AlgebraicGeometry.FormalSpace.isSeparatedMorphism_of_isPullback, AlgebraicGeometry.FormalSpace.isQuasiCompact_mapDesc, AlgebraicGeometry.FormalSpace.isSeparatedMorphism_mapDesc, AlgebraicGeometry.FormalSpace.relativelyRepresentable_mapDesc_of_isAffineFormal, AlgebraicGeometry.FormalSpace.relative_locallyQuasiFinite_mapDesc_of_isAffineFormal
statement: formalized
proof: formalized
---

# 87.30 Separation axioms for morphisms

Section 87.30 of the Stacks Project, [Tag 0ARM](https://stacks.math.columbia.edu/tag/0ARM). 5 tags here are carried by 47 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0ARN, a definition

[Tag 0ARN](https://stacks.math.columbia.edu/tag/0ARN) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.HasQuasiCompactDiagonal`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphism.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphism.lean#L112). The attribute's comment: “part (2): quasi-separated, the relative diagonal quasi-compact in the sense of Stacks 0AJC”.

> **Stacks 0ARN, part (2).** A morphism of formal algebraic spaces over `S` is
> *quasi-separated* when its relative diagonal `X ⟶ X ×_Y X` is a quasi-compact morphism of
> formal algebraic spaces, quasi-compactness being `AlgebraicGeometry.FormalSpace.IsQuasiCompact`,
> the condition of Stacks 0AJC. The condition makes sense, and is stated, for an arbitrary
> morphism of fppf sheaves on the big fppf site of `S`.

```lean
abbrev HasQuasiCompactDiagonal {X Y : FppfSheaf B S hS} (f : X ⟶ Y) : Prop
```

**`AlgebraicGeometry.FormalSpace.IsSeparatedMorphism`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L113). The attribute's comment: “part (1): separated”. References: EGA I (10.15.1), “separated morphism”.

> A morphism of formal algebraic spaces over `S` is *separated* when its relative diagonal
> is a closed immersion, stated for an arbitrary morphism of fppf sheaves on the big fppf site
> of `S`.

```lean
abbrev IsSeparatedMorphism {X Y : FppfSheaf B S hS} (f : X ⟶ Y) : Prop
```

## Tag 0ARP, a lemma

[Tag 0ARP](https://stacks.math.columbia.edu/tag/0ARP) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.HasQuasiCompactDiagonal.of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphism.lean, line 134](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphism.lean#L134). The attribute's comment: “quasi-separated”.

> **Stacks 0ARP** for the quasi-separatedness axiom of Stacks 0ARN: a base change of a
> quasi-separated morphism of formal algebraic spaces over `S` is quasi-separated. In a
> cartesian square of fppf sheaves on the big fppf site of `S` whose right-hand column `f` is
> quasi-separated, the left-hand column `snd` is quasi-separated, since the relative diagonal of
> `snd` is a base change of the relative diagonal of `f` and quasi-compact morphisms are stable
> under base change. As with the definition itself, no hypothesis that the four sheaves are
> formal algebraic spaces is needed.

```lean
theorem HasQuasiCompactDiagonal.of_isPullback {X Y Y' W : FppfSheaf B S hS}
    {fst : W ⟶ X} {snd : W ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y} (sq : IsPullback fst snd f g)
    (hf : HasQuasiCompactDiagonal B S hS f) : HasQuasiCompactDiagonal B S hS snd
```

**`AlgebraicGeometry.FormalSpace.isSeparatedMorphism_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L139). The attribute's comment: “separated”.

> A base change of a separated morphism of formal algebraic spaces over `S` is separated: in a
> cartesian square of fppf sheaves on the big fppf site of `S` whose right-hand column `f` is
> separated, the left-hand column `snd` is separated.

```lean
theorem isSeparatedMorphism_of_isPullback {X Y Y' W : FppfSheaf B S hS}
    {fst : W ⟶ X} {snd : W ⟶ Y'} {f : X ⟶ Y} {g : Y' ⟶ Y} (sq : IsPullback fst snd f g)
    (hf : IsSeparatedMorphism B S hS f) : IsSeparatedMorphism B S hS snd
```

## Tag 0ARQ, a lemma

[Tag 0ARQ](https://stacks.math.columbia.edu/tag/0ARQ) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isQuasiCompact_mapDesc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphism.lean, line 163](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphism.lean#L163). The attribute's comment: “part (3), for Z ⟶ T quasi-separated. Both notions are the source's own: the hypothesis is quasi-separatedness as Stacks 0ARN, part (2) declares it, the relative diagonal quasi-compact in the sense of Stacks 0AJC (HasQuasiCompactDiagonal of this file), and the conclusion is quasi-compactness of a morphism of formal algebraic spaces in that same sense of Stacks 0AJC (IsQuasiCompact of QuasiCompactMorphism.lean). Nothing is carried and nothing is assumed beyond the tag's own hypothesis on Z ⟶ T; in particular this is independent of Stacks 0AN2 and of Stacks 0AIP, which parts (1) and (2) of the tag need. Parts (1) and (2) are registered in SeparatedMorphism.lean”.

> **Stacks 0ARQ, part (3).** For morphisms `f : X ⟶ Z`, `g : Y ⟶ Z` and `h : Z ⟶ T` of
> formal algebraic spaces over `S` with `h` quasi-separated, the comparison
> `X ×_Z Y ⟶ X ×_T Y` of the two fibre products is a quasi-compact morphism of formal algebraic
> spaces.
>
> The whole content is one cartesian square, the *magic diagram* of Mathlib's
> `CategoryTheory.Limits.pullback_map_diagonal_isPullback`: the comparison is a base change of
> the relative diagonal of `h`, along the morphism `X ×_T Y ⟶ Z ×_T Z` induced by `f` and `g`.
> Quasi-separatedness of `h` says that relative diagonal is quasi-compact, and quasi-compactness
> is stable under base change by
> `AlgebraicGeometry.FormalSpace.IsQuasiCompact.of_isPullback`. No hypothesis on `f`, `g` or the
> four sheaves is needed, so the statement is made for arbitrary fppf sheaves, as both conditions
> occurring in it are.

```lean
theorem isQuasiCompact_mapDesc {X Y Z T : FppfSheaf B S hS} (f : X ⟶ Z) (g : Y ⟶ Z)
    (h : Z ⟶ T) (hh : HasQuasiCompactDiagonal B S hS h) :
    IsQuasiCompact B S hS (pullback.mapDesc f g h)
```

**`AlgebraicGeometry.FormalSpace.isSeparatedMorphism_mapDesc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 1345](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L1345). The attribute's comment: “part (1): separated, separatedness read in the sense of Stacks 0ARN”.

> The comparison `X ×_Z Y ⟶ X ×_T Y` of two fibre products of fppf sheaves on the big fppf
> site of `S` is separated in the sense of Stacks 0ARN.

```lean
theorem isSeparatedMorphism_mapDesc (f : X ⟶ Z) (g : Y ⟶ Z) (h : Z ⟶ T) :
    IsSeparatedMorphism B S hS (pullback.mapDesc f g h)
```

**`AlgebraicGeometry.FormalSpace.relativelyRepresentable_mapDesc_of_isAffineFormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 1378](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L1378). The attribute's comment: “part (1): representable by schemes, unconditionally for Z an affine formal algebraic space”.

> When `Z` is an *affine* formal algebraic space, the comparison `X ×_Z Y ⟶ X ×_T Y` is
> representable by schemes.

```lean
theorem relativelyRepresentable_mapDesc_of_isAffineFormal (f : X ⟶ Z) (g : Y ⟶ Z) (h : Z ⟶ T)
    (hZ : IsAffineFormalAlgebraicSpace B S hS Z) :
    (fppfYoneda B S hS).relativelyRepresentable (pullback.mapDesc f g h)
```

**`AlgebraicGeometry.FormalSpace.relative_locallyQuasiFinite_mapDesc_of_isAffineFormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 1389](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L1389). The attribute's comment: “part (1): locally quasi-finite, unconditionally for Z an affine formal algebraic space”.

> When `Z` is an *affine* formal algebraic space, every represented base change of the
> comparison `X ×_Z Y ⟶ X ×_T Y` is a locally quasi-finite, locally of finite type morphism of
> schemes.

```lean
theorem relative_locallyQuasiFinite_mapDesc_of_isAffineFormal (f : X ⟶ Z) (g : Y ⟶ Z)
    (h : Z ⟶ T) (hZ : IsAffineFormalAlgebraicSpace B S hS Z) :
    (MorphismProperty.inverseImage
      ((@AlgebraicGeometry.LocallyOfFiniteType.{u} : MorphismProperty Scheme.{u}) ⊓
        (@AlgebraicGeometry.LocallyQuasiFinite.{u} : MorphismProperty Scheme.{u}))
      (BigFppfOver.toScheme B S hS)).relative (fppfYoneda B S hS)
      (pullback.mapDesc f g h)
```

**`AlgebraicGeometry.FormalSpace.relative_locallyOfFiniteType_mapDesc_of_isAffineFormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 1403](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L1403). The attribute's comment: “part (1): locally of finite type, unconditionally for Z an affine formal algebraic space”.

> When `Z` is an *affine* formal algebraic space, every represented base change of the
> comparison `X ×_Z Y ⟶ X ×_T Y` is a locally of finite type morphism of schemes.

```lean
theorem relative_locallyOfFiniteType_mapDesc_of_isAffineFormal (f : X ⟶ Z) (g : Y ⟶ Z)
    (h : Z ⟶ T) (hZ : IsAffineFormalAlgebraicSpace B S hS Z) :
    (MorphismProperty.inverseImage
      (@AlgebraicGeometry.LocallyOfFiniteType.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).relative (fppfYoneda B S hS)
      (pullback.mapDesc f g h)
```

**`AlgebraicGeometry.FormalSpace.relative_isSeparated_mapDesc_of_isAffineFormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 1416](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L1416). The attribute's comment: “part (1): separated in the represented-base-change sense of Stacks 0AN2, unconditionally for Z an affine formal algebraic space”.

> When `Z` is an *affine* formal algebraic space, every represented base change of the
> comparison `X ×_Z Y ⟶ X ×_T Y` is a separated morphism of schemes.

```lean
theorem relative_isSeparated_mapDesc_of_isAffineFormal (f : X ⟶ Z) (g : Y ⟶ Z) (h : Z ⟶ T)
    (hZ : IsAffineFormalAlgebraicSpace B S hS Z) :
    (MorphismProperty.inverseImage
      (@AlgebraicGeometry.IsSeparated.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).relative (fppfYoneda B S hS)
      (pullback.mapDesc f g h)
```

**`AlgebraicGeometry.FormalSpace.relativelyRepresentable_mapDesc_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 1427](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L1427). The attribute's comment: “part (1): representable by schemes, for Z an arbitrary formal algebraic space”.

> When `Z` is a formal algebraic space, the comparison `X ×_Z Y ⟶ X ×_T Y` is representable
> by schemes.

```lean
theorem relativelyRepresentable_mapDesc_of_isFormalAlgebraicSpace (f : X ⟶ Z) (g : Y ⟶ Z)
    (h : Z ⟶ T) (hZ : IsFormalAlgebraicSpace B S hS Z) :
    (fppfYoneda B S hS).relativelyRepresentable (pullback.mapDesc f g h)
```

**`AlgebraicGeometry.FormalSpace.relative_locallyQuasiFinite_mapDesc_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 1436](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L1436). The attribute's comment: “part (1): locally quasi-finite, for Z an arbitrary formal algebraic space”.

> When `Z` is a formal algebraic space, every represented base change of the comparison
> `X ×_Z Y ⟶ X ×_T Y` is a locally quasi-finite, locally of finite type morphism of schemes.

```lean
theorem relative_locallyQuasiFinite_mapDesc_of_isFormalAlgebraicSpace (f : X ⟶ Z) (g : Y ⟶ Z)
    (h : Z ⟶ T) (hZ : IsFormalAlgebraicSpace B S hS Z) :
    (MorphismProperty.inverseImage
      ((@AlgebraicGeometry.LocallyOfFiniteType.{u} : MorphismProperty Scheme.{u}) ⊓
        (@AlgebraicGeometry.LocallyQuasiFinite.{u} : MorphismProperty Scheme.{u}))
      (BigFppfOver.toScheme B S hS)).relative (fppfYoneda B S hS)
      (pullback.mapDesc f g h)
```

**`AlgebraicGeometry.FormalSpace.relative_locallyOfFiniteType_mapDesc_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 1449](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L1449). The attribute's comment: “part (1): locally of finite type, for Z an arbitrary formal algebraic space”.

> When `Z` is a formal algebraic space, every represented base change of the comparison
> `X ×_Z Y ⟶ X ×_T Y` is a locally of finite type morphism of schemes.

```lean
theorem relative_locallyOfFiniteType_mapDesc_of_isFormalAlgebraicSpace (f : X ⟶ Z) (g : Y ⟶ Z)
    (h : Z ⟶ T) (hZ : IsFormalAlgebraicSpace B S hS Z) :
    (MorphismProperty.inverseImage
      (@AlgebraicGeometry.LocallyOfFiniteType.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).relative (fppfYoneda B S hS)
      (pullback.mapDesc f g h)
```

**`AlgebraicGeometry.FormalSpace.relative_isSeparated_mapDesc_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 1462](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L1462). The attribute's comment: “part (1): separated in the represented-base-change sense of Stacks 0AN2, for Z an arbitrary formal algebraic space”.

> When `Z` is a formal algebraic space, every represented base change of the comparison
> `X ×_Z Y ⟶ X ×_T Y` is a separated morphism of schemes.

```lean
theorem relative_isSeparated_mapDesc_of_isFormalAlgebraicSpace (f : X ⟶ Z) (g : Y ⟶ Z)
    (h : Z ⟶ T) (hZ : IsFormalAlgebraicSpace B S hS Z) :
    (MorphismProperty.inverseImage
      (@AlgebraicGeometry.IsSeparated.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).relative (fppfYoneda B S hS)
      (pullback.mapDesc f g h)
```

**`AlgebraicGeometry.FormalSpace.isClosedImmersion_mapDesc`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 1474](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L1474). The attribute's comment: “part (2), for Z ⟶ T separated”.

> If `h : Z ⟶ T` is separated then the comparison `X ×_Z Y ⟶ X ×_T Y` is a closed
> immersion.

```lean
theorem isClosedImmersion_mapDesc (f : X ⟶ Z) (g : Y ⟶ Z) (h : Z ⟶ T)
    (hh : IsSeparatedMorphism B S hS h) :
    IsClosedImmersion B S hS (pullback.mapDesc f g h)
```

Declarations registered for the tag:

- [`CategoryTheory.Limits.pullback.mono_mapDesc`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/MapDescent.lean#L60), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 1502](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L1502) (StacksFrontier): “part (1): monomorphism”.

## Tag 0ARR, a lemma

[Tag 0ARR](https://stacks.math.columbia.edu/tag/0ARR) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isQuasiSeparatedMorphism_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComposition.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComposition.lean#L195). The attribute's comment: “part (2): quasi-separated, with quasi-compactness of the relative diagonal read as the condition AlgebraicGeometry.Space.IsQuasiCompactULift that this library's AlgebraicGeometry.FormalSpace.IsQuasiSeparatedMorphism is built from; the comparison of the two relative self-products is quasi-compact by Stacks 0ARQ, part (3), and that condition is stable under composition over formal algebraic spaces by AlgebraicGeometry.Space.isQuasiCompactULift\_comp\_of\_presheaf”.

> **Stacks 0ARR for the quasi-separatedness axiom of Stacks 0ARN.** A composite of two
> morphisms of fppf sheaves on the big fppf site of `S` with quasi-compact relative diagonal
> again has quasi-compact relative diagonal: the relative diagonal of `f ≫ g` factors as the
> relative diagonal of `f`, quasi-compact since `f` is quasi-separated, followed by the
> comparison `X ×_Y X ⟶ X ×_Z X`, quasi-compact since `g` is quasi-separated by Stacks 0ARQ,
> part (3); and the quasi-compactness condition is stable under composition with no hypothesis
> that the objects are algebraic spaces.
>
> Quasi-compactness is read throughout as `AlgebraicGeometry.Space.IsQuasiCompactULift`, the
> condition `AlgebraicGeometry.FormalSpace.IsQuasiSeparatedMorphism` is built from. As with the
> definition, no hypothesis that the three sheaves are formal algebraic spaces is needed.

```lean
theorem isQuasiSeparatedMorphism_comp {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : IsQuasiSeparatedMorphism B S hS f) (hg : IsQuasiSeparatedMorphism B S hS g) :
    IsQuasiSeparatedMorphism B S hS (f ≫ g)
```

**`AlgebraicGeometry.FormalSpace.isSeparatedMorphism_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphismComposition.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphismComposition.lean#L122). The attribute's comment: “part (1): separated, separatedness read in the sense of Stacks 0ARN; the comparison of the two relative self-products is a closed immersion by Stacks 0ARQ, part (2), and closed immersions compose by Stacks 0GHW”.

> **Stacks 0ARR for the separatedness axiom of Stacks 0ARN.** A composite of two separated
> morphisms of fppf sheaves on the big fppf site of `S` is separated: the relative diagonal of
> `f ≫ g` factors as the relative diagonal of `f`, a closed immersion since `f` is separated,
> followed by the comparison `X ×_Y X ⟶ X ×_Z X`, a closed immersion since `g` is separated by
> Stacks 0ARQ, part (2); and closed immersions of formal algebraic spaces compose by
> Stacks 0GHW.

```lean
theorem isSeparatedMorphism_comp {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : IsSeparatedMorphism B S hS f) (hg : IsSeparatedMorphism B S hS g) :
    IsSeparatedMorphism B S hS (f ≫ g)
```

**`AlgebraicGeometry.FormalSpace.hasRelativeDiagonal_quasiCompact_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphismComposition.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphismComposition.lean#L139). The attribute's comment: “part (2): quasi-separated, with quasi-compactness of the relative diagonal read as the relative diagonal condition for quasi-compact morphisms of schemes, which is the second of the two cases of Stacks 0ARN in the uniform shape of Stacks 0ARS; stability under composition of quasi-compact morphisms of schemes is taken from Mathlib”.

> **Stacks 0ARR for the quasi-separatedness axiom of Stacks 0ARN**, with quasi-compactness of
> the relative diagonal read as the relative diagonal condition for quasi-compact morphisms of
> schemes: if the relative diagonals of `f` and of `g` are quasi-compact in that sense, then so
> is the relative diagonal of `f ≫ g`. Quasi-compact morphisms of schemes are stable under
> composition, so this is the case `P = AlgebraicGeometry.QuasiCompact` of
> `AlgebraicGeometry.FormalSpace.hasRelativeDiagonal_comp`.

```lean
theorem hasRelativeDiagonal_quasiCompact_comp {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y)
    (g : Y ⟶ Z)
    (hf : HasRelativeDiagonal B S hS
      (@AlgebraicGeometry.QuasiCompact.{u} : MorphismProperty Scheme.{u}) f)
    (hg : HasRelativeDiagonal B S hS
      (@AlgebraicGeometry.QuasiCompact.{u} : MorphismProperty Scheme.{u}) g) :
    HasRelativeDiagonal B S hS
      (@AlgebraicGeometry.QuasiCompact.{u} : MorphismProperty Scheme.{u}) (f ≫ g)
```

## Tag 0ARS, a lemma

[Tag 0ARS](https://stacks.math.columbia.edu/tag/0ARS) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.hasQuasiCompactDiagonal_iff_forall_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComparison.lean, line 328](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComparison.lean#L328). The attribute's comment: “clauses (1) and (2) for the quasi-separated axiom of Stacks 0ARN: a morphism of formal algebraic spaces with relatively representable relative diagonal is quasi-separated if and only if its base change to every scheme over the target is quasi-separated; the representability hypothesis is discharged for a source which is a formal algebraic space in `…hasQuasiCompactDiagonal_iff_forall_baseChange_of_isFormalAlgebraicSpace`”.

> **Stacks 0ARS, clauses (1) and (2) for the quasi-separatedness axiom of Stacks 0ARN.** A
> morphism `f : X ⟶ Y` of fppf sheaves on the big fppf site of `S` whose relative diagonal is
> representable by objects of the site is quasi-separated exactly when its base change to every
> scheme over the target is quasi-separated.
>
> The hypothesis `hf` is carried: unlike the separatedness axiom, whose spelling in this library
> contains representability of the relative diagonal, the quasi-separatedness axiom does not, and
> the comparison with the relative diagonal condition of
> `AlgebraicGeometry.FormalSpace.HasRelativeDiagonal` needs it. It is discharged for a source
> which is a formal algebraic space — the hypothesis of Stacks 0ARS itself — in
> `…hasQuasiCompactDiagonal_iff_forall_baseChange_of_isFormalAlgebraicSpace`
> below.

```lean
theorem hasQuasiCompactDiagonal_iff_forall_baseChange {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hf : (fppfYoneda B S hS).relativelyRepresentable (pullback.diagonal f)) :
    HasQuasiCompactDiagonal B S hS f ↔
      ∀ (U : BigFppfOver B S hS) (g : (fppfYoneda B S hS).obj U ⟶ Y),
        HasQuasiCompactDiagonal B S hS (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.hasQuasiCompactDiagonal_iff_forall_baseChange_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComparison.lean, line 354](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComparison.lean#L354). The attribute's comment: “clauses (1) and (2) for the quasi-separated axiom of Stacks 0ARN, in the source's form with no extra hypothesis: a morphism of formal algebraic spaces is quasi-separated if and only if its base change to every scheme over the target is quasi-separated”.

> **Stacks 0ARS, clauses (1) and (2) for the quasi-separatedness axiom of Stacks 0ARN**, in
> the source's own form: a morphism `f : X ⟶ Y` of fppf sheaves on the big fppf site of `S` whose
> source is a formal algebraic space is quasi-separated exactly when its base change to every
> scheme over the target is quasi-separated. The representability hypothesis of
> `AlgebraicGeometry.FormalSpace.hasQuasiCompactDiagonal_iff_forall_baseChange` is discharged
> here: the relative diagonal of `f` is a base change of the absolute diagonal of `X`, which is
> representable by objects of the site by **Stacks 0AIP**.

```lean
theorem hasQuasiCompactDiagonal_iff_forall_baseChange_of_isFormalAlgebraicSpace
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y) (hX : IsFormalAlgebraicSpace B S hS X) :
    HasQuasiCompactDiagonal B S hS f ↔
      ∀ (U : BigFppfOver B S hS) (g : (fppfYoneda B S hS).obj U ⟶ Y),
        HasQuasiCompactDiagonal B S hS (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.hasQuasiCompactDiagonal_iff_forall_affine_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComparison.lean, line 381](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComparison.lean#L381). The attribute's comment: “clauses (1) and (3) for the quasi-separated axiom of Stacks 0ARN: a morphism of formal algebraic spaces with relatively representable relative diagonal is quasi-separated if and only if its base change to every affine scheme over the target is quasi-separated; the representability hypothesis is discharged for a source which is a formal algebraic space in `…hasQuasiCompactDiagonal_iff_forall_affine_baseChange_of_isFormalAlgebraicSpace`”.

> **Stacks 0ARS, clauses (1) and (3) for the quasi-separatedness axiom of Stacks 0ARN.** A
> morphism `f : X ⟶ Y` of fppf sheaves on the big fppf site of `S` whose relative diagonal is
> representable by objects of the site is quasi-separated exactly when its base change to every
> *affine* scheme over the target is quasi-separated. Quasi-compactness of morphisms of schemes
> is Zariski local on the target, which is what lets the test objects be restricted to the affine
> ones.
>
> As in clauses (1) and (2), the hypothesis `hf` is carried, and is discharged for a source which
> is a formal algebraic space in
> `…hasQuasiCompactDiagonal_iff_forall_affine_baseChange_of_isFormalAlgebraicSpace`
> below.

```lean
theorem hasQuasiCompactDiagonal_iff_forall_affine_baseChange {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) (hf : (fppfYoneda B S hS).relativelyRepresentable (pullback.diagonal f)) :
    HasQuasiCompactDiagonal B S hS f ↔
      ∀ (U : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj U) →
        ∀ (g : (fppfYoneda B S hS).obj U ⟶ Y),
          HasQuasiCompactDiagonal B S hS (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.hasQuasiCompactDiagonal_iff_forall_affine_baseChange_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComparison.lean, line 405](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComparison.lean#L405). The attribute's comment: “clauses (1) and (3) for the quasi-separated axiom of Stacks 0ARN, in the source's form with no extra hypothesis: a morphism of formal algebraic spaces is quasi-separated if and only if its base change to every affine scheme over the target is quasi-separated”.

> **Stacks 0ARS, clauses (1) and (3) for the quasi-separatedness axiom of Stacks 0ARN**, in
> the source's own form: a morphism `f : X ⟶ Y` of fppf sheaves on the big fppf site of `S` whose
> source is a formal algebraic space is quasi-separated exactly when its base change to every
> affine scheme over the target is quasi-separated. The representability hypothesis of
> `AlgebraicGeometry.FormalSpace.hasQuasiCompactDiagonal_iff_forall_affine_baseChange` is
> discharged by **Stacks 0AIP** and **Stacks 0AN2** as before.

```lean
theorem hasQuasiCompactDiagonal_iff_forall_affine_baseChange_of_isFormalAlgebraicSpace
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y) (hX : IsFormalAlgebraicSpace B S hS X) :
    HasQuasiCompactDiagonal B S hS f ↔
      ∀ (U : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj U) →
        ∀ (g : (fppfYoneda B S hS).obj U ⟶ Y),
          HasQuasiCompactDiagonal B S hS (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.hasQuasiCompactDiagonal_iff_isQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComparison.lean, line 436](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComparison.lean#L436). The attribute's comment: “clauses (3) and (4) for the quasi-separated axiom of Stacks 0ARN: a morphism of formal algebraic spaces to an affine scheme with relatively representable relative diagonal is quasi-separated if and only if its source is a quasi-separated formal algebraic space; the representability hypothesis is discharged for a source which is a formal algebraic space in `…hasQuasiCompactDiagonal_iff_isQuasiSeparated_of_isFormalAlgebraicSpace`”.

> **Stacks 0ARS, clauses (3) and (4) for the quasi-separatedness axiom of Stacks 0ARN.** A
> morphism `f : X ⟶ Z` of fppf sheaves on the big fppf site of `S` whose target is represented by
> an affine scheme of the site and whose relative diagonal is representable by objects of the
> site is quasi-separated exactly when the source `X` is quasi-separated as a single sheaf, in the
> sense of clause (1) of Stacks 0AJ7 — that is, clause (3) of Stacks 0AJ5: the fibre product over
> `X` of any two affine scheme-valued points of `X` has quasi-compact underlying scheme.
>
> Both directions are the argument of the source read through the comparison of the two fibre
> product descriptions
> `U ×_X V = X ×_{Δ, X ×_Z X} (U ×_Z V)`, which is
> `AlgebraicGeometry.FormalSpace.pair_diagonal_square` in one direction and
> `AlgebraicGeometry.FormalSpace.diagonal_test_pair_square` in the other. The scheme-level inputs
> are that a quasi-compact morphism into a quasi-compact scheme has quasi-compact source, and
> conversely that a morphism from a quasi-compact scheme to an affine one is quasi-compact.

```lean
theorem hasQuasiCompactDiagonal_iff_isQuasiSeparated {X : FppfSheaf B S hS}
    {Z : BigFppfOver B S hS} (hZ : IsAffine ((BigFppfOver.toScheme B S hS).obj Z))
    (f : X ⟶ (fppfYoneda B S hS).obj Z)
    (hf : (fppfYoneda B S hS).relativelyRepresentable (pullback.diagonal f)) :
    HasQuasiCompactDiagonal B S hS f ↔ IsQuasiSeparated B S hS X
```

**`AlgebraicGeometry.FormalSpace.hasQuasiCompactDiagonal_iff_isQuasiSeparated_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComparison.lean, line 487](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComparison.lean#L487). The attribute's comment: “clauses (3) and (4) for the quasi-separated axiom of Stacks 0ARN, in the source's form with no extra hypothesis: a morphism from a formal algebraic space to an affine scheme is quasi-separated if and only if its source is a quasi-separated formal algebraic space”.

> **Stacks 0ARS, clauses (3) and (4) for the quasi-separatedness axiom of Stacks 0ARN**, in
> the source's own form: a morphism from a formal algebraic space to a sheaf represented by an
> affine scheme of the site is quasi-separated exactly when its source is a quasi-separated
> formal algebraic space, quasi-separatedness of a single sheaf being read as clause (1) of
> Stacks 0AJ7. The representability hypothesis of
> `AlgebraicGeometry.FormalSpace.hasQuasiCompactDiagonal_iff_isQuasiSeparated` is discharged by
> **Stacks 0AIP** and **Stacks 0AN2**.

```lean
theorem hasQuasiCompactDiagonal_iff_isQuasiSeparated_of_isFormalAlgebraicSpace
    {X : FppfSheaf B S hS} {Z : BigFppfOver B S hS}
    (hZ : IsAffine ((BigFppfOver.toScheme B S hS).obj Z))
    (f : X ⟶ (fppfYoneda B S hS).obj Z) (hX : IsFormalAlgebraicSpace B S hS X) :
    HasQuasiCompactDiagonal B S hS f ↔ IsQuasiSeparated B S hS X
```

**`AlgebraicGeometry.FormalSpace.hasQuasiCompactDiagonal_of_locallySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComparison.lean, line 507](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComparison.lean#L507). The attribute's comment: “the descent step of clause (5) for the quasi-separated axiom of Stacks 0ARN: quasi-separatedness descends along a single locally surjective morphism onto the relative self-product, which is the atlas clause with the covering of Definition 0AIM replaced by one locally surjective morphism, and is not the atlas form itself”.

> **Stacks 0ARS, the descent step of clause (5) for the quasi-separatedness axiom of
> Stacks 0ARN.** Quasi-separatedness of a morphism of fppf sheaves whose relative diagonal is
> relatively representable descends along a locally surjective morphism onto the relative
> self-product. Quasi-compactness of morphisms of schemes is fppf local on the target by
> **Stacks 02WH**, which is what the descent step consumes.

```lean
theorem hasQuasiCompactDiagonal_of_locallySurjective {X Y W : FppfSheaf B S hS} (f : X ⟶ Y)
    (b : W ⟶ pullback f f) (hb : Sheaf.IsLocallySurjective b)
    (hrep : (fppfYoneda B S hS).relativelyRepresentable (pullback.diagonal f))
    (hbase : (MorphismProperty.inverseImage (@AlgebraicGeometry.QuasiCompact.{u})
      (BigFppfOver.toScheme B S hS)).relative (fppfYoneda B S hS)
      (pullback.snd (pullback.diagonal f) b)) :
    HasQuasiCompactDiagonal B S hS f
```

**`AlgebraicGeometry.FormalSpace.exists_atlas_hasQuasiCompactDiagonal_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComparison.lean, line 529](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComparison.lean#L529). The attribute's comment: “clause (5) in the covering form of Definition 0AIM, necessity for the quasi-separated axiom of Stacks 0ARN: a quasi-separated morphism of formal algebraic spaces has quasi-separated base change to every member of some covering of the target as in Definition 0AIM”.

> **Stacks 0ARS, clause (1) implies clause (5) for the quasi-separatedness axiom of
> Stacks 0ARN, in the covering form.** If `Y` is a formal algebraic space and `f : X ⟶ Y` is
> quasi-separated then there is a covering `{Y_j ⟶ Y}` as in Definition 0AIM along which every
> base change of `f` is quasi-separated. The covering is the atlas of `Y` furnished by
> Definition 0AIM; the base changes inherit the condition by **Stacks 0ARP**.

```lean
theorem exists_atlas_hasQuasiCompactDiagonal_pullback_snd {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hY : IsFormalAlgebraicSpace B S hS Y) (hf : HasQuasiCompactDiagonal B S hS f) :
    letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) := Sheaf.instHasColimitsOfSize
    ∃ (I : Type (u + 1)) (Yj : I → FppfSheaf B S hS) (g : ∀ j, Yj j ⟶ Y),
      (∀ j, IsAffineFormalAlgebraicSpace B S hS (Yj j)) ∧
      (∀ j, ∃ hgj : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS (g j).hom,
        Space.HasPropertyULift.{u + 1} B S hS
          (fun _ _ k ↦ Space.IsEtaleULift.{u + 1} B S hS k.hom) (g j).hom hgj) ∧
      Sheaf.IsLocallySurjective (Sigma.desc g) ∧
      ∀ j, HasQuasiCompactDiagonal B S hS (pullback.snd f (g j))
```

**`AlgebraicGeometry.FormalSpace.hasQuasiCompactDiagonal_of_atlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComparison.lean, line 560](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComparison.lean#L560). The attribute's comment: “clause (5) in the covering form of Definition 0AIM, sufficiency for the quasi-separated axiom of Stacks 0ARN: a morphism of formal algebraic spaces with relatively representable relative diagonal is quasi-separated as soon as its base change to every member of a covering of the target as in Definition 0AIM is quasi-separated; the representability hypothesis is discharged for a source which is a formal algebraic space in `…hasQuasiCompactDiagonal_of_atlas_of_isFormalAlgebraicSpace`”.

> **Stacks 0ARS, clause (5) implies clause (1) for the quasi-separatedness axiom of
> Stacks 0ARN, in the covering form of Definition 0AIM.** Let `f : X ⟶ Y` be a morphism of fppf
> sheaves on the big fppf site of `S` whose relative diagonal is representable by objects of the
> site. If there is a family `{Y_j ⟶ Y}` whose induced morphism from the coproduct is a surjection
> of sheaves — the covering condition of Definition 0AIM — such that every base change
> `Y_j ×_Y X ⟶ Y_j` of `f` is quasi-separated, then `f` is quasi-separated.
>
> The hypothesis `hrep` is carried, and is discharged for a source which is a formal algebraic
> space in
> `AlgebraicGeometry.FormalSpace.hasQuasiCompactDiagonal_of_atlas_of_isFormalAlgebraicSpace`
> below.

```lean
theorem hasQuasiCompactDiagonal_of_atlas {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (I : Type (u + 1)) (Yj : I → FppfSheaf B S hS) (g : ∀ j, Yj j ⟶ Y)
    (hsurj : letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) :=
        Sheaf.instHasColimitsOfSize
      Sheaf.IsLocallySurjective (Sigma.desc g))
    (hrep : (fppfYoneda B S hS).relativelyRepresentable (pullback.diagonal f))
    (hqs : ∀ j, HasQuasiCompactDiagonal B S hS (pullback.snd f (g j))) :
    HasQuasiCompactDiagonal B S hS f
```

**`AlgebraicGeometry.FormalSpace.hasQuasiCompactDiagonal_of_atlas_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComparison.lean, line 588](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComparison.lean#L588). The attribute's comment: “clause (5) in the covering form of Definition 0AIM, sufficiency for the quasi-separated axiom of Stacks 0ARN, in the source's form with no extra hypothesis: a morphism of formal algebraic spaces is quasi-separated as soon as its base change to every member of a covering of the target as in Definition 0AIM is quasi-separated”.

> **Stacks 0ARS, clause (5) implies clause (1) for the quasi-separatedness axiom of
> Stacks 0ARN**, in the covering form of Definition 0AIM and in the source's own form: a morphism
> `f : X ⟶ Y` of fppf sheaves on the big fppf site of `S` whose source is a formal algebraic space
> is quasi-separated as soon as its base change to every member of some covering of the target as
> in Definition 0AIM is. The representability hypothesis of
> `AlgebraicGeometry.FormalSpace.hasQuasiCompactDiagonal_of_atlas` is discharged by
> **Stacks 0AIP** and **Stacks 0AN2**.

```lean
theorem hasQuasiCompactDiagonal_of_atlas_of_isFormalAlgebraicSpace {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) (I : Type (u + 1)) (Yj : I → FppfSheaf B S hS) (g : ∀ j, Yj j ⟶ Y)
    (hsurj : letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) :=
        Sheaf.instHasColimitsOfSize
      Sheaf.IsLocallySurjective (Sigma.desc g))
    (hX : IsFormalAlgebraicSpace B S hS X)
    (hqs : ∀ j, HasQuasiCompactDiagonal B S hS (pullback.snd f (g j))) :
    HasQuasiCompactDiagonal B S hS f
```

**`AlgebraicGeometry.FormalSpace.separationAxiom_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComparison.lean, line 703](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/QuasiSeparatedMorphismComparison.lean#L703). The attribute's comment: “in full: the five conditions are equivalent for each of the two separation axioms of Definition 0ARN, quasi-separated and separated, for any morphism of formal algebraic spaces”.

> **Stacks 0ARS.** Let `f : X ⟶ Y` be a morphism of formal algebraic spaces over `S`. For
> each of the two separation axioms `P` of Stacks 0ARN — quasi-separated (the relative diagonal
> quasi-compact) and separated (the relative diagonal a closed immersion) — the following are
> equivalent: (1) `f` is `P`; (2) every base change `Z ×_Y X ⟶ Z` along a scheme `Z ⟶ Y` is `P`;
> (3) every such base change with `Z` affine is `P`; (4) for every affine scheme `Z ⟶ Y` the
> formal algebraic space `Z ×_Y X` is `P` in the sense of Stacks 0AJ7; (5) there is a covering
> `{Y_j ⟶ Y}` as in Definition 0AIM with every base change `Y_j ×_Y X ⟶ Y_j` being `P`.
>
> The first conjunct is `AlgebraicGeometry.FormalSpace.hasQuasiCompactDiagonal_tfae`, the second
> `AlgebraicGeometry.FormalSpace.isSeparatedMorphism_tfae`.

```lean
theorem separationAxiom_tfae {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsFormalAlgebraicSpace B S hS X) (hY : IsFormalAlgebraicSpace B S hS Y) :
    letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) := Sheaf.instHasColimitsOfSize
    List.TFAE
      [HasQuasiCompactDiagonal B S hS f,
        ∀ (Z : BigFppfOver B S hS) (g : (fppfYoneda B S hS).obj Z ⟶ Y),
          HasQuasiCompactDiagonal B S hS (pullback.snd f g),
        ∀ (Z : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
          ∀ (g : (fppfYoneda B S hS).obj Z ⟶ Y),
            HasQuasiCompactDiagonal B S hS (pullback.snd f g),
        ∀ (Z : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
          ∀ (g : (fppfYoneda B S hS).obj Z ⟶ Y), IsQuasiSeparated B S hS (pullback f g),
        ∃ (I : Type (u + 1)) (Yj : I → FppfSheaf B S hS) (g : ∀ j, Yj j ⟶ Y),
          (∀ j, IsAffineFormalAlgebraicSpace B S hS (Yj j)) ∧
          (∀ j, ∃ hgj : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS (g j).hom,
            Space.HasPropertyULift.{u + 1} B S hS
              (fun _ _ k ↦ Space.IsEtaleULift.{u + 1} B S hS k.hom) (g j).hom hgj) ∧
          Sheaf.IsLocallySurjective (Sigma.desc g) ∧
          ∀ j, HasQuasiCompactDiagonal B S hS (pullback.snd f (g j))] ∧
    List.TFAE
      [IsSeparatedMorphism B S hS f,
        ∀ (Z : BigFppfOver B S hS) (g : (fppfYoneda B S hS).obj Z ⟶ Y),
          IsSeparatedMorphism B S hS (pullback.snd f g),
        ∀ (Z : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
          ∀ (g : (fppfYoneda B S hS).obj Z ⟶ Y),
            IsSeparatedMorphism B S hS (pullback.snd f g),
        ∀ (Z : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj Z) →
          ∀ (g : (fppfYoneda B S hS).obj Z ⟶ Y), IsSeparated B S hS (pullback f g),
        ∃ (I : Type (u + 1)) (Yj : I → FppfSheaf B S hS) (g : ∀ j, Yj j ⟶ Y),
          (∀ j, IsAffineFormalAlgebraicSpace B S hS (Yj j)) ∧
          (∀ j, ∃ hgj : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS (g j).hom,
            Space.HasPropertyULift.{u + 1} B S hS
              (fun _ _ k ↦ Space.IsEtaleULift.{u + 1} B S hS k.hom) (g j).hom hgj) ∧
          Sheaf.IsLocallySurjective (Sigma.desc g) ∧
          ∀ j, IsSeparatedMorphism B S hS (pullback.snd f (g j))]
```

**`AlgebraicGeometry.FormalSpace.hasRelativeDiagonal_iff_forall_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 632](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L632). The attribute's comment: “clauses (1) and (2): a relative diagonal condition holds for a morphism of formal algebraic spaces if and only if it holds for its base change to every scheme over the target”.

> A morphism `f : X ⟶ Y` of fppf sheaves on the big fppf site of `S` has relative diagonal `P`
> exactly when, for every object `Z` of the site and every morphism from the sheaf it represents to
> `Y`, the base change `Z ×_Y X ⟶ Z` of `f` has relative diagonal `P`.

```lean
theorem hasRelativeDiagonal_iff_forall_baseChange (P : MorphismProperty Scheme.{u})
    [P.RespectsIso] {X Y : FppfSheaf B S hS} (f : X ⟶ Y) :
    HasRelativeDiagonal B S hS P f ↔
      ∀ (U : BigFppfOver B S hS) (g : (fppfYoneda B S hS).obj U ⟶ Y),
        HasRelativeDiagonal B S hS P (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.isSeparatedMorphism_iff_forall_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 651](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L651). The attribute's comment: “clauses (1) and (2) for separatedness: a morphism of formal algebraic spaces is separated if and only if its base change to every scheme over the target is separated”.

> A morphism of fppf sheaves on the big fppf site of `S` is separated exactly when its base
> change to every scheme over the target is separated.

```lean
theorem isSeparatedMorphism_iff_forall_baseChange {X Y : FppfSheaf B S hS} (f : X ⟶ Y) :
    IsSeparatedMorphism B S hS f ↔
      ∀ (U : BigFppfOver B S hS) (g : (fppfYoneda B S hS).obj U ⟶ Y),
        IsSeparatedMorphism B S hS (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.hasRelativeDiagonal_iff_forall_affine_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 670](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L670). The attribute's comment: “clauses (1) and (3): a Zariski-local relative diagonal condition holds for a morphism of formal algebraic spaces if and only if its relative diagonal is relatively representable and the condition holds for the base change to every affine scheme over the target”.

> A morphism `f : X ⟶ Y` of fppf sheaves on the big fppf site of `S` has relative diagonal `P`,
> for `P` a Zariski-local property of morphisms of schemes, exactly when its relative diagonal is
> relatively representable and, for every *affine* object `Z` of the site and every morphism from
> the sheaf it represents to `Y`, the base change `Z ×_Y X ⟶ Z` of `f` has relative diagonal
> `P`.

```lean
theorem hasRelativeDiagonal_iff_forall_affine_baseChange (P : MorphismProperty Scheme.{u})
    [IsZariskiLocalAtTarget P] {X Y : FppfSheaf B S hS} (f : X ⟶ Y) :
    HasRelativeDiagonal B S hS P f ↔
      (fppfYoneda B S hS).relativelyRepresentable (pullback.diagonal f) ∧
        ∀ (U : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj U) →
          ∀ (g : (fppfYoneda B S hS).obj U ⟶ Y),
            HasRelativeDiagonal B S hS P (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.isSeparatedMorphism_iff_forall_affine_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 691](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L691). The attribute's comment: “clauses (1) and (3) for separatedness: a morphism of formal algebraic spaces is separated if and only if its relative diagonal is relatively representable and its base change to every affine scheme over the target is separated”.

> A morphism of fppf sheaves on the big fppf site of `S` is separated exactly when its relative
> diagonal is relatively representable and its base change to every affine scheme over the target
> is separated.

```lean
theorem isSeparatedMorphism_iff_forall_affine_baseChange {X Y : FppfSheaf B S hS} (f : X ⟶ Y) :
    IsSeparatedMorphism B S hS f ↔
      (fppfYoneda B S hS).relativelyRepresentable (pullback.diagonal f) ∧
        ∀ (U : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj U) →
          ∀ (g : (fppfYoneda B S hS).obj U ⟶ Y),
            IsSeparatedMorphism B S hS (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.isSeparatedMorphism_iff_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 780](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L780). The attribute's comment: “clauses (3) and (4) for separatedness: a morphism of formal algebraic spaces to an affine scheme is separated if and only if its relative diagonal is relatively representable and its source is a separated formal algebraic space”.

> A morphism `f : X ⟶ Z` of fppf sheaves on the big fppf site of `S` whose target is represented
> by an affine scheme of the site is separated exactly when its relative diagonal is relatively
> representable and the source `X` is separated as a single sheaf, in the sense of clause (2) of
> Stacks 0AJ6: the fibre product over `X` of any two affine scheme-valued points of `X` is affine
> with surjective comparison from the tensor product of their coordinate rings.

```lean
theorem isSeparatedMorphism_iff_isSeparated {X : FppfSheaf B S hS} {Z : BigFppfOver B S hS}
    (hZ : IsAffine ((BigFppfOver.toScheme B S hS).obj Z)) (f : X ⟶ (fppfYoneda B S hS).obj Z) :
    IsSeparatedMorphism B S hS f ↔
      (fppfYoneda B S hS).relativelyRepresentable (pullback.diagonal f) ∧
        IsSeparated B S hS X
```

**`AlgebraicGeometry.FormalSpace.isSeparatedMorphism_iff_forall_affine_baseChange_of_relativelyRepresentable_diag`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 846](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L846). The attribute's comment: “clauses (1) and (3) for separatedness with no extra conjunct, generalized past the source: the binder `hX` asks only that the absolute diagonal of the source be relatively representable, which every formal algebraic space satisfies by Stacks 0AIP, so the source's own case needs no such binder and is proved outright in `…isSeparatedMorphism_iff_forall_affine_baseChange_of_isFormalAlgebraicSpace`”.

> A morphism of fppf sheaves whose source has relatively representable absolute diagonal is
> separated exactly when its base change to every affine scheme over the target is separated.

```lean
theorem isSeparatedMorphism_iff_forall_affine_baseChange_of_relativelyRepresentable_diag
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : (fppfYoneda B S hS).relativelyRepresentable (diag X)) :
    IsSeparatedMorphism B S hS f ↔
      ∀ (U : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj U) →
        ∀ (g : (fppfYoneda B S hS).obj U ⟶ Y),
          IsSeparatedMorphism B S hS (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.isSeparatedMorphism_iff_isSeparated_of_relativelyRepresentable_diag`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 863](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L863). The attribute's comment: “clauses (3) and (4) for separatedness with no extra conjunct, generalized past the source: the binder `hX` asks only that the absolute diagonal of the source be relatively representable, which every formal algebraic space satisfies by Stacks 0AIP, so the source's own case needs no such binder and is proved outright in `…isSeparatedMorphism_iff_isSeparated_of_isFormalAlgebraicSpace`”.

> A morphism to an affine scheme out of a sheaf with relatively representable absolute
> diagonal is separated exactly when that sheaf is separated.

```lean
theorem isSeparatedMorphism_iff_isSeparated_of_relativelyRepresentable_diag
    {X : FppfSheaf B S hS} {Z : BigFppfOver B S hS}
    (hZ : IsAffine ((BigFppfOver.toScheme B S hS).obj Z)) (f : X ⟶ (fppfYoneda B S hS).obj Z)
    (hX : (fppfYoneda B S hS).relativelyRepresentable (diag X)) :
    IsSeparatedMorphism B S hS f ↔ IsSeparated B S hS X
```

**`AlgebraicGeometry.FormalSpace.isSeparatedMorphism_iff_forall_affine_baseChange_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 877](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L877). The attribute's comment: “clauses (1) and (3) for separatedness, in the source's form with no extra conjunct: a morphism of formal algebraic spaces is separated if and only if its base change to every affine scheme over the target is separated”.

> A morphism `f : X ⟶ Y` of fppf sheaves on the big fppf site of `S` whose source is a formal
> algebraic space is separated exactly when its base change to every affine scheme over the target is
> separated.

```lean
theorem isSeparatedMorphism_iff_forall_affine_baseChange_of_isFormalAlgebraicSpace
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y) (hX : IsFormalAlgebraicSpace B S hS X) :
    IsSeparatedMorphism B S hS f ↔
      ∀ (U : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj U) →
        ∀ (g : (fppfYoneda B S hS).obj U ⟶ Y),
          IsSeparatedMorphism B S hS (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.isSeparatedMorphism_iff_isSeparated_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 892](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L892). The attribute's comment: “clauses (3) and (4) for separatedness, in the source's form with no extra conjunct: a morphism from a formal algebraic space to an affine scheme is separated if and only if its source is a separated formal algebraic space”.

> A morphism from a formal algebraic space to a sheaf represented by an affine scheme of the
> site is separated exactly when its source is a separated formal algebraic space, separatedness of
> a single sheaf being read as clause (2) of Stacks 0AJ6.

```lean
theorem isSeparatedMorphism_iff_isSeparated_of_isFormalAlgebraicSpace
    {X : FppfSheaf B S hS} {Z : BigFppfOver B S hS}
    (hZ : IsAffine ((BigFppfOver.toScheme B S hS).obj Z)) (f : X ⟶ (fppfYoneda B S hS).obj Z)
    (hX : IsFormalAlgebraicSpace B S hS X) :
    IsSeparatedMorphism B S hS f ↔ IsSeparated B S hS X
```

**`AlgebraicGeometry.FormalSpace.hasRelativeDiagonal_iff_forall_affine_baseChange_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 907](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L907). The attribute's comment: “clauses (1) and (3) for a relative diagonal condition, in the source's form with no extra conjunct: the condition holds for a morphism of formal algebraic spaces if and only if it holds for the base change to every affine scheme over the target”.

> A morphism `f : X ⟶ Y` of fppf sheaves on the big fppf site of `S` whose source is a formal
> algebraic space has relative diagonal `P`, for `P` a Zariski-local property of morphisms of
> schemes, exactly when its base change to every affine scheme over the target has relative diagonal
> `P`.

```lean
theorem hasRelativeDiagonal_iff_forall_affine_baseChange_of_isFormalAlgebraicSpace
    (P : MorphismProperty Scheme.{u}) [IsZariskiLocalAtTarget P] {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) (hX : IsFormalAlgebraicSpace B S hS X) :
    HasRelativeDiagonal B S hS P f ↔
      ∀ (U : BigFppfOver B S hS), IsAffine ((BigFppfOver.toScheme B S hS).obj U) →
        ∀ (g : (fppfYoneda B S hS).obj U ⟶ Y),
          HasRelativeDiagonal B S hS P (pullback.snd f g)
```

**`AlgebraicGeometry.FormalSpace.hasRelativeDiagonal_of_locallySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 1064](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L1064). The attribute's comment: “the descent step of clause (5): a relative diagonal condition descends along a single locally surjective morphism onto the relative self-product, which is the atlas clause with the covering of Definition 0AIM replaced by one locally surjective morphism, and is not the atlas form itself”.

> A relative diagonal condition for an fppf-local property `P` of morphisms of schemes
> descends along a locally surjective morphism `b` onto the relative self-product `X ×_Y X`: if the
> base change of the relative diagonal of `f` along `b` has `P` relative to the site, and the
> relative diagonal is relatively representable, then `f` has relative diagonal `P`.

```lean
theorem hasRelativeDiagonal_of_locallySurjective (P : MorphismProperty Scheme.{u})
    [P.IsStableUnderBaseChange] [P.IsLocalAtTarget Scheme.fppfPrecoverage]
    {X Y W : FppfSheaf B S hS} (f : X ⟶ Y) (b : W ⟶ pullback f f)
    (hb : Sheaf.IsLocallySurjective b)
    (hrep : (fppfYoneda B S hS).relativelyRepresentable (pullback.diagonal f))
    (hbase : (MorphismProperty.inverseImage P (BigFppfOver.toScheme B S hS)).relative
      (fppfYoneda B S hS) (pullback.snd (pullback.diagonal f) b)) :
    HasRelativeDiagonal B S hS P f
```

**`AlgebraicGeometry.FormalSpace.isSeparatedMorphism_of_locallySurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 1088](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L1088). The attribute's comment: “the descent step of clause (5) for separatedness: separatedness descends along a single locally surjective morphism onto the relative self-product, which is the atlas clause with the covering of Definition 0AIM replaced by one locally surjective morphism, and is not the atlas form itself”.

> Separatedness of a morphism of fppf sheaves whose relative diagonal is relatively representable
> descends along a locally surjective morphism onto the relative self-product.

```lean
theorem isSeparatedMorphism_of_locallySurjective {X Y W : FppfSheaf B S hS} (f : X ⟶ Y)
    (b : W ⟶ pullback f f) (hb : Sheaf.IsLocallySurjective b)
    (hrep : (fppfYoneda B S hS).relativelyRepresentable (pullback.diagonal f))
    (hbase : (MorphismProperty.inverseImage
      (@AlgebraicGeometry.IsClosedImmersion.{u} : MorphismProperty Scheme.{u})
      (BigFppfOver.toScheme B S hS)).relative (fppfYoneda B S hS)
      (pullback.snd (pullback.diagonal f) b)) :
    IsSeparatedMorphism B S hS f
```

**`AlgebraicGeometry.FormalSpace.hasRelativeDiagonal_of_locallySurjectiveFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 1111](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L1111). The attribute's comment: “the descent step of clause (5) for a covering family: a relative diagonal condition descends along a family of morphisms onto the relative self-product whose induced morphism out of the coproduct is a surjection of sheaves”.

> A relative diagonal condition for an fppf-local property `P` of morphisms of schemes
> descends along a *family* `(b i : W i ⟶ X ×_Y X)` of morphisms onto the relative self-product
> whose induced morphism out of the coproduct is a surjection of sheaves: if the base change of the
> relative diagonal of `f` along each `b i` has `P` relative to the site, and the relative diagonal
> is relatively representable, then `f` has relative diagonal `P`.

```lean
theorem hasRelativeDiagonal_of_locallySurjectiveFamily (P : MorphismProperty Scheme.{u})
    [P.IsStableUnderBaseChange] [P.IsLocalAtTarget Scheme.fppfPrecoverage]
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y) (I : Type (u + 1)) (W : I → FppfSheaf B S hS)
    (b : ∀ i, W i ⟶ pullback f f)
    (hb : letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) :=
        Sheaf.instHasColimitsOfSize
      Sheaf.IsLocallySurjective (Sigma.desc b))
    (hrep : (fppfYoneda B S hS).relativelyRepresentable (pullback.diagonal f))
    (hbase : ∀ i, (MorphismProperty.inverseImage P (BigFppfOver.toScheme B S hS)).relative
      (fppfYoneda B S hS) (pullback.snd (pullback.diagonal f) (b i))) :
    HasRelativeDiagonal B S hS P f
```

**`AlgebraicGeometry.FormalSpace.exists_atlas_hasRelativeDiagonal_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 1141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L1141). The attribute's comment: “clause (5) in the covering form of Definition 0AIM, necessity: a relative diagonal condition for a morphism of formal algebraic spaces holds for the base change to every member of some covering of the target as in Definition 0AIM”.

> If `Y` is a formal algebraic space and the morphism `f : X ⟶ Y` of fppf sheaves on the big fppf
> site of `S` has relative diagonal `P`, then there is a covering `{Y_j ⟶ Y}` as in Definition 0AIM
> such that the base change `Y_j ×_Y X ⟶ Y_j` of `f` has relative diagonal `P` for every `j`.

```lean
theorem exists_atlas_hasRelativeDiagonal_pullback_snd (P : MorphismProperty Scheme.{u})
    [P.RespectsIso] {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hY : IsFormalAlgebraicSpace B S hS Y) (hf : HasRelativeDiagonal B S hS P f) :
    letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) := Sheaf.instHasColimitsOfSize
    ∃ (I : Type (u + 1)) (Yj : I → FppfSheaf B S hS) (g : ∀ j, Yj j ⟶ Y),
      (∀ j, IsAffineFormalAlgebraicSpace B S hS (Yj j)) ∧
      (∀ j, ∃ hgj : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS (g j).hom,
        Space.HasPropertyULift.{u + 1} B S hS
          (fun _ _ k ↦ Space.IsEtaleULift.{u + 1} B S hS k.hom) (g j).hom hgj) ∧
      Sheaf.IsLocallySurjective (Sigma.desc g) ∧
      ∀ j, HasRelativeDiagonal B S hS P (pullback.snd f (g j))
```

**`AlgebraicGeometry.FormalSpace.exists_atlas_isSeparatedMorphism_pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 1161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L1161). The attribute's comment: “clause (5) in the covering form of Definition 0AIM, necessity for separatedness: a separated morphism of formal algebraic spaces has separated base change to every member of some covering of the target as in Definition 0AIM”.

> If `Y` is a formal algebraic space and `f : X ⟶ Y` is separated then there is a covering
> `{Y_j ⟶ Y}` as in Definition 0AIM along which every base change of `f` is separated.

```lean
theorem exists_atlas_isSeparatedMorphism_pullback_snd {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hY : IsFormalAlgebraicSpace B S hS Y) (hf : IsSeparatedMorphism B S hS f) :
    letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) := Sheaf.instHasColimitsOfSize
    ∃ (I : Type (u + 1)) (Yj : I → FppfSheaf B S hS) (g : ∀ j, Yj j ⟶ Y),
      (∀ j, IsAffineFormalAlgebraicSpace B S hS (Yj j)) ∧
      (∀ j, ∃ hgj : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS (g j).hom,
        Space.HasPropertyULift.{u + 1} B S hS
          (fun _ _ k ↦ Space.IsEtaleULift.{u + 1} B S hS k.hom) (g j).hom hgj) ∧
      Sheaf.IsLocallySurjective (Sigma.desc g) ∧
      ∀ j, IsSeparatedMorphism B S hS (pullback.snd f (g j))
```

**`AlgebraicGeometry.FormalSpace.hasRelativeDiagonal_of_atlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 1228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L1228). The attribute's comment: “clause (5) in the covering form of Definition 0AIM, sufficiency for a relative diagonal condition: the condition holds for a morphism of formal algebraic spaces with relatively representable relative diagonal as soon as it holds for the base change to every member of a covering of the target as in Definition 0AIM”.

> Let `f : X ⟶ Y` be a morphism of fppf sheaves on the big fppf site of `S` and let `P` be a
> property of morphisms of schemes which is stable under base change and local on the target for
> the fppf topology. If there is a family `{Y_j ⟶ Y}` whose induced morphism from the coproduct is
> a surjection of sheaves — the covering condition of Definition 0AIM — such that every base change
> `Y_j ×_Y X ⟶ Y_j` of `f` has relative diagonal `P`, and the relative diagonal of `f` is
> relatively representable, then `f` has relative diagonal `P`.

```lean
theorem hasRelativeDiagonal_of_atlas (P : MorphismProperty Scheme.{u})
    [P.IsStableUnderBaseChange] [P.IsLocalAtTarget Scheme.fppfPrecoverage]
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (I : Type (u + 1)) (Yj : I → FppfSheaf B S hS) (g : ∀ j, Yj j ⟶ Y)
    (hsurj : letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) :=
        Sheaf.instHasColimitsOfSize
      Sheaf.IsLocallySurjective (Sigma.desc g))
    (hrep : (fppfYoneda B S hS).relativelyRepresentable (pullback.diagonal f))
    (hP : ∀ j, HasRelativeDiagonal B S hS P (pullback.snd f (g j))) :
    HasRelativeDiagonal B S hS P f
```

**`AlgebraicGeometry.FormalSpace.hasRelativeDiagonal_of_atlas_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 1256](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L1256). The attribute's comment: “clause (5) in the covering form of Definition 0AIM, sufficiency for a relative diagonal condition, in the source's form with no extra conjunct: the condition holds for a morphism of formal algebraic spaces as soon as it holds for the base change to every member of a covering of the target as in Definition 0AIM”.

> A morphism `f : X ⟶ Y` of fppf sheaves on the big fppf site of `S` whose source is a formal
> algebraic space has relative diagonal `P` as soon as its base change to every member of some
> covering of the target as in Definition 0AIM does.

```lean
theorem hasRelativeDiagonal_of_atlas_of_isFormalAlgebraicSpace (P : MorphismProperty Scheme.{u})
    [P.IsStableUnderBaseChange] [P.IsLocalAtTarget Scheme.fppfPrecoverage]
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (I : Type (u + 1)) (Yj : I → FppfSheaf B S hS) (g : ∀ j, Yj j ⟶ Y)
    (hsurj : letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) :=
        Sheaf.instHasColimitsOfSize
      Sheaf.IsLocallySurjective (Sigma.desc g))
    (hX : IsFormalAlgebraicSpace B S hS X)
    (hP : ∀ j, HasRelativeDiagonal B S hS P (pullback.snd f (g j))) :
    HasRelativeDiagonal B S hS P f
```

**`AlgebraicGeometry.FormalSpace.isSeparatedMorphism_of_atlas`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean, line 1277](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/SeparatedMorphism.lean#L1277). The attribute's comment: “clause (5) in the covering form of Definition 0AIM, sufficiency for separatedness: a morphism of formal algebraic spaces is separated as soon as its base change to every member of a covering of the target as in Definition 0AIM is separated”.

> Let `f : X ⟶ Y` be a morphism of fppf sheaves on the big fppf site of `S`. If there is a family
> `{Y_j ⟶ Y}` whose induced morphism from the coproduct is a surjection of sheaves — which is the
> covering condition of Definition 0AIM — such that every base change `Y_j ×_Y X ⟶ Y_j` of `f` is
> separated, then `f` is separated.

```lean
theorem isSeparatedMorphism_of_atlas {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (I : Type (u + 1)) (Yj : I → FppfSheaf B S hS) (g : ∀ j, Yj j ⟶ Y)
    (hsurj : letI : HasColimitsOfSize.{u + 1, u + 1} (FppfSheaf B S hS) :=
        Sheaf.instHasColimitsOfSize
      Sheaf.IsLocallySurjective (Sigma.desc g))
    (hsep : ∀ j, IsSeparatedMorphism B S hS (pullback.snd f (g j))) :
    IsSeparatedMorphism B S hS f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 87.30, Tag 0ARM](https://stacks.math.columbia.edu/tag/0ARM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
