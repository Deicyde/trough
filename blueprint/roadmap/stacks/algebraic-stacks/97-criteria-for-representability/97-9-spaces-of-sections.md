---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.isSurjective_restrictionOfScalars_projection_of_isPullback, AlgebraicGeometry.Space.exists_surjective_etale_sectionsOver, AlgebraicGeometry.Space.isSurjective_restrictionOfScalars_projection, AlgebraicGeometry.Space.exists_surjective_etale_sectionOverBase, AlgebraicGeometry.Space.isAlgebraicSpace_isEtale_restrictionOfScalars_of_isPullback, AlgebraicGeometry.Space.isAlgebraicSpace_restrictionOfScalars, AlgebraicGeometry.Space.isEtale_projection_restrictionOfScalars, AlgebraicGeometry.Space.exists_sectionSpace
statement: formalized
proof: formalized
---

# 97.9 Spaces of sections

Section 97.9 of the Stacks Project, [Tag 05XZ](https://stacks.math.columbia.edu/tag/05XZ). 2 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05XQ, a lemma

[Tag 05XQ](https://stacks.math.columbia.edu/tag/05XQ) in the Stacks Project.

**`AlgebraicGeometry.Space.isSurjective_restrictionOfScalars_projection_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ChartComparisonAssembly.lean, line 317](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/ChartComparisonAssembly.lean#L317). The attribute's comment: “surjectivity of `Res_{Z_U/U}(W) ⟶ U` for `Z_U` a base change of a finite locally free morphism of algebraic spaces”.

> **Stacks 05XQ for the fibre data of Stacks 05YD.**  Let `z : Z ⟶ Q` be a finite locally free
> morphism of algebraic spaces over `S`, let `U` be an object of the big fppf category over `S`,
> let `Z_U` be an algebraic space exhibited as a base change `U ×_{a, Q} Z` of `z`, and let
> `w : W ⟶ Z_U` be surjective and étale.  Then the restriction of scalars `Res_{Z_U/U}(W) ⟶ U` is
> surjective.
>
> Stacks 05XQ is formalized at a morphism of the site whose underlying morphism of schemes is finite,
> as `AlgebraicGeometry.Space.isSurjective_restrictionOfScalars_projection`.  Here `Z_U` is only
> *isomorphic* to a representable presheaf: `z` is affine, hence representable, so the chosen
> represented base change `ψ : Z' ⟶ U` of `z` along `a` identifies `Z_U` with `yoneda.obj Z'`, and
> `ψ` is finite as a morphism of schemes by
> `AlgebraicGeometry.Space.isFinite_of_isPullback_of_isFiniteLocallyFree`.  Transporting the
> section produced over `Z'` back along that identification gives a pair of Stacks 05Y9 over a
> surjective base change of `U`, which is what surjectivity of the projection asks for.

```lean
theorem isSurjective_restrictionOfScalars_projection_of_isPullback
    {Z Q : AlgebraicSpaces B S hS} (z : Z ⟶ Q) (hz : IsFiniteLocallyFree B S hS z)
    (U : BigFppfOver B S hS) (ZU W : AlgebraicSpaces B S hS)
    (ζ : ZU ⟶ (⟨yoneda.obj U, isAlgebraicSpace_yoneda B S hS U⟩ : AlgebraicSpaces B S hS))
    (w : W ⟶ ZU) (a : yoneda.obj U ⟶ Q.obj) (ι : ZU.obj ⟶ Z.obj)
    (sq : IsPullback ζ.hom ι a z.hom)
    (hw_surjective : IsSurjective B S hS w.hom) (hw_etale : IsEtale B S hS w.hom) :
    IsSurjective B S hS (restrictionOfScalars B S hS w ζ).projection
```

**`AlgebraicGeometry.Space.exists_surjective_etale_sectionsOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SectionSpaces.lean, line 331](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SectionSpaces.lean#L331).

> **Stacks 05XQ.** Let `Z → U` be a finite morphism of schemes, let `W` be an algebraic space
> over `U` and let `w : W → Z` be surjective and étale. Then there is a surjective étale morphism
> `T → U` together with a section of `W_T → Z_T`.

```lean
theorem Space.exists_surjective_etale_sectionsOver (B : BigFppfSite.{u}) (U : Scheme.{u})
    (hU : B.Contains U) (Z : BigFppfOver B U hU) [IsFinite (B.inclusion.map Z.hom)]
    (W : (BigFppfOver B U hU)ᵒᵖ ⥤ Type u) (w : W ⟶ yoneda.obj Z)
    (hW : IsAlgebraicSpace B U hU W) (hw_surjective : Space.IsSurjective B U hU w)
    (hw_etale : Space.IsEtale B U hU w) :
    ∃ T : BigFppfOver B U hU, Surjective (B.inclusion.map T.hom) ∧
      Etale (B.inclusion.map T.hom) ∧ Nonempty (Space.SectionsOver B U hU Z T W w)
```

**`AlgebraicGeometry.Space.isSurjective_restrictionOfScalars_projection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SectionSpaces.lean, line 468](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SectionSpaces.lean#L468). The attribute's comment: “surjectivity of `Res_{Z/U}(W) ⟶ U` for `Z ⟶ U` finite”.

> **Stacks 05XQ.** Let `ζ : Z ⟶ U` be a morphism of the big fppf site of `S` whose underlying
> morphism of schemes is finite, let `W` be an algebraic space over `S` and let `w : W ⟶ Z` be
> surjective and étale. Then the restriction of scalars `Res_{Z/U}(W) ⟶ U` of Stacks 05YA — the
> functor assigning to `T` a morphism `T ⟶ U` together with a section of `W_T ⟶ Z_T` — is
> surjective.
>
> A point of `U` is hit by a point of `Res_{Z/U}(W)` because the base change `τ : T ⟶ U` of
> `AlgebraicGeometry.Space.exists_surjective_etale_section_of_isFinite` carries a section, so
> `h_T ⟶ U` factors through `Res_{Z/U}(W)`, and `τ` is surjective on points.

```lean
theorem Space.isSurjective_restrictionOfScalars_projection (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) {U Z : BigFppfOver B S hS} (ζ : Z ⟶ U)
    [IsFinite ((BigFppfOver.toScheme B S hS).map ζ)] (W : AlgebraicSpaces B S hS)
    (w : W ⟶ (schemeSpace Z : AlgebraicSpaces B S hS))
    (hw_surjective : Space.IsSurjective B S hS w.hom)
    (hw_etale : Space.IsEtale B S hS w.hom) :
    Space.IsSurjective B S hS
      (Space.restrictionOfScalars B S hS w
        (ObjectProperty.homMk (yoneda.map ζ) :
          (schemeSpace Z : AlgebraicSpaces B S hS) ⟶
            schemeSpace U)).projection
```

**`AlgebraicGeometry.Space.exists_surjective_etale_sectionOverBase`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SectionSpacesOverBase.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SectionSpacesOverBase.lean#L90).

> **Stacks 05XQ over a base object of the site.** Let `ζ : Z ⟶ U` be a morphism of the big
> fppf site of `S` whose underlying morphism of schemes is finite, let `W` be an algebraic space
> over `S` and let `w : W ⟶ h_Z` be surjective and étale. Then there is an object `T` of the big
> fppf site of `S` and a morphism `r : T ⟶ U`, surjective and étale on underlying schemes,
> together with a section of `W ⟶ h_Z` over `T ×_U Z`, that is a morphism `h_{T ×_U Z} ⟶ W`
> whose composite with `w` is the projection to `h_Z`.

```lean
theorem Space.exists_surjective_etale_sectionOverBase (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (U Z : BigFppfOver B S hS) (ζ : Z ⟶ U)
    (hζ : IsFinite ((BigFppfOver.toScheme B S hS).map ζ))
    (W : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u) (w : W ⟶ yoneda.obj Z)
    (hW : IsAlgebraicSpace B S hS W) (hw_surjective : Space.IsSurjective B S hS w)
    (hw_etale : Space.IsEtale B S hS w) :
    ∃ (T : BigFppfOver B S hS) (r : T ⟶ U),
      Surjective ((BigFppfOver.toScheme B S hS).map r) ∧
      Etale ((BigFppfOver.toScheme B S hS).map r) ∧
      ∃ σ : pullback (yoneda.map r) (yoneda.map ζ) ⟶ W,
        σ ≫ w = pullback.snd (yoneda.map r) (yoneda.map ζ)
```

## Tag 05XR, a lemma

[Tag 05XR](https://stacks.math.columbia.edu/tag/05XR) in the Stacks Project.

**`AlgebraicGeometry.Space.isAlgebraicSpace_isEtale_restrictionOfScalars_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FibreSectionsAlgebraicEtale.lean, line 310](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/FibreSectionsAlgebraicEtale.lean#L310). The attribute's comment: “the restriction of scalars of a base change of a finite locally free morphism along an étale morphism is an algebraic space étale over the base”.

> **Stacks 05XR for the fibre data of Stacks 05YD and Stacks 05Y5.** Let `z : Z ⟶ Q` be a
> finite locally free morphism of algebraic spaces over `S`, let `U` be an object of the big fppf
> category over `S`, let `Z_U` be an algebraic space exhibited as a base change `U ×_{a, Q} Z` of
> `z` and let `w : W ⟶ Z_U` be an étale morphism of algebraic spaces over `S`. Then the restriction
> of scalars `Res_{Z_U/U}(W)` is an algebraic space over `S` and its projection to `U` is étale.

```lean
theorem isAlgebraicSpace_isEtale_restrictionOfScalars_of_isPullback
    {Z Q : AlgebraicSpaces B S hS} (z : Z ⟶ Q) (hz : IsFiniteLocallyFree B S hS z)
    (U : BigFppfOver B S hS) (ZU W : AlgebraicSpaces B S hS)
    (ζ : ZU ⟶ (schemeSpace U : AlgebraicSpaces B S hS))
    (w : W ⟶ ZU) (a : yoneda.obj U ⟶ Q.obj) (ι : ZU.obj ⟶ Z.obj)
    (sq : IsPullback ζ.hom ι a z.hom) (hw : IsEtale B S hS w.hom) :
    IsAlgebraicSpace B S hS (restrictionOfScalars B S hS w ζ).presheaf ∧
      IsEtale B S hS (restrictionOfScalars B S hS w ζ).projection
```

**`AlgebraicGeometry.Space.isAlgebraicSpace_restrictionOfScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IsFibreSectionsGeneral.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IsFibreSectionsGeneral.lean#L180). The attribute's comment: “algebraic space”.

> **Stacks 05XR, the algebraic space.** The restriction of scalars `Res_{Z/Q}(X)` of an étale
> `x : X ⟶ Z` along a finite `z : Z ⟶ Q` is an algebraic space over `S`.
>
> The source states this for `z` finite locally free and for `Q` an object of the site; finiteness
> of `z` is all that is used, and `Q` is an arbitrary algebraic space over `S`.

```lean
theorem isAlgebraicSpace_restrictionOfScalars (hx : IsEtale B S hS x.hom)
    (hz : IsFinite B S hS z.hom) :
    IsAlgebraicSpace B S hS (restrictionOfScalars B S hS x z).presheaf
```

**`AlgebraicGeometry.Space.isEtale_projection_restrictionOfScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/IsFibreSectionsGeneral.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/IsFibreSectionsGeneral.lean#L200). The attribute's comment: “étale morphism”.

> **Stacks 05XR, the étale morphism.** The projection `Res_{Z/Q}(X) ⟶ Q` of the restriction of
> scalars of an étale `x : X ⟶ Z` along a finite `z : Z ⟶ Q` is étale.
>
> The source states this for `z` finite locally free and for `Q` an object of the site; finiteness
> of `z` is all that is used, and `Q` is an arbitrary algebraic space over `S`.

```lean
theorem isEtale_projection_restrictionOfScalars (hx : IsEtale B S hS x.hom)
    (hz : IsFinite B S hS z.hom) :
    IsEtale B S hS (restrictionOfScalars B S hS x z).projection
```

**`AlgebraicGeometry.Space.exists_sectionSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SectionSpace.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SectionSpace.lean#L177). The attribute's comment: “the functor”.

> The natural, small-valued functor of sections of `W → Z` of Stacks 05XR exists: there
> is a presheaf on the big fppf site of `U` whose value at `T` is the set of sections of
> `W_T → Z_T`, naturally in `T`, the restriction maps being base change. Stacks 05XR itself is
> `AlgebraicGeometry.Space.isAlgebraicSpace_sectionSpace_and_isEtale`.

```lean
theorem exists_sectionSpace (Z : BigFppfOver B U hU)
    (W : (BigFppfOver B U hU)ᵒᵖ ⥤ Type u) (w : W ⟶ yoneda.obj Z) :
    ∃ F : (BigFppfOver B U hU)ᵒᵖ ⥤ Type u,
      ∃ e : ∀ T : BigFppfOver B U hU, F.obj (Opposite.op T) ≃
          SectionsOver B U hU Z T W w,
        ∀ (T T' : BigFppfOver B U hU) (f : T' ⟶ T)
          (s : F.obj (Opposite.op T)),
          ((e T') (F.map f.op s)).1 =
            prod.map (yoneda.map f) (𝟙 (yoneda.obj Z)) ≫ ((e T) s).1
```

**`AlgebraicGeometry.Space.isAlgebraicSpace_sectionSpace_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SectionSpaceChartSurjectiveEtale.lean, line 450](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SectionSpaceChartSurjectiveEtale.lean#L450). The attribute's comment: “the space of sections is an algebraic space, with no separatedness”.

> **Stacks 05XR, the algebraicity of the space of sections, in general.** Let `Z ⟶ U` be a
> morphism of the big fppf site of `U` whose underlying morphism of schemes is finite, and let
> `w : W ⟶ h_Z` be an étale morphism of presheaves with `W` an algebraic space over `U`. Then the
> space of sections of `W_T ⟶ Z_T` is an algebraic space over `U`.
>
> No separatedness is assumed: a surjective étale chart of `W` whose scheme is separated exists by
> Stacks 03FX, and along such a chart the comparison of the spaces of sections is surjective and
> étale by `AlgebraicGeometry.Space.isEtale_and_isSurjective_of_isPullback_sectionSpaceMap`.

```lean
theorem isAlgebraicSpace_sectionSpace_of_isEtale (hW : IsAlgebraicSpace B U hU W)
    (hw : IsEtale B U hU w)
    (hZfin : _root_.AlgebraicGeometry.IsFinite (B.inclusion.map Z.hom)) :
    IsAlgebraicSpace B U hU (sectionSpace B U hU Z W w)
```

**`AlgebraicGeometry.Space.isEtale_sectionSpace_of_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SectionSpaceChartSurjectiveEtale.lean, line 461](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SectionSpaceChartSurjectiveEtale.lean#L461). The attribute's comment: “the space of sections is étale over the base, with no separatedness”.

> **Stacks 05XR, the étaleness of the space of sections over the base, in general.** Under the
> hypotheses of `AlgebraicGeometry.Space.isAlgebraicSpace_sectionSpace_of_isEtale` the structure
> morphism of the space of sections to `U` is étale.

```lean
theorem isEtale_sectionSpace_of_isEtale (hW : IsAlgebraicSpace B U hU W)
    (hw : IsEtale B U hU w)
    (hZfin : _root_.AlgebraicGeometry.IsFinite (B.inclusion.map Z.hom)) :
    IsEtale B U hU (terminal.from (sectionSpace B U hU Z W w))
```

**`AlgebraicGeometry.Space.isAlgebraicSpace_sectionSpace_and_isEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SectionSpaceEtale.lean, line 618](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/SectionSpaceEtale.lean#L618).

> **Stacks 05XR.** Let `Z ⟶ U` be a finite morphism of schemes, let `W` be an algebraic space
> over `U` and let `w : W ⟶ Z` be étale. Then the functor of sections of `W_T ⟶ Z_T` over `T/U` is an
> algebraic space, and its structure morphism to `U` is étale.
>
> The source asks `Z ⟶ U` to be finite locally free; only finiteness is used.

```lean
theorem isAlgebraicSpace_sectionSpace_and_isEtale (hW : IsAlgebraicSpace B U hU W)
    (hw : IsEtale B U hU w) (hZfin : _root_.AlgebraicGeometry.IsFinite (B.inclusion.map Z.hom)) :
    IsAlgebraicSpace B U hU (sectionSpace B U hU Z W w) ∧
      IsEtale B U hU (terminal.from (sectionSpace B U hU Z W w))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 97.9, Tag 05XZ](https://stacks.math.columbia.edu/tag/05XZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
