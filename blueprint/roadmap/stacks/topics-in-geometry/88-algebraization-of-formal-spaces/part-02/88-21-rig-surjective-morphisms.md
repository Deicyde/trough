---
declaration: section
origin: cited
lean: AlgebraicGeometry.FormalSpace.IsRigSurjective, AlgebraicGeometry.FormalSpace.FractionalPowers.noAdicPoints_isRigSurjective_isDomain, AlgebraicGeometry.FormalSpace.IsRigSurjective.comp, AlgebraicGeometry.FormalSpace.IsRigSurjective.comp_of_isFormalAlgebraicSpace, AlgebraicGeometry.FormalSpace.IsRigSurjective.of_isPullback, AlgebraicGeometry.FormalSpace.hasRigSurjectiveOnPullbackCharts_of_isRigSurjective, AlgebraicGeometry.FormalSpace.IsRigSurjective.of_isPullback_of_representable, AlgebraicGeometry.FormalSpace.IsRigSurjective.of_comp_of_mono
statement: formalized
proof: formalized
---

# 88.21 Rig-surjective morphisms

Section 88.21 of the Stacks Project, [Tag 0AQP](https://stacks.math.columbia.edu/tag/0AQP). 14 tags here are carried by 23 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0AQQ, a definition

[Tag 0AQQ](https://stacks.math.columbia.edu/tag/0AQQ) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsRigSurjective`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjective.lean, line 116](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjective.lean#L116).

> **Stacks 0AQQ.** A morphism `f : X ⟶ Y` of fppf sheaves on the big fppf site of `S` is
> *rig-surjective* when every adic morphism `p : Spf R ⟶ Y` out of the formal spectrum of a
> complete discrete valuation ring `R` lifts to `X` along the formal spectrum of an extension
> `R ⊂ R'` of complete discrete valuation rings. Adic means representable by algebraic spaces,
> which is the definition of an adic morphism, Stacks 0AQ3.
>
> The source defines the notion for a morphism of locally Noetherian formal algebraic spaces that
> is locally of finite type. The predicate drops those standing hypotheses and asks for the same
> lifting condition for any morphism of fppf sheaves. Under them it is the source's definition.

```lean
abbrev IsRigSurjective (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y) : Prop
```

## Tag 0AQZ, a remark

[Tag 0AQZ](https://stacks.math.columbia.edu/tag/0AQZ) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.FractionalPowers.noAdicPoints_isRigSurjective_isDomain`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/NoAdicDiscreteValuationPointsRigSurjective.lean, line 212](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/NoAdicDiscreteValuationPointsRigSurjective.lean#L212).

> **Stacks 0AQZ.** Let `A = (⋃_{n ≥ 1} k[t^{1/n}])^∧` be the `t`-adic completion of the ring
> of polynomials in the fractional powers of `t` over a field `k`, carrying its `t`-adic topology.
> There are no adic morphisms `Spf R ⟶ Spf A` with `R` a complete discrete valuation ring; thus
> every morphism `X ⟶ Spf A` is rig-surjective; and yet `A` is a domain and `t ∈ A` is not zero.

```lean
theorem noAdicPoints_isRigSurjective_isDomain [TopologicalSpace (Completion k)]
    (hA : _root_.IsAdic (Ideal.span {completionGenerator k}))
    (D : QuotientSystem B S hS (Completion k)) :
    (∀ (R : Type u) [CommRing R] [IsDomain R] [IsDiscreteValuationRing R] [TopologicalSpace R],
      _root_.IsAdic (IsLocalRing.maximalIdeal R) →
        IsAdicComplete (IsLocalRing.maximalIdeal R) R →
          ∀ (E : QuotientSystem B S hS R) (p : formalSpectrum E ⟶ formalSpectrum D),
            ¬ Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS p.hom) ∧
      (∀ {X : FppfSheaf B S hS} (f : X ⟶ formalSpectrum D), IsRigSurjective B S hS f) ∧
      IsDomain (Completion k) ∧ completionGenerator k ≠ 0
```

## Tag 0AQR, a lemma

[Tag 0AQR](https://stacks.math.columbia.edu/tag/0AQR) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsRigSurjective.comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjective.lean, line 171](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjective.lean#L171). The attribute's comment: “assuming Stacks 0AN5 and, for the second factor, Stacks 0AQ0”.

> **Stacks 0AQR**, carrying two hypotheses. A composite of rig-surjective morphisms of formal
> algebraic spaces over `S` which are locally of finite type is locally of finite type and
> rig-surjective: an adic point of the final target lifts through the second factor over an
> extension of complete discrete valuation rings, that lift is again adic, and so lifts through
> the first factor over a further extension; the two extensions compose to one.
>
> Adicness of the intermediate lift is `hcancel`, which is **Stacks 0AQ0** for the second factor,
> applied to the composite made representable by `hformalSpectrumMap`, which is **Stacks 0AN5**,
> (3) implies (1); neither is available in this library.

```lean
theorem IsRigSurjective.comp (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : IsLocallyOfFiniteType B S hS f) (hg : IsLocallyOfFiniteType B S hS g)
    (hformalSpectrumMap : ∀ (A₁ A₂ : Type u) [CommRing A₁] [TopologicalSpace A₁]
      [IsTopologicalRing A₁] [IsLinearTopology A₁ A₁] [CommRing A₂] [TopologicalSpace A₂]
      [IsTopologicalRing A₂] (hA₁ : TopologicalRing.IsWeaklyAdmissible A₁)
      (D₁ : QuotientSystem B S hS A₁) (D₂ : QuotientSystem B S hS A₂)
      (φ : ContinuousHom D₁ D₂), RingHom.IsTaut φ.toRingHom →
      Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS (formalSpectrumMap hA₁ φ).hom)
    (hcancel : ∀ {W : FppfSheaf B S hS} (q : W ⟶ Y),
      Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS (q.hom ≫ g.hom) →
      Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS q.hom)
    (hsf : IsRigSurjective B S hS f) (hsg : IsRigSurjective B S hS g) :
    IsLocallyOfFiniteType B S hS (f ≫ g) ∧ IsRigSurjective B S hS (f ≫ g)
```

**`AlgebraicGeometry.FormalSpace.IsRigSurjective.comp_of_isFormalAlgebraicSpace`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveComposition.lean, line 150](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveComposition.lean#L150).

> **Stacks 0AQR.** A composite of rig-surjective morphisms of formal algebraic spaces over `S`
> which are locally of finite type is locally of finite type and rig-surjective: an adic point of
> the final target lifts through the second factor over an extension of complete discrete
> valuation rings, that lift is again adic, and so lifts through the first factor over a further
> extension; the two extensions compose to one.
>
> Adicness of the intermediate lift is Stacks 0AQ0 for the second factor, applied to the
> composite made representable by the implication (3) ⟹ (1) of Stacks 0AN5. The hypothesis `hY`
> is what Stacks 0AQ0 asks of the source of the second factor, and the source of Stacks 0AQR
> assumes it of `Y` in the stronger form of a locally Noetherian formal algebraic space.

```lean
theorem IsRigSurjective.comp_of_isFormalAlgebraicSpace
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hY : IsFormalAlgebraicSpace B S hS Y)
    (hf : IsLocallyOfFiniteType B S hS f) (hg : IsLocallyOfFiniteType B S hS g)
    (hsf : IsRigSurjective B S hS f) (hsg : IsRigSurjective B S hS g) :
    IsLocallyOfFiniteType B S hS (f ≫ g) ∧ IsRigSurjective B S hS (f ≫ g)
```

## Tag 0AQS, a lemma

[Tag 0AQS](https://stacks.math.columbia.edu/tag/0AQS) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsRigSurjective.of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveBaseChange.lean, line 80](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveBaseChange.lean#L80).

> **Stacks 0AQS.** Let `f : X ⟶ Y` and `g : Z ⟶ Y` be morphisms of formal algebraic spaces
> over `S` which are locally of finite type. A base change `p : W ⟶ Z` of `f` along `g` is
> locally of finite type, and is rig-surjective as soon as `f` is.
>
> An adic point of `Z` out of the formal spectrum of a complete discrete valuation ring becomes,
> after composition with `g`, an adic point of `Y`, because `g` is representable by algebraic
> spaces; a lift of it to `X` over an extension of complete discrete valuation rings pairs with
> the point of `Z` to give a lift to `W`.

```lean
theorem IsRigSurjective.of_isPullback {W X Y Z : FppfSheaf B S hS}
    {p : W ⟶ Z} {q : W ⟶ X} {g : Z ⟶ Y} {f : X ⟶ Y} (sq : IsPullback p q g f)
    (hf : IsLocallyOfFiniteType B S hS f) (hg : IsLocallyOfFiniteType B S hS g)
    (hsf : IsRigSurjective B S hS f) :
    IsLocallyOfFiniteType B S hS p ∧ IsRigSurjective B S hS p
```

**`AlgebraicGeometry.FormalSpace.hasRigSurjectiveOnPullbackCharts_of_isRigSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveClosedImmersionCharts.lean, line 612](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveClosedImmersionCharts.lean#L612). The attribute's comment: “the chart shape in which the proof of Stacks 0GD5 uses it, carrying nothing beyond rig-surjectivity of f: a chart which is representable by algebraic spaces and etale is in particular representable, so the base change of f along it is rig-surjective, and the presenting isomorphisms of the chart are stripped off by Stacks 0AQT and its postcomposition companion. Local finite typeness of f and of the chart, which the source assumes, is used by the source only for the conclusion that the base change is locally of finite type, which is not asserted here”.

> **Stacks 0AQS** in the chart shape in which the proof of Stacks 0GD5 uses it: a
> rig-surjective morphism has rig-surjective chart base changes, presented as formal spectra of
> the chart homomorphisms. Nothing is carried.
>
> A chart `b : V ⟶ Y` which is representable by algebraic spaces and étale is in particular
> representable by algebraic spaces, so
> `AlgebraicGeometry.FormalSpace.IsRigSurjective.of_isPullback_of_representable` makes the chart
> base change `t` rig-surjective; local finite typeness of `f`, which Stacks 0AQS assumes, enters
> that lemma only through the conclusion that the base change is locally of finite type, which is
> not asserted here. The presenting isomorphisms of the chart are then stripped off by
> Stacks 0AQT and its postcomposition companion, which is the step the module documentation used
> to record as missing.

```lean
theorem hasRigSurjectiveOnPullbackCharts_of_isRigSurjective {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) (hf : IsRigSurjective B S hS f) :
    HasRigSurjectiveOnPullbackCharts B S hS f
```

**`AlgebraicGeometry.FormalSpace.IsRigSurjective.of_isPullback_of_representable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveRigEtaleDiagonal.lean, line 202](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveRigEtaleDiagonal.lean#L202). The attribute's comment: “rig-surjectivity alone, for a base change along a morphism assumed only representable by algebraic spaces rather than locally of finite type”.

> **Stacks 0AQS**, with both hypotheses that
> `AlgebraicGeometry.FormalSpace.IsRigSurjective.of_isPullback` makes on local finite typeness
> dropped. A base change of a rig-surjective morphism of formal algebraic spaces over `S` along
> a morphism representable by algebraic spaces is rig-surjective.
>
> An adic point of `Z` out of the formal spectrum of a complete discrete valuation ring becomes,
> after composition with `g`, an adic point of `Y`, because `g` is representable by algebraic
> spaces; a lift of it to `X` over an extension of complete discrete valuation rings pairs with
> the point of `Z` to give a lift to `W`. Local finite typeness of `g` enters Stacks 0AQS only
> through this use of representability, and local finite typeness of `f` only through the
> conclusion that the base change is locally of finite type, which is not asserted here.

```lean
theorem IsRigSurjective.of_isPullback_of_representable {W X Y Z : FppfSheaf B S hS}
    {p : W ⟶ Z} {q : W ⟶ X} {g : Z ⟶ Y} {f : X ⟶ Y} (sq : IsPullback p q g f)
    (hgrep : Space.IsRepresentableByAlgebraicSpacesULift.{u + 1} B S hS g.hom)
    (hsf : IsRigSurjective B S hS f) :
    IsRigSurjective B S hS p
```

## Tag 0GH5, a lemma

[Tag 0GH5](https://stacks.math.columbia.edu/tag/0GH5) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsRigSurjective.of_comp_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveMonomorphism.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveMonomorphism.lean#L75).

> **Stacks 0GH5.** Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of locally Noetherian formal
> algebraic spaces over `S` which are locally of finite type. If `g ∘ f` is rig-surjective and
> `g` is a monomorphism, then `f` is rig-surjective.
>
> As `g` is a monomorphism, the square with sides `𝟙 X` and `f` over `g ∘ f` and `g` is
> cartesian, so `f` is the base change of `g ∘ f` along `g`; and the base change of a
> rig-surjective morphism locally of finite type along a morphism locally of finite type is
> rig-surjective, by Stacks 0AQS.

```lean
theorem IsRigSurjective.of_comp_of_mono {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : IsLocallyOfFiniteType B S hS f) (hg : IsLocallyOfFiniteType B S hS g)
    (hsfg : IsRigSurjective B S hS (f ≫ g)) (hgmono : Mono g) :
    IsRigSurjective B S hS f
```

## Tag 0AQT, a lemma

[Tag 0AQT](https://stacks.math.columbia.edu/tag/0AQT) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.IsRigSurjective.of_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjective.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjective.lean#L138).

> **Stacks 0AQT.** If a composition of morphisms of formal algebraic spaces over `S` is
> rig-surjective, then so is its second factor: a lift of an adic point of the final target to
> the initial source is, after composition with the first factor, a lift to the intermediate
> space.

```lean
theorem IsRigSurjective.of_comp (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hgf : IsRigSurjective B S hS (f ≫ g)) :
    IsRigSurjective B S hS g
```

## Tag 0AQU, a lemma

[Tag 0AQU](https://stacks.math.columbia.edu/tag/0AQU) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigSurjective_of_isSurjective_of_isRepresentableEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleAdicPointLift.lean, line 629](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/EtaleAdicPointLift.lean#L629).

> **Stacks 0AQU.** A morphism of fppf sheaves over `S` which is representable by algebraic
> spaces, étale and surjective is rig-surjective.
>
> Let `p : Spf R ⟶ Y` be an adic morphism out of the formal spectrum of a complete discrete
> valuation ring. The closed point of `Spf R` maps to a point of `Y`, which by surjectivity is
> the image of a point of `X`; together they give a point of `Spf R ×_Y X`
> (`AlgebraicGeometry.Space.exists_point_of_isPullbackULift`), and
> `exists_lift_of_pointsULift_pullback_of_isRepresentableEtale` turns that point into the lift
> the definition of rig-surjectivity asks for.
>
> The source states this for locally Noetherian formal algebraic spaces `X` and `Y`; neither
> hypothesis is used, so neither is assumed. Nor is adicness of `p`: the lift exists for every
> morphism out of the formal spectrum of a complete discrete valuation ring.

```lean
theorem isRigSurjective_of_isSurjective_of_isRepresentableEtale {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) (hf : IsRepresentableEtale B S hS f) (hsurj : IsSurjective B S hS f) :
    IsRigSurjective B S hS f
```

**`AlgebraicGeometry.FormalSpace.isRigSurjective_of_isRepresentableEtale_of_isSurjective'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveEtaleSurjectiveRefined.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveEtaleSurjectiveRefined.lean#L59).

> A morphism of locally Noetherian formal algebraic spaces over `S` which is representable by
> algebraic spaces, étale and surjective is rig-surjective.

```lean
theorem isRigSurjective_of_isRepresentableEtale_of_isSurjective'
    {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y)
    (hf : IsRepresentableEtale B S hS f) (hsurj : IsSurjective B S hS f) :
    IsRigSurjective B S hS f
```

## Tag 0AQV, a lemma

[Tag 0AQV](https://stacks.math.columbia.edu/tag/0AQV) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigSurjective_iff_forall_pullback_snd_of_isRepresentableEtale`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/JointlyRigSurjectiveEtale.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/JointlyRigSurjectiveEtale.lean#L132). The attribute's comment: “for a morphism f : X ⟶ Y locally of finite type and a family of representable étale morphisms gᵢ : Yᵢ ⟶ Y from formal algebraic spaces with ∐ gᵢ surjective, f is rig-surjective if and only if every base change X ×\_Y Yᵢ ⟶ Yᵢ is; the locally Noetherian hypotheses of the source are not needed”.

> **Stacks 0AQV.** Let `f : X ⟶ Y` be a morphism of fppf sheaves over `S` which is locally of
> finite type and let `{gᵢ : Yᵢ ⟶ Y}` be a family of morphisms from formal algebraic spaces which
> are representable by algebraic spaces and étale and which is jointly surjective on points (that
> is, `∐ gᵢ` is surjective). Then `f` is rig-surjective if and only if each base change
> `fᵢ : X ×_Y Yᵢ ⟶ Yᵢ` is rig-surjective.
>
> This is `isRigSurjective_iff_forall_pullback_snd'` together with joint rig-surjectivity of the
> family, which is the family form of Stacks 0AQU,
> `isJointlyRigSurjective_of_isRepresentableEtale_of_isJointlySurjective`: the source's proof
> applies Stacks 0AQU to `∐ gᵢ`, and that form avoids the coproduct by catching each adic point in
> one member of the family.
>
> The source states this for locally Noetherian formal algebraic spaces `X`, `Y` and `Yᵢ`. The
> proof uses that the `Yᵢ` are formal algebraic spaces and nothing more, so the locally Noetherian
> hypotheses and the hypotheses on `X` and `Y` are omitted.

```lean
theorem isRigSurjective_iff_forall_pullback_snd_of_isRepresentableEtale (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) {I : Type v} {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (Yi : I → FppfSheaf B S hS) (g : ∀ i, Yi i ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f)
    (hYi : ∀ i, IsFormalAlgebraicSpace B S hS (Yi i))
    (hg : ∀ i, IsRepresentableEtale B S hS (g i))
    (hcover : IsJointlySurjective B S hS Yi g) :
    IsRigSurjective B S hS f ↔ ∀ i, IsRigSurjective B S hS (pullback.snd f (g i))
```

## Tag 0AQX, a lemma

[Tag 0AQX](https://stacks.math.columbia.edu/tag/0AQX) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigSurjective_formalSpectrumMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveCriterion.lean, line 191](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveCriterion.lean#L191).

> Let `A` be a Noetherian ring complete with respect to an ideal `I`, and let `C` be an
> `I`-adically complete `A`-algebra. If `A/Iⁿ → C/IⁿC` is of finite type and flat for every `n`,
> and faithfully flat for `n = 1`, then `Spf C → Spf A` is rig-surjective.

```lean
theorem isRigSurjective_formalSpectrumMap
    {A C : Type u} [CommRing A] [CommRing C] [Algebra A C]
    [TopologicalSpace A] [IsTopologicalRing A] [IsLinearTopology A A]
    [TopologicalSpace C] [IsTopologicalRing C] [IsLinearTopology C C]
    [IsNoetherianRing A] (I : Ideal A)
    (hAadic : IsAdic I) (hAcomplete : IsAdicComplete I A)
    (hCadic : IsAdic (I.map (algebraMap A C)))
    (hCcomplete : IsAdicComplete (I.map (algebraMap A C)) C)
    (hfinite : ∀ n : ℕ,
      Algebra.FiniteType (A ⧸ I ^ n) (C ⧸ (I ^ n).map (algebraMap A C)))
    (hflat : ∀ n : ℕ, Module.Flat (A ⧸ I ^ n) (C ⧸ (I ^ n).map (algebraMap A C)))
    (hfaithful : Module.FaithfullyFlat (A ⧸ I) (C ⧸ I.map (algebraMap A C)))
    (D : QuotientSystem B S hS A) (E : QuotientSystem B S hS C)
    (f : ContinuousHom D E) (hf : f.toRingHom = algebraMap A C) :
    IsRigSurjective B S hS
      (formalSpectrumMap
        (TopologicalRing.isWeaklyAdmissible_of_isAdic hAadic hAcomplete) f)
```

## Tag 0AQY, a lemma

[Tag 0AQY](https://stacks.math.columbia.edu/tag/0AQY) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigSurjective_formalSpectrumMap_iff_faithfullyFlat'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveFaithfullyFlatUnconditional.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveFaithfullyFlatUnconditional.lean#L228).

> **Stacks 0AQY.** Let `A` be a Noetherian ring complete with respect to an ideal `I` whose
> `I`-torsion vanishes, and let `C` be an `I`-adically complete `A`-algebra such that
> `A/Iⁿ → C/IⁿC` is flat and of finite type for every `n`. Then `Spf C → Spf A` is rig-surjective
> if and only if `A/I → C/IC` is faithfully flat.
>
> Faithful flatness gives rig-surjectivity by Stacks 0AQX. Conversely, a closed point of
> `Spec(A/I)` is a maximal ideal `I ⊆ 𝔪 ⊆ A`, and
> `exists_isPrime_comap_eq_of_isRigSurjective'` contracts a prime of `C` onto it; so
> `Spec(C/IC) → Spec(A/I)` meets every closed point, which for a flat map is faithful flatness
> (Stacks 00HQ).

```lean
theorem isRigSurjective_formalSpectrumMap_iff_faithfullyFlat' (I : Ideal A)
    (hAadic : IsAdic I) (hAcomplete : IsAdicComplete I A)
    (hCadic : IsAdic (I.map (algebraMap A C)))
    (hCcomplete : IsAdicComplete (I.map (algebraMap A C)) C)
    (hTorsion : Submodule.torsionBySet A A (I : Set A) = ⊥)
    (hfinite : ∀ n : ℕ, Algebra.FiniteType (A ⧸ I ^ n) (C ⧸ (I ^ n).map (algebraMap A C)))
    (hflat : ∀ n : ℕ, Module.Flat (A ⧸ I ^ n) (C ⧸ (I ^ n).map (algebraMap A C)))
    (D : QuotientSystem B S hS A) (E : QuotientSystem B S hS C)
    (f : ContinuousHom D E) (hf : f.toRingHom = algebraMap A C) :
    IsRigSurjective B S hS
      (formalSpectrumMap
        (TopologicalRing.isWeaklyAdmissible_of_isAdic hAadic hAcomplete) f) ↔
      Module.FaithfullyFlat (A ⧸ I) (C ⧸ I.map (algebraMap A C))
```

## Tag 0AR0, a lemma

[Tag 0AR0](https://stacks.math.columbia.edu/tag/0AR0) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigSurjective_iff_factorsAdicCompleteDvrPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveDvrCriterion.lean, line 383](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveDvrCriterion.lean#L383).

> **Stacks 0AR0.** Let `f : X ⟶ Y` be a morphism of formal algebraic
> spaces over `S` with `X` and `Y` locally Noetherian, `f` locally of finite type and `f` a
> monomorphism. Then `f` is rig-surjective if and only if every adic morphism `Spf R ⟶ Y`, with
> `R` a complete discrete valuation ring, factors through `X`.
>
> The forward implication uses that `X` and `Y` are fpqc sheaves, Stacks 0AQD,
> `AlgebraicGeometry.FormalSpace.isSheaf_fpqc`.

```lean
theorem isRigSurjective_iff_factorsAdicCompleteDvrPoints {X Y : FppfSheaf B S hS} (f : X ⟶ Y)
    (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y)
    (hft : IsLocallyOfFiniteType B S hS f) [Mono f] :
    IsRigSurjective B S hS f ↔ FactorsAdicCompleteDvrPoints B S hS f
```

## Tag 0GD5, a lemma

[Tag 0GD5](https://stacks.math.columbia.edu/tag/0GD5) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigSurjective_iff_hasAnnihilatedKerPowOnPullbackCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveClosedImmersion.lean, line 404](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveClosedImmersion.lean#L404). The attribute's comment: “both directions, carrying three hypotheses: Stacks 0AQI in the chart form of Stacks 0GD4, that the chart homomorphism is a surjection of WAdm^Noeth which is adic of topologically finite type (hAQI); the equivalence of rig-surjectivity of f with rig-surjectivity of its chart base changes, which is Stacks 0AQS forwards and Stacks 0AQV backwards (hAQV); and Stacks 0AR0 for the chart maps, read through the full faithfulness of Spf of Stacks 0AN0, identifying rig-surjectivity of a chart map with the factorisation of its adic discrete valuation points (hAR0). The algebraic equivalence joining the factorisation criterion to the annihilation condition, which is what the source's two implications come down to and which uses Stacks 00PH, is proved”.

> **Stacks 0GD5**, both directions, carrying three hypotheses. Let `f : X ⟶ Y` be a closed
> immersion of locally Noetherian formal algebraic spaces over `S`. Then `f` is rig-surjective
> exactly when on every affine representable étale chart `V ⟶ Y` of the target the fibre product
> `X ×_Y V ⟶ V` is given by a surjection of `WAdm^{Noeth}` some ideal of definition of whose
> source annihilates a positive power of its kernel.
>
> The hypothesis `hAQI` is Stacks 0AQI in the chart form of Stacks 0GD4, `hAQV` is the
> equivalence of rig-surjectivity of `f` with rig-surjectivity of its chart base changes
> (Stacks 0AQS forwards, Stacks 0AQV backwards), and `hAR0` is Stacks 0AR0 for the chart maps,
> read through the full faithfulness of `Spf`. The passage from the factorisation criterion to
> the annihilation condition is the algebraic equivalence proved here, which uses
> **Stacks 00PH**.

```lean
theorem isRigSurjective_iff_hasAnnihilatedKerPowOnPullbackCharts {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) (_hX : IsLocallyNoetherian B S hS X) (_hY : IsLocallyNoetherian B S hS Y)
    (_hf : IsClosedImmersion B S hS f)
    (hAQI : HasAdicQuotientOnPullbackCharts B S hS f)
    (hAQV : IsRigSurjective B S hS f ↔ HasRigSurjectiveOnPullbackCharts B S hS f)
    (hAR0 : HasRigSurjectiveOnPullbackCharts B S hS f ↔
      HasDvrFactorizationOnPullbackCharts B S hS f) :
    IsRigSurjective B S hS f ↔ HasAnnihilatedKerPowOnPullbackCharts B S hS f
```

**`AlgebraicGeometry.FormalSpace.isRigSurjective_iff_hasAnnihilatedKerPow_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveClosedImmersionAtlas.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSurjectiveClosedImmersionAtlas.lean#L92).

> **Stacks 0GD5.** Let `f : X ⟶ Y` be a closed immersion of locally Noetherian formal
> algebraic spaces over `S`. Then `f` is rig-surjective if and only if for every affine formal
> algebraic space `V` and every morphism `V ⟶ Y` which is representable by algebraic spaces and
> étale, the base change `X ×_Y V ⟶ V` corresponds to a surjection `B → A` of `WAdm^{Noeth}`
> whose kernel `J` satisfies `I J ^ n = 0` for some ideal of definition `I` of `B` and some
> `n ≥ 1`.
>
> Condition (2) is `AlgebraicGeometry.FormalSpace.HasAnnihilatedKerPowOnPullbackCharts`, asked
> of every presentation of the base change by Noetherian rings with adic topologies. The
> equivalence of condition (2) with rig-surjectivity of every chart map is
> `AlgebraicGeometry.FormalSpace.hasAnnihilatedKerPow_iff_hasRigSurjective_of_isClosedImmersion`
> (Stacks 0AQI, 0AR0 and 00PH). Rig-surjectivity of `f` gives that of the chart maps by
> Stacks 0AQS, `AlgebraicGeometry.FormalSpace.hasRigSurjectiveOnPullbackCharts_of_isRigSurjective`,
> and conversely by Stacks 0AQV,
> `AlgebraicGeometry.FormalSpace.isRigSurjective_of_hasRigSurjectiveOnPullbackCharts`.

```lean
theorem isRigSurjective_iff_hasAnnihilatedKerPow_of_isClosedImmersion {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y)
    (hf : IsClosedImmersion B S hS f) :
    IsRigSurjective B S hS f ↔ HasAnnihilatedKerPowOnPullbackCharts B S hS f
```

## Tag 0GD6, a lemma

[Tag 0GD6](https://stacks.math.columbia.edu/tag/0GD6) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigSmooth_and_isRigSurjective_tfae_of_isClosedImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmoothRigSurjectiveClosedImmersion.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmoothRigSurjectiveClosedImmersion.lean#L253). The attribute's comment: “all three conditions and every implication between them, carrying exactly the four hypotheses which this library's Stacks 0GD4 and Stacks 0GD5 already carry and nothing more: Stacks 0AQI in the chart form of Stacks 0GD4, that the chart homomorphism is a surjection of WAdm^Noeth which is adic of topologically finite type (hAQI), whose library carrier covers only the countably indexed case, which the Noetherian charts here are not; Stacks 0GCZ read as the proof of Stacks 0GD4 reads it, that rig-etaleness of f need only be checked on the ring maps appearing in condition (3) (hGCZ); the equivalence of rig-surjectivity of f with rig-surjectivity of its chart base changes, Stacks 0AQS forwards and Stacks 0AQV backwards (hAQV), undischargeable because Tag 0AJG, IsEtaleULift implies IsLocallyOfFiniteTypeULift, has no carrier in this library; and Stacks 0AR0 for the chart maps read through the full faithfulness of Spf of Stacks 0AN0 (hAR0), undischargeable because its substantial direction rests on the EXISTENCE half of Tag 0AQD, whose carriers supply uniqueness only. No carried hypothesis is an implication of this lemma. The combination the source calls trivial is proved, including the ring-theoretic observation the source omits: I * J ^ n = 0 together with I * J <= J ^ 2 forces I ^ n * J = 0”.

> **Stacks 0GD6.** Let `f : X ⟶ Y` be a closed immersion of locally Noetherian formal
> algebraic spaces over `S`. Then the following are equivalent: (1) `f` is rig-smooth and
> rig-surjective; (2) `f` is rig-étale and rig-surjective; (3) on every affine representable étale
> chart `V ⟶ Y` of the target the fibre product `X ×_Y V ⟶ V` is given by a surjection of
> `WAdm^{Noeth}` whose kernel is annihilated by some ideal of definition of the source.
>
> The equivalence of the two rigidity notions is Stacks 0GD4, the identification of
> rig-surjectivity with the annihilation of a power of the kernel is Stacks 0GD5, and the
> passage from "a power of `J` is annihilated and `J / J ^ 2` is annihilated" to "`J` is
> annihilated" is `Rig.exists_idealOfDefinition_mul_eq_bot`, the ring-theoretic step whose proof
> the source omits.
>
> The hypotheses `hAQI`, `hGCZ`, `hAQV` and `hAR0` are precisely the ones the library's
> Stacks 0GD4 and Stacks 0GD5 carry: Stacks 0AQI in chart form, Stacks 0GCZ as the proof of
> Stacks 0GD4 uses it, the equivalence of rig-surjectivity of `f` with rig-surjectivity of its
> chart base changes (Stacks 0AQS forwards, Stacks 0AQV backwards), and Stacks 0AR0 for the chart
> maps read through Stacks 0AN0.

```lean
theorem isRigSmooth_and_isRigSurjective_tfae_of_isClosedImmersion {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y)
    (hf : IsClosedImmersion B S hS f)
    (hAQI : HasAdicQuotientOnPullbackCharts B S hS f)
    (hGCZ : HasRigEtaleOnPullbackCharts B S hS f → IsRigEtale B S hS f)
    (hAQV : IsRigSurjective B S hS f ↔ HasRigSurjectiveOnPullbackCharts B S hS f)
    (hAR0 : HasRigSurjectiveOnPullbackCharts B S hS f ↔
      HasDvrFactorizationOnPullbackCharts B S hS f) :
    List.TFAE
      [IsRigSmooth B S hS f ∧ IsRigSurjective B S hS f,
        IsRigEtale B S hS f ∧ IsRigSurjective B S hS f,
        HasAnnihilatedKerOnPullbackCharts B S hS f]
```

**`AlgebraicGeometry.FormalSpace.isRigSmooth_and_isRigSurjective_tfae_of_isClosedImmersion'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmoothRigSurjectiveClosedImmersionCharts.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmoothRigSurjectiveClosedImmersionCharts.lean#L65).

> **Stacks 0GD6.** Let `f : X ⟶ Y` be a closed immersion of locally Noetherian formal
> algebraic spaces over `S`. Then the following are equivalent: (1) `f` is rig-smooth and
> rig-surjective; (2) `f` is rig-étale and rig-surjective; (3) on every affine representable étale
> chart `V ⟶ Y` of the target the fibre product `X ×_Y V ⟶ V` is given by a surjection of
> `WAdm^{Noeth}` whose kernel is annihilated by some ideal of definition of the source.
>
> The equivalence of the two rigidity notions with the annihilation of the conormal module
> `J / J ^ 2` is Stacks 0GD4, the identification of rig-surjectivity with the annihilation of a
> power of the kernel is Stacks 0GD5, and the passage from "a power of `J` is annihilated and
> `J / J ^ 2` is annihilated" to "`J` is annihilated" is `Rig.exists_idealOfDefinition_mul_eq_bot`,
> applied chart by chart in `hasAnnihilatedKer_of_hasAnnihilatedConormal_of_hasAnnihilatedKerPow`.

```lean
theorem isRigSmooth_and_isRigSurjective_tfae_of_isClosedImmersion' {X Y : FppfSheaf B S hS}
    (f : X ⟶ Y) (hX : IsLocallyNoetherian B S hS X) (hY : IsLocallyNoetherian B S hS Y)
    (hf : IsClosedImmersion B S hS f) :
    List.TFAE
      [IsRigSmooth B S hS f ∧ IsRigSurjective B S hS f,
        IsRigEtale B S hS f ∧ IsRigSurjective B S hS f,
        HasAnnihilatedKerOnPullbackCharts B S hS f]
```

## Tag 0GH6, a lemma

[Tag 0GH6](https://stacks.math.columbia.edu/tag/0GH6) in the Stacks Project.

**`AlgebraicGeometry.FormalSpace.isRigSmooth_of_comp_of_isRigSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmoothRigSurjectiveDescent.lean, line 292](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmoothRigSurjectiveDescent.lean#L292). The attribute's comment: “the rig-smooth case, assuming Stacks 0GCK (hlocal), the transfer of Remark 0GBG to formal algebraic spaces (htransfer), that a representable étale morphism is adic and locally of finite type (hetaleAdic, hetaleFiniteType), and the chart-level argument of the source's proof (hdescent)”.

> **Stacks 0GH6**, the rig-smooth case, carrying four hypotheses. Let `f : X ⟶ Y` and
> `g : Y ⟶ Z` be morphisms of formal algebraic spaces over `S`. If `g` is locally of finite type,
> `f` is rig-smooth and rig-surjective, and `f ≫ g` is rig-smooth, then `g` is rig-smooth.
>
> Rig-smoothness of `g` is tested on affine étale chart squares over it, by conditions (1) and
> (2) of Stacks 0GCQ. At such a square the three hypotheses produce exactly the data the source's
> argument consumes: the chart morphism `t` is locally of finite type, the base change
> `X ×_Y V ⟶ V` of `f` along the chart of `Y` is rig-surjective and rig-smooth on charts, and its
> composite with `t ≫ b` — that is, its composite with `g ∘ f` through the projection to `X` — is
> rig-smooth on charts.
>
> The hypotheses carried are `hlocal`, which is Stacks 0GCK; `htransfer`, the transfer of Remark
> 0GBG to formal algebraic spaces; `hetaleAdic` and `hetaleFiniteType`, that a representable étale
> morphism is adic and locally of finite type; and `hdescent`, the chart-level argument of the
> source. Local finiteness of type of `f`, which Definition 0AQQ presupposes, is the hypothesis
> `hfft`.

```lean
theorem isRigSmooth_of_comp_of_isRigSurjective
    (hlocal : TopologicalRing.PropertyIsLocalNoetherian.{u}
      (fun {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
        [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂] (φ : R₁ →+* R₂) ↦
        RingHom.IsRigSmoothArrow φ))
    (htransfer : TransfersBaseChangeOnAffineEtaleDiagrams B S hS)
    (hetaleAdic : ∀ {U V : FppfSheaf B S hS} (w : U ⟶ V),
      IsRepresentableEtale B S hS w →
        IsAdicOnEveryAffineEtaleDiagramNoetherian B S hS w)
    (hetaleFiniteType : ∀ {U V : FppfSheaf B S hS} (w : U ⟶ V),
      IsRepresentableEtale B S hS w → IsLocallyOfFiniteType B S hS w)
    (hdescent : HasRigSurjectiveChartDescent B S hS
      (fun {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
        [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂] (φ : R₁ →+* R₂) ↦
        RingHom.IsRigSmoothArrow φ))
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hgft : IsLocallyOfFiniteType B S hS g) (hfft : IsLocallyOfFiniteType B S hS f)
    (hf : IsRigSmooth B S hS f) (hfs : IsRigSurjective B S hS f)
    (hgf : IsRigSmooth B S hS (f ≫ g)) :
    IsRigSmooth B S hS g
```

**`AlgebraicGeometry.FormalSpace.isRigEtale_of_comp_of_isRigSurjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmoothRigSurjectiveDescent.lean, line 331](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmoothRigSurjectiveDescent.lean#L331). The attribute's comment: “the rig-étale case, assuming Stacks 0AQL (hlocal), the transfer of Remark 0GBG to formal algebraic spaces (htransfer), that a representable étale morphism is adic and locally of finite type (hetaleAdic, hetaleFiniteType), and the chart-level argument of the source's proof (hdescent)”.

> **Stacks 0GH6**, the rig-étale case, carrying four hypotheses. Let `f : X ⟶ Y` and
> `g : Y ⟶ Z` be morphisms of formal algebraic spaces over `S`. If `g` is locally of finite type,
> `f` is rig-étale and rig-surjective, and `f ≫ g` is rig-étale, then `g` is rig-étale.
>
> The proof is the proof of the rig-smooth case with rig-smoothness of arrows of `WAdm^{Noeth}`
> replaced by rig-étaleness throughout: conditions (1) and (2) of Stacks 0GCZ replace those of
> Stacks 0GCQ, and Stacks 0GCW replaces Stacks 0GCL as the base-change input. The hypotheses are
> the same four, with `hlocal` now Stacks 0AQL.

```lean
theorem isRigEtale_of_comp_of_isRigSurjective
    (hlocal : TopologicalRing.PropertyIsLocalNoetherian.{u}
      (fun {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
        [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂] (φ : R₁ →+* R₂) ↦
        RingHom.IsRigEtaleArrow φ))
    (htransfer : TransfersBaseChangeOnAffineEtaleDiagrams B S hS)
    (hetaleAdic : ∀ {U V : FppfSheaf B S hS} (w : U ⟶ V),
      IsRepresentableEtale B S hS w →
        IsAdicOnEveryAffineEtaleDiagramNoetherian B S hS w)
    (hetaleFiniteType : ∀ {U V : FppfSheaf B S hS} (w : U ⟶ V),
      IsRepresentableEtale B S hS w → IsLocallyOfFiniteType B S hS w)
    (hdescent : HasRigSurjectiveChartDescent B S hS
      (fun {R₁ R₂ : Type u} [CommRing R₁] [TopologicalSpace R₁] [IsTopologicalRing R₁]
        [CommRing R₂] [TopologicalSpace R₂] [IsTopologicalRing R₂] (φ : R₁ →+* R₂) ↦
        RingHom.IsRigEtaleArrow φ))
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z)
    (hgft : IsLocallyOfFiniteType B S hS g) (hfft : IsLocallyOfFiniteType B S hS f)
    (hf : IsRigEtale B S hS f) (hfs : IsRigSurjective B S hS f)
    (hgf : IsRigEtale B S hS (f ≫ g)) :
    IsRigEtale B S hS g
```

**`AlgebraicGeometry.FormalSpace.isRigSmooth_of_comp_of_isRigSurjective_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmoothRigSurjectiveDescentCharts.lean, line 285](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmoothRigSurjectiveDescentCharts.lean#L285). The attribute's comment: “the rig-smooth case”.

> **Stacks 0GH6**, the rig-smooth case. Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of formal
> algebraic spaces over `S` with `X` locally Noetherian. If `g` is locally of finite type, `f` is
> rig-smooth and rig-surjective, and `g ∘ f` is rig-smooth, then `g` is rig-smooth.
>
> The source also assumes `Y` and `Z` locally Noetherian and `f` locally of finite type; none of
> these is used, see the module documentation.

```lean
theorem isRigSmooth_of_comp_of_isRigSurjective_of_isLocallyNoetherian
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z) (hX : IsLocallyNoetherian B S hS X)
    (hgft : IsLocallyOfFiniteType B S hS g) (hf : IsRigSmooth B S hS f)
    (hfs : IsRigSurjective B S hS f) (hgf : IsRigSmooth B S hS (f ≫ g)) :
    IsRigSmooth B S hS g
```

**`AlgebraicGeometry.FormalSpace.isRigEtale_of_comp_of_isRigSurjective_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmoothRigSurjectiveDescentCharts.lean, line 301](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/FormalSpace/RigSmoothRigSurjectiveDescentCharts.lean#L301). The attribute's comment: “the rig-étale case”.

> **Stacks 0GH6**, the rig-étale case. Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of formal
> algebraic spaces over `S` with `X` locally Noetherian. If `g` is locally of finite type, `f` is
> rig-étale and rig-surjective, and `g ∘ f` is rig-étale, then `g` is rig-étale.
>
> The source also assumes `Y` and `Z` locally Noetherian and `f` locally of finite type; none of
> these is used, see the module documentation.

```lean
theorem isRigEtale_of_comp_of_isRigSurjective_of_isLocallyNoetherian
    {X Y Z : FppfSheaf B S hS} (f : X ⟶ Y) (g : Y ⟶ Z) (hX : IsLocallyNoetherian B S hS X)
    (hgft : IsLocallyOfFiniteType B S hS g) (hf : IsRigEtale B S hS f)
    (hfs : IsRigSurjective B S hS f) (hgf : IsRigEtale B S hS (f ≫ g)) :
    IsRigEtale B S hS g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 88.21, Tag 0AQP](https://stacks.math.columbia.edu/tag/0AQP)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
