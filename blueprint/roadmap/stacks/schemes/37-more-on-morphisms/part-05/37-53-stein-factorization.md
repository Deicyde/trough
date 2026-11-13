---
declaration: section
origin: cited
lean: Stacks.SteinFactorization.toNormalization_fromNormalization, Stacks.SteinFactorization.quasiCompact_toNormalization, Stacks.SteinFactorization.quasiSeparated_toNormalization, Stacks.SteinFactorization.isIntegralHom_fromNormalization, Stacks.SteinFactorization.universallyClosed_toNormalization, Stacks.SteinFactorization.surjective_toNormalization, Stacks.SteinFactorization.isIso_normalizationPullback, Stacks.SteinFactorization.normalizationPullbackIso
statement: formalized
proof: formalized
---

# 37.53 Stein factorization

Section 37.53 of the Stacks Project, [Tag 03GX](https://stacks.math.columbia.edu/tag/03GX). 9 tags here are carried by 35 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03GY, a lemma

[Tag 03GY](https://stacks.math.columbia.edu/tag/03GY) in the Stacks Project.

**`Stacks.SteinFactorization.toNormalization_fromNormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Basic.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Basic.lean#L63). The attribute's comment: “relative\_normalization”.

> **Stacks Project, Tag 03GY.**  A quasi-compact, quasi-separated morphism `f : X ⟶ S`
> factors as `f = f' ≫ π`, where `S'` is the normalization of `S` in `X`, where `f'` is the
> canonical map to `S'` and where `π` is the structure morphism of `S'`.
>
> A proper morphism is quasi-compact and quasi-separated, so this also supplies the factorization
> of [Stacks Project, Tag 03H2].

```lean
public theorem toNormalization_fromNormalization :
    f.toNormalization ≫ f.fromNormalization = f
```

**`Stacks.SteinFactorization.quasiCompact_toNormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Basic.lean, line 69](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Basic.lean#L69). The attribute's comment: “first\_quasi\_compact”.

> **Stacks Project, Tag 03GY.**  The first map of the factorization is quasi-compact.

```lean
public theorem quasiCompact_toNormalization : QuasiCompact f.toNormalization
```

**`Stacks.SteinFactorization.quasiSeparated_toNormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Basic.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Basic.lean#L74). The attribute's comment: “first\_quasi\_separated”.

> **Stacks Project, Tag 03GY.**  The first map of the factorization is quasi-separated.

```lean
public theorem quasiSeparated_toNormalization : QuasiSeparated f.toNormalization
```

**`Stacks.SteinFactorization.isIntegralHom_fromNormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Basic.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Basic.lean#L83). The attribute's comment: “integral\_second\_map”.

> **Stacks Project, Tag 03GY.**  The second map of the factorization, the structure morphism
> of the normalization of `S` in `X`, is integral.
>
> A proper morphism is quasi-compact and quasi-separated, so this also supplies the integrality of
> the second factor in [Stacks Project, Tag 03H2].

```lean
public theorem isIntegralHom_fromNormalization : IsIntegralHom f.fromNormalization
```

**`Stacks.SteinFactorization.universallyClosed_toNormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Basic.lean, line 95](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Basic.lean#L95). The attribute's comment: “first\_universally\_closed”.

> **Stacks Project, Tag 03GY.**  The first map of the factorization of a universally closed,
> quasi-separated morphism is universally closed.

```lean
public theorem universallyClosed_toNormalization : UniversallyClosed f.toNormalization
```

**`Stacks.SteinFactorization.surjective_toNormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Basic.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Basic.lean#L101). The attribute's comment: “first\_surjective”.

> **Stacks Project, Tag 03GY.**  The first map of the factorization of a universally closed,
> quasi-separated morphism is surjective: it is universally closed and dominant.

```lean
public theorem surjective_toNormalization : Surjective f.toNormalization
```

**`Stacks.SteinFactorization.isIso_normalizationPullback`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/FlatBaseChange.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/FlatBaseChange.lean#L228). The attribute's comment: “flat\_base\_change”. References: EGA III (4.3.4), “more general”.

> **Stacks Project, Tag 03GY (flat\_base\_change).**  Formation of the factorization
> `f = π ∘ f'` of a universally closed, quasi-separated morphism commutes with flat base change:
> the comparison morphism from the normalization of the base change `f_T : X ×_S T ⟶ T` to the
> base change `T ×_S S'` of the normalization of `S` in `X` is an isomorphism.
>
> Together with `AlgebraicGeometry.Scheme.Hom.normalizationPullback_snd` and
> `AlgebraicGeometry.Scheme.Hom.toNormalization_normalizationPullback_fst`, which say that the
> comparison morphism matches the two factors, this is the assertion that the whole factorization
> is obtained from that of `f` by base change.

```lean
public instance isIso_normalizationPullback : IsIso (f.normalizationPullback g)
```

**`Stacks.SteinFactorization.normalizationPullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/FlatBaseChange.lean, line 244](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/FlatBaseChange.lean#L244). The attribute's comment: “flat\_base\_change”. References: EGA III (4.3.4), “more general”.

> **Stacks Project, Tag 03GY (flat\_base\_change).**  The identification, over `T`, of the
> intermediate scheme of the factorization of the base change `f_T : X ×_S T ⟶ T` with the base
> change `T ×_S S'` of the intermediate scheme of the factorization of `f`.

```lean
public noncomputable def normalizationPullbackIso :
    Over.mk (pullback.snd f g).fromNormalization ≅
      Over.mk (pullback.snd f.fromNormalization g)
```

**`Stacks.SteinFactorization.toNormalization_normalizationPullbackIso_hom_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/FlatBaseChange.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/FlatBaseChange.lean#L252). The attribute's comment: “flat\_base\_change”.

> **Stacks Project, Tag 03GY (flat\_base\_change).**  Under that identification the first
> factor of the factorization of `f_T` becomes the base change of the first factor of `f`.

```lean
public theorem toNormalization_normalizationPullbackIso_hom_left :
    (pullback.snd f g).toNormalization ≫ (normalizationPullbackIso f g).hom.left ≫
        pullback.fst f.fromNormalization g = pullback.fst f g ≫ f.toNormalization
```

**`Stacks.SteinFactorization.overIsoPushforwardSpectrum`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/RelativeSpectrum.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/RelativeSpectrum.lean#L67). The attribute's comment: “relative\_spectrum”. References: EGA III (7.8.10), “partial”; SGA 1 X (1.2), “Y′ ≅ Spec f\_*O\_X over Y”; SGA 6 XII (2.5), “partial”.

> **Stacks Project, Tag 03GY (relative\_spectrum).**  Clause (4) of the factorization of a
> universally closed, quasi-separated morphism `f : X ⟶ S`: the intermediate scheme `S'` of the
> factorization is, as a scheme over `S`, the relative spectrum `Spec_S(f_* 𝒪_X)` of the
> pushed-forward structure sheaf.  Being an isomorphism over `S` is the statement that the second
> factor `π : S' ⟶ S` becomes the structure morphism of the relative spectrum.

```lean
public noncomputable def overIsoPushforwardSpectrum :
    Over.mk f.fromNormalization ≅ Over.mk (pushforwardSpectrum f).toBase
```

**`Stacks.SteinFactorization.toNormalization_overIsoPushforwardSpectrum_hom_left`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/RelativeSpectrum.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/RelativeSpectrum.lean#L79). The attribute's comment: “relative\_spectrum”. References: EGA III (7.8.10), “partial”; SGA 1 X (1.2), “Under Y′ ≅ Spec f\_*O\_X”; SGA 6 XII (2.5), “partial”.

> **Stacks Project, Tag 03GY (relative\_spectrum).**  Under the identification of the
> intermediate scheme of the factorization with `Spec_S(f_* 𝒪_X)`, the first factor
> `f' : X ⟶ S'` becomes the canonical morphism `X ⟶ Spec_S(f_* 𝒪_X)` of [Stacks, Tag 01LY].

```lean
public theorem toNormalization_overIsoPushforwardSpectrum_hom_left :
    f.toNormalization ≫ (overIsoPushforwardSpectrum f).hom.left = canonicalMorphism f
```

**`Stacks.SteinFactorization.isIso_c_toNormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/StructureSheaf.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/StructureSheaf.lean#L158). The attribute's comment: “pushforward\_structure\_sheaf”.

> **Stacks Project, Tag 03GY.**  Clause (3) of the factorization of a universally closed,
> quasi-separated morphism `f : X ⟶ S`: the canonical map from the structure sheaf of the
> normalization `S'` of `S` in `X` to the pushforward of the structure sheaf of `X` along the
> first map `f' : X ⟶ S'` is an isomorphism, that is, `f'_*𝒪_X = 𝒪_{S'}`.

```lean
public theorem isIso_c_toNormalization : IsIso f.toNormalization.c
```

## Tag 0E0M, a lemma

[Tag 0E0M](https://stacks.math.columbia.edu/tag/0E0M) in the Stacks Project.

**`Stacks.SteinFactorization.finite_preimage_singleton_fromNormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/FiniteFibres.lean, line 183](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/FiniteFibres.lean#L183). The attribute's comment: “finite\_fibre”.

> For a universally closed, quasi-separated morphism `f` that is locally of finite type, the
> fibres of the second map `π` of the factorization `X ⟶ f.normalization ⟶ S` are finite.

```lean
public theorem finite_preimage_singleton_fromNormalization (s : S) :
    (f.fromNormalization ⁻¹' {s}).Finite
```

**`Stacks.SteinFactorization.finite_residueFieldMap_fromNormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/FiniteFibres.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/FiniteFibres.lean#L240). The attribute's comment: “finite\_residue\_extensions”.

> For a universally closed, quasi-separated morphism `f` that is locally of finite type, the
> residue field of `f.normalization` at a point is a finite extension of the residue field of `S` at
> its image under the second map `π` of the factorization: the ring map `κ(π s') ⟶ κ(s')` makes
> `κ(s')` a finite `κ(π s')`-module.

```lean
public theorem finite_residueFieldMap_fromNormalization (s' : f.normalization) :
    (f.fromNormalization.residueFieldMap s').hom.Finite
```

## Tag 03GZ, a lemma

[Tag 03GZ](https://stacks.math.columbia.edu/tag/03GZ) in the Stacks Project.

**`AlgebraicGeometry.geometricallyConnected_fiber_iff_forall_etaleNeighborhood`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/GeometricallyConnectedFibre.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/EtaleNeighbourhood/GeometricallyConnectedFibre.lean#L85).

> **Stacks Project, Tag 03GZ.** The fibre of a morphism at a point is geometrically connected
> if and only if the fibre at the distinguished point after pullback to every étale neighborhood
> is connected.

```lean
theorem geometricallyConnected_fiber_iff_forall_etaleNeighborhood
    {X S : Scheme.{u}} (f : X ⟶ S) (s : S) :
    GeometricallyConnected (f.fiberToSpecResidueField s) ↔
      ∀ U : EtaleNeighborhood S s,
        ConnectedSpace ((pullback.snd f U.toBase).fiber U.point)
```

## Tag 03H0, a theorem

[Tag 03H0](https://stacks.math.columbia.edu/tag/03H0) in the Stacks Project.

**`Stacks.SteinFactorization.isFinite_fromNormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Noetherian.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Noetherian.lean#L216). The attribute's comment: “clause (2): the second factor of the Stein factorization of a proper morphism over a locally Noetherian base is finite. Proved from [Stacks, Tag 02O5] (`AlgebraicGeometry.ProperCoherenceWitness.isCoherent_pushforward`), with no carried hypothesis”. References: EGA III (7.8.10), “partial”; SGA 1 X (1.2), “Y′ is finite over Y”.

> **Stacks Project, Tag 03H0, clause (2).**  For a proper morphism `f : X ⟶ S` onto a locally
> Noetherian scheme, the second factor `π : S' ⟶ S` of the Stein factorization — the structure
> morphism of the normalization of `S` in `X` — is **finite**.  **No hypothesis.**
>
> This is the one clause of Tag 03H0 that is not already a clause of the general Tag 03H2, where
> `π` is only asserted to be integral, and it is where local Noetherianness of `S` is used.  The
> proof is the source's: `f_* 𝒪_X` is coherent by [Stacks, Tag 02O5], so `Γ(S, U) ⟶ Γ(X, f ⁻¹ᵁ U)`
> is finite for `U ⊆ S` affine open (`Stacks.SteinFactorization.finite_app_of_isProper`); that map
> is `Γ(S, U) ⟶ Γ(S', π ⁻¹ᵁ U) ⟶ Γ(X, f ⁻¹ᵁ U)` and the second map is an isomorphism by
> [Stacks, Tag 03GY] (`Stacks.SteinFactorization.isIso_app_toNormalization`), so the first is
> finite;  and `π` is affine, being integral.

```lean
public theorem isFinite_fromNormalization : IsFinite f.fromNormalization
```

**`Stacks.SteinFactorization.geometricallyConnected_toNormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Noetherian.lean, line 352](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Noetherian.lean#L352). The attribute's comment: “clause (1), the geometric connectedness conjunct: the first factor of the Stein factorization of a proper morphism onto a locally Noetherian base has geometrically connected fibres. The properness conjunct of the same clause is isProper\_toNormalization\_of\_isLocallyNoetherian”. References: EGA III (4.3.4), “special case”.

> **Stacks Project, Tag 03H0, clause (1), the geometric connectedness conjunct.**  For `f`
> proper onto a locally Noetherian scheme `S`, the first factor `f' : X ⟶ S'` of the Stein
> factorization — `S'` the normalization of `S` in `X` and `f' = f.toNormalization` — has
> geometrically connected fibres.
>
> Unconditional, at the hypotheses of the tag.  It is the reading of
> `Stacks.SteinFactorization.geometricallyConnected_toNormalization_of_isProper`, clause (1) of the
> general [Stacks, Tag 03H2], at the stronger hypotheses of this tag;  the local Noetherianness of
> `S` is not used.
>
> The properness conjunct of the same clause is
> `Stacks.SteinFactorization.isProper_toNormalization_of_isLocallyNoetherian` below.

```lean
public theorem geometricallyConnected_toNormalization (f : X ⟶ S) [IsLocallyNoetherian S]
    [IsProper f] : GeometricallyConnected f.toNormalization
```

**`Stacks.SteinFactorization.toNormalization_fromNormalization_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Noetherian.lean, line 376](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Noetherian.lean#L376). The attribute's comment: “the factorization itself together with clause (5): f factors as X --f'--> S' --π--> S with S' the normalization of S in X (Stacks 035H), f' = f.toNormalization and π = f.fromNormalization. No carried hypothesis”.

> **Stacks Project, Tag 03H0: the factorization, together with clause (5).**  A proper morphism
> `f : X ⟶ S` onto a locally Noetherian scheme factors as `X --f'--> S' --π--> S` *through the
> normalization of `S` in `X`* ([Stacks, Tag 035H],
> `AlgebraicGeometry.Scheme.Hom.normalization`), with `f' = f.toNormalization` and
> `π = f.fromNormalization`.  That the intermediate scheme of the factorization is the
> normalization of `S` in `X` is clause (5), and since the intermediate scheme produced here *is*
> `f.normalization` the whole content of that clause is the displayed equation.
>
> Local Noetherianness is not needed: this is the general factorization of [Stacks, Tag 03H2],
> which holds for any proper morphism, specialized to the hypotheses of Tag 03H0.

```lean
public theorem toNormalization_fromNormalization_of_isLocallyNoetherian :
    f.toNormalization ≫ f.fromNormalization = f
```

**`Stacks.SteinFactorization.isProper_toNormalization_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Noetherian.lean, line 388](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Noetherian.lean#L388). The attribute's comment: “clause (1), the properness half: the first factor of the Stein factorization is proper. No carried hypothesis”.

> **Stacks Project, Tag 03H0, clause (1), properness half.**  The first factor
> `f' : X ⟶ S'` of the Stein factorization of a proper morphism onto a locally Noetherian scheme is
> proper.  Local Noetherianness is not needed: `f'` is universally closed because `f` is, and
> separated and locally of finite type by cancellation along `π`, which is the general
> [Stacks, Tag 03H2] specialized to the hypotheses of Tag 03H0.

```lean
public theorem isProper_toNormalization_of_isLocallyNoetherian : IsProper f.toNormalization
```

**`Stacks.SteinFactorization.isIso_c_toNormalization_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Noetherian.lean, line 399](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Noetherian.lean#L399). The attribute's comment: “clause (3): f'\_* 𝒪\_X = 𝒪\_\{S'}, i.e. the canonical map 𝒪\_\{S'} ⟶ f'\_* 𝒪\_X is an isomorphism. No carried hypothesis”.

> **Stacks Project, Tag 03H0, clause (3).**  `f'_* 𝒪_X = 𝒪_{S'}` for the first factor of the
> Stein factorization of a proper morphism onto a locally Noetherian scheme:  the canonical map
> `𝒪_{S'} ⟶ f'_* 𝒪_X` is an isomorphism.  Local Noetherianness is not needed; this is
> [Stacks, Tag 03H2] clause (3), which holds for any proper morphism, specialized to the hypotheses
> of Tag 03H0.

```lean
public theorem isIso_c_toNormalization_of_isLocallyNoetherian : IsIso f.toNormalization.c
```

**`Stacks.SteinFactorization.overIsoPushforwardSpectrum_of_isLocallyNoetherian`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Noetherian.lean, line 411](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Noetherian.lean#L411). The attribute's comment: “clause (4): S' = Spec\_S(f\_* 𝒪\_X), as an isomorphism in Over S, so that π is carried to the structure morphism of the relative spectrum. No carried hypothesis”. References: EGA III (7.8.10), “partial”; SGA 1 X (1.2), “Y′ ≅ Spec f\_*O\_X over Y”; SGA 6 XII (2.5), “partial”.

> **Stacks Project, Tag 03H0, clause (4).**  The intermediate scheme `S'` of the Stein
> factorization of a proper morphism onto a locally Noetherian scheme is the relative spectrum
> `Spec_S(f_* 𝒪_X)`, as a scheme over `S`.  Being an isomorphism in `CategoryTheory.Over S` is what
> makes this an identification of *factorizations*:  it says that `π` is carried to the structure
> morphism of the relative spectrum.  Local Noetherianness is not needed; this is
> [Stacks, Tag 03H2] clause (4) specialized to the hypotheses of Tag 03H0.

```lean
public noncomputable def overIsoPushforwardSpectrum_of_isLocallyNoetherian :
    Over.mk f.fromNormalization ≅ Over.mk (pushforwardSpectrum f).toBase
```

**`Stacks.SteinFactorization.toNormalization_overIsoPushforwardSpectrum_hom_left_of_isLocallyNoetherian`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Noetherian.lean, line 423](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Noetherian.lean#L423). The attribute's comment: “clause (4), continued: the identification of clause (4) carries f' to the canonical morphism X ⟶ Spec\_S(f\_* 𝒪\_X) of Stacks 01LY. No carried hypothesis”. References: SGA 1 X (1.2), “Under Y′ ≅ Spec f\_*O\_X”.

> **Stacks Project, Tag 03H0, clause (4), continued.**  The identification of clause (4) carries
> the first factor `f'` to the canonical morphism `X ⟶ Spec_S(f_* 𝒪_X)` of [Stacks, Tag 01LY];  this
> is what makes clause (4) an identification of the factorization `f = f' ≫ π` with the
> factorization of `f` through its relative spectrum.

```lean
public theorem toNormalization_overIsoPushforwardSpectrum_hom_left_of_isLocallyNoetherian :
    f.toNormalization ≫ (overIsoPushforwardSpectrum_of_isLocallyNoetherian f).hom.left =
      canonicalMorphism f
```

**`Stacks.SteinFactorization.exists_isSteinFactorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Noetherian.lean, line 485](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Noetherian.lean#L485). References: EGA II (8.11.8), “(ii), special case”; EGA III (4.3.1); EGA III (7.8.10), “more general”; SGA 1 IX (6.6), “partial”; SGA 1 X (1.2).

> **Stacks Project, Tag 03H0 (Stein factorization, Noetherian case).**  Let `S` be a locally
> Noetherian scheme and let `f : X ⟶ S` be proper.  Then `f` factors as `X --f'--> S' --π--> S`
> with all five properties of the tag:  `f'` proper with geometrically connected fibres, `π`
> finite, `f'_* 𝒪_X = 𝒪_{S'}`, `S' = Spec_S(f_* 𝒪_X)`, and `S'` the normalization of `S` in `X`.
>
> The witnesses are the ones the source names:  `S'` is the normalization of `S` in `X`, `f'` is
> `f.toNormalization` and `π` is `f.fromNormalization`.
>
> Unconditional.  Each of the five clauses is a theorem of its own above;  the last of them to be
> proved was the connectedness conjunct of clause (1),
> `Stacks.SteinFactorization.geometricallyConnected_toNormalization`, which rests on
> [Stacks, Tag 0G7X] at a locally Noetherian base and through it on the theorem on formal
> functions.

```lean
public theorem exists_isSteinFactorization
    (f : X ⟶ S) [IsLocallyNoetherian S] [IsProper f] :
    ∃ (S' : Scheme.{u}) (f' : X ⟶ S') (π : S' ⟶ S), Nonempty (IsSteinFactorization f f' π)
```

## Tag 03H2, a theorem

[Tag 03H2](https://stacks.math.columbia.edu/tag/03H2) in the Stacks Project.

**`Stacks.SteinFactorization.toNormalization_fromNormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Basic.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Basic.lean#L63). The attribute's comment: “normalization”.

> **Stacks Project, Tag 03GY.**  A quasi-compact, quasi-separated morphism `f : X ⟶ S`
> factors as `f = f' ≫ π`, where `S'` is the normalization of `S` in `X`, where `f'` is the
> canonical map to `S'` and where `π` is the structure morphism of `S'`.
>
> A proper morphism is quasi-compact and quasi-separated, so this also supplies the factorization
> of [Stacks Project, Tag 03H2].

```lean
public theorem toNormalization_fromNormalization :
    f.toNormalization ≫ f.fromNormalization = f
```

**`Stacks.SteinFactorization.isIntegralHom_fromNormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Basic.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Basic.lean#L83). The attribute's comment: “integral\_second\_map”.

> **Stacks Project, Tag 03GY.**  The second map of the factorization, the structure morphism
> of the normalization of `S` in `X`, is integral.
>
> A proper morphism is quasi-compact and quasi-separated, so this also supplies the integrality of
> the second factor in [Stacks Project, Tag 03H2].

```lean
public theorem isIntegralHom_fromNormalization : IsIntegralHom f.fromNormalization
```

**`Stacks.SteinFactorization.geometricallyConnected_toNormalization_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/ConnectedFibres.lean, line 474](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/ConnectedFibres.lean#L474). The attribute's comment: “clause (1), the geometric connectedness conjunct: the first factor of the Stein factorization of a proper morphism has geometrically connected fibres, over an arbitrary base. The properness conjunct of the same clause is isProper\_toNormalization”. References: EGA III (4.3.4), “partial”.

> **Stacks Project, Tag 03H2, clause (1), the geometric connectedness conjunct.**  For `f`
> proper onto an arbitrary scheme `S`, the first factor `f' : X ⟶ S'` of the Stein factorization —
> `S'` the normalization of `S` in `X` and `f' = f.toNormalization` — has geometrically connected
> fibres.
>
> Unconditional, at the hypotheses of the tag:  nothing is assumed of `S`.  The two inputs are the
> reduction above, which is the source's — [Stacks, Tag 03GZ] together with degree-zero flat base
> change and `f'_* 𝒪_X = 𝒪_{S'}` — and [Stacks, Tag 0G7X] for the base changes of `f'` to étale
> neighbourhoods of `S'`, which is
> `Stacks.AlgebraicGeometry.Fibres.extendsOverNeighbourhood_of_isProper`.
>
> The same statement covers the connectedness conjunct of clause (1) of [Stacks, Tag 03H0], whose
> hypotheses are strictly stronger;
> `Stacks.SteinFactorization.geometricallyConnected_toNormalization` in
> `StacksFrontier.AlgebraicGeometry.MoreMorphisms.SteinFactorization.Noetherian` is that reading
> of it.
> The properness conjunct of clause (1) is `Stacks.SteinFactorization.isProper_toNormalization`.

```lean
public theorem geometricallyConnected_toNormalization_of_isProper :
    GeometricallyConnected f.toNormalization
```

**`Stacks.SteinFactorization.isProper_toNormalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Proper.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/Proper.lean#L51). The attribute's comment: “proper\_first\_map”.

> **Stacks Project, Tag 03H2.**  The first map of the factorization of a proper morphism is
> proper.  It is universally closed because `f` is, separated and locally of finite type by
> cancellation along the second map.

```lean
public theorem isProper_toNormalization : IsProper f.toNormalization
```

**`Stacks.SteinFactorization.overIsoPushforwardSpectrum_of_isProper`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/RelativeSpectrum.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/RelativeSpectrum.lean#L96). The attribute's comment: “relative\_spectrum”. References: EGA III (7.8.10), “partial”; SGA 1 X (1.2), “Y′ ≅ Spec f\_*O\_X over Y”; SGA 6 XII (2.5), “partial”.

> **Stacks Project, Tag 03H2 (relative\_spectrum).**  Clause (4) of the factorization of a
> proper morphism `f : X ⟶ S`: the intermediate scheme `S'` of the factorization is, as a scheme
> over `S`, the relative spectrum `Spec_S(f_* 𝒪_X)` of the pushed-forward structure sheaf.

```lean
public noncomputable def overIsoPushforwardSpectrum_of_isProper :
    Over.mk f.fromNormalization ≅ Over.mk (pushforwardSpectrum f).toBase
```

**`Stacks.SteinFactorization.toNormalization_overIsoPushforwardSpectrum_hom_left_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/RelativeSpectrum.lean, line 108](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/RelativeSpectrum.lean#L108). The attribute's comment: “relative\_spectrum”. References: EGA III (7.8.10), “partial”; SGA 1 X (1.2), “Under Y′ ≅ Spec f\_*O\_X”; SGA 6 XII (2.5), “partial”.

> **Stacks Project, Tag 03H2 (relative\_spectrum).**  Under the identification of the
> intermediate scheme of the factorization of a proper morphism with `Spec_S(f_* 𝒪_X)`, the first
> factor `f' : X ⟶ S'` becomes the canonical morphism `X ⟶ Spec_S(f_* 𝒪_X)` of
> [Stacks, Tag 01LY].

```lean
public theorem toNormalization_overIsoPushforwardSpectrum_hom_left_of_isProper :
    f.toNormalization ≫ (overIsoPushforwardSpectrum_of_isProper f).hom.left =
      canonicalMorphism f
```

**`Stacks.SteinFactorization.isIso_c_toNormalization_of_isProper`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/StructureSheaf.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/StructureSheaf.lean#L173). The attribute's comment: “structure\_sheaf\_pushforward”.

> **Stacks Project, Tag 03H2.**  Clause (3) of the factorization of a proper morphism
> `f : X ⟶ S`: the pushforward of the structure sheaf of `X` along the first map
> `f' : X ⟶ f.normalization` is the structure sheaf of `f.normalization`.

```lean
public theorem isIso_c_toNormalization_of_isProper {X S : Scheme.{u}} (f : X ⟶ S) [IsProper f] :
    IsIso f.toNormalization.c
```

## Tag 0AY8, a lemma

[Tag 0AY8](https://stacks.math.columbia.edu/tag/0AY8) in the Stacks Project.

**`Stacks.SteinFactorization.isIso_c_of_isNormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/NormalBase.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/NormalBase.lean#L297). The attribute's comment: “pushforward of the structure sheaf”.

> **Stacks Project, Tag 0AY8, first conclusion.**  Let `f : X ⟶ S` be a proper morphism from a
> reduced scheme onto a normal integral scheme with generic point `ξ`.  If every generic point of
> an irreducible component of `X` maps to `ξ` and `H⁰(X_ξ, 𝒪) = κ(ξ)`, then `f_*𝒪_X = 𝒪_S`.
>
> The second factor of the Stein factorization is an isomorphism, and the first already satisfies
> `f'_*𝒪_X = 𝒪_{S'}` by clause (3) of [Stacks, Tag 03H2].

```lean
public theorem isIso_c_of_isNormal (f : X ⟶ S) [IsProper f] [IsIntegral S]
    [AlgebraicGeometry.IsNormal S] [IsReduced X]
    (hgen : ∀ x : X, x ∈ genericPoints X → f x = genericPoint S)
    (hΓ : IsIso ((Scheme.ΓSpecIso (S.residueField (genericPoint S))).inv ≫
      (f.fiberToSpecResidueField (genericPoint S)).appTop)) :
    IsIso f.c
```

**`Stacks.SteinFactorization.geometricallyConnected_of_isNormal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/NormalBase.lean, line 373](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/SteinFactorization/NormalBase.lean#L373). The attribute's comment: “the second conclusion, that f has geometrically connected fibres. The first conclusion, f\_*𝒪\_X = 𝒪\_S, is isIso\_c\_of\_isNormal”. References: EGA III (4.3.8), “special case”.

> **Stacks Project, Tag 0AY8, the second conclusion.**  Under the hypotheses of Tag 0AY8 — `f`
> proper, `S` integral and normal, `X` reduced, every generic point of `X` over the generic point
> `ξ` of `S`, and `H⁰(X_ξ, 𝒪) = κ(ξ)` — the morphism `f` has geometrically connected fibres.
>
> The proof follows the source: the second factor `π : S' ⟶ S` of the Stein factorization is an
> isomorphism
> (`Stacks.SteinFactorization.isIso_fromNormalization_of_isNormal`), so the fibres of `f` are those
> of the first factor, and their geometric connectedness is clause (1) of [Stacks, Tag 03H2],
> `Stacks.SteinFactorization.geometricallyConnected_toNormalization_of_isProper`.
>
> The first conclusion, `f_*𝒪_X = 𝒪_S`, is `Stacks.SteinFactorization.isIso_c_of_isNormal`.

```lean
public theorem geometricallyConnected_of_isNormal
    (f : X ⟶ S) [IsProper f] [IsIntegral S] [AlgebraicGeometry.IsNormal S] [IsReduced X]
    (hgen : ∀ x : X, x ∈ genericPoints X → f x = genericPoint S)
    (hΓ : IsIso ((Scheme.ΓSpecIso (S.residueField (genericPoint S))).inv ≫
      (f.fiberToSpecResidueField (genericPoint S)).appTop)) :
    GeometricallyConnected f
```

## Tag 0BUI, a lemma

[Tag 0BUI](https://stacks.math.columbia.edu/tag/0BUI) in the Stacks Project.

**`AlgebraicGeometry.lowerSemicontinuous_numGeometricConnectedComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FibreConnectedComponents/LowerSemicontinuity.lean, line 492](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FibreConnectedComponents/LowerSemicontinuity.lean#L492). References: EGA IV (15.5.4), “Flat case”; EGA IV (15.5.9).

> **[Stacks, Tag 0BUI].**  For a flat proper morphism of finite presentation, the number of
> geometric connected components of the fibres is a lower semicontinuous function on the base.
>
> The count is the `ℕ∞`-valued function of Tag 055F.  The proof is the source's:  the Stein
> factorization `f = f.fromNormalization ∘ f.toNormalization` has a first factor with
> geometrically connected fibres (Tag 03H2), so it does not change the count, and a second factor
> that is integral and, as `f` is flat of finite presentation and `f.toNormalization` is
> surjective, universally open.

```lean
theorem lowerSemicontinuous_numGeometricConnectedComponents {X S : Scheme.{u}} (f : X ⟶ S)
    [IsProper f] [Flat f] [LocallyOfFinitePresentation f] :
    LowerSemicontinuous (numGeometricConnectedComponents f)
```

## Tag 0E0N, a lemma

[Tag 0E0N](https://stacks.math.columbia.edu/tag/0E0N) in the Stacks Project.

**`AlgebraicGeometry.isLocallyConstant_numGeometricConnectedComponents`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/FibreConnectedComponents/LocalConstancy.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/FibreConnectedComponents/LocalConstancy.lean#L158). References: EGA IV (15.5.7), “Flat”; EGA IV (15.5.9), “(ii), special case”.

> **The number of geometric connected components of the fibres is locally constant**, for
> `f : X ⟶ S` proper, flat, of finite presentation, with geometrically reduced fibres.
>
> It is lower semicontinuous by [Stacks, Tag 0BUI], and it is the degree-zero derived-fibre Betti
> function of the perfect object `Rf_*𝒪_X` (`numGeometricConnectedComponents_eq_derivedFiberBetti`),
> which is upper semicontinuous by part (2) of [Stacks, Tag 0BDI]
> (`DerivedFibreBetti.upperSemicontinuous_derivedFiberBetti`). The hypothesis `hred` that the
> geometric fibres are reduced asks this of the base change of `f` to the spectrum of every
> algebraically closed field; it gives Mathlib's `GeometricallyReduced f`, reducedness after base
> change to every field, by `geometricallyReduced_iff_forall_isAlgClosed`.

```lean
theorem isLocallyConstant_numGeometricConnectedComponents
    {X S : Scheme.{u}} (f : X ⟶ S) [IsProper f] [Flat f] [LocallyOfFinitePresentation f]
    (hred : ∀ (k : Type u) [Field k] [IsAlgClosed k] (s : Spec (.of k) ⟶ S),
      IsReduced (pullback f s)) :
    IsLocallyConstant (numGeometricConnectedComponents f)
```

## Tag 0CT9, a lemma

[Tag 0CT9](https://stacks.math.columbia.edu/tag/0CT9) in the Stacks Project.

**`AlgebraicGeometry.exists_isClopen_isProper_of_henselianPair`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/MoreMorphisms/ProperPartOverHenselianPair/Chow.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/MoreMorphisms/ProperPartOverHenselianPair/Chow.lean#L270). The attribute's comment: “the whole statement”.

> Let `(A, I)` be a henselian pair and let `f : X ⟶ Spec A` be separated and of finite type.  An
> open and closed subscheme `i : Y ⟶ X ×_{Spec A} Spec (A ⧸ I)` of the closed fibre which is proper
> over `Spec (A ⧸ I)` is the closed fibre of an open and closed subscheme `w : W ⟶ X` which is
> proper over `Spec A`: there is an isomorphism `Y ≅ W ×_{Spec A} Spec (A ⧸ I)` over the closed
> fibre.

```lean
theorem exists_isClopen_isProper_of_henselianPair (A : Type u) [CommRing A]
    (I : Ideal A) (hI : HenselianPair A I) {X : Scheme.{u}} (f : X ⟶ Spec (.of A))
    [LocallyOfFiniteType f] [QuasiCompact f] [IsSeparated f] {Y : Scheme.{u}}
    (i : Y ⟶ pullback f (Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I))))
    [IsOpenImmersion i] [IsClosedImmersion i]
    [IsProper (i ≫ pullback.snd f (Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I))))] :
    ∃ (W : Scheme.{u}) (w : W ⟶ X) (_ : IsOpenImmersion w) (_ : IsClosedImmersion w)
      (_ : IsProper (w ≫ f)),
      let q := Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I))
      let w₀ : pullback (w ≫ f) q ⟶ pullback f q :=
        pullback.lift (pullback.fst (w ≫ f) q ≫ w) (pullback.snd (w ≫ f) q)
          (by rw [Category.assoc]; exact pullback.condition)
      ∃ e : Y ≅ pullback (w ≫ f) q, e.hom ≫ w₀ = i
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 37.53, Tag 03GX](https://stacks.math.columbia.edu/tag/03GX)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
