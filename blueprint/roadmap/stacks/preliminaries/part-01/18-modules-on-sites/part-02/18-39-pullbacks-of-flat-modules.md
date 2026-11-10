---
declaration: section
origin: cited
lean: Stacks.Sheaves.RingedToposModules.isFlat_pullbackModules, Stacks.Sheaves.RingedToposModules.isFlat_pullbackModules_maxSectionUniverse, Stacks.ModuleUp.isFlat_pullback_of_representablyFlat, Stacks.SheafOfModules.isFlatModuleStalk_of_isFlat, Stacks.isFlatModuleStalk_of_isFlat, Stacks.isFlat_iff_forall_isFlatModuleStalk_of_weakSheafify, Stacks.Sheaves.RingedToposModules.shortExact_map_pullbackModules, AlgebraicGeometry.RingedToposHom.exists_shortExact_map_pullbackModules
statement: formalized
proof: formalized
---

# 18.39 Pullbacks of flat modules

Section 18.39 of the Stacks Project, [Tag 05VA](https://stacks.math.columbia.edu/tag/05VA). 4 tags here are carried by 8 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05VD, a lemma

[Tag 05VD](https://stacks.math.columbia.edu/tag/05VD) in the Stacks Project.

**`Stacks.Sheaves.RingedToposModules.isFlat_pullbackModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackFlatInverseImage.lean, line 359](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackFlatInverseImage.lean#L359). The attribute's comment: “ringed topoi, at free universes, assuming on each site the HasSheafCompose, HasWeakSheafify, WEqualsLocallyBijective and HasSheafify instances of the variable block; isFlat_pullbackModules_maxSectionUniverse is the same statement with all of them derived”. References: SGA 4 V (8.2.9); SGA 4 V (1.7.1).

> **Stacks Project, Tag 05VD.**  The pullback of a flat sheaf of modules along a morphism of
> ringed topoi is flat.
>
> All five universe parameters of the tagged statement are free here; what the tag does not state
> are the sheafification hypotheses in the `variable` block above — `HasSheafCompose` for the three
> forgetful functors, `HasWeakSheafify` and `WEqualsLocallyBijective` for `AddCommGrpCat`, and
> `HasSheafify` for `Type` — on each of the two sites.  They arise because `Stacks.ringSheaf` and
> `Stacks.SheafOfModules.IsFlat` take them as instance binders where a `ringSheaf` construction
> could build them internally, so they are a formulation difference rather than added mathematical
> strength; but they are *not* nothing, and a consumer whose binder context lacks them cannot apply
> this theorem without supplying them.
>
> They need not be supplied when each ringed topos has its section universe equal to the `max` of
> its site's object and morphism universes, which is what
> `Stacks.Sheaves.RingedToposModules.isFlat_pullbackModules_maxSectionUniverse` below records: at
> that shape every one of them is an instance of the pinned Mathlib, so that statement of Stacks
> 05VD assumes nothing beyond the source's own hypotheses.  Both object universes and both morphism
> universes stay free there; it is only the two section universes that are determined.

```lean
theorem isFlat_pullbackModules (hG : Stacks.SheafOfModules.IsFlat (O := Y.O) G) :
    Stacks.SheafOfModules.IsFlat (O := X.O) ((f.pullbackModules).obj G)
```

**`Stacks.Sheaves.RingedToposModules.isFlat_pullbackModules_maxSectionUniverse`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackFlatInverseImage.lean, line 421](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackFlatInverseImage.lean#L421). The attribute's comment: “ringed topoi whose section universe is the max of their site's object and morphism universes -- object and morphism universes free and independent -- with no sheafification hypothesis assumed: HasSheafCompose, HasWeakSheafify, WEqualsLocallyBijective and HasSheafify are all derived”. References: SGA 4 V (8.2.9); SGA 4 V (1.7.1); SGA 4 VI (8.6.4), “special case”.

> **Stacks Project, Tag 05VD, assuming nothing the source does not assume.**  The pullback of a
> flat sheaf of modules along a morphism of ringed topoi is flat.
>
> This is `Stacks.Sheaves.RingedToposModules.isFlat_pullbackModules` with every one of its
> sheafification hypotheses discharged by instance search instead of assumed.  That is possible
> exactly when each ringed topos has its section universe equal to the `max u v` of its site's
> object and morphism universes, which is the shape above; the two object universes and the two
> morphism universes remain free and independent.
>
> Where each hypothesis comes from, and which of them need the section universe at all:
>
> * the three `HasSheafCompose` hypotheses hold at **every** universe and for every site, so they
>   were never where the narrowing lived: `forget AddCommGrpCat` by
>   `CategoryTheory.hasSheafCompose_of_preservesMulticospan`, and `forget RingCat` and
>   `forget₂ CommRingCat RingCat` by `CategoryTheory.hasSheafComposeEssentiallySmallSite`;
> * `HasSheafify J (Type (max u v))` is `CategoryTheory.instHasSheafifyType`, and it too is less
>   rigid than it looks: `HasSheafify J (Type w)` holds for a free `w` under
>   `UnivLE.{max u v, w}`, by
>   `CategoryTheory.instHasSheafifyOfPreservesLimitsForgetOfHasFiniteLimitsOfSmallOppositeCover`;
> * `HasWeakSheafify J AddCommGrpCat.{max u v}` is `CategoryTheory.instHasWeakSheafifyOfHasSheafify`
>   applied to that same plus-construction instance at `AddCommGrpCat`;
> * `J.WEqualsLocallyBijective AddCommGrpCat.{max u v}` follows from the previous one by the
>   concrete-category instance of `Mathlib/CategoryTheory/Sites/LocallyBijective.lean`, built on
>   `CategoryTheory.GrothendieckTopology.WEqualsLocallyBijective.mk'`.
>
> **Why the section universe cannot be left free.**  Exactly one of the five resists:
> `HasWeakSheafify J AddCommGrpCat.{w}` for a free `w`, which fails even under
> `UnivLE.{max u v, w}`.  The plus construction needs `PreservesColimitsOfShape (J.Cover X)ᵒᵖ
> (forget AddCommGrpCat.{w})`, and the only instance supplying it is
> `AddCommGrpCat.FilteredColimits.forget_preservesFilteredColimits`, which is
> `PreservesFilteredColimits (forget AddCommGrpCat.{w})` — filtered shapes in the *same* universe
> `w` as the groups, while the cover categories live in `max u v`.  The two agree precisely at
> `w = max u v`.  Since `Stacks.SheafOfModules.IsFlat` takes `HasWeakSheafify` as an instance
> binder, this blocks the statement and not merely the proof.  For a `w` strictly below `max u v`
> there is nothing to lift at all: sheafification of `AddCommGrpCat.{w}`-valued presheaves on a
> site whose covers are `max u v`-large does not exist in general.  So
> `isFlat_pullbackModules` above, with the hypotheses carried and all five universes free, and this
> statement, with the section universes determined and no hypotheses, are each the strongest
> available in their own direction, and neither subsumes the other.

```lean
theorem isFlat_pullbackModules_maxSectionUniverse
    (hG : Stacks.SheafOfModules.IsFlat (J := Y.J) (O := Y.O) G) :
    Stacks.SheafOfModules.IsFlat (J := X.J) (O := X.O) ((f.pullbackModules).obj G)
```

**`Stacks.ModuleUp.isFlat_pullback_of_representablyFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SiteUpSheafificationPullback.lean, line 654](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/SiteUpSheafificationPullback.lean#L654). The attribute's comment: “ringed sites, for a morphism of sites given by a continuous representably flat functor, with no sheafification hypothesis assumed: the HasWeakSheafify, HasSheafCompose, WEqualsLocallyBijective and HasLeftKanExtension instances are all derived. The reduction of an arbitrary morphism of ringed sites to this case is Stacks 03CR”. References: SGA 4 V (8.2.9), “representably flat u”; SGA 4 V (1.7.1), “representably flat u”.

> **Stacks 05VD for a morphism of ringed sites, assuming nothing the source does not assume.**
>
> This is `Stacks.ModuleUp.isFlat_pullback` with every sheafification hypothesis of the section
> above discharged by instance search instead of assumed: `HasWeakSheafify` for `CommRingCat`,
> `RingCat` and `AddCommGrpCat` on both sites, `HasSheafCompose` for
> `forget₂ CommRingCat RingCat` on both sites, `WEqualsLocallyBijective` for `RingCat` and
> `AddCommGrpCat` on both sites, and the two `HasLeftKanExtension` families.  All eleven are
> instances of the pinned Mathlib for a small site, so what is left — `RepresentablyFlat u` and
> `u.IsContinuous K J` — is exactly the situation the source's proof reduces to.
>
> They are kept as binders in the section above because they are wanted at *elaboration* time by
> the definitions there: with them removed, `Stacks.ModuleUp.upSheafUnitRingOfCommRing` no longer
> elaborates and `Stacks.ModuleUp.upSheafify_comp_bridge` exhausts the `isDefEq` heartbeat budget
> re-deriving `J.PreservesSheafification (forget₂ CommRingCat RingCat)`, the synthesis already
> recorded as too expensive in the implementation notes.  Discharging them once, here, at the
> statement of the theorem costs nothing.
>
> **The single-universe restriction is not liftable on this branch.**  The sites are small
> categories in `Type w` with the structure sheaves and modules also at `w`.  This is forced by
> `PresheafOfModules.pullbackObjIsDefined_eq_top`, the only unconditional source of
> `(PresheafOfModules.pushforward φ).IsRightAdjoint` and hence of `SheafOfModules.pullback`
> itself, which Mathlib states for `{C D : Type u} [SmallCategory C] [SmallCategory D]` and
> `RingCat.{u}`.  Nothing weaker is available, so the object, morphism and section universes
> cannot be separated here without first generalizing that Mathlib declaration.

```lean
theorem isFlat_pullback_of_representablyFlat {R : Sheaf J CommRingCat.{w}}
    {O : Sheaf K CommRingCat.{w}}
    (η : O ⟶ (u.sheafPushforwardContinuous CommRingCat.{w} K J).obj R)
    (F : _root_.SheafOfModules.{w} (Stacks.commRingSheafToRingSheaf (J := K) O))
    (hF : Stacks.SheafOfModules.IsFlat (J := K) (O := O) F) :
    Stacks.SheafOfModules.IsFlat (J := J) (O := R)
      ((SheafOfModules.pullback.{w} (ringSheafMapOfPushforward u J η)).obj F)
```

## Tag 05VB, a lemma

[Tag 05VB](https://stacks.math.columbia.edu/tag/05VB) in the Stacks Project.

**`Stacks.SheafOfModules.isFlatModuleStalk_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatStalk.lean, line 297](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/FlatStalk.lean#L297). References: SGA 4 V (1.6), “assertion 1”.

> **Stacks Project, Tag 05VB.** Let `(C, O)` be a ringed site and let `Φ` be a point of `C`. If
> `F` is a flat sheaf of `O`-modules, then the stalk of `F` at `Φ` is a flat module over the stalk
> of `O` at `Φ`.
>
> The proof runs the equational criterion for flatness on both sides. A relation `∑ fᵢ xᵢ = 0` in
> the stalk is lifted to a relation among sections over a neighbourhood of `Φ`; the local
> equational criterion for a flat sheaf of modules, Stacks 08FC part (2), factors those sections
> through a finite free module on a covering of that neighbourhood; the point's fibre meets one
> member of the covering, and the germs of that factorisation exhibit the original relation as
> trivial, which is flatness of the stalk by Mathlib's equational criterion.

```lean
theorem isFlatModuleStalk_of_isFlat (Φ : J.Point.{max v w})
    (O : Sheaf J CommRingCat.{max v w})
    (F : _root_.SheafOfModules.{max v w} (commRingSheafToRingSheaf O)) (hF : IsFlat F) :
    IsFlatModuleStalk Φ O F
```

**`Stacks.isFlatModuleStalk_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Point/FlatModuleStalk.lean, line 165](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Point/FlatModuleStalk.lean#L165).

> **Stacks 05VB.**  The stalk at a point of a site of a flat sheaf of `O`-modules is a flat
> module over the stalk of `O`.

```lean
theorem isFlatModuleStalk_of_isFlat
    (F : _root_.SheafOfModules.{max v w} (commRingSheafToRingSheaf O))
    (hF : SheafOfModules.IsFlat F) (Φ : J.Point.{max v w}) :
    IsFlatModuleStalk Φ O F
```

## Tag 05VC, a lemma

[Tag 05VC](https://stacks.math.columbia.edu/tag/05VC) in the Stacks Project.

**`Stacks.isFlat_iff_forall_isFlatModuleStalk_of_weakSheafify`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/StalkTensorComparisonWeak.lean, line 37](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/StalkTensorComparisonWeak.lean#L37). References: SGA 4 V (1.6), “2)”.

> A sheaf of modules is flat if and only if its stalks at a conservative family of points are
> flat, assuming `HasWeakSheafify J AddCommGrpCat.{w}` and
> `J.WEqualsLocallyBijective AddCommGrpCat.{w}`.

```lean
theorem isFlat_iff_forall_isFlatModuleStalk_of_weakSheafify {C : Type u} [Category.{v} C]
    [LocallySmall.{w} C] {J : GrothendieckTopology C}
    [J.HasSheafCompose (forget₂ CommRingCat.{w} RingCat.{w})]
    [J.WEqualsLocallyBijective AddCommGrpCat.{w}] [HasWeakSheafify J AddCommGrpCat.{w}]
    {t : Type*} (p : t → J.Point.{w})
    (hp : (ObjectProperty.ofObj p).IsConservativeFamilyOfPoints) (O : Sheaf J CommRingCat.{w})
    (F : SheafOfModules.{w} (commRingSheafToRingSheaf O)) :
    SheafOfModules.IsFlat F ↔ ∀ i, IsFlatModuleStalk (p i) O F
```

## Tag 0G6R, a lemma

[Tag 0G6R](https://stacks.math.columbia.edu/tag/0G6R) in the Stacks Project.

**`Stacks.Sheaves.RingedToposModules.shortExact_map_pullbackModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackShortExactFlat.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/PullbackShortExactFlat.lean#L140). References: EGA IV (2.1.8), “(i), G' = O_{Y'}”.

> **Stacks Project, Tag 0G6R.**  Let `(f, f♯) : (Sh(C), O_C) ⟶ (Sh(D), O_D)` be a morphism of
> ringed topoi and let `0 → F → G → H → 0` be a short exact sequence of sheaves of `O_D`-modules
> with `H` a flat `O_D`-module.  Then `0 → f^*F → f^*G → f^*H → 0` is short exact.
>
> The pullback of Stacks 03D6 part (2) is the inverse image of Stacks 03D2 followed by extension
> of scalars along `f♯`.  The inverse image is exact (Stacks 04JC) and carries `H` to a flat
> `f⁻¹O_D`-module (Stacks 05VD), and extension of scalars keeps a short exact sequence with flat
> third term short exact (Stacks 03EX).

```lean
theorem shortExact_map_pullbackModules
    (S : ShortComplex (SheafOfModules.{w'} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)))
    (hS : S.ShortExact)
    (hflat : Stacks.SheafOfModules.IsFlat (O := Y.O) S.X₃) :
    (S.map (f.pullbackModules)).ShortExact
```

**`AlgebraicGeometry.RingedToposHom.exists_shortExact_map_pullbackModules`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/PullbackOfAShortExactSequence.lean, line 83](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cohomology/DerivedPullback/PullbackOfAShortExactSequence.lean#L83). The attribute's comment: “morphisms of ringed topoi, with the source ringed topos's site small in the universe of its sections and the target's section universe equal to the max of its object and morphism universes”. References: EGA IV (2.1.8), “(i), G' = O_{Y'}”.

> **Stacks Project, Tag 0G6R.**  For a morphism of ringed topoi
> `(f, f♯) : (Sh(C), O_C) ⟶ (Sh(D), O_D)` and a short exact sequence of sheaves of `O_D`-modules
> whose final term is flat, the pullback sequence `0 ⟶ f^*F₁ ⟶ f^*F₂ ⟶ f^*F₃ ⟶ 0` is short exact.
>
> The pullback is the one of Stacks 03D6 part (2), `O_C ⊗_{f⁻¹O_D} f⁻¹(-)`.  The composite-is-zero
> witness is carried in the statement, so that the statement does not mention preservation of zero
> morphisms by the pullback, which is not part of that functor's public interface.

```lean
theorem exists_shortExact_map_pullbackModules (hS : S.ShortExact)
    (hflat : Stacks.SheafOfModules.IsFlat (O := Y.O) S.X₃) :
    ∃ h : (f.pullbackModules).map S.f ≫ (f.pullbackModules).map S.g = 0,
      (ShortComplex.mk ((f.pullbackModules).map S.f)
        ((f.pullbackModules).map S.g) h).ShortExact
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.39, Tag 05VA](https://stacks.math.columbia.edu/tag/05VA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
