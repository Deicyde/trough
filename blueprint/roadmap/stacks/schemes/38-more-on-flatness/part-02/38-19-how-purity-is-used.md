---
declaration: section
origin: cited
lean: AlgebraicGeometry.forall_injective_stalkLinearMap_associatedPoints_iff_mono, AlgebraicGeometry.isLocallyProjective_pushforward_iff_isPureRelative, AlgebraicGeometry.projective_iff_isPureRelative_tilde, AlgebraicGeometry.isPureRelative_of_isLocallyProjective_pushforward, AlgebraicGeometry.isPureRelative_tilde_of_projective, AlgebraicGeometry.exists_affineOpen_projective_sections_of_chart, AlgebraicGeometry.exists_elementaryEtaleNeighborhood_free_sections, AlgebraicGeometry.exists_elementaryEtaleNeighborhood_free_sections_of_finitePresentation
statement: formalized
proof: formalized
---

# 38.19 How purity is used

Section 38.19 of the Stacks Project, [Tag 05L7](https://stacks.math.columbia.edu/tag/05L7). 7 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05L8, a lemma

[Tag 05L8](https://stacks.math.columbia.edu/tag/05L8) in the Stacks Project.

**`AlgebraicGeometry.forall_injective_stalkLinearMap_associatedPoints_iff_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/InjectivityOnClosedFibre.lean, line 155](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/InjectivityOnClosedFibre.lean#L155). The attribute's comment: “the equivalence, both directions; `S` local with closed point `s` is rendered by the hypothesis that every point of `S` specializes to `s`, which is what a local base supplies”.

> **Stacks Project, Tag 05L8.** Let `f : X ⟶ S` be a morphism of finite type, let `ℱ` be a
> quasi-coherent `𝒪_X`-module of finite type, and let `s` be a point of `S` to which every point
> of `S` specializes — for instance the closed point of a local base. Assume `ℱ` is pure along the
> fibre `X_s` and flat over `S`. Then a map `φ : ℱ ⟶ 𝒢` of quasi-coherent `𝒪_X`-modules is
> injective if and only if the stalk map `φ_x` is injective at every point `x` of `X_s` associated
> to the restriction `ℱ_s`.
>
> One direction is immediate: the stalk maps of a monomorphism are injective at every point. For
> the other, the kernel of `φ` has no weakly associated point — such a point would lie in
> `Ass_{X/S}(ℱ)` by flatness, would specialize into `X_s` by purity, and the hypothesis at the
> associated point of `ℱ_s` it specializes to by Tag 05L3 would put that point outside the support
> of the kernel, which is stable under specialization.

```lean
theorem forall_injective_stalkLinearMap_associatedPoints_iff_mono
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f] [QuasiCompact f]
    (F G : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType] [G.IsQuasicoherent]
    (s : S) (hclosed : ∀ t : S, t ⤳ s)
    (hpure : IsPureAlong ({ S := S, X := X, f := f, F := F, s := s } : PrePureSituation.{u}))
    (hflat : IsFlatOver f.toLRSHom.toShHom F) (φ : F ⟶ G) :
    (∀ x : f.fiber s,
        x ∈ Stacks.Divisors.associatedPoints ((Scheme.Modules.pullback (f.fiberι s)).obj F) →
          Function.Injective (stalkLinearMap F G φ (f.fiberι s x))) ↔ Mono φ
```

## Tag 05MD, a proposition

[Tag 05MD](https://stacks.math.columbia.edu/tag/05MD) in the Stacks Project.

**`AlgebraicGeometry.isLocallyProjective_pushforward_iff_isPureRelative`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/ProjectivePushforwardConverse.lean, line 156](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/ProjectivePushforwardConverse.lean#L156). The attribute's comment: “the scheme criterion, as a biconditional”. References: SGA 3 VIB (6.9), “more general”.

> **Stacks Project, Tag 05MD**, the scheme form. For an affine morphism of finite presentation
> and a quasi-coherent module of finite presentation which is flat over the base, the direct image
> is locally projective exactly when the module is pure relative to the base.
>
> The implication from local projectivity to purity is
> `AlgebraicGeometry.isPureRelative_of_isLocallyProjective_pushforward`, which needs neither
> flatness nor finite presentation; the converse is
> `AlgebraicGeometry.isLocallyProjective_pushforward_of_isPureRelative`.

```lean
theorem isLocallyProjective_pushforward_iff_isPureRelative {X S : Scheme.{u}} (f : X ⟶ S)
    [IsAffineHom f] [LocallyOfFinitePresentation f] [QuasiCompact f] [QuasiSeparated f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFinitePresentation]
    (hflat : IsFlatOver f.toLRSHom.toShHom F) :
    letI : F.IsFiniteType := SheafOfModules.instIsFiniteTypeOfIsFinitePresentation F
    Scheme.Modules.IsLocallyProjective ((Scheme.Modules.pushforward f).obj F) ↔
      IsPureRelative f F
```

**`AlgebraicGeometry.projective_iff_isPureRelative_tilde`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/ProjectivePushforwardConverse.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/ProjectivePushforwardConverse.lean#L177). The attribute's comment: “the affine ring specialization, as a biconditional”.

> **Stacks Project, Tag 05MD**, the ring form. Let `A → B` be of finite presentation and let `N`
> be a finitely presented `B`-module which is flat over `A`. Then `N` is projective over `A` exactly
> when the sheaf `Ñ` on `Spec B` is pure relative to `Spec A`.
>
> Both directions come from the scheme form applied to `Spec B ⟶ Spec A`: the direct image of `Ñ`
> is the sheaf associated to `N` viewed as an `A`-module (Tag 01I9,
> `AlgebraicGeometry.pushforwardTildeIso`), so local projectivity of the direct image is
> projectivity of that `A`-module by Tag 05JQ
> (`AlgebraicGeometry.isLocallyProjective_tilde_iff_projective`).

```lean
theorem projective_iff_isPureRelative_tilde (A B N : Type u) [CommRing A] [CommRing B]
    [Algebra A B] [AddCommGroup N] [Module A N] [Module B N] [IsScalarTower A B N]
    [Algebra.FinitePresentation A B] [Module.FinitePresentation B N] [Module.Flat A N] :
    Module.Projective A N ↔
      IsPureRelative (Spec.map (CommRingCat.ofHom (algebraMap A B)))
        (tilde (ModuleCat.of (CommRingCat.of B) N))
```

**`AlgebraicGeometry.isPureRelative_of_isLocallyProjective_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/ProjectivePushforwardCriterion.lean, line 63](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/ProjectivePushforwardCriterion.lean#L63). The attribute's comment: “the implication from local projectivity of the direct image to relative purity, in the scheme form”. References: SGA 3 VIB (6.9), “6.9 a)”.

> **Stacks Project, Tag 05MD**, the implication from (1) to (2). For an affine morphism of
> finite type, a finite type quasi-coherent module whose direct image is locally projective on the
> base is pure relative to the base.
>
> This implication of Tag 05MD assumes neither flatness over the base nor finite presentation,
> which the statement of that tag assumes for the converse: it is Tag 05K6, whose conclusion is
> universal purity relative to the base, followed by the fact that universal purity along a fibre
> is purity along it with the étale and elementary hypotheses on the base change dropped.

```lean
theorem isPureRelative_of_isLocallyProjective_pushforward
    {X S : Scheme.{u}} (f : X ⟶ S) [IsAffineHom f] [LocallyOfFiniteType f] [QuasiCompact f]
    (F : X.Modules) [F.IsFiniteType] [F.IsQuasicoherent]
    (hF : Scheme.Modules.IsLocallyProjective ((Scheme.Modules.pushforward f).obj F)) :
    IsPureRelative f F
```

**`AlgebraicGeometry.isPureRelative_tilde_of_projective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/ProjectivePushforwardCriterion.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/ProjectivePushforwardCriterion.lean#L90). The attribute's comment: “the implication from projectivity to relative purity, in the ring form of the final assertion”.

> **Stacks Project, Tag 05MD**, the ring specialization of the implication from (1) to (2).
> Let `A → B` be a ring map of finite presentation and let `N` be a finitely presented
> `B`-module. If `N` is projective as an `A`-module, then the sheaf `Ñ` on `Spec B` is pure
> relative to `Spec A`.
>
> As in the scheme form, flatness of `N` over `A` — which the statement of Tag 05MD assumes for
> the converse — is not needed for this implication. The direct image of `Ñ` along
> `Spec B ⟶ Spec A` is the sheaf associated to `N` viewed as an `A`-module, by Tag 01I9, so local
> projectivity of the direct image is projectivity of that `A`-module by Tag 05JQ.

```lean
theorem isPureRelative_tilde_of_projective
    (A B N : Type u) [CommRing A] [CommRing B] [Algebra A B]
    [AddCommGroup N] [Module A N] [Module B N] [IsScalarTower A B N]
    [Algebra.FinitePresentation A B] [Module.FinitePresentation B N]
    (hproj : Module.Projective A N) :
    IsPureRelative (Spec.map (CommRingCat.ofHom (algebraMap A B)))
      (tilde (ModuleCat.of (CommRingCat.of B) N))
```

## Tag 05ME, a lemma

[Tag 05ME](https://stacks.math.columbia.edu/tag/05ME) in the Stacks Project.

**`AlgebraicGeometry.exists_affineOpen_projective_sections_of_chart`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Flatness/PureModules/ProjectiveSectionsAffineOpen05ME.lean, line 864](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Flatness/PureModules/ProjectiveSectionsAffineOpen05ME.lean#L864).

> **Stacks Project, Tag 05ME.** Let `f : X ⟶ S` be locally of finite presentation, let `F` be a
> quasi-coherent `𝒪_X`-module of finite presentation, and let `x ∈ X` lie over `s ∈ S` with `F` flat
> over `S` at `x`. Then there are an affine elementary étale neighbourhood `(S', s') ⟶ (S, s)` and
> an affine open `U' ⊆ X ×_S S'` containing `x' = (x, s')` such that `Γ(U', F|_{U'})` is a
> projective `Γ(S', 𝒪_{S'})`-module.
>
> The chart whose name this declaration carries is the one of Tag 05KW, built inside
> `AlgebraicGeometry.exists_openImmersion_projective_sections_of_affine` after `X` has been shrunk
> twice: by openness of the flat locus, Tag 0399 (`AlgebraicGeometry.isOpen_setOf_flatOverAt`), and
> by finiteness of the associated points of the fibre, Tag 05AF
> (`AlgebraicGeometry.associatedPoints_inter_finite`), which removes the ones not generalizing `x`.
> The affine open produced over the shrunken `X` is transported to `X ×_S S'` along the resulting
> open immersion.

```lean
theorem exists_affineOpen_projective_sections_of_chart
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFinitePresentation f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFinitePresentation]
    (s : S) (x : X) (hxs : f x = s) (hflat : IsFlatOverAt f.toLRSHom.toShHom F x) :
    ∃ (N : EtaleNeighborhood S s) (_ : N.IsElementary) (_ : IsAffine N.scheme)
      (x' : (pullback f N.toBase : Scheme.{u}))
      (_ : pullback.fst f N.toBase x' = x)
      (_ : pullback.snd f N.toBase x' = N.point)
      (U' : (pullback f N.toBase : Scheme.{u}).Opens)
      (_ : IsAffineOpen U') (_ : x' ∈ U'),
      let G := (Scheme.Modules.pullback (pullback.fst f N.toBase)).obj F
      letI : Module Γ(N.scheme, ⊤) Γ(G, U') :=
        Module.compHom Γ(G, U') ((pullback.snd f N.toBase).appLE ⊤ U' (by simp)).hom
      Module.Projective Γ(N.scheme, ⊤) Γ(G, U')
```

## Tag 05MF, a lemma

[Tag 05MF](https://stacks.math.columbia.edu/tag/05MF) in the Stacks Project.

**`AlgebraicGeometry.exists_elementaryEtaleNeighborhood_free_sections`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/FreeSections05MF.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/FreeSections05MF.lean#L153). The attribute's comment: “RESTRICTED: carries hproj, this same existential with Module.Projective in place of Module.Free and the clause on the image of x' in Spec 𝒪\_\{S', s'} dropped, which is the 05ME half of the source's proof (Lemma 05ME composed with Proposition 05I5)”.

> **Stacks Project, Tag 05MF.** A finite-type quasi-coherent module which is flat over the base
> at a point has free sections on an affine neighbourhood of the lifted point after base change to
> the local scheme of an affine elementary étale neighbourhood.
>
> The obligation `hproj` is Lemma 05ME composed with Proposition 05I5: the same existential with
> `Module.Projective` in place of `Module.Free`, and with nothing asserted about the image of `x'`
> in `Spec 𝒪_{S', s'}`. Projectivity becomes freeness by Kaplansky's theorem (Tag 0593), and the
> image of `x'` is the distinguished point automatically, by
> `AlgebraicGeometry.EtaleNeighborhood.fromSpecStalk_snd_eq_point`.

```lean
theorem exists_elementaryEtaleNeighborhood_free_sections
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType] (x : X)
    (hflat : IsFlatOverAt f.toLRSHom.toShHom F x)
    (hproj : IsFlatOverAt f.toLRSHom.toShHom F x →
      ∃ (N : EtaleNeighborhood S (f x)),
        N.IsElementary ∧ IsAffine N.scheme ∧
          let g := N.scheme.fromSpecStalk N.point ≫ N.toBase
          let P := pullback f g
          ∃ (x' : P) (W : P.Opens),
            pullback.fst f g x' = x ∧
              IsAffineOpen W ∧ x' ∈ W ∧
                let F' := (Scheme.Modules.pullback (pullback.fst f g)).obj F
                letI : Module (N.scheme.presheaf.stalk N.point) Γ(F', W) :=
                  Module.compHom Γ(F', W)
                    (((Scheme.ΓSpecIso (.of (N.scheme.presheaf.stalk N.point))).inv ≫
                      (pullback.snd f g).appLE ⊤ W (by simp)).hom)
                Module.Projective (N.scheme.presheaf.stalk N.point) Γ(F', W)) :
    ∃ (N : EtaleNeighborhood S (f x)),
      N.IsElementary ∧ IsAffine N.scheme ∧
        let g := N.scheme.fromSpecStalk N.point ≫ N.toBase
        let P := pullback f g
        ∃ (x' : P) (W : P.Opens),
          pullback.fst f g x' = x ∧
            N.scheme.fromSpecStalk N.point (pullback.snd f g x') = N.point ∧
            IsAffineOpen W ∧ x' ∈ W ∧
              let F' := (Scheme.Modules.pullback (pullback.fst f g)).obj F
              letI : Module (N.scheme.presheaf.stalk N.point) Γ(F', W) :=
                Module.compHom Γ(F', W)
                  (((Scheme.ΓSpecIso (.of (N.scheme.presheaf.stalk N.point))).inv ≫
                    (pullback.snd f g).appLE ⊤ W (by simp)).hom)
              Module.Free (N.scheme.presheaf.stalk N.point) Γ(F', W)
```

**`AlgebraicGeometry.exists_elementaryEtaleNeighborhood_free_sections_of_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/FreeSections05MF.lean, line 243](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/FreeSections05MF.lean#L243). The attribute's comment: “for f locally of finite presentation and F of finite presentation”.

> **Stacks Project, Tag 05MF** for a morphism locally of finite presentation and a module of
> finite presentation, with no hypothesis beyond flatness at the point.
>
> Under those hypotheses the obligation `hproj` of
> `AlgebraicGeometry.exists_elementaryEtaleNeighborhood_free_sections` is Lemma 05ME base changed to
> the local scheme of the neighbourhood it produces, which is
> `AlgebraicGeometry.exists_affineOpen_projective_sections_stalk`. The source states Tag 05MF for
> `f` locally of finite *type* and `F` of finite type, and reaches the hypotheses used here by a
> closed immersion into affine space and by Proposition 05I5; those two reductions are what the
> general statement still waits on.

```lean
theorem exists_elementaryEtaleNeighborhood_free_sections_of_finitePresentation
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFinitePresentation f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFinitePresentation] (x : X)
    (hflat : IsFlatOverAt f.toLRSHom.toShHom F x) :
    ∃ (N : EtaleNeighborhood S (f x)),
      N.IsElementary ∧ IsAffine N.scheme ∧
        let g := N.scheme.fromSpecStalk N.point ≫ N.toBase
        let P := pullback f g
        ∃ (x' : P) (W : P.Opens),
          pullback.fst f g x' = x ∧
            N.scheme.fromSpecStalk N.point (pullback.snd f g x') = N.point ∧
            IsAffineOpen W ∧ x' ∈ W ∧
              let F' := (Scheme.Modules.pullback (pullback.fst f g)).obj F
              letI : Module (N.scheme.presheaf.stalk N.point) Γ(F', W) :=
                Module.compHom Γ(F', W)
                  (((Scheme.ΓSpecIso (.of (N.scheme.presheaf.stalk N.point))).inv ≫
                    (pullback.snd f g).appLE ⊤ W (by simp)).hom)
              Module.Free (N.scheme.presheaf.stalk N.point) Γ(F', W)
```

**`AlgebraicGeometry.exists_elementaryEtaleNeighborhood_free_sections_of_finiteType`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/FreeSectionsFiniteType05MF.lean, line 890](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Etale/ElementaryNeighborhood/FreeSectionsFiniteType05MF.lean#L890).

> **Stacks Project, Tag 05MF.** A finite-type quasi-coherent module which is flat over the
> base at a point has free sections on an affine neighbourhood of the lifted point after base
> change to the local scheme of an affine elementary étale neighbourhood.

```lean
public theorem exists_elementaryEtaleNeighborhood_free_sections_of_finiteType
    {X S : Scheme.{u}} (f : X ⟶ S) [LocallyOfFiniteType f]
    (F : X.Modules) [F.IsQuasicoherent] [F.IsFiniteType] (x : X)
    (hflat : AlgebraicGeometry.IsFlatOverAt f.toLRSHom.toShHom F x) :
    ∃ (N : AlgebraicGeometry.EtaleNeighborhood S (f x)),
      N.IsElementary ∧ IsAffine N.scheme ∧
        let g := N.scheme.fromSpecStalk N.point ≫ N.toBase
        let P := pullback f g
        ∃ (x' : P) (W : P.Opens),
          pullback.fst f g x' = x ∧
            N.scheme.fromSpecStalk N.point (pullback.snd f g x') = N.point ∧
            IsAffineOpen W ∧ x' ∈ W ∧
              let F' := (Scheme.Modules.pullback (pullback.fst f g)).obj F
              letI : Module (N.scheme.presheaf.stalk N.point) Γ(F', W) :=
                Module.compHom Γ(F', W)
                  (((Scheme.ΓSpecIso (.of (N.scheme.presheaf.stalk N.point))).inv ≫
                    (pullback.snd f g).appLE ⊤ W (by simp)).hom)
              Module.Free (N.scheme.presheaf.stalk N.point) Γ(F', W)
```

## Tag 05U7, a lemma

[Tag 05U7](https://stacks.math.columbia.edu/tag/05U7) in the Stacks Project.

**`exists_filteredColimit_free_with_injective_reduction_and_isMittagLeffler`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/HenselianEssFiniteTypeColimit.lean, line 165](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/HenselianEssFiniteTypeColimit.lean#L165).

> **Stacks Project, Tag 05U7.** Let `A → B` be a local homomorphism of local rings which is
> essentially of finite type, and let `N` be a finite `B`-module which is flat as an `A`-module. If
> `A` is henselian, then `N` is a filtered colimit `N = colim_i F_i` of free `A`-modules `F_i` such
> that every transition map `F_i → F_{i'}` of the system induces an injective map
> `F_i/𝔪_A F_i → F_{i'}/𝔪_A F_{i'}`. Also, `N` is a Mittag-Leffler `A`-module.
>
> The colimit is computed in `ModuleCat A`, in the joint universe of `A` and `N`, so its vertex is
> compared with the universe lift of `N`; `F_i/𝔪_A F_i` is `F_i ⧸ 𝔪_A • ⊤` and the induced map is
> `Submodule.mapQ`. The Mittag-Leffler condition is that of Stacks 059F, with the finitely
> presented source and the test module in arbitrary universes.

```lean
theorem exists_filteredColimit_free_with_injective_reduction_and_isMittagLeffler
    {A : Type u} {B : Type v} {N : Type uM} [CommRing A] [CommRing B]
    [IsLocalRing B] [HenselianLocalRing A]
    [Algebra A B] [IsLocalHom (algebraMap A B)]
    (hB : Algebra.EssFiniteType A B)
    [AddCommGroup N] [Module A N] [Module B N] [IsScalarTower A B N]
    [Module.Finite B N] [Module.Flat A N] :
    (∃ (I : Type (max u uM)) (_ : SmallCategory I) (_ : IsFiltered I)
      (F : I ⥤ ModuleCat.{max u uM} A) (c : Cocone F),
      (∀ i, Module.Free A (F.obj i)) ∧
      (∀ {i j : I} (f : i ⟶ j), Function.Injective
        (Submodule.mapQ
          (maximalIdeal A • (⊤ : Submodule A (F.obj i)))
          (maximalIdeal A • (⊤ : Submodule A (F.obj j)))
          (F.map f).hom
          (Submodule.smul_top_le_comap_smul_top (maximalIdeal A)
            (F.map f).hom))) ∧
      Nonempty (IsColimit c) ∧
      Nonempty (c.pt ≅ ModuleCat.of A (ULift.{u} N))) ∧
    IsMittagLeffler.{u, uP, uM, max u uQ, uN} A N
```

**`isMittagLeffler_of_flat_finite_essFiniteType_local`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/MittagLefflerEssFiniteType.lean, line 330](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/MittagLefflerEssFiniteType.lean#L330). The attribute's comment: “the Mittag-Leffler conclusion”.

> Let `A → B` be an essentially finite type local homomorphism of local rings with `A`
> henselian, and let `N` be a finite `B`-module which is flat over `A`. Then `N` is a
> Mittag-Leffler `A`-module.

```lean
theorem isMittagLeffler_of_flat_finite_essFiniteType_local
    {A : Type u} {B : Type v} {N : Type uM} [CommRing A] [CommRing B]
    [IsLocalRing B] [HenselianLocalRing A]
    [Algebra A B] [IsLocalHom (algebraMap A B)]
    (hB : Algebra.EssFiniteType A B)
    [AddCommGroup N] [Module A N] [Module B N] [IsScalarTower A B N]
    [Module.Finite B N] [Module.Flat A N] :
    IsMittagLeffler.{u, uP, uM, max u uQ, uN} A N
```

**`exists_filteredColimit_free_with_injective_reduction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/MittagLefflerFilteredColimitPresentation/FreePresentation.lean, line 580](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/MittagLefflerFilteredColimitPresentation/FreePresentation.lean#L580). The attribute's comment: “filtered-colimit presentation”.

> Let `A` be a henselian local ring, `A → B` a local homomorphism of local rings with `B`
> essentially of finite type over `A`, and `N` a finite `B`-module which is flat over `A`. Then `N`
> is a filtered colimit of free `A`-modules `F i` such that every transition map `F i → F j` induces
> an injective map `F i / 𝔪_A F i → F j / 𝔪_A F j`.

```lean
public theorem exists_filteredColimit_free_with_injective_reduction
    {A : Type u} {B : Type v} {N : Type uM} [CommRing A] [CommRing B]
    [IsLocalRing B] [HenselianLocalRing A]
    [Algebra A B] [IsLocalHom (algebraMap A B)]
    (hB : Algebra.EssFiniteType A B)
    [AddCommGroup N] [Module A N] [Module B N] [IsScalarTower A B N]
    [Module.Finite B N] [Module.Flat A N] :
    ∃ (I : Type (max u uM)) (_ : SmallCategory I) (_ : IsFiltered I)
      (F : I ⥤ ModuleCat.{max u uM} A) (c : Cocone F),
      (∀ i, Module.Free A (F.obj i)) ∧
      (∀ {i j : I} (f : i ⟶ j), Function.Injective
        (Submodule.mapQ
          (maximalIdeal A • (⊤ : Submodule A (F.obj i)))
          (maximalIdeal A • (⊤ : Submodule A (F.obj j)))
          (F.map f).hom
          (Submodule.smul_top_le_comap_smul_top (maximalIdeal A)
            (F.map f).hom))) ∧
      Nonempty (IsColimit c) ∧
      Nonempty (c.pt ≅ ModuleCat.of A (ULift.{u} N))
```

## Tag 0ASX, a lemma

[Tag 0ASX](https://stacks.math.columbia.edu/tag/0ASX) in the Stacks Project.

**`IsContentIdeal.isPrincipal_of_valuationRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/ContentIdeal.lean, line 52](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/ContentIdeal.lean#L52). The attribute's comment: “the principality assertion, unconditionally and in strengthened form: no hypothesis beyond `ValuationRing A` is used, since a content ideal is finitely generated (0ASB) and a valuation ring is Bézout (090Q).”.

> **Stacks Tag 0ASX**, the principality assertion. A content ideal of an element of a module
> over a valuation ring is a principal ideal.
>
> The source states this for a finite module over an essentially finite type local algebra which
> is flat over the valuation ring, but, as its proof shows, none of that is used: a content ideal
> is finitely generated by Stacks 0ASB, and in a valuation ring every finitely generated ideal is
> principal by Stacks 090Q. Flatness of the module is not needed either, for the same reason it is
> not needed in Stacks 0ASB. Dropping the hypotheses only strengthens the statement.

```lean
theorem IsContentIdeal.isPrincipal_of_valuationRing
    {A : Type u} [CommRing A] [IsDomain A] [ValuationRing A]
    {N : Type w} [AddCommGroup N] [Module A N]
    {x : N} {I : Ideal A} (hI : IsContentIdeal x I) : I.IsPrincipal
```

**`exists_isContentIdeal_isPrincipal_of_valuationRing_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Valuation/ContentIdealExistence.lean, line 511](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Valuation/ContentIdealExistence.lean#L511).

> **Stacks Tag 0ASX.** Let `A → B` be a local ring map of local rings which is essentially of
> finite type, and let `N` be a finite `B`-module which is flat as an `A`-module. If `A` is a
> valuation ring, then every element `x` of `N` has a content ideal `I ⊆ A` in the sense of
> Stacks 0ASA, and that ideal is principal.
>
> Existence is `exists_isContentIdeal_of_valuationRing` and principality is
> `IsContentIdeal.isPrincipal_of_valuationRing`.

```lean
theorem exists_isContentIdeal_isPrincipal_of_valuationRing_of_flat
    {A : Type u} {B : Type v} {N : Type w}
    [CommRing A] [IsDomain A] [ValuationRing A]
    [CommRing B] [IsLocalRing B] [Algebra A B] [IsLocalHom (algebraMap A B)]
    [Algebra.EssFiniteType A B]
    [AddCommGroup N] [Module A N] [Module B N] [IsScalarTower A B N]
    [Module.Finite B N] [Module.Flat A N]
    (x : N) :
    ∃ I : Ideal A, IsContentIdeal x I ∧ I.IsPrincipal
```

## Tag 0H2T, a lemma

[Tag 0H2T](https://stacks.math.columbia.edu/tag/0H2T) in the Stacks Project.

**`isReduced_and_isReduced_fiber_of_isProper_over_valuationRing`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/ReducedOverValuationRing.lean, line 437](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Fibres/ReducedOverValuationRing.lean#L437).

> Let `f : X ⟶ Spec R` be a proper flat morphism where `R` is a valuation ring. If the special
> fibre is reduced, then `X` and every fibre of `X ⟶ Spec R` are reduced.

```lean
public theorem isReduced_and_isReduced_fiber_of_isProper_over_valuationRing
    {R : Type u} [CommRing R] [IsDomain R] [ValuationRing R]
    {X : Scheme.{u}} (f : X ⟶ Spec (.of R)) [IsProper f] [Flat f]
    (hspecial : IsReduced (f.fiber (IsLocalRing.closedPoint R))) :
    IsReduced X ∧ ∀ s : Spec (.of R), IsReduced (f.fiber s)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 38.19, Tag 05L7](https://stacks.math.columbia.edu/tag/05L7)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
