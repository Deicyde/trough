---
declaration: section
origin: cited
lean: AlgebraicGeometry.isSchemeTheoreticallyDense_preimage, AlgebraicGeometry.Space.isSchemeTheoreticallyDense_iff_exists_surjective_etale_chart, AlgebraicGeometry.Space.schemeTheoreticClosure, AlgebraicGeometry.Space.IsSchemeTheoreticallyDense, AlgebraicGeometry.Space.isSchemeTheoreticallyDense_iff_schemeTheoreticClosure_eq_top, AlgebraicGeometry.Space.isSchemeTheoreticallyDense_iff_mono_fSharp, AlgebraicGeometry.Space.isSchemeTheoreticallyDense_inf, AlgebraicGeometry.Space.isOpenImmersion_and_dense_toSchemeTheoreticImage_of_qc_or_reduced
statement: formalized
proof: formalized
---

# 67.17 Scheme theoretic closure and density

Section 67.17 of the Stacks Project, [Tag 0831](https://stacks.math.columbia.edu/tag/0831). 8 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0832, a lemma

[Tag 0832](https://stacks.math.columbia.edu/tag/0832) in the Stacks Project.

**`AlgebraicGeometry.isSchemeTheoreticallyDense_preimage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Closure/DensePreimageQuasiFinite.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Morphisms/Closure/DensePreimageQuasiFinite.lean#L322). References: EGA IV (20.5.7), “special case”.

> **Stacks 0832.** The inverse image of a scheme-theoretically dense open subscheme under a
> morphism of schemes which is flat, locally of finite presentation and locally quasi-finite is
> scheme-theoretically dense.

```lean
public theorem isSchemeTheoreticallyDense_preimage {X S : Scheme.{u}} (f : X ⟶ S)
    [Flat f] [LocallyOfFinitePresentation f] [LocallyQuasiFinite f]
    {W : S.Opens} (hW : Scheme.Opens.IsSchemeTheoreticallyDense W) :
    Scheme.Opens.IsSchemeTheoreticallyDense (f ⁻¹ᵁ W)
```

## Tag 0833, a lemma

[Tag 0833](https://stacks.math.columbia.edu/tag/0833) in the Stacks Project.

**`AlgebraicGeometry.Space.isSchemeTheoreticallyDense_iff_exists_surjective_etale_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticDensity/ChartCriterion.lean, line 183](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticDensity/ChartCriterion.lean#L183).

> **Stacks 0833.** Let `U` be an open subspace of an algebraic space `X` over a scheme `S`
> contained in a big fppf site `B`. Then `U` is scheme-theoretically dense in `X` -- the
> scheme-theoretic closure of `U ×_X V` in `V` is all of `V` for every étale morphism `V ⟶ X` of
> algebraic spaces over `S` -- if and only if there are a scheme `V` and a surjective étale
> morphism `φ : V ⟶ X` for which that holds over the open subschemes of `V` alone: the
> scheme-theoretic closure of `U ×_X W` in `W` is all of `W` for every open subscheme `W` of `V`.
> The second condition says exactly that the open subscheme `U ×_X V` of `V` is
> scheme-theoretically dense in the sense of Stacks 01RB.
>
> The first condition trivially implies the second, since the composite of an open immersion with
> an étale morphism is étale. For the converse let `C` be an étale scheme chart of `X`; by
> `AlgebraicGeometry.Space.isSchemeTheoreticallyDense_iff_forall_chart` it suffices to make the
> scheme-theoretic closure of `U ×_X C` in `C` everything, and the two conditions are compared
> over `T = V ×_X C`. The projection `T ⟶ V` is a base change of the étale chart `C`, hence étale
> and so flat, locally of finite presentation and locally quasi-finite, so Stacks 0832 carries
> scheme-theoretic density of `U ×_X V` in `V` to scheme-theoretic density of `U ×_X T` in `T`;
> chartwise this is read through
> `AlgebraicGeometry.Space.schemeTheoreticImageSubfunctor_preimage_eq_top_iff`, which identifies
> closures of inverse images with scheme-theoretic dominance of the representing morphisms of
> schemes. The projection `T ⟶ C` is a base change of `φ`, hence surjective étale, and
> `AlgebraicGeometry.Space.subfunctor_eq_top_of_isSurjective_isEtale_preimage` descends the
> closure over `T` to the closure over `C`.
>
> Scheme-theoretic density of `U ×_X V` in `V`, rather than merely the equality of the
> scheme-theoretic closure of `U ×_X V` with `V`, is what the second condition has to say, and
> the source's literal reading of it is false. Take for `X` a scheme and for `φ` the identity,
> which is a surjective étale morphism from a scheme: the literal reading of condition (2) is
> then exactly that the scheme-theoretic closure of `U` in `X` is `X`, whereas condition (1),
> applied to the open immersions `W ⟶ X` -- which are étale -- is exactly that `U` is a
> scheme-theoretically dense open subscheme of `X` in the sense of Stacks 01RB. Stacks 01RC
> exhibits an affine scheme `X = Spec(k[x, z₁, z₂, …]/(xⁿzₙ))` and an open `U = X ∖ V(z₁, z₂, …)`
> with the former but not the latter: the closure is `X` because `A ⟶ ∏ₙ A_{zₙ}` is injective,
> while `U` is not even topologically dense in `X`, hence not scheme-theoretically dense. The
> literal reading would moreover make the quasi-compactness hypothesis of Stacks 0835
> superfluous, and contradict the remark that follows Stacks 0834. By Stacks 01RD the two
> readings agree exactly when the inclusion is quasi-compact, and it is the density form that
> Stacks 0832 transports.
>
> The part of the source's argument for (2) implies (1) that does hold for the bare equality is
> `AlgebraicGeometry.Space.schemeTheoreticClosure_eq_top_of_isSurjective_isEtale`: a surjective
> étale chart over which the scheme-theoretic closure of the inverse image is everything already
> forces the scheme-theoretic closure of `U` in `X` to be everything.

```lean
theorem isSchemeTheoreticallyDense_iff_exists_surjective_etale_chart
    (hX : IsAlgebraicSpace B S hS X) (U : Subfunctor X) (hU : IsOpenSubspace B S hS U) :
    IsSchemeTheoreticallyDense B S hS U ↔
      ∃ (V : BigFppfOver B S hS) (φ : yoneda.obj V ⟶ X),
        IsSurjective B S hS φ ∧ IsEtale B S hS φ ∧
          ∀ (W : BigFppfOver B S hS) (ψ : W ⟶ V),
            AlgebraicGeometry.IsOpenImmersion ((BigFppfOver.toScheme B S hS).map ψ) →
              schemeTheoreticClosure B S hS (U.preimage (yoneda.map ψ ≫ φ)) = ⊤
```

## Tag 0834, a definition

[Tag 0834](https://stacks.math.columbia.edu/tag/0834) in the Stacks Project.

**`AlgebraicGeometry.Space.schemeTheoreticClosure`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticDensity/Density.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticDensity/Density.lean#L38). The attribute's comment: “part (1): the scheme-theoretic closure of an open subspace”.

> **Stacks 0834, part (1).** The *scheme-theoretic closure* of a subspace `U` of an algebraic
> space `X` over `S` is the scheme-theoretic image of Stacks 082X of its inclusion.

```lean
abbrev schemeTheoreticClosure (U : Subfunctor X) : Subfunctor X
```

**`AlgebraicGeometry.Space.IsSchemeTheoreticallyDense`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticDensity/Density.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticDensity/Density.lean#L49). The attribute's comment: “part (2): scheme-theoretic density of an open subspace”. References: EGA IV (11.10.2), “single open subspace”.

> **Stacks 0834, part (2).** An open subspace `U` of an algebraic space `X` over `S` is
> *scheme-theoretically dense in `X`* when, for every étale morphism `φ : V ⟶ X` of algebraic
> spaces over `S`, the scheme-theoretic closure of `U ×_X V` in `V` is all of `V`.
>
> This is the first of the equivalent conditions of Stacks 0833, and is in general strictly
> stronger than the scheme-theoretic closure of `U` itself being all of `X`.

```lean
def IsSchemeTheoreticallyDense (U : Subfunctor X) : Prop
```

## Tag 0835, a lemma

[Tag 0835](https://stacks.math.columbia.edu/tag/0835) in the Stacks Project.

**`AlgebraicGeometry.Space.isSchemeTheoreticallyDense_iff_schemeTheoreticClosure_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompactSchemeTheoreticDensity.lean, line 114](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/QuasiCompactSchemeTheoreticDensity.lean#L114).

> Let `S` be a scheme contained in a big fppf site `B`, let `X` be an algebraic space over `S`
> and let `U ⊆ X` be an open subspace. If the inclusion `U ⟶ X` is quasi-compact, then `U` is
> scheme-theoretically dense in `X` if and only if the scheme-theoretic closure of `U` in `X` is
> `X`.

```lean
theorem isSchemeTheoreticallyDense_iff_schemeTheoreticClosure_eq_top
    (hX : IsAlgebraicSpace B S hS X) (U : Subfunctor X) (hU : IsOpenSubspace B S hS U)
    (hqc : IsQuasiCompact B S hS U.ι) :
    IsSchemeTheoreticallyDense B S hS U ↔ schemeTheoreticClosure B S hS U = ⊤
```

## Tag 0836, a lemma

[Tag 0836](https://stacks.math.columbia.edu/tag/0836) in the Stacks Project.

**`AlgebraicGeometry.Space.isSchemeTheoreticallyDense_iff_mono_fSharp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticDensity/Density.lean, line 118](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticDensity/Density.lean#L118).

> **Stacks 0836.** Let `j : U ⟶ X` be an open immersion of algebraic spaces over a scheme
> `S` contained in a big fppf site `B`. Then `U` is scheme-theoretically dense in `X` if and only
> if the canonical homomorphism `𝒪_X ⟶ j_* 𝒪_U` of sheaves of commutative rings on the small
> étale site of `X` is injective, that is, a monomorphism.
>
> Both sides are tested on the étale scheme charts of `X`. On the one hand the structure map of
> the morphism of ringed topoi of Stacks 03G8 is a monomorphism exactly when, over every étale
> scheme chart `V` of `X`, pullback of regular functions along the open immersion of schemes
> representing `U ×_X V` is injective; the sections of the direct image over `V` are a limit over
> the étale charts of `U` above `U ×_X V`, which for a representable morphism is attained at the
> single chart `U ×_X V`. On the other hand the scheme-theoretic closure of `U ×_X V` is all of
> `V` exactly when that open immersion of schemes is scheme-theoretically dominant, and -- since
> the charts of `X` include every open subscheme of every chart -- dominance over all charts is
> the same as injectivity on global sections over all charts. Finally density may be tested on
> the charts alone, by
> `AlgebraicGeometry.Space.isSchemeTheoreticallyDense_iff_forall_chart`.

```lean
theorem isSchemeTheoreticallyDense_iff_mono_fSharp (hX : IsAlgebraicSpace B S hS X)
    (U : Subfunctor X) (hU : IsOpenSubspace B S hS U) :
    IsSchemeTheoreticallyDense B S hS U ↔
      Mono (smallEtaleRingedToposHom B S hS
        (ObjectProperty.homMk U.ι :
          (⟨U.toFunctor, hU.1⟩ : AlgebraicSpaces B S hS) ⟶
          (⟨X, hX⟩ : AlgebraicSpaces B S hS))).fSharp
```

## Tag 0837, a lemma

[Tag 0837](https://stacks.math.columbia.edu/tag/0837) in the Stacks Project.

**`AlgebraicGeometry.Space.isSchemeTheoreticallyDense_inf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticDensity/Density.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SchemeTheoreticDensity/Density.lean#L229).

> **Stacks 0837.** If `U` and `V` are scheme-theoretically dense open subspaces of an
> algebraic space `X` over a scheme `S` contained in a big fppf site `B`, then so is `U ∩ V`.
>
> Let `φ : W ⟶ X` be an étale morphism of algebraic spaces over `S`. The scheme-theoretic
> closure of `(U ∩ V) ×_X W` in `W` is a closed subspace containing the inverse image of
> `U ∩ V`, hence is all of `W` by
> `AlgebraicGeometry.Space.eq_top_of_preimage_inf_le`: the density of `U` along the étale
> morphism `V ×_X W ⟶ X` and the density of `V` along `φ` are used in turn.

```lean
theorem isSchemeTheoreticallyDense_inf (hX : IsAlgebraicSpace B S hS X) (U V : Subfunctor X)
    (hU : IsOpenSubspace B S hS U) (hV : IsOpenSubspace B S hS V)
    (hUdense : IsSchemeTheoreticallyDense B S hS U)
    (hVdense : IsSchemeTheoreticallyDense B S hS V) :
    IsOpenSubspace B S hS (U ⊓ V) ∧ IsSchemeTheoreticallyDense B S hS (U ⊓ V)
```

## Tag 088G, a lemma

[Tag 088G](https://stacks.math.columbia.edu/tag/088G) in the Stacks Project.

**`AlgebraicGeometry.Space.isOpenImmersion_and_dense_toSchemeTheoreticImage_of_qc_or_reduced`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/ImmersionDenseOpenInSchemeTheoreticImage.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/ImmersionDenseOpenInSchemeTheoreticImage.lean#L74).

> **Stacks 088G.** Let `S` be a scheme and let `h : Z ⟶ X` be an immersion of algebraic
> spaces over `S`.  Assume either that `h` is quasi-compact or that `Z` is reduced, and let
> `Z̄ ⊆ X` be the scheme-theoretic image of `h`.  Then the morphism `Z ⟶ Z̄` is an open immersion
> which identifies `Z` with a scheme-theoretically dense open subspace of `Z̄`; moreover `Z` is
> topologically dense in `Z̄`.
>
> Spelled out, the five assertions are: the morphism onto the scheme-theoretic image is an open
> immersion; it is an isomorphism onto its range, which is the identification of `Z` with a
> subspace of `Z̄`; that range is an open subspace of `Z̄`; it is scheme-theoretically dense in
> `Z̄`; and the induced map on points has dense range.
>
> Each is proved separately in
> `StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ImmersionSchemeTheoreticallyDenseOpen.lean`,
> the identification being the only one not stated there: it is
> `CategoryTheory.Subfunctor.toRange` of the morphism onto the image, which is an isomorphism
> because that morphism is an open immersion and hence a monomorphism.

```lean
theorem isOpenImmersion_and_dense_toSchemeTheoreticImage_of_qc_or_reduced
    {Z X : (BigFppfOver B S hS)ᵒᵖ ⥤ Type u} (hZ : IsAlgebraicSpace B S hS Z)
    (hX : IsAlgebraicSpace B S hS X) (h : Z ⟶ X) (hh : IsImmersion B S hS h)
    (hq_or_hr : IsQuasiCompact B S hS h ∨
      HasEtaleLocalProperty B S hS Z (fun W : Scheme.{u} => IsReduced W)) :
    IsOpenImmersion B S hS (toSchemeTheoreticImage B S hS h) ∧
      IsIso (Subfunctor.toRange (toSchemeTheoreticImage B S hS h)) ∧
      IsOpenSubspace B S hS (Subfunctor.range (toSchemeTheoreticImage B S hS h)) ∧
      IsSchemeTheoreticallyDense B S hS (Subfunctor.range (toSchemeTheoreticImage B S hS h)) ∧
      DenseRange (pointsMap B S hS Z (toSchemeTheoreticImage B S hS h))
```

## Tag 084N, a lemma

[Tag 084N](https://stacks.math.columbia.edu/tag/084N) in the Stacks Project.

**`AlgebraicGeometry.Space.eq_of_eq_on_of_schemeTheoreticImageSubfunctor_eq_top`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparatedEqualizer.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/SeparatedEqualizer.lean#L161).

> **Stacks 084N.** Let `X` and `Y` be algebraic spaces over an algebraic space `T` with
> structure morphisms `p : X ⟶ T` and `q : Y ⟶ T`, and let `f, g : X ⟶ Y` be morphisms over `T`.
> Let `U ⊆ X` be an open subspace with `f` and `g` agreeing on `U`. If the scheme-theoretic closure
> of `U` in `X`, that is the scheme-theoretic image of `U ⟶ X`, is all of `X` and `q` is separated,
> then `f = g`.
>
> The agreement locus of `f` and `g` is a closed subspace of `X` containing `U`, so minimality of
> the scheme-theoretic image of `U ⟶ X` puts that image inside the agreement locus, which is
> therefore all of `X`. Openness of `U`, and indeed algebraicity of `U`, are not used.

```lean
theorem eq_of_eq_on_of_schemeTheoreticImageSubfunctor_eq_top (hT : IsAlgebraicSpace B S hS T)
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (p : X ⟶ T) (q : Y ⟶ T)
    (f g : X ⟶ Y) (hf : f ≫ q = p) (hg : g ≫ q = p) (U : Subfunctor X)
    (_hU : IsOpenSubspace B S hS U) (hfg : U.ι ≫ f = U.ι ≫ g)
    (hclosure : schemeTheoreticImageSubfunctor B S hS U.ι = ⊤) (hq : IsSeparated B S hS q) :
    f = g
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.17, Tag 0831](https://stacks.math.columbia.edu/tag/0831)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
