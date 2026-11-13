---
declaration: section
origin: cited
lean: Stacks.Sheaves.LocalizedRingedTopos.sliceEquivalence, Stacks.Sheaves.LocalizedRingedTopos.shriekAdjunction, Stacks.Sheaves.LocalizedRingedTopos.sliceEquivalenceFibers, AlgebraicGeometry.SmallEtale.localizedToposEquivalence, AlgebraicGeometry.SmallEtale.openLocalizedToposEquivalence, AlgebraicGeometry.SmallEtale.openRepresentableLocalizedToposEquivalence, AlgebraicGeometry.SmallEtale.openLocalizedRingedToposHom, AlgebraicGeometry.SmallEtale.elementSiteSheafEquivalence
statement: formalized
proof: formalized
---

# 18.21 Localization of ringed topoi

Section 18.21 of the Stacks Project, [Tag 04ID](https://stacks.math.columbia.edu/tag/04ID). 5 tags here are carried by 58 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 04IE, a lemma

[Tag 04IE](https://stacks.math.columbia.edu/tag/04IE) in the Stacks Project.

**`Stacks.Sheaves.LocalizedRingedTopos.sliceEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RelocalizationSliceComparison.lean, line 160](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RelocalizationSliceComparison.lean#L160). The attribute's comment: “equivalence with the slice topos”. References: SGA 3 IV (4.5.4), “more general”; SGA 4 III (5.4), “special case”.

> **Stacks 04IE**, the equivalence with the slice topos: sheaves on the site of elements of `F`
> are the same thing as sheaves on `C` over `F`. This is the sheaf-level restriction of the
> canonical equivalence of Tag 0791, taken from
> `CategoryTheory.Presheaf.IsSheaf.exists_sheafEquivalence_costructuredArrow_yoneda`.

```lean
noncomputable def sliceEquivalence (X : RingedTopos.{u}) (F : X.Topos) :
    (localizedRingedTopos X F).Topos ≌ Over F
```

**`Stacks.Sheaves.LocalizedRingedTopos.shriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RelocalizationSliceComparison.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RelocalizationSliceComparison.lean#L170). The attribute's comment: “part (3): lower shriek on sets”. References: SGA 4 III (5.5), “Clause 3), special case”.

> **Stacks 04IE**, part (3): the lower shriek of the localization morphism on sheaves of sets is
> the forgetful functor of the slice. Concretely, `Sh(C/F) ≌ Sh(C)/F` followed by `Over.forget F` is
> left adjoint to the inverse image of the localization morphism, which is restriction along the
> projection from the site of elements.

```lean
noncomputable def shriekAdjunction (X : RingedTopos.{u}) (F : X.Topos) :
    (sliceEquivalence X F).functor ⋙ Over.forget F ⊣
      (localizationToposMorphism X F).inverseImage
```

**`Stacks.Sheaves.LocalizedRingedTopos.sliceEquivalenceFibers`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RelocalizationSliceComparison.lean, line 181](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RelocalizationSliceComparison.lean#L181). The attribute's comment: “canonical identification with the slice topos”.

> **Stacks 04IE**: the equivalence with the slice topos is the canonical fibre construction and
> not merely an abstract equivalence. On underlying presheaves, the inverse of `sliceEquivalence`
> sends an object `φ : A ⟶ F` of `Sh(C)/F` to the presheaf `(U, t) ↦ {x ∈ A(U) | φ(x) = t}` on the
> site of elements of `F`.

```lean
noncomputable def sliceEquivalenceFibers (X : RingedTopos.{u}) (F : X.Topos) :
    (sliceEquivalence X F).inverse ⋙ sheafToPresheaf (elementTopology X F) (Type u) ≅
      Over.post (X := F) (sheafToPresheaf X.J (Type u)) ⋙
        (overEquivPresheafCostructuredArrow F.obj).functor
```

**`AlgebraicGeometry.SmallEtale.localizedToposEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/OpenLocalization.lean, line 299](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/OpenLocalization.lean#L299). The attribute's comment: “for the small étale site: the topos of the small étale site of an object `U` of the small étale site of `S` is the topos of the localization of the small étale ringed topos of `S` at the sheaf represented by `U`. This form identifies the two topoi; the identification of the two RINGED topoi, structure sheaves included, is `AlgebraicGeometry.SmallEtale.localizedRingedToposHom`. It is the composite of three equivalences: the equivalence of sites between the small étale site of the scheme of `U` and the slice of the small étale site of `S` at `U`, read on sheaves; Stacks 00Y1 for the slice site; and the equivalence of the localization at a sheaf with the slice of the topos”.

> **Stacks 04IE for the small étale site: the small étale topos of an object `U` of the small
> étale site of `S` is the localization of the small étale topos of `S` at the sheaf `h_U^#`.**
>
> The three steps of the identification are each proved elsewhere and none of them is rebuilt here.
> The small étale site of the scheme of `U` is the slice `(S_étale)/U`, so their topoi agree
> (`AlgebraicGeometry.SmallEtale.localizationSheafEquivalence`, which is
> `AlgebraicGeometry.SmallEtale.localizationEquivalence` read on sheaves); the topos of a slice
> site is the slice of the topos at the represented sheaf, which is Stacks 00Y1
> (`CategoryTheory.OverShriek.sheafEquivalence`); and the slice of a topos at a sheaf is the
> localization of the ringed topos at that sheaf, which is Stacks 04IE in the generality it is
> formalized in (`AlgebraicGeometry.RingedTopos.localizationEquivalence`).
>
> What this is *not*: an identification of **ringed** topoi. It identifies the two topoi only.
> Upgrading it needs the comparison of the two structure sheaves — the structure sheaf of the
> localization is the restriction of `𝒪_S` along the projection from the site of elements of
> `h_U^#`, and the structure sheaf of the small étale site of the scheme of `U` is its own sheaf
> of global functions — and that comparison is not carried here.

```lean
noncomputable def localizedToposEquivalence :
    Sheaf (SmallEtale.topology B U.obj.left.obj U.obj.left.property) (Type u) ≌
      (RingedTopos.localizedRingedTopos
        (RingedSite.toRingedTopos (smallEtaleRingedSite B S hS))
        ((presheafToSheaf (SmallEtale.topology B S hS) (Type u)).obj (yoneda.obj U))).Topos
```

**`AlgebraicGeometry.SmallEtale.openLocalizedToposEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/OpenLocalization.lean, line 333](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/OpenLocalization.lean#L333). The attribute's comment: “for an open subscheme: the topos of the small étale site of an open subscheme `V` of `S` is the topos of the localization of the small étale ringed topos of `S` at the sheaf represented by `V` regarded as étale over `S`. This is the composite of `AlgebraicGeometry.opensToBoundedEtale` with the identification of the small étale site of an object with the slice over it. The sheaf localized at is the one `V` represents in the small étale site; that it agrees with `AlgebraicGeometry.openRepresentable'` is `AlgebraicGeometry.SmallEtale.openRepresentableSheafIsoYoneda`, and the identification of the two RINGED topoi at that spelling is `AlgebraicGeometry.SmallEtale.openLocalizedRingedToposHom`”. References: SGA 4 VIII (6.2), “partial”.

> **Stacks 04IE for an open subscheme: the small étale topos of an open subscheme `V` of `S`
> is the localization of the small étale topos of `S` at the sheaf represented by `V`.**
>
> This is `AlgebraicGeometry.SmallEtale.localizedToposEquivalence` at the object
> `AlgebraicGeometry.opensToBoundedEtale B S hS V` of the small étale site, the open subscheme `V`
> regarded as étale over `S` — the composite of that functor with
> `AlgebraicGeometry.SmallEtale.localizationEquivalence`, which is the identification the Zariski
> gluing of Stacks 04I7 restricts along.
>
> The sheaf it localizes at is `h_V^#` for `V` read in the small étale site. It is **not** stated
> here to agree with `AlgebraicGeometry.openRepresentable'`, which spells the same idea as the
> restriction to the small étale site of the presheaf `V` represents in the big étale slice, with
> its sections raised by `CategoryTheory.uliftYoneda`; identifying the two is a separate
> comparison and is not carried.

```lean
noncomputable def openLocalizedToposEquivalence (V : S.Opens) :
    Sheaf (SmallEtale.topology B V.toScheme
        (Scheme.size_lt_of_isOpenImmersion V.ι hS)) (Type u) ≌
      (RingedTopos.localizedRingedTopos
        (RingedSite.toRingedTopos (smallEtaleRingedSite B S hS))
        ((presheafToSheaf (SmallEtale.topology B S hS) (Type u)).obj
          (yoneda.obj ((opensToBoundedEtale B S hS).obj V)))).Topos
```

**`AlgebraicGeometry.SmallEtale.openRepresentableLocalizedToposEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/OpenLocalization.lean, line 389](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/OpenLocalization.lean#L389). The attribute's comment: “for an open subscheme `V` of `S`, with the sheaf localized at spelled as the sheafification of `AlgebraicGeometry.openRepresentable'`: the topos of the small étale site of `V` is the topos of the localization of the small étale ringed topos of `S` at that sheaf. This is `AlgebraicGeometry.SmallEtale.openLocalizedToposEquivalence` transported along the comparison of the two spellings of the represented sheaf; the identification of the two RINGED topoi at this spelling, structure sheaves included, is `AlgebraicGeometry.SmallEtale.openLocalizedRingedToposHom`”.

> **Stacks 04IE for an open subscheme, at the `AlgebraicGeometry.openRepresentable'`
> spelling of the sheaf it localizes at.**
>
> This is `AlgebraicGeometry.SmallEtale.openLocalizedToposEquivalence` moved along
> `AlgebraicGeometry.SmallEtale.openRepresentableSheafIsoYoneda` by
> `AlgebraicGeometry.RingedTopos.localizedToposEquivalenceOfIso`, and it is the form in which
> Stacks 04IE meets Stacks 04IF: the target of `AlgebraicGeometry.localizedOverOpen` and the
> source `AlgebraicGeometry.inverseImageOpenLocalizedToposEquivalence` produces are both
> localizations at the sheafification of `AlgebraicGeometry.openRepresentable'`.
>
> Still the two **topoi** only.  The morphism of ringed topoi of Stacks 04IF therefore composes
> with these as a morphism of topoi and not yet as one of ringed topoi; what is missing is the
> comparison of the two structure sheaves, and this module's implementation notes record what that
> needs.

```lean
noncomputable def openRepresentableLocalizedToposEquivalence (V : S.Opens) :
    Sheaf (SmallEtale.topology B V.toScheme
        (Scheme.size_lt_of_isOpenImmersion V.ι hS)) (Type u) ≌
      (RingedTopos.localizedRingedTopos
        (RingedSite.toRingedTopos (smallEtaleRingedSite B S hS))
        ((presheafToSheaf (SmallEtale.topology B S hS) (Type u)).obj
          (openRepresentable'.{u, u} B S hS V))).Topos
```

**`AlgebraicGeometry.SmallEtale.openLocalizedRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/OpenLocalization.lean, line 449](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/OpenLocalization.lean#L449). The attribute's comment: “for an open subscheme `V` of `S`, as a morphism of RINGED topoi and at the `AlgebraicGeometry.openRepresentable'` spelling of the sheaf: the small étale ringed topos of `V` IS the localization of the small étale ringed topos of `S` at the sheaf `V` represents, structure sheaves included. It is 04IE at the representable spelling (`AlgebraicGeometry.SmallEtale.localizedRingedToposHom`, whose identification of the topoi is a restriction along a functor of sites, which is what makes the structure sheaves comparable) followed by the transport of a localization along an isomorphism of sheaves (`AlgebraicGeometry.RingedTopos.localizedRingedToposHomOfIso`). This is the spelling Stacks 04IF's half of input (1) of the Zariski gluing of 04I7 localizes at, so with it that input is closed”.

> **Stacks 04IE for an open subscheme, as a morphism of ringed topoi, at the
> `AlgebraicGeometry.openRepresentable'` spelling.** The small étale ringed topos of an open
> subscheme `V` of `S` is the localization of the small étale ringed topos of `S` at the sheaf
> `V` represents — structure sheaves included, and at the spelling of that sheaf which Stacks
> 04IF's half of input (1) of the Zariski gluing of Stacks 04I7 localizes at.
>
> It is `AlgebraicGeometry.SmallEtale.localizedRingedToposHom`, which is Stacks 04IE at the
> representable spelling, followed by
> `AlgebraicGeometry.RingedTopos.localizedRingedToposHomOfIso` along
> `AlgebraicGeometry.SmallEtale.openRepresentableSheafIso`.  With it, the target of
> `AlgebraicGeometry.localizedOverOpen` and the source
> `AlgebraicGeometry.inverseImageOpenLocalizedToposEquivalence` produces are both identified with
> small étale ringed topoi of opens, as morphisms of ringed topoi, and input (1) is closed.
>
> **Universes.** `AlgebraicGeometry.RingedToposHom.comp` elaborates its own nine universe
> parameters before its arguments, and the three belonging to the source default to zero if left
> to be inferred; they are supplied positionally, in the order
> `comp.{Xv, Xu, Xw, Yv, Yu, Yw, Zv, Zu, Zw}` that `pp.universes` reports, with the two
> localizations' object universe written `max (u + 1) u`.  Annotating the argument, `let`-binding
> it with its type written out, and `by exact` all come too late.

```lean
def openLocalizedRingedToposHom (V : S.Opens) :
    RingedToposHom (RingedSite.toRingedTopos (smallEtaleRingedSite B V.toScheme
        (Scheme.size_lt_of_isOpenImmersion V.ι hS)))
      (RingedTopos.localizedRingedTopos.{u, u + 1}
        (RingedSite.toRingedTopos (smallEtaleRingedSite B S hS))
        ((presheafToSheaf (SmallEtale.topology B S hS) (Type u)).obj
          (openRepresentable'.{u, u} B S hS V)))
```

**`AlgebraicGeometry.SmallEtale.elementSiteSheafEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/SmallEtaleElementSite.lean, line 283](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/SmallEtaleElementSite.lean#L283). The attribute's comment: “for the small étale site of an object `U` of the small étale site of `S`, with the identification given as restriction along a functor of sites: the small étale topos of the scheme of `U` is the topos of the localization of the small étale ringed topos of `S` at the sheaf `U` represents. The functor of sites is the equivalence of the small étale site of the scheme of `U` with the slice at `U`, followed by the identification of that slice with the site of elements of the represented sheaf, which is available because the small étale topology is subcanonical; the comparison of the two topologies is `AlgebraicGeometry.SmallEtale.functorPushforward_mem_elementTopology_iff`”.

> **Stacks 04IE for the small étale site, on the topoi, by restriction along a functor of
> sites.** The small étale topos of the scheme of `U` is the topos of the localization of the small
> étale ringed topos of `S` at the sheaf `U` represents, and the identification is restriction
> along `AlgebraicGeometry.SmallEtale.toElementSite`.
>
> That it is a restriction, and not merely an equivalence, is the whole point: the three
> topos-level forms in
> `StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/OpenLocalization.lean` factor
> through Stacks 00Y1, whose functor is a lower shriek, and so carry no comparison of structure
> sheaves; this one does, and the comparison is
> `AlgebraicGeometry.SmallEtale.sheafPushforward_localizedRingedTopos_O`.

```lean
def elementSiteSheafEquivalence :
    Sheaf (SmallEtale.topology B U.obj.left.obj U.obj.left.property) (Type u) ≌
      (RingedTopos.localizedRingedTopos.{u, u + 1}
        (RingedSite.toRingedTopos (smallEtaleRingedSite B S hS))
        (representableSheaf B S hS U)).Topos
```

**`AlgebraicGeometry.SmallEtale.sheafPushforward_localizedRingedTopos_O`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/SmallEtaleElementSite.lean, line 312](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/SmallEtaleElementSite.lean#L312). The attribute's comment: “the comparison of the two structure sheaves, for the small étale site: the structure sheaf of the localization of the small étale ringed topos of `S` at the sheaf an object `U` represents, restricted along the functor of sites identifying the small étale site of the scheme of `U` with the site of elements, IS the structure sheaf of the small étale site of the scheme of `U`. An equality of sheaves of commutative rings, both being the restriction of the structure sheaf of `S` along post-composition with the structure morphism of `U`”.

> **The structure sheaf of the localization, restricted to the small étale site of the scheme
> of `U`, is its structure sheaf.** This is the cheap presheaf identity, and it is an *equality*:
> the structure sheaf of the localization is the restriction of `𝒪_S` along the projection from
> the site of elements, restricting that along `toElementSite` restricts along the composite
> (`AlgebraicGeometry.SmallEtale.toElementSite_comp_elementProjection`), the composite is
> `AlgebraicGeometry.SmallEtale.postcompose`, and
> `AlgebraicGeometry.SmallEtale.commRingStructurePresheaf` is
> `(SmallEtale.toScheme B S hS).op ⋙ Scheme.Γ`, which `postcompose` leaves alone.
>
> This is the comparison that the topos-level forms of Stacks 04IE do not carry, and the reason
> this route was taken.

```lean
theorem sheafPushforward_localizedRingedTopos_O :
    ((toElementSite B S hS U).sheafPushforwardContinuous CommRingCat.{u}
        (SmallEtale.topology B U.obj.left.obj U.obj.left.property)
        (RingedTopos.elementTopology.{u, u + 1}
          (RingedSite.toRingedTopos (smallEtaleRingedSite B S hS))
          (representableSheaf B S hS U))).obj
      (RingedTopos.localizedRingedTopos.{u, u + 1}
        (RingedSite.toRingedTopos (smallEtaleRingedSite B S hS))
        (representableSheaf B S hS U)).O =
    SmallEtale.commRingStructureSheaf B U.obj.left.obj U.obj.left.property
```

**`AlgebraicGeometry.SmallEtale.localizedRingedToposHom`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/SmallEtaleElementSite.lean, line 419](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/RecoveringMorphisms/SmallEtaleElementSite.lean#L419). The attribute's comment: “for the small étale site, as a morphism of RINGED topoi: the small étale ringed topos of the scheme of an object `U` of the small étale site of `S` is the localization of the small étale ringed topos of `S` at the sheaf `U` represents, structure sheaves included. The morphism of topoi is restriction along the functor of sites identifying the small étale site of the scheme of `U` with the site of elements of that sheaf, and the structure map is the adjunct of the comparison of the two structure sheaves, which is an isomorphism because the comparison is — the two structure sheaves being equal, both the restriction of the structure sheaf of `S` along post-composition with the structure morphism of `U`”.

> **Stacks 04IE for the small étale site, as a morphism of ringed topoi.** The small étale
> ringed topos of the scheme of an object `U` of the small étale site of `S` is the localization of
> the small étale ringed topos of `S` at the sheaf `U` represents — structure sheaves included.
>
> The morphism of topoi is the identification of the two topoi, an equivalence; the structure map
> is the adjunct of `AlgebraicGeometry.SmallEtale.localizedStructureSheafIso`, so it is an
> isomorphism, and the two ringed topoi are identified and not merely compared.

```lean
def localizedRingedToposHom :
    RingedToposHom (RingedSite.toRingedTopos
        (smallEtaleRingedSite B U.obj.left.obj U.obj.left.property))
      (RingedTopos.localizedRingedTopos.{u, u + 1}
        (RingedSite.toRingedTopos (smallEtaleRingedSite B S hS))
        (representableSheaf B S hS U))
```

**`AlgebraicGeometry.RingedTopos.extensionByZeroPresheafSectionIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/ExtensionByZeroFormula.lean, line 384](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/ExtensionByZeroFormula.lean#L384). The attribute's comment: “part (4): direct-sum formula”.

> **Stacks 04IE, part (4): the direct-sum formula.** The sections over `V` of the
> presheaf-level lower shriek of `G` along the localization of `X` at `F` are the direct sum,
> over the sections `s` of `F` over `V`, of the sections of `G` at the element `(V, s)`.

```lean
noncomputable def extensionByZeroPresheafSectionIso
    (G : SheafOfModules.{u} (localizedRingSheaf X F)) (V : X.C) :
    ((PresheafOfModules.pullback.{u}
      (F := elementProjection X F)
      (R := (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj)
      (S := (localizedRingSheaf X F).obj)
      (elementModuleRingPresheafHom X F)).obj G.val).obj (Opposite.op V) ≅
      (∐ extensionByZeroSummands X F G V)
```

**`AlgebraicGeometry.RingedTopos.extensionByZeroPresheafSectionIso_inv_ι`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/ExtensionByZeroFormula.lean, line 398](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/ExtensionByZeroFormula.lean#L398). The attribute's comment: “part (4): canonical comparison on summands”.

> **The direct-sum comparison is the canonical one.** On the summand indexed by a section `s`
> of `F` over `V` it is the component, at the element `(V, s)`, of the unit of the adjunction
> between the presheaf-level lower shriek and restriction to the site of elements.

```lean
theorem extensionByZeroPresheafSectionIso_inv_ι
    (G : SheafOfModules.{u} (localizedRingSheaf X F)) (V : X.C)
    (s : F.obj.obj (Opposite.op V)) :
    HEq (Limits.Sigma.ι (extensionByZeroSummands X F G V) s ≫
      (extensionByZeroPresheafSectionIso X F G V).inv)
      (((PresheafOfModules.pullbackPushforwardAdjunction.{u}
        (F := elementProjection X F)
        (R := (Stacks.SheafOfModules.Tensor.ringSheaf X.O).obj)
        (S := (localizedRingSheaf X F).obj)
        (elementModuleRingPresheafHom X F)).unit.app G.val).app
          (Opposite.op
            (CostructuredArrow.mk (yonedaEquiv.symm s) : elementSite X F)))
```

**`AlgebraicGeometry.RingedTopos.moduleRestriction_obj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/ExtensionByZeroFormula.lean, line 419](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/ExtensionByZeroFormula.lean#L419). The attribute's comment: “part (2): module sections”.

> **Stacks 04IE, part (2): module sections.** At an element `(V, s)` of `F`, the restriction
> of a sheaf of `O`-modules to the site of elements has precisely the sections of the original
> module over `V`.

```lean
theorem moduleRestriction_obj (G : SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    (V : (elementSite X F)ᵒᵖ) :
    (((SheafOfModules.pushforward (F := elementProjection X F)
      (J := elementTopology X F) (K := X.J)
      (elementModuleRingHom X F)).obj G).val.obj V : Type u) =
      (G.val.obj (Opposite.op ((elementProjection X F).obj V.unop)) : Type u)
```

**`AlgebraicGeometry.RingedTopos.localizationModulePullbackIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/ModulePullback.lean, line 133](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/ModulePullback.lean#L133). The attribute's comment: “part (2): inverse image on modules”.

> **Stacks 04IE, part (2): the inverse image on modules.** Pullback of sheaves of modules
> along the localization morphism — the inverse image of Stacks 03D2 followed by extension of
> scalars along the structure map — is restriction to the site of elements of `F`.

```lean
noncomputable def localizationModulePullbackIso :
    (localizationMorphism X F).toRingedToposModulesHom.pullbackModules ≅
      SheafOfModules.pushforward (F := elementProjection X F)
        (J := elementTopology X F) (K := X.J) (elementModuleRingHom X F)
```

**`AlgebraicGeometry.RingedTopos.extensionByZeroModules_adjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/ModulePullback.lean, line 170](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/ModulePullback.lean#L170). The attribute's comment: “part (2) and part (4): module adjunction”.

> **Stacks 04IE, parts (2) and (4): the module adjunction.** On sheaves of modules the lower
> shriek of the localization is left adjoint to pullback along the localization morphism.

```lean
noncomputable def extensionByZeroModules_adjunction :
    SheafOfModules.pullback.{u}
      (F := elementProjection X F) (J := elementTopology X F) (K := X.J)
      (elementModuleRingHom X F) ⊣
      (localizationMorphism X F).toRingedToposModulesHom.pullbackModules
```

**`AlgebraicGeometry.RingedTopos.localizationEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/SliceEquivalence.lean, line 122](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/SliceEquivalence.lean#L122). The attribute's comment: “equivalence with the slice topos”.

> The **canonical equivalence between the localization of `X` at `F` and the slice topos**
> `Sh(C)/F`: the equivalence supplied by Stacks 0791, whose inverse is the fibre construction
> recorded in `localizationEquivalence_fibers`.

```lean
noncomputable def localizationEquivalence : (localizedRingedTopos X F).Topos ≌ Over F
```

**`AlgebraicGeometry.RingedTopos.localizationEquivalence_fibers`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/SliceEquivalence.lean, line 129](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/SliceEquivalence.lean#L129). The attribute's comment: “canonical identification with the slice topos”.

> The equivalence with the slice topos is the canonical fibre construction: on underlying
> presheaves its inverse sends an object `φ : G ⟶ F` of `Sh(C)/F` to the presheaf
> `(U, s) ↦ {t ∈ G(U) | φ(t) = s}` on the site of elements of `F`.

```lean
noncomputable def localizationEquivalence_fibers :
    (localizationEquivalence X F).inverse ⋙
      sheafToPresheaf (elementTopology X F) (Type v) ≅
      Over.post (X := F) (sheafToPresheaf X.J (Type v)) ⋙
        (overEquivPresheafCostructuredArrow F.obj).functor
```

**`AlgebraicGeometry.RingedTopos.localizationShriekAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/SliceEquivalence.lean, line 143](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/SliceEquivalence.lean#L143). The attribute's comment: “part (3): lower shriek on sets”. References: SGA 4 III (5.5), “Clause 3”.

> **The lower shriek of the localization on sheaves of sets is `Over.forget F`**: read
> through the equivalence with the slice topos, the left adjoint of the inverse image of the
> localization morphism is the forgetful functor from `Sh(C)/F`.
>
> This is the adjunction of Stacks 0791 for the same equivalence as
> `localizationEquivalence_fibers`, which is what pins the comparisons built from it down.

```lean
noncomputable def localizationShriekAdjunction :
    (localizationEquivalence X F).functor ⋙ Over.forget F ⊣
      (localizationMorphism X F).toToposHom.inverseImage
```

**`AlgebraicGeometry.RingedTopos.localizationInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/SliceEquivalence.lean, line 158](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/SliceEquivalence.lean#L158). The attribute's comment: “part (1): inverse image”. References: SGA 4 IV (5.2).

> **The inverse image of the localization is product with `F`**: read through the
> equivalence with the slice topos, the inverse image of the localization morphism is
> `toOver F`, which sends a sheaf `G` to the product `G × F` viewed as an object over `F`.

```lean
noncomputable def localizationInverseImageIso :
    (localizationMorphism X F).toToposHom.inverseImage ⋙
      (localizationEquivalence X F).functor ≅ toOver F
```

**`AlgebraicGeometry.RingedTopos.forget_localizationInverseImageIso_hom_app`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/SliceEquivalence.lean, line 174](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/SliceEquivalence.lean#L174). The attribute's comment: “part (1): the comparison is the one the lower shriek prescribes”.

> **The comparison of the inverse image with `toOver F` is the one the lower shriek
> prescribes**: the component of `localizationInverseImageIso` at a sheaf `G`, followed by the
> projection `G × F ⟶ G`, is the counit of the lower shriek adjunction at `G`.
>
> This is what `localizationInverseImageIso` means, and it is a statement only because the
> equivalence and the adjunction come from one package: for an unrelated adjunction the two sides
> are morphisms that nothing relates. With `localizationInverseImageIso_eq` it pins the comparison
> down completely.

```lean
theorem forget_localizationInverseImageIso_hom_app (G : X.Topos) :
    (Over.forget F).map ((localizationInverseImageIso X F).hom.app G) ≫
        (forgetAdjToOver F).counit.app G =
      (localizationShriekAdjunction X F).counit.app G
```

**`AlgebraicGeometry.RingedTopos.localizationInverseImageIso_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/SliceEquivalence.lean, line 204](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/SliceEquivalence.lean#L204). The attribute's comment: “part (1): the comparison is unique”.

> **The comparison of the inverse image with `toOver F` is unique**: an isomorphism of
> `j⁻¹ ⋙ E.functor` with `toOver F` whose components are, after the projection `G × F ⟶ G`, the
> counit of the lower shriek adjunction is `localizationInverseImageIso`.
>
> A morphism into `toOver F` over `F` is determined by its composite with that projection, its
> composite with the other one being its structure morphism — which is
> `CategoryTheory.Iso.ext_of_left_comp_forgetAdjToOver_counit`. Together with
> `forget_localizationInverseImageIso_hom_app` this is what makes the comparison of a relocalization
> with base change computable: it is enough to exhibit one isomorphism with the right counits.

```lean
theorem localizationInverseImageIso_eq
    (Ψ : (localizationMorphism X F).toToposHom.inverseImage ⋙
      (localizationEquivalence X F).functor ≅ toOver F)
    (h : ∀ G : X.Topos, (Over.forget F).map (Ψ.hom.app G) ≫ (forgetAdjToOver F).counit.app G =
      (localizationShriekAdjunction X F).counit.app G) :
    Ψ = localizationInverseImageIso X F
```

**`AlgebraicGeometry.RingedTopos.fibreTranspose_shriek_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/SliceEquivalence.lean, line 327](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/SliceEquivalence.lean#L327). The attribute's comment: “part (1): the fibre transpose of the lower shriek counit”.

> **The fibre transpose of the lower shriek counit is the unit of the equivalence.** Both
> morphisms `E⁻¹(E(j⁻¹G)) ⟶ j⁻¹G` agree on fibre sections, by
> `CategoryTheory.Presheaf.IsSheaf.app_fibers_inv_comp_homEquiv_shriek` and by
> `CategoryTheory.Presheaf.IsSheaf.app_fibers_inv_comp_unitInv`; the fibre identification is an
> isomorphism, so they are equal.
>
> This is the functor-level form of Stacks 0791's bridge between the fibre description of the
> equivalence and the counit of `j_!`, and it is what lets a comparison built from fibres be
> compared with the counit.

```lean
theorem fibreTranspose_shriek_counit (G : X.Topos) :
    fibreTranspose X F ((localizationEquivalence X F).functor.obj
          ((X.localizationMorphism F).toToposHom.inverseImage.obj G)) G
        ((X.localizationShriekAdjunction F).counit.app G) =
      (localizationEquivalence X F).unitInv.app
        ((X.localizationMorphism F).toToposHom.inverseImage.obj G)
```

**`AlgebraicGeometry.RingedTopos.localizedRingedTopos`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/ToposLocalization.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/ToposLocalization.lean#L153). The attribute's comment: “the localized ringed topos”. References: SGA 4 IV (11.2.1), “(E/X, A|X)”.

> The **localization of the ringed topos `X` at the sheaf `F`**: the site of elements of `F`,
> with the restricted topology, and with the restriction of `O` along the projection as structure
> sheaf.

```lean
noncomputable abbrev localizedRingedTopos : RingedTopos.{v, max u v, v}
```

**`AlgebraicGeometry.RingedTopos.localizationMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/ToposLocalization.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/ToposLocalization.lean#L188). The attribute's comment: “canonical morphism of ringed topoi”. References: SGA 4 IV (11.2.1), “localization morphism”.

> The localization as a morphism of ringed topoi: the morphism of topoi above, with the
> identification of the inverse image of `O` with the localized structure sheaf as structure
> map.

```lean
noncomputable def localizationMorphism :
    RingedToposHom (localizedRingedTopos X F) X
```

Declarations registered for the tag:

- [`SheafOfModules.pushforward`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.pushforward#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/ModulePullback.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/ModulePullback.lean#L180) (StacksFrontier): “part (2): restriction of modules”. References: EGA 0 (4.2.1), “more general”; EGA 0 (5.3.12); EGA II (1.1.1), “more general”; EGA II (1.1.2), “partial”; EGA IV (21.13.3); SGA 4 IV (11.2.2), “more general”; SGA 4 IV (13.2.1), “special case”; SGA 4 Vbis (1.3.6), “special case”.
- [`SheafOfModules.pullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.pullback#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/ModulePullback.lean, line 189](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/ModulePullback.lean#L189) (StacksFrontier): “part (4): lower shriek on modules”. References: EGA IV (11.9.16), “more general”; EGA IV (2.5.1), “partial”; EGA IV (4.8.2), “more general”; EGA IV (9.4.9); SGA 3 I (4.6.1), “more general”; SGA 3 III (0.1.4), “more general”; SGA 4 VI (8.7.1), “partial”; SGA 4 XVII (4.1); SGA 7 XIV (4.5), “more general”.
- [`SheafOfModules.pullbackIso`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.pullbackIso#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/ModulePullback.lean, line 190](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/ModulePullback.lean#L190) (StacksFrontier): “part (4): sheafification”.

## Tag 04J2, a definition

[Tag 04J2](https://stacks.math.columbia.edu/tag/04J2) in the Stacks Project.

**`AlgebraicGeometry.RingedTopos.localizedRingedTopos`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/ToposLocalization.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/ToposLocalization.lean#L153). The attribute's comment: “part (1): the localization of the ringed topos at F”. References: SGA 4 IV (11.2.1), “(E/X, A|X)”.

> The **localization of the ringed topos `X` at the sheaf `F`**: the site of elements of `F`,
> with the restricted topology, and with the restriction of `O` along the projection as structure
> sheaf.

```lean
noncomputable abbrev localizedRingedTopos : RingedTopos.{v, max u v, v}
```

**`AlgebraicGeometry.RingedTopos.localizationMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/ToposLocalization.lean, line 188](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/ToposLocalization.lean#L188). The attribute's comment: “part (2): the localization morphism”. References: SGA 4 IV (11.2.1), “localization morphism”.

> The localization as a morphism of ringed topoi: the morphism of topoi above, with the
> identification of the inverse image of `O` with the localized structure sheaf as structure
> map.

```lean
noncomputable def localizationMorphism :
    RingedToposHom (localizedRingedTopos X F) X
```

## Tag 04J3, a lemma

[Tag 04J3](https://stacks.math.columbia.edu/tag/04J3) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.left_representableLocalizationForwardInverseImageIso_hom_app_comp_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableLocalization.lean, line 285](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableLocalization.lean#L285). The attribute's comment: “part (2): the comparison of inverse images, read through the lower shriek”.

> **Stacks 04J3's comparison of inverse images, read through the lower shriek.** The
> comparison of the two inverse images in the direction of the slice topos, read through
> `Over.forget` and followed by the lower shriek counit of the localization at `h_U^#`, is Stacks
> 00Y1's identification of `Φ_U ⋙ Over.forget` with `j_{U!}` followed by the lower shriek counit
> of the localization at `U`.
>
> This is the statement that connects the two lower shrieks the comparison of Stacks 04J3 sits
> between — that of the slice site `C/U` and that of the localization of the ringed topos at
> `h_U^#` — and it is what lets an equation built from one be compared with an equation built
> from the other after transposing across `j_{U!}`.
>
> Each of the two factors of `representableLocalizationForwardInverseImageIso` contributes one
> step, and each step is already proved: Stacks 04IQ's comparison read through `Over.forget` and
> followed by the first projection is Stacks 00Y1's identification followed by the slice-site
> counit (`CategoryTheory.OverShriek.left_overPullbackCompSheafFunctorToOverIso_hom_app_comp_fst`);
> and Stacks 04IE's comparison carries the projection to the localization counit
> (`RingedTopos.forget_localizationInverseImageIso_inv_app`), whose right-hand side is that first
> projection.
>
> The step that replaces a factor *inside* the composite is taken by `rw` rather than by an
> explicit `congrArg`: a `congrArg` against a hand-written `fun z => z ≫ _` has to have its own
> spelling of the composite identified with the goal's, and that identification unfolds the body of
> `localizationShriekAdjunction` — the equation is the same, and the proof is five times the
> elaborator's budget. `rw` substitutes into the goal's own term, so no such identification
> arises.

```lean
theorem left_representableLocalizationForwardInverseImageIso_hom_app_comp_counit
    (A : Sheaf X.J (Type u)) :
    ((representableLocalizationForwardInverseImageIso X U).hom.app A).left ≫
        (X.ringedTopos.localizationShriekAdjunction (representableSheaf X U)).counit.app A =
      (CategoryTheory.OverShriek.sheafFunctorToOverForgetIso X.J).hom.app
          ((X.J.overPullback (Type u) U).obj A) ≫
        ((Over.forget U).sheafAdjunctionContinuous (Type u) (X.J.over U) X.J).counit.app A
```

**`AlgebraicGeometry.RingedSite.representableLocalizationInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableLocalization.lean, line 313](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableLocalization.lean#L313). The attribute's comment: “part (2): canonical comparison of inverse images”.

> **The canonical comparison of the two inverse images**: the inverse image of the
> localization at `h_U^#`, read through the identification of the two localized topoi, is the
> inverse image of the localization at `U`. This is the previous comparison transported across
> the unit of Stacks 00Y1's equivalence, so it is not an arbitrary isomorphism.

```lean
noncomputable def representableLocalizationInverseImageIso :
    (RingedTopos.localizationMorphism X.ringedTopos
          (representableSheaf X U)).toToposHom.inverseImage ⋙
        (representableLocalizationEquivalence X U).inverse ≅
      (X.localizationCommRingedToposHom U).toToposHom.inverseImage
```

**`AlgebraicGeometry.RingedSite.shriek_representableLocalizationInverseImageIso_hom_app_comp_counit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableLocalization.lean, line 390](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableLocalization.lean#L390). The attribute's comment: “part (2): the comparison of inverse images after the unit cancellation, read through the lower shriek”.

> **Stacks 04J3's comparison of inverse images, read through the lower shriek.** Applying
> `j_{U!}` to the comparison and following it by the counit of `j_{U!} ⊣ j_U^{-1}` is Stacks 00Y1's
> identification of `j_{U!}Phi_U^{-1}` with `Over.forget` followed by the counit of the lower
> shriek of the localization at `h_U^#`.
>
> This is the form of Stacks 04J3's comparison that an equation transposed across `j_{U!}`
> consumes: on one side of such an equation the lower shriek is the slice site's, on the other it
> is the localization's, and nothing but this lemma relates them. It is the comparison *after* the
> cancellation of Stacks 00Y1's unit, so it applies to
> `representableLocalizationInverseImageIso` itself rather than to the comparison in the slice
> direction that it is built from.
>
> The three steps are `shriek_sheafEquivalence_unitInv` for the cancelled unit, the naturality of
> `CategoryTheory.OverShriek.inverseCompShriekIso`, and
> `left_representableLocalizationForwardInverseImageIso_inv_app_comp_counit` for the comparison in
> the slice direction.
>
> The last of those is whiskered on by `CategoryTheory.whisker_eq` with the whiskering morphism left
> to unification: written as a `congrArg` against an explicit `fun z => _ ≫ z`, the step alone takes
> the whole of the elaborator's budget, because the lambda's spelling of the comparison has to be
> identified with the goal's and that unfolds the body of `localizationShriekAdjunction`.

```lean
theorem shriek_representableLocalizationInverseImageIso_hom_app_comp_counit
    (A : Sheaf X.J (Type u)) :
    ((Over.forget U).sheafPullback (Type u) (X.J.over U) X.J).map
          ((representableLocalizationInverseImageIso X U).hom.app A) ≫
        ((Over.forget U).sheafAdjunctionContinuous (Type u) (X.J.over U) X.J).counit.app A =
      (CategoryTheory.OverShriek.inverseCompShriekIso X.J).hom.app
          ((X.ringedTopos.localizationEquivalence (representableSheaf X U)).functor.obj
            ((X.ringedTopos.localizationMorphism
              (representableSheaf X U)).toToposHom.inverseImage.obj A)) ≫
        (X.ringedTopos.localizationShriekAdjunction (representableSheaf X U)).counit.app A
```

**`AlgebraicGeometry.RingedSite.representableLocalizationStructureSheafIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableLocalization.lean, line 485](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableLocalization.lean#L485). The attribute's comment: “part (1): canonical structure-sheaf comparison”.

> **The canonical comparison of the two structure sheaves.** Read through the identification
> of the two localized topoi, the structure sheaf of the localization at `h_U^#` is the structure
> sheaf `O|_U` of the localization at `U`: the inverse image of the former along the
> identification is the inverse image of `O` along the composite, which the lift above identifies
> with the inverse image of `O` along the localization at `U`, which is `O|_U`.

```lean
noncomputable def representableLocalizationStructureSheafIso :
    (inverseImageCommRingFunctor (representableLocalizationToposMorphism X U)).obj
        (RingedTopos.localizedRingedTopos X.ringedTopos (representableSheaf X U)).O ≅
      (X.over U).ringedTopos.O
```

**`AlgebraicGeometry.RingedSite.representableLocalizationRingInverseImageIso_existsUnique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableLocalization.lean, line 540](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableLocalization.lean#L540). The attribute's comment: “part (2): canonical comparison on ring sheaves”.

> **The comparison of inverse images lifts uniquely to sheaves of commutative rings.** For
> the composite of the localization at `h_U^#` with the identification of the two localized
> topoi, and for the localization at `U`, there is exactly one isomorphism of their inverse
> images of sheaves of commutative rings whose underlying map of sheaves of sets is the canonical
> comparison.

```lean
theorem representableLocalizationRingInverseImageIso_existsUnique :
    ∃! β : inverseImageCommRingFunctor.{u, u, u, u, u, u}
        ((RingedTopos.localizationMorphism X.ringedTopos (representableSheaf X U)).comp
          (representableLocalizationRingedMorphism X U)).toToposHom ≅
        inverseImageCommRingFunctor.{u, u, u, u, u, u}
          (X.localizationCommRingedToposHom U).toToposHom,
      ∀ R : Sheaf X.J CommRingCat.{u},
        (sheafCompose (X.J.over U) (forget CommRingCat.{u})).map (β.hom.app R) =
          (representableLocalizationInverseImageIso X U).hom.app
            ((sheafCompose X.J (forget CommRingCat.{u})).obj R)
```

**`AlgebraicGeometry.RingedSite.representableLocalizationMorphism_compare`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/StructureSheafComparison.lean, line 298](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/StructureSheafComparison.lean#L298). The attribute's comment: “part (2): compatibility of localization structure maps”.

> **The two localizations have the same structure map**, under the canonical comparison of
> their inverse images of sheaves of commutative rings. This is the last compatibility of Stacks
> 04J3: the identification of the two localized ringed topoi is compatible with their structure
> maps, so it is an identification of localizations and not merely of topoi.

```lean
theorem representableLocalizationMorphism_compare :
    (representableLocalizationRingInverseImageIso X U).inv.app X.O ≫
        ((RingedTopos.localizationMorphism X.ringedTopos (representableSheaf X U)).comp
          (representableLocalizationRingedMorphism X U)).fSharpInverseImage =
      (X.localizationCommRingedToposHom U).fSharpInverseImage
```

## Tag 04J4, a lemma

[Tag 04J4](https://stacks.math.columbia.edu/tag/04J4) in the Stacks Project.

**`Stacks.Sheaves.LocalizedRingedTopos.OverSite.elementPostcomp_isCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardRightExact.lean, line 595](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardRightExact.lean#L595). The attribute's comment: “cocontinuity of postcomposition”.

> **Stacks 04J4, cocontinuity of postcomposition.**

```lean
public theorem elementPostcomp_isCocontinuous (s : G ⟶ F) :
    (elementPostcomp s).IsCocontinuous (elementTopology G) (elementTopology F)
```

**`Stacks.Sheaves.LocalizedRingedTopos.OverSite.elementPostcomp_isContinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardRightExact.lean, line 639](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardRightExact.lean#L639). The attribute's comment: “continuity of postcomposition”.

> **Stacks 04J4, continuity of postcomposition.**

```lean
public theorem elementPostcomp_isContinuous (s : G ⟶ F) :
    (elementPostcomp s).IsContinuous (elementTopology G) (elementTopology F)
```

**`Stacks.Sheaves.LocalizedRingedTopos.elementPostcomp_isCocontinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardRightExact.lean, line 730](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardRightExact.lean#L730). The attribute's comment: “cocontinuity of postcomposition”.

> **Stacks 04J4, cocontinuity of postcomposition.** The tag is registered on
> `OverSite.elementPostcomp_isCocontinuous`, which states the same thing over a bare site.

```lean
public theorem elementPostcomp_isCocontinuous (s : G ⟶ F) :
    (elementPostcomp s).IsCocontinuous (elementTopology X G) (elementTopology X F)
```

**`Stacks.Sheaves.LocalizedRingedTopos.elementPostcomp_isContinuous`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardRightExact.lean, line 747](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PushforwardRightExact.lean#L747). The attribute's comment: “continuity of postcomposition”.

> **Stacks 04J4, continuity of postcomposition.** The tag is registered on
> `OverSite.elementPostcomp_isContinuous`, which states the same thing over a bare site.

```lean
public theorem elementPostcomp_isContinuous (s : G ⟶ F) :
    (elementPostcomp s).IsContinuous (elementTopology X G) (elementTopology X F)
```

**`CategoryTheory.Functor.preservesFiniteLimits_sheafPushforwardContinuous`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Relocalization.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/Relocalization.lean#L90). The attribute's comment: “left exactness of relocalization”. References: SGA 4 III (1.8), “partial”; SGA 4½ Arcata (2.3.3), “more general”; SGA 7 VI (3.1(a)), “partial”.

> **Stacks 04J4**, left exactness of relocalization: restriction of sheaves along a
> continuous functor of sites is left exact. For the relocalization of a topos at a morphism of
> sheaves `G ⟶ F` the continuous functor is postcomposition with that morphism on the sites of
> elements, and this is the left exactness that makes the relocalization a morphism of topoi.

```lean
noncomputable instance preservesFiniteLimits_sheafPushforwardContinuous [HasFiniteLimits A] :
    PreservesFiniteLimits (F.sheafPushforwardContinuous A J K)
```

**`Stacks.Sheaves.LocalizedRingedTopos.relocalizationToposMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RelocalizationRingedTopos.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RelocalizationRingedTopos.lean#L137). The attribute's comment: “the relocalization geometric morphism”.

> **Stacks 04J4**, the geometric morphism of the relocalization. A morphism of sheaves
> `s : G ⟶ F` postcomposes sections, giving a functor between the sites of elements which is
> continuous and cocontinuous and whose restriction functor is left exact; those three facts are
> exactly the data of a morphism of topoi `Sh(C/G) ⟶ Sh(C/F)`.

```lean
noncomputable def relocalizationToposMorphism (s : G ⟶ F) :
    MorphismOfTopoi (localizedRingedTopos X G).Topos (localizedRingedTopos X F).Topos
```

**`Stacks.Sheaves.LocalizedRingedTopos.comp_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RelocalizationRingedTopos.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RelocalizationRingedTopos.lean#L153). The attribute's comment: “the relocalization triangle of topoi, on inverse images”.

> **Stacks 04J4**, the inverse-image half of the relocalization triangle: localizing at `F`
> and then relocalizing along `s : G ⟶ F` has the same inverse image as localizing at `G`
> directly, on the nose. Postcomposition with `s` leaves the underlying object of the site
> unchanged, so the two functors of sites to `C` are equal, and restriction along a composite is
> the composite of the restrictions.

```lean
theorem comp_inverseImage (s : G ⟶ F) :
    ((localizationToposMorphism X F).comp (relocalizationToposMorphism s)).inverseImage =
      (localizationToposMorphism X G).inverseImage
```

**`Stacks.Sheaves.LocalizedRingedTopos.relocalizationRingIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RelocalizationRingedTopos.lean, line 197](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RelocalizationRingedTopos.lean#L197). The attribute's comment: “identification of the localized structure sheaves”.

> **Stacks 04J4**, the identification of the localized structure sheaves: restricting the
> structure sheaf of the localization at `F` along postcomposition with `s : G ⟶ F` gives the
> structure sheaf of the localization at `G`. Both are the restriction of `O` along a projection
> from a site of elements and the two projections agree, so the identification is the identity
> isomorphism.

```lean
noncomputable def relocalizationRingIso (s : G ⟶ F) :
    (relocalizationRingInverseImage s).obj (localizedRingedTopos X F).O ≅
      (localizedRingedTopos X G).O
```

**`Stacks.Sheaves.LocalizedRingedTopos.relocalizationRingAdjunction_homEquiv_symm_fSharp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RelocalizationRingedTopos.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RelocalizationRingedTopos.lean#L214). The attribute's comment: “canonical structure-sheaf map”.

> **Stacks 04J4**, the canonical structure-sheaf map: the structure map of the relocalization
> morphism, read in its inverse-image form `f⁻¹O_F ⟶ O_G` through the ring-level adjunction, is
> the canonical identification of the restriction of `O_F` with `O_G`.

```lean
theorem relocalizationRingAdjunction_homEquiv_symm_fSharp (s : G ⟶ F) :
    ((relocalizationRingAdjunction s).homEquiv _ _).symm (relocalizationFSharp s) =
      (relocalizationRingIso s).hom
```

**`Stacks.Sheaves.LocalizedRingedTopos.relocalization_inverseImage_unique`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RelocalizationSliceComparison.lean, line 200](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RelocalizationSliceComparison.lean#L200). The attribute's comment: “uniqueness of the comparison with base change on slice topoi”.

> **Stacks 04J4**, the uniqueness half of the identification of the relocalization inverse image
> with base change. Fix an identification `eF` of the localization of `X` at `F` with the slice topos
> `Sh(C)/F` whose composite with `Over.forget F` is the lower shriek, i.e. is left adjoint to the
> inverse image of the localization morphism (the canonical such identification is
> `sliceEquivalence`, with `shriekAdjunction`). Then two isomorphisms of a functor `P` with
> `eF ⋙ (base change along s)` which agree after whiskering with the inverse image of the
> localization at `F` are equal.
>
> `P` is arbitrary; the case of interest is `P = (relocalization inverse image) ⋙ eG`, for an
> identification `eG` of the localization at `G` with `Sh(C)/G`. The hypothesis on `eF` is used only
> through the faithfulness of the lower shriek.

```lean
theorem relocalization_inverseImage_unique (s : G ⟶ F)
    {eF : (localizedRingedTopos X F).Topos ≌ Over F}
    (adjF : eF.functor ⋙ Over.forget F ⊣ (localizationToposMorphism X F).inverseImage)
    {P : (localizedRingedTopos X F).Topos ⥤ Over G}
    {γ γ' : P ≅ eF.functor ⋙ Over.pullback s}
    (h : Functor.isoWhiskerLeft (localizationToposMorphism X F).inverseImage γ
      = Functor.isoWhiskerLeft (localizationToposMorphism X F).inverseImage γ') :
    γ = γ'
```

**`Stacks.Sheaves.LocalizedRingedTopos.relocalization_inverseImage_unique_of_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RelocalizationSliceComparison.lean, line 216](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RelocalizationSliceComparison.lean#L216). The attribute's comment: “the comparison with base change is pinned down by the localization comparisons”.

> **Stacks 04J4**, the uniqueness half in the shape of the source's `∃!`: a comparison of the
> relocalization inverse image with base change is determined by a compatibility equation with the
> localization comparisons. Here `Φ` is the isomorphism against which the compatibility is stated
> and `Ψ` is the prescribed value; both are arbitrary, so this covers any choice of the comparison
> isomorphisms for the localizations at `F` and at `G`.

```lean
theorem relocalization_inverseImage_unique_of_eq (s : G ⟶ F)
    {eF : (localizedRingedTopos X F).Topos ≌ Over F}
    (adjF : eF.functor ⋙ Over.forget F ⊣ (localizationToposMorphism X F).inverseImage)
    {P : (localizedRingedTopos X F).Topos ⥤ Over G} {R : X.Topos ⥤ Over G}
    (Φ : (localizationToposMorphism X F).inverseImage ⋙ (eF.functor ⋙ Over.pullback s) ≅ R)
    (Ψ : (localizationToposMorphism X F).inverseImage ⋙ P ≅ R)
    {γ γ' : P ≅ eF.functor ⋙ Over.pullback s}
    (hγ : Functor.isoWhiskerLeft (localizationToposMorphism X F).inverseImage γ ≪≫ Φ = Ψ)
    (hγ' : Functor.isoWhiskerLeft (localizationToposMorphism X F).inverseImage γ' ≪≫ Φ = Ψ) :
    γ = γ'
```

**`AlgebraicGeometry.RingedTopos.relocalizationMorphism`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Recovery04IH/ToposRelocalization.lean, line 177](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Recovery04IH/ToposRelocalization.lean#L177). The attribute's comment: “the upper edge `(j, j♯)` of the relocalization triangle”.

> **Stacks 04J4.** The relocalization morphism of ringed topoi attached to a morphism
> `s : G ⟶ F` of sheaves on a ringed topos: the morphism of topoi is restriction along
> postcomposition of sections, and the structure map is the canonical identification of the
> inverse image of the structure sheaf of the localization at `F` with that of the localization
> at `G`.

```lean
noncomputable def relocalizationMorphism (s : G ⟶ F) :
    RingedToposHom (localizedRingedTopos X G) (localizedRingedTopos X F)
```

**`AlgebraicGeometry.RingedTopos.relocalizationInverseImageSliceIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizationBaseChange.lean, line 390](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizationBaseChange.lean#L390). The attribute's comment: “the inverse image of the relocalization is base change on slice topoi”.

> **Stacks 04J4.** The inverse image of the relocalization morphism along a morphism
> `a : H ⟶ K` of sheaves of sets, read through Stacks 04IE's identifications of the localization
> of `X` at `H` and at `K` with the slice topoi `Sh(C)/H` and `Sh(C)/K`, is base change along
> `a`.
>
> This is `relocalizationFibreIso` transported across the two equivalences.

```lean
noncomputable def relocalizationInverseImageSliceIso (a : H ⟶ K) :
    (X.relocalizationMorphism a).toToposHom.inverseImage ⋙
        (localizationEquivalence X H).functor ≅
      (localizationEquivalence X K).functor ⋙ Over.pullback a
```

**`AlgebraicGeometry.RingedTopos.localizationInverseImageIso_eq_relocalization`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizationBaseChange.lean, line 538](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizationBaseChange.lean#L538). The attribute's comment: “the comparison with base change is the one the localization comparisons of 04IE prescribe”.

> **Stacks 04J4: the comparison with base change is the one the localization comparisons
> prescribe.** Stacks 04IE identifies the inverse image of the localization at `H` with
> `toOver H`; that identification is `localizationInverseImageIso X H`, and this says it is the
> comparison with base change along `a`, whiskered with the inverse image of the localization at
> `K`, followed by Stacks 04IE at `K` and by the identification
> `toOver K ⋙ Over.pullback a ≅ toOver H` of Stacks 03EH.
>
> With `Stacks.Sheaves.LocalizedRingedTopos.relocalization_inverseImage_unique` this is the full
> `∃!` of the source: uniqueness holds for every choice of the two identifications, and here is the
> one solution for the canonical choice. The proof is
> `localizationInverseImageIso_eq` — the comparison is determined by its lower shriek counits —
> fed with `forget_map_relocalizationInverseImageSliceIso_hom_app` for the relocalization half,
> `CategoryTheory.forget_map_toOverCompPullbackIso_hom_app` for the Stacks 03EH half, and
> `localizationInverseImageIso`'s own counit description at `K`.

```lean
theorem localizationInverseImageIso_eq_relocalization (a : H ⟶ K) :
    localizationInverseImageIso X H =
      Functor.isoWhiskerLeft (X.localizationMorphism K).toToposHom.inverseImage
          (X.relocalizationInverseImageSliceIso a) ≪≫
        Functor.isoWhiskerRight (localizationInverseImageIso X K) (Over.pullback a) ≪≫
          toOverCompPullbackIso a
```

**`AlgebraicGeometry.RingedTopos.localizationAtRelocalizationObjectInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizationObject.lean, line 141](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizationObject.lean#L141). The attribute's comment: “the localization at `G/F` has base change along `s` as its inverse image”. References: SGA 4 IV (5.2).

> **The inverse image of the localization at `G/F`.** Read through the identification of
> Stacks 04IE of the localization of `X` at `F` with `Sh(C)/F`, and through the identification of
> the slice at `G/F` with `Sh(C)/G`, the inverse image of the localization morphism of
> `(Sh(C)/F, O_F)` at the object `G/F` is base change along `s`.
>
> This is Stacks 04IR for the slice topos `Sh(C)/F`: the inverse image of a localization at an
> object is the product with that object (`localizationInverseImageIso`), and the product with
> `G/F` is base change along `s` (`relocalizationStarIso`).

```lean
noncomputable def localizationAtRelocalizationObjectInverseImageIso (s : G ⟶ F) :
    (localizationMorphism (X.localizedRingedTopos F)
            (X.relocalizationObject s)).toToposHom.inverseImage ⋙
        ((localizationEquivalence (X.localizedRingedTopos F)
            (X.relocalizationObject s)).functor ⋙
          (X.relocalizationSliceEquivalence s).functor) ≅
      (localizationEquivalence X F).functor ⋙ Over.pullback s
```

**`AlgebraicGeometry.RingedTopos.relocalizationObjectTriangleInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizationObject.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizationObject.lean#L173). The attribute's comment: “the triangle whose upper edge is the localization at `G/F` commutes on inverse images”.

> The relocalization triangle with the localization at `G/F` as its upper edge, on inverse
> images: the composite of the localization of `(Sh(C)/F, O_F)` at the object
> `G/F` with the localization morphism `j_F`, read through `relocalizationObjectEquivalence`, is
> the localization morphism `j_G`.
>
> The inverse image of `j_F` is the product with `F` and that of `j_G` the product with `G`, both
> by Stacks 04IE; the inverse image of the localization at `G/F` is base change along `s`; and the
> product with `F` followed by base change along `s` is the product with `G`.

```lean
noncomputable def relocalizationObjectTriangleInverseImageIso (s : G ⟶ F) :
    ((X.localizationMorphism F).comp
          (localizationMorphism (X.localizedRingedTopos F)
            (X.relocalizationObject s))).toToposHom.inverseImage ⋙
        (X.relocalizationObjectEquivalence s).functor ≅
      (X.localizationMorphism G).toToposHom.inverseImage
```

**`AlgebraicGeometry.RingedTopos.relocalizationObjectTriangle_fSharpInverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizationObject.lean, line 199](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizationObject.lean#L199). The attribute's comment: “the triangle commutes on structure maps, both of them being the identity”.

> The relocalization triangle with the localization at `G/F` as its upper edge, on structure
> maps: both edges from the localization at `G/F` to `X` have the identity as
> their structure map on underlying sheaves of sets, so the triangle commutes as a triangle of
> *ringed* topoi and not merely of topoi.
>
> Each of the three localization morphisms in the triangle has the identity as its structure map
> on underlying sheaves of sets, and the structure map of a composite is the restriction of the
> first factor's followed by the second factor's.

```lean
theorem relocalizationObjectTriangle_fSharpInverseImage (s : G ⟶ F) :
    ((X.localizedRingedTopos F).localizedRingedTopos
          (X.relocalizationObject s)).forgetRing.map
        ((X.localizationMorphism F).comp (localizationMorphism (X.localizedRingedTopos F)
          (X.relocalizationObject s))).fSharpInverseImage =
      𝟙 (((X.localizedRingedTopos F).localizedRingedTopos
            (X.relocalizationObject s)).forgetRing.obj
          ((X.localizedRingedTopos F).localizedRingedTopos (X.relocalizationObject s)).O) ∧
      (X.localizedRingedTopos G).forgetRing.map (X.localizationMorphism G).fSharpInverseImage =
        𝟙 ((X.localizedRingedTopos G).forgetRing.obj (X.localizedRingedTopos G).O)
```

**`AlgebraicGeometry.RingedTopos.relocalizationObjectInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizationObject.lean, line 237](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizationObject.lean#L237). The attribute's comment: “the localization at `G/F` and the relocalization have the same inverse image”.

> **The two relocalizations have the same inverse image.** Read through
> `relocalizationObjectEquivalence`, the inverse image of the localization of `(Sh(C)/F, O_F)` at
> the object `G/F` is the inverse image of the relocalization morphism along `s`.
>
> Both are base change along `s` on slice topoi — the first by
> `localizationAtRelocalizationObjectInverseImageIso`, the second by
> `relocalizationInverseImageSliceIso` — so the two agree once the equivalence at `G` is
> cancelled.

```lean
noncomputable def relocalizationObjectInverseImageIso (s : G ⟶ F) :
    (localizationMorphism (X.localizedRingedTopos F)
          (X.relocalizationObject s)).toToposHom.inverseImage ⋙
        (X.relocalizationObjectEquivalence s).functor ≅
      (X.relocalizationMorphism s).toToposHom.inverseImage
```

**`AlgebraicGeometry.RingedToposHom.toposRelocalizationTriangle`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizedMorphismComparison.lean, line 463](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizedMorphismComparison.lean#L463). The attribute's comment: “the relocalization triangle commutes as a triangle of ringed topoi”.

> **Stacks 04J4**, commutativity of the relocalization triangle as a triangle of ringed topoi:
> `(j_G, j_G♯)` is `(j_F, j_F♯)` composed with the relocalization `(j, j♯)` along `s`.
>
> The two inverse images are equal on the nose — restriction along postcomposition followed by
> restriction along the projection from the site of elements of `F` is restriction along the
> projection from the site of elements of `G` — and all three structure maps are identities on
> underlying sheaves of sets, so there is nothing left to check.

```lean
noncomputable def toposRelocalizationTriangle (W : RingedTopos.{u, u, u}) {H K : W.Topos}
    (a : H ⟶ K) :
    TwoIso (A := W.localizedRingedTopos H) (B := W)
      (W.localizationMorphism H)
      (comp (X := W.localizedRingedTopos H) (Y := W.localizedRingedTopos K) (Z := W)
        (W.localizationMorphism K) (W.relocalizationMorphism a))
```

**`AlgebraicGeometry.RingedToposHom.relocalizationCompTwoIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizedNaturalitySquare.lean, line 105](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizedNaturalitySquare.lean#L105). The attribute's comment: “the relocalization morphisms of ringed topoi compose”.

> **Stacks 04J4: the relocalization morphisms of ringed topoi compose.** Relocalizing along
> `s : F ⟶ H` after relocalizing along `a : F' ⟶ F` is relocalizing along `a ≫ s`.

```lean
noncomputable def relocalizationCompTwoIso (W : RingedTopos.{u, u, u}) {F' F H : W.Topos}
    (a : F' ⟶ F) (s : F ⟶ H) :
    TwoIso (A := W.localizedRingedTopos F') (B := W.localizedRingedTopos H)
      (comp (X := W.localizedRingedTopos F') (Y := W.localizedRingedTopos F)
        (Z := W.localizedRingedTopos H) (W.relocalizationMorphism s) (W.relocalizationMorphism a))
      (W.relocalizationMorphism (a ≫ s))
```

**`AlgebraicGeometry.RingedToposHom.relocalizationSquareTwoIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizedNaturalitySquare.lean, line 139](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RelocalizedNaturalitySquare.lean#L139). The attribute's comment: “a commuting square of sheaves gives a commuting square of relocalization morphisms of ringed topoi”.

> **Stacks 04J4: a commuting square of sheaves gives a commuting square of relocalizations.** For
> `a ≫ s = s' ≫ c`, relocalizing along `s'` and then along `c` agrees with relocalizing along `a` and
> then along `s`, as morphisms of ringed topoi.

```lean
noncomputable def relocalizationSquareTwoIso (W : RingedTopos.{u, u, u})
    {F' F H' H : W.Topos} (a : F' ⟶ F) (s : F ⟶ H) (s' : F' ⟶ H') (c : H' ⟶ H)
    (h : a ≫ s = s' ≫ c) :
    TwoIso (A := W.localizedRingedTopos F') (B := W.localizedRingedTopos H)
      (comp (X := W.localizedRingedTopos F') (Y := W.localizedRingedTopos H')
        (Z := W.localizedRingedTopos H) (W.relocalizationMorphism c)
        (W.relocalizationMorphism s'))
      (comp (X := W.localizedRingedTopos F') (Y := W.localizedRingedTopos F)
        (Z := W.localizedRingedTopos H) (W.relocalizationMorphism s)
        (W.relocalizationMorphism a))
```

## Tag 04J5, a lemma

[Tag 04J5](https://stacks.math.columbia.edu/tag/04J5) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.representableRelocalizationInverseImageIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableRelocalization.lean, line 194](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableRelocalization.lean#L194). The attribute's comment: “the two relocalizations have the same inverse image, via the identifications of 04J3”.

> **Stacks 04J5**, on inverse images. Read through the identification of Stacks 04J3 of
> `Sh(C/U)` with the localization of the ringed topos at `h_U^#`, and through the identification
> of the localization at `h_V^#/h_U^#` with `Sh(C/V)`, the inverse image of the localization of
> `(Sh(C)/h_U^#, O_{h_U^#})` at the object `h_V^#/h_U^#` is the inverse image of the
> relocalization of the ringed site along `f : V ⟶ U`.

```lean
noncomputable def representableRelocalizationInverseImageIso {U V : X.C} (f : V ⟶ U) :
    (X.representableLocalizationEquivalence U).functor ⋙
        (RingedTopos.localizationMorphism
            (RingedTopos.localizedRingedTopos X.ringedTopos (representableSheaf X U))
            (representableRelocalizationObject X f)).toToposHom.inverseImage ⋙
          (representableRelocalizationEquivalence X f).functor ≅
      (X.relocalizationRingedToposHom f).toToposHom.inverseImage
```

**`AlgebraicGeometry.RingedSite.representableRelocalizationPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableRelocalization.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableRelocalization.lean#L217). The attribute's comment: “the two relocalizations have the same direct image”.

> **Stacks 04J5**, on direct images. Read through the same two identifications, the direct
> image of the localization of `(Sh(C)/h_U^#, O_{h_U^#})` at `h_V^#/h_U^#` is the direct image of
> the relocalization of the ringed site along `f : V ⟶ U`. The two inverse images agree, so the
> two direct images agree by uniqueness of right adjoints.

```lean
noncomputable def representableRelocalizationPushforwardIso {U V : X.C} (f : V ⟶ U) :
    ((representableRelocalizationEquivalence X f).inverse ⋙
          (RingedTopos.localizationMorphism
            (RingedTopos.localizedRingedTopos X.ringedTopos (representableSheaf X U))
            (representableRelocalizationObject X f)).toToposHom.pushforward) ⋙
        (X.representableLocalizationEquivalence U).inverse ≅
      (X.relocalizationRingedToposHom f).toToposHom.pushforward
```

**`AlgebraicGeometry.RingedSite.representableRelocalization_fSharpSet`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableRelocalization.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableRelocalization.lean#L240). The attribute's comment: “the two maps j^sharp agree, both being the identity”.

> **Stacks 04J5**, on structure maps: the two relocalizations have the same structure map
> `j^♯`, both being the identity on underlying sheaves of sets. For the localization of the ringed
> topos at `h_V^#/h_U^#` the structure sheaf is the restriction of `O_{h_U^#}` along the
> projection from the site of elements, and for the relocalization of the ringed site it is the
> restriction of `O|_U` along `Over.map f`; in both cases the structure map is the comparison of
> an inverse image with that restriction, which is the identity on sections.

```lean
theorem representableRelocalization_fSharpSet {U V : X.C} (f : V ⟶ U) :
    RingedToposHom.fSharpSet
          (RingedTopos.localizationMorphism
            (RingedTopos.localizedRingedTopos X.ringedTopos (representableSheaf X U))
            (representableRelocalizationObject X f)) =
        𝟙 ((RingedTopos.localizationMorphism
              (RingedTopos.localizedRingedTopos X.ringedTopos (representableSheaf X U))
              (representableRelocalizationObject X f)).toToposHom.inverseImage.obj
            ((RingedTopos.localizedRingedTopos X.ringedTopos
              (representableSheaf X U)).forgetRing.obj
                (RingedTopos.localizedRingedTopos X.ringedTopos (representableSheaf X U)).O)) ∧
      RingedToposHom.fSharpSet (X.relocalizationRingedToposHom f) =
        𝟙 ((X.relocalizationRingedToposHom f).toToposHom.inverseImage.obj
          ((ringedTopos (X.over U)).forgetRing.obj (X.over U).O))
```

**`AlgebraicGeometry.RingedSite.representableRelocalizationTwoIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableRelocalizationRinged.lean, line 462](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableRelocalizationRinged.lean#L462). The attribute's comment: “the diagrams of 04IY and 04J4 agree via the identifications of 04J3, as a 2-isomorphism of morphisms of ringed topoi”.

> **The two upper edges agree**, as a 2-isomorphism of morphisms of ringed topoi: the
> localization of `(Sh(C)/h_U^#, O_{h_U^#})` at the object `h_V^#/h_U^#`, read through the
> identification of the localization at `h_V^#/h_U^#` with `Sh(C/V)`, *is* the relocalization of
> the ringed site along `f : V ⟶ U`, read through the identification of Stacks 04J3 at `U`.

```lean
noncomputable def representableRelocalizationTwoIso :
    TwoIso (A := ringedTopos (X.over V)) (B := representableLocalizedRingedTopos X U)
      (AlgebraicGeometry.RingedToposHom.comp (X := ringedTopos (X.over V))
        (Y := representableRelocalizedRingedTopos X f)
        (Z := representableLocalizedRingedTopos X U)
        (RingedTopos.localizationMorphism (representableLocalizedRingedTopos X U)
          (representableRelocalizationObject X f))
        (representableRelocalizationRingedMorphism X f))
      (AlgebraicGeometry.RingedToposHom.comp (X := ringedTopos (X.over V))
        (Y := ringedTopos (X.over U)) (Z := representableLocalizedRingedTopos X U)
        (representableLocalizationRingedMorphism X U) (X.relocalizationRingedToposHom f))
```

**`AlgebraicGeometry.RingedSite.representableRelocalizationTriangleCompare`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableRelocalizationRinged.lean, line 497](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/CategoryTheory/Sites/Modules/Localization/RepresentableRelocalizationRinged.lean#L497). The attribute's comment: “the triangle of 04J4 at a representable is the triangle of 04IY, via the identifications of 04J3”.

> **The two relocalization triangles agree**: the relocalization triangle of Stacks 04J4 at the
> morphism `h_f^# : h_V^# ⟶ h_U^#` of representable sheaves, read through the identifications of
> Stacks 04J3 at `U` and the identification of the localization at `h_V^#/h_U^#` with `Sh(C/V)`,
> *is* the relocalization triangle of Stacks 04IY along `f : V ⟶ U`.

```lean
noncomputable def representableRelocalizationTriangleCompare :
    TwoIso (A := ringedTopos (X.over V)) (B := ringedTopos X)
      (AlgebraicGeometry.RingedToposHom.comp (X := ringedTopos (X.over V))
        (Y := representableLocalizedRingedTopos X U) (Z := ringedTopos X)
        (RingedTopos.localizationMorphism X.ringedTopos (representableSheaf X U))
        (AlgebraicGeometry.RingedToposHom.comp (X := ringedTopos (X.over V))
          (Y := representableRelocalizedRingedTopos X f)
          (Z := representableLocalizedRingedTopos X U)
          (RingedTopos.localizationMorphism (representableLocalizedRingedTopos X U)
            (representableRelocalizationObject X f))
          (representableRelocalizationRingedMorphism X f)))
      (X.localizationRingedToposHom V)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.21, Tag 04ID](https://stacks.math.columbia.edu/tag/04ID)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
