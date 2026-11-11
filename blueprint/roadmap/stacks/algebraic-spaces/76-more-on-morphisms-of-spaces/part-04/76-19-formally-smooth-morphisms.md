---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.FormallySmooth, AlgebraicGeometry.Space.FormallySmooth.comp, AlgebraicGeometry.Space.FormallySmooth.baseChange, AlgebraicGeometry.formallyEtale_iff_formallySmooth_and_formallyUnramified, AlgebraicGeometry.Space.formallySmooth_of_isEtale_square, AlgebraicGeometry.Space.isSmooth_iff_isLocallyOfFinitePresentation_and_formallySmooth, AlgebraicGeometry.Space.isSmooth_of_isLocallyOfFinitePresentation_of_formallySmooth, AlgebraicGeometry.Space.isLocallyOfFinitePresentation_and_formallySmooth_of_isSmooth
statement: formalized
proof: formalized
---

# 76.19 Formally smooth morphisms

Section 76.19 of the Stacks Project, [Tag 049R](https://stacks.math.columbia.edu/tag/049R). 14 tags here are carried by 22 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 060G, a definition

[Tag 060G](https://stacks.math.columbia.edu/tag/060G) in the Stacks Project.

**`AlgebraicGeometry.Space.FormallySmooth`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Defs.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Defs.lean#L68). The attribute's comment: “formal smoothness of a morphism of algebraic spaces”. References: SGA 3 XI (1.6), “formally smooth”.

> **Stacks 049S, part (1).** Every commutative affine square against a
> square-zero closed immersion admits a lift.

```lean
public abbrev FormallySmooth {F G : (BigFppfOver B S hS)ᵒᵖ ⥤ Type v} (a : F ⟶ G) : Prop
```

## Tag 061E, a lemma

[Tag 061E](https://stacks.math.columbia.edu/tag/061E) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.FormallySmooth.comp`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Comp.lean#L48), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Spaces.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Spaces.lean#L68) (StacksFrontier).

## Tag 061F, a lemma

[Tag 061F](https://stacks.math.columbia.edu/tag/061F) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.Space.FormallySmooth.baseChange`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/BaseChange.lean#L227), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Spaces.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/Spaces.lean#L72) (StacksFrontier).

## Tag 061G, a lemma

[Tag 061G](https://stacks.math.columbia.edu/tag/061G) in the Stacks Project.

Declarations registered for the tag:

- [`AlgebraicGeometry.formallyEtale_iff_formallySmooth_and_formallyUnramified`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Etale/FormallyEtaleSmoothUnramified.lean#L46), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallyEtale/Basic.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallyEtale/Basic.lean#L121) (StacksFrontier): “the same equivalence for a morphism of schemes”.

## Tag 061H, a lemma

[Tag 061H](https://stacks.math.columbia.edu/tag/061H) in the Stacks Project.

**`AlgebraicGeometry.Space.formallySmooth_of_isEtale_square`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/EtaleSquare.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/EtaleSquare.lean#L56).

> **Stacks 061H.** Let `ψ : U ⟶ V`, `u : U ⟶ X`, `v : V ⟶ Y` and `f : X ⟶ Y` be morphisms of
> algebraic spaces over `S` forming a commuting square. If the two vertical arrows `u` and `v`
> are étale and `f` is formally smooth, then `ψ` is formally smooth.

```lean
theorem formallySmooth_of_isEtale_square
    (B : BigFppfSite.{u}) (S : Scheme.{u}) (hS : B.Contains S)
    {U V X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u}
    (hU : IsAlgebraicSpace B S hS U) (hV : IsAlgebraicSpace B S hS V)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y)
    (ψ : U ⟶ V) (u : U ⟶ X) (v : V ⟶ Y) (f : X ⟶ Y)
    (hsq : u ≫ f = ψ ≫ v)
    (hu : IsEtale B S hS u) (hv : IsEtale B S hS v)
    (hf : FormallySmooth f) :
    FormallySmooth ψ
```

## Tag 04AM, a lemma

[Tag 04AM](https://stacks.math.columbia.edu/tag/04AM) in the Stacks Project.

**`AlgebraicGeometry.Space.isSmooth_iff_isLocallyOfFinitePresentation_and_formallySmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/OfIsSmooth.lean, line 417](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/OfIsSmooth.lean#L417).

> **Stacks 04AM.** A morphism of algebraic spaces over `S` is smooth exactly when it is locally
> of finite presentation and formally smooth.

```lean
theorem isSmooth_iff_isLocallyOfFinitePresentation_and_formallySmooth
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    IsSmooth B S hS f ↔ IsLocallyOfFinitePresentation B S hS f ∧ FormallySmooth f
```

**`AlgebraicGeometry.Space.isSmooth_of_isLocallyOfFinitePresentation_of_formallySmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothFormallySmooth.lean, line 735](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothFormallySmooth.lean#L735). The attribute's comment: “condition (2) implies condition (1)”.

> **Stacks 04AM, the implication towards smoothness.** A morphism of algebraic spaces over
> `S` which is locally of finite presentation and formally smooth is smooth.
>
> Smoothness of `f` is a property of its étale charts, so there is nothing to descend: a chart
> `h : U ⟶ V` is locally of finite presentation by hypothesis, and
> `AlgebraicGeometry.Space.exists_lift_scheme_of_formallySmooth` solves every lifting problem for
> it along a first-order thickening of affine schemes *contained in the site*. That is exactly
> the hypothesis of `Stacks.Smooth.smooth_of_exists_lift_of_size_lt`, which upgrades it to
> smoothness: the only thickening the criterion needs is the spectrum of a polynomial
> presentation of the sections over an affine chart, and the site contains it.

```lean
theorem isSmooth_of_isLocallyOfFinitePresentation_of_formallySmooth
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} {f : X ⟶ Y}
    (hlfp : IsLocallyOfFinitePresentation B S hS f) (hf : FormallySmooth f) :
    IsSmooth B S hS f
```

**`AlgebraicGeometry.Space.isLocallyOfFinitePresentation_and_formallySmooth_of_isSmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothFormallySmooth.lean, line 758](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothFormallySmooth.lean#L758). The attribute's comment: “condition (1) implies condition (2), for a representable morphism”.

> **Stacks 04AM, the implication from smoothness, for a representable morphism.** A smooth
> representable morphism of algebraic spaces over `S` is locally of finite presentation and
> formally smooth.
>
> Local finite presentation is Tag 04AJ. For formal smoothness, smoothness of a representable
> morphism is smoothness of each of its base changes to an object of the site by Tag 03MJ, so the
> base change of `f` along a section `y` of the target over the thickened test object is a smooth
> morphism of schemes; the scheme case Tag 02H6 extends the section of that base change cut out
> by the given section of `X` over the test object, and the extension is a morphism of the site
> because the inclusion of the site into schemes is fully faithful.

```lean
theorem isLocallyOfFinitePresentation_and_formallySmooth_of_isSmooth
    {X Y : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) {f : X ⟶ Y}
    (hrep : yoneda.relativelyRepresentable f) (hf : IsSmooth B S hS f) :
    IsLocallyOfFinitePresentation B S hS f ∧ FormallySmooth f
```

## Tag 0CHJ, a lemma

[Tag 0CHJ](https://stacks.math.columbia.edu/tag/0CHJ) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_isEtaleCovering_lift_of_isSmooth_of_isThickeningHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmoothStrongLift.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmoothStrongLift.lean#L193).

> **Stacks 0CHJ.** Let `S` be a scheme and consider a commutative square of algebraic spaces
> over `S`
> ```
> X ←--a-- T
> |        |
> f        i
> ↓        ↓
> Y ←--b-- T'
> ```
> in which `f` is smooth and `i` is a thickening. Then there is an étale covering of `T'` by
> affine schemes `T'ₚ` of the site such that over each member the square can be filled in: there
> is a `ψ : T'ₚ ⟶ X` with `ψ` over `Y` equal to `T'ₚ ⟶ T' ⟶ Y` and with the restriction of `ψ` to
> `T ×_{T'} T'ₚ` equal to the restriction of `a`.
>
> The covering is indexed by the points of `T'`, and the member at a point contains that point.
>
> The proof follows the source, with the three reductions performed in one step for each member of
> the covering rather than globally. Write `Z = X ×_Y T'`; it is smooth over `T'` because `f` is,
> and the given data provide a section `σ : T ⟶ Z` of `Z ⟶ T'` over `T`. Given a point of `T'`,
> choose an affine étale chart `P` of `T'` through it (Stacks 03FX, in the pointwise form
> `AlgebraicGeometry.Space.exists_affine_etale_chart_at_point`) and let `J = T ×_{T'} P`, an affine
> scheme and a thickening of `P`. Pulling an atlas of `Z` back along `J ⟶ Z` and intersecting with
> the base change of `P` to that atlas produces an affine chart `U` of `Z` lying over `P` — so that
> `U ⟶ P` is a *smooth morphism of affine schemes*, since smoothness of `Z ⟶ T'` is exactly the
> condition on every square of étale charts — together with an étale `N ⟶ J` through the chosen
> point and a morphism `N ⟶ U` over `Z`. Topological invariance of the étale site (Stacks 039R, in
> the size-controlled cartesian form
> `AlgebraicGeometry.Space.exists_etaleLift_isPullback_of_chart`) lifts `N ⟶ J` to an étale
> `V ⟶ P` with `N = T ×_{T'} V`; shrinking `V` to an affine open through the point makes it affine,
> and `Stacks.Smooth.exists_lift_of_isClosedImmersion_of_surjective` — the geometric form of
> Algebra, Lemma 10.138.17 — then extends `T ×_{T'} V' ⟶ U` over the thickening to `V' ⟶ U`. The
> member of the covering is `V'`, and `ψ` is `V' ⟶ U ⟶ Z ⟶ X`.

```lean
theorem exists_isEtaleCovering_lift_of_isSmooth_of_isThickeningHom
    {X Y T T' : AlgebraicSpaces B S hS} {f : X ⟶ Y} (hf : IsSmooth B S hS f.hom)
    {i : T ⟶ T'} (hi : IsThickeningHom B S hS i) (a : T ⟶ X) (b : T' ⟶ Y)
    (hcomm : a ≫ f = i ≫ b) :
    ∃ (Z : points B S hS T'.obj → BigFppfOver B S hS)
      (q : ∀ p, yoneda.obj (Z p) ⟶ T'.obj),
      (∀ p, IsAffine ((BigFppfOver.toScheme B S hS).obj (Z p))) ∧
      IsEtaleCovering B S hS (fun p ↦ yoneda.obj (Z p)) q ∧
      ∀ p, ∃ ψ : yoneda.obj (Z p) ⟶ X.obj,
        ψ ≫ f.hom = q p ≫ b.hom ∧
        pullback.snd i.hom (q p) ≫ ψ = pullback.fst i.hom (q p) ≫ a.hom
```

## Tag 061I, a lemma

[Tag 061I](https://stacks.math.columbia.edu/tag/061I) in the Stacks Project.

**`AlgebraicGeometry.isLocallyProjective_relativeDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallySmooth/Differentials.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FormallySmooth/Differentials.lean#L78). The attribute's comment: “for morphisms of schemes”. References: EGA IV (17.2.3), “(i) locally projective”.

> **Stacks 06B5.** The sheaf of relative differentials of a formally smooth morphism of
> schemes is locally projective on its source. This is **Stacks 061I** for a morphism of
> algebraic spaces that is a morphism of schemes.

```lean
theorem isLocallyProjective_relativeDifferentials {X S : Scheme.{u}} {f : X ⟶ S}
    (hf : FormallySmooth f) :
    Scheme.Modules.IsLocallyProjective (Scheme.Hom.relativeDifferentials f)
```

**`AlgebraicGeometry.Space.isLocallyProjective_sheafOfDifferentials`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsLocallyProjective.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsLocallyProjective.lean#L206).

> **Stacks 061I.**  The sheaf of relative differentials `Ω_{X/Y}` of a formally smooth
> morphism `f : X ⟶ Y` of algebraic spaces over a scheme `S` is locally projective on `X`.

```lean
theorem isLocallyProjective_sheafOfDifferentials {X Y : AlgebraicSpaces B S hS} (f : X ⟶ Y)
    (hf : FormallySmooth f.hom) :
    IsLocallyProjective B S hS X.2
      ⟨sheafOfDifferentials B S hS f, isQuasicoherentOnSite_sheafOfDifferentials B S hS f⟩
```

## Tag 061J, a lemma

[Tag 061J](https://stacks.math.columbia.edu/tag/061J) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.subsingleton_sheafH_one_sheafHom_associatedModule`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/InternalHomAffineVanishing.lean, line 341](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/InternalHomAffineVanishing.lean#L341).

> **Stacks 061J for an associated module.**  Let `T` be an affine scheme and let `M` be a
> locally projective quasi-coherent `𝒪_T`-module.  The first cohomology of the internal hom from
> the associated module `M^a` to an `𝒪`-module `𝓖` on the small étale site of `T` vanishes.

```lean
public theorem subsingleton_sheafH_one_sheafHom_associatedModule
    [AlgebraicGeometry.IsAffine T] (M : T.Modules)
    [M.IsQuasicoherent] (hM : Scheme.Modules.IsLocallyProjective M)
    (G : SheafOfModules.{u} (structureSheaf B T hT)) [G.IsQuasicoherentOnSite] :
    Subsingleton (Sheaf.H.{w}
      ((SheafOfModules.toSheaf (structureSheaf B T hT)).obj
        (sheafHom B T hT ((associatedModule B T hT).obj M) G)) 1)
```

**`AlgebraicGeometry.SmallEtale.subsingleton_sheafH_one_sheafHom_of_isLocallyProjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/InternalHomAffineVanishing.lean, line 357](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/InternalHomAffineVanishing.lean#L357).

> **Stacks 061J.**  Let `T` be an affine scheme and let `𝓕` and `𝓖` be quasi-coherent
> `𝒪`-modules on the small étale site of `T`.  If `𝓕` is locally projective — that is, if its
> restriction to the small Zariski site of `T` is a locally projective `𝒪_T`-module, which is what
> Stacks 060R defines local projectivity to mean — then the first cohomology of the internal hom
> `𝓗om_𝒪(𝓕, 𝓖)` vanishes.

```lean
public theorem subsingleton_sheafH_one_sheafHom_of_isLocallyProjective
    [AlgebraicGeometry.IsAffine T]
    (F G : SheafOfModules.{u} (structureSheaf B T hT)) [F.IsQuasicoherentOnSite]
    [G.IsQuasicoherentOnSite]
    (hF : Scheme.Modules.IsLocallyProjective ((restrictModule B T hT).obj F)) :
    Subsingleton (Sheaf.H.{w}
      ((SheafOfModules.toSheaf (structureSheaf B T hT)).obj (sheafHom B T hT F G)) 1)
```

## Tag 061K, a lemma

[Tag 061K](https://stacks.math.columbia.edu/tag/061K) in the Stacks Project.

**`AlgebraicGeometry.Space.formallySmooth_tfae_etaleCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/ChartGlue/Main061K.lean, line 316](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/ChartGlue/Main061K.lean#L316).

> For a morphism `f : X ⟶ Y` of algebraic spaces over `S`, the following are equivalent:
> 1. `f` is formally smooth;
> 2. for every commuting square of étale scheme charts `a : U ⟶ X`, `b : V ⟶ Y`, `ψ : U ⟶ V`, the
>    morphism of schemes `ψ` is formally smooth;
> 3. there is a commuting square of étale scheme charts with `a` and `b` surjective and `ψ`
>    formally smooth.

```lean
theorem formallySmooth_tfae_etaleCharts (hX : IsAlgebraicSpace B S hS X)
    (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    List.TFAE [FormallySmooth f,
      HoldsOnEveryEtaleChart B S hS (@Stacks.Smooth.FormallySmoothScheme.{u}) f,
      ∃ (U V : BigFppfOver B S hS) (a : yoneda.obj U ⟶ X) (b : yoneda.obj V ⟶ Y) (ψ : U ⟶ V),
        (MorphismProperty.inverseImage (@AlgebraicGeometry.Etale.{u} : MorphismProperty
          Scheme.{u}) (BigFppfOver.toScheme B S hS)).presheaf a ∧
        (MorphismProperty.inverseImage (@AlgebraicGeometry.Etale.{u} : MorphismProperty
          Scheme.{u}) (BigFppfOver.toScheme B S hS)).presheaf b ∧
        (MorphismProperty.inverseImage (@AlgebraicGeometry.Surjective.{u} : MorphismProperty
          Scheme.{u}) (BigFppfOver.toScheme B S hS)).presheaf a ∧
        (MorphismProperty.inverseImage (@AlgebraicGeometry.Surjective.{u} : MorphismProperty
          Scheme.{u}) (BigFppfOver.toScheme B S hS)).presheaf b ∧
        yoneda.map ψ ≫ b = a ≫ f ∧
        Stacks.Smooth.FormallySmoothScheme ((BigFppfOver.toScheme B S hS).map ψ)]
```

**`AlgebraicGeometry.Space.formallySmooth_iff_etaleCharts`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmoothChartBiconditional.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmoothChartBiconditional.lean#L282). The attribute's comment: “condition (2), granted Stacks 0D0F (3) ⟹ (1) and the pseudo-torsor triviality of 03AJ”.

> **Stacks 061K, the equivalence of (1) and (2).** A morphism of algebraic spaces over `S` is
> formally smooth exactly when the morphism of schemes underlying every commuting square of étale
> scheme charts is formally smooth, granted the scheme-level implication (3) ⟹ (1) of
> [Stacks Project, Tag 0D0F] and the triviality of the pseudo-torsor of lifts.

```lean
theorem formallySmooth_iff_etaleCharts
    (h0D0F : ∀ {X' Y' : Scheme.{u}} (g : X' ⟶ Y'),
      Stacks.Smooth.FormallySmoothAffineLocally g → Stacks.Smooth.FormallySmoothScheme g)
    (hGlue : ∀ {X' Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : X' ⟶ Y'),
      IsAlgebraicSpace B S hS X' → IsAlgebraicSpace B S hS Y' →
      FormallySmoothEtaleLocally B S hS g → FormallySmooth g)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    FormallySmooth f ↔
      HoldsOnEveryEtaleChart B S hS (@Stacks.Smooth.FormallySmoothScheme.{u}) f
```

**`AlgebraicGeometry.Space.formallySmooth_iff_surjectiveEtaleChart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmoothChartBiconditional.lean, line 305](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmoothChartBiconditional.lean#L305). The attribute's comment: “condition (3), granted Stacks 0D0F (3) ⟹ (1) and the pseudo-torsor triviality of 03AJ”.

> **Stacks 061K, the equivalence of (1) and (3).** A morphism of algebraic spaces over `S` is
> formally smooth exactly when there is one commuting square of étale scheme charts, both chart
> maps surjective, whose underlying morphism of schemes is formally smooth, granted the
> scheme-level implication (3) ⟹ (1) of [Stacks Project, Tag 0D0F] and the triviality of the
> pseudo-torsor of lifts.

```lean
theorem formallySmooth_iff_surjectiveEtaleChart
    (h0D0F : ∀ {X' Y' : Scheme.{u}} (g : X' ⟶ Y'),
      Stacks.Smooth.FormallySmoothAffineLocally g → Stacks.Smooth.FormallySmoothScheme g)
    (hGlue : ∀ {X' Y' : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (g : X' ⟶ Y'),
      IsAlgebraicSpace B S hS X' → IsAlgebraicSpace B S hS Y' →
      FormallySmoothEtaleLocally B S hS g → FormallySmooth g)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y) :
    FormallySmooth f ↔
      ∃ (U V : BigFppfOver B S hS) (a : yoneda.obj U ⟶ X) (b : yoneda.obj V ⟶ Y) (ψ : U ⟶ V),
        (MorphismProperty.inverseImage (@AlgebraicGeometry.Etale.{u} : MorphismProperty
          Scheme.{u}) (BigFppfOver.toScheme B S hS)).presheaf a ∧
        (MorphismProperty.inverseImage (@AlgebraicGeometry.Etale.{u} : MorphismProperty
          Scheme.{u}) (BigFppfOver.toScheme B S hS)).presheaf b ∧
        (MorphismProperty.inverseImage (@AlgebraicGeometry.Surjective.{u} : MorphismProperty
          Scheme.{u}) (BigFppfOver.toScheme B S hS)).presheaf a ∧
        (MorphismProperty.inverseImage (@AlgebraicGeometry.Surjective.{u} : MorphismProperty
          Scheme.{u}) (BigFppfOver.toScheme B S hS)).presheaf b ∧
        yoneda.map ψ ≫ b = a ≫ f ∧
        Stacks.Smooth.FormallySmoothScheme ((BigFppfOver.toScheme B S hS).map ψ)
```

## Tag 06CS, a lemma

[Tag 06CS](https://stacks.math.columbia.edu/tag/06CS) in the Stacks Project.

**`AlgebraicGeometry.Space.formallySmooth_isLocalAtTarget_fpqc'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/FpqcLocalAtTarget.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmooth/FpqcLocalAtTarget.lean#L55).

> Formal smoothness of morphisms of algebraic spaces over `S` is local on the base for the fpqc
> topology of Stacks 03YH: for every fpqc covering `{Yᵢ ⟶ Y}` of algebraic spaces, a morphism
> `f : X ⟶ Y` is formally smooth if and only if every base change `X ×_Y Yᵢ ⟶ Yᵢ` is.

```lean
theorem formallySmooth_isLocalAtTarget_fpqc' (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) :
    (formallySmoothProperty B S hS).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

**`AlgebraicGeometry.Space.formallySmooth_isLocalAtTarget_fpqc_of_chartDescent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmoothFpqcLocalAtTarget.lean, line 389](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmoothFpqcLocalAtTarget.lean#L389). The attribute's comment: “granting the implication (3) ⟹ (1) of Stacks 061K with condition (3) read on affine opens; the library's own Stacks 061K is itself conditional on the implication (3) ⟹ (1) of Stacks 0D0F and on the pseudo-torsor triviality of Stacks 03AJ, and this grant is implied by those two, so it is the weaker assumption”.

> **Stacks 06CS, granting the implication (3) ⟹ (1) of Stacks 061K.** Formal smoothness of
> morphisms of algebraic spaces over `S` is local on the base for the fpqc topology of
> Stacks 03YH.
>
> The ascent half is Stacks 049U. For the descent half, a lifting problem for `f : X ⟶ Y` is one
> for the base change of `f` along a point of `Y` with affine source
> (`AlgebraicGeometry.Space.formallySmooth_iff_affine_pullback`); over such a point the fpqc
> condition of Stacks 03MQ supplies a finite family of affine objects covering it and refining the
> given covering, and `AlgebraicGeometry.Space.formallySmooth_of_affineFpqcPresieve` descends along
> that family.

```lean
theorem formallySmooth_isLocalAtTarget_fpqc_of_chartDescent (B : BigFppfSite.{u})
    (S : Scheme.{u}) (hS : B.Contains S) (hchart : FormallySmoothEtaleChartDescent B S hS) :
    (formallySmoothProperty B S hS).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

**`AlgebraicGeometry.Space.formallySmooth_isLocalAtTarget_fpqc`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/FormallySmoothFpqcLocalAtTarget.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/FormallySmoothFpqcLocalAtTarget.lean#L432). The attribute's comment: “granting the implication (3) ⟹ (1) of Stacks 061K with condition (3) read on affine opens; the library's own Stacks 061K is itself conditional on the implication (3) ⟹ (1) of Stacks 0D0F and on the pseudo-torsor triviality of Stacks 03AJ, and this grant is implied by those two, so it is the weaker assumption”.

> **Stacks 06CS.** Formal smoothness of morphisms of algebraic spaces over `S` is local on the
> base for the fpqc topology of Stacks 03YH.
>
> The one input not available in this library is the implication (3) ⟹ (1) of Stacks 061K, read on
> affine opens, which is carried as the instance hypothesis
> `AlgebraicGeometry.Space.FormallySmoothEtaleChartDescent`; see
> `AlgebraicGeometry.Space.formallySmooth_isLocalAtTarget_fpqc_of_chartDescent`, where it appears
> as an explicit hypothesis, for the argument.

```lean
instance formallySmooth_isLocalAtTarget_fpqc (B : BigFppfSite.{u}) (S : Scheme.{u})
    (hS : B.Contains S) [hchart : FormallySmoothEtaleChartDescent B S hS] :
    (formallySmoothProperty B S hS).IsLocalAtTarget
      (Topology.precoverage.{u, v} .fpqc B S hS)
```

## Tag 06BI, a lemma

[Tag 06BI](https://stacks.math.columbia.edu/tag/06BI) in the Stacks Project.

**`AlgebraicGeometry.Space.triangleDifferentials_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/RelativeDifferentialsShortExact.lean, line 264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/RelativeDifferentialsShortExact.lean#L264). The attribute's comment: “granted as `hchart` the étale localization of 04CU and 04CS identifying the restriction of the comparison map of Ω to a surjective étale chart with the chart morphisms' own comparison map of Ω”.

> **Stacks 06BI.** For morphisms `f : X ⟶ Y` and `g : Y ⟶ B` of algebraic spaces over `S`
> with `f` formally smooth, the transitivity sequence
> `0 ⟶ f^*Ω_{Y/B} ⟶ Ω_{X/B} ⟶ Ω_{X/Y} ⟶ 0` of Stacks 05Z8 is short exact.
>
> Short exactness adds monomorphy of the first map to the three clauses of Stacks 05Z8, and
> `AlgebraicGeometry.Space.pullbackDifferentialsMap_mono_of_formallySmooth` supplies it from the
> case of schemes by étale localization, granted the chart comparison.

```lean
theorem triangleDifferentials_shortExact (f : X ⟶ Y) (g : Y ⟶ Z) (hf : FormallySmooth f.hom)
    (hchart : PullbackDifferentialsMapChartComparison B S hS f g) :
    ∃ h : pullbackDifferentialsMap B S hS f g ≫ toRelativeDifferentials B S hS f g = 0,
      (ShortComplex.mk _ _ h).ShortExact
```

**`AlgebraicGeometry.Space.triangleDifferentials_shortExact_of_formallySmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsSchemeComparisonMapSquare.lean, line 570](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SheafOfDifferentialsSchemeComparisonMapSquare.lean#L570).

> **Stacks 06BI.** Let `f : X ⟶ Y` and `g : Y ⟶ Z` be morphisms of algebraic spaces over `S`
> with `f` formally smooth.  Then the sequence `0 ⟶ f^*Ω_{Y/Z} ⟶ Ω_{X/Z} ⟶ Ω_{X/Y} ⟶ 0` of
> Stacks 05Z8 is short exact.
>
> The first map is a monomorphism étale locally: on compatible étale charts `U ⟶ V ⟶ W` with
> `U ⟶ V` formally smooth (Stacks 061K) it is the scheme statement (Stacks 02HP), carried to the
> spaces by Stacks 04CU and 04CS
> (`AlgebraicGeometry.Space.pullbackDifferentialsMapSchemeSpaceComparison`); exactness at the other
> two terms is Stacks 05Z8.

```lean
theorem triangleDifferentials_shortExact_of_formallySmooth (f : X ⟶ Y) (g : Y ⟶ Z)
    (hf : FormallySmooth f.hom) :
    ∃ h : pullbackDifferentialsMap B S hS f g ≫ toRelativeDifferentials B S hS f g = 0,
      (ShortComplex.mk _ _ h).ShortExact
```

## Tag 06BJ, a lemma

[Tag 06BJ](https://stacks.math.columbia.edu/tag/06BJ) in the Stacks Project.

**`AlgebraicGeometry.Space.IsUniversalFirstOrderThickening.conormalSequence_shortExact_of_formallySmooth`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceFormallySmoothShortExact.lean, line 190](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceFormallySmoothShortExact.lean#L190).

> **Stacks 06BJ.**  Let `h = ι ≫ h' : Z ⟶ X` be a formally unramified morphism of algebraic
> spaces over `Y`, with universal first order thickening `Z ⊂ Z'` over `X` given by `hZ`, and
> assume `Z` is formally smooth over `Y`.  Then the canonical exact sequence
> ```
>   0 ⟶ 𝒞_{Z/X} ⟶ h^*Ω_{X/Y} ⟶ Ω_{Z/Y} ⟶ 0
> ```
> of Stacks 060F, `AlgebraicGeometry.Space.IsUniversalFirstOrderThickening.conormalSequence`, is
> short exact.
>
> Exactness at the middle and the epimorphism on the right are Stacks 060F.  The first arrow
> followed by the isomorphism of Stacks 060E is the first arrow of Stacks 05ZA for `Z ⊂ Z'`, which
> is a monomorphism by `AlgebraicGeometry.Space.mono_conormalSequenceFirstMap_of_formallySmooth`.

```lean
theorem conormalSequence_shortExact_of_formallySmooth
    (hZ : IsUniversalFirstOrderThickening B S hS Z h') (p : X ⟶ Y)
    (hsm : FormallySmooth (universalThickeningInclusion B S hS hZ ≫ h' ≫ p).hom) :
    ShortComplex.ShortExact (C := Modules.{u, u} B S hS (universalThickeningSubSpace B S hS hZ).obj
      (universalThickeningSubSpace B S hS hZ).property) (hZ.conormalSequence B S hS p)
```

## Tag 06BK, a lemma

[Tag 06BK](https://stacks.math.columbia.edu/tag/06BK) in the Stacks Project.

**`AlgebraicGeometry.Space.exists_retraction_modulePullback_conormalMap_universalThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceUnramifiedPairSplitting.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceUnramifiedPairSplitting.lean#L307). The attribute's comment: “the first arrow of the conormal sequence is split over an affine étale chart”.

> **Stacks 06BK: the first arrow of the conormal sequence is étale-locally split.**  Let
> `i : Z ⟶ X` and `j : Z ⟶ Y` sit in a commutative triangle `i ≫ g = j` with `g` formally
> smooth, let `Z ⊂ Z'` be a universal first-order thickening of `Z` over `X` and `Z ⊂ Z''` one of
> `Z` over `Y`, and let `V ⟶ Z''` be an étale chart with `V` affine.  Then the inverse image
> along the projection `Z ×_{Z''} V ⟶ Z` of the first arrow `𝒞_{Z/Y} ⟶ 𝒞_{Z/X}` of the conormal
> sequence of [Stacks Project, Tag 06BE] admits a retraction.
>
> The first arrow is named here through its definition: it is the conormal map of
> [Stacks Project, Tag 04CP] for the square of [Stacks Project, Tag 060A] built from the canonical
> morphism `Z' ⟶ Z''` and the identification of the two smaller spaces, which is what
> `AlgebraicGeometry.Space.universalThickeningConormalMap` abbreviates.

```lean
theorem exists_retraction_modulePullback_conormalMap_universalThickening (g : X ⟶ Y)
    {i : Z ⟶ X} {j : Z ⟶ Y} (hij : i ≫ g = j)
    (ti : UniversalFirstOrderThickening B S hS i)
    (tj : UniversalFirstOrderThickening B S hS j) (hg : FormallySmooth g.hom)
    (V : BigFppfOver B S hS) (v : yoneda.obj V ⟶ tj.ambient.obj) (hv : IsEtale B S hS v)
    (hV : IsAffine ((BigFppfOver.toScheme B S hS).obj V)) :
    ∃ r, (modulePullback B S hS (thickeningChartProjection B S hS ti tj V v)).map
        (@conormalMap B S hS ti.ambient tj.ambient ti.closedSub tj.closedSub
          (universalThickeningComparison B S hS g hij ti tj)
          (ObjectProperty.homMk (universalThickeningSourceMap B S hS ti tj))
          (universalThickeningComparison_square B S hS g hij ti tj)) ≫ r = 𝟙 _
```

**`AlgebraicGeometry.Space.exists_retraction_cover_modulePullback_conormalMap_universalThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceUnramifiedPairSplitting.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceUnramifiedPairSplitting.lean#L405). The attribute's comment: “the first arrow of the conormal sequence is split over a covering by affine étale charts”.

> **Stacks 06BK, in a covering form.**  Under the hypotheses of
> `AlgebraicGeometry.Space.exists_retraction_modulePullback_conormalMap_universalThickening`, an
> arbitrary étale chart `V ⟶ Z''` is covered by affine étale charts over whose chart of `Z` the
> first arrow of the conormal sequence admits a retraction.

```lean
theorem exists_retraction_cover_modulePullback_conormalMap_universalThickening (g : X ⟶ Y)
    {i : Z ⟶ X} {j : Z ⟶ Y} (hij : i ≫ g = j)
    (ti : UniversalFirstOrderThickening B S hS i)
    (tj : UniversalFirstOrderThickening B S hS j) (hg : FormallySmooth g.hom)
    (V : BigFppfOver B S hS) (v : yoneda.obj V ⟶ tj.ambient.obj) (hv : IsEtale B S hS v) :
    ∃ (I : Type u) (V' : I → BigFppfOver B S hS) (π : ∀ k, V' k ⟶ V),
      Sieve.generate (Presieve.ofArrows V' π) ∈ BigFppfOver.topology B S hS V ∧
        ∀ k, ∃ r, (modulePullback B S hS
              (thickeningChartProjection B S hS ti tj (V' k) (yoneda.map (π k) ≫ v))).map
            (@conormalMap B S hS ti.ambient tj.ambient ti.closedSub tj.closedSub
              (universalThickeningComparison B S hS g hij ti tj)
              (ObjectProperty.homMk (universalThickeningSourceMap B S hS ti tj))
              (universalThickeningComparison_square B S hS g hij ti tj)) ≫ r = 𝟙 _
```

**`AlgebraicGeometry.Space.mono_conormalMap_universalThickening`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceUnramifiedPairSplitting.lean, line 438](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ConormalSequenceUnramifiedPairSplitting.lean#L438). The attribute's comment: “the conormal sequence is exact on the left”.

> **Stacks 06BK: the conormal sequence is exact on the left.**  Let `i : Z ⟶ X` and
> `j : Z ⟶ Y` sit in a commutative triangle `i ≫ g = j` with `g` formally smooth, and let
> `Z ⊂ Z'` be a universal first-order thickening of `Z` over `X` and `Z ⊂ Z''` one of `Z` over
> `Y`.  Then the first arrow `𝒞_{Z/Y} ⟶ 𝒞_{Z/X}` of the conormal sequence of
> [Stacks Project, Tag 06BE] is a monomorphism.
>
> The first arrow is named through its definition, as the conormal map of
> [Stacks Project, Tag 04CP] for the square of [Stacks Project, Tag 060A]; see the implementation
> notes of this file.  It is split injective over each affine étale chart of `Z''` by
> `AlgebraicGeometry.Space.exists_retraction_modulePullback_conormalMap_universalThickening`, and
> the charts of `Z` cut out by the affine étale charts of an atlas of `Z''` form an étale covering
> of `Z`, so the two inverse images of a pair of morphisms it equalises agree on that covering and
> the pair is equal.

```lean
theorem mono_conormalMap_universalThickening (g : X ⟶ Y) {i : Z ⟶ X} {j : Z ⟶ Y}
    (hij : i ≫ g = j) (ti : UniversalFirstOrderThickening B S hS i)
    (tj : UniversalFirstOrderThickening B S hS j) (hg : FormallySmooth g.hom) :
    Mono (@conormalMap B S hS ti.ambient tj.ambient ti.closedSub tj.closedSub
      (universalThickeningComparison B S hS g hij ti tj)
      (ObjectProperty.homMk (universalThickeningSourceMap B S hS ti tj))
      (universalThickeningComparison_square B S hS g hij ti tj))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 76.19, Tag 049R](https://stacks.math.columbia.edu/tag/049R)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
