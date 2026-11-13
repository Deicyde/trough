---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.presheaf_isQuasiAffineHom_iff, AlgebraicGeometry.Space.IsQuasiAffineHom, AlgebraicGeometry.Space.isQuasiAffineHom_tfae_etaleChart_of_isAlgebraicSpace, AlgebraicGeometry.Space.IsQuasiAffineHom.comp, AlgebraicGeometry.Space.IsQuasiAffineHom.of_isPullback, AlgebraicGeometry.Space.isQuasiAffineHom_iff_isOpenImmersion_overHomOfPushforwardAlgebraIso, AlgebraicGeometry.Space.isQuasiAffineHom_iff_isOpenImmersion_toDirectImageSpec, AlgebraicGeometry.Space.isQuasiAffineHom_of_isOpenImmersion_qcqsDirectImageFactorizationMap
statement: formalized
proof: formalized
---

# 67.21 Quasi-affine morphisms

Section 67.21 of the Stacks Project, [Tag 03WJ](https://stacks.math.columbia.edu/tag/03WJ). 6 tags here are carried by 9 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03WK, a lemma

[Tag 03WK](https://stacks.math.columbia.edu/tag/03WK) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.presheaf_isQuasiAffineHom_iff`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiAffineRepresentable.lean#L214), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiAffineComposition.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiAffineComposition.lean#L52) (StacksFrontier): “representable case: 03HA-quasi-affine iff affine base changes are quasi-affine”.

## Tag 03WL, a definition

[Tag 03WL](https://stacks.math.columbia.edu/tag/03WL) in the Stacks Project.

**`AlgebraicGeometry.Space.IsQuasiAffineHom`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiAffine.lean, line 47](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiAffine.lean#L47).

> A morphism of algebraic spaces is quasi-affine if each of its base changes to an affine scheme
> is represented by a quasi-affine scheme.

```lean
abbrev IsQuasiAffineHom (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y) : Prop
```

## Tag 03WM, a lemma

[Tag 03WM](https://stacks.math.columbia.edu/tag/03WM) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiAffineHom_tfae_etaleChart_of_isAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiAffineTfaeComplete.lean, line 104](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiAffineTfaeComplete.lean#L104).

> For a morphism `f : X ⟶ Y` of algebraic spaces over a scheme `S` the following four conditions
> are equivalent: `f` is relatively representable and all of its represented base changes are
> quasi-affine morphisms of schemes; `f` is quasi-affine in the sense of Stacks 03WL; the base
> change of `f` along some surjective étale scheme chart of `Y` is quasi-affine; and there is a
> Zariski covering of `Y` over whose members `f` is quasi-affine.

```lean
theorem isQuasiAffineHom_tfae_etaleChart_of_isAlgebraicSpace
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    List.TFAE [
      (MorphismProperty.presheaf (MorphismProperty.inverseImage
        (@_root_.AlgebraicGeometry.IsQuasiAffineHom.{u} : MorphismProperty Scheme.{u})
        (BigFppfOver.toScheme B S hS))) f,
      IsQuasiAffineHom B S hS f,
      (∃ (V : BigFppfOver B S hS) (g : yoneda.obj V ⟶ Y),
        (MorphismProperty.presheaf (MorphismProperty.inverseImage
          (@Surjective.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS))) g ∧
        (MorphismProperty.presheaf (MorphismProperty.inverseImage
          (@Etale.{u} : MorphismProperty Scheme.{u})
          (BigFppfOver.toScheme B S hS))) g ∧
        IsQuasiAffineHom B S hS (pullback.fst g f)),
      (∃ (I : Type u) (U : I → Subfunctor Y),
        IsZariskiCover B S hS I U ∧
        ∀ i, IsQuasiAffineHom B S hS (pullback.fst (U i).ι f))
    ]
```

## Tag 03WN, a lemma

[Tag 03WN](https://stacks.math.columbia.edu/tag/03WN) in the Stacks Project.

**`AlgebraicGeometry.Space.IsQuasiAffineHom.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiAffineComposition.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiAffineComposition.lean#L38).

> The composite of two quasi-affine morphisms of algebraic spaces over a
> scheme `S` is quasi-affine.

```lean
theorem IsQuasiAffineHom.comp {B : BigFppfSite.{u}} {S : Scheme.{u}} {hS : B.Contains S}
    {X Y Z : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (hZ : IsAlgebraicSpace B S hS Z) {f : X ⟶ Y} {g : Y ⟶ Z}
    (hf : IsQuasiAffineHom B S hS f) (hg : IsQuasiAffineHom B S hS g) :
    IsQuasiAffineHom B S hS (f ≫ g)
```

## Tag 03WO, a lemma

[Tag 03WO](https://stacks.math.columbia.edu/tag/03WO) in the Stacks Project.

**`AlgebraicGeometry.Space.IsQuasiAffineHom.of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiAffineTfae.lean, line 102](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiAffineTfae.lean#L102).

> Quasi-affineness of a morphism of algebraic spaces over `S` is stable under base change: if
> `f'` sits in a Cartesian square over `f`, then `f'` is quasi-affine as soon as `f` is.

```lean
theorem IsQuasiAffineHom.of_isPullback {X' Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    {f : X ⟶ Y} {g : Y' ⟶ Y} {k : X' ⟶ X} {f' : X' ⟶ Y'} (sq : IsPullback k f' f g)
    (hf : IsQuasiAffineHom B S hS f) : IsQuasiAffineHom B S hS f'
```

## Tag 086S, a lemma

[Tag 086S](https://stacks.math.columbia.edu/tag/086S) in the Stacks Project.

**`AlgebraicGeometry.Space.isQuasiAffineHom_iff_isOpenImmersion_overHomOfPushforwardAlgebraIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiAffineCanonicalFactorization.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiAffineCanonicalFactorization.lean#L71). The attribute's comment: “for every algebraic space P affine over X with an identification e of its direct-image algebra with f\_* O\_Y, i.e. every relative spectrum of f\_* O\_Y: a quasi-compact f is quasi-affine iff the canonical morphism Y ⟶ P over X of 081X attached to e is an open immersion; quasi-separatedness of f is not needed once P and e are given”.

> **Stacks 086S.**  Let `f : Y ⟶ X` be a quasi-compact morphism of algebraic spaces over `S`,
> let `P` be an algebraic space affine over `X`, and let `e : P_* 𝒪_P ≅ f_* 𝒪_Y` identify its
> direct-image algebra with that of `f`, so that `P` is the relative spectrum
> `\underline{Spec}_X(f_* 𝒪_Y)`.  Then `f` is quasi-affine if and only if the canonical morphism
> `Y ⟶ P` over `X` of Stacks 081X attached to `e` is an open immersion.

```lean
theorem isQuasiAffineHom_iff_isOpenImmersion_overHomOfPushforwardAlgebraIso
    {X Y : AlgebraicSpaces B S hS} (f : Y ⟶ X) (hfqc : IsQuasiCompact B S hS f.hom)
    (P : AffineOver B S hS X)
    (e : pushforwardAlgebra B S hS P.obj ≅ pushforwardAlgebra B S hS (Over.mk f)) :
    IsQuasiAffineHom B S hS f.hom ↔
      IsOpenImmersion B S hS (overHomOfPushforwardAlgebraIso B S hS e).left.hom
```

**`AlgebraicGeometry.Space.isQuasiAffineHom_iff_isOpenImmersion_toDirectImageSpec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiAffineCanonicalFactorization.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiAffineCanonicalFactorization.lean#L96). The attribute's comment: “corrected (bounded) form: Spec\_X(f\_* O\_Y) is directImageSpec f, the relative spectrum of 081W in its bounded form (the unbounded 081V is refuted by not\_nonempty\_affineAlgebraAntiEquivalence\_of\_hasNonzeroAffineChart), whose size condition on f\_* O\_Y is proved; the morphism is toDirectImageSpec f, the canonical factorization of 081X; hypotheses exactly f quasi-compact and quasi-separated”.

> **Stacks 086S, in the corrected (bounded) form.**  A quasi-compact, quasi-separated morphism
> `f : Y ⟶ X` of algebraic spaces over `S` is quasi-affine if and only if its canonical
> factorization `Y ⟶ \underline{Spec}_X(f_* 𝒪_Y)` of Stacks 081X is an open immersion.
>
> The relative spectrum is `AlgebraicGeometry.Space.directImageSpec`, Stacks 081W in its corrected
> form: the relative spectrum of a quasi-coherent algebra whose sections over every chart number
> fewer than the cutoff of the site.  The unbounded form of 081V that the source's
> `\underline{Spec}_X` presupposes is refuted in this development by
> `AlgebraicGeometry.Space.not_nonempty_affineAlgebraAntiEquivalence_of_hasNonzeroAffineChart`.
> The size condition on `f_* 𝒪_Y` is proved, not assumed
> (`AlgebraicGeometry.Space.sectionsBelowCutoff_pushforwardAlgebra`), so the hypotheses are exactly
> those of the source.

```lean
theorem isQuasiAffineHom_iff_isOpenImmersion_toDirectImageSpec {X Y : AlgebraicSpaces B S hS}
    (f : Y ⟶ X) (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom) :
    IsQuasiAffineHom B S hS f.hom ↔
      IsOpenImmersion B S hS (toDirectImageSpec B S hS f hfqc hfqs).left.hom
```

**`AlgebraicGeometry.Space.isQuasiAffineHom_of_isOpenImmersion_qcqsDirectImageFactorizationMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiAffineDirectImageFactorization.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiAffineDirectImageFactorization.lean#L113). The attribute's comment: “proves only: the factorization is an open immersion implies f is quasi-affine”.

> A quasi-compact, quasi-separated morphism `f : Y ⟶ X` of algebraic spaces over `S` whose
> canonical morphism `Y ⟶ \underline{Spec}_X(f_* 𝒪_Y)` is an open immersion is quasi-affine.

```lean
theorem isQuasiAffineHom_of_isOpenImmersion_qcqsDirectImageFactorizationMap (f : Y ⟶ X)
    (hfqc : IsQuasiCompact B S hS f.hom) (hfqs : IsQuasiSeparated B S hS f.hom)
    (hoi : IsOpenImmersion B S hS
      (qcqsDirectImageFactorizationMap B S hS E C f hfqc hfqs
        fun hqc hqs => isQuasicoherentOnSite_modulePushforward_of_qcqs B S hS f hqc hqs).left.hom) :
    IsQuasiAffineHom B S hS f.hom
```

**`AlgebraicGeometry.Space.isQuasiAffineHom_iff_isOpenImmersion_affineOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiAffineOpenImmersionAffineOver.lean, line 431](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiAffineOpenImmersionAffineOver.lean#L431). The attribute's comment: “both directions, for every P affine over X by p and every g : Y ⟶ P over X whose map on direct-image algebras p\_* O\_P ⟶ f\_* O\_Y is an isomorphism: a quasi-compact f is quasi-affine iff g is an open immersion; this is the general form, and the canonical morphism of 081X is one such g”.

> Let `f : Y ⟶ X` be a quasi-compact morphism of algebraic spaces over `S`, let `P` be an
> algebraic space affine over `X` by `p`, and let `g : Y ⟶ P` be a morphism over `X` whose map on
> direct-image algebras `p_* 𝒪_P ⟶ f_* 𝒪_Y` is an isomorphism. Then `f` is quasi-affine if and only
> if `g` is an open immersion.

```lean
theorem isQuasiAffineHom_iff_isOpenImmersion_affineOver {X Y : AlgebraicSpaces B S hS} (f : Y ⟶ X)
    (hfqc : IsQuasiCompact B S hS f.hom) (P : AffineOver B S hS X) (g : Over.mk f ⟶ P.obj)
    (hring : IsIso (pushforwardRingMap B S hS g)) :
    IsQuasiAffineHom B S hS f.hom ↔ IsOpenImmersion B S hS g.left.hom
```

**`AlgebraicGeometry.Space.isQuasiAffineHom_of_isOpenImmersion_qcqsDirectImageFactorizationMap_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/QuasiAffineOpenImmersionAffineOver.lean, line 455](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Spaces/QuasiAffineOpenImmersionAffineOver.lean#L455). The attribute's comment: “proves only: the factorization is an open immersion implies f is quasi-affine — and presupposes AffineAlgebraAntiEquivalence, which this development proves uninhabited (not\_nonempty\_affineAlgebraAntiEquivalence\_of\_hasNonzeroAffineChart), so the statement is vacuous; the non-vacuous form is isQuasiAffineHom\_of\_isOpenImmersion\_boundedRelativeSpecDirectImage”.

> A quasi-compact, quasi-separated morphism `f : Y ⟶ X` of algebraic spaces over `S` whose
> canonical morphism `Y ⟶ \underline{Spec}_X(f_* 𝒪_Y)` of Stacks 081X is an open immersion is
> quasi-affine.
>
> The hypothesis `E` is an inhabitant of `AlgebraicGeometry.Space.AffineAlgebraAntiEquivalence`,
> which `AlgebraicGeometry.Space.not_nonempty_affineAlgebraAntiEquivalence_of_hasNonzeroAffineChart`
> proves uninhabited, so the statement is vacuous.

```lean
theorem isQuasiAffineHom_of_isOpenImmersion_qcqsDirectImageFactorizationMap_unconditional
    (f : Y ⟶ X) (hfqc : IsQuasiCompact B S hS f.hom)
    (hfqs : IsQuasiSeparated B S hS f.hom)
    (hoi : IsOpenImmersion B S hS
      (qcqsDirectImageFactorizationMap_unconditional B S hS E C f hfqc hfqs).left.hom) :
    IsQuasiAffineHom B S hS f.hom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.21, Tag 03WJ](https://stacks.math.columbia.edu/tag/03WJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
