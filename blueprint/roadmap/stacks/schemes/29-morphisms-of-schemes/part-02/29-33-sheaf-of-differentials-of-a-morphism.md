---
declaration: section
origin: cited
lean: Stacks.Smooth.cotangentDerivation, Stacks.Smooth.cotangentSheaf, AlgebraicGeometry.SheafOfModules.universalDerivation_isUniversal, Stacks.AlgebraicGeometry.DifferentialsRestrict.existsUnique_relativeDifferentials_restrict, AlgebraicGeometry.AffineDerivations.globalSectionsDerivation_bijective, Stacks.AlgebraicGeometry.AffineDifferentialsIso.existsUnique_sectionsIso, Stacks.AlgebraicGeometry.AffineDifferentialsIso.existsUnique_tildeKaehlerIso, Stacks.AlgebraicGeometry.AffineDifferentialsIso.existsUnique_affineDifferentialsIso
statement: formalized
proof: formalized
---

# 29.33 Sheaf of differentials of a morphism

Section 29.33 of the Stacks Project, [Tag 01UM](https://stacks.math.columbia.edu/tag/01UM). 18 tags here are carried by 49 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01UQ, a definition

[Tag 01UQ](https://stacks.math.columbia.edu/tag/01UQ) in the Stacks Project.

**`Stacks.Smooth.cotangentDerivation`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Smooth/CotangentDerivation.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Smooth/CotangentDerivation.lean#L70). The attribute's comment: “the universal S-derivation d\_\{X/S} that the sheaf of differentials `Stacks.Smooth.cotangentSheaf` of a morphism of schemes is equipped with”.

> The universal `S`-derivation `d_{X/S} : 𝒪_X ⟶ Ω_{X/S}` that the sheaf of differentials of a
> morphism of schemes `f : X ⟶ S` is equipped with: the universal derivation of the underlying
> morphism of ringed spaces, read as a relative derivation over the structural map
> `f⁻¹𝒪_S ⟶ 𝒪_X` of `f`.

```lean
noncomputable def cotangentDerivation :
    SheafOfModules.SheafDerivation (inverseImageStructureMap f) (cotangentSheaf f)
```

**`Stacks.Smooth.cotangentSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Smooth/CotangentSheafScheme.lean, line 93](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Smooth/CotangentSheafScheme.lean#L93). The attribute's comment: “the sheaf of differentials of a morphism of schemes, namely the differentials of the underlying morphism of ringed spaces; the universal S-derivation d\_\{X/S} it is equipped with is `Stacks.Smooth.cotangentDerivation`”. References: SGA 6 0 (2.1).

> The sheaf of relative differentials `Ω_{X/S}` of a morphism of schemes `f : X ⟶ S`, as a
> sheaf of `𝒪_X`-modules: the module of differentials of the morphism of sheaves of rings
> `f⁻¹𝒪_S ⟶ 𝒪_X`, which is how Stacks Project, Tag 01UM defines it.

```lean
noncomputable def cotangentSheaf {X S : Scheme.{u}} (f : X ⟶ S) : X.Modules
```

## Tag 01UR, a lemma

[Tag 01UR](https://stacks.math.columbia.edu/tag/01UR) in the Stacks Project.

**`AlgebraicGeometry.SheafOfModules.universalDerivation_isUniversal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/Differentials.lean, line 130](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Modules/Differentials.lean#L130). The attribute's comment: “postcomposition with the universal derivation is bijective onto the derivations”. References: EGA IV (16.5.3), “(ii)”.

> **Stacks Project, Tag 08RM.** Postcomposition with the universal
> derivation gives the unique morphism from the module of relative
> differentials to any coefficient sheaf.

```lean
theorem universalDerivation_isUniversal {X : TopCat.{u}}
    {O₁ O₂ : TopCat.Sheaf CommRingCat.{max u v} X} (φ : O₁ ⟶ O₂) :
    IsUniversal.{u, v, u_1} (universalDerivation.{u, v, u_1} φ)
```

## Tag 01US, a lemma

[Tag 01US](https://stacks.math.columbia.edu/tag/01US) in the Stacks Project.

**`Stacks.AlgebraicGeometry.DifferentialsRestrict.existsUnique_relativeDifferentials_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DifferentialsRestrict/Basic.lean, line 488](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DifferentialsRestrict/Basic.lean#L488).

> Restricting a morphism of schemes to compatible open subschemes identifies the
> restriction of its sheaf of relative differentials with the sheaf of relative differentials
> of the restricted morphism, and this is the unique identification carrying the restricted
> universal derivation to the universal derivation.

```lean
theorem existsUnique_relativeDifferentials_restrict :
    ∃! i : Scheme.Modules.restrict (Scheme.Hom.relativeDifferentials f) U.ι ≅
        Scheme.Hom.relativeDifferentials (f.resLE V U e),
      ∀ (W : U.toScheme.Opens) (x : Γ(U.toScheme, W)),
        (i.hom.val.app (.op W)).hom
            ((Scheme.Modules.restrictAppIso U.ι
                (Scheme.Hom.relativeDifferentials f) W).inv.hom
              ((Scheme.Hom.universalRelativeDerivation f).d (((U.ι.appIso W).inv).hom x))) =
          (Scheme.Hom.universalRelativeDerivation (f.resLE V U e)).d x
```

## Tag 01UO, a lemma

[Tag 01UO](https://stacks.math.columbia.edu/tag/01UO) in the Stacks Project.

**`AlgebraicGeometry.AffineDerivations.globalSectionsDerivation_bijective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Recovery252629/Chapter29.lean, line 708](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Recovery252629/Chapter29.lean#L708). References: EGA IV (16.5.2).

> **Stacks Project, Tag 01UO.** On an affine scheme, evaluation on global
> sections gives a bijection from relative sheaf derivations to relative ring
> derivations.

```lean
theorem globalSectionsDerivation_bijective {R A : CommRingCat.{u}} (φ : R ⟶ A)
    (F : SheafOfModules.{v} (SheafOfModules.underlyingRingSheaf (Spec A).sheaf)) :
    Function.Bijective (globalSectionsDerivation φ F)
```

## Tag 01UT, a lemma

[Tag 01UT](https://stacks.math.columbia.edu/tag/01UT) in the Stacks Project.

**`Stacks.AlgebraicGeometry.AffineDifferentialsIso.existsUnique_sectionsIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineDifferentialsIso/SpecComparison.lean, line 300](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/AffineDifferentialsIso/SpecComparison.lean#L300). The attribute's comment: “affine case in the coordinate rings: the global differentials of Spec φ are Ω[A⁄R]”.

> **Uniqueness of the comparison of global differentials.** There is exactly one isomorphism
> of `A`-modules from `Ω[A⁄R]` to the global differentials of `Spec φ` compatible with the
> universal derivations.

```lean
theorem existsUnique_sectionsIso :
    ∃! e : CommRingCat.KaehlerDifferential φ ≅
        moduleSpecΓFunctor.obj (Scheme.Hom.relativeDifferentials (Spec.map φ)),
      ∀ a : A, e.hom.hom (CommRingCat.KaehlerDifferential.d a) =
        (Scheme.Hom.universalRelativeDerivation (Spec.map φ)).d ((Scheme.ΓSpecIso A).inv a)
```

**`Stacks.AlgebraicGeometry.AffineDifferentialsIso.existsUnique_tildeKaehlerIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineDifferentialsIso/SpecComparison.lean, line 358](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/AffineDifferentialsIso/SpecComparison.lean#L358). The attribute's comment: “affine case as a sheaf comparison: Ω\_\{Spec A/Spec R} is the sheaf of Ω[A⁄R]”.

> **Uniqueness of the comparison of sheaves.** There is exactly one isomorphism from the
> quasi-coherent sheaf associated to `Ω[A⁄R]` to the sheaf of relative differentials of `Spec φ`
> carrying the global section determined by the universal differential of `a : A` to the
> universal relative differential of the global section of `𝒪_{Spec A}` corresponding to `a`.

```lean
theorem existsUnique_tildeKaehlerIso :
    ∃! e : (tilde.functor A).obj (CommRingCat.KaehlerDifferential φ) ≅
        Scheme.Hom.relativeDifferentials (Spec.map φ),
      ∀ a : A,
        (tilde.toTildeΓNatIso.hom.app (CommRingCat.KaehlerDifferential φ) ≫
            moduleSpecΓFunctor.map e.hom).hom (CommRingCat.KaehlerDifferential.d a) =
          (Scheme.Hom.universalRelativeDerivation (Spec.map φ)).d
            ((Scheme.ΓSpecIso A).inv a)
```

**`Stacks.AlgebraicGeometry.AffineDifferentialsIso.existsUnique_affineDifferentialsIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AffineDifferentialsIso/Surjective.lean, line 481](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/AffineDifferentialsIso/Surjective.lean#L481).

> **Stacks Project, Tag 01UT.** Let `f : X ⟶ S` be a morphism of schemes, let `V` be an
> affine open of `S` and let `U ≤ f ⁻¹ᵁ V` be an affine open of `X`. The sections of the sheaf
> of relative differentials of `f` on `U` are *uniquely* isomorphic to the Kähler differentials
> of `Γ(S, V) ⟶ Γ(X, U)`, compatibly with the universal derivations.

```lean
theorem existsUnique_affineDifferentialsIso (hV : IsAffineOpen V) :
    ∃! e : (Scheme.Hom.relativeDifferentials f).val.obj (.op U) ≅
        CommRingCat.KaehlerDifferential (f.appLE V U hUV),
      ∀ a : Γ(X, U), e.hom.hom ((Scheme.Hom.universalRelativeDerivation f).d a) =
        CommRingCat.KaehlerDifferential.d a
```

**`Stacks.Smooth.existsUnique_linearEquiv_universalD`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Smooth/CotangentSectionsAffineOpen.lean, line 310](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Smooth/CotangentSectionsAffineOpen.lean#L310). The attribute's comment: “unique isomorphism Γ(U, Ω\_\{X/S}) = Ω\_\{A/R} compatible with the differentials”.

> Let `f : X ⟶ S` be a morphism of schemes. For any pair of affine opens `Spec A = U ⊆ X` and
> `Spec R = V ⊆ S` with `f(U) ⊆ V` there is a unique isomorphism
>
> `Ω[A⁄R] ≃ₗ[A] Γ(Ω_{X/S}, U)`
>
> compatible with `d_{X/S}` and with `d : A → Ω[A⁄R]`.

```lean
theorem existsUnique_linearEquiv_universalD (hU : IsAffineOpen U) (hV : IsAffineOpen V)
    (hUV : U ≤ f ⁻¹ᵁ V) :
    letI := algebraAppLE f hUV
    ∃! e : Ω[Γ(X, U)⁄Γ(S, V)] ≃ₗ[Γ(X, U)] Γ(cotangentSheaf f, U),
      ∀ b : Γ(X, U), e (KaehlerDifferential.D Γ(S, V) Γ(X, U) b) = universalD f U b
```

## Tag 01UU, a remark

[Tag 01UU](https://stacks.math.columbia.edu/tag/01UU) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isBasis_affineOpensOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/AffineBasis.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/AffineBasis.lean#L143). The attribute's comment: “the affine opens mapping into an affine open of the base form a basis”.

> **The affine opens over affine opens form a basis.** The affine opens of `X` mapping into
> an affine open of `S` form a basis of the topology of `X`.

```lean
theorem isBasis_affineOpensOver : Opens.IsBasis f.affineOpensOver
```

**`AlgebraicGeometry.Scheme.Hom.kaehlerOnAffineOpensOver`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/AffineBasis.lean, line 209](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/AffineBasis.lean#L209). The attribute's comment: “the presheaf on the basis with sections the Kähler differentials”.

> **The ansatz `Γ(U, Ω_{X/S}) = Ω_{A/R}`.** The presheaf of modules on the basis
> `f.affineOpensOver`, over the restriction of `𝒪_X`, with sections the Kähler differentials
> `Ω_{A/R}` over `U = Spec A` lying over `V = Spec R`. Its restriction maps are described by
> `kaehlerOnAffineOpensOver_map_d`.

```lean
noncomputable def kaehlerOnAffineOpensOver :
    _root_.PresheafOfModules.{u} (restrictRingSheafToBasis
      f.isBasis_affineOpensOver X.ringCatSheaf).obj
```

**`AlgebraicGeometry.Scheme.Hom.kaehlerOnAffineOpensOver_map_d`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/AffineBasis.lean, line 220](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/AffineBasis.lean#L220). The attribute's comment: “the restriction maps”.

> **The restriction maps.** For `U' ⊆ U` in the basis, the restriction map
> `Ω_{A/R} ⟶ Ω_{A'/R'}` sends `d a` to `d (a|_{U'})`.

```lean
theorem kaehlerOnAffineOpensOver_map_d
    {U U' : BasisCat f.affineOpensOver} (i : U' ⟶ U)
    (a : Γ(X, U.obj)) :
    (f.kaehlerOnAffineOpensOver.map i.op).hom (CommRingCat.KaehlerDifferential.d a) =
      CommRingCat.KaehlerDifferential.d
        (X.presheaf.map ((basisInclusion _).map i).op a)
```

**`AlgebraicGeometry.Scheme.Hom.isSheaf_kaehlerOnAffineOpensOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/AffineBasis.lean, line 235](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/AffineBasis.lean#L235). The attribute's comment: “the sheaf condition”.

> **The sheaf condition.** The presheaf with sections `Ω_{A/R}` is a sheaf on the basis.

```lean
theorem isSheaf_kaehlerOnAffineOpensOver :
    Presheaf.IsSheaf (basisGrothendieckTopology f.isBasis_affineOpensOver)
      f.kaehlerOnAffineOpensOver.presheaf
```

**`AlgebraicGeometry.Scheme.Hom.restrictRelativeDifferentialsIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/AffineBasis.lean, line 253](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/AffineBasis.lean#L253). The attribute's comment: “the sheaf on the basis is the restriction of the sheaf of differentials”.

> **The construction gives `Ω_{X/S}`.** The restriction of the sheaf of relative
> differentials to the basis `f.affineOpensOver` is the sheaf with sections `Ω_{A/R}`; on
> sections it is the identification of Stacks 01UT
> (`restrictRelativeDifferentialsIso_hom_app_d`).

```lean
noncomputable def restrictRelativeDifferentialsIso :
    (restrictModuleSheaf.{u, u} f.isBasis_affineOpensOver
      X.ringCatSheaf).obj (relativeDifferentials f) ≅ f.kaehlerSheafOnAffineOpensOver
```

**`AlgebraicGeometry.Scheme.Hom.nonempty_iso_relativeDifferentials_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/AffineBasis.lean, line 270](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/AffineBasis.lean#L270). The attribute's comment: “the sheaf on the basis determines the sheaf of differentials”.

> **The sheaf on the basis determines `Ω_{X/S}`.** A sheaf of `𝒪_X`-modules is isomorphic to
> the sheaf of relative differentials if and only if its restriction to the basis
> `f.affineOpensOver` is isomorphic to the sheaf with sections `Ω_{A/R}`.

```lean
theorem nonempty_iso_relativeDifferentials_iff (M : X.Modules) :
    Nonempty (M ≅ relativeDifferentials f) ↔
      Nonempty ((restrictModuleSheaf.{u, u} f.isBasis_affineOpensOver
        X.ringCatSheaf).obj M ≅ f.kaehlerSheafOnAffineOpensOver)
```

## Tag 08S2, a lemma

[Tag 08S2](https://stacks.math.columbia.edu/tag/08S2) in the Stacks Project.

**`Stacks.Tag08S2Assembly.relativeDifferentialsIsoDiagonalConormal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Assembly/Basic.lean, line 543](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Assembly/Basic.lean#L543). References: EGA IV (16.3.1), “Ω¹\_\{X/S}=Gr₁(Δ\_f)”; EGA IV (17.13.5); SGA 7 VI (5.5), “ordinary schemes”.

> **[Stacks, Tag 08S2].** The canonical isomorphism from the sheaf of relative differentials
> of `X` over `S` to the conormal sheaf of its diagonal in `X ×_S X`.
>
> This is `Stacks.LeibnizDerivation.diagonalConormalIso`, whose single hypothesis
> `IsIso (Stacks.LeibnizDerivation.toConormal f)` is now discharged by `isIso_toConormal` and so
> is carried by no argument here: `f` is an arbitrary morphism of schemes, and nothing is affine,
> separated, Noetherian or quasi-compact.

```lean
noncomputable def relativeDifferentialsIsoDiagonalConormal :
    Scheme.Hom.relativeDifferentials f ≅
      Stacks.Conormal.conormalSheaf (pullback.diagonal f)
```

**`Stacks.Tag08S2Assembly.relativeDifferentialsIsoDiagonalConormal_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Assembly/Basic.lean, line 556](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Assembly/Basic.lean#L556). The attribute's comment: “canonical quotient formula”.

> **[Stacks, Tag 08S2], the canonical quotient formula.** The comparison isomorphism sends
> `d b` to the image of `p₂^♯ b - p₁^♯ b` under the canonical quotient map from the ideal sheaf of
> the diagonal to its conormal sheaf, on any open `V` of the coborder neighbourhood admitting the
> tag's two containments.
>
> This is `Stacks.LeibnizDerivation.diagonalConormalIso_hom_d_eq_quotientMap`, again with its
> hypothesis discharged.

```lean
theorem relativeDifferentialsIsoDiagonalConormal_apply
    (V : (pullback.diagonal f).coborderRange.toScheme.Opens)
    (h₁ : (pullback.diagonal f).coborderRange.ι ''ᵁ V ≤
      (pullback.fst f f) ⁻¹ᵁ ((pullback.diagonal f).liftCoborder ⁻¹ᵁ V))
    (h₂ : (pullback.diagonal f).coborderRange.ι ''ᵁ V ≤
      (pullback.snd f f) ⁻¹ᵁ ((pullback.diagonal f).liftCoborder ⁻¹ᵁ V))
    (b : Γ(X, (pullback.diagonal f).liftCoborder ⁻¹ᵁ V))
    (x : (Stacks.ClosedImmersion.idealSheaf
      (pullback.diagonal f).liftCoborder.toLRSHom.toShHom).val.obj (.op V))
    (hx : (kernel.ι (SheafOfModules.unitToPushforwardObjUnit (structureSheafHom
        (pullback.diagonal f).liftCoborder.toLRSHom.toShHom))).val.app (.op V) x =
      ((pullback.snd f f).appLE _ _ h₂).hom b - ((pullback.fst f f).appLE _ _ h₁).hom b) :
    ((relativeDifferentialsIsoDiagonalConormal f).hom.val.app
          (.op ((pullback.diagonal f).liftCoborder ⁻¹ᵁ V))).hom
        ((Scheme.Hom.universalRelativeDerivation f).d b) =
      (Stacks.Conormal.conormalQuotientMap (pullback.diagonal f)
        (pullback.diagonal f).coborderRange (pullback.diagonal f).liftCoborder
        (pullback.diagonal f).liftCoborder_ι).val.app (.op V) x
```

## Tag 01UV, a lemma

[Tag 01UV](https://stacks.math.columbia.edu/tag/01UV) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.existsUnique_relativeDifferentialsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/Functoriality.lean, line 110](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/Functoriality.lean#L110). References: EGA IV (16.5.13), “more general”; EGA IV (17.3.6), “more general”; SGA 3 III (0.1.7), “partial”.

> A commutative square of schemes induces a unique morphism `f^* Ω_{X/S} ⟶ Ω_{X'/S'}`
> carrying the universal differential of every local section to the universal differential of
> its pullback.

```lean
theorem existsUnique_relativeDifferentialsMap {X' X S' S : Scheme.{u}} (f : X' ⟶ X)
    (p : X ⟶ S) (p' : X' ⟶ S') (g : S' ⟶ S) (hcomm : f ≫ p = p' ≫ g) :
    ∃! c : (Scheme.Modules.pullback f).obj (relativeDifferentials p) ⟶
      relativeDifferentials p', IsRelativeDifferentialsMap f p p' c
```

**`AlgebraicGeometry.Scheme.Hom.isRelativeDifferentialsMap_iff_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/Functoriality.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/Functoriality.lean#L137). The attribute's comment: “characterization of the canonical map”.

> Compatibility with the universal derivations characterizes the canonical morphism on
> relative differentials associated to a commutative square of schemes.

```lean
theorem isRelativeDifferentialsMap_iff_eq {X' X S' S : Scheme.{u}} (f : X' ⟶ X)
    (p : X ⟶ S) (p' : X' ⟶ S') (g : S' ⟶ S) (hcomm : f ≫ p = p' ≫ g)
    (c : (Scheme.Modules.pullback f).obj (relativeDifferentials p) ⟶
      relativeDifferentials p') :
    IsRelativeDifferentialsMap f p p' c ↔ c = relativeDifferentialsMap f p p' g hcomm
```

## Tag 01UX, a lemma

[Tag 01UX](https://stacks.math.columbia.edu/tag/01UX) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.toRelativeDifferentials_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/Triangle.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/Triangle.lean#L181). The attribute's comment: “exactness at the right term”.

> **Stacks Project, Tag 01UX.** The canonical map `Ω_{X/S} ⟶ Ω_{X/Y}` of a composable pair of
> morphisms of schemes is an epimorphism; equivalently, the canonical sequence
> `f^* Ω_{Y/S} ⟶ Ω_{X/S} ⟶ Ω_{X/Y} ⟶ 0` is exact at `Ω_{X/Y}`. For the underlying ringed spaces
> this is Stacks Project, Tag 0H79.

```lean
theorem toRelativeDifferentials_epi (f : X ⟶ Y) (g : Y ⟶ S) :
    Epi (f.toRelativeDifferentials g)
```

**`AlgebraicGeometry.Scheme.Hom.toRelativeDifferentials_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/Triangle.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/Triangle.lean#L195). The attribute's comment: “exactness at the middle term”.

> **Stacks Project, Tag 01UX.** For morphisms of schemes `f : X ⟶ Y` and `g : Y ⟶ S` the
> canonical maps of relative differentials, both obtained from
> `AlgebraicGeometry.Scheme.Hom.relativeDifferentialsMap`, form a complex
> `f^* Ω_{Y/S} ⟶ Ω_{X/S} ⟶ Ω_{X/Y}` which is exact at `Ω_{X/S}`. Together with
> `AlgebraicGeometry.Scheme.Hom.toRelativeDifferentials_epi` this is the exactness of
> `f^* Ω_{Y/S} ⟶ Ω_{X/S} ⟶ Ω_{X/Y} ⟶ 0`. For the underlying ringed spaces this is Stacks
> Project, Tag 0H79.

```lean
theorem toRelativeDifferentials_exact (f : X ⟶ Y) (g : Y ⟶ S) :
    ∃ h : relativeDifferentialsMap f g (f ≫ g) (𝟙 S) (Category.comp_id (f ≫ g)).symm ≫
        f.toRelativeDifferentials g = 0,
      (ShortComplex.mk _ _ h).Exact
```

## Tag 01V0, a lemma

[Tag 01V0](https://stacks.math.columbia.edu/tag/01V0) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isIso_relativeDifferentialsMap_of_isPullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/BaseChange.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/BaseChange.lean#L119).

> **Stacks Project, Tag 01V0.** For a cartesian square of schemes with left edge `f' : X' ⟶ S'`,
> right edge `f : X ⟶ S` and top edge `g' : X' ⟶ X`, the canonical map
> `g'^* Ω_{X/S} ⟶ Ω_{X'/S'}` of Tag 01UV is an isomorphism.

```lean
theorem isIso_relativeDifferentialsMap_of_isPullback {X' X S' S : Scheme.{u}} (g' : X' ⟶ X)
    (f' : X' ⟶ S') (f : X ⟶ S) (g : S' ⟶ S) (h : IsPullback g' f' f g) :
    IsIso (relativeDifferentialsMap g' f f' g h.w)
```

## Tag 01V1, a lemma

[Tag 01V1](https://stacks.math.columbia.edu/tag/01V1) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isIso_biprodDesc_relativeDifferentialsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/BaseChange.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/BaseChange.lean#L152). References: EGA IV (16.4.23).

> **Stacks Project, Tag 01V1.** Let `f : X ⟶ S` and `g : Y ⟶ S` be morphisms of schemes with
> the same target and let `p : W ⟶ X`, `q : W ⟶ Y` be the projections of a fibre product of `f` and
> `g`. The two canonical maps of Tag 01UV give an isomorphism
> `p^* Ω_{X/S} ⊕ q^* Ω_{Y/S} ⟶ Ω_{W/S}`.

```lean
theorem isIso_biprodDesc_relativeDifferentialsMap {W X Y S : Scheme.{u}} (p : W ⟶ X) (q : W ⟶ Y)
    (f : X ⟶ S) (g : Y ⟶ S) (h : IsPullback p q f g) :
    IsIso (biprod.desc
      (relativeDifferentialsMap p f (p ≫ f) (𝟙 S) (Category.comp_id (p ≫ f)).symm)
      (relativeDifferentialsMap q g (p ≫ f) (𝟙 S)
        (h.w.symm.trans (Category.comp_id (p ≫ f)).symm)))
```

## Tag 01V2, a lemma

[Tag 01V2](https://stacks.math.columbia.edu/tag/01V2) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isFiniteType_relativeDifferentials`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/FiniteType.lean, line 86](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/FiniteType.lean#L86). References: EGA IV (17.4.1.2).

> **Stacks Project, Tag 01V2.** The sheaf of relative differentials of a morphism of schemes
> which is locally of finite type is an `𝒪_X`-module of finite type.

```lean
instance Scheme.Hom.isFiniteType_relativeDifferentials (f : X ⟶ S) [LocallyOfFiniteType f] :
    (Scheme.Hom.relativeDifferentials f).IsFiniteType
```

## Tag 01V3, a lemma

[Tag 01V3](https://stacks.math.columbia.edu/tag/01V3) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isFinitePresentation_relativeDifferentials`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/FinitePresentation.lean, line 85](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/FinitePresentation.lean#L85). References: EGA IV (16.4.22); EGA IV (17.4.1.2), “special case”; SGA 3 III (0.14), “more general”.

> **Stacks Project, Tag 01V3.** The sheaf of relative differentials of a morphism of schemes
> which is locally of finite presentation is an `𝒪_X`-module of finite presentation.

```lean
instance Scheme.Hom.isFinitePresentation_relativeDifferentials (f : X ⟶ S)
    [LocallyOfFinitePresentation f] :
    (Scheme.Hom.relativeDifferentials f).IsFinitePresentation
```

## Tag 01UY, a lemma

[Tag 01UY](https://stacks.math.columbia.edu/tag/01UY) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Hom.isZero_relativeDifferentials_of_mono`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Differentials.lean, line 75](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Differentials.lean#L75).

> The sheaf of relative differentials of a monomorphism of schemes is a zero object.

```lean
theorem isZero_relativeDifferentials_of_mono (f : X ⟶ S) [Mono f] :
    IsZero (relativeDifferentials f)
```

**`AlgebraicGeometry.Scheme.Hom.isZero_relativeDifferentials_of_isImmersion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Differentials.lean, line 81](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Unramified/Differentials.lean#L81). The attribute's comment: “the immersion case named in the first clause of the statement”.

> The sheaf of relative differentials of an immersion of schemes is a zero object.

```lean
theorem isZero_relativeDifferentials_of_isImmersion (f : X ⟶ S) [IsImmersion f] :
    IsZero (relativeDifferentials f)
```

## Tag 01UZ, a lemma

[Tag 01UZ](https://stacks.math.columbia.edu/tag/01UZ) in the Stacks Project.

**`Stacks.ConormalSequenceRight.differentialsMapOver_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalSequenceRight/Basic.lean, line 257](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ConormalSequenceRight/Basic.lean#L257). The attribute's comment: “exactness at the right term”. References: EGA IV (16.4.21), “→ 0 (surjectivity)”.

> **[Stacks, Tag 01UZ], exactness at the right term.** For an immersion `i : Z ⟶ X` of
> schemes over `S`, the canonical map `i^*Ω_{X/S} ⟶ Ω_{Z/S}` of [Stacks, Tag 01UV] is an
> epimorphism, so the conormal sequence of `i` ends in zero.

```lean
theorem differentialsMapOver_epi (i : Z ⟶ X) [IsImmersion i] (p : X ⟶ S) :
    Epi (Scheme.Hom.relativeDifferentialsMap i p (i ≫ p) (𝟙 S) (by simp))
```

**`Stacks.ConormalSequenceRight.conormalDifferential`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalSequenceRight/Basic.lean, line 380](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ConormalSequenceRight/Basic.lean#L380). The attribute's comment: “the first arrow”.

> **[Stacks, Tag 01UZ], the first arrow.** For an immersion `i : Z ⟶ X` of schemes over `S`,
> the canonical morphism `𝒞_{Z/X} ⟶ i^*Ω_{X/S}` induced by `d_{X/S}`: the adjoint transpose of
> the map carrying a section `f` of the defining ideal sheaf of the closed factor to `1 ⊗ d f`.

```lean
noncomputable def conormalDifferential :
    (conormalSheaf i : Z.Modules) ⟶
      (Scheme.Modules.pullback i).obj (Scheme.Hom.relativeDifferentials p)
```

**`Stacks.ConormalSequenceRight.equationDifferentialsComplexOver_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalSequenceRight/Middle.lean, line 394](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ConormalSequenceRight/Middle.lean#L394). The attribute's comment: “exactness at the middle term”.

> **[Stacks, Tag 01UZ], exactness at the middle term.** For an immersion `i : Z ⟶ X` of schemes
> over `S` cut out by global sections `f j` of `𝒪_X`, the conormal sequence is exact at
> `i^*Ω_{X/S}`: the kernel of the canonical map `i^*Ω_{X/S} ⟶ Ω_{Z/S}` of [Stacks, Tag 01UV] is
> generated by the pulled-back differentials `d (f j)`, which generate the image of the conormal
> module of the immersion.

```lean
theorem equationDifferentialsComplexOver_exact (i : Z ⟶ X) [IsImmersion i] (p : X ⟶ S)
    {I : Type u} (f : I → Γ(X, ⊤)) (hf : IsCutOutBy i f) :
    (equationDifferentialsComplex i p (by simp) f hf).Exact
```

**`Stacks.ConormalSequenceRight.conormalShortComplex_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalSequenceRight/SchemeShortExact.lean, line 359](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ConormalSequenceRight/SchemeShortExact.lean#L359). The attribute's comment: “exactness at the middle term of the sequence 𝒞\_\{Z/X} ⟶ i^*Ω\_\{X/S} ⟶ Ω\_\{Z/S}, for an arbitrary immersion and with the conormal sheaf itself at the left-hand end”. References: SGA 7 XI (1.3), “partial”.

> **[Stacks, Tag 01UZ], exactness at the middle term of the conormal sequence,
> unconditionally.** For an immersion of schemes `i : Z ⟶ X` over `p : X ⟶ S` the conormal
> sequence `𝒞_{Z/X} ⟶ i^*Ω_{X/S} ⟶ Ω_{Z/S} ⟶ 0` is exact at `i^*Ω_{X/S}`: the image of the
> conormal differential is the kernel of the canonical map of [Stacks, Tag 01UV].
>
> No hypothesis beyond `IsImmersion i` is used, and the sequence is the canonical one rather than
> a presentation by equations. Injectivity of the first arrow, which would make the sequence short
> exact, is false in general and holds under the smoothness hypothesis of [Stacks, Tag 06AA]; see
> `Stacks.ConormalSequenceRight.conormalShortComplex_shortExact`.

```lean
theorem conormalShortComplex_exact (p : X ⟶ S) : (conormalShortComplex i p).Exact
```

Declarations registered for the tag:

- [`AlgebraicGeometry.Scheme.Hom.relativeDifferentialsMap`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/Functoriality.lean#L122), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/ConormalSequenceRight/Basic.lean, line 539](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ConormalSequenceRight/Basic.lean#L539) (StacksFrontier): “the functorial second arrow”.

## Tag 0474, a lemma

[Tag 0474](https://stacks.math.columbia.edu/tag/0474) in the Stacks Project.

**`Stacks.ConormalSequenceSplit.isSplitEpi_differentialsMapOver_of_retraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalSequenceSplit/Basic.lean, line 175](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ConormalSequenceSplit/Basic.lean#L175). The attribute's comment: “a left inverse splits the second arrow”.

> **[Stacks, Tag 0474], a left inverse splits the second arrow.**  For an immersion
> `i : Z ⟶ X` of schemes over `S` admitting a left inverse `g : X ⟶ Z` over `S`, the second arrow
> `i^*Ω_{X/S} ⟶ Ω_{Z/S}` of the conormal sequence of [Stacks, Tag 01UZ] is a split epimorphism.
>
> Together with `Stacks.ConormalSequenceRight.differentialsMapOver_epi` this is the right-hand half
> of the source's conclusion. Split exactness of the three-term sequence, which this statement
> supplies the section for, is
> `Stacks.ConormalSequenceSplit.conormalShortComplexSplitting_of_retraction`.

```lean
theorem isSplitEpi_differentialsMapOver_of_retraction (i : Z ⟶ X) [IsImmersion i] (p : X ⟶ S)
    (g : X ⟶ Z) (hg : i ≫ g = 𝟙 Z) (hgS : g ≫ (i ≫ p) = p) :
    IsSplitEpi (relativeDifferentialsMap i p (i ≫ p) (𝟙 S) (by simp))
```

**`Stacks.ConormalSequenceSplit.forall_exists_isSplitEpi_restrict_of_localRetraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalSequenceSplit/Basic.lean, line 251](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ConormalSequenceSplit/Basic.lean#L251). The attribute's comment: “a local left inverse locally splits the second arrow”.

> **[Stacks, Tag 0474], a local left inverse locally splits the second arrow.**  Let
> `i : Z ⟶ X` be an immersion of schemes over `S` which *locally has a left inverse*: every point
> `z` of `Z` has an open neighbourhood `V` which `i` maps into an open `U` of `X`, the restricted
> morphism `j : V ⟶ U` admitting a left inverse `g : U ⟶ V` over `S`.  Then the second arrow
> `i^*Ω_{X/S} ⟶ Ω_{Z/S}` of the conormal sequence of [Stacks, Tag 01UZ] restricts to a split
> epimorphism on a neighbourhood of every point of `Z`.
>
> This is the "(locally)" reading of the source's hypothesis and conclusion, on the second arrow.
> Local split exactness of the three-term sequence is
> `Stacks.ConormalSequenceSplit.forall_exists_nonempty_splitting_restrict_of_localRetraction`,
> which combines this splitting with the short exactness
> `Stacks.ConormalSequenceSplit.conormalShortComplex_shortExact_of_localRetraction` proved under
> the same hypothesis.

```lean
theorem forall_exists_isSplitEpi_restrict_of_localRetraction
    (i : Z ⟶ X) [IsImmersion i] (p : X ⟶ S)
    (hloc : ∀ z : Z, ∃ (V : Z.Opens) (U : X.Opens) (j : V.toScheme ⟶ U.toScheme)
      (g : U.toScheme ⟶ V.toScheme), z ∈ V ∧ V.ι ≫ i = j ≫ U.ι ∧ j ≫ g = 𝟙 V.toScheme ∧
        g ≫ (V.ι ≫ i ≫ p) = U.ι ≫ p) :
    ∀ z : Z, ∃ V : Z.Opens, z ∈ V ∧
      IsSplitEpi ((Scheme.Modules.pullback V.ι).map
        (relativeDifferentialsMap i p (i ≫ p) (𝟙 S) (by simp)))
```

**`Stacks.ConormalSequenceSplit.conormalShortComplex_shortExact_of_localRetraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalSequenceSplit/ShortExact.lean, line 499](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ConormalSequenceSplit/ShortExact.lean#L499). The attribute's comment: “the local clause: under a local left inverse — every point of Z has a neighbourhood V mapping into an open U of X with the restricted morphism admitting a left inverse over S — the sequence 0 ⟶ 𝒞\_\{Z/X} ⟶ i^*Ω\_\{X/S} ⟶ Ω\_\{Z/S} ⟶ 0 of Tag 01UZ is short exact. This is exactness, globally; the local splitting under the same hypothesis is forall\_exists\_nonempty\_splitting\_restrict\_of\_localRetraction”.

> **[Stacks, Tag 0474], short exactness under a *local* left inverse.** Let `i : Z ⟶ X` be an
> immersion of schemes over `p : X ⟶ S` which *locally has a left inverse*: every point `z` of `Z`
> has an open neighbourhood `V` which `i` maps into an open `U` of `X`, the restricted morphism
> `j : V ⟶ U` admitting a left inverse `g : U ⟶ V` over `S`. Then the conormal sequence
> `0 ⟶ 𝒞_{Z/X} ⟶ i^*Ω_{X/S} ⟶ Ω_{Z/S} ⟶ 0` of [Stacks, Tag 01UZ] is short exact.
>
> This is the exactness half of the source's *locally split exact* under the source's local
> hypothesis, and it is global: being a monomorphism is a stalkwise condition, so a left inverse
> near each point is enough. The splitting half under the same hypothesis is
> `Stacks.ConormalSequenceSplit.forall_exists_isSplitEpi_restrict_of_localRetraction`, which
> splits the second arrow over a neighbourhood of every point; the two combine into the local
> split exactness
> `Stacks.ConormalSequenceSplit.forall_exists_nonempty_splitting_restrict_of_localRetraction`.

```lean
theorem conormalShortComplex_shortExact_of_localRetraction {Z X S : Scheme.{u}} (i : Z ⟶ X)
    [IsImmersion i] (p : X ⟶ S)
    (hloc : ∀ z : Z, ∃ (V : Z.Opens) (U : X.Opens) (j : V.toScheme ⟶ U.toScheme)
      (g : U.toScheme ⟶ V.toScheme), z ∈ V ∧ V.ι ≫ i = j ≫ U.ι ∧ j ≫ g = 𝟙 V.toScheme ∧
        g ≫ (V.ι ≫ i ≫ p) = U.ι ≫ p) :
    (conormalShortComplex i p).ShortExact
```

**`Stacks.ConormalSequenceSplit.conormalShortComplexSplitting_of_retraction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalSequenceSplit/ShortExact.lean, line 523](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ConormalSequenceSplit/ShortExact.lean#L523). The attribute's comment: “a left inverse over S splits the sequence 0 ⟶ 𝒞\_\{Z/X} ⟶ i^*Ω\_\{X/S} ⟶ Ω\_\{Z/S} ⟶ 0 of Tag 01UZ: a splitting is produced, so in particular the sequence is short exact. The hypothesis is a global left inverse g : X ⟶ Z with i ≫ g = 𝟙 Z and g ≫ (i ≫ p) = p; the source's parenthetical local clause is forall\_exists\_nonempty\_splitting\_restrict\_of\_localRetraction”.

> **[Stacks, Tag 0474], a left inverse splits the sequence.** For an immersion `i : Z ⟶ X` of
> schemes over `p : X ⟶ S` admitting a left inverse `g : X ⟶ Z` over `S`, the conormal sequence
> `0 ⟶ 𝒞_{Z/X} ⟶ i^*Ω_{X/S} ⟶ Ω_{Z/S} ⟶ 0` of [Stacks, Tag 01UZ] is *split* short exact: a
> splitting is produced, consisting of a retraction of the first arrow and a section of the second
> whose composites add up to the identity of `i^*Ω_{X/S}`.
>
> The section of the second arrow is the source's `i^*c_g`, through
> `Stacks.ConormalSequenceSplit.isSplitEpi_differentialsMapOver_of_retraction`; the sequence is
> short exact by `Stacks.ConormalSequenceSplit.conormalShortComplex_shortExact_of_retraction`, and
> a short exact sequence whose epimorphism has a section is split.

```lean
noncomputable def conormalShortComplexSplitting_of_retraction {Z X S : Scheme.{u}} (i : Z ⟶ X)
    [IsImmersion i] (p : X ⟶ S) (g : X ⟶ Z) (hg : i ≫ g = 𝟙 Z) (hgS : g ≫ (i ≫ p) = p) :
    (conormalShortComplex i p).Splitting
```

**`Stacks.ConormalSequenceSplit.forall_exists_nonempty_splitting_restrict_of_localRetraction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalSequenceSplit/ShortExact.lean, line 582](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ConormalSequenceSplit/ShortExact.lean#L582). The attribute's comment: “the parenthetical local clause: under a local left inverse — every point of Z has a neighbourhood V mapping into an open U of X with the restricted morphism j : V ⟶ U admitting a left inverse over S — the sequence 0 ⟶ 𝒞\_\{Z/X} ⟶ i^*Ω\_\{X/S} ⟶ Ω\_\{Z/S} ⟶ 0 of Tag 01UZ is *locally split exact*: every point of Z has an open neighbourhood V over which the restricted sequence carries a ShortComplex.Splitting, so both a retraction of the first arrow and a section of the second are produced over V. This is the full (locally) reading of the source's hypothesis and conclusion; the global reading is conormalShortComplexSplitting\_of\_retraction”. References: EGA IV (16.4.21), “special case”.

> **[Stacks, Tag 0474], a local left inverse makes the conormal sequence locally split
> exact.** Let `i : Z ⟶ X` be an immersion of schemes over `p : X ⟶ S` which *locally has a left
> inverse*: every point `z` of `Z` has an open neighbourhood `V` which `i` maps into an open `U` of
> `X`, the restricted morphism `j : V ⟶ U` admitting a left inverse `g : U ⟶ V` over `S`. Then
> every point of `Z` has an open neighbourhood `V` over which the conormal sequence
> `0 ⟶ 𝒞_{Z/X} ⟶ i^*Ω_{X/S} ⟶ Ω_{Z/S} ⟶ 0` of [Stacks, Tag 01UZ] is *split* short exact: the
> sequence restricted to `V` carries a `CategoryTheory.ShortComplex.Splitting`.
>
> This is the source's *(locally) split exact* under the source's *(locally) has a left inverse*.
> The neighbourhood produced is the one the hypothesis supplies, and the splitting over it is
> `Stacks.ConormalSequenceSplit.conormalShortComplexRestrictSplitting_of_localRetraction`.

```lean
theorem forall_exists_nonempty_splitting_restrict_of_localRetraction
    {Z X S : Scheme.{u}} (i : Z ⟶ X) [IsImmersion i] (p : X ⟶ S)
    (hloc : ∀ z : Z, ∃ (V : Z.Opens) (U : X.Opens) (j : V.toScheme ⟶ U.toScheme)
      (g : U.toScheme ⟶ V.toScheme), z ∈ V ∧ V.ι ≫ i = j ≫ U.ι ∧ j ≫ g = 𝟙 V.toScheme ∧
        g ≫ (V.ι ≫ i ≫ p) = U.ι ≫ p) :
    ∀ z : Z, ∃ V : Z.Opens, z ∈ V ∧
      Nonempty (((conormalShortComplex i p).map
        (Scheme.Modules.restrictFunctor V.ι)).Splitting)
```

**`Stacks.ConormalSequenceSplit.isIso_conormalDifferential_of_section`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalSequenceSplit/ShortExact.lean, line 606](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ConormalSequenceSplit/ShortExact.lean#L606). The attribute's comment: “the source's final assertion: for a section s of p, the first arrow 𝒞\_\{S/X} ⟶ s^*Ω\_\{X/S} of the sequence of Tag 01UZ, which is induced by d\_\{X/S}, is an isomorphism”. References: SGA 6 VIII (2.2), “(b)”.

> **[Stacks, Tag 0474], the conormal sheaf of a section.** For a section `s : S ⟶ X` of
> `p : X ⟶ S` the first arrow `𝒞_{S/X} ⟶ s^*Ω_{X/S}` of the conormal sequence of
> [Stacks, Tag 01UZ] is an isomorphism.
>
> A section is an immersion whose left inverse over `S` is `p` itself, so the sequence of `s` is
> short exact; and `Ω_{S/S}` is a zero object by [Stacks, Tag 01UY], `s ≫ p = 𝟙 S` being a
> monomorphism. The first arrow is therefore both a monomorphism and, the sequence being exact at
> the middle term with zero on the right, an epimorphism.

```lean
theorem isIso_conormalDifferential_of_section {X S : Scheme.{u}} (p : X ⟶ S) (s : S ⟶ X)
    (hs : s ≫ p = 𝟙 S) :
    haveI := isImmersion_of_section p s hs
    IsIso (conormalDifferential s p)
```

## Tag 060N, a remark

[Tag 060N](https://stacks.math.columbia.edu/tag/060N) in the Stacks Project.

**`Stacks.DiagonalSplitSequence.relativeDifferentialsIsoDiagonalConormal_hom_comp_conormalDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/DiagonalConormalSequence.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/DiagonalConormalSequence.lean#L133). The attribute's comment: “under the identification Ω\_\{X/S} ≅ 𝒞\_\{X/X ×\_S X} of Tag 08S2 (convention d = s₂ - s₁), the first arrow 𝒞\_\{X/X ×\_S X} ⟶ Δ^*Ω\_\{X ×\_S X/S} of the conormal sequence of the diagonal is (-1,1) into Ω\_\{X/S} ⊕ Ω\_\{X/S} = Δ^*Ω\_\{X ×\_S X/S}”.

> **[Stacks, Tag 060N]: under the identification of [Stacks, Tag 08S2] the left arrow is
> `(-1, 1)`.**  The first arrow `𝒞_{X/X ×_S X} ⟶ Δ^* Ω_{X ×_S X/S}` of the conormal sequence of
> the diagonal ([Stacks, Tag 01UZ]), precomposed with the isomorphism
> `Ω_{X/S} ≅ 𝒞_{X/X ×_S X}` of [Stacks, Tag 08S2] (which sends `d b` to the class of
> `p₂^♯ b - p₁^♯ b`, the convention `d = s₂ - s₁`), is the map `(-1, 1)` into
> `Δ^* Ω_{X ×_S X/S} = Ω_{X/S} ⊕ Ω_{X/S}`.
>
> Both sides are maps out of `Ω_{X/S}`, so it suffices to compare them on `d b`; the left side
> gives `Δ^* d_{X ×_S X/S}(p₂^♯ b - p₁^♯ b)` and the right side is computed by the footnote
> `Stacks.DiagonalSplitSequence.pullbackSection_d_diffSection`.

```lean
theorem relativeDifferentialsIsoDiagonalConormal_hom_comp_conormalDifferential :
    (Stacks.Tag08S2Assembly.relativeDifferentialsIsoDiagonalConormal f).hom ≫
        (Stacks.Conormal.DefiningIdealBridge.conormalSheafBridge (pullback.diagonal f)).inv ≫
          Stacks.ConormalSequenceRight.conormalDifferential (pullback.diagonal f)
            (pullback.fst f f ≫ f) =
      leftArrow f
```

**`Stacks.DiagonalSplitSequence.conormalShortComplex_diagonal_shortExact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/DiagonalConormalSequence.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/DiagonalConormalSequence.lean#L174). The attribute's comment: “the canonical short exact sequence 0 → 𝒞\_\{X/X ×\_S X} → Δ^*Ω\_\{X ×\_S X/S} → Ω\_\{X/S} → 0: the conormal sequence of the diagonal (Tag 01UZ) is short exact, by Tag 0474 for the left inverse pr₁ of Δ”.

> **[Stacks, Tag 060N]: the canonical short exact sequence.**  The conormal sequence
> `0 → 𝒞_{X/X ×_S X} → Δ^* Ω_{X ×_S X/S} → Ω_{X/S} → 0` of the diagonal
> ([Stacks, Tag 01UZ], with structure morphism `pr₁ ≫ f` of `X ×_S X` over `S`) is short exact: the
> diagonal is an immersion with the left inverse `pr₁` over `S`, so [Stacks, Tag 0474] applies.
> Through `Stacks.DiagonalSplitSequence.diagonalBiprodIso` the middle term is
> `Ω_{X/S} ⊕ Ω_{X/S}`; the arrows are identified by
> `Stacks.DiagonalSplitSequence.diagonalShortComplexIso`.

```lean
theorem conormalShortComplex_diagonal_shortExact :
    (Stacks.ConormalSequenceRight.conormalShortComplex (pullback.diagonal f)
      (pullback.fst f f ≫ f)).ShortExact
```

**`Stacks.DiagonalSplitSequence.diagonalShortComplexIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/DiagonalConormalSequence.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/DiagonalConormalSequence.lean#L231). The attribute's comment: “the canonical sequence 0 → 𝒞\_\{X/X ×\_S X} → Ω\_\{X/S} ⊕ Ω\_\{X/S} → Ω\_\{X/S} → 0, identified: an isomorphism of short complexes from Ω → Ω ⊕ Ω → Ω with arrows (-1,1), (1,1) to the conormal sequence of the diagonal, through Tag 08S2 on the left and Tag 01V1 in the middle”.

> **[Stacks, Tag 060N]: the canonical sequence, with its arrows identified.**  An
> isomorphism from the three-term complex
> `Ω_{X/S} → Ω_{X/S} ⊕ Ω_{X/S} → Ω_{X/S}` with arrows `(-1, 1)` and `(1, 1)`
> (`Stacks.DiagonalSplitSequence.shortComplex`) to the conormal sequence
> `𝒞_{X/X ×_S X} → Δ^* Ω_{X ×_S X/S} → Ω_{X/S}` of the diagonal.  Its components are the
> isomorphism `Ω_{X/S} ≅ 𝒞_{X/X ×_S X}` of [Stacks, Tag 08S2] (`d = s₂ - s₁`), the
> identification `Ω_{X/S} ⊕ Ω_{X/S} ≅ Δ^* Ω_{X ×_S X/S}` coming from [Stacks, Tag 01V1], and the
> identity of `Ω_{X/S}` (read through `Δ ≫ pr₁ ≫ f = f`).  Commutativity of the two squares says
> that the left arrow is `(-1, 1)` and the right arrow is `(1, 1)`.

```lean
noncomputable def diagonalShortComplexIso :
    shortComplex f ≅ Stacks.ConormalSequenceRight.conormalShortComplex (pullback.diagonal f)
      (pullback.fst f f ≫ f)
```

**`Stacks.DiagonalSplitSequence.diagonalBiprodIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/DiagonalSplitSequence.lean, line 341](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/DiagonalSplitSequence.lean#L341). The attribute's comment: “the middle term: Δ^*Ω\_\{X ×\_S X/S} = Ω\_\{X/S} ⊕ Ω\_\{X/S}”.

> **[Stacks, Tag 060N]: `Δ^* Ω_{X ×_S X/S} = Ω_{X/S} ⊕ Ω_{X/S}`.**  The direct sum
> decomposition `Ω_{X ×_S X/S} = pr_1^* Ω_{X/S} ⊕ pr_2^* Ω_{X/S}` of [Stacks, Tag 01V1], pulled
> back along the diagonal: the two summands become `Ω_{X/S}` because `Δ ≫ pr_i = id`.

```lean
noncomputable def diagonalBiprodIso :
    relativeDifferentials f ⊞ relativeDifferentials f ≅
      (Scheme.Modules.pullback (pullback.diagonal f)).obj
        (relativeDifferentials (pullback.fst f f ≫ f))
```

**`Stacks.DiagonalSplitSequence.diagonalBiprodIso_hom_comp_diagonalDifferentialsMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/DiagonalSplitSequence.lean, line 351](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/DiagonalSplitSequence.lean#L351). The attribute's comment: “the right arrow is (1,1)”.

> **[Stacks, Tag 060N]: the right arrow is `(1, 1)`.**  Under the identification
> `Δ^* Ω_{X ×_S X/S} = Ω_{X/S} ⊕ Ω_{X/S}` the canonical map `Δ^* Ω_{X ×_S X/S} ⟶ Ω_{X/S}` of
> [Stacks, Tag 01UV] — the second arrow of the conormal sequence of `Δ` — is `(1, 1)`.

```lean
theorem diagonalBiprodIso_hom_comp_diagonalDifferentialsMap :
    (diagonalBiprodIso f).hom ≫ diagonalDifferentialsMap f =
      biprod.desc (𝟙 (relativeDifferentials f)) (𝟙 (relativeDifferentials f))
```

**`Stacks.DiagonalSplitSequence.isSplitEpi_diagonalDifferentialsMap`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/DiagonalSplitSequence.lean, line 362](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/DiagonalSplitSequence.lean#L362). The attribute's comment: “the right arrow is a split surjection”.

> **[Stacks, Tag 060N]: the right arrow is a split surjection.**  The diagonal has the global
> left inverse `pr_1` over `S`, so the second arrow of its conormal sequence is a split
> epimorphism; this is [Stacks, Tag 0474] for `Δ`.

```lean
instance isSplitEpi_diagonalDifferentialsMap : IsSplitEpi (diagonalDifferentialsMap f)
```

**`Stacks.DiagonalSplitSequence.pullbackSection_d_diffSection`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/DiagonalSplitSequence.lean, line 466](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/DiagonalSplitSequence.lean#L466). The attribute's comment: “the footnote: the left arrow on sections”.

> **[Stacks, Tag 060N], the footnote.**  The local section `d_{X/S} b = p_2^♯ b - p_1^♯ b` of
> the ideal sheaf of the diagonal is carried by `d_{X ×_S X/S}`, pulled back along `Δ`, to
> `pr_2^* d_{X/S} b - pr_1^* d_{X/S} b`; that is, to the image of `d_{X/S} b` under the map
> `(-1, 1)` of the direct sum decomposition.  This is what fixes the sign of the left arrow.

```lean
theorem pullbackSection_d_diffSection (U : X.Opens) (b : Γ(X, U)) :
    Scheme.Modules.pullbackSection (pullback.diagonal f)
        (relativeDifferentials (pullback.fst f f ≫ f)) (Stacks.Diagonal.prodOpen f U) U
        (Stacks.Diagonal.le_diagonal_preimage_prodOpen f U)
        ((universalRelativeDerivation (pullback.fst f f ≫ f)).d
          (Stacks.Diagonal.diffSection f U b)) =
      ((leftArrow f).val.app (op U)) ((universalRelativeDerivation f).d b)
```

## Tag 067L, a lemma

[Tag 067L](https://stacks.math.columbia.edu/tag/067L) in the Stacks Project.

**`Stacks.ConormalSequenceTwoImmersions.epi_conormalDifferential`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/TwoImmersionsConormalExact.lean, line 79](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/TwoImmersionsConormalExact.lean#L79). The attribute's comment: “surjectivity of the second arrow 𝒞\_\{Z/X} ⟶ i^*Ω\_\{X/Y}, which is the ⟶ 0 at the right-hand end of the sequence”.

> **[Stacks, Tag 067L], surjectivity of the second arrow.** For immersions `i : Z ⟶ X` and
> `j : Z ⟶ Y` in a commutative triangle `i ≫ p = j`, the second arrow `𝒞_{Z/X} ⟶ i^*Ω_{X/Y}` of
> the conormal sequence is an epimorphism, which is the `⟶ 0` at its right-hand end.
>
> The sequence of [Stacks, Tag 01UZ] for `i` over `p` is exact at `i^*Ω_{X/Y}` and continues by
> `i^*Ω_{X/Y} ⟶ Ω_{Z/Y}`, whose target vanishes because `j` is an immersion, hence formally
> unramified.

```lean
theorem epi_conormalDifferential {Z X Y : Scheme.{u}} (i : Z ⟶ X) (j : Z ⟶ Y) (p : X ⟶ Y)
    [IsImmersion i] [IsImmersion j] (h : i ≫ p = j) :
    Epi (Stacks.ConormalSequenceRight.conormalDifferential i p)
```

**`Stacks.ConormalSequenceTwoImmersions.conormalTransitivityMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/TwoImmersionsConormalSequence.lean, line 112](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Morphisms/Differentials/TwoImmersionsConormalSequence.lean#L112). The attribute's comment: “the first arrow”.

> **[Stacks, Tag 067L], the first arrow.** For immersions `i : Z ⟶ X` and `j : Z ⟶ Y` in a
> commutative triangle `i ≫ p = j`, the canonical map `𝒞_{Z/Y} ⟶ 𝒞_{Z/X}` of conormal sheaves.
>
> It is the canonical map of [Stacks, Tag 01R4] for the square whose top morphism is `𝟙 Z`,
> transported along the identification of pullback along an identity with the identity
> functor.

```lean
def conormalTransitivityMap (h : i ≫ p = j) :
    Stacks.Conormal.conormalSheaf j ⟶ Stacks.Conormal.conormalSheaf i
```

**`Stacks.ConormalSequenceTwoImmersions.conormalDifferentialModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairSplitConormalSequence.lean, line 1166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairSplitConormalSequence.lean#L1166). The attribute's comment: “the second arrow 𝒞\_\{Z/X} ⟶ i^*Ω\_\{X/Y}, in the spelling that composes with the first arrow: the conormal differential of Tag 01UZ for i over p, read through the identification conormalSheafComparisonIso of the two presentations of 𝒞\_\{Z/X}”.

> **The second arrow `𝒞_{Z/X} ⟶ i^*Ω_{X/Y}` of [Stacks, Tag 067L]**, with its source in the
> spelling the first arrow uses. The conormal differential of [Stacks, Tag 01UZ] is built on the
> pullback of a *sectionwise* kernel and the first arrow on the pullback of the *categorical*
> kernel; `Stacks.ConormalSequenceUnramifiedPair.conormalSheafComparisonIso` identifies the two
> presentations, and this arrow is the conormal differential read through it.

```lean
def conormalDifferentialModules :
    immersionConormalSheafModules i ⟶
      (Scheme.Modules.pullback i).obj (Scheme.Hom.relativeDifferentials p)
```

**`Stacks.ConormalSequenceTwoImmersions.conormalTransitivityMapModules_comp_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairSplitConormalSequence.lean, line 1177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairSplitConormalSequence.lean#L1177). The attribute's comment: “the composite 𝒞\_\{Z/Y} ⟶ 𝒞\_\{Z/X} ⟶ i^*Ω\_\{X/Y} of the two arrows vanishes, so they form a complex; only the commutative triangle i ≫ p = j of immersions is assumed”.

> **[Stacks, Tag 067L]: the two arrows of the conormal sequence form a complex.** The composite
> `𝒞_{Z/Y} ⟶ 𝒞_{Z/X} ⟶ i^*Ω_{X/Y}` vanishes, for immersions `i : Z ⟶ X` and `j : Z ⟶ Y` in a
> commutative triangle `i ≫ p = j` and with no hypothesis on `p`.

```lean
theorem conormalTransitivityMapModules_comp_eq_zero (h : i ≫ p = j) :
    conormalTransitivityMapModules i j p h ≫ conormalDifferentialModules i p = 0
```

**`Stacks.ConormalSequenceTwoImmersions.conormalShortComplexModules_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairSplitConormalSequence.lean, line 1188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Thickenings/UnramifiedPairSplitConormalSequence.lean#L1188). The attribute's comment: “exactness at the middle term 𝒞\_\{Z/X}: the image of the first arrow 𝒞\_\{Z/Y} ⟶ 𝒞\_\{Z/X} is the kernel of the second arrow 𝒞\_\{Z/X} ⟶ i^*Ω\_\{X/Y}; only the commutative triangle i ≫ p = j of immersions is assumed”.

> **[Stacks, Tag 067L]: the conormal sequence of two immersions is exact at `𝒞_{Z/X}`.** The
> kernel of the second arrow `𝒞_{Z/X} ⟶ i^*Ω_{X/Y}` is exactly the image of the first arrow
> `𝒞_{Z/Y} ⟶ 𝒞_{Z/X}`, for immersions `i : Z ⟶ X` and `j : Z ⟶ Y` in a commutative triangle
> `i ≫ p = j` and with no hypothesis on `p`.

```lean
theorem conormalShortComplexModules_exact (h : i ≫ p = j) :
    (ShortComplex.mk _ _
      (conormalTransitivityMapModules_comp_eq_zero i j p h)).Exact
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.33, Tag 01UM](https://stacks.math.columbia.edu/tag/01UM)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
