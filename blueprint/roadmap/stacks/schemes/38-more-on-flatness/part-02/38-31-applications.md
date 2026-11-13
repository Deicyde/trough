---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_isAdmissibleBlowup_flat_finitePresentation_strictTransform_of_affineCase, AlgebraicGeometry.exists_isAdmissibleBlowup_isFiniteLocallyFree_strictTransform_of_isProper, AlgebraicGeometry.exists_isAdmissibleBlowup_isOpenImmersion_strictTransform, AlgebraicGeometry.strictTransformOpenImmersion_of_isIso_morphismRestrict, AlgebraicGeometry.exists_isAdmissibleBlowup_dominating_of_affineCase, AlgebraicGeometry.exists_isAdmissibleBlowup_extending_section_of_qcqs
statement: formalized
proof: formalized
---

# 38.31 Applications

Section 38.31 of the Stacks Project, [Tag 081Q](https://stacks.math.columbia.edu/tag/081Q). 5 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 081R, a lemma

[Tag 081R](https://stacks.math.columbia.edu/tag/081R) in the Stacks Project.

**`AlgebraicGeometry.exists_isAdmissibleBlowup_flat_finitePresentation_strictTransform_of_affineCase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Flattening/StrictTransformFinitePresentationFromFlat.lean, line 410](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Flattening/StrictTransformFinitePresentationFromFlat.lean#L410). The attribute's comment: “the conclusion in full -- the strict transform flat AND of finite presentation -- under exactly the source's hypotheses (1) and (2). The affine case of the flatness assertion of [Stacks, Tag 0815] is proved inside, from hypothesis (2), by `AlgebraicGeometry.AffineChartFlatteningCentre.of_affineCase` (through the immersion into affine space of [Stacks, Tag 04II] and `AlgebraicGeometry.AffineChartFlatteningCentreUnderSourceHypotheses.of_compactSpace`, proved from [Stacks, Tag 0811]); the finite-presentation clause comes from the flatness clause by [Stacks, Tag 081N]”.

> **Stacks Project, Tag 081R.** Let `S` be a quasi-compact and quasi-separated scheme, let
> `f : X ⟶ S` be of finite type and quasi-separated and let `U ⊆ S` be a quasi-compact open such
> that `X_U ⟶ U` is flat and locally of finite presentation. Then there is a `U`-admissible blowup
> of `S` along which the strict transform of `X` is flat and of finite presentation.
>
> Both hypotheses of the source are present: (1) `f` of finite type and quasi-separated, and (2)
> `X_U ⟶ U` flat and locally of finite presentation. Hypothesis (2) is what
> `exists_isAdmissibleBlowup_flat_finitePresentation_strictTransform_of_affineCharts`
> and `AlgebraicGeometry.exists_isAdmissibleBlowup_flat_strictTransform` omit the flatness half of,
> on the ground that it enters only through the affine case they take as an input. It does enter
> only through it, but the hypothesis-free `AlgebraicGeometry.AffineChartFlatteningCentre` that
> those forms take is false in general, so no proof of the affine case can supply it. With
> hypothesis (2) present the chain closes:
> `AlgebraicGeometry.AffineChartFlatteningCentre.of_affineCase`
> produces the chart predicate precisely from hypothesis (2), by the source's own route through the
> immersion into affine space of [Stacks, Tag 04II], and the affine case it calls on is
> `AffineChartFlatteningCentreUnderSourceHypotheses.of_compactSpace`, itself proved from
> [Stacks, Tag 0811].

```lean
theorem exists_isAdmissibleBlowup_flat_finitePresentation_strictTransform_of_affineCase
    [CompactSpace S] [QuasiSeparatedSpace S] [LocallyOfFiniteType f] [QuasiCompact f]
    [QuasiSeparated f] (U : S.Opens) (hU : IsCompact (U : Set S)) (hflat : Flat (f ∣_ U))
    (hfp : LocallyOfFinitePresentation (f ∣_ U)) :
    ∃ ℐ : S.IdealSheafData,
      FinitePresentation ℐ.subschemeι ∧
        Disjoint (U : Set S) (ℐ.support : Set S) ∧
          Stacks.Blowup.IsAdmissibleBlowup U (blowUpToBase ℐ) ∧
            Flat (strictTransformToBlowUp f ℐ) ∧
              FinitePresentation (strictTransformToBlowUp f ℐ)
```

## Tag 0B49, a lemma

[Tag 0B49](https://stacks.math.columbia.edu/tag/0B49) in the Stacks Project.

**`AlgebraicGeometry.exists_isAdmissibleBlowup_isFiniteLocallyFree_strictTransform_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Applications/FiniteLocallyFreeStrictTransformOfProper.lean, line 46](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Applications/FiniteLocallyFreeStrictTransformOfProper.lean#L46). The attribute's comment: “the conclusion in full, under exactly the source's hypotheses (1) and (2)”.

> **Stacks Project, Tag 0B49.** Let `S` be a quasi-compact and quasi-separated scheme, let
> `f : X ⟶ S` be proper and let `U ⊆ S` be a quasi-compact open over which `X` is finite locally
> free. Then there is a `U`-admissible blowup of `S` along which the strict transform of `X` is
> finite locally free.

```lean
theorem exists_isAdmissibleBlowup_isFiniteLocallyFree_strictTransform_of_isProper
    {X S : Scheme.{u}} [CompactSpace S] [QuasiSeparatedSpace S] (f : X ⟶ S) [IsProper f]
    (U : S.Opens) (hU : IsCompact (U : Set S))
    [Stacks.Morphisms.IsFiniteLocallyFree (pullback.snd f U.ι)] :
    ∃ I : S.IdealSheafData,
      Stacks.Blowup.IsAdmissibleBlowup U (blowUpToBase I) ∧
        Stacks.Morphisms.IsFiniteLocallyFree (strictTransformToBlowUp f I)
```

## Tag 081S, a lemma

[Tag 081S](https://stacks.math.columbia.edu/tag/081S) in the Stacks Project.

**`AlgebraicGeometry.exists_isAdmissibleBlowup_isOpenImmersion_strictTransform`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Compactification/StrictTransformOpenSubscheme.lean, line 55](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Compactification/StrictTransformOpenSubscheme.lean#L55).

> Let `f : X ⟶ S` be a separated morphism of finite type with `S` quasi-compact and
> quasi-separated, and let `U ⊆ S` be a quasi-compact open such that `f` is an isomorphism over
> `U`. Then there is a centre `M` on `S`, finitely presented and supported away from `U`, such
> that the blowup of `S` in `M` is `U`-admissible and the strict transform of `X` along it is an
> open subscheme of that blowup.

```lean
theorem exists_isAdmissibleBlowup_isOpenImmersion_strictTransform {X S : Scheme.{u}} (f : X ⟶ S)
    [IsSeparated f] [LocallyOfFiniteType f] [QuasiCompact f]
    [CompactSpace S] [QuasiSeparatedSpace S] (U : S.Opens) (hU : IsCompact (U : Set S))
    [IsIso (f ∣_ U)] :
    ∃ M : S.IdealSheafData, FinitePresentation M.subschemeι ∧
      Disjoint (U : Set S) (M.support : Set S) ∧
        Stacks.Blowup.IsAdmissibleBlowup U (blowUpToBase M) ∧
          IsOpenImmersion (strictTransformToBlowUp f M)
```

**`AlgebraicGeometry.strictTransformOpenImmersion_of_isIso_morphismRestrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/Compactification/StrictTransformOpenSubscheme.lean, line 142](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/Compactification/StrictTransformOpenSubscheme.lean#L142).

> A separated morphism of finite type which is an isomorphism over a quasi-compact open `U` of
> a quasi-compact quasi-separated base satisfies `AlgebraicGeometry.StrictTransformOpenImmersion`:
> along the blowup in some finitely presented centre avoiding `U`, its strict transform is an
> open subscheme of the blowup.

```lean
theorem strictTransformOpenImmersion_of_isIso_morphismRestrict {X S : Scheme.{u}} (f : X ⟶ S)
    [IsSeparated f] [LocallyOfFiniteType f] [QuasiCompact f]
    [CompactSpace S] [QuasiSeparatedSpace S] (U : S.Opens) (hU : IsCompact (U : Set S))
    [IsIso (f ∣_ U)] : StrictTransformOpenImmersion f U
```

## Tag 081T, a lemma

[Tag 081T](https://stacks.math.columbia.edu/tag/081T) in the Stacks Project.

**`AlgebraicGeometry.exists_isAdmissibleBlowup_dominating_of_affineCase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/DominatingBlowupFromFlattening.lean, line 87](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/DominatingBlowupFromFlattening.lean#L87). The attribute's comment: “complete, under exactly the source's hypotheses”.

> **Stacks Project, Tag 081T.** Let `f : X ⟶ S` be a proper morphism with `S` quasi-compact and
> quasi-separated, and let `U ⊆ S` be a quasi-compact open such that `f` is an isomorphism over
> `U`. Then there is a `U`-admissible blowup `b : S' ⟶ S` which dominates `X`: a morphism
> `g : S' ⟶ X` with `g ≫ f = b`.
>
> The hypotheses are exactly the source's. Both results the source cites are supplied by proved
> declarations: [Stacks, Tag 080Y] by `AlgebraicGeometry.cartierBoundaryReduction` and
> [Stacks, Tag 081S] by `AlgebraicGeometry.strictTransformOpenImmersion_of_isIso_morphismRestrict`,
> each of which stands on its own hypotheses alone.

```lean
theorem exists_isAdmissibleBlowup_dominating_of_affineCase (f : X ⟶ S) [IsProper f]
    [CompactSpace S] [QuasiSeparatedSpace S] (U : S.Opens) (hU : IsCompact (U : Set S))
    [IsIso (f ∣_ U)] :
    ∃ (S' : Scheme.{u}) (b : S' ⟶ S),
      Stacks.Blowup.IsAdmissibleBlowup U b ∧ ∃ g : S' ⟶ X, g ≫ f = b
```

## Tag 0CP1, a lemma

[Tag 0CP1](https://stacks.math.columbia.edu/tag/0CP1) in the Stacks Project.

**`AlgebraicGeometry.exists_isAdmissibleBlowup_extending_section_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Blowup/SectionExtensionOfQcqs.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Blowup/SectionExtensionOfQcqs.lean#L50). The attribute's comment: “the full statement, under the source's hypotheses (1)-(3)”.

> **Stacks Project, Tag 0CP1.** Let `S` be a quasi-compact and quasi-separated scheme, let
> `W ⊆ S` be a quasi-compact open subscheme and let `U ⊆ W` be a quasi-compact open subscheme.
> Let `f : X ⟶ W` be proper and let `s : U ⟶ X` satisfy `s ≫ f = U.ι`. Then there is a
> `U`-admissible blowup `b : S' ⟶ S` and a morphism `s' : b⁻¹(W) ⟶ X` with `s' ≫ f = b|_{b⁻¹(W)}`
> extending `s`, the extension being witnessed by a morphism `t : U ⟶ b⁻¹(W)` over `W`.
>
> The two results [Stacks, Tag 081T] uses are supplied by
> `AlgebraicGeometry.cartierBoundaryReduction` and
> `AlgebraicGeometry.strictTransformOpenImmersion_of_isIso_morphismRestrict`.

```lean
theorem exists_isAdmissibleBlowup_extending_section_of_qcqs [CompactSpace S]
    [QuasiSeparatedSpace S] (W : S.Opens) (U : W.toScheme.Opens) (hW : IsCompact (W : Set S))
    (hU : IsCompact (U : Set W.toScheme)) (f : X ⟶ W.toScheme) [IsProper f]
    (s : U.toScheme ⟶ X) (hs : s ≫ f = U.ι) :
    ∃ (S' : Scheme.{u}) (b : S' ⟶ S),
      Stacks.Blowup.IsAdmissibleBlowup (W.ι ''ᵁ U) b ∧
        ∃ s' : (b ⁻¹ᵁ W).toScheme ⟶ X,
          s' ≫ f = b ∣_ W ∧
            ∃ t : U.toScheme ⟶ (b ⁻¹ᵁ W).toScheme, t ≫ b ∣_ W = U.ι ∧ t ≫ s' = s
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.31, Tag 081Q](https://stacks.math.columbia.edu/tag/081Q)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
