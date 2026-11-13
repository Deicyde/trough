---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.PicardSituation.isGerbeOver_toPicardFunctorBased, AlgebraicGeometry.Space.PicardSituation.isImmersion_and_isQuasiCompact_diagonal_of_iso_picardFunctor, AlgebraicGeometry.Space.PicardSituation.isQuasiSeparated_and_isLocallyOfFinitePresentation_of_represents_picardFunctor, AlgebraicGeometry.Space.PicardSituation.isSeparated_of_represents_picardFunctor_of_hasIntegralGeometricFibres, AlgebraicGeometry.Space.isAlgebraicSpaceOver_and_isSmooth_picardFunctor
statement: formalized
proof: formalized
---

# 108.9 Properties of the Picard functor

Section 108.9 of the Stacks Project, [Tag 0DMD](https://stacks.math.columbia.edu/tag/0DMD). 5 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0DME, a lemma

[Tag 0DME](https://stacks.math.columbia.edu/tag/0DME) in the Stacks Project.

**`AlgebraicGeometry.Space.PicardSituation.isGerbeOver_toPicardFunctorBased`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardStackGerbe.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardStackGerbe.lean#L270).

> In Situation 0D25 — a morphism `f : X ⟶ B` of algebraic spaces over `S` —
> the morphism `Picardstack_{X/B} ⟶ Pic_{X/B}`, sending an object `(U, b, L)` to the element of
> `Pic_{X/B}(U, b)` named by the class of `L`, turns the Picard stack into a gerbe over the Picard
> functor: it satisfies the two conditions of Stacks 06P2 (conditions (2)(a) and (2)(b) of
> Stacks 06P1) over the big fppf site of `S`, which is the condition of Stacks 06QC.
>
> The section's assumptions on `f` (flat, proper, of finite presentation, with
> `𝒪_T ≅ f_{T,*}𝒪_{X_T}` for every `T`) are not assumed.

```lean
theorem isGerbeOver_toPicardFunctorBased :
    IsGerbeOver (BigFppfOver.topology B S hS) s.picardFunctorBasedCategory.p
      s.toPicardFunctorBased.toFunctor
```

## Tag 0DMF, a lemma

[Tag 0DMF](https://stacks.math.columbia.edu/tag/0DMF) in the Stacks Project.

**`AlgebraicGeometry.Space.PicardSituation.isImmersion_and_isQuasiCompact_diagonal_of_iso_picardFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardFunctorDiagonalQuasiCompactImmersion.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardFunctorDiagonalQuasiCompactImmersion.lean#L59).

> Let `f : X ⟶ B` be a morphism of algebraic spaces over `S` which is flat, proper and of
> finite presentation, such that `𝒪_T ⟶ f_{T,*}𝒪_{X_T}` is an isomorphism for every scheme `T`
> over `B`, and let `p : H ⟶ B` be an algebraic space over `B` whose functor of points over `B` is
> identified (`c`) with the relative Picard functor `Pic_{X/B}` (such an `H` exists by Stacks 0D2C,
> `AlgebraicGeometry.Space.isAlgebraicSpaceOver_picardFunctor`). Then the diagonal `H ⟶ H ×_B H` of
> `Pic_{X/B}` over `B` is a quasi-compact immersion.

```lean
theorem isImmersion_and_isQuasiCompact_diagonal_of_iso_picardFunctor
    {s : PicardSituation B S hS} (hflat : IsFlat B S hS s.f.hom)
    (hfp : IsFinitePresentation B S hS s.f.hom) (hproper : IsProper B S hS s.f.hom)
    (h : s.StructureSheafMapIso) {H : AlgebraicSpaces B S hS} {p : H ⟶ s.base}
    (c : spacePointsOver p ⋙ uliftFunctor.{u + 1, u} ≅ s.picardFunctor) :
    IsImmersion B S hS (pullback.diagonal p.hom) ∧
      IsQuasiCompact B S hS (pullback.diagonal p.hom)
```

## Tag 0DNI, a lemma

[Tag 0DNI](https://stacks.math.columbia.edu/tag/0DNI) in the Stacks Project.

**`AlgebraicGeometry.Space.PicardSituation.isQuasiSeparated_and_isLocallyOfFinitePresentation_of_represents_picardFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardFunctorRepresentingSpace.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardFunctorRepresentingSpace.lean#L62). The attribute's comment: “Stated for every algebraic space representing Pic\_\{X/B}, i.e. with an identification c of its points over B with Pic\_\{X/B}, since Section 0DMD presupposes that Pic\_\{X/B} is an algebraic space (Stacks 0D2C); with Pic\_\{X/B} itself as that space this is the lemma as printed. The cohomological-flatness condition O\_T -> f\_\{T,*}O\_\{X\_T} iso of the section is dropped: f flat, proper and of finite presentation suffices.”.

> Let `f : X ⟶ B` be a flat, proper morphism of finite presentation of algebraic spaces, and
> let `p : H ⟶ B` be an algebraic space over `B` whose functor of points over `B` is identified
> (`c`) with the relative Picard functor `Pic_{X/B}`. Then `p` is quasi-separated and locally of
> finite presentation.

```lean
theorem isQuasiSeparated_and_isLocallyOfFinitePresentation_of_represents_picardFunctor
    (c : spacePointsOver p ⋙ uliftFunctor.{u + 1, u} ≅ s.picardFunctor)
    (hflat : IsFlat B S hS s.f.hom) (hfp : IsFinitePresentation B S hS s.f.hom)
    (hproper : IsProper B S hS s.f.hom) :
    IsQuasiSeparated B S hS p.hom ∧ Space.IsLocallyOfFinitePresentation B S hS p.hom
```

## Tag 0DNJ, a lemma

[Tag 0DNJ](https://stacks.math.columbia.edu/tag/0DNJ) in the Stacks Project.

**`AlgebraicGeometry.Space.PicardSituation.isSeparated_of_represents_picardFunctor_of_hasIntegralGeometricFibres`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardFunctorRepresentingSpace.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardFunctorRepresentingSpace.lean#L78). The attribute's comment: “Stated for every algebraic space representing Pic\_\{X/B}, i.e. with an identification c of its points over B with Pic\_\{X/B}, since Section 0DMD presupposes that Pic\_\{X/B} is an algebraic space (Stacks 0D2C); with Pic\_\{X/B} itself as that space this is the lemma as printed.”.

> Let `f : X ⟶ B` be a flat, proper morphism of finite presentation of algebraic spaces with
> `𝒪_T ≅ f_{T,*}𝒪_{X_T}` for every scheme `T` over `B`, whose geometric fibres are integral, and
> let `p : H ⟶ B` be an algebraic space over `B` whose functor of points over `B` is identified
> (`c`) with the relative Picard functor `Pic_{X/B}`. Then `p` is separated.

```lean
theorem isSeparated_of_represents_picardFunctor_of_hasIntegralGeometricFibres
    (c : spacePointsOver p ⋙ uliftFunctor.{u + 1, u} ≅ s.picardFunctor)
    (hflat : IsFlat B S hS s.f.hom) (hfp : IsFinitePresentation B S hS s.f.hom)
    (hproper : IsProper B S hS s.f.hom) (hstein : s.StructureSheafMapIso)
    (hgeom : HasIntegralGeometricFibres B S hS s.f.hom) :
    IsSeparated B S hS p.hom
```

## Tag 0DPK, a lemma

[Tag 0DPK](https://stacks.math.columbia.edu/tag/0DPK) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpaceOver_and_isSmooth_picardFunctor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Quot/PicardFunctorSmooth.lean, line 208](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Quot/PicardFunctorSmooth.lean#L208). The attribute's comment: “the full statement, in the setting of Section 0DMD: f flat (hflat), of finite presentation (hfp), proper (hproper), O\_T -> f\_\{T,*}O\_\{X\_T} an isomorphism for every T (hstr), of relative dimension ≤ 1 (hd); the conclusion contains that Pic\_\{X/B} is an algebraic space over B (Stacks 0D2C) and that its morphism to B is smooth, for every algebraic space representing it”.

> **The Picard functor is smooth in relative dimension `≤ 1`.** Let `f : X ⟶ Y` be a morphism
> of algebraic spaces over `S` which is flat, of finite presentation and proper, with
> `𝒪_T ⟶ f_{T,*}𝒪_{X_T}` an isomorphism for every scheme `T` over `Y` (the standing assumptions of
> Section 0DMD), and of relative dimension `≤ 1`. Then `Pic_{X/Y}` is an algebraic space over `Y`
> (Stacks 0D2C) and `Pic_{X/Y} ⟶ Y` is smooth: every algebraic space `H` with a morphism
> `p : H ⟶ Y` whose functor of points over `Y` is identified with `Pic_{X/Y}` has `p` smooth.

```lean
theorem isAlgebraicSpaceOver_and_isSmooth_picardFunctor {X Y : AlgebraicSpaces B S hS}
    (f : X ⟶ Y) (hflat : IsFlat B S hS f.hom) (hfp : IsFinitePresentation B S hS f.hom)
    (hproper : IsProper B S hS f.hom)
    (hstr : (PicardSituation.mk X Y f).StructureSheafMapIso)
    (hd : HasRelativeDimensionLE 1 B S hS f.hom) :
    IsAlgebraicSpaceOver (PicardSituation.mk X Y f).picardFunctor ∧
      ∀ (H : AlgebraicSpaces B S hS) (p : H ⟶ Y),
        Nonempty (spacePointsOver p ⋙ uliftFunctor.{u + 1, u} ≅
          (PicardSituation.mk X Y f).picardFunctor) →
        IsSmooth B S hS p.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 108.9, Tag 0DMD](https://stacks.math.columbia.edu/tag/0DMD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
