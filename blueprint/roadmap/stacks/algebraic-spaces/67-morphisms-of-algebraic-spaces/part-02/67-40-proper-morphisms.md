---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isProperULift_whiskerRight_iff, AlgebraicGeometry.Space.IsProper, AlgebraicGeometry.Space.isProper_tfae, AlgebraicGeometry.Space.isProper_isStableUnderBaseChange, AlgebraicGeometry.Space.isProper_comp', AlgebraicGeometry.Space.isProper_of_isClosedImmersion, AlgebraicGeometry.Space.isProper_of_comp_of_isSeparated, AlgebraicGeometry.Space.universallyClosed_of_comp_of_isSeparated
statement: formalized
proof: formalized
---

# 67.40 Proper morphisms

Section 67.40 of the Stacks Project, [Tag 03ZL](https://stacks.math.columbia.edu/tag/03ZL). 9 tags here are carried by 16 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03ZM, a definition

[Tag 03ZM](https://stacks.math.columbia.edu/tag/03ZM) in the Stacks Project.

**`AlgebraicGeometry.Space.isProperULift_whiskerRight_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedProperTransfer.lean, line 134](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/LargeValuedProperTransfer.lean#L134). The attribute's comment: “for a universe lift”.

> **Stacks 03ZM for a universe lift.** The universe lift of a morphism of presheaves of
> `Type u` on the big fppf site of `S` is proper — separated, of finite type and universally
> closed — exactly when the morphism is.
>
> Each conjunct transfers separately: separatedness by
> `AlgebraicGeometry.Space.isSeparatedULift_whiskerRight_iff`, being of finite type by
> `AlgebraicGeometry.Space.isFiniteTypeULift_whiskerRight_iff` and universal closedness by
> `AlgebraicGeometry.Space.universallyClosedULift_whiskerRight_iff`.

```lean
theorem isProperULift_whiskerRight_iff {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (q : F ⟶ G) :
    IsProperULift.{w} B S hS (Functor.whiskerRight q uliftFunctor.{w}) ↔
      IsProper B S hS q
```

**`AlgebraicGeometry.Space.IsProper`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversallyClosed.lean, line 132](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversallyClosed.lean#L132).

> A morphism of algebraic spaces over `S` is *proper* when it is separated, of finite type and
> universally closed.

```lean
abbrev IsProper (f : F ⟶ G) : Prop
```

## Tag 083R, a lemma

[Tag 083R](https://stacks.math.columbia.edu/tag/083R) in the Stacks Project.

**`AlgebraicGeometry.Space.isProper_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ProperCriteria.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ProperCriteria.lean#L162).

> **Stacks 083R.** For a morphism `f : X ⟶ Y` of algebraic spaces over `S` the following are
> equivalent: `f` is proper; the base change of `f` along every morphism to `Y` from a presheaf
> represented by an object of the site is proper; the same for the objects with affine underlying
> scheme; the base change of `f` along some surjective étale morphism to `Y` from a represented
> presheaf is proper; and there is a Zariski covering of `Y` along each member of which the base
> change of `f` is proper.

```lean
theorem isProper_tfae (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) :
    List.TFAE
      [IsProper B S hS f,
        ∀ (W : BigFppfOver B S hS) (g : yoneda.obj W ⟶ Y),
          IsProper B S hS (pullback.fst g f),
        ∀ (W : BigFppfOver B S hS) (g : yoneda.obj W ⟶ Y),
          IsAffine ((BigFppfOver.toScheme B S hS).obj W) →
            IsProper B S hS (pullback.fst g f),
        ∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
          IsSurjective B S hS g ∧ IsEtale B S hS g ∧
            IsProper B S hS (pullback.fst g f),
        ∃ (I : Type u) (U : I → Subfunctor Y) (_ : IsZariskiCover B S hS I U),
          ∀ i, IsProper B S hS (pullback.fst (U i).ι f)]
```

## Tag 04WP, a lemma

[Tag 04WP](https://stacks.math.columbia.edu/tag/04WP) in the Stacks Project.

**`AlgebraicGeometry.Space.isProper_isStableUnderBaseChange`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperBaseChange.lean, line 164](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperBaseChange.lean#L164).

> Properness of morphisms of algebraic spaces over `S` is stable under base
> change.

```lean
instance isProper_isStableUnderBaseChange :
    MorphismProperty.IsStableUnderBaseChange
      (fun ⦃F G : AlgebraicSpaces B S hS⦄ (f : F ⟶ G) => IsProper B S hS f.hom)
```

## Tag 04XY, a lemma

[Tag 04XY](https://stacks.math.columbia.edu/tag/04XY) in the Stacks Project.

**`AlgebraicGeometry.Space.isProper_comp'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperPermanence.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperPermanence.lean#L81).

> **Stacks 04XY.** The composite of two proper morphisms of algebraic spaces over `S` is
> proper: each of the three conjuncts of properness is stable under composition.
>
> Algebraicity of the source is not needed and is not assumed, which is what distinguishes this
> from `AlgebraicGeometry.Space.isProper_comp`. None of the three conjuncts asks for it:
> separatedness is a condition on a relative diagonal, and the quantifiers of
> `AlgebraicGeometry.Space.IsQuasiCompact` and `AlgebraicGeometry.Space.UniversallyClosed` reach
> only the intermediate and final spaces.

```lean
theorem isProper_comp' (f : X ⟶ Y) (g : Y ⟶ Z)
    (hY : IsAlgebraicSpace B S hS Y) (hZ : IsAlgebraicSpace B S hS Z)
    (hf : IsProper B S hS f) (hg : IsProper B S hS g) :
    IsProper B S hS (f ≫ g)
```

## Tag 04XZ, a lemma

[Tag 04XZ](https://stacks.math.columbia.edu/tag/04XZ) in the Stacks Project.

**`AlgebraicGeometry.Space.isProper_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ProperClosedImmersion.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ProperClosedImmersion.lean#L202).

> **Stacks 04XZ.** A closed immersion of algebraic spaces over `S` is proper.

```lean
theorem isProper_of_isClosedImmersion
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (f : X ⟶ Y) (hf : IsClosedImmersion B S hS f) :
    IsProper B S hS f
```

## Tag 04NX, a lemma

[Tag 04NX](https://stacks.math.columbia.edu/tag/04NX) in the Stacks Project.

**`AlgebraicGeometry.Space.isProper_of_comp_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SeparationCancellation.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SeparationCancellation.lean#L120). The attribute's comment: “part (2): properness”.

> **Stacks 04NX, part (2).** If a composite of morphisms of algebraic spaces over `S` is proper
> and its second factor is separated, then its first factor is proper.
>
> Properness is separatedness, finite type and universal closedness (**Stacks 03ZM**). The first
> cancels by **Stacks 03KR** and the universal closedness by part (1) of Stacks 04NX; finite type
> is local finite type, which cancels by **Stacks 0462**, together with quasi-compactness, which
> cancels by **Stacks 03KS** against a quasi-separated second factor — and the second factor is
> quasi-separated, being separated (**Stacks 03KK**).

```lean
theorem isProper_of_comp_of_isSeparated {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hfg : IsProper B S hS (f ≫ g)) (hg : IsSeparated B S hS g) :
    IsProper B S hS f
```

**`AlgebraicGeometry.Space.universallyClosed_of_comp_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversallyClosedPermanence.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversallyClosedPermanence.lean#L67). The attribute's comment: “part (1): universal closedness”. References: EGA II (5.4.9), “5.4.3 univ. closed”.

> **Stacks 04NX, part (1).** Let `X ⟶ Y ⟶ Z` be morphisms of algebraic spaces over `S`. If
> the composite `X ⟶ Z` is universally closed and `Y ⟶ Z` is separated, then `X ⟶ Y` is
> universally closed.

```lean
theorem universallyClosed_of_comp_of_isSeparated {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hfg : UniversallyClosed B S hS (f ≫ g)) (hg : IsSeparated B S hS g) :
    UniversallyClosed B S hS f
```

**`AlgebraicGeometry.Space.isClosed_range_of_comp_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversallyClosedPermanence.lean, line 91](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversallyClosedPermanence.lean#L91). The attribute's comment: “part (1): closed image”.

> **Stacks 04NX, part (1).** Under the hypotheses of
> `AlgebraicGeometry.Space.universallyClosed_of_comp_of_isSeparated`, the image of `|X|` in
> `|Y|` is closed.

```lean
theorem isClosed_range_of_comp_of_isSeparated {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (g : Y ⟶ Z)
    (hfg : UniversallyClosed B S hS (f ≫ g)) (hg : IsSeparated B S hS g) :
    _root_.IsClosed (Set.range (pointsMap B S hS X f))
```

## Tag 08AJ, a lemma

[Tag 08AJ](https://stacks.math.columbia.edu/tag/08AJ) in the Stacks Project.

**`AlgebraicGeometry.Space.universallyClosed_of_isSurjective_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Proper.lean, line 120](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Proper.lean#L120). The attribute's comment: “universally closed image”.

> **Stacks 08AJ, universally closed image.** Let `X ⟶ Y ⟶ T` be morphisms of algebraic
> spaces over `S`. If `X` is universally closed over `T` and `X ⟶ Y` is surjective, then `Y` is
> universally closed over `T`.

```lean
theorem universallyClosed_of_isSurjective_comp
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hT : IsAlgebraicSpace B S hS T) (f : X ⟶ Y) (q : Y ⟶ T)
    (hfq : UniversallyClosed B S hS (f ≫ q)) (hf : IsSurjective B S hS f) :
    UniversallyClosed B S hS q
```

**`AlgebraicGeometry.Space.isProper_of_isSurjective_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Proper.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/Proper.lean#L160). The attribute's comment: “properness of the image”.

> **Stacks 08AJ, properness of the image.** Let `X ⟶ Y ⟶ T` be morphisms of algebraic
> spaces over `S`. If `X` is universally closed over `T`, the morphism `X ⟶ Y` is surjective and
> `Y` is separated and of finite type over `T`, then `Y` is proper over `T`.

```lean
theorem isProper_of_isSurjective_comp
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hT : IsAlgebraicSpace B S hS T) (f : X ⟶ Y) (q : Y ⟶ T)
    (hfq : UniversallyClosed B S hS (f ≫ q)) (hf : IsSurjective B S hS f)
    (hsep : IsSeparated B S hS q) (hft : IsFiniteType B S hS q) :
    IsProper B S hS q
```

**`AlgebraicGeometry.Space.universallyClosed_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversallyClosedImage.lean, line 105](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversallyClosedImage.lean#L105). The attribute's comment: “first assertion: universal closedness”.

> **Stacks 08AJ, first assertion.** Let `p : X ⟶ Z` and `q : Y ⟶ Z` be morphisms of
> algebraic spaces over `S` and let `f : X ⟶ Y` be a morphism over `Z`. If `p` is universally
> closed and `f` is surjective, then `q` is universally closed.
>
> A base change `T ×_Z Y ⟶ T` of `q` is, after the pasting isomorphism
> `(T ×_Z Y) ×_Y X ≅ T ×_Z X`, preceded by the base change of `f`, which is surjective on
> points by Stacks 03MH; the composite is the base change `T ×_Z X ⟶ T` of `p`, closed by
> hypothesis.

```lean
theorem universallyClosed_of_isSurjective {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (_hX : IsAlgebraicSpace B S hS X) (_hY : IsAlgebraicSpace B S hS Y)
    (_hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (p : X ⟶ Z) (q : Y ⟶ Z)
    (hcomm : f ≫ q = p) (hf : IsSurjective B S hS f)
    (hp : UniversallyClosed B S hS p) :
    UniversallyClosed B S hS q
```

**`AlgebraicGeometry.Space.isProper_of_isSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/UniversallyClosedImage.lean, line 124](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/UniversallyClosedImage.lean#L124). The attribute's comment: “second assertion: properness”.

> **Stacks 08AJ, second assertion.** In the situation of
> `AlgebraicGeometry.Space.universallyClosed_of_isSurjective`, if moreover `q` is separated and
> of finite type, then `q` is proper.

```lean
theorem isProper_of_isSurjective {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hZ : IsAlgebraicSpace B S hS Z) (f : X ⟶ Y) (p : X ⟶ Z) (q : Y ⟶ Z)
    (hcomm : f ≫ q = p) (hf : IsSurjective B S hS f)
    (hp : UniversallyClosed B S hS p)
    (hsep : IsSeparated B S hS q) (hft : IsFiniteType B S hS q) :
    IsProper B S hS q
```

## Tag 0AGD, a lemma

[Tag 0AGD](https://stacks.math.columbia.edu/tag/0AGD) in the Stacks Project.

**`AlgebraicGeometry.Space.isSurjective_toSchemeTheoreticImage_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ProperSchemeTheoreticImage.lean, line 106](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ProperSchemeTheoreticImage.lean#L106). The attribute's comment: “second assertion: surjectivity onto the scheme-theoretic image”.

> **Stacks 0AGD, second assertion.** Let `h : X ⟶ Y`, `f : X ⟶ T` and `g : Y ⟶ T` be
> morphisms of algebraic spaces over `S` with `h ≫ g = f`. If `f` is proper and `g` is separated,
> then the morphism from `X` to the scheme-theoretic image of `h` is surjective.
>
> The image of `|X|` in `|Z|` is dense, by part (4) of Stacks 082Z, `h` being quasi-compact by
> Stacks 03KS; and it is closed, being the preimage along the continuous injection `|Z| → |Y|` of
> the image of `|X|` in `|Y|`, which is closed by part (1) of Stacks 04NX.

```lean
theorem isSurjective_toSchemeTheoreticImage_of_isProper
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hT : IsAlgebraicSpace B S hS T) (h : X ⟶ Y) (f : X ⟶ T) (g : Y ⟶ T)
    (hcomm : h ≫ g = f) (hf : IsProper B S hS f) (hg : IsSeparated B S hS g) :
    IsSurjective B S hS (toSchemeTheoreticImage B S hS h)
```

**`AlgebraicGeometry.Space.isProper_schemeTheoreticImageSubfunctor_inclusion_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ProperSchemeTheoreticImage.lean, line 149](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ProperSchemeTheoreticImage.lean#L149). The attribute's comment: “first assertion: the scheme-theoretic image is proper over the base”.

> **Stacks 0AGD, first assertion.** Let `h : X ⟶ Y`, `f : X ⟶ T` and `g : Y ⟶ T` be morphisms
> of algebraic spaces over `S` with `h ≫ g = f`. If `f` is proper and `g` is separated and
> locally of finite type, then the scheme-theoretic image of `h` is proper over `T`.
>
> The scheme-theoretic image is a closed subspace of `Y` (Stacks 082X), so its structure morphism
> over `T` is separated by Stacks 04CH and Stacks 03KQ, and locally of finite type by Stacks 03XG;
> it is quasi-compact by part (2) of Stacks 040W, `X ⟶ T` being quasi-compact and `X` surjecting
> onto the image by
> `AlgebraicGeometry.Space.isSurjective_toSchemeTheoreticImage_of_isProper`. Properness is then
> the second assertion of Stacks 08AJ, `f` being universally closed.

```lean
theorem isProper_schemeTheoreticImageSubfunctor_inclusion_comp
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (hT : IsAlgebraicSpace B S hS T) (h : X ⟶ Y) (f : X ⟶ T) (g : Y ⟶ T)
    (hcomm : h ≫ g = f) (hf : IsProper B S hS f) (hg : IsSeparated B S hS g)
    (hgft : IsLocallyOfFiniteType B S hS g) :
    IsProper B S hS ((schemeTheoreticImageSubfunctor B S hS h).ι ≫ g)
```

## Tag 04Y0, a lemma

[Tag 04Y0](https://stacks.math.columbia.edu/tag/04Y0) in the Stacks Project.

**`AlgebraicGeometry.Space.isSeparated_tfae_diagonal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/DiagonalProperTFAE.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/DiagonalProperTFAE.lean#L49).

> For a morphism of algebraic spaces over `S` the following are equivalent: it is separated;
> its relative diagonal is universally closed; its relative diagonal is proper.

```lean
theorem isSeparated_tfae_diagonal (f : X ⟶ Y) (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) :
    List.TFAE [IsSeparated B S hS f,
      UniversallyClosed B S hS (pullback.diagonal f),
      IsProper B S hS (pullback.diagonal f)]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.40, Tag 03ZL](https://stacks.math.columbia.edu/tag/03ZL)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
