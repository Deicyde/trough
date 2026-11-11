---
declaration: section
origin: cited
lean: AlgebraicGeometry.SmallEtale.localizedSmallModelMorphism, AlgebraicGeometry.localizedOverOpen, AlgebraicGeometry.Space.localizedSmallModelMorphism, Stacks.Sheaves.RingedToposModules.localizationCompPushforwardModulesIso, AlgebraicGeometry.RingedToposHom.localizedRingedToposSquare, AlgebraicGeometry.RingedToposHom.localizedInverseImageIso, AlgebraicGeometry.RingedToposHom.inverseImageCompLocalizationIso, AlgebraicGeometry.RingedToposHom.localizationCompPushforwardIso
statement: formalized
proof: formalized
---

# 18.22 Localization of morphisms of ringed topoi

Section 18.22 of the Stacks Project, [Tag 04J6](https://stacks.math.columbia.edu/tag/04J6). 4 tags here are carried by 25 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04IF, a lemma

[Tag 04IF](https://stacks.math.columbia.edu/tag/04IF) in the Stacks Project.

**`AlgebraicGeometry.SmallEtale.localizedSmallModelMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleLocalizedMorphism.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Descent/AssociatedModule/SmallEtaleLocalizedMorphism.lean#L89). The attribute's comment: “the localized morphism of ringed topoi of a morphism of the small étale ringed topoi of two schemes, obtained by transporting the morphism through the `Type u` equi-universe models of the two small étale ringed topoi, to which the statement at `RingedTopos.{u, u, u}` applies”.

> **Stacks 04IF for the small étale ringed topoi of schemes.**  Let
> `ψ : (S_étale, 𝒪_S) ⟶ (T_étale, 𝒪_T)` be a morphism of the small étale ringed topoi of two
> schemes of a big étale site and let `G` be a sheaf of sets on the equi-universe model of the
> target.  This is the localized morphism of ringed topoi `ψ'` of Stacks 04IF, from the
> localization of the model of the source at the inverse image of `G` to the localization of the
> model of the target at `G`.
>
> It is obtained by transport: `ψ` is conjugated by the comparisons of the two small étale ringed
> topoi with their equi-universe models — an equivalence of ringed topoi on each side, so nothing
> is lost — and Stacks 04IF is applied to the conjugate, whose two ringed topoi are
> `AlgebraicGeometry.RingedTopos.{u, u, u}`.

```lean
def localizedSmallModelMorphism
    (ψ : RingedToposHom (ringedTopos B S hS) (ringedTopos B T hT))
    (G : (smallModelRingedTopos B T hT).Topos) :
    RingedToposHom
      ((smallModelRingedTopos B S hS).localizedRingedTopos
        (letI : EssentiallySmall.{u} (ringedTopos B S hS).C := essentiallySmall B S hS
         letI : EssentiallySmall.{u} (ringedTopos B T hT).C := essentiallySmall B T hT
         (RingedToposHom.smallModelTransport.{u} ψ).toToposHom.inverseImage.obj G))
      ((smallModelRingedTopos B T hT).localizedRingedTopos G)
```

**`AlgebraicGeometry.localizedOverOpen`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/OpenLocalization.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/OpenLocalization.lean#L178). The attribute's comment: “the localization of a morphism of ringed topoi at the sheaf represented by an open subscheme `V` of the target, for the small étale ringed topoi of two schemes: the morphism of ringed topoi from the localization of the source at the inverse image of that sheaf to the localization of the target at it, with the structure map of 04IF. This is the instance of 04IF at `RingedTopos.{u, u + 1, u}`, the universes of the small étale ringed topos, which is what the Zariski gluing of 04I7 restricts along; it is *not* a morphism between the small étale ringed topoi of two open subschemes, that identification being 04IE for the étale site, which is not carried”.

> **Stacks 04IF for the small étale ringed topoi: the restriction of a morphism of ringed
> topoi to a pair of opens.**
>
> For schemes `X` and `Y` of a big étale site, a morphism of ringed topoi
> `g : (Sh(X_étale), 𝒪_X) ⟶ (Sh(Y_étale), 𝒪_Y)` and an open subscheme `V` of `Y`, this is the
> localization of `g` at the sheaf `h_V^#` represented by `V`: the morphism of ringed topoi
> ```
>   (Sh(X_étale)/g⁻¹h_V^#, (𝒪_X)_{g⁻¹h_V^#}) ⟶ (Sh(Y_étale)/h_V^#, (𝒪_Y)_{h_V^#})
> ```
> of Stacks 04IF, whose inverse image is `(H ⟶ h_V^#) ↦ (g⁻¹H ⟶ g⁻¹h_V^#)`.
>
> It carries no hypothesis beyond `g` and `V`: the essential smallness of the small étale site
> that Stacks 04IF's localization needs is the instance
> `AlgebraicGeometry.SmallEtale.essentiallySmall`.  This is the first input of the Zariski gluing
> in the proof of Stacks 04I7; the identification of the source with the small étale ringed topos
> of the open subscheme of `X` representing `g⁻¹h_V^#` is Stacks 04IE for the étale site and is
> not carried here, so this is not yet that gluing's input in full.

```lean
def localizedOverOpen (X Y : B.Scheme)
    (g : RingedToposHom (RingedSite.toRingedTopos (smallEtaleRingedSite B X.obj X.property))
      (RingedSite.toRingedTopos (smallEtaleRingedSite B Y.obj Y.property)))
    (V : Y.obj.Opens) :
    RingedToposHom
      ((RingedSite.toRingedTopos (smallEtaleRingedSite B X.obj X.property)).localizedRingedTopos
        (g.toToposHom.inverseImage.obj
          ((presheafToSheaf (SmallEtale.topology B Y.obj Y.property) (Type u)).obj
            (openRepresentable'.{u, u} B Y.obj Y.property V))))
      ((RingedSite.toRingedTopos (smallEtaleRingedSite B Y.obj Y.property)).localizedRingedTopos
        ((presheafToSheaf (SmallEtale.topology B Y.obj Y.property) (Type u)).obj
          (openRepresentable'.{u, u} B Y.obj Y.property V)))
```

**`AlgebraicGeometry.Space.localizedSmallModelMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleLocalizedMorphism.lean, line 85](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/SmallEtaleLocalizedMorphism.lean#L85). The attribute's comment: “the localized morphism of ringed topoi of a morphism of the small étale ringed topoi of two algebraic spaces, obtained by transporting the morphism through the `Type u` equi-universe models of the two small étale ringed topoi, to which the statement at `RingedTopos.{u, u, u}` applies”.

> **Stacks 04IF for the small étale ringed topoi of algebraic spaces.**  Let
> `ψ : (X_étale, 𝒪_X) ⟶ (Y_étale, 𝒪_Y)` be a morphism of the small étale ringed topoi of two
> algebraic spaces and let `G` be a sheaf of sets on the equi-universe model of the target.  This is
> the localized morphism of ringed topoi `ψ'` of Stacks 04IF, from the localization of the model of
> the source at the inverse image of `G` to the localization of the model of the target at `G`.
>
> It is obtained by transport: `ψ` is conjugated by the comparisons of the two small étale ringed
> topoi with their equi-universe models — an equivalence of ringed topoi on each side, so nothing is
> lost — and the library's Stacks 04IF is applied to the conjugate, whose two ringed topoi are
> `AlgebraicGeometry.RingedTopos.{u, u, u}`.

```lean
def localizedSmallModelMorphism
    (ψ : RingedToposHom (smallEtaleRingedTopos B S hS X) (smallEtaleRingedTopos B S hS Y))
    (G : (RingedTopos.smallModel.{u} (SmallEtale.topology B S hS Y.1)
      (structureSheaf B S hS Y.1 Y.2)).Topos) :
    RingedToposHom
      ((RingedTopos.smallModel.{u} (SmallEtale.topology B S hS X.1)
          (structureSheaf B S hS X.1 X.2)).localizedRingedTopos
        ((RingedToposHom.smallModelTransport.{u} ψ).toToposHom.inverseImage.obj G))
      ((RingedTopos.smallModel.{u} (SmallEtale.topology B S hS Y.1)
        (structureSheaf B S hS Y.1 Y.2)).localizedRingedTopos G)
```

**`Stacks.Sheaves.RingedToposModules.localizationCompPushforwardModulesIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/ModulePushforwardLocalization.lean, line 1011](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/ModulePushforwardLocalization.lean#L1011). The attribute's comment: “f'\_* j\_F^* = j\_G^* f\_*, on sheaves of modules”.

> **Stacks 04IF, the clause `f'_* j_F^* = j_G^* f_*` on sheaves of modules.** For a morphism
> of ringed topoi `f : (Sh(C), O) ⟶ (Sh(D), O')`, a sheaf of sets `G` on `D` and `F = f^{-1}G`,
> pulling a sheaf of `O`-modules back along the localization `j_F` and pushing it forward along
> the localized morphism `f'` is pushing it forward along `f` and pulling back along the
> localization `j_G`, naturally in the sheaf of modules.
>
> Both pullbacks are the pullbacks of sheaves of modules of Stacks 03D6 part (2) along the
> localization morphisms, which Stacks 04IE part (2)
> (`AlgebraicGeometry.RingedTopos.localizationModulePullbackIso`) identifies with restriction to
> the site of elements; the comparison is therefore
> `elementRestrictionCompPushforwardModulesIso` conjugated by those two identifications.

```lean
noncomputable def localizationCompPushforwardModulesIso :
    RingedToposHom.pullbackModules.{uu, uu, uu, uu, uu, uu}
          (X := X.localizedRingedTopos (f.toToposHom.inverseImage.obj G)) (Y := X)
          (X.localizationMorphism
            (f.toToposHom.inverseImage.obj G)).toRingedToposModulesHom ⋙
        pushforwardModules.{uu, uu, uu, uu, uu, uu}
          (f.localized G).toRingedToposModulesHom ≅
      pushforwardModules.{uu, uu, uu, uu, uu, uu} f.toRingedToposModulesHom ⋙
        RingedToposHom.pullbackModules.{uu, uu, uu, uu, uu, uu}
          (X := Y.localizedRingedTopos G) (Y := Y)
          (Y.localizationMorphism G).toRingedToposModulesHom
```

**`AlgebraicGeometry.RingedToposHom.localizedRingedToposSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizedMorphismComparison.lean, line 504](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizedMorphismComparison.lean#L504). The attribute's comment: “the square of 04IF as a 2-isomorphism of ringed topoi”.

> **Stacks 04IF**: the square of Stacks 04IF as a 2-isomorphism of ringed topoi.
>
> The comparison of inverse images is `inverseImageCompLocalizationIso`, and the compatibility of
> the three structure maps that it needs is `localized_fSharpInverseImage_forget`; the structure
> maps of the two localization morphisms are identities on underlying sheaves of sets, so they
> drop out of the two composites.

```lean
noncomputable def localizedRingedToposSquare (G : Y.Topos) :
    TwoIso (A := X.localizedRingedTopos (f.toToposHom.inverseImage.obj G)) (B := Y)
      (comp (X := X.localizedRingedTopos (f.toToposHom.inverseImage.obj G))
        (Y := Y.localizedRingedTopos G) (Z := Y)
        (Y.localizationMorphism G) (f.localized G))
      (comp (X := X.localizedRingedTopos (f.toToposHom.inverseImage.obj G)) (Y := X) (Z := Y)
        f (X.localizationMorphism (f.toToposHom.inverseImage.obj G)))
```

**`AlgebraicGeometry.RingedToposHom.localizedInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RingedToposMorphismLocalization.lean, line 275](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RingedToposMorphismLocalization.lean#L275). The attribute's comment: “the characterization (f')^\{-1}(H → G) = (f^\{-1}H → F) of f'”.

> **Stacks 04IF**, the rule characterizing `f'`: read through the identifications of the two
> localizations with their slice topoi, the inverse image of `f'` is `Over.post f⁻¹`, that is
> ```
> (f')⁻¹(H ⟶ G) = (f⁻¹H ⟶ f⁻¹G) .
> ```

```lean
noncomputable def localizedInverseImageIso :
    (localizedToposMorphism f G).inverseImage ⋙
        (X.localizationEquivalence (f.toToposHom.inverseImage.obj G)).functor ≅
      (Y.localizationEquivalence G).functor ⋙ Over.post f.toToposHom.inverseImage
```

**`AlgebraicGeometry.RingedToposHom.inverseImageCompLocalizationIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RingedToposMorphismLocalization.lean, line 289](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RingedToposMorphismLocalization.lean#L289). The attribute's comment: “commutativity of the square, on inverse images”.

> **Stacks 04IF**, commutativity of the square on inverse images: `f⁻¹ ⋙ j\_F⁻¹ = j\_G⁻¹ ⋙
> (f')⁻¹`. Concretely, the inverse image of a sheaf `H` on `D`, localized at `F`, is the inverse
> image under `f'` of `H` localized at `G`; this is Stacks 04H1's version of the same square,
> transported across the identifications of the localizations with their slice topoi.

```lean
noncomputable def inverseImageCompLocalizationIso :
    f.toToposHom.inverseImage ⋙
        (X.localizationMorphism (f.toToposHom.inverseImage.obj G)).toToposHom.inverseImage ≅
      (Y.localizationMorphism G).toToposHom.inverseImage ⋙
        (localizedToposMorphism f G).inverseImage
```

**`AlgebraicGeometry.RingedToposHom.localizationCompPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RingedToposMorphismLocalization.lean, line 315](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RingedToposMorphismLocalization.lean#L315). The attribute's comment: “f'\_* j\_F^\{-1} = j\_G^\{-1} f\_*, on sheaves of sets”.

> **Stacks 04IF**: `f'_* j_F⁻¹ = j_G⁻¹ f_*`, on sheaves of sets.
>
> This is Stacks 04H1's identity `f'_* ∘ toOver F = toOver G ∘ f_*` for the slice topoi, read
> through the identification of the inverse image of each localization morphism with `toOver`
> (Stacks 04IE part (1)) and through the two identifications of the localizations with their
> slice topoi.

```lean
noncomputable def localizationCompPushforwardIso :
    (X.localizationMorphism (f.toToposHom.inverseImage.obj G)).toToposHom.inverseImage ⋙
        (localizedToposMorphism f G).pushforward ≅
      f.toToposHom.pushforward ⋙ (Y.localizationMorphism G).toToposHom.inverseImage
```

**`AlgebraicGeometry.RingedToposHom.localized`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RingedToposMorphismLocalization.lean, line 365](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RingedToposMorphismLocalization.lean#L365). The attribute's comment: “the localized morphism of ringed topoi (f', (f')^sharp)”.

> **Stacks 04IF.** The **localized morphism of ringed topoi**
> `(f', (f')♯) : (Sh(C)/F, O_F) ⟶ (Sh(D)/G, O'_G)`, with `F = f⁻¹G`.
>
> Its structure map is the restriction `j_G⁻¹(f♯)` of the structure map of `f`: the localized
> structure sheaf `O'_G` is the inverse image `j_G⁻¹O'`, applying `j_G⁻¹` to `f♯ : O' ⟶ f_*O` lands
> in `j_G⁻¹f_*O`, and that is `f'_*j_F⁻¹O = f'_*O_F` by
> `localizedPushforwardCommRingIso`.

```lean
noncomputable def localized :
    RingedToposHom (X.localizedRingedTopos (f.toToposHom.inverseImage.obj G))
      (Y.localizedRingedTopos G)
```

**`AlgebraicGeometry.RingedToposHom.localized_fSharpInverseImage_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RingedToposMorphismLocalization.lean, line 730](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RingedToposMorphismLocalization.lean#L730). The attribute's comment: “commutativity of the square as a square of ringed topoi: the comparison of inverse images is compatible with the structure maps”.

> **Stacks 04IF**: the square of Stacks 04IF is a square of *ringed* topoi — the comparison of
> inverse images carries the structure map of `f` restricted to the site of elements of `f⁻¹G` to
> the structure map of the localized morphism.
>
> This is the compatibility that commutativity of 04IF's square as a square of ringed topoi needs,
> in inverse-image form and on underlying sheaves of sets, and with it
> `AlgebraicGeometry.RingedToposHom.TwoIso.ofInverseImageIso` turns 04IF's comparison of inverse
> images into a 2-isomorphism of ringed topoi.
>
> The proof is the adjointness the source omits. Both structure maps are adjunct to their
> direct-image forms (`fSharpInverseImage_forget`), the direct-image form of `(f')♯` is `j_G⁻¹(f♯)`
> followed by the comparison of direct images (`localized_fSharp_forget`), and
> `inverseImageCompLocalizationIso_hom_app_comp_counit` says that 04IF's two comparisons are mates
> of each other; naturality of the comparison of inverse images at `f♯` matches the two up.

```lean
theorem localized_fSharpInverseImage_forget :
    (f.inverseImageCompLocalizationIso G).hom.app (Y.forgetRing.obj Y.O) ≫
        (X.localizedRingedTopos (f.toToposHom.inverseImage.obj G)).forgetRing.map
          (f.localized G).fSharpInverseImage =
      (X.localizationMorphism (f.toToposHom.inverseImage.obj G)).toToposHom.inverseImage.map
        (X.forgetRing.map f.fSharpInverseImage)
```

## Tag 04J7, a lemma

[Tag 04J7](https://stacks.math.columbia.edu/tag/04J7) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.Hom.localizedComparisonTwoIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/LocalizedRepresentableKey/TransposedComparison.lean, line 758](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/LocalizedRepresentableKey/TransposedComparison.lean#L758). The attribute's comment: “the diagrams of 04J0 and 04IF agree via the identifications of 04J3, as a 2-isomorphism of morphisms of ringed topoi”.

> **Stacks 04J7.** The diagrams of Stacks 04J0 and Stacks 04IF agree, via the identifications of
> Stacks 04J3: the square commutes: the composite
> `j_V ∘ f'_{04J0}` of the localization of the source at `V` with Stacks 04J0's localized morphism
> is 2-isomorphic to the composite `f'_{04IF} ∘ compareMid` of Stacks 04IF's localized morphism
> with Stacks 04D3's identification of the two localizations of the source.
>
> The 2-isomorphism is `Hom.localizedRepresentableCompInverseImageIso` on inverse images; what
> makes it a 2-isomorphism of morphisms of ringed topoi is `Hom.key`, its compatibility with the
> two structure maps.

```lean
noncomputable def Hom.localizedComparisonTwoIso :
    AlgebraicGeometry.RingedToposHom.TwoIso
      (A := ringedTopos (X.over (f.u.obj V)))
      (B := RingedTopos.localizedRingedTopos Y.ringedTopos (representableSheaf Y V))
      (AlgebraicGeometry.RingedToposHom.comp.{u, u, u, u, u, u, u, u, u}
        (X := ringedTopos (X.over (f.u.obj V)))
        (Y := ringedTopos (Y.over V))
        (Z := RingedTopos.localizedRingedTopos Y.ringedTopos (representableSheaf Y V))
        (representableLocalizationRingedMorphism Y V)
        (f.localizedRingedToposHom V))
      (AlgebraicGeometry.RingedToposHom.comp.{u, u, u, u, u, u, u, u, u}
        (X := ringedTopos (X.over (f.u.obj V)))
        (Y := RingedTopos.localizedRingedTopos X.ringedTopos
          (f.inverseImageRepresentableSheaf V))
        (Z := RingedTopos.localizedRingedTopos Y.ringedTopos (representableSheaf Y V))
        (f.ringedToposHom.localized (representableSheaf Y V))
        (f.compareMid V))
```

**`AlgebraicGeometry.RingedSite.Hom.localizedRepresentableInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableMorphismLocalization.lean, line 299](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableMorphismLocalization.lean#L299). The attribute's comment: “the two localized morphisms have the same inverse image, via the identifications of 04J3”.

> **Stacks 04J7**, on inverse images.  Read through the identifications of Stacks 04J3 of
> `Sh(D/V)` with the localization of the ringed topos at `h_V^#` and of `Sh(C/U)` with the
> localization at `h_U^#`, and through Stacks 04D3's identification of `F = f^{-1}h_V^#` with
> `h_U^#`, the inverse image of the morphism of ringed topoi that Stacks 04IF obtains by localizing
> at `F` and `G = h_V^#` is the inverse image of the morphism of ringed topoi that Stacks 04J0
> obtains by localizing the morphism of ringed sites at `V`.

```lean
noncomputable def Hom.localizedRepresentableInverseImageIso :
    (Y.representableLocalizationEquivalence V).functor ⋙
        (RingedToposHom.localizedToposMorphism f.ringedToposHom
            (representableSheaf Y V)).inverseImage ⋙
          (f.localizedSourceEquivalence V).functor ≅
      (f.localizedRingedToposHom V).toToposHom.inverseImage ⋙
        (X.representableLocalizationEquivalence (f.u.obj V)).functor
```

**`AlgebraicGeometry.RingedSite.Hom.localizedRepresentablePushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableMorphismLocalization.lean, line 318](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableMorphismLocalization.lean#L318). The attribute's comment: “the two localized morphisms have the same direct image”.

> **Stacks 04J7**, on direct images.  Read through the same identifications, the direct image
> of Stacks 04IF's localized morphism is the direct image of Stacks 04J0's localized morphism.  The
> two inverse images agree, so the two direct images agree by uniqueness of right adjoints.

```lean
noncomputable def Hom.localizedRepresentablePushforwardIso :
    ((f.localizedSourceEquivalence V).inverse ⋙
          (RingedToposHom.localizedToposMorphism f.ringedToposHom
            (representableSheaf Y V)).pushforward) ⋙
        (Y.representableLocalizationEquivalence V).inverse ≅
      (X.representableLocalizationEquivalence (f.u.obj V)).inverse ⋙
        (f.localizedRingedToposHom V).toToposHom.pushforward
```

**`AlgebraicGeometry.RingedSite.Hom.localizedRepresentable_forgetFSharp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableMorphismLocalization.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableMorphismLocalization.lean#L346). The attribute's comment: “the two maps (f')^sharp agree, each being the restriction j^\{-1}(f^sharp) of the structure map of f along its own localization morphism”.

> **Stacks 04J7**, on structure maps: the two `(f')^♯` are the same formula, each being the
> restriction `j^{-1}(f^♯)` of the structure map of `f` along its own localization morphism — along
> `j_V` for Stacks 04J0 and along `j_G` for Stacks 04IF — and Stacks 04J3 identifies
> `(j_G, j_G^♯)` with `(j_V, j_V^♯)`.
>
> For Stacks 04J0 the restriction is the whole formula, because Stacks 03CF's clause (d) is a
> strict equality of functors `f'_*j_U^{-1} = j_V^{-1}f_*`.  For Stacks 04IF, where `G` is an
> arbitrary sheaf, that identity is only an isomorphism, and the formula is the restriction followed
> by it; the identifications of sheaves of commutative rings that Stacks 04IF's definition inserts
> contribute nothing, being the identity on underlying sheaves of sets.

```lean
theorem Hom.localizedRepresentable_forgetFSharp :
    AlgebraicGeometry.RingedToposHom.forgetFSharp (f.localizedRingedToposHom V) =
        (Y.overMorphismOfTopoi V).inverseImage.map
          (AlgebraicGeometry.RingedToposHom.forgetFSharp f.ringedToposHom) ∧
      AlgebraicGeometry.RingedToposHom.forgetFSharp
          (AlgebraicGeometry.RingedToposHom.localized f.ringedToposHom
            (representableSheaf Y V)) =
        (RingedTopos.localizationMorphism Y.ringedTopos
              (representableSheaf Y V)).toToposHom.inverseImage.map
            (AlgebraicGeometry.RingedToposHom.forgetFSharp f.ringedToposHom) ≫
          (RingedTopos.localizedRingedTopos Y.ringedTopos
              (representableSheaf Y V)).forgetRing.map
            (AlgebraicGeometry.RingedToposHom.localizedStructureIso f.ringedToposHom
              (representableSheaf Y V)).hom
```

## Tag 04J8, a lemma

[Tag 04J8](https://stacks.math.columbia.edu/tag/04J8) in the Stacks Project.

**`AlgebraicGeometry.RingedToposHom.relocalizedNaturalityInverseImageSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizedNaturalitySquare.lean, line 168](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizedNaturalitySquare.lean#L168). The attribute's comment: “the naturality square of the last assertion, on inverse images”.

> **Stacks 04J8**, the naturality square on inverse images:
> `(j_{F'/F})⁻¹ ∘ (f_s)⁻¹ ≅ (f_{s'})⁻¹ ∘ (j_{G'/G})⁻¹`.
>
> Along the factorization `f_s = f'_G ∘ j_s` this is the relocalization square
> `relocalizationInverseImage_square` for `a ≫ s = s' ≫ f⁻¹b`, whiskered by the inverse image of
> `f'_G`, pasted with the comparison `localizedCompRelocalizationIso` of the localized morphism
> of Stacks 04IF at `G` with the one at `G'`, whiskered by the inverse image of the relocalization
> along `s'`.

```lean
noncomputable def relocalizedNaturalityInverseImageSquare
    (hs : a ≫ s = s' ≫ f.toToposHom.inverseImage.map b) :
    (comp (X := X.localizedRingedTopos F') (Y := X.localizedRingedTopos F)
        (Z := Y.localizedRingedTopos G) (f.relocalized s)
        (X.relocalizationMorphism a)).toToposHom.inverseImage ≅
      (comp (X := X.localizedRingedTopos F') (Y := Y.localizedRingedTopos G')
        (Z := Y.localizedRingedTopos G) (Y.relocalizationMorphism b)
        (f.relocalized s')).toToposHom.inverseImage
```

**`AlgebraicGeometry.RingedToposHom.relocalizedNaturalityToposSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizedNaturalitySquare.lean, line 194](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizedNaturalitySquare.lean#L194). The attribute's comment: “the naturality square of the last assertion, as a square of topoi”.

> **Stacks 04J8**, the naturality square as a square of *topoi*: the comparison of the two direct
> images conjugate to `relocalizedNaturalityInverseImageSquare`.

```lean
noncomputable def relocalizedNaturalityToposSquare
    (hs : a ≫ s = s' ≫ f.toToposHom.inverseImage.map b) :
    (comp (X := X.localizedRingedTopos F') (Y := Y.localizedRingedTopos G')
        (Z := Y.localizedRingedTopos G) (Y.relocalizationMorphism b)
        (f.relocalized s')).toToposHom.pushforward ≅
      (comp (X := X.localizedRingedTopos F') (Y := X.localizedRingedTopos F)
        (Z := Y.localizedRingedTopos G) (f.relocalized s)
        (X.relocalizationMorphism a)).toToposHom.pushforward
```

**`AlgebraicGeometry.RingedToposHom.relocalizedNaturalitySquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizedNaturalitySquare.lean, line 530](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizedNaturalitySquare.lean#L530). The attribute's comment: “the final assertion: for `b`, `a`, `s'` with the compatibility square, the induced square of ringed topoi on the slices commutes”.

> **Stacks 04J8**, the naturality square of the last assertion as a square of *ringed* topoi:
> ```
>   (j_{G'/G}, …) ∘ (f_{s'}, f_{s'}♯) ≅ (f_s, f_s♯) ∘ (j_{F'/F}, …) .
> ```
> This is the pasting of `relocalizationSquareTwoIso` for `a ≫ s = s' ≫ f⁻¹b` with
> `localizedCompRelocalizationRingedSquare` along the factorization `f_s = f'_G ∘ j_s`.

```lean
noncomputable def relocalizedNaturalitySquare
    (hs : a ≫ s = s' ≫ f.toToposHom.inverseImage.map b) :
    TwoIso (A := X.localizedRingedTopos F') (B := Y.localizedRingedTopos G)
      (comp (X := X.localizedRingedTopos F') (Y := Y.localizedRingedTopos G')
        (Z := Y.localizedRingedTopos G) (Y.relocalizationMorphism b) (f.relocalized s'))
      (comp (X := X.localizedRingedTopos F') (Y := X.localizedRingedTopos F)
        (Z := Y.localizedRingedTopos G) (f.relocalized s) (X.relocalizationMorphism a))
```

**`AlgebraicGeometry.RingedToposHom.relocalized`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RingedToposRelocalizedMorphism.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RingedToposRelocalizedMorphism.lean#L193). The attribute's comment: “the morphism (f\_s, f\_s^sharp), and its factorization as the morphism of 04IF after the relocalization morphism of 04J4”.

> **Stacks 04J8.** The morphism of ringed topoi
> `(f_s, f_s♯) : (Sh(C)/F, O_F) ⟶ (Sh(D)/G, O'_G)` attached to a morphism of ringed topoi
> `(f, f♯)`, a sheaf `G` on the target, a sheaf `F` on the source and a morphism
> `s : F ⟶ f⁻¹G`: the composition of the localized morphism of Stacks 04IF, from the localization
> at `f⁻¹G`, with the relocalization morphism of Stacks 04J4 along `s`.
>
> The factorization that Stacks 04J8 asserts is this definition.

```lean
noncomputable def relocalized :
    RingedToposHom (X.localizedRingedTopos F) (Y.localizedRingedTopos G)
```

**`AlgebraicGeometry.RingedToposHom.relocalizedInverseImageSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RingedToposRelocalizedMorphism.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RingedToposRelocalizedMorphism.lean#L224). The attribute's comment: “commutativity of the localization square, on inverse images”.

> **Stacks 04J8**, commutativity of the localization square on inverse images:
> `f⁻¹ ⋙ j_F⁻¹ ≅ j_G⁻¹ ⋙ (f_s)⁻¹`.
>
> Since `j_F⁻¹` is `j_{f⁻¹G}⁻¹` followed by the inverse image of the relocalization along `s` on
> the nose, this is Stacks 04IF's inverse-image square whiskered by that relocalization.

```lean
noncomputable def relocalizedInverseImageSquare :
    (comp (X := X.localizedRingedTopos F) (Y := X) (Z := Y) f
        (X.localizationMorphism F)).toToposHom.inverseImage ≅
      (comp (X := X.localizedRingedTopos F) (Y := Y.localizedRingedTopos G) (Z := Y)
        (Y.localizationMorphism G) (f.relocalized s)).toToposHom.inverseImage
```

**`AlgebraicGeometry.RingedToposHom.relocalizedToposSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RingedToposRelocalizedMorphism.lean, line 252](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RingedToposRelocalizedMorphism.lean#L252). The attribute's comment: “commutativity of the localization square, as a square of topoi”.

> **Stacks 04J8**, commutativity of the localization square as a square of *topoi*: the
> comparison of the two direct images conjugate to `relocalizedInverseImageSquare`.
>
> This is the underlying morphism-of-topoi content of the square; its compatibility with the
> structure sheaves is `relocalizedRingedSquare`.

```lean
noncomputable def relocalizedToposSquare :
    (comp (X := X.localizedRingedTopos F) (Y := Y.localizedRingedTopos G) (Z := Y)
        (Y.localizationMorphism G) (f.relocalized s)).toToposHom.pushforward ≅
      (comp (X := X.localizedRingedTopos F) (Y := X) (Z := Y) f
        (X.localizationMorphism F)).toToposHom.pushforward
```

**`AlgebraicGeometry.RingedToposHom.relocalizedRingedSquare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RingedToposRelocalizedMorphism.lean, line 309](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RingedToposRelocalizedMorphism.lean#L309). The attribute's comment: “commutativity of the localization square as a square of ringed topoi”.

> **Stacks 04J8**, commutativity of the localization square as a square of *ringed* topoi.
>
> The structure-map compatibility of Stacks 04IF's own square is
> `AlgebraicGeometry.RingedToposHom.localized_fSharpInverseImage_forget`: the inverse-image form of
> `(f')♯` for the morphism `f'` of Stacks 04IF, read through 04IF's inverse-image square, is the
> restriction of the inverse-image form of `f♯` to the site of elements of `f⁻¹G`. It is the one
> thing beyond the inverse-image and pushforward squares of Stacks 04IF that commutativity of 04J8's
> square as a square of ringed topoi needs; see the implementation notes of this file.
>
> Given it, the square for `f_s` follows with no further geometry: the structure map of the
> relocalization along `s` and that of the two localization morphisms are identities on
> underlying sheaves of sets, and `j_F⁻¹` is `j_{f⁻¹G}⁻¹` followed by the inverse image of the
> relocalization on the nose.

```lean
noncomputable def relocalizedRingedSquare :
    TwoIso (A := X.localizedRingedTopos F) (B := Y)
      (comp (X := X.localizedRingedTopos F) (Y := Y.localizedRingedTopos G) (Z := Y)
          (Y.localizationMorphism G) (f.relocalized s))
      (comp (X := X.localizedRingedTopos F) (Y := X) (Z := Y) f
        (X.localizationMorphism F))
```

## Tag 04J9, a lemma

[Tag 04J9](https://stacks.math.columbia.edu/tag/04J9) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.Hom.relocalized_fSharpInverseImage_forget`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizedMorphismComparison.lean, line 872](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizedMorphismComparison.lean#L872). The attribute's comment: “the relocalized morphism of 04J1 and the relocalized morphism of 04J8 have the same structure map: each is the structure map of its own `f'` restricted along its own relocalization, the relocalization contributing the identity, so that the assertion reduces to the one of 04J7”.

> **Stacks 04J9**, on structure maps: the two relocalized morphisms have the same structure
> map, each being the structure map of its own localized morphism `f'` restricted along its own
> relocalization.
>
> Read in inverse-image form and on underlying sheaves of sets, the structure map of `f_c` is
> `j_c^{-1}` applied to the structure map of the morphism of Stacks 04J0, and the structure map of
> `f_s` is `j_s^{-1}` applied to the structure map of the morphism of Stacks 04IF; the structure
> maps of the two relocalizations themselves are identities and drop out. Stacks 04J7
> (`AlgebraicGeometry.RingedSite.Hom.localizedRepresentable_forgetFSharp`) says that the two
> structure maps so restricted are the same formula, namely the structure map of `f` restricted
> along the localization morphism.

```lean
theorem Hom.relocalized_fSharpInverseImage_forget :
    (ringedTopos (X.over U)).forgetRing.map (f.relocalized c).fSharpInverseImage =
      (X.relocalizationRingedToposHom c).toToposHom.inverseImage.map
        ((ringedTopos (X.over (f.u.obj V))).forgetRing.map
          (f.localizedRingedToposHom V).fSharpInverseImage) ∧
    (RingedTopos.localizedRingedTopos X.ringedTopos (representableSheaf X U)).forgetRing.map
        (f.ringedToposHom.relocalized (f.relocalizationSheafMap c)).fSharpInverseImage =
      (X.ringedTopos.relocalizationMorphismOfTopoi (f.relocalizationSheafMap c)).inverseImage.map
        ((RingedTopos.localizedRingedTopos X.ringedTopos
            (f.ringedToposHom.toToposHom.inverseImage.obj
              (representableSheaf Y V))).forgetRing.map
          (f.ringedToposHom.localized (representableSheaf Y V)).fSharpInverseImage)
```

**`AlgebraicGeometry.RingedSite.Hom.relocalizedCompInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizedMorphismInverseImage.lean, line 137](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizedMorphismInverseImage.lean#L137). The attribute's comment: “on inverse images: the relocalized morphism of 04J1 and the relocalized morphism of 04J8 have the same inverse image, through the identifications of 04J3 at `U` and at `V`, the comparison being pasted from 04J5 and 04J7 on inverse images. The upgrade of this comparison to a 2-isomorphism of ringed topoi, and the agreement of the two localization squares under it, are not established here”.

> The relocalized morphism of Stacks 04J1 followed by the identification of Stacks 04J3 at `V`,
> and the relocalized morphism of Stacks 04J8 preceded by the identification of Stacks 04J3 at `U`,
> have the same inverse image.

```lean
noncomputable def Hom.relocalizedCompInverseImageIso :
    (AlgebraicGeometry.RingedToposHom.comp (X := ringedTopos (X.over U))
        (Y := ringedTopos (Y.over V))
        (Z := RingedTopos.localizedRingedTopos Y.ringedTopos (representableSheaf Y V))
        (representableLocalizationRingedMorphism Y V)
        (f.relocalized c)).toToposHom.inverseImage ≅
      (AlgebraicGeometry.RingedToposHom.comp (X := ringedTopos (X.over U))
        (Y := RingedTopos.localizedRingedTopos X.ringedTopos (representableSheaf X U))
        (Z := RingedTopos.localizedRingedTopos Y.ringedTopos (representableSheaf Y V))
        (f.ringedToposHom.relocalized (f.relocalizationSheafMap c))
        (representableLocalizationRingedMorphism X U)).toToposHom.inverseImage
```

**`AlgebraicGeometry.RingedSite.Hom.relocalizedComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizedTriangleComparison.lean, line 555](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizedTriangleComparison.lean#L555). The attribute's comment: “the commutative diagrams of 04J1 and of 04J8 agree via the identifications of 04J3”.

> **Stacks 04J9.** The commutative diagram of Stacks 04J1 and the commutative diagram of
> Stacks 04J8 agree via the identifications of Stacks 04J3: there is a 2-isomorphism
> `β : ι_V ∘ f_c ≅ f_s ∘ ι_U` of morphisms of ringed topoi under which the localization square of
> Stacks 04J1 *is* the localization square of Stacks 04J8.

```lean
theorem Hom.relocalizedComparison : f.RelocalizedComparisonStatement c
```

**`AlgebraicGeometry.RingedSite.representableRelocalizationSheafMapCompInverseImageIso_hom_app_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableRelocalizationCoherence.lean, line 397](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableRelocalizationCoherence.lean#L397). The attribute's comment: “the comparison of 04J5 on inverse images is the one determined by 04J3 at U and at V”.

> **Stacks 04J5's comparison of inverse images is the one Stacks 04J3 prescribes.** The
> component of the comparison of the relocalization of the ringed topos along `h_f^#` with the
> relocalization of the ringed site along `f`, taken at an object `j_{h_U^#}^{-1}A` and followed by
> Stacks 04J3's comparison at `U` restricted along `Over.map f`, is Stacks 04J3's comparison at
> `V`.
>
> The two strictness facts the statement uses hold on the nose: the inverse image of the
> relocalization of the ringed topos composed with that of the localization at `h_U^#` *is* the
> inverse image of the localization at `h_V^#`, because
> `AlgebraicGeometry.RingedToposHom.toposRelocalizationTriangle` is built from `Iso.refl` on
> inverse images, and `Over.forget V = Over.map f ⋙ Over.forget U`.
>
> Both sides are morphisms into `j_V^{-1}A`, so the equation is equivalent to its transpose across
> `j_{V!} ⊣ j_V^{-1}`, which is
> `shriek_representableRelocalizationSheafMapCompInverseImageIso_hom_app_comp`.

```lean
theorem representableRelocalizationSheafMapCompInverseImageIso_hom_app_comp
    (A : Sheaf X.J (Type u)) :
    (representableRelocalizationSheafMapCompInverseImageIso X f).hom.app
          ((RingedTopos.localizationMorphism X.ringedTopos
            (representableSheaf X U)).toToposHom.inverseImage.obj A) ≫
        (X.relocalizationRingedToposHom f).toToposHom.inverseImage.map
          ((X.representableLocalizationInverseImageIso U).hom.app A) =
      (X.representableLocalizationInverseImageIso V).hom.app A
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.22, Tag 04J6](https://stacks.math.columbia.edu/tag/04J6)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
