---
declaration: section
origin: cited
lean: Stacks.Sheaves.LocalizedPullback.localizedPullbackMapData, Stacks.Sheaves.LocalizedPullback.isQuasicoherentOnSite_pullbackTopos_of_quasicoherentData, Stacks.Sheaves.LocalizedPullback.isQuasicoherentOnSite_pullbackTopos, Stacks.Sheaves.LocalizedPullback.isFiniteFree_over_pullbackTopos, Stacks.Sheaves.LocalizedPullback.isFiniteLocallyFreeOnSite_pullbackTopos, Stacks.Sheaves.LocalizedPullback.isFree_over_pullbackTopos, Stacks.Sheaves.LocalizedPullback.isLocallyFreeOnSite_pullbackTopos, Stacks.Sheaves.LocalizedPullback.generatingSectionsPullbackTopos
statement: formalized
proof: formalized
---

# 18.18 Intrinsic properties of modules

Section 18.18 of the Stacks Project, [Tag 03DG](https://stacks.math.columbia.edu/tag/03DG). 1 tag here is carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03DG, the section

[Tag 03DG](https://stacks.math.columbia.edu/tag/03DG) in the Stacks Project.

**`Stacks.Sheaves.LocalizedPullback.localizedPullbackMapData`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalizedPullbackQuasicoherent.lean, line 440](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalizedPullbackQuasicoherent.lean#L440). The attribute's comment: “condition (3) of the method, for the quasi-coherent property: the datum needed to carry a global presentation along a pullback is the pullback along the localized morphism of ringed topoi of 04J0, and this constructs it”.

> **The localized pullback datum of Section 03DG, for the quasi-coherent property.** Let
> `(f, f♯) : (C, O) ⟶ (D, O')` be a morphism of ringed sites whose underlying functor `u : D ⥤ C`
> is left exact, and let `q` be quasi-coherent data for a sheaf of `O'`-modules `M`: a family
> `{W_i}` covering the final object of `D` together with a global presentation of `M|_{W_i}` for
> each `i`.  Then the family `{u(W_i)}` covers the final object of `C`, and pullback along the
> localized morphism of ringed topoi `(Sh(C/u(W_i)), O_{u(W_i)}) ⟶ (Sh(D/W_i), O'_{W_i})` of
> Stacks 04J0 carries `M|_{W_i}` to `(f^*M)|_{u(W_i)}` and the structure sheaf to the structure
> sheaf, and preserves colimits.
>
> Section 03DG's method for defining an intrinsic property of modules asks, in its condition (3),
> that the property be preserved by pullback along a morphism of ringed sites presented by a left
> exact continuous functor; the functor that verification needs is the pullback along the
> localized morphism of ringed topoi, and this is that datum for quasi-coherence.  The three
> properties of it required are exactly the fields of
> `Stacks.SheafOfModules.QuasicoherentData.MapData`, and each is one of the property-agnostic
> pieces above: colimit preservation is
> `Stacks.Sheaves.LocalizedPullback.preservesColimitsOfSize_localizedPullbackTopos`, the unit
> isomorphism is `.localizedPullbackUnitIso`, and the identification of the transported module is
> `.localizedPullbackOverIso`.

```lean
def localizedPullbackMapData (q : M.QuasicoherentData.{ww}) :
    Stacks.SheafOfModules.QuasicoherentData.MapData
      f.toRingedToposSiteHom.pullbackTopos q
```

**`Stacks.Sheaves.LocalizedPullback.isQuasicoherentOnSite_pullbackTopos_of_quasicoherentData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalizedPullbackQuasicoherent.lean, line 472](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalizedPullbackQuasicoherent.lean#L472). The attribute's comment: “condition (3) verified for the quasi-coherent property: the pullback of a quasi-coherent module along a morphism of ringed sites presented by a left exact continuous functor is quasi-coherent”.

> **The quasi-coherent clause of Stacks 03DO for a morphism of ringed sites presented by a
> left exact continuous functor.** The pullback of a sheaf of `O'`-modules admitting quasi-coherent
> data is quasi-coherent on the site.
>
> The data is transported by `Stacks.Sheaves.LocalizedPullback.localizedPullbackMapData` and the
> transported presentations assemble into quasi-coherence on the site by
> `Stacks.SheafOfModules.isQuasicoherentOnSite_of_mapData`.
>
> This is the case to which Stacks 03DO's own proof reduces its quasi-coherent clause through
> Section 03DG; the general statement, for an arbitrary morphism of ringed topoi, is
> `AlgebraicGeometry.RingedToposHom.isQuasicoherentOnSite_pullbackModules`, which transports this
> one along the two equivalences of ringed topoi that Stacks 03CR produces.

```lean
theorem isQuasicoherentOnSite_pullbackTopos_of_quasicoherentData
    (q : M.QuasicoherentData.{ww}) :
    (f.toRingedToposSiteHom.pullbackTopos.obj M).IsQuasicoherentOnSite
```

**`Stacks.Sheaves.LocalizedPullback.isQuasicoherentOnSite_pullbackTopos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalizedPullbackQuasicoherent.lean, line 527](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalizedPullbackQuasicoherent.lean#L527). The attribute's comment: “condition (3) verified for the quasi-coherent property, with the hypothesis in the form 03DO states it: the pullback of a quasi-coherent module along a morphism of ringed sites presented by a left exact continuous functor is quasi-coherent”.

> **The quasi-coherent clause of Stacks 03DO for a morphism of ringed sites, with the
> hypothesis in the form the clause states it.** If a sheaf of `O'`-modules is quasi-coherent on
> the site, so is its pullback along a morphism of ringed sites presented by a left exact
> continuous functor.
>
> Quasi-coherence may be tested on a single family covering the final object, by Stacks 03DN in the
> form `Stacks.SheafOfModules.isQuasicoherentOnSite_iff_exists_cover_hasGlobalPresentation`.  Such
> a family `{W_i}` for `M` is carried to the family `{u(W_i)}` by
> `Stacks.Sheaves.LocalizedPullback.coversTop_mapObj`, and the global presentation of `M|_{W_i}` to
> one of `(f^*M)|_{u(W_i)}` by
> `Stacks.Sheaves.LocalizedPullback.hasGlobalPresentation_over_pullbackTopos`.  No smallness
> hypothesis on the slices of the target site is needed, for the reason recorded there.
>
> This is the case to which Stacks 03DO's own proof reduces its quasi-coherent clause through
> Section 03DG; the general statement, for an arbitrary morphism of ringed topoi, is
> `AlgebraicGeometry.RingedToposHom.isQuasicoherentOnSite_pullbackModules`, which transports this
> one along the two equivalences of ringed topoi that Stacks 03CR produces.

```lean
theorem isQuasicoherentOnSite_pullbackTopos (hM : M.IsQuasicoherentOnSite) :
    (f.toRingedToposSiteHom.pullbackTopos.obj M).IsQuasicoherentOnSite
```

**`Stacks.Sheaves.LocalizedPullback.isFiniteFree_over_pullbackTopos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalizedPullbackQuasicoherent.lean, line 554](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalizedPullbackQuasicoherent.lean#L554). The attribute's comment: “condition (3) of the method, for the finite locally free property: the datum needed to carry a finite free cofan along a pullback is the pullback along the localized morphism of ringed topoi of 04J0, and this is that transport”. References: EGA 0 (5.4.5), “partial”.

> **The localized pullback datum of Section 03DG, for the finite locally free property.** Let
> `(f, f♯) : (C, O) ⟶ (D, O')` be a morphism of ringed sites whose underlying functor `u : D ⥤ C`
> is left exact, let `M` be a sheaf of `O'`-modules and let `W` be an object of `D` on which `M`
> is finite free, that is, on which `M|_W` is a coproduct of finitely many copies of `O'_W`.  Then
> `(f^*M)|_{u(W)}` is a coproduct of as many copies of `O_{u(W)}`.
>
> The three pieces of the localized pullback datum are what the transport consumes: pullback along
> the localized morphism of ringed topoi of Stacks 04J0 preserves colimits, carries `O'_W` to
> `O_{u(W)}`, and carries `M|_W` to `(f^*M)|_{u(W)}`.  None of them mentions a property of
> modules; the property enters only through
> `Stacks.Sheaves.LocalizedPullback.isFiniteFree_map`, which is the statement that finite freeness
> is expressed by a colimit.

```lean
theorem isFiniteFree_over_pullbackTopos (W : Y.C)
    (h : _root_.SheafOfModules.IsFiniteFree ((Stacks.SheafOfModules.Tensor.ringSheaf Y.O).over W)
      (M.over W)) :
    _root_.SheafOfModules.IsFiniteFree
      ((Stacks.SheafOfModules.Tensor.ringSheaf X.O).over (f.u.obj W))
      ((f.toRingedToposSiteHom.pullbackTopos.obj M).over (f.u.obj W))
```

**`Stacks.Sheaves.LocalizedPullback.isFiniteLocallyFreeOnSite_pullbackTopos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalizedPullbackQuasicoherent.lean, line 590](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalizedPullbackQuasicoherent.lean#L590). The attribute's comment: “condition (3) verified for the finite locally free property: the pullback of a finite locally free module along a morphism of ringed sites presented by a left exact continuous functor is finite locally free”. References: EGA II (6.4.8), “more general”.

> **The finite locally free clause of Stacks 03DO for a morphism of ringed sites presented by
> a left exact continuous functor.** If a sheaf of `O'`-modules is finite locally free on the
> site, so is its pullback along a morphism of ringed sites whose underlying functor is left
> exact.  This is the clause of Stacks 03DO for Stacks 03DL (2).
>
> Finite local freeness may be tested on a single family covering the final object, by Stacks 03DN
> in the form `Stacks.SheafOfModules.isFiniteLocallyFreeOnSite_iff_exists_cover_isFiniteFree`.
> Such a family `{W_i}` for `M` is carried to the family `{u(W_i)}` by
> `Stacks.Sheaves.LocalizedPullback.coversTop_mapObj`, and the finite freeness of `M|_{W_i}` is
> carried to that of `(f^*M)|_{u(W_i)}` by
> `Stacks.Sheaves.LocalizedPullback.isFiniteFree_over_pullbackTopos`.
>
> This is the case to which Stacks 03DO's own proof reduces the clause through Section 03DG; the
> general statement, for an arbitrary morphism of ringed topoi, is
> `AlgebraicGeometry.RingedToposHom.isFiniteLocallyFreeOnSite_pullbackModules`, which transports
> this one along the two equivalences of ringed topoi that Stacks 03CR produces.

```lean
theorem isFiniteLocallyFreeOnSite_pullbackTopos
    (hM : SheafOfModules.IsFiniteLocallyFreeOnSite M) :
    SheafOfModules.IsFiniteLocallyFreeOnSite
      (f.toRingedToposSiteHom.pullbackTopos.obj M)
```

**`Stacks.Sheaves.LocalizedPullback.isFree_over_pullbackTopos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalizedPullbackQuasicoherent.lean, line 618](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalizedPullbackQuasicoherent.lean#L618). The attribute's comment: “condition (3) of the method, for the locally free property: the datum needed to carry a free cofan along a pullback is the pullback along the localized morphism of ringed topoi of 04J0, and this is that transport”.

> **The localized pullback datum of Section 03DG, for the locally free property.** Let
> `(f, f♯) : (C, O) ⟶ (D, O')` be a morphism of ringed sites whose underlying functor `u : D ⥤ C`
> is left exact, let `M` be a sheaf of `O'`-modules and let `W` be an object of `D` on which `M`
> is free, that is, on which `M|_W` is a coproduct of copies of `O'_W`.  Then `(f^*M)|_{u(W)}` is
> a coproduct of copies of `O_{u(W)}` indexed by the same type.
>
> As for finite freeness, the three pieces of the localized pullback datum are what the transport
> consumes, and the property enters only through
> `Stacks.Sheaves.LocalizedPullback.isFree_map`.

```lean
theorem isFree_over_pullbackTopos (W : Y.C)
    (h : (M.over W).IsFree) :
    ((f.toRingedToposSiteHom.pullbackTopos.obj M).over (f.u.obj W)).IsFree
```

**`Stacks.Sheaves.LocalizedPullback.isLocallyFreeOnSite_pullbackTopos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalizedPullbackQuasicoherent.lean, line 650](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalizedPullbackQuasicoherent.lean#L650). The attribute's comment: “condition (3) verified for the locally free property: the pullback of a locally free module along a morphism of ringed sites presented by a left exact continuous functor is locally free”.

> **The locally free clause of Stacks 03DO for a morphism of ringed sites presented by a left
> exact continuous functor.** If a sheaf of `O'`-modules is locally free on the site, so is its
> pullback along a morphism of ringed sites whose underlying functor is left exact.  This is the
> clause of Stacks 03DO for Stacks 03DL (1).
>
> Local freeness may be tested on a single family covering the final object, by Stacks 03DN in the
> form `Stacks.SheafOfModules.isLocallyFreeOnSite_iff_exists_cover_isFree`.  Such a family `{W_i}`
> for `M` is carried to the family `{u(W_i)}` by
> `Stacks.Sheaves.LocalizedPullback.coversTop_mapObj`, and the freeness of `M|_{W_i}` is carried to
> that of `(f^*M)|_{u(W_i)}` by `Stacks.Sheaves.LocalizedPullback.isFree_over_pullbackTopos`.
>
> This is the case to which Stacks 03DO's own proof reduces the clause through Section 03DG; the
> general statement, for an arbitrary morphism of ringed topoi, is
> `AlgebraicGeometry.RingedToposHom.isLocallyFreeOnSite_pullbackModules`, which transports this
> one along the two equivalences of ringed topoi that Stacks 03CR produces.

```lean
theorem isLocallyFreeOnSite_pullbackTopos (hM : SheafOfModules.IsLocallyFreeOnSite M) :
    SheafOfModules.IsLocallyFreeOnSite
      (f.toRingedToposSiteHom.pullbackTopos.obj M)
```

**`Stacks.Sheaves.LocalizedPullback.generatingSectionsPullbackTopos`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalizedPullbackQuasicoherent.lean, line 675](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalizedPullbackQuasicoherent.lean#L675). The attribute's comment: “condition (3) of the method, for the locally generated property: the datum needed to carry a generating family of global sections along a pullback is the pullback along the localized morphism of ringed topoi of 04J0, and this is that transport”.

> **The localized pullback datum of Section 03DG, for the locally generated property.**
> Generating global sections of `M|_W` are carried by the pullback along the localized morphism of
> ringed topoi of Stacks 04J0 to generating global sections of `(f^*M)|_{u(W)}`, indexed by the
> same type.
>
> The transport is Mathlib's `SheafOfModules.GeneratingSections.map`, whose two hypotheses are
> again pieces of the localized pullback datum: colimit preservation and the identification of the
> two structure sheaves.  The identification of the transported module with `(f^*M)|_{u(W)}` is
> `Stacks.Sheaves.LocalizedPullback.localizedPullbackOverIso`.

```lean
def generatingSectionsPullbackTopos (W : Y.C) (σ : (M.over W).GeneratingSections) :
    ((f.toRingedToposSiteHom.pullbackTopos.obj M).over (f.u.obj W)).GeneratingSections
```

**`Stacks.Sheaves.LocalizedPullback.isLocallyGeneratedBySectionsOnSite_pullbackTopos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalizedPullbackQuasicoherent.lean, line 713](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalizedPullbackQuasicoherent.lean#L713). The attribute's comment: “condition (3) verified for the locally generated property: the pullback of a module locally generated by sections along a morphism of ringed sites presented by a left exact continuous functor is locally generated by sections”.

> **The locally generated clause of Stacks 03DO for a morphism of ringed sites presented by a
> left exact continuous functor.** If a sheaf of `O'`-modules is locally generated by sections, so
> is its pullback along a morphism of ringed sites whose underlying functor is left exact.  This is
> the clause of Stacks 03DO for Stacks 03DL (3).
>
> Local generation by sections may be tested on a single family covering the final object, by
> Stacks 03DN in the form
> `Stacks.SheafOfModules.isLocallyGeneratedBySectionsOnSite_iff_exists_cover_generatingSections`.
> Such a family `{W_i}` for `M` is carried to the family `{u(W_i)}` by
> `Stacks.Sheaves.LocalizedPullback.coversTop_mapObj`, and the generating sections of `M|_{W_i}`
> to those of `(f^*M)|_{u(W_i)}` by
> `Stacks.Sheaves.LocalizedPullback.generatingSectionsPullbackTopos`.
>
> This is the case to which Stacks 03DO's own proof reduces the clause through Section 03DG; the
> general statement, for an arbitrary morphism of ringed topoi, is
> `AlgebraicGeometry.RingedToposHom.isLocallyGeneratedBySectionsOnSite_pullbackModules`, which
> transports this one along the two equivalences of ringed topoi that Stacks 03CR produces.  The
> clause for local generation by a fixed number `r` of sections, Stacks 03DL (4), is proved for an
> arbitrary morphism of ringed topoi in
> `Stacks.Sheaves.LocalGeneration.pullbackModules_isLocallyGeneratedByOnSite`.

```lean
theorem isLocallyGeneratedBySectionsOnSite_pullbackTopos
    (hM : SheafOfModules.IsLocallyGeneratedBySectionsOnSite M) :
    SheafOfModules.IsLocallyGeneratedBySectionsOnSite
      (f.toRingedToposSiteHom.pullbackTopos.obj M)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.18, Tag 03DG](https://stacks.math.columbia.edu/tag/03DG)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
