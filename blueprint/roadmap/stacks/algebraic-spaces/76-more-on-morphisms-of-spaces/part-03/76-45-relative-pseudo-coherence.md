---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.locallyOfFiniteType_of_represents, AlgebraicGeometry.Space.existsUnique_representableDerivedPullback_iso, AlgebraicGeometry.Space.IsRepresentablyRelativelyPseudoCoherentFrom, AlgebraicGeometry.Space.relativePseudoCoherence_chart_tfae, AlgebraicGeometry.Space.relativePseudoCoherence_etaleSquare_tfae, AlgebraicGeometry.Space.IsRelativelyPseudoCoherentFrom, AlgebraicGeometry.Space.IsRelativelyPseudoCoherent, AlgebraicGeometry.Space.IsModuleRelativelyPseudoCoherentFrom
statement: formalized
proof: formalized
---

# 76.45 Relative pseudo-coherence

Section 76.45 of the Stacks Project, [Tag 0CSV](https://stacks.math.columbia.edu/tag/0CSV). 4 tags here are carried by 13 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0CSW, a remark

[Tag 0CSW](https://stacks.math.columbia.edu/tag/0CSW) in the Stacks Project.

**`AlgebraicGeometry.Space.locallyOfFiniteType_of_represents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Representable.lean, line 52](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Representable.lean#L52). The attribute's comment: “representing\_locally\_finite\_type”.

> **Stacks 0CSW.** If a morphism `f` of algebraic spaces over `S` is locally of finite
> type and a morphism `f₀` of objects of the site represents it, through isomorphisms
> `yoneda.obj U ≅ X` and `yoneda.obj V ≅ Y`, then the scheme morphism underlying `f₀` is
> locally of finite type.

```lean
theorem locallyOfFiniteType_of_represents (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f) (U V : BigFppfOver B S hS) (f₀ : U ⟶ V)
    (eX : yoneda.obj U ≅ X) (eY : yoneda.obj V ≅ Y)
    (hrep : yoneda.map f₀ ≫ eY.hom = eX.hom ≫ f) :
    LocallyOfFiniteType ((BigFppfOver.toScheme B S hS).map f₀)
```

**`AlgebraicGeometry.Space.existsUnique_representableDerivedPullback_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RepresentableDescent.lean, line 150](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RepresentableDescent.lean#L150). The attribute's comment: “every E in D\_QCoh(O\_X) is the pullback of a unique E\_0 in D\_QCoh(O\_\{X\_0}), by Tag 071Q”.

> Let `X` be an algebraic space represented by the scheme `X₀` underlying `U`, through
> `eX : h_U ≅ X`. Every object `E` of `D_QCoh(𝒪_X)` is the pullback of an object `E₀` of
> `D(𝒪_{X₀})` with quasi-coherent cohomology sheaves, and `E₀` is unique: any object of
> `D_QCoh(𝒪_{X₀})` whose pullback is isomorphic to `E` is isomorphic to `E₀`.

```lean
theorem existsUnique_representableDerivedPullback_iso
    (E : QuasicoherentDerivedCategory.{u, u} B S hS X hX) :
    ∃ E₀ : DerivedCategory ((BigFppfOver.toScheme B S hS).obj U).Modules,
      (∀ i : ℤ, ((DerivedCategory.homologyFunctor _ i).obj E₀).IsQuasicoherent) ∧
        Nonempty ((representableDerivedPullback B S hS hX eX).obj E₀ ≅ E.obj) ∧
          ∀ E₀' : DerivedCategory ((BigFppfOver.toScheme B S hS).obj U).Modules,
            (∀ i : ℤ, ((DerivedCategory.homologyFunctor _ i).obj E₀').IsQuasicoherent) →
              Nonempty ((representableDerivedPullback B S hS hX eX).obj E₀' ≅ E.obj) →
                Nonempty (E₀' ≅ E₀)
```

**`AlgebraicGeometry.Space.IsRepresentablyRelativelyPseudoCoherentFrom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RepresentableDescent.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RepresentableDescent.lean#L213). The attribute's comment: “the convention: E is m-pseudo-coherent relative to Y when E\_0 is m-pseudo-coherent relative to Y\_0 (Tag 09UI)”.

> Let `f : X → Y` be a morphism of representable algebraic spaces over `S` which is locally of
> finite type, represented by the morphism of schemes `f₀ : X₀ → Y₀` underlying `f₀ : U ⟶ V`
> through `eX : h_U ≅ X` and `eY : h_V ≅ Y`. An object `E` of `D_QCoh(𝒪_X)` is
> *`m`-pseudo-coherent relative to `Y`* when the object `E₀` of `D_QCoh(𝒪_{X₀})` whose pullback is
> `E` is `m`-pseudo-coherent relative to `Y₀` in the sense of Stacks 09UI. This makes sense because
> `f₀` is locally of finite type (`AlgebraicGeometry.Space.locallyOfFiniteType_of_represents`), and
> it does not depend on the choice of `E₀`
> (`AlgebraicGeometry.Space.isRepresentablyRelativelyPseudoCoherentFrom_iff`).

```lean
def IsRepresentablyRelativelyPseudoCoherentFrom
    (E : QuasicoherentDerivedCategory.{u, u} B S hS X hX) (m : ℤ) : Prop
```

## Tag 0CSX, a lemma

[Tag 0CSX](https://stacks.math.columbia.edu/tag/0CSX) in the Stacks Project.

**`AlgebraicGeometry.Space.relativePseudoCoherence_chart_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Relative.lean, line 565](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/Relative.lean#L565). The attribute's comment: “proved relative to the carried inputs `h`. Its `comparison` field is the second sentence of Remark 0CSW — that an object of D\_QCoh of a representable algebraic space is the pullback of a unique object of D\_QCoh of a representing scheme, which is what gives E|\_U its meaning — and is absent from the library, whose 0CSW is the first sentence only; `chartComplexPullback` is its compatibility with passing to a finer chart. The descent half of 0CSN is carried as `fppfDescent` because only the forward half is proved. 09US is not carried: it is recovered from its own 0E23 input, carried through as `torIndependentBaseChange`.”.

> **Stacks 0CSX.**  Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` locally of
> finite type, let `m` be an integer and let `E` be an object of `D_QCoh(𝒪_X)`.  With the complex
> `E|_U` of Remark 0CSW the following are equivalent:
>
> 1. for every commuting square of étale scheme charts `U ⟶ V` over `X ⟶ Y`, the complex `E|_U` is
>    `m`-pseudo-coherent relative to `V`;
> 2. for some such square with `U ⟶ X` surjective, the complex `E|_U` is `m`-pseudo-coherent
>    relative to `V`;
> 3. for every such square with `U` and `V` affine, the complex `RΓ(U, E)` of `𝒪_X(U)`-modules is
>    `m`-pseudo-coherent relative to `𝒪_Y(V)`.
>
> See the module docstring for the four inputs that `h` carries.

```lean
theorem relativePseudoCoherence_chart_tfae (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) (h : RelativePseudoCoherenceInput B S hS)
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) (hf : IsLocallyOfFiniteType B S hS f)
    (E : QuasicoherentDerivedCategory.{u, u} B S hS X hX) (m : ℤ) :
    List.TFAE
      [∀ (U V : BigFppfOver B S hS) (a : yoneda.obj U ⟶ X) (b : yoneda.obj V ⟶ Y) (g : U ⟶ V)
          (ha : HasSchemeProperty B S hS (@AlgebraicGeometry.Etale.{u}) a)
          (hb : HasSchemeProperty B S hS (@AlgebraicGeometry.Etale.{u}) b)
          (hc : yoneda.map g ≫ b = a ≫ f),
          IsPseudoCoherentFromOnChart B S hS h hX f hf E m U V a b g ha hb hc,
       ∃ (U V : BigFppfOver B S hS) (a : yoneda.obj U ⟶ X) (b : yoneda.obj V ⟶ Y) (g : U ⟶ V)
          (ha : HasSchemeProperty B S hS (@AlgebraicGeometry.Etale.{u}) a)
          (hb : HasSchemeProperty B S hS (@AlgebraicGeometry.Etale.{u}) b),
          IsSurjective B S hS a ∧ ∃ hc : yoneda.map g ≫ b = a ≫ f,
            IsPseudoCoherentFromOnChart B S hS h hX f hf E m U V a b g ha hb hc,
       ∀ (U V : BigFppfOver B S hS) (a : yoneda.obj U ⟶ X) (b : yoneda.obj V ⟶ Y) (g : U ⟶ V)
          (ha : HasSchemeProperty B S hS (@AlgebraicGeometry.Etale.{u}) a)
          (hb : HasSchemeProperty B S hS (@AlgebraicGeometry.Etale.{u}) b)
          (hc : yoneda.map g ≫ b = a ≫ f)
          (hU : IsAffine ((BigFppfOver.toScheme B S hS).obj U))
          (hV : IsAffine ((BigFppfOver.toScheme B S hS).obj V)),
          haveI : LocallyOfFiniteType ((BigFppfOver.toScheme B S hS).map g) :=
            hf U V a b g ha hb hc
          haveI := hU
          haveI := hV
          ((BigFppfOver.toScheme B S hS).map g).DerivedSectionsPseudoCoherentOn'
            (h.chartComplex hX E ha).obj m (isAffineOpen_top _) (isAffineOpen_top _)
            (by simp)]
```

**`AlgebraicGeometry.Space.relativePseudoCoherence_etaleSquare_tfae`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativeChartTests.lean, line 480](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativeChartTests.lean#L480). The attribute's comment: “all three conditions and their equivalence, at the source's hypotheses: f a morphism of algebraic spaces over S locally of finite type, E in D\_QCoh(O\_X), any m; the phrase 'E|\_U is m-pseudo-coherent relative to V' is the convention of Remark 0CSW”.

> **Stacks 0CSX.**  Let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is locally
> of finite type, let `m` be an integer and let `E` be an object of `D_QCoh(𝒪_X)`.  With the
> notation of Remark 0CSW the following are equivalent:
>
> 1. for every commutative square `U ⟶ V` over `f` of schemes `U`, `V` with étale charts
>    `U ⟶ X`, `V ⟶ Y`, the complex `E|_U` is `m`-pseudo-coherent relative to `V`;
> 2. for some such square with `U ⟶ X` surjective, `E|_U` is `m`-pseudo-coherent relative to `V`;
> 3. for every such square with `U` and `V` affine, the complex `RΓ(U, E)` of `𝒪_X(U)`-modules is
>    `m`-pseudo-coherent relative to `𝒪_Y(V)`.
>
> (1) ⟹ (2) and (1) ⟹ (3) and (3) ⟹ (1) are
> `AlgebraicGeometry.Space.exists_surjective_isPseudoCoherentFromOnEtaleSquare`,
> `AlgebraicGeometry.Space.derivedSectionsPseudoCoherentOnEtaleSquare_of_forall` and
> `AlgebraicGeometry.Space.isPseudoCoherentFromOnEtaleSquare_of_forall_derivedSections`.  For
> (2) ⟹ (1), `AlgebraicGeometry.Space.exists_surjective_etale_isPseudoCoherentFrom_derivedPullback`
> gives, on a second square, relative `m`-pseudo-coherence of the pullback of `E|_{U'}` along a
> surjective étale morphism `W ⟶ U'`; that morphism alone is an fppf covering, and Stacks 0CSN
> descends the property to `E|_{U'}`.

```lean
theorem relativePseudoCoherence_etaleSquare_tfae :
    List.TFAE
      [∀ (U V : BigFppfOver B S hS) (a : yoneda.obj U ⟶ X) (b : yoneda.obj V ⟶ Y) (g : U ⟶ V)
          (ha : HasSchemeProperty B S hS (@AlgebraicGeometry.Etale.{u}) a)
          (hb : HasSchemeProperty B S hS (@AlgebraicGeometry.Etale.{u}) b)
          (hc : yoneda.map g ≫ b = a ≫ f),
          IsPseudoCoherentFromOnEtaleSquare hX f hf E m U V a b g ha hb hc,
       ∃ (U V : BigFppfOver B S hS) (a : yoneda.obj U ⟶ X) (b : yoneda.obj V ⟶ Y) (g : U ⟶ V)
          (ha : HasSchemeProperty B S hS (@AlgebraicGeometry.Etale.{u}) a)
          (hb : HasSchemeProperty B S hS (@AlgebraicGeometry.Etale.{u}) b),
          IsSurjective B S hS a ∧ ∃ hc : yoneda.map g ≫ b = a ≫ f,
            IsPseudoCoherentFromOnEtaleSquare hX f hf E m U V a b g ha hb hc,
       ∀ (U V : BigFppfOver B S hS) (a : yoneda.obj U ⟶ X) (b : yoneda.obj V ⟶ Y) (g : U ⟶ V)
          (ha : HasSchemeProperty B S hS (@AlgebraicGeometry.Etale.{u}) a)
          (hb : HasSchemeProperty B S hS (@AlgebraicGeometry.Etale.{u}) b)
          (hc : yoneda.map g ≫ b = a ≫ f)
          (hU : IsAffine ((BigFppfOver.toScheme B S hS).obj U))
          (hV : IsAffine ((BigFppfOver.toScheme B S hS).obj V)),
          DerivedSectionsPseudoCoherentOnEtaleSquare hX f hf E m U V a b g ha hb hc hU hV]
```

## Tag 0CSY, a definition

[Tag 0CSY](https://stacks.math.columbia.edu/tag/0CSY) in the Stacks Project.

**`AlgebraicGeometry.Space.IsRelativelyPseudoCoherentFrom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativeDefinition.lean, line 200](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativeDefinition.lean#L200). The attribute's comment: “part (1): m-pseudo-coherence relative to Y of an object of D\_QCoh, through condition (3) of Tag 0CSX”.

> **Stacks 0CSY, part (1).** An object `E` of `D_QCoh(𝒪_X)` is *`m`-pseudo-coherent relative
> to `Y`* when, for every commuting square of étale scheme charts `U` of `X` and `V` of `Y` over
> `f` with `U` and `V` affine, the complex `RΓ(U, E)` of `𝒪_X(U)`-modules is `m`-pseudo-coherent
> relative to the ring `𝒪_Y(V)` in the sense of Tag 065I.
>
> This is condition (3) of Tag 0CSX; see "Which of the equivalent conditions of Tag 0CSX
> is taken as the definition" in the module docstring.

```lean
def IsRelativelyPseudoCoherentFrom {Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f)
    (E : QuasicoherentDerivedCategory.{u, u} B S hS X hX) (m : ℤ) : Prop
```

**`AlgebraicGeometry.Space.IsRelativelyPseudoCoherent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativeDefinition.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativeDefinition.lean#L225). The attribute's comment: “part (2): pseudo-coherence relative to Y of an object of D\_QCoh”.

> **Stacks 0CSY, part (2).** An object of `D_QCoh(𝒪_X)` is *pseudo-coherent relative to `Y`*
> when it is `m`-pseudo-coherent relative to `Y` for every integer `m`.

```lean
def IsRelativelyPseudoCoherent {Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f)
    (E : QuasicoherentDerivedCategory.{u, u} B S hS X hX) : Prop
```

**`AlgebraicGeometry.Space.IsModuleRelativelyPseudoCoherentFrom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativeDefinition.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativeDefinition.lean#L236). The attribute's comment: “part (3): m-pseudo-coherence relative to Y of a quasi-coherent module”.

> **Stacks 0CSY, part (3).** A quasi-coherent `𝒪_X`-module is *`m`-pseudo-coherent relative
> to `Y`* when the complex it determines in degree zero, an object of `D_QCoh(𝒪_X)` by
> `AlgebraicGeometry.Space.derivedCategoryB_singleFunctor_obj`, is.

```lean
def IsModuleRelativelyPseudoCoherentFrom {Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f)
    (F : Modules.{u, u} B S hS X hX) (hF : F.IsQuasicoherentOnSite) (m : ℤ) : Prop
```

**`AlgebraicGeometry.Space.IsModuleRelativelyPseudoCoherent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativeDefinition.lean, line 246](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativeDefinition.lean#L246). The attribute's comment: “part (4): pseudo-coherence relative to Y of a quasi-coherent module”.

> **Stacks 0CSY, part (4).** A quasi-coherent `𝒪_X`-module is *pseudo-coherent relative to
> `Y`* when the complex it determines in degree zero is.

```lean
def IsModuleRelativelyPseudoCoherent {Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (f : X ⟶ Y)
    (hf : IsLocallyOfFiniteType B S hS f)
    (F : Modules.{u, u} B S hS X hX) (hF : F.IsQuasicoherentOnSite) : Prop
```

## Tag 0DII, a lemma

[Tag 0DII](https://stacks.math.columbia.edu/tag/0DII) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isPseudoCoherent_iff_of_flat_of_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeAbsolute.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/PseudoCoherent/RelativeAbsolute.lean#L229). The attribute's comment: “the case of schemes”.

> **Stacks 0DII, the case of schemes.** Let `f : X ⟶ Y` be a flat morphism of schemes locally of
> finite presentation and let `E` be an object of `D(𝒪_X)`. Then `E` is pseudo-coherent relative to
> `Y` in the sense of Stacks 09UI if and only if `E` is pseudo-coherent on `X` in the sheaf-level
> sense of Stacks 08CB.

```lean
public theorem isPseudoCoherent_iff_of_flat_of_locallyOfFinitePresentation {X Y : Scheme.{u}}
    (f : X ⟶ Y) [Flat f] [LocallyOfFinitePresentation f] (E : DerivedCategory X.Modules) :
    f.IsPseudoCoherent E ↔ RingedSpace.IsPseudoCoherent (X := X.toRingedSpace) E
```

**`AlgebraicGeometry.Space.isRelativelyPseudoCoherentFrom_iff_forall_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativeAbsolute.lean, line 1022](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativeAbsolute.lean#L1022). The attribute's comment: “the fixed-degree etale-chart localization: relative m-pseudo-coherence over Y is m-pseudo-coherence of RGamma(U, E) over O\_X(U) on every square of affine etale charts”.

> **Stacks 0DII in a fixed degree, by étale localization.** Let `f : X ⟶ Y` be a flat morphism
> of algebraic spaces over `S` which is locally of finite presentation, let `E` be an object of
> `D_QCoh(𝒪_X)` and let `m` be an integer.  Then `E` is `m`-pseudo-coherent relative to `Y` if and
> only if, on every commuting square of affine étale scheme charts `U` of `X` and `V` of `Y` over
> `f`, the complex `RΓ(U, E)` is `m`-pseudo-coherent over the ring `𝒪_X(U)`.
>
> Relative `m`-pseudo-coherence is by definition the relative condition on those same squares, so
> the two sides differ square by square only, and on one square the equivalence is
> `AlgebraicGeometry.Space.relativePseudoCoherence_chart_iff`.

```lean
theorem isRelativelyPseudoCoherentFrom_iff_forall_chart
    (hflat : IsFlat B S hS f) (hfp : IsLocallyOfFinitePresentation B S hS f)
    (E : QuasicoherentDerivedCategory.{u, u} B S hS X hX) (m : ℤ) :
    IsRelativelyPseudoCoherentFrom B S hS X hX f
        (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation B S hS hfp) E m ↔
      ∀ (U : SmallEtale B S hS X) (V : SmallEtale B S hS Y)
          (g : (SmallEtale.toOver B S hS X).obj U ⟶ (SmallEtale.toOver B S hS Y).obj V),
          yoneda.map g ≫ V.obj.hom = U.obj.hom ≫ f →
          IsAffine (chartScheme U) → IsAffine (chartScheme V) →
        StacksDraft.PseudoCoherence.IsPseudoCoherentFrom
          (chartDerivedSections B S hS X hX U E) m
```

**`AlgebraicGeometry.Space.isRelativelyPseudoCoherent_iff_forall_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativeAbsolute.lean, line 1049](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativeAbsolute.lean#L1049). The attribute's comment: “the etale-chart localization: pseudo-coherence relative to Y is pseudo-coherence of RGamma(U, E) over O\_X(U) on every square of affine etale charts”.

> **Stacks 0DII by étale localization.** Let `f : X ⟶ Y` be a flat morphism of algebraic
> spaces over `S` which is locally of finite presentation and let `E` be an object of
> `D_QCoh(𝒪_X)`.  Then `E` is pseudo-coherent relative to `Y` if and only if, on every commuting
> square of affine étale scheme charts `U` of `X` and `V` of `Y` over `f`, the complex `RΓ(U, E)`
> is pseudo-coherent over the ring `𝒪_X(U)` — the target playing no role.
>
> This is the all-degrees clause of
> `AlgebraicGeometry.Space.relativePseudoCoherence_chart_iff` on each of the squares that relative
> pseudo-coherence of Stacks 0CSY is tested on; see "What is proved, and what the right-hand side
> says" in the module docstring for the sense in which the right-hand side is the absolute
> condition.

```lean
theorem isRelativelyPseudoCoherent_iff_forall_chart
    (hflat : IsFlat B S hS f) (hfp : IsLocallyOfFinitePresentation B S hS f)
    (E : QuasicoherentDerivedCategory.{u, u} B S hS X hX) :
    IsRelativelyPseudoCoherent B S hS X hX f
        (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation B S hS hfp) E ↔
      ∀ (U : SmallEtale B S hS X) (V : SmallEtale B S hS Y)
          (g : (SmallEtale.toOver B S hS X).obj U ⟶ (SmallEtale.toOver B S hS Y).obj V),
          yoneda.map g ≫ V.obj.hom = U.obj.hom ≫ f →
          IsAffine (chartScheme U) → IsAffine (chartScheme V) →
        StacksDraft.PseudoCoherence.IsPseudoCoherent
          (chartDerivedSections B S hS X hX U E)
```

**`AlgebraicGeometry.Space.isRelativelyPseudoCoherent_iff_isPseudoCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativeAbsoluteChartDictionary.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/PseudoCoherent/RelativeAbsoluteChartDictionary.lean#L353).

> Let `S` be a scheme and let `f : X ⟶ Y` be a morphism of algebraic spaces over `S` which is
> flat and locally of finite presentation.  Let `E` be an object of `D_QCoh(𝒪_X)`.  Then `E` is
> pseudo-coherent relative to `Y` if and only if `E` is pseudo-coherent on `X`, the latter read on
> the small étale ringed site of `X`.
>
> This is
> `AlgebraicGeometry.Space.isRelativelyPseudoCoherent_iff_isPseudoCoherent_of_chartDictionary` at
> `AlgebraicGeometry.Space.chartPseudoCoherenceDictionaryFrom_holds` in every degree.  It is not the
> fixed-degree statement above read degree by degree: the all-degrees clause of Stacks 08FT (3) asks
> for one complex which is `m`-pseudo-coherent for every `m`, and the quantifier swap happens on the
> site side, inside that theorem.

```lean
public theorem isRelativelyPseudoCoherent_iff_isPseudoCoherent (f : X ⟶ Y)
    (hflat : IsFlat B S hS f.hom) (hfp : IsLocallyOfFinitePresentation B S hS f.hom)
    (E : QuasicoherentDerivedCategory.{u, u} B S hS X.1 X.2) :
    IsRelativelyPseudoCoherent B S hS X.1 X.2 f.hom
        (isLocallyOfFiniteType_of_isLocallyOfFinitePresentation B S hS hfp) E ↔
      (smallEtaleRingedSite B S hS X.1 X.2).IsPseudoCoherent E.obj
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.45, Tag 0CSV](https://stacks.math.columbia.edu/tag/0CSV)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
