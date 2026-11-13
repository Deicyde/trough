---
declaration: section
origin: cited
lean: Stacks.Conormal.conormalSheaf_isQuasicoherent, Stacks.Conormal.conormalSheaf, Stacks.Thickenings.immersionConormalSheaf, Stacks.Conormal.affineConormalIsoCotangent, Stacks.Conormal.pushforwardConormalIsoCotangent, Stacks.Conormal.pushforwardConormalIsoCotangent_apply, Stacks.Conormal.conormalSheafIsoPullbackIdealSheaf, Stacks.Conormal.conormalSheafIsoPullbackIdealSheaf_liftCoborder
statement: formalized
proof: formalized
---

# 29.32 Conormal sheaf of an immersion

Section 29.32 of the Stacks Project, [Tag 01R1](https://stacks.math.columbia.edu/tag/01R1). 5 tags here are carried by 28 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01R2, a definition

[Tag 01R2](https://stacks.math.columbia.edu/tag/01R2) in the Stacks Project.

**`Stacks.Conormal.conormalSheaf_isQuasicoherent`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalAlgebra/Sheaf.lean, line 57](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ConormalAlgebra/Sheaf.lean#L57). The attribute's comment: “quasi-coherence”.

> **Stacks Project, Tag 01R2.**  The conormal sheaf of an immersion is quasi-coherent.

```lean
instance conormalSheaf_isQuasicoherent {Z X : Scheme.{u}} (i : Z ⟶ X) [IsImmersion i] :
    (conormalSheaf i).IsQuasicoherent
```

**`Stacks.Conormal.conormalSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalComparison/IdealSheafComparison.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ConormalComparison/IdealSheafComparison.lean#L141). The attribute's comment: “construction”.

> **[Stacks, Tag 01R2].** The conormal sheaf of an immersion: the module pullback, along the
> canonical closed immersion `i.liftCoborder` into the coborder neighbourhood of the image, of the
> ideal sheaf of that closed immersion.
>
> Keeping it an abbreviation is deliberate: [Stacks, Tag 01R3]'s normalization clause compares an
> isomorphism of this object with `Iso.refl`, which requires the two sides to have the same
> type without a transport.
>
> Quasi-coherence, the other half of the assertion of [Stacks, Tag 01R2], is
> `Stacks.Conormal.conormalSheaf_isQuasicoherent`.

```lean
noncomputable abbrev conormalSheaf {Z X : Scheme.{u}} (i : Z ⟶ X) [IsImmersion i] :
    SheafOfModules.{u} (structureSheafRing Z.toLocallyRingedSpace.toRingedSpace)
```

**`Stacks.Thickenings.immersionConormalSheaf`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Thickenings/UniversalConormalSheaf.lean, line 128](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Thickenings/UniversalConormalSheaf.lean#L128). The attribute's comment: “construction”. References: SGA 3 I (6.8.5); SGA 3 III (4.5.0); SGA 6 VII (1.6).

> **Stacks Project, Tag 01R2.** The conormal sheaf `𝒞_{Z/X} = I/I²` of an immersion
> `i : Z ⟶ X` of schemes: the pullback along the closed immersion
> `AlgebraicGeometry.Scheme.Hom.liftCoborder` of `i` into the canonical open neighbourhood
> `AlgebraicGeometry.Scheme.Hom.coborderRange` of its image of the defining ideal sheaf of that
> closed immersion.
>
> By [Stacks Project, Tag 01R3] part (1) this pullback *is* the conormal sheaf: its pushforward
> along the closed immersion is `I/I²`. Only the construction is provided; the quasi-coherence
> asserted by [Stacks Project, Tag 01R2] is not proved here.
>
> This is the same construction as `Stacks.Conormal.conormalSheaf`, and is defined as that
> declaration: `schemeConormalSheaf i.liftCoborder` unfolds, by two abbreviations, to its body.

```lean
noncomputable abbrev immersionConormalSheaf {Z X : Scheme.{u}} (i : Z ⟶ X) [IsImmersion i] :
    SheafOfModules.{u} (structureSheafRing Z.toLocallyRingedSpace.toRingedSpace)
```

## Tag 01R3, a lemma

[Tag 01R3](https://stacks.math.columbia.edu/tag/01R3) in the Stacks Project.

**`Stacks.Conormal.affineConormalIsoCotangent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalAlgebra/AffineIdentification.lean, line 475](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ConormalAlgebra/AffineIdentification.lean#L475). The attribute's comment: “part (2): affine conormal sections”.

> **The affine computation of the conormal sheaf.**  Let `i : Z ⟶ X` be an immersion and
> `U ⊆ X` an affine open with `Z ∩ U = Spec (Γ(X, U) ⧸ I)` over `U`.  Then the sections of the
> conormal sheaf of `i` over `Z ∩ U` are canonically `I/I²`, which is the assertion of
> [Stacks, Tag 01R3] (2).
>
> The conormal sheaf is [Stacks, Tag 01R2]'s, written out: the pullback along
> `i.liftCoborder : Z ⟶ i.coborderRange` of the ideal sheaf of that closed immersion.  Its
> sections over `Z ∩ U` are presented as the sections over `U` of its pushforward along `i`, so
> that the module is one of `Γ(X, U)`-modules, as `I.Cotangent` is.

```lean
def affineConormalIsoCotangent {Z X : Scheme.{u}} (i : Z ⟶ X) [IsImmersion i]
    (U : X.Opens) (hU : IsAffineOpen U) (I : Ideal Γ(X, U))
    (e : pullback i U.ι ≅ Spec (.of (Γ(X, U) ⧸ I)))
    (he : pullback.snd i U.ι ≫ hU.isoSpec.hom =
      e.hom ≫ Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I))) :
    ((modulePushforward i.toLRSHom.toShHom).obj
        ((modulePullback i.liftCoborder.toLRSHom.toShHom).obj
          (Stacks.ClosedImmersion.idealSheaf i.liftCoborder.toLRSHom.toShHom))).val.obj (op U)
      ≅ ModuleCat.of Γ(X, U) I.Cotangent
```

**`Stacks.Conormal.pushforwardConormalIsoCotangent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalAlgebra/Factorization.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ConormalAlgebra/Factorization.lean#L157). The attribute's comment: “part (1): pushforward is the ideal modulo its square”.

> **[Stacks, Tag 01R3] (1), the affine form of `i'_* 𝒞_{Z/X} = ℐ/ℐ²`.**  Let `i : Z ⟶ X` be an
> immersion factored as a closed immersion `i' : Z ⟶ U` into an open subscheme, let `V ⊆ U` be an
> affine open, and suppose `Z ∩ V = Spec (Γ(U, V) ⧸ I)` over `V`.  Then the sections over `V` of
> the direct image along `i'` of the conormal sheaf are canonically `I/I²`.
>
> Part (1) identifies the conormal sheaf with `(i')^* ℐ`, after which this is
> `Stacks.Conormal.affineIdealPullbackIsoCotangent` for the closed immersion `i'` — the
> ring-theoretic content `I ⊗_R R/I = I/I²` — with the kernel of the map on sections identified
> with `I` by the affine model.

```lean
noncomputable def pushforwardConormalIsoCotangent {Z X : Scheme.{u}} (i : Z ⟶ X)
    [IsImmersion i] (U : X.Opens) (i' : Z ⟶ U.toScheme) [IsClosedImmersion i']
    (hfac : i' ≫ U.ι = i) (V : U.toScheme.Opens) (hV : IsAffineOpen V)
    (I : Ideal Γ(U.toScheme, V))
    (e : CategoryTheory.Limits.pullback i' V.ι ≅ Spec (.of (Γ(U.toScheme, V) ⧸ I)))
    (he : CategoryTheory.Limits.pullback.snd i' V.ι ≫ hV.isoSpec.hom =
      e.hom ≫ Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I))) :
    ((modulePushforward i'.toLRSHom.toShHom).obj (conormalSheaf i)).val.obj (op V) ≅
      ModuleCat.of Γ(U.toScheme, V) I.Cotangent
```

**`Stacks.Conormal.pushforwardConormalIsoCotangent_apply`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalAlgebra/Factorization.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ConormalAlgebra/Factorization.lean#L178). The attribute's comment: “part (1): canonical affine quotient formula”.

> **[Stacks, Tag 01R3] (1), the normalization of the affine form of `i'_* 𝒞_{Z/X} = ℐ/ℐ²`.**
> The isomorphism sends the canonical quotient of a section of the ideal sheaf to the class of
> that section modulo `I²`.  Since `Ideal.toCotangent` is surjective this determines the
> isomorphism, so it is the canonical one and not merely some isomorphism of the right type.

```lean
theorem pushforwardConormalIsoCotangent_apply {Z X : Scheme.{u}} (i : Z ⟶ X)
    [IsImmersion i] (U : X.Opens) (i' : Z ⟶ U.toScheme) [IsClosedImmersion i']
    (hfac : i' ≫ U.ι = i) (V : U.toScheme.Opens) (hV : IsAffineOpen V)
    (I : Ideal Γ(U.toScheme, V))
    (e : CategoryTheory.Limits.pullback i' V.ι ≅ Spec (.of (Γ(U.toScheme, V) ⧸ I)))
    (he : CategoryTheory.Limits.pullback.snd i' V.ι ≫ hV.isoSpec.hom =
      e.hom ≫ Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I)))
    (x : (Stacks.ClosedImmersion.idealSheaf i'.toLRSHom.toShHom).val.obj (op V))
    (hx : (kernel.ι (SheafOfModules.unitToPushforwardObjUnit
      (structureSheafHom i'.toLRSHom.toShHom))).val.app (op V) x ∈ I) :
    (pushforwardConormalIsoCotangent i U i' hfac V hV I e he).hom.hom
        ((conormalQuotientMap i U i' hfac).val.app (op V) x) =
      I.toCotangent ⟨(kernel.ι (SheafOfModules.unitToPushforwardObjUnit
        (structureSheafHom i'.toLRSHom.toShHom))).val.app (op V) x, hx⟩
```

**`Stacks.Conormal.conormalSheafIsoPullbackIdealSheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalComparison/IdealSheafComparison.lean, line 187](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ConormalComparison/IdealSheafComparison.lean#L187). The attribute's comment: “part (1): pullback of the ideal sheaf”.

> **[Stacks, Tag 01R3], part (1).** The conormal sheaf of an immersion `i : Z ⟶ X` is the
> module pullback of the ideal sheaf of *any* factorization of `i` as a closed immersion into
> an open subscheme followed by the inclusion of that open subscheme.
>
> The given open `U` is contained in `i.coborderRange` by
> `Stacks.Conormal.le_coborderRange_of_comp_eq`, and the factorizing morphism followed by the
> induced open immersion is `i.liftCoborder` by
> `Stacks.Conormal.comp_homOfLE_eq_liftCoborder`. So this is
> `pullbackIdealSheafIsoOfCompEq` for that open immersion.

```lean
noncomputable def conormalSheafIsoPullbackIdealSheaf {Z X : Scheme.{u}} (i : Z ⟶ X)
    [IsImmersion i] (U : X.Opens) (i' : Z ⟶ U.toScheme) [IsClosedImmersion i']
    (hfac : i' ≫ U.ι = i) :
    conormalSheaf i ≅
      (modulePullback i'.toLRSHom.toShHom).obj
        (Stacks.ClosedImmersion.idealSheaf i'.toLRSHom.toShHom)
```

**`Stacks.Conormal.conormalSheafIsoPullbackIdealSheaf_liftCoborder`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalComparison/Normalization.lean, line 272](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ConormalComparison/Normalization.lean#L272). The attribute's comment: “part (1): canonical normalization”.

> **[Stacks, Tag 01R3], part (1): canonical normalization.**

```lean
theorem conormalSheafIsoPullbackIdealSheaf_liftCoborder {Z X : Scheme.{u}} (i : Z ⟶ X)
    [IsImmersion i] :
    conormalSheafIsoPullbackIdealSheaf i i.coborderRange i.liftCoborder i.liftCoborder_ι =
      Iso.refl (conormalSheaf i)
```

**`Stacks.Conormal.OpenFactorizations.conormalQuotientMap_restrict_factorization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ConormalOpenFactorizations/Compatibility.lean, line 297](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/ConormalOpenFactorizations/Compatibility.lean#L297). The attribute's comment: “part (1): compatibility of open factorizations”.

> **[Stacks, Tag 01R3], part (1): compatibility of open factorizations.** The quotient
> identifications from two open factorizations agree on common conormal sections: images of the
> same ambient ideal generator agree after restriction to any common source open.
>
> This is `generator_eq_of_two_factorizations` at `r = (a : Γ(X, V))`. The presentation data
> `hV`, `I`, `e`, `he` is carried because the tagged statement carries it; the proof does not use it,
> and the
> statement proved is the stronger one with `a : I` replaced by an arbitrary `r : Γ(X, V)` and the
> presentation dropped altogether.

```lean
theorem conormalQuotientMap_restrict_factorization {Z X : Scheme.{u}} (i : Z ⟶ X) [IsImmersion i]
    (V : X.Opens) (hV : IsAffineOpen V)
    (I : Ideal Γ(X, V))
    (e : Limits.pullback i V.ι ≅ Spec (.of (Γ(X, V) ⧸ I)))
    (he : Limits.pullback.snd i V.ι ≫ hV.isoSpec.hom =
      e.hom ≫ Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I)))
    (U₁ U₂ : X.Opens)
    (i₁ : Z ⟶ U₁.toScheme) [IsClosedImmersion i₁]
    (i₂ : Z ⟶ U₂.toScheme) [IsClosedImmersion i₂]
    (hfac₁ : i₁ ≫ U₁.ι = i) (hfac₂ : i₂ ≫ U₂.ι = i)
    (W₁ : U₁.toScheme.Opens) (hW₁ : W₁ ≤ U₁.ι ⁻¹ᵁ V)
    (W₂ : U₂.toScheme.Opens) (hW₂ : W₂ ≤ U₂.ι ⁻¹ᵁ V)
    (a : I)
    (x₁ : (Stacks.ClosedImmersion.idealSheaf i₁.toLRSHom.toShHom).val.obj (.op W₁))
    (x₂ : (Stacks.ClosedImmersion.idealSheaf i₂.toLRSHom.toShHom).val.obj (.op W₂))
    (hx₁ : (U₁.ι.appLE V W₁ hW₁).hom (a : Γ(X, V)) =
      (kernel.ι (SheafOfModules.unitToPushforwardObjUnit
        (structureSheafHom i₁.toLRSHom.toShHom))).val.app (.op W₁) x₁)
    (hx₂ : (U₂.ι.appLE V W₂ hW₂).hom (a : Γ(X, V)) =
      (kernel.ι (SheafOfModules.unitToPushforwardObjUnit
        (structureSheafHom i₂.toLRSHom.toShHom))).val.app (.op W₂) x₂)
    (T : Z.Opens) (hT₁ : T ≤ i₁ ⁻¹ᵁ W₁) (hT₂ : T ≤ i₂ ⁻¹ᵁ W₂) :
    (conormalSheaf i).val.map (homOfLE hT₁).op
        ((conormalQuotientMap i U₁ i₁ hfac₁).val.app (.op W₁) x₁) =
      (conormalSheaf i).val.map (homOfLE hT₂).op
        ((conormalQuotientMap i U₂ i₂ hfac₂).val.app (.op W₂) x₂)
```

**`Stacks.Conormal.Tag01R3Generators.conormalQuotientMap_epi`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Generators/Epi.lean, line 138](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Generators/Epi.lean#L138). The attribute's comment: “part (1): sheaf quotient map is epimorphic”.

> **[Stacks, Tag 01R3], part (1): the ideal sheaf surjects onto the pushforward conormal
> sheaf.** For an immersion `i : Z ⟶ X` and any closed-immersion factorization `i' : Z ⟶ U`,
> `Stacks.Conormal.conormalQuotientMap` is an epimorphism of sheaves of modules.
>
> `Stacks.SheafOfModules.EpiMono.epi_of_isLocallySurjective` at
> `isLocallySurjective_conormalQuotientMap`. No affineness, Noetherian or finiteness hypothesis is
> used, and `Stacks.Conormal.epi_conormalQuotientMap_iff`'s named blocker — epimorphy of the
> adjunction unit — is bypassed rather than proved; see the module docstring.

```lean
theorem conormalQuotientMap_epi {Z X : Scheme.{u}} (i : Z ⟶ X) [IsImmersion i]
    (U : X.Opens) (i' : Z ⟶ U.toScheme) [IsClosedImmersion i'] (hfac : i' ≫ U.ι = i) :
    Epi (Stacks.Conormal.conormalQuotientMap i U i' hfac)
```

**`Stacks.Conormal.Tag01R3Generators.conormalQuotientMap_kernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Generators/Kernel.lean, line 132](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Generators/Kernel.lean#L132). The attribute's comment: “part (1): quotient by the ideal square”.

> **[Stacks, Tag 01R3], part (1): the quotient is by the square of the ideal.** On an affine
> open `V` of a closed-immersion factorization `i' : Z ⟶ U` of an immersion `i : Z ⟶ X`, a section
> `x` of the ideal sheaf of `i'` over `V` is killed by `Stacks.Conormal.conormalQuotientMap`
> exactly when its image in the structure sheaf lies in `(i'.ker.ideal ⟨V, hV⟩) ^ 2`.
>
> The statement involves no presentation data; one is produced inside the proof by
> `Stacks.DiagonalPresentation.exists_presentation` and its ideal identified with
> `i'.ker.ideal ⟨V, hV⟩` by `presentationIdeal_eq_ker_app`. The vanishing is then transported
> across `Stacks.Conormal.pushforwardConormalIsoCotangent` by
> `Stacks.Conormal.pushforwardConormalIsoCotangent_apply` and read off by
> `Ideal.toCotangent_eq_zero`.

```lean
theorem conormalQuotientMap_kernel {Z X : Scheme.{u}} (i : Z ⟶ X) [IsImmersion i]
    (U : X.Opens) (i' : Z ⟶ U.toScheme) [IsClosedImmersion i'] (hfac : i' ≫ U.ι = i)
    (V : U.toScheme.Opens) (hV : IsAffineOpen V)
    (x : (Stacks.ClosedImmersion.idealSheaf i'.toLRSHom.toShHom).val.obj (.op V)) :
    (Stacks.Conormal.conormalQuotientMap i U i' hfac).val.app (.op V) x = 0 ↔
      (kernel.ι (SheafOfModules.unitToPushforwardObjUnit
        (structureSheafHom i'.toLRSHom.toShHom))).val.app (.op V) x ∈
          (i'.ker.ideal ⟨V, hV⟩) ^ 2
```

**`Stacks.Tag01R3PartTwo.affineConormalIsoCotangent_inv_toCotangent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PartTwo/Generators.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PartTwo/Generators.lean#L92). The attribute's comment: “part (2): canonical affine generators”.

> **[Stacks, Tag 01R3], part (2): canonical affine generators.** The inverse affine
> identification sends the class of an ideal section to its canonical conormal quotient, on every
> open of every closed-immersion factorization, after restricting the ambient section.
>
> The formula is proved at the coborder factorization by
> `conormalAffineSectionsIsoCotangent_toCotangent` and moved to `(U, i')` by the compatibility
> `Stacks.Conormal.OpenFactorizations.generator_eq_of_two_factorizations`, at the common source
> open `i' ⁻¹ᵁ W`. The section of the coborder ideal sheaf that the comparison needs is produced by
> `exists_coborderSection` from the presentation alone.

```lean
theorem affineConormalIsoCotangent_inv_toCotangent {Z X : Scheme.{u}} (i : Z ⟶ X) [IsImmersion i]
    (V : X.Opens) (hV : IsAffineOpen V) (I : Ideal Γ(X, V))
    (e : Limits.pullback i V.ι ≅ Spec (.of (Γ(X, V) ⧸ I)))
    (he : Limits.pullback.snd i V.ι ≫ hV.isoSpec.hom =
      e.hom ≫ Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I)))
    (U : X.Opens) (i' : Z ⟶ U.toScheme) [IsClosedImmersion i']
    (hfac : i' ≫ U.ι = i)
    (W : U.toScheme.Opens) (hW : W ≤ U.ι ⁻¹ᵁ V)
    (a : I)
    (x : (Stacks.ClosedImmersion.idealSheaf i'.toLRSHom.toShHom).val.obj (.op W))
    (hx : (U.ι.appLE V W hW).hom (a : Γ(X, V)) =
      (kernel.ι (SheafOfModules.unitToPushforwardObjUnit
        (structureSheafHom i'.toLRSHom.toShHom))).val.app (.op W) x) :
    (Stacks.Conormal.conormalSheaf i).val.map
        (homOfLE (show i' ⁻¹ᵁ W ≤ i ⁻¹ᵁ V from by
          rw [← hfac]; exact i'.preimage_mono hW)).op
        ((Stacks.Conormal.affineConormalIsoCotangent i V hV I e he).inv.hom
          (I.toCotangent a)) =
      (Stacks.Conormal.conormalQuotientMap i U i' hfac).val.app (.op W) x
```

**`Stacks.Tag01R3PartTwo.affineConormalIsoCotangentWithQuotient`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PartTwo/Generators.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PartTwo/Generators.lean#L137). The attribute's comment: “part (2): affine identification with canonical quotient generators”.

> **[Stacks, Tag 01R3], part (2): the affine identification with canonical quotient
> generators.** The sections over an affine open `V` of the ambient scheme of the direct image of
> the conormal sheaf are `I.Cotangent`, *together with* the formula on ideal generators for every
> closed-immersion factorization and every open of it.
>
> The isomorphism is `Stacks.Conormal.affineConormalIsoCotangent` and the second component is
> `affineConormalIsoCotangent_inv_toCotangent`.

```lean
noncomputable def affineConormalIsoCotangentWithQuotient {Z X : Scheme.{u}} (i : Z ⟶ X)
    [IsImmersion i] (V : X.Opens) (hV : IsAffineOpen V) (I : Ideal Γ(X, V))
    (e : Limits.pullback i V.ι ≅ Spec (.of (Γ(X, V) ⧸ I)))
    (he : Limits.pullback.snd i V.ι ≫ hV.isoSpec.hom =
      e.hom ≫ Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I))) :
    { c : ((modulePushforward i.toLRSHom.toShHom).obj
        (Stacks.Conormal.conormalSheaf i)).val.obj (.op V) ≅
          ModuleCat.of Γ(X, V) I.Cotangent //
      ∀ (U : X.Opens) (i' : Z ⟶ U.toScheme) [IsClosedImmersion i']
        (hfac : i' ≫ U.ι = i)
        (W : U.toScheme.Opens) (hW : W ≤ U.ι ⁻¹ᵁ V)
        (a : I)
        (x : (Stacks.ClosedImmersion.idealSheaf i'.toLRSHom.toShHom).val.obj (.op W)),
        (U.ι.appLE V W hW).hom (a : Γ(X, V)) =
          (kernel.ι (SheafOfModules.unitToPushforwardObjUnit
            (structureSheafHom i'.toLRSHom.toShHom))).val.app (.op W) x →
        (Stacks.Conormal.conormalSheaf i).val.map
          (homOfLE (show i' ⁻¹ᵁ W ≤ i ⁻¹ᵁ V from by
            rw [← hfac]; exact i'.preimage_mono hW)).op
          (c.inv.hom (I.toCotangent a)) =
            (Stacks.Conormal.conormalQuotientMap i U i' hfac).val.app (.op W) x }
```

**`Stacks.Tag01R3PartTwo.affineConormalIsoCotangent_inv_toCotangent_liftCoborder`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PartTwo/Generators.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PartTwo/Generators.lean#L170). The attribute's comment: “part (2): defining adjunction-unit generators”.

> **[Stacks, Tag 01R3], part (2): defining adjunction-unit generators.** On the defining
> factorization the affine generator is the image under the defining adjunction unit itself.
>
> This is `affineConormalIsoCotangent_inv_toCotangent` at `(i.coborderRange, i.liftCoborder)`,
> with `Stacks.Conormal.OpenFactorizations.conormalQuotientMap_liftCoborder` — the normalization
> `Stacks.Conormal.conormalSheafIsoPullbackIdealSheaf_liftCoborder` read on the quotient map —
> replacing the quotient map by the unit.

```lean
theorem affineConormalIsoCotangent_inv_toCotangent_liftCoborder {Z X : Scheme.{u}} (i : Z ⟶ X)
    [IsImmersion i] (V : X.Opens) (hV : IsAffineOpen V) (I : Ideal Γ(X, V))
    (e : Limits.pullback i V.ι ≅ Spec (.of (Γ(X, V) ⧸ I)))
    (he : Limits.pullback.snd i V.ι ≫ hV.isoSpec.hom =
      e.hom ≫ Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I)))
    (W : i.coborderRange.toScheme.Opens) (hW : W ≤ i.coborderRange.ι ⁻¹ᵁ V)
    (a : I)
    (x : (Stacks.ClosedImmersion.idealSheaf i.liftCoborder.toLRSHom.toShHom).val.obj (.op W))
    (hx : (i.coborderRange.ι.appLE V W hW).hom (a : Γ(X, V)) =
      (kernel.ι (SheafOfModules.unitToPushforwardObjUnit
        (structureSheafHom i.liftCoborder.toLRSHom.toShHom))).val.app (.op W) x) :
    (Stacks.Conormal.conormalSheaf i).val.map
        (homOfLE (show i.liftCoborder ⁻¹ᵁ W ≤ i ⁻¹ᵁ V from
          (i.liftCoborder.preimage_mono hW).trans_eq
            (congrArg (fun f : Z ⟶ X ↦ f ⁻¹ᵁ V) i.liftCoborder_ι))).op
        ((Stacks.Conormal.affineConormalIsoCotangent i V hV I e he).inv.hom
          (I.toCotangent a)) =
      ((modulePullbackPushforwardAdjunction i.liftCoborder.toLRSHom.toShHom).unit.app
        (Stacks.ClosedImmersion.idealSheaf i.liftCoborder.toLRSHom.toShHom)).val.app (.op W) x
```

**`Stacks.Tag01R3PartTwo.affineConormalIsoCotangent_restrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/PartTwo/Restrict.lean, line 72](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/PartTwo/Restrict.lean#L72). The attribute's comment: “part (2): compatibility with restriction”.

> **[Stacks, Tag 01R3], part (2): compatibility with restriction.** The affine identifications
> commute with restriction: the class of an ideal section restricts to the class of its
> restriction.
>
> This is the generator-level naturality needed to use the affine formula to characterize
> morphisms of conormal sheaves. See the module docstring for the route; the point is that
> `affineConormalIsoCotangent_inv_toCotangent` is available at the coborder factorization over the
> *smaller* open, so one section of the coborder ideal sheaf serves both presentations.

```lean
theorem affineConormalIsoCotangent_restrict {Z X : Scheme.{u}} (i : Z ⟶ X) [IsImmersion i]
    (U V : X.Opens) (hVU : V ≤ U) (hU : IsAffineOpen U) (hV : IsAffineOpen V)
    (I : Ideal Γ(X, U)) (J : Ideal Γ(X, V))
    (eU : Limits.pullback i U.ι ≅ Spec (.of (Γ(X, U) ⧸ I)))
    (heU : Limits.pullback.snd i U.ι ≫ hU.isoSpec.hom =
      eU.hom ≫ Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk I)))
    (eV : Limits.pullback i V.ι ≅ Spec (.of (Γ(X, V) ⧸ J)))
    (heV : Limits.pullback.snd i V.ι ≫ hV.isoSpec.hom =
      eV.hom ≫ Spec.map (CommRingCat.ofHom (Ideal.Quotient.mk J)))
    (x : I)
    (hx : (X.presheaf.map (homOfLE hVU).op).hom (x : Γ(X, U)) ∈ J) :
    (Stacks.Conormal.affineConormalIsoCotangent i V hV J eV heV).hom.hom
      (((modulePushforward i.toLRSHom.toShHom).obj
        (Stacks.Conormal.conormalSheaf i)).val.map (homOfLE hVU).op
          ((Stacks.Conormal.affineConormalIsoCotangent i U hU I eU heU).inv.hom
            (I.toCotangent x))) =
      J.toCotangent
        ⟨(X.presheaf.map (homOfLE hVU).op).hom (x : Γ(X, U)), hx⟩
```

## Tag 01R4, a lemma

[Tag 01R4](https://stacks.math.columbia.edu/tag/01R4) in the Stacks Project.

**`Stacks.Immersion.immersionConormalSheafMap_ideal_mem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Conormal/SquareMap.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Conormal/SquareMap.lean#L180). The attribute's comment: “affine ideal containment”.

> **[Stacks Project, Tag 01R4]: the ambient ring map carries the target ideal into the source
> ideal.** On a pair of affine opens `U ⊆ X` and `V ⊆ X'` with `g(U) ⊆ V` presenting the
> scheme-theoretic intersections as `Spec (Γ(X, U) ⧸ I)` and `Spec (Γ(X', V) ⧸ J)`, the map
> `g^♯ : Γ(X', V) ⟶ Γ(X, U)` sends `J` into `I`.
>
> This is what lets the affine characterisation speak of the class in `I/I²` of the image of a
> class in `J/J²`.

```lean
theorem immersionConormalSheafMap_ideal_mem (i : Z ⟶ X) (i' : Z' ⟶ X')
    [IsImmersion i] [IsImmersion i'] (f : Z ⟶ Z') (g : X ⟶ X') (comm : i ≫ g = f ≫ i')
    (U : X.Opens) (hU : IsAffineOpen U) (V : X'.Opens) (hV : IsAffineOpen V)
    (hUV : U ≤ g ⁻¹ᵁ V) (I : Ideal Γ(X, U)) (J : Ideal Γ(X', V))
    (eZ : pullback i U.ι ≅ Spec (quotRing I))
    (heZ : pullback.snd i U.ι ≫ hU.isoSpec.hom = eZ.hom ≫ quotImmersion Γ(X, U) I)
    (eZ' : pullback i' V.ι ≅ Spec (quotRing J))
    (heZ' : pullback.snd i' V.ι ≫ hV.isoSpec.hom = eZ'.hom ≫ quotImmersion Γ(X', V) J)
    (a : J) : (g.appLE V U hUV).hom (a : Γ(X', V)) ∈ I
```

**`Stacks.Immersion.immersionConormalSheafMap_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Conormal/SquareMap.lean, line 321](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Conormal/SquareMap.lean#L321). The attribute's comment: “uniqueness”.

> **[Stacks Project, Tag 01R4]: the affine formula determines the map.** A morphism
> `f^* 𝒞_{Z'/X'} ⟶ 𝒞_{Z/X}` satisfying the affine characterisation is
> `Stacks.Immersion.immersionConormalSheafMap`.
>
> Transposing along `f^* ⊣ f_*` and testing on the basis of `Z'` given by the opens `i' ⁻¹ᵁ V` for
> affine `V ⊆ X'` inside `i'.coborderRange` reduces this to
> `Stacks.Immersion.transpose_eq_of_coborder_affine`.

```lean
theorem immersionConormalSheafMap_unique (i : Z ⟶ X) (i' : Z' ⟶ X')
    [IsImmersion i] [IsImmersion i'] (f : Z ⟶ Z') (g : X ⟶ X') (comm : i ≫ g = f ≫ i')
    (φ : (modulePullback f.toLRSHom.toShHom).obj
        (conormalSheaf i'.liftCoborder.toLRSHom.toShHom) ⟶
      conormalSheaf i.liftCoborder.toLRSHom.toShHom)
    (hφ : IsInducedConormalSheafMap i i' f g comm φ) :
    φ = immersionConormalSheafMap i i' f g (toShHom_square comm)
```

Declarations registered for the tag:

- [`Stacks.Immersion.immersionConormalSheafMap`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Thickenings/UniversalConormalGenerators.lean#L257), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Conormal/SquareMap.lean, line 618](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Conormal/SquareMap.lean#L618) (StacksFrontier): “canonical map”.
- [`Stacks.Immersion.isInducedConormalSheafMap_immersionConormalSheafMap`](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Thickenings/UniversalConormalGenerators.lean#L354), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Conormal/SquareMap.lean, line 620](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Conormal/SquareMap.lean#L620) (StacksFrontier): “affine formula”.

## Tag 0473, a lemma

[Tag 0473](https://stacks.math.columbia.edu/tag/0473) in the Stacks Project.

**`Stacks.Immersion.epi_immersionConormalSheafMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Conormal/SquareEpi.lean, line 310](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Conormal/SquareEpi.lean#L310). The attribute's comment: “surjectivity”.

> For a cartesian square of schemes whose horizontal maps `i` and `i'` are immersions, the
> canonical map `f^* 𝒞_{Z'/X'} ⟶ 𝒞_{Z/X}` of conormal sheaves is an epimorphism.

```lean
theorem epi_immersionConormalSheafMap (i : Z ⟶ X) (i' : Z' ⟶ X') [IsImmersion i] [IsImmersion i']
    (f : Z ⟶ Z') (g : X ⟶ X') (sq : IsPullback i f g i') :
    Epi (immersionConormalSheafMap i i' f g (toShHom_square sq.w))
```

**`Stacks.Immersion.isIso_immersionConormalSheafMap_of_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Conormal/SquareFlatIso.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Conormal/SquareFlatIso.lean#L254). The attribute's comment: “flat base change”.

> For a cartesian square of schemes whose horizontal maps `i` and `i'` are immersions and
> whose ambient vertical map `g` is flat, the canonical map `f^* 𝒞_{Z'/X'} ⟶ 𝒞_{Z/X}` of
> [Stacks Project, Tag 01R4] is an isomorphism.

```lean
theorem isIso_immersionConormalSheafMap_of_flat (i : Z ⟶ X) (i' : Z' ⟶ X')
    [IsImmersion i] [IsImmersion i']
    (f : Z ⟶ Z') (g : X ⟶ X') [Flat g] (sq : IsPullback i f g i') :
    IsIso (Stacks.Immersion.immersionConormalSheafMap i i' f g
      (Stacks.Immersion.toShHom_square sq.w))
```

**`Deformation.Examples.isBaseCompatibleConormalMap_deformationConormalBaseChangeIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeDeformationConormalBaseChange.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/SchemeDeformationConormalBaseChange.lean#L252). The attribute's comment: “naturality in the base object: the flat base change for the conormal sheaf of the special fibre of the target of an arrow of deformations is the conormal datum compatible with the base along the factorisation through the spectrum of the source's base object, the map on the base being the conormal map of the morphism of base objects. This is one of the two readings of a single canonical map of Tag 01R4, not a computation of either reading on sections”.

> **The flat base change of the target deformation is compatible with the base, along the other
> factorisation of the same composite square.** The square carrying the special fibre of `Q` over
> the closed point of `Spec A` also factors through `Spec B`: the special-fibre square of `Q`
> followed by the square of closed points
> `Deformation.Examples.residueSpecMap_naturality`. Reading the canonical map of
> [Stacks Project, Tag 01R4] along *that* factorisation makes
> `Deformation.Examples.deformationConormalBaseChangeIso` at `Q` the compatible datum, the map
> coming from the base being the conormal map
> `Deformation.Examples.residueConormalMap` of `φ.base`.
>
> Together with `Deformation.Examples.isBaseCompatibleConormalMap_deformationConormalMap` this is
> the naturality of flat base change for the conormal sheaf of a special fibre in the base object
> of `𝒞_Λ`: the two statements are the two readings of one canonical map.

```lean
theorem isBaseCompatibleConormalMap_deformationConormalBaseChangeIso (φ : P ⟶ Q) :
    IsBaseCompatibleConormalMap Q.specialMap (residueSpecMap Q.base) (residueSpecMap P.base)
      (𝟙 (Spec (CommRingCat.of k))) (baseSpecMap φ.base) (Q.toBase ≫ baseSpecMap φ.base) X.hom
      (residueSpecMap_comp_baseSpecMap' φ.base)
      (square_comp Q.specialCartesian.w (residueSpecMap_comp_baseSpecMap' φ.base))
      (deformationConormalBaseChangeIso Q).hom
```

**`Deformation.Examples.deformationConormalBaseChangeIso_naturality`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/Examples/Geometric/SchemeDeformationConormalBaseChange.lean, line 322](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/Examples/Geometric/SchemeDeformationConormalBaseChange.lean#L322). The attribute's comment: “naturality of flat base change for the conormal sheaf of a special fibre in the base object: for an arrow of deformations, the pullback along the structure morphism of the conormal map of the morphism of base objects, followed by the flat base change of the target, is the flat base change of the source followed by the conormal map of the arrow -- up to the eqToHom comparing the two unit composites of the edge on the closed subschemes. Both conormal maps are the canonical maps of Tag 01R4; nothing is computed on sections and the map on the base is NOT identified with the map of maximal ideals”.

> **The flat base change of the conormal sheaf of a special fibre is natural in the base object
> of `𝒞_Λ`.** For an arrow `φ : P ⟶ Q` of deformations of `X` the square
>
> `p_X^* 𝒞_{Spec k/Spec A} ⟶ 𝒞_{X/P.scheme}`, `p_X^* 𝒞_{Spec k/Spec B} ⟶ 𝒞_{X/Q.scheme}`
>
> commutes, the horizontal maps being
> `Deformation.Examples.deformationConormalBaseChangeIso` and the vertical ones the pullback along
> `p_X` of the conormal map of `φ.base` and the conormal map of `φ`. **This is the statement that
> the conormal map of an arrow of deformations corresponds, under flat base change, to the conormal
> map of the morphism of base objects.**
>
> Both maps of conormal sheaves are written in the unstripped shape [Stacks Project, Tag 01R4]
> produces — that is, out of the pullback along the edge on the closed subschemes, which is an
> identity — so each composite begins with the comparison
> `RingedSpaceModuleAdjunction.modulePullbackComp` of the pullback along a composite with the
> composite of the pullbacks, and the two composites `𝟙_X ≫ p_X` and `p_X ≫ 𝟙_{Spec k}` of those
> edges differ by a `CategoryTheory.eqToHom`. The stripped maps are
> `Deformation.Examples.deformationConormalMap` and
> `Deformation.Examples.residueConormalMap`.
>
> The proof is the two factorisations
> `Deformation.Examples.isBaseCompatibleConormalMap_deformationConormalBaseChangeIso` and
> `Deformation.Examples.isBaseCompatibleConormalMap_deformationConormalMap` of the one canonical
> map, compared by `Stacks.Immersion.immersionConormalSheafMap_congr` along the equality of edges;
> the right-hand edges of the two squares over `Spec A` are identified by the cartesian square
> `Deformation.Examples.SchemeDeformationCategory.Hom.cartesian` of the arrow.

```lean
theorem deformationConormalBaseChangeIso_naturality (φ : P ⟶ Q) :
    (modulePullbackComp X.hom.toLRSHom.toShHom
            (Scheme.Hom.toLRSHom (𝟙 (Spec (CommRingCat.of k)))).toShHom).hom.app
          (immersionConormalSheaf (residueSpecMap P.base)) ≫
        (modulePullback X.hom.toLRSHom.toShHom).map
            (immersionConormalSheafMap (residueSpecMap Q.base) (residueSpecMap P.base)
              (𝟙 (Spec (CommRingCat.of k))) (baseSpecMap φ.base)
              (toShHom_square (residueSpecMap_comp_baseSpecMap' φ.base))) ≫
          (deformationConormalBaseChangeIso Q).hom =
      eqToHom (congrArg (fun p : X.left ⟶ Spec (CommRingCat.of k) =>
            (modulePullback p.toLRSHom.toShHom).obj
              (immersionConormalSheaf (residueSpecMap P.base)))
            ((Category.id_comp X.hom).trans (Category.comp_id X.hom).symm).symm) ≫
        (modulePullbackComp (Scheme.Hom.toLRSHom (𝟙 X.left)).toShHom
              X.hom.toLRSHom.toShHom).hom.app
            (immersionConormalSheaf (residueSpecMap P.base)) ≫
          (modulePullback (Scheme.Hom.toLRSHom (𝟙 X.left)).toShHom).map
              (deformationConormalBaseChangeIso P).hom ≫
            immersionConormalSheafMap Q.specialMap P.specialMap (𝟙 X.left) φ.map
              (toShHom_square (specialMap_comp_map φ))
```

**`Ideal.bijective_cotangentBaseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/RingTheory/Flat/CotangentBaseChange.lean, line 332](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/RingTheory/Flat/CotangentBaseChange.lean#L332). The attribute's comment: “flat case, affine”. References: EGA IV (16.2.2), “(iii)”; EGA IV (17.13.1), “special case”; SGA 6 VIII (2.2), “special case”.

> **[Stacks Project, Tag 0473], the flat case in the affine picture.** Let `S` be a flat
> `R`-algebra, let `I` be an ideal of `R` and let `I S` be the ideal of `S` generated by its image.
> Then the canonical map
>
> `I ⧸ I ^ 2 ⊗[R] S ⟶ I S ⧸ (I S) ^ 2`
>
> is an isomorphism.  This is the commutative algebra statement the proof of that tag reduces to;
> the sheaf-level statement for a cartesian square of immersions of schemes is not proved here, and
> the surjectivity half of the tag is `Stacks.Immersion.epi_immersionConormalSheafMap`.

```lean
theorem bijective_cotangentBaseChange [Module.Flat R S] :
    Function.Bijective (I.cotangentBaseChange S)
```

## Tag 062S, a lemma

[Tag 062S](https://stacks.math.columbia.edu/tag/062S) in the Stacks Project.

**`Stacks.Immersion.conormalSequenceRightMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Conormal/ConormalSequence.lean, line 92](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Conormal/ConormalSequence.lean#L92). The attribute's comment: “the second arrow 𝒞\_\{Z/X} ⟶ 𝒞\_\{Z/Y}”.

> **The right-hand map `𝒞_{Z/X} ⟶ 𝒞_{Z/Y}` of the conormal sequence of
> [Stacks Project, Tag 062S].** It is the canonical map of [Stacks Project, Tag 01R4] attached to
> the square with horizontal maps `i` and `i ≫ j` and vertical maps `𝟙_Z` and `j`, read through the
> identification of the pullback along the identity with the identity functor.

```lean
def conormalSequenceRightMap (i : Z ⟶ Y) (j : Y ⟶ X) [IsImmersion i] [IsImmersion j] :
    conormalSheaf (i ≫ j).liftCoborder.toLRSHom.toShHom ⟶
      conormalSheaf i.liftCoborder.toLRSHom.toShHom
```

**`Stacks.Immersion.epi_conormalSequenceRightMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Conormal/ConormalSequence.lean, line 109](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Conormal/ConormalSequence.lean#L109). The attribute's comment: “exactness at the right term: the canonical map 𝒞\_\{Z/X} ⟶ 𝒞\_\{Z/Y} is epi”. References: EGA IV (16.2.7), “surjectivity at right”.

> **[Stacks Project, Tag 062S]: the conormal sequence is exact at `𝒞_{Z/Y}`.** For immersions
> `Z ⟶ Y ⟶ X` the canonical map `𝒞_{Z/X} ⟶ 𝒞_{Z/Y}` is an epimorphism, which is the `⟶ 0` at the
> right-hand end of the canonical sequence `i^* 𝒞_{Y/X} ⟶ 𝒞_{Z/X} ⟶ 𝒞_{Z/Y} ⟶ 0`.
>
> The defining square is cartesian by `Stacks.Immersion.conormalSequence_isPullback`, so
> `Stacks.Immersion.epi_immersionConormalSheafMap` applies; the pullback-identity isomorphism is an
> epimorphism.

```lean
theorem epi_conormalSequenceRightMap (i : Z ⟶ Y) (j : Y ⟶ X) [IsImmersion i] [IsImmersion j] :
    Epi (conormalSequenceRightMap i j)
```

**`Stacks.Immersion.conormalSequence_comp_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Conormal/ConormalSequenceExact.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Conormal/ConormalSequenceExact.lean#L198). The attribute's comment: “the two canonical maps form a complex: the composite i^* 𝒞\_\{Y/X} ⟶ 𝒞\_\{Z/X} ⟶ 𝒞\_\{Z/Y} is zero, for any immersions i : Z ⟶ Y and j : Y ⟶ X; the left-hand map is Stacks.Immersion.conormalLeftMap, equal to Stacks.AlgebraicGeometry.conormalSequenceLeftMap by Stacks.AlgebraicGeometry.conormalSequenceLeftMap\_eq”.

> **[Stacks Project, Tag 062S]: the two canonical maps of the conormal sequence compose to
> zero.** For immersions `Z ⟶ Y ⟶ X` the composite
> `i^* 𝒞_{Y/X} ⟶ 𝒞_{Z/X} ⟶ 𝒞_{Z/Y}` vanishes.
>
> Transposing along `i^* ⊣ i_*` turns the statement into one about sections over opens of `Y`. Over
> the preimage of a chart a section of `𝒞_{Y/X}` is the class of a function `k` cutting out `Y`, the
> left-hand map carries it to the class of `k` as a function cutting out `Z` in `X`, and the
> right-hand map carries that to the class of the restriction of `k` to the preimage of the chart
> in `Y`, which is zero because `k` vanishes there. The charts refine every open of `Y`.

```lean
theorem conormalSequence_comp_zero (i : Z ⟶ Y) (j : Y ⟶ X) [IsImmersion i] [IsImmersion j] :
    conormalLeftMap i j ≫ conormalSequenceRightMap i j = 0
```

**`Stacks.Immersion.conormalSequenceShortComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Conormal/ConormalSequenceExact.lean, line 280](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Conormal/ConormalSequenceExact.lean#L280). The attribute's comment: “the sequence as a short complex”.

> **The conormal sequence of [Stacks Project, Tag 062S]** as a two-term complex of
> `𝒪_Z`-modules, `i^* 𝒞_{Y/X} ⟶ 𝒞_{Z/X} ⟶ 𝒞_{Z/Y}`.

```lean
def conormalSequenceShortComplex (i : Z ⟶ Y) (j : Y ⟶ X) [IsImmersion i] [IsImmersion j] :
    ShortComplex (SheafOfModules.{u} (structureSheafRing Z.toLocallyRingedSpace.toRingedSpace))
```

**`Stacks.Immersion.conormalSequence_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Conormal/ConormalSequenceExact.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Conormal/ConormalSequenceExact.lean#L298). The attribute's comment: “exactness in the middle: for any immersions i : Z ⟶ Y and j : Y ⟶ X the image of i^* 𝒞\_\{Y/X} ⟶ 𝒞\_\{Z/X} is the kernel of 𝒞\_\{Z/X} ⟶ 𝒞\_\{Z/Y} (equality, as ShortComplex.Exact of the complex built from the two canonical maps of Tag 01R4); no hypothesis beyond the two immersions”.

> **[Stacks Project, Tag 062S]: the conormal sequence is exact at `𝒞_{Z/X}`.** For immersions
> `Z ⟶ Y ⟶ X` the kernel of the canonical map `𝒞_{Z/X} ⟶ 𝒞_{Z/Y}` is the image of the canonical
> map `i^* 𝒞_{Y/X} ⟶ 𝒞_{Z/X}`.
>
> Exactness is local, and it is tested over the preimages of the charts of the chain
> (`Stacks.Immersion.exact_of_chartwise`). Over a chart the two maps are, on sections, the two maps
> of conormal modules of the tower of rings `Γ(X, V) ⟶ Γ(X, V) ⟶ Γ(Y, j⁻¹V)`, whose exactness is
> `Stacks.Conormal.exact_mapCotangent_comap`; that is
> `Stacks.Immersion.ConormalChart.exists_leftMap_eq`.

```lean
theorem conormalSequence_exact (i : Z ⟶ Y) (j : Y ⟶ X) [IsImmersion i] [IsImmersion j] :
    (conormalSequenceShortComplex i j).Exact
```

**`Stacks.AlgebraicGeometry.conormalSequenceLeftMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Conormal/SplitSequence.lean, line 43](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Conormal/SplitSequence.lean#L43). The attribute's comment: “the first arrow i^* 𝒞\_\{Y/X} ⟶ 𝒞\_\{Z/X}”.

> **The left-hand map `i^* 𝒞_{Y/X} ⟶ 𝒞_{Z/X}` of the conormal sequence of
> [Stacks Project, Tag 062S].** It is the canonical map of [Stacks Project, Tag 01R4] attached to
> the square with horizontal maps `i ≫ j` and `j` and vertical maps `i` and `𝟙 X`.

```lean
def conormalSequenceLeftMap (i : Z ⟶ Y) (j : Y ⟶ X) [IsImmersion i] [IsImmersion j] :
    (modulePullback i.toLRSHom.toShHom).obj
        (Stacks.ClosedImmersion.conormalSheaf j.liftCoborder.toLRSHom.toShHom) ⟶
      Stacks.ClosedImmersion.conormalSheaf (i ≫ j).liftCoborder.toLRSHom.toShHom
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 29.32, Tag 01R1](https://stacks.math.columbia.edu/tag/01R1)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
