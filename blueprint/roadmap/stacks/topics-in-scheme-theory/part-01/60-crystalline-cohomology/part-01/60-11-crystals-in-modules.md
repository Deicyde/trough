---
declaration: section
origin: cited
lean: Crystalline.GlobalCrystallineSituation.IsLocallyQuasiCoherent, Crystalline.GlobalCrystallineSituation.SmallSite.IsLocallyQuasiCoherent, Crystalline.GlobalCrystallineSituation.IsSheafCrystal, Crystalline.GlobalCrystallineSituation.SmallSite.IsSheafCrystal, SheafOfModules.IsQuasicoherentOnSite, Crystalline.GlobalCrystallineSituation.isSheafCrystal_of_isQuasicoherentOnSite, Crystalline.GlobalCrystallineSituation.isLocallyQuasiCoherent_of_isQuasicoherentOnSite, Crystalline.GlobalCrystallineSituation.isQuasicoherentOnSite_of_isLocallyQuasiCoherent
statement: formalized
proof: formalized
---

# 60.11 Crystals in modules

Section 60.11 of the Stacks Project, [Tag 07IR](https://stacks.math.columbia.edu/tag/07IR). 3 tags here are carried by 14 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 07IS, a definition

[Tag 07IS](https://stacks.math.columbia.edu/tag/07IS) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.IsLocallyQuasiCoherent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/LocallyQuasicoherent.lean, line 88](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/LocallyQuasicoherent.lean#L88). The attribute's comment: “part (1): locally quasi-coherent, on the big site CRIS(X/S)”.

> A sheaf of `𝒪_{X/S}`-modules on the big crystalline site is *locally quasi-coherent* when
> for every object `(U, T, δ)` the restriction `F_T` is a quasi-coherent `𝒪_T`-module.

```lean
def IsLocallyQuasiCoherent (M : SheafOfModules.{u} (crystallineStructureSheaf S)) : Prop
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.IsLocallyQuasiCoherent`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/LocallyQuasicoherent.lean, line 104](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/LocallyQuasicoherent.lean#L104). The attribute's comment: “part (1): locally quasi-coherent, on the small site Cris(X/S)”.

> A sheaf of `𝒪_{X/S}`-modules on the small crystalline site is *locally quasi-coherent* when
> for every object `(U, T, δ)` of `Cris(X/S)` the restriction `F_T` is a quasi-coherent
> `𝒪_T`-module. The restriction is the pushforward of `F` along the restrictions of the object to
> the opens of its ambient scheme, lifted to `Cris(X/S)`; it is a module over the restriction of the
> structure sheaf of the big crystalline site to the ambient scheme of the underlying object.

```lean
def IsLocallyQuasiCoherent (M : SheafOfModules.{u} (structureSheaf S)) : Prop
```

**`Crystalline.GlobalCrystallineSituation.IsSheafCrystal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/SheafCrystal.lean, line 294](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/SheafCrystal.lean#L294). The attribute's comment: “part (3): crystal in modules on the big site CRIS(X/S), with the comparison maps of sheaves of modules”.

> **Stacks Project, Tag 07IS.**  A sheaf of `𝒪_{X/S}`-modules on the big crystalline site is a
> *crystal in `𝒪_{X/S}`-modules* when for every morphism `f : (U, T, δ) ⟶ (U', T', δ')` of the site
> the comparison map `c_f : f^* F_{T'} ⟶ F_T` of *sheaves* of `𝒪_T`-modules is an isomorphism.
>
> This is the sheaf-level reading of the condition, the pullback being the pullback of sheaves of
> modules, that is, the sheafification of the pullback of presheaves of modules.  It is the reading
> the source intends and it is weaker than the presheaf-level condition
> `Crystalline.GlobalCrystallineSituation.IsCrystal`; see the correction described in the module
> documentation.

```lean
def IsSheafCrystal {S : GlobalCrystallineSituation.{u}}
    (M : SheafOfModules.{u} (crystallineStructureSheaf S)) : Prop
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.IsSheafCrystal`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/SheafCrystal.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/SheafCrystal.lean#L219). The attribute's comment: “part (3): crystal in modules on the small site Cris(X/S), with the comparison maps of sheaves”.

> **Stacks Project, Tag 07IS, part (3) for `𝒞 = Cris(X/S)`.**  A sheaf of `𝒪_{X/S}`-modules on
> the small crystalline site is a *crystal in `𝒪_{X/S}`-modules* when for every morphism
> `f : (U, T, δ) ⟶ (U', T', δ')` of `Cris(X/S)` the comparison map `c_f : f^* F_{T'} ⟶ F_T` of
> *sheaves* of `𝒪_T`-modules is an isomorphism.
>
> This is the sheaf-level reading of the condition, the pullback being the pullback of sheaves of
> modules, that is, the sheafification of the pullback of presheaves of modules.  It is the reading
> the source intends and it is weaker than the condition read with the comparison maps of presheaves
> of modules.  The same clause for the big crystalline site is
> `Crystalline.GlobalCrystallineSituation.IsSheafCrystal`.

```lean
def IsSheafCrystal {S : GlobalCrystallineSituation.{u}}
    (M : SheafOfModules.{u} (structureSheaf S)) : Prop
```

Declarations registered for the tag:

- [`SheafOfModules.IsQuasicoherentOnSite`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/QuasicoherentOnSite.lean#L99), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/Basic.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/Basic.lean#L34) (StacksFrontier): “part (2): quasi-coherent, on either crystalline site”.

## Tag 07IT, a lemma

[Tag 07IT](https://stacks.math.columbia.edu/tag/07IT) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.isSheafCrystal_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/QuasicoherentCrystal.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/QuasicoherentCrystal.lean#L405). The attribute's comment: “the implication (1) ⇒ (2)(b) on the big site CRIS(X/S): a quasi-coherent sheaf of 𝒪\_\{X/S}-modules is a crystal in 𝒪\_\{X/S}-modules, the crystal condition being read with the comparison maps of sheaves of modules. The same implication on the small site Cris(X/S), and the implication (1) ⇒ (2)(a) on each of the two sites, carry this tag separately. The converse (2) ⇒ (1) is a separate statement”.

> **Stacks Project, Tag 07IT, the implication (1) ⇒ (2)(b): a quasi-coherent sheaf of
> `𝒪_{X/S}`-modules on the big crystalline site is a crystal in `𝒪_{X/S}`-modules.**
>
> For a morphism `f : (U, T, δ) ⟶ (U', T', δ')` the comparison map `c_f : f^* F_{T'} ⟶ F_T` of
> sheaves of `𝒪_T`-modules is an isomorphism.  This is the source's argument, with its opening
> reduction "it suffices to prove (a) and (b) Zariski locally" carried out: quasi-coherence gives,
> around every point of `T'`, an open `V` on whose restriction `(U' ∩ V, V, δ'|_V)` the module has a
> global presentation, the restrictions of `f` over those opens cover `T`, and over each of them the
> source's computation applies on the localised site `CRIS(X/S)/(U' ∩ V, V, δ'|_V)`, by
> `Thickening.isIso_moduleComparisonSheaf_of_hasGlobalPresentation_target`.
> The comparison maps of the structure morphisms of the two restrictions are isomorphisms, those
> morphisms being Cartesian open immersions, so the `f`-map cocycle
> (`Crystalline.GlobalCrystallineSituation.Thickening.fmapComp_comp`) transfers bijectivity of the
> `f`-map composition to the direct images from the members of the cover, and invertibility of
> `c_f` follows because it is Zariski-local on `T`.

```lean
theorem isSheafCrystal_of_isQuasicoherentOnSite
    (M : SheafOfModules.{u} (crystallineStructureSheaf S)) (hM : M.IsQuasicoherentOnSite) :
    IsSheafCrystal M
```

**`Crystalline.GlobalCrystallineSituation.isLocallyQuasiCoherent_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/QuasicoherentImpliesLocal.lean, line 489](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/QuasicoherentImpliesLocal.lean#L489). The attribute's comment: “the implication (1) ⇒ (2)(a) on the big site CRIS(X/S): quasi-coherent implies locally quasi-coherent. The same implication on the small site Cris(X/S), and the other half (1) ⇒ (2)(b) that a quasi-coherent module is a crystal, on each of the two sites, carry this tag separately. The converse (2) ⇒ (1) is a separate statement”.

> **Stacks Project, Tag 07IT, the implication (1) ⇒ (2)(a): a quasi-coherent sheaf of
> `𝒪_{X/S}`-modules on the big crystalline site is locally quasi-coherent.**
>
> Quasi-coherence gives, around every point of the ambient scheme `T` of every object `(U, T, δ)`,
> an open `V` on whose restriction `(U ∩ V, V, δ|_V)` the module has a global presentation
> (`Crystalline.GlobalCrystallineSituation.exists_hasGlobalPresentation_restrictOpen`, which is
> cocontinuity of the restriction functor).  Intersecting `V` with a given open `W` of `T` makes
> those opens into an open cover of `W`, and each presentation restricts to one of `F_T` on the
> Zariski site localised at `V ⊓ W` by
> `Crystalline.GlobalCrystallineSituation.hasGlobalPresentation_moduleRestrictionSheaf_over`; that
> is quasi-coherence of `F_T` over `W`.
>
> This is one of the two halves of the implication (1) ⇒ (2) of the tag, on this site; the other
> half, that a quasi-coherent module is a crystal, is
> `Crystalline.GlobalCrystallineSituation.isSheafCrystal_of_isQuasicoherentOnSite` of
> `StacksFrontier.AlgebraicGeometry.Crystalline.CrystalsModules.QuasicoherentCrystal`.  The same
> implication for `𝒞 = Cris(X/S)`, the other site the tag is stated for, is
> `Crystalline.GlobalCrystallineSituation.SmallSite.isLocallyQuasiCoherent_of_isQuasicoherentOnSite`
> of `StacksFrontier.AlgebraicGeometry.Crystalline.SmallSite.QuasicoherentImpliesLocal`.

```lean
theorem isLocallyQuasiCoherent_of_isQuasicoherentOnSite
    (M : SheafOfModules.{u} (crystallineStructureSheaf S)) (hM : M.IsQuasicoherentOnSite) :
    IsLocallyQuasiCoherent M
```

**`Crystalline.GlobalCrystallineSituation.isQuasicoherentOnSite_of_isLocallyQuasiCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/QuasicoherentOfCrystal.lean, line 352](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/QuasicoherentOfCrystal.lean#L352). The attribute's comment: “the implication (2) ⇒ (1) on the big site CRIS(X/S): a sheaf of 𝒪\_\{X/S}-modules whose restrictions F\_T are all quasi-coherent and which is a crystal in 𝒪\_\{X/S}-modules is quasi-coherent on the site”.

> **The implication (2) ⇒ (1) of [Stacks, Tag 07IT] on the big crystalline site `CRIS(X/S)`: a
> locally quasi-coherent sheaf of `𝒪_{X/S}`-modules which is a crystal in `𝒪_{X/S}`-modules is
> quasi-coherent on the site.**
>
> Quasi-coherence is Zariski-local on the ambient scheme of each object
> (`Crystalline.GlobalCrystallineSituation.isQuasicoherentOnSite_of_forall_isAffine`), so it is
> enough to present `F` globally on the localisation of `CRIS(X/S)` at an object whose ambient scheme
> is affine, which is
> `Crystalline.GlobalCrystallineSituation.hasGlobalPresentation_over_of_isAffine`.
>
> The crystal condition is read at sheaf level, as
> `Crystalline.GlobalCrystallineSituation.IsSheafCrystal`; that is the reading under which the tag
> holds, and the two hypotheses are exactly the source's conditions (a) and (b).

```lean
theorem isQuasicoherentOnSite_of_isLocallyQuasiCoherent
    {M : SheafOfModules.{u} (crystallineStructureSheaf S)} (hlqc : IsLocallyQuasiCoherent M)
    (hcrys : IsSheafCrystal M) : M.IsQuasicoherentOnSite
```

**`Crystalline.GlobalCrystallineSituation.isQuasicoherentOnSite_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/QuasicoherentOfCrystal.lean, line 371](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/QuasicoherentOfCrystal.lean#L371). The attribute's comment: “the equivalence on the big site CRIS(X/S), with the crystal condition read with the comparison maps of sheaves of modules”.

> **[Stacks, Tag 07IT] on the big crystalline site `CRIS(X/S)`:** a sheaf of
> `𝒪_{X/S}`-modules is quasi-coherent on the site if and only if all its restrictions `F_T` are
> quasi-coherent `𝒪_T`-modules and it is a crystal in `𝒪_{X/S}`-modules.
>
> The two halves of the forward implication are
> `Crystalline.GlobalCrystallineSituation.isLocallyQuasiCoherent_of_isQuasicoherentOnSite` and
> `Crystalline.GlobalCrystallineSituation.isSheafCrystal_of_isQuasicoherentOnSite`; the converse is
> `Crystalline.GlobalCrystallineSituation.isQuasicoherentOnSite_of_isLocallyQuasiCoherent`.  The
> crystal condition is read at sheaf level, which is the reading under which the tag holds; see the
> module documentation.

```lean
theorem isQuasicoherentOnSite_iff (M : SheafOfModules.{u} (crystallineStructureSheaf S)) :
    M.IsQuasicoherentOnSite ↔ IsLocallyQuasiCoherent M ∧ IsSheafCrystal M
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.isSheafCrystal_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/QuasicoherentCrystal.lean, line 497](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/QuasicoherentCrystal.lean#L497). The attribute's comment: “the implication (1) ⇒ (2)(b) on the small site Cris(X/S): a quasi-coherent sheaf of 𝒪\_\{X/S}-modules is a crystal in 𝒪\_\{X/S}-modules, the crystal condition being read with the comparison maps of sheaves of modules. The same implication on the big site CRIS(X/S), and the implication (1) ⇒ (2)(a) on each of the two sites, carry this tag separately. The converse (2) ⇒ (1) is a separate statement”.

> **Stacks Project, Tag 07IT, the implication (1) ⇒ (2)(b): a quasi-coherent sheaf of
> `𝒪_{X/S}`-modules on the small crystalline site is a crystal in `𝒪_{X/S}`-modules.**
>
> For a morphism `f : (U, T, δ) ⟶ (U', T', δ')` of `Cris(X/S)` the comparison map
> `c_f : f^* F_{T'} ⟶ F_T` of sheaves of `𝒪_T`-modules is an isomorphism.  This is the source's
> argument, with its opening reduction "it suffices to prove (a) and (b) Zariski locally" carried
> out: quasi-coherence gives, around every point of `T'`, an open `V` on whose restriction
> `(U' ∩ V, V, δ'|_V)` the module has a global presentation
> (`Crystalline.GlobalCrystallineSituation.SmallSite.exists_hasGlobalPresentation_restrictOpen`), the
> restrictions of `f` over those opens cover `T`, and over each of them the source's computation
> applies on the localised site `Cris(X/S)/(U' ∩ V, V, δ'|_V)`, by
> `Crystalline.GlobalCrystallineSituation.SmallSite.CohomologyRestriction`
> `.isIso_moduleComparisonSheaf_of_hasGlobalPresentation_target`.  The comparison maps of the
> structure morphisms of the two restrictions are isomorphisms, those morphisms being Cartesian open
> immersions, so the `f`-map cocycle
> (`Crystalline.GlobalCrystallineSituation.SmallSite.CohomologyRestriction.fmapComp_comp`) transfers
> bijectivity of the `f`-map composition to the direct images from the members of the cover, and
> invertibility of `c_f` follows because it is Zariski-local on `T`.

```lean
theorem isSheafCrystal_of_isQuasicoherentOnSite
    (M : SheafOfModules.{u} (structureSheaf S)) (hM : M.IsQuasicoherentOnSite) :
    IsSheafCrystal M
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.isLocallyQuasiCoherent_of_isQuasicoherentOnSite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/QuasicoherentImpliesLocal.lean, line 384](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/QuasicoherentImpliesLocal.lean#L384). The attribute's comment: “the implication (1) ⇒ (2)(a) on the small site Cris(X/S): quasi-coherent implies locally quasi-coherent. The same implication on the big site CRIS(X/S), and the other half (1) ⇒ (2)(b) that a quasi-coherent module is a crystal, on each of the two sites, carry this tag separately. The converse (2) ⇒ (1) is a separate statement”.

> **Stacks Project, Tag 07IT for `𝒞 = Cris(X/S)`, the implication (1) ⇒ (2)(a): a quasi-coherent
> sheaf of `𝒪_{X/S}`-modules on the small crystalline site is locally quasi-coherent.**
>
> Quasi-coherence gives, around every point of the ambient scheme `T` of every object `(U, T, δ)` of
> `Cris(X/S)`, an open `V` on whose restriction `(U ∩ V, V, δ|_V)` the module has a global
> presentation (`Crystalline.GlobalCrystallineSituation.SmallSite`
> `.exists_hasGlobalPresentation_restrictOpen`, which is cocontinuity of the restriction functor).
> Intersecting `V` with a given open `W` of `T` makes those opens into an open cover of `W`, and each
> presentation restricts to one of `F_T` on the Zariski site localised at `V ⊓ W` by
> `Crystalline.GlobalCrystallineSituation.SmallSite`
> `.hasGlobalPresentation_moduleRestrictionSheaf_over`; that is quasi-coherence of `F_T` over `W`.
>
> This is one of the two halves of the implication (1) ⇒ (2) of the tag; the other half, that a
> quasi-coherent module is a crystal, is
> `Crystalline.GlobalCrystallineSituation.SmallSite.isSheafCrystal_of_isQuasicoherentOnSite` of
> `StacksFrontier.AlgebraicGeometry.Crystalline.SmallSite.QuasicoherentCrystal`.

```lean
theorem isLocallyQuasiCoherent_of_isQuasicoherentOnSite
    (M : SheafOfModules.{u} (structureSheaf S)) (hM : M.IsQuasicoherentOnSite) :
    IsLocallyQuasiCoherent M
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.isQuasicoherentOnSite_of_isLocallyQuasiCoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/QuasicoherentOfCrystal.lean, line 333](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/QuasicoherentOfCrystal.lean#L333). The attribute's comment: “the implication (2) ⇒ (1) on the small site Cris(X/S): a sheaf of 𝒪\_\{X/S}-modules whose restrictions F\_T are all quasi-coherent and which is a crystal in 𝒪\_\{X/S}-modules is quasi-coherent on the site”.

> **The implication (2) ⇒ (1) of [Stacks, Tag 07IT] on the small crystalline site `Cris(X/S)`: a
> locally quasi-coherent sheaf of `𝒪_{X/S}`-modules which is a crystal in `𝒪_{X/S}`-modules is
> quasi-coherent on the site.**
>
> Quasi-coherence is Zariski-local on the ambient scheme of each object
> (`Crystalline.GlobalCrystallineSituation.SmallSite.isQuasicoherentOnSite_of_forall_isAffine`), so
> it is enough to present `F` globally on the localisation of `Cris(X/S)` at an object whose ambient
> scheme is affine, which is
> `Crystalline.GlobalCrystallineSituation.SmallSite.hasGlobalPresentation_over_of_isAffine`.
>
> The crystal condition is read at sheaf level, as
> `Crystalline.GlobalCrystallineSituation.SmallSite.IsSheafCrystal`; that is the reading under which
> the tag holds, and the two hypotheses are exactly the source's conditions (a) and (b).

```lean
theorem isQuasicoherentOnSite_of_isLocallyQuasiCoherent
    {M : SheafOfModules.{u} (structureSheaf S)} (hlqc : IsLocallyQuasiCoherent M)
    (hcrys : IsSheafCrystal M) : M.IsQuasicoherentOnSite
```

**`Crystalline.GlobalCrystallineSituation.SmallSite.isQuasicoherentOnSite_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/QuasicoherentOfCrystal.lean, line 353](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/SmallSite/QuasicoherentOfCrystal.lean#L353). The attribute's comment: “the equivalence on the small site Cris(X/S), with the crystal condition read with the comparison maps of sheaves of modules”.

> **[Stacks, Tag 07IT] on the small crystalline site `Cris(X/S)`:** a sheaf of
> `𝒪_{X/S}`-modules is quasi-coherent on the site if and only if all its restrictions `F_T` are
> quasi-coherent `𝒪_T`-modules and it is a crystal in `𝒪_{X/S}`-modules.
>
> The two halves of the forward implication are
> `Crystalline.GlobalCrystallineSituation.SmallSite.isLocallyQuasiCoherent_of_isQuasicoherentOnSite`
> and `Crystalline.GlobalCrystallineSituation.SmallSite.isSheafCrystal_of_isQuasicoherentOnSite`; the
> converse is
> `Crystalline.GlobalCrystallineSituation.SmallSite.isQuasicoherentOnSite_of_isLocallyQuasiCoherent`.
> The crystal condition is read at sheaf level, which is the reading under which the tag holds; see
> the module documentation.

```lean
theorem isQuasicoherentOnSite_iff (M : SheafOfModules.{u} (structureSheaf S)) :
    M.IsQuasicoherentOnSite ↔ IsLocallyQuasiCoherent M ∧ IsSheafCrystal M
```

## Tag 07IU, a definition

[Tag 07IU](https://stacks.math.columbia.edu/tag/07IU) in the Stacks Project.

**`Crystalline.GlobalCrystallineSituation.SmallSite.IsFiniteLocallyFreeQuasicoherentCrystal`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/FiniteLocallyFreeCrystal.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/FiniteLocallyFreeCrystal.lean#L135). The attribute's comment: “crystals in finite locally free modules on the small site Cris(X/S), with the crystal in quasi-coherent modules taken as condition (1) of Stacks 07IT”.

> **Stacks Project, Tag 07IU.**  A *crystal in finite locally free modules* on the small
> crystalline site: a sheaf of `𝒪_{X/S}`-modules on `Cris(X/S)` which is a crystal in quasi-coherent
> modules — that is, quasi-coherent, condition (1) of [Stacks, Tag 07IT] — and is finite locally
> free.  [Stacks, Tag 07IS] states the conditions for `CRIS(X/S)` and for `Cris(X/S)` alike, and
> both predicates used here are the general ones for a sheaf of modules on a site, so this differs
> from the condition on the big site only in the site it is read on.

```lean
structure IsFiniteLocallyFreeQuasicoherentCrystal {S : GlobalCrystallineSituation.{u}}
    (M : SheafOfModules.{u} (structureSheaf S)) : Prop
```

**`Crystalline.GlobalCrystallineSituation.IsFiniteLocallyFreeQuasicoherentCrystal`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Crystalline/FCrystal.lean, line 380](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/FCrystal.lean#L380). The attribute's comment: “crystals in finite locally free modules on the big site CRIS(X/S), with the crystal in quasi-coherent modules taken as condition (1) of Stacks 07IT”.

> **Stacks Project, Tag 07IU.**  A *crystal in finite locally free modules* on the big
> crystalline site: a sheaf of `𝒪_{X/S}`-modules on `CRIS(X/S)` which is a crystal in quasi-coherent
> modules — that is, quasi-coherent, condition (1) of [Stacks, Tag 07IT] — and is finite locally
> free, every object of the site having a covering on whose members the restricted module is a
> finite free module over the restricted structure sheaf.
>
> This is the condition [Stacks, Tag 07N3] builds its F-crystal on, so it is stated here, upstream
> of `Crystalline.FCrystal`; the small-site form of the same condition and what either form gives
> through [Stacks, Tag 07IT] are in
> `StacksFrontier.AlgebraicGeometry.Crystalline.CrystalsModules.FiniteLocallyFreeCrystal`.

```lean
structure IsFiniteLocallyFreeQuasicoherentCrystal {S : GlobalCrystallineSituation.{u}}
    (M : SheafOfModules.{u} (crystallineStructureSheaf S)) : Prop
```

Declarations registered for the tag:

- [`SheafOfModules.IsQuasicoherentOnSite`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Topologies/QuasicoherentOnSite.lean#L99), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/FiniteLocallyFreeCrystal.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Crystalline/CrystalsModules/FiniteLocallyFreeCrystal.lean#L112) (StacksFrontier): “a crystal in quasi-coherent modules on either crystalline site is a quasi-coherent sheaf of modules, condition (1) of Stacks 07IT”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 60.11, Tag 07IR](https://stacks.math.columbia.edu/tag/07IR)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
