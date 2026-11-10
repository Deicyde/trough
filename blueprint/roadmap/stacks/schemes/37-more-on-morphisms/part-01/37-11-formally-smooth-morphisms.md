---
declaration: section
origin: cited
lean: Stacks.Smooth.FormallySmoothScheme, AlgebraicGeometry.FormallySmooth.comp, AlgebraicGeometry.FormallySmooth.pullback_snd, AlgebraicGeometry.formallyEtale_iff_formallySmooth_and_formallyUnramified, AlgebraicGeometry.FormallySmooth.resLE, Stacks.Smooth.FormallySmooth.resLE, AlgebraicGeometry.formallySmooth_iff_appTop_formallySmooth, Stacks.Smooth.smooth_iff_locallyOfFinitePresentation_and_formallySmooth
statement: formalized
proof: formalized
---

# 37.11 Formally smooth morphisms

Section 37.11 of the Stacks Project, [Tag 02GZ](https://stacks.math.columbia.edu/tag/02GZ). 13 tags here are carried by 19 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 02H0, a definition

[Tag 02H0](https://stacks.math.columbia.edu/tag/02H0) in the Stacks Project.

**`Stacks.Smooth.FormallySmoothScheme`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Smooth/FormallySmoothScheme.lean, line 103](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Smooth/FormallySmoothScheme.lean#L103). References: EGA IV (17.1.1); SGA 3 XVII (5.7.1).

> A morphism of schemes `f : X ⟶ S` is **formally smooth** when it has the infinitesimal
> lifting property: for every first-order thickening `i : T ⟶ T'` of affine schemes, every
> commutative square
> ```
> T  --g--→ X
> |         |
> i         f
> ↓         ↓
> T' --h--→ S
> ```
> has a diagonal filler `g' : T' ⟶ X`, that is a morphism with `g' ≫ f = h` and `i ≫ g' = g`.

```lean
abbrev FormallySmoothScheme {X S : Scheme.{u}} (f : X ⟶ S) : Prop
```

## Tag 02H1, a lemma

[Tag 02H1](https://stacks.math.columbia.edu/tag/02H1) in the Stacks Project.

**`AlgebraicGeometry.FormallySmooth.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallySmooth/Basic.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallySmooth/Basic.lean#L60).

> A composition of formally smooth morphisms is formally smooth.

```lean
theorem FormallySmooth.comp {X Y S : Scheme.{u}} {f : X ⟶ Y} {g : Y ⟶ S}
    (hf : FormallySmooth f) (hg : FormallySmooth g) :
    FormallySmooth (f ≫ g)
```

## Tag 02H2, a lemma

[Tag 02H2](https://stacks.math.columbia.edu/tag/02H2) in the Stacks Project.

**`AlgebraicGeometry.FormallySmooth.pullback_snd`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallySmooth/Basic.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallySmooth/Basic.lean#L70).

> An arbitrary base change of a formally smooth morphism is formally smooth.

```lean
theorem FormallySmooth.pullback_snd {X S S' : Scheme.{u}} (f : X ⟶ S)
    (g : S' ⟶ S) (hf : FormallySmooth f) :
    FormallySmooth (pullback.snd f g)
```

## Tag 02HH, a lemma

[Tag 02HH](https://stacks.math.columbia.edu/tag/02HH) in the Stacks Project.

**`AlgebraicGeometry.formallyEtale_iff_formallySmooth_and_formallyUnramified`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/FormallyEtaleSmoothUnramified.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FormallyEtaleSmoothUnramified.lean#L46). References: EGA IV (17.1.1), “étale ⟺ smooth+unram”.

> A morphism of schemes is formally étale if and only if it is formally smooth and formally
> unramified.

```lean
theorem formallyEtale_iff_formallySmooth_and_formallyUnramified
    {X S : Scheme.{u}} (f : X ⟶ S) :
    FormallyEtale f ↔ (FormallySmooth f ∧ FormallyUnramified f)
```

## Tag 02H3, a lemma

[Tag 02H3](https://stacks.math.columbia.edu/tag/02H3) in the Stacks Project.

**`AlgebraicGeometry.FormallySmooth.resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallySmooth/Basic.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallySmooth/Basic.lean#L82).

> Formal smoothness is preserved by restriction to compatible open subschemes.

```lean
theorem FormallySmooth.resLE {X S : Scheme.{u}} {f : X ⟶ S}
    (hf : FormallySmooth f) (U : X.Opens) (V : S.Opens)
    (hUV : U ≤ f ⁻¹ᵁ V) :
    FormallySmooth (f.resLE V U hUV)
```

**`Stacks.Smooth.FormallySmooth.resLE`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Smooth/FormallySmoothCriterion.lean, line 208](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Smooth/FormallySmoothCriterion.lean#L208).

> **Stacks Project, Tag 02H3.** Formal smoothness passes to the restriction of a morphism to
> opens of the source and of the target. The point is that a first-order thickening of affine
> schemes is surjective on points, so a lift over the ambient morphism has the same image as the
> morphism it extends and therefore factors through the given open of the source.

```lean
theorem FormallySmooth.resLE {X S : Scheme.{u}} {f : X ⟶ S} (hf : FormallySmooth f)
    {U : S.Opens} {V : X.Opens} (e : V ≤ f ⁻¹ᵁ U) : FormallySmooth (f.resLE U V e)
```

## Tag 02H4, a lemma

[Tag 02H4](https://stacks.math.columbia.edu/tag/02H4) in the Stacks Project.

**`AlgebraicGeometry.formallySmooth_iff_appTop_formallySmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallySmooth/Basic.lean, line 92](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallySmooth/Basic.lean#L92).

> A morphism of affine schemes is formally smooth if and only if its map on global sections is
> formally smooth.

```lean
theorem formallySmooth_iff_appTop_formallySmooth
    {X S : Scheme.{u}} [IsAffine X] [IsAffine S] (f : X ⟶ S) :
    FormallySmooth f ↔ f.appTop.hom.FormallySmooth
```

## Tag 02H6, a lemma

[Tag 02H6](https://stacks.math.columbia.edu/tag/02H6) in the Stacks Project.

**`Stacks.Smooth.smooth_iff_locallyOfFinitePresentation_and_formallySmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Smooth/SmoothFormallySmoothTag.lean, line 684](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Smooth/SmoothFormallySmoothTag.lean#L684). References: EGA IV (17.3.2), “(ii) smooth”; EGA 0 (19.0.1); EGA IV (17.3.1); SGA 3 XI (1.1); SGA 3 XV (1.1), “more general”.

> **A scheme morphism is smooth exactly when it is locally of finite presentation and formally
> smooth.** This is the infinitesimal lifting criterion for smoothness.
>
> The implication from the right is `Stacks.Smooth.smooth_of_formallySmoothScheme`, and
> the implication to the right is `Stacks.Smooth.formallySmoothScheme_of_smooth` together with the
> fact that a smooth morphism is locally of finite presentation.

```lean
theorem smooth_iff_locallyOfFinitePresentation_and_formallySmooth {X S : Scheme.{u}}
    (f : X ⟶ S) :
    AlgebraicGeometry.Smooth f ↔
      (AlgebraicGeometry.LocallyOfFinitePresentation f ∧ FormallySmoothScheme f)
```

## Tag 06B5, a lemma

[Tag 06B5](https://stacks.math.columbia.edu/tag/06B5) in the Stacks Project.

**`AlgebraicGeometry.isLocallyProjective_relativeDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallySmooth/Differentials.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallySmooth/Differentials.lean#L78). References: EGA IV (17.2.3), “(i) locally projective”.

> **Stacks 06B5.** The sheaf of relative differentials of a formally smooth morphism of
> schemes is locally projective on its source. This is **Stacks 061I** for a morphism of
> algebraic spaces that is a morphism of schemes.

```lean
theorem isLocallyProjective_relativeDifferentials {X S : Scheme.{u}} {f : X ⟶ S}
    (hf : FormallySmooth f) :
    Scheme.Modules.IsLocallyProjective (Scheme.Hom.relativeDifferentials f)
```

## Tag 0D0E, a lemma

[Tag 0D0E](https://stacks.math.columbia.edu/tag/0D0E) in the Stacks Project.

**`Stacks.Cohomology.Affine.isZero_firstCohomology_sheafHom_of_isLocallyProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineCohomologyVanishing/InternalHom.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AffineCohomologyVanishing/InternalHom.lean#L168).

> **The first cohomology of an internal hom out of a locally projective module on an affine
> scheme vanishes.** The source is a retract of a free module, so the internal hom is a retract of
> the internal hom out of that free module, which is a product of copies of the target; the first
> cohomology of that product vanishes because the first cohomology of a quasi-coherent module on
> an affine scheme does.

```lean
theorem isZero_firstCohomology_sheafHom_of_isLocallyProjective (T : Scheme.{u}) [IsAffine T]
    (F G : T.Modules) [F.IsQuasicoherent] [G.IsQuasicoherent] (H : SheafHom T.sheaf F G)
    (hF : Scheme.Modules.IsLocallyProjective F) :
    IsZero (Hgroup T.ringCatSheaf ⊤ 1 H.obj)
```

## Tag 0D0F, a lemma

[Tag 0D0F](https://stacks.math.columbia.edu/tag/0D0F) in the Stacks Project.

**`Stacks.Smooth.formallySmooth_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Smooth/FormallySmoothTFAE.lean, line 833](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Smooth/FormallySmoothTFAE.lean#L833). The attribute's comment: “all four criteria, for an arbitrary morphism of schemes”.

> **[Stacks Project, Tag 0D0F].** For a morphism of schemes `f : X ⟶ Y` the following are
> equivalent: `f` is formally smooth; `f` is formally smooth on a neighbourhood of every point of
> `X`; the ring map `Γ(Y, V) ⟶ Γ(X, U)` is formally smooth for every pair of affine opens with
> `f(U) ⊆ V`; and there is one affine open covering of `Y` together with, over each of its
> members, an affine open covering of its inverse image, on whose charts those ring maps are
> formally smooth.
>
> The implications `1 → 3`, `1 → 2`, `3 → 4`, `4 → 2` and `2 → 3` are the formal manipulations of
> [Stacks Project, Tag 02H3] and the affine criterion [Stacks Project, Tag 02H4] together with the
> affine-locality of formal smoothness of ring maps. The remaining implication `3 → 1` is
> `Stacks.Smooth.formallySmooth_of_formallySmooth_appLE`, the torsor argument of the source, whose
> pseudo-torsor is `Stacks.Smooth.isLiftPseudoTorsor`.

```lean
theorem formallySmooth_tfae {X Y : Scheme.{u}} (f : X ⟶ Y) :
    List.TFAE
      [AlgebraicGeometry.FormallySmooth f,
        ∀ x : X, ∃ (U : X.Opens) (V : Y.Opens), x ∈ U ∧ f.base x ∈ V ∧
          ∃ hUV : U ≤ f ⁻¹ᵁ V, AlgebraicGeometry.FormallySmooth (f.resLE V U hUV),
        ∀ U : X.Opens, IsAffineOpen U → ∀ V : Y.Opens, IsAffineOpen V →
          ∀ hUV : U ≤ f ⁻¹ᵁ V, (f.appLE V U hUV).hom.FormallySmooth,
        ∃ (J : Type u) (V : J → Y.Opens), IsOpenCover V ∧ (∀ j, IsAffineOpen (V j)) ∧
          ∀ j, ∃ (I : Type u) (U : I → X.Opens) (hU : (⨆ i, U i) = f ⁻¹ᵁ V j),
            (∀ i, IsAffineOpen (U i)) ∧
              ∀ i, (f.appLE (V j) (U i) ((le_iSup U i).trans hU.le)).hom.FormallySmooth]
```

## Tag 06B6, a lemma

[Tag 06B6](https://stacks.math.columbia.edu/tag/06B6) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.toRelativeDifferentials_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/FormallySmooth.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/FormallySmooth.lean#L318). References: EGA IV (17.2.3).

> For morphisms of schemes `f : X ⟶ Y` and `g : Y ⟶ S` with `f` formally smooth, the canonical
> sequence `0 ⟶ f^* Ω_{Y/S} ⟶ Ω_{X/S} ⟶ Ω_{X/Y} ⟶ 0` of `𝒪_X`-modules is short exact. The case of a
> smooth `f` is the special case obtained from
> `Stacks.Smooth.smooth_iff_locallyOfFinitePresentation_and_formallySmooth`.

```lean
theorem toRelativeDifferentials_shortExact (f : X ⟶ Y) (g : Y ⟶ S) (hf : FormallySmooth f) :
    ∃ h : relativeDifferentialsMap f g (f ≫ g) (𝟙 S) (Category.comp_id (f ≫ g)).symm ≫
        f.toRelativeDifferentials g = 0,
      (ShortComplex.mk _ _ h).ShortExact
```

## Tag 06B7, a lemma

[Tag 06B7](https://stacks.math.columbia.edu/tag/06B7) in the Stacks Project.

**`Stacks.UnramifiedConormalSequence.exists_localRetraction_of_formallySmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallySmooth/UnramifiedConormalSequence.lean, line 145](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallySmooth/UnramifiedConormalSequence.lean#L145). The attribute's comment: “the step of the proof using formal smoothness of Z over S: locally on the universal first-order thickening Z' there is a left inverse Z' ⟶ Z over S”.

> **A local left inverse `Z' ⟶ Z` over `S`, from formal smoothness of `Z` over `S`.** Let
> `i : Z ⟶ Z'` with structure morphism `h' : Z' ⟶ X` be a universal first-order thickening of
> `h : Z ⟶ X`, let `p : X ⟶ S`, and assume `Z` is formally smooth over `S`, that is
> `h ≫ p : Z ⟶ S` has the lifting property of [Stacks, Tag 02H0]. Then every point `z` of `Z` has
> an open neighbourhood `V` and an open `W ⊆ Z'` such that `i` restricts to `j : V ⟶ W` and `j`
> admits a left inverse `g : W ⟶ V` over `S`.
>
> This is the step of the proof of [Stacks, Tag 06B7] reading "by formal smoothness of `Z` over `S`
> there exists, after replacing `Z'` by an open neighbourhood, a left inverse `Z' ⟶ Z` over `S`".
> `V` is any affine open neighbourhood of `z` and `W` is the open of `Z'` attached to it by
> `Stacks.Thickenings.UniversalFirstOrderThickening.ambientOpens`, which is affine because
> `V ⟶ W` is a first-order thickening of `V`; the lifting property applies to that affine
> first-order thickening, and the resulting lift `W ⟶ Z` factors through `V` because `V ⟶ W` is
> surjective on points.

```lean
theorem exists_localRetraction_of_formallySmooth {Z' : Scheme.{u}} {h : Z ⟶ X} {i : Z ⟶ Z'}
    {h' : Z' ⟶ X} (hi : Stacks.Thickenings.IsUniversalFirstOrderThickening h i h') (p : X ⟶ S)
    (hZ : FormallySmooth (h ≫ p)) (z : Z) :
    ∃ (V : Z.Opens) (W : Z'.Opens) (j : V.toScheme ⟶ W.toScheme)
      (g : W.toScheme ⟶ V.toScheme), z ∈ V ∧ V.ι ≫ i = j ≫ W.ι ∧
        j ≫ g = 𝟙 V.toScheme ∧ g ≫ (V.ι ≫ (h ≫ p)) = W.ι ≫ (h' ≫ p)
```

**`Stacks.UnramifiedConormalSequence.forall_exists_isSplitEpi_restrict_relativeDifferentialsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallySmooth/UnramifiedConormalSequence.lean, line 251](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallySmooth/UnramifiedConormalSequence.lean#L251). The attribute's comment: “the conclusion of the source's proof before Tag 0474 is invoked: the sequence is locally split, i.e. the second arrow h^*Ω\_\{X/S} ⟶ Ω\_\{Z/S} restricts to a split epimorphism on a neighbourhood of every point of Z. Left exactness, the assertion of the tag, is not this declaration: it is conormalShortComplex\_shortExact of StacksFrontier.AlgebraicGeometry.MoreMorphisms.FormallySmooth.UnramifiedConormalShortExact”.

> **[Stacks, Tag 06B7]: the conormal sequence of a formally unramified morphism with formally
> smooth source is locally split.** Let `h : Z ⟶ X` be formally unramified, let `p : X ⟶ S`, and
> assume `Z` is formally smooth over `S`. Then the second arrow `h^*Ω_{X/S} ⟶ Ω_{Z/S}` of the
> sequence of [Stacks, Tag 04FC] — the canonical map of [Stacks, Tag 01UV] — restricts to a *split*
> epimorphism on a neighbourhood of every point of `Z`.
>
> A split epimorphism being an epimorphism, this contains local surjectivity of that arrow, which
> [Stacks, Tag 01UZ] supplies only for a morphism surjective on stalks; splitness is what formal
> smoothness buys, and it is the source's "hence the sequence is locally split". Left exactness of
> the sequence, which is the assertion of the tag, is not proved here; it is
> `Stacks.UnramifiedConormalSequence.conormalShortComplex_shortExact` in
> `StacksFrontier.AlgebraicGeometry.MoreMorphisms.FormallySmooth.UnramifiedConormalShortExact`.

```lean
theorem forall_exists_isSplitEpi_restrict_relativeDifferentialsMap (h : Z ⟶ X)
    [FormallyUnramified h] (p : X ⟶ S) (hZ : FormallySmooth (h ≫ p)) (z : Z) :
    ∃ V : Z.Opens, z ∈ V ∧ IsSplitEpi ((Scheme.Modules.pullback V.ι).map
      (relativeDifferentialsMap h p (h ≫ p) (𝟙 S)
        (show h ≫ p = (h ≫ p) ≫ 𝟙 S by simp)))
```

**`Stacks.UnramifiedConormalSequence.conormalShortComplex_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallySmooth/UnramifiedConormalShortExact.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallySmooth/UnramifiedConormalShortExact.lean#L318). References: EGA IV (17.2.5), “more general”; SGA 7 XI (1.3), “partial”; SGA 7 XVII (5.1), “more general”.

> Let `h : Z ⟶ X` be a formally unramified morphism of schemes over `p : X ⟶ S` and assume
> `Z` is formally smooth over `S`. Then the canonical sequence
>
> ```
> 0 ⟶ 𝒞_{Z/X} ⟶ h^*Ω_{X/S} ⟶ Ω_{Z/S} ⟶ 0
> ```
>
> is short exact: the first arrow is a monomorphism, the sequence is exact at `h^*Ω_{X/S}`, and the
> second arrow is an epimorphism. Here `𝒞_{Z/X}` is the conormal sheaf of the inclusion of `Z`
> into the universal first-order thickening of `Z` over `X`.

```lean
theorem conormalShortComplex_shortExact
    (hZ : AlgebraicGeometry.FormallySmooth (h ≫ p)) :
    (conormalShortComplex h p).ShortExact
```

## Tag 067W, a lemma

[Tag 067W](https://stacks.math.columbia.edu/tag/067W) in the Stacks Project.

**`Stacks.ConormalSequenceUnramifiedPair.exists_retraction_restrict_universalConormalTransitivityMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairSplitConormalSequence.lean, line 360](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairSplitConormalSequence.lean#L360). The attribute's comment: “locally split, in the sense the source's proof produces and its final sentence defines: every point of Z has an open neighbourhood over which the first arrow 𝒞\_\{Z/Y} ⟶ 𝒞\_\{Z/X} of Tag 067V admits a retraction”.

> **[Stacks, Tag 067W]: the conormal sequence is locally split.** For formally unramified
> `i : Z ⟶ X` and `j : Z ⟶ Y` in a commutative triangle `i ≫ p = j` with `p` formally smooth, every
> point of `Z` has an open neighbourhood `V` over which the first arrow `𝒞_{Z/Y} ⟶ 𝒞_{Z/X}` of
> [Stacks, Tag 067V] admits a retraction.

```lean
theorem exists_retraction_restrict_universalConormalTransitivityMap (h : i ≫ p = j)
    (hp : FormallySmooth p) (z : Z) :
    ∃ V : Z.Opens, z ∈ V ∧
      ∃ r : (Scheme.Modules.restrictFunctor V.ι).obj (universalConormalSheaf i) ⟶
          (Scheme.Modules.restrictFunctor V.ι).obj (universalConormalSheaf j),
        (Scheme.Modules.restrictFunctor V.ι).map (universalConormalTransitivityMap i j p h) ≫ r =
          𝟙 _
```

**`Stacks.ConormalSequenceUnramifiedPair.mono_conormalSequenceFirstArrow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairSplitConormalSequence.lean, line 462](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairSplitConormalSequence.lean#L462). The attribute's comment: “exact on the left: the first arrow 𝒞\_\{Z/Y} ⟶ 𝒞\_\{Z/X} of Tag 067V is a monomorphism, which is the only strengthening of Tag 067V's right-exact sequence to a short exact one that this tag asserts; obtained from the local splitting”.

> **[Stacks, Tag 067W]: the first arrow of the conormal sequence is a monomorphism.** This is
> the `0 ⟶` at the left-hand end of the sequence, and the only strengthening of the right-exact
> sequence of [Stacks, Tag 067V] to a short exact one.

```lean
theorem mono_conormalSequenceFirstArrow (h : i ≫ p = j) (hp : FormallySmooth p) :
    Mono (conormalSequenceFirstArrow i j p h)
```

**`Stacks.ConormalSequenceUnramifiedPair.exists_retraction_restrict_conormalSequenceFirstArrow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairSplitConormalSequence.lean, line 478](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairSplitConormalSequence.lean#L478). The attribute's comment: “locally split, in the shape of the locallySplit clause the library uses for the sibling tag 062S”.

> **The local splitting, stated for
> `Stacks.ConormalSequenceUnramifiedPair.conormalSequenceFirstArrow`.** This is the `locallySplit`
> clause in the shape the library uses for the sibling tag [Stacks, Tag 062S], namely
> `Stacks.AlgebraicGeometry.IsSplitExactConormalSequence.locallySplit`.

```lean
theorem exists_retraction_restrict_conormalSequenceFirstArrow (h : i ≫ p = j)
    (hp : FormallySmooth p) (z : Z) :
    ∃ V : Z.Opens, z ∈ V ∧
      ∃ r : (Scheme.Modules.restrictFunctor V.ι).obj (conormalSheafModules i) ⟶
          (Scheme.Modules.restrictFunctor V.ι).obj (conormalSheafModules j),
        (Scheme.Modules.restrictFunctor V.ι).map (conormalSequenceFirstArrow i j p h) ≫ r =
          𝟙 _
```

**`Stacks.ConormalSequenceUnramifiedPair.shortExact_of_comp_eq_zero_of_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairSplitConormalSequence.lean, line 1130](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairSplitConormalSequence.lean#L1130). The attribute's comment: “the sequence of Tag 067V is short exact: exactness at the middle term and surjectivity of the second arrow are the assertions of Tag 067V, and injectivity of the first arrow is what this tag adds, by way of the local splitting its proof produces”.

> **[Stacks, Tag 067W]: the conormal sequence is short exact.** For formally unramified
> `i : Z ⟶ X` and `j : Z ⟶ Y` in a commutative triangle `i ≫ p = j` with `p` formally smooth, the
> sequence `0 ⟶ 𝒞_{Z/Y} ⟶ 𝒞_{Z/X} ⟶ i^*Ω_{X/Y} ⟶ 0` of [Stacks, Tag 067V] is short exact.
>
> Exactness at the middle term and surjectivity of the second arrow are the assertions of
> [Stacks, Tag 067V]; what this tag adds is injectivity of the first arrow.

```lean
theorem shortExact_of_comp_eq_zero_of_exact (h : i ≫ p = j) (hp : FormallySmooth p) :
    (ShortComplex.mk _ _ (conormalSequenceComp_eq_zero i j p h)).ShortExact
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.11, Tag 02GZ](https://stacks.math.columbia.edu/tag/02GZ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
