---
declaration: section
origin: cited
lean: Stacks.Sheaves.LocallyRingedSite.condition1_iff_condition2_and_condition2_iff_condition3, AlgebraicGeometry.RingedSite.stalksAreZeroOrLocal_of_locallyUnitOrOneSubUnit, AlgebraicGeometry.RingedSite.locallyUnitOrOneSubUnit_iff_stalksAreZeroOrLocal, AlgebraicGeometry.RingedSite.oneIsNeverZero, Stacks.Sheaves.LocallyRingedSite.oneIsNeverZero, Stacks.Sheaves.LocallyRingedSite.isIso_oneIsNeverZero_iff, AlgebraicGeometry.RingedSite.nontrivial_stalk_of_isIso_oneIsNeverZero, AlgebraicGeometry.RingedSite.isIso_oneIsNeverZero_iff_forall_nontrivial_stalk
statement: formalized
proof: formalized
---

# 18.40 Locally ringed topoi

Section 18.40 of the Stacks Project, [Tag 04ER](https://stacks.math.columbia.edu/tag/04ER). 13 tags here are carried by 48 declarations of the repository (all in StacksFrontier) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04ES, a lemma

[Tag 04ES](https://stacks.math.columbia.edu/tag/04ES) in the Stacks Project.

**`Stacks.Sheaves.LocallyRingedSite.condition1_iff_condition2_and_condition2_iff_condition3`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/LocalUnitConditions.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/LocalUnitConditions.lean#L302). References: SGA 4 IV (13.9), “b) (ii) <=> (iii)”.

> **Theorem (Stacks Tag 04ES).** For a ringed site `(C, O)`, conditions (1), (2),
> (3) are equivalent. We state the equivalence as the conjunction of the two
> biconditionals `(1) ↔ (2)` and `(2) ↔ (3)`.

```lean
theorem condition1_iff_condition2_and_condition2_iff_condition3
    (O : Sheaf J CommRingCat.{v}) :
    (Condition1 O ↔ Condition2 O) ∧ (Condition2 O ↔ Condition3 O)
```

## Tag 04ET, a lemma

[Tag 04ET](https://stacks.math.columbia.edu/tag/04ET) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.stalksAreZeroOrLocal_of_locallyUnitOrOneSubUnit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/Defs.lean, line 177](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/Defs.lean#L177). The attribute's comment: “(1) implies (2)”. References: SGA 4 IV (13.9), “b) (iii) => (iv)”.

> The local unit-or-unit-complement condition makes every stalk of the structure sheaf either
> the zero ring or a local ring.

```lean
theorem stalksAreZeroOrLocal_of_locallyUnitOrOneSubUnit (X : RingedSite.{u, u, u})
    (h : LocallyUnitOrOneSubUnit X) : StalksAreZeroOrLocal X
```

**`AlgebraicGeometry.RingedSite.locallyUnitOrOneSubUnit_iff_stalksAreZeroOrLocal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/Defs.lean, line 219](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/Defs.lean#L219). The attribute's comment: “equivalence when the site has enough points”. References: SGA 4 IV (13.9), “b) (iii) <=> (iv)”.

> On a site with a conservative family of points, the local unit-or-unit-complement condition
> is equivalent to all stalks of the structure sheaf being zero rings or local rings.

```lean
theorem locallyUnitOrOneSubUnit_iff_stalksAreZeroOrLocal (X : RingedSite.{u, u, u})
    (hX : X.J.HasConservativeFamily.{u}) :
    LocallyUnitOrOneSubUnit X ↔ StalksAreZeroOrLocal X
```

## Tag 05D7, an equation

[Tag 05D7](https://stacks.math.columbia.edu/tag/05D7) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.oneIsNeverZero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/Defs.lean, line 308](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/Defs.lean#L308).

> The canonical morphism from the empty sheaf to the equalizer of the zero and one sections
> of the structure sheaf.

```lean
noncomputable def oneIsNeverZero (X : RingedSite.{u, v, w}) :
    ⊥_ (Sheaf X.J (Type w)) ⟶ equalizer (zeroSection X) (oneSection X)
```

**`Stacks.Sheaves.LocallyRingedSite.oneIsNeverZero`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/OneIsNeverZero.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/OneIsNeverZero.lean#L156). The attribute's comment: “the displayed morphism from the empty sheaf to the equalizer of 0 and 1”.

> The canonical morphism of sheaves of sets
>
>   `∅^# ⟶ Equalizer(0, 1 : * ⟶ O)`
>
> from the initial sheaf to the equalizer of the zero and one sections of the structure sheaf.
> The first condition in the definition of a locally ringed site (Tag 04EU) is that it be an
> isomorphism.

```lean
noncomputable def oneIsNeverZero (O : Sheaf J CommRingCat.{w}) :
    ⊥_ (Sheaf J (Type w)) ⟶ equalizer (zeroSection J O) (oneSection J O)
```

**`Stacks.Sheaves.LocallyRingedSite.isIso_oneIsNeverZero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/OneIsNeverZero.lean, line 187](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/OneIsNeverZero.lean#L187). The attribute's comment: “the equivalent sections-level form: 0 ≠ 1 over every object the empty sieve does not cover”.

> The canonical morphism `∅^# ⟶ Equalizer(0, 1)` is an isomorphism exactly when, for every
> object `U` that is not sheaf-theoretically empty, the sections `0` and `1` of `O(U)` are
> distinct.

```lean
theorem isIso_oneIsNeverZero_iff (O : Sheaf J CommRingCat.{w}) :
    IsIso (oneIsNeverZero J O) ↔
      ∀ U : C, (⊥ : Sieve U) ∉ J U → (0 : O.obj.obj (op U)) ≠ 1
```

## Tag 05D8, a lemma

[Tag 05D8](https://stacks.math.columbia.edu/tag/05D8) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.nontrivial_stalk_of_isIso_oneIsNeverZero`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/Defs.lean, line 450](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/Defs.lean#L450). The attribute's comment: “the implication (1) ⇒ (2)”.

> If zero and one are nowhere equal, then the stalk of the structure sheaf at every point is a
> nonzero ring.

```lean
lemma nontrivial_stalk_of_isIso_oneIsNeverZero (X : RingedSite.{v, u, u})
    [IsIso (oneIsNeverZero X)] (p : X.J.Point.{u}) :
    Nontrivial ((p.presheafFiber (A := CommRingCat.{u})).obj X.O.obj)
```

**`AlgebraicGeometry.RingedSite.isIso_oneIsNeverZero_iff_forall_nontrivial_stalk`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/Defs.lean, line 458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/Defs.lean#L458). The attribute's comment: “the equivalence (1) ⇔ (2) when the site has enough points”.

> On a site with a conservative family of points, zero and one are nowhere equal if and only if
> every stalk of the structure sheaf is a nonzero ring.

```lean
lemma isIso_oneIsNeverZero_iff_forall_nontrivial_stalk (X : RingedSite.{v, u, u})
    (hX : X.J.HasConservativeFamily.{u}) :
    IsIso (oneIsNeverZero X) ↔
      ∀ p : X.J.Point.{u}, Nontrivial ((p.presheafFiber (A := CommRingCat.{u})).obj X.O.obj)
```

**`Stacks.Sheaves.LocallyRingedSite.nontrivial_stalkRingObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/OneIsNeverZero.lean, line 263](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/OneIsNeverZero.lean#L263). The attribute's comment: “(1) implies (2): if the morphism of 05D7 is an isomorphism then no stalk of the structure sheaf is the zero ring”.

> If the morphism of Tag 05D7 is an isomorphism then for every point `p` of the site the stalk
> `O_p` is not the zero ring.

```lean
theorem nontrivial_stalkRingObj (h : IsIso (oneIsNeverZero X.J X.O))
    (p : Stacks.Sheaves.LocallyRingedTopos.Point X) : Nontrivial p.stalkRingObj
```

## Tag 04EU, a definition

[Tag 04EU](https://stacks.math.columbia.edu/tag/04EU) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.IsLocallyRinged`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/Defs.lean, line 344](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/Defs.lean#L344).

> A ringed site is locally ringed when the sections `0` and `1` of its structure sheaf are
> nowhere equal and every section is locally either a unit or has unit complement.

```lean
abbrev IsLocallyRinged (X : RingedSite.{u, v, w}) : Prop
```

**`Stacks.Sheaves.LocallyRingedSite.isLocallyRingedSite_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/OneIsNeverZero.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/OneIsNeverZero.lean#L240). The attribute's comment: “Definition 18.40.4 in the source's spelling (05D7 an isomorphism, plus 04ES)”.

> Definition 18.40.4 in the source's own spelling (the morphism of Tag 05D7 is an isomorphism,
> and the equivalent conditions of Tag 04ES hold) is equivalent to the sections-level predicate
> `IsLocallyRingedSite`.

```lean
theorem isLocallyRingedSite_iff :
    IsIso (oneIsNeverZero X.J X.O) ∧ Stacks.Sheaves.LocallyRingedSite.Condition1 X.O ↔
      LocalizedRingedTopos.IsLocallyRingedSite X
```

## Tag 04H7, a lemma

[Tag 04H7](https://stacks.math.columbia.edu/tag/04H7) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isLocallyRinged_inverseImage`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedTopoi/InverseImage.lean, line 394](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedTopoi/InverseImage.lean#L394). The attribute's comment: “part (1)”.

> **Stacks Project, Tag 04H7, part (1).** The inverse image of a locally ringed site by a
> morphism of topoi is locally ringed.

```lean
theorem isLocallyRinged_inverseImage (hY : IsLocallyRinged Y) :
    IsLocallyRinged
      ({ C := C, J := J, O := (inverseImageCommRingFunctor f).obj Y.O } :
        RingedSite.{u, u, u})
```

**`AlgebraicGeometry.RingedToposHom.isLocallyRinged_iff_of_ringedToposEquivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedTopoi/InverseImage.lean, line 437](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedTopoi/InverseImage.lean#L437). The attribute's comment: “part (2)”.

> **Stacks Project, Tag 04H7, part (2).** An equivalence of ringed topoi preserves and
> reflects local ringedness.

```lean
theorem isLocallyRinged_iff_of_ringedToposEquivalence (f : RingedToposHom X Y)
    [f.toToposHom.inverseImage.IsEquivalence] [IsIso f.fSharp] :
    RingedSite.IsLocallyRinged ({ C := Y.C, J := Y.J, O := Y.O } : RingedSite.{v, v, v}) ↔
      RingedSite.IsLocallyRinged ({ C := X.C, J := X.J, O := X.O } : RingedSite.{u, u, u})
```

## Tag 04H8, a definition

[Tag 04H8](https://stacks.math.columbia.edu/tag/04H8) in the Stacks Project.

**`Stacks.Sheaves.LocallyRingedSite.isLocallyRingedSite_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/OneIsNeverZero.lean, line 240](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/OneIsNeverZero.lean#L240). The attribute's comment: “a ringed topos is locally ringed exactly when its underlying ringed site is”.

> Definition 18.40.4 in the source's own spelling (the morphism of Tag 05D7 is an isomorphism,
> and the equivalent conditions of Tag 04ES hold) is equivalent to the sections-level predicate
> `IsLocallyRingedSite`.

```lean
theorem isLocallyRingedSite_iff :
    IsIso (oneIsNeverZero X.J X.O) ∧ Stacks.Sheaves.LocallyRingedSite.Condition1 X.O ↔
      LocalizedRingedTopos.IsLocallyRingedSite X
```

**`AlgebraicGeometry.RingedTopos.IsLocallyRinged`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedTopoi/Defs.lean, line 63](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedTopoi/Defs.lean#L63).

> **Stacks Project, Tag 04H8.** A ringed topos is locally ringed when the ringed site
> presenting it is a locally ringed site.

```lean
abbrev RingedTopos.IsLocallyRinged (X : RingedTopos.{v, u, w}) : Prop
```

**`AlgebraicGeometry.RingedTopos.isLocallyRinged_iff_of_equivalence`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedTopoi/Defs.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedTopoi/Defs.lean#L76). The attribute's comment: “well-posedness: invariance under an equivalence of ringed topoi”.

> **Stacks Project, Tag 04H8**, well-posedness. Being locally ringed is a property of a ringed
> topos and not of a site presenting it: by Stacks 04H7 part (2) an equivalence of ringed topoi
> preserves and reflects it.

```lean
theorem RingedTopos.isLocallyRinged_iff_of_equivalence {X : RingedTopos.{u, u, u}}
    {Y : RingedTopos.{v, v, v}} (f : RingedToposHom X Y)
    [f.toToposHom.inverseImage.IsEquivalence] [IsIso f.fSharp] :
    Y.IsLocallyRinged ↔ X.IsLocallyRinged
```

## Tag 0B8Q, a lemma

[Tag 0B8Q](https://stacks.math.columbia.edu/tag/0B8Q) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.isInvertible_of_isFiniteLocallyFreeOfRank_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InvertibleRankOne.lean, line 485](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InvertibleRankOne.lean#L485). The attribute's comment: “locally free of rank one implies invertible”.

> **Stacks Project, Tag 0B8Q**, the unconditional clause. On the ringed topos of a ringed
> site, a sheaf of modules which is locally free of rank one is invertible.

```lean
theorem isInvertible_of_isFiniteLocallyFreeOfRank_one
    (X : AlgebraicGeometry.RingedSite.{u, v, max u v w})
    (L : SheafOfModules.{max u v w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    (hL : AlgebraicGeometry.RingedSite.IsFiniteLocallyFreeOfRank X L 1) :
    Stacks.SheafOfModules.IsInvertible X.O.obj
      (Stacks.SheafOfModules.Tensor.ringSheaf X.O).property L
```

**`AlgebraicGeometry.RingedSite.isInvertible_iff_isFiniteLocallyFreeOfRank_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InvertibleRankOne.lean, line 733](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InvertibleRankOne.lean#L733). The attribute's comment: “characterization for locally ringed sites”.

> **Stacks Project, Tag 0B8Q**, the characterization clause. On a locally ringed site, a
> sheaf of modules is invertible exactly when it is locally free of rank one.

```lean
theorem isInvertible_iff_isFiniteLocallyFreeOfRank_one
    (X : AlgebraicGeometry.RingedSite.{u, max u v, max u v})
    (L : SheafOfModules.{max u v} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))
    (hX : AlgebraicGeometry.RingedSite.IsLocallyRinged X) :
    Stacks.SheafOfModules.IsInvertible X.O.obj
      (Stacks.SheafOfModules.Tensor.ringSheaf X.O).property L ↔
      AlgebraicGeometry.RingedSite.IsFiniteLocallyFreeOfRank X L 1
```

**`AlgebraicGeometry.RingedSite.exists_isInvertible_not_isFiniteLocallyFreeOfRank_one`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/InvertibleRankOne.lean, line 870](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InvertibleRankOne.lean#L870). The attribute's comment: “the converse fails in general”.

> **Stacks Project, Tag 0B8Q**, the parenthetical clause. Without local ringedness the
> converse fails: there is a ringed site carrying an invertible sheaf of modules which is not
> locally free of rank one.

```lean
theorem exists_isInvertible_not_isFiniteLocallyFreeOfRank_one :
    ∃ (X : AlgebraicGeometry.RingedSite.{u, v, w})
      (L : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)),
      Stacks.SheafOfModules.IsInvertible X.O.obj
        (Stacks.SheafOfModules.Tensor.ringSheaf X.O).property L ∧
        ¬ AlgebraicGeometry.RingedSite.IsFiniteLocallyFreeOfRank X L 1
```

## Tag 04H9, a lemma

[Tag 04H9](https://stacks.math.columbia.edu/tag/04H9) in the Stacks Project.

**`AlgebraicGeometry.RingedSite.HomGeneral.reflectsUnitsObj_of_isLocallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/IsLocallyRingedCriterion.lean, line 209](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/IsLocallyRingedCriterion.lean#L209). The attribute's comment: “(1)⇒(3), independent universes”. References: SGA 4 IV (13.9), “c) (i) ⇒ (ii)”.

> **Stacks 04H9, (1) ⇒ (3) at independent universes.** If a morphism of ringed sites is
> locally ringed, then every left exact functor to sets reflects units for the induced morphism
> `f⁻¹O_Y ⟶ O_X`; at a stalk functor this is locality of the induced map of stalk rings.

```lean
theorem reflectsUnitsObj_of_isLocallyRinged (hf : f.IsLocallyRinged)
    (P : Sheaf X.J (Type w) ⥤ Type t) [PreservesFiniteLimits P] :
    RingedTopos.ReflectsUnitsObj P f.fSharpRingMap
```

**`AlgebraicGeometry.RingedSite.HomGeneral.isLocallyRinged_iff_reflectsUnitsObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/IsLocallyRingedCriterion.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/IsLocallyRingedCriterion.lean#L221). The attribute's comment: “(1)⇔(3) at a conservative family, independent universes”. References: SGA 4 IV (13.9), “c) (i)⇔(ii) enough pts”.

> **Stacks 04H9, (1) ⇔ (3) at independent universes.** For a family of left exact functors to
> sets which detects isomorphisms — in practice the stalk functors at a conservative family of
> points — a morphism of ringed sites is locally ringed exactly when each member reflects units
> for `f⁻¹O_Y ⟶ O_X`.

```lean
theorem isLocallyRinged_iff_reflectsUnitsObj {ι : Type*}
    (P : ι → Sheaf X.J (Type w) ⥤ Type t) (hP : ∀ i, PreservesFiniteLimits (P i))
    [HasPullback (RingedTopos.unitsιOf X.O)
      (RingedTopos.forgetRingMap f.fSharpRingMap)]
    (hcons : ∀ {F G : Sheaf X.J (Type w)} (ψ : F ⟶ G), (∀ i, IsIso ((P i).map ψ)) → IsIso ψ) :
    f.IsLocallyRinged ↔ ∀ i, RingedTopos.ReflectsUnitsObj (P i) f.fSharpRingMap
```

**`Stacks.Sheaves.LocallyRingedTopos.condition1_imp_condition2`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/StalkCriterion.lean, line 572](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/StalkCriterion.lean#L572). The attribute's comment: “(1)⇒(2)”. References: SGA 4 IV (13.9), “c) (i) => (ii)”.

> **Theorem, part 1: (1) ⇒ (2) always holds** (no hypotheses beyond Definition 1).
>
> Each stalk functor `(.)_p = p^{-1}` is exact, hence preserves the cartesian square of
> condition (1); together with the identifications `(f^{-1} O_D)_p = O_{D,q}` and
> `(f^{-1} O_D^*)_p = O_{D,q}^*`, this yields condition (2).

```lean
theorem condition1_imp_condition2 (f : RingedToposHom X Y)
    (h : Condition1 f) : Condition2 f
```

**`Stacks.Sheaves.LocallyRingedTopos.condition1_of_condition2OnFamily`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/StalkCriterion.lean, line 589](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/StalkCriterion.lean#L589). The attribute's comment: “(2)-family⇒(1)”. References: SGA 4 IV (13.9), “c) (ii)⇒(i) conserv fam”.

> **Theorem, part 4 (general case): (2) on a conservative family implies (1).**
>
> If condition (2) holds for every point of a conservative family of points of `C`, then
> condition (1) holds (the family detects cartesianness of the sheaf square).

```lean
theorem condition1_of_condition2OnFamily (f : RingedToposHom X Y)
    (P : ConservativeFamily X) (h : Condition2OnFamily f P) :
    Condition1 f
```

**`Stacks.Sheaves.LocallyRingedTopos.condition1_iff_condition2_of_enoughPoints`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/StalkCriterion.lean, line 657](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/StalkCriterion.lean#L657). The attribute's comment: “(1)⇔(2)”. References: SGA 4 IV (13.9), “c) (i) <=> (ii)”.

> **Theorem, part 2: if `C` has enough points, then (1) ⇔ (2).**
>
> Forward is part 1. Conversely a conservative family of points detects whether a square
> of sheaves is cartesian (cartesianness is preserved and reflected by the exact,
> jointly-conservative stalk functors), so condition (2) forces condition (1).

```lean
theorem condition1_iff_condition2_of_enoughPoints (f : RingedToposHom X Y)
    (hC : HasEnoughPoints X) :
    Condition1 f ↔ Condition2 f
```

**`Stacks.Sheaves.LocallyRingedTopos.condition2_iff_condition3_of_locallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/StalkCriterion.lean, line 911](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/StalkCriterion.lean#L911). The attribute's comment: “(2)⇔(3)”.

> **Theorem, part 3: in the locally ringed case, (2) ⇔ (3).**
>
> When both topoi are locally ringed, every stalk `O_{C,p}` and `O_{D,q}` is a local ring
> (via `IsLocallyRinged.isLocalRing_stalk`, with no enough-points assumption on either
> `C` or `D`), so condition (2) at `p` — the cartesianness of the stalk-of-units-sheaves
> square — is, via the identifications `(O^*)_p = (O_p)^*` (`stalkUnitsIso`), exactly the
> statement that the unit-inclusion square of `phi_p` is cartesian, which by the
> algebraic core lemma is equivalent to `phi_p` being a local ring map.

```lean
theorem condition2_iff_condition3_of_locallyRinged (f : RingedToposHom X Y)
    (hlrC : IsLocallyRinged X) (hlrD : IsLocallyRinged Y) :
    Condition2 f ↔ Condition3 f
```

**`Stacks.Sheaves.LocallyRingedTopos.condition1_of_condition3OnFamily_of_locallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/StalkCriterion.lean, line 926](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/StalkCriterion.lean#L926). The attribute's comment: “(3)-family⇒(1)”. References: SGA 4 IV (13.9), “c) (ii)⇒(i) conserv fam”.

> **Theorem, part 4 (locally ringed case): (3) on a conservative family implies (1).**
>
> If both topoi are locally ringed and `phi_p` is a local ring map for every point `p` of
> a conservative family of points of `C`, then condition (1) holds. No enough-points
> assumption on `D` is needed.

```lean
theorem condition1_of_condition3OnFamily_of_locallyRinged (f : RingedToposHom X Y)
    (hlrC : IsLocallyRinged X) (hlrD : IsLocallyRinged Y)
    (P : ConservativeFamily X) (h : Condition3OnFamily f P) :
    Condition1 f
```

**`AlgebraicGeometry.RingedTopos.isLocalHom_sheafFiber_iff_reflectsUnitsObj`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/StalkReflectsUnits.lean, line 276](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/StalkReflectsUnits.lean#L276). The attribute's comment: “that the two spellings of condition (3) at a single point of the site agree, at independent universes: reflection of units by the set-valued fibre functor is locality of the fibre ring map. Neither implication between conditions (1), (2) and (3) is proved here — the forward half of this equivalence is proved in this file and the converse alongside it; what the statement supplies is the bridge at a site with `C : Type u`, `Category.{v} C` and sections at `w` all independent, which the collapsed formulation of StalkCriterion.lean cannot state”.

> **Stacks 04H9, reflection of units and locality of the stalk map are equivalent, at
> independent universes.**  The fibre functor of `Φ` on sheaves of sets reflects units for `φ`
> exactly when the fibre of `φ` at `Φ` taken in commutative rings is a local ring
> homomorphism.

```lean
theorem isLocalHom_sheafFiber_iff_reflectsUnitsObj {C : Type u} [Category.{v} C]
    {J : GrothendieckTopology C} (Φ : J.Point.{w}) {O₁ O₂ : Sheaf J CommRingCat.{w}}
    (φ : O₁ ⟶ O₂)
    [LocallySmall.{w} C] [J.HasSheafCompose (forget RingCat.{w})]
    [J.HasSheafCompose (forget₂ CommRingCat.{w} RingCat.{w})] :
    IsLocalHom ((Φ.sheafFiber (A := CommRingCat.{w})).map φ).hom ↔
      ReflectsUnitsObj (Φ.sheafFiber (A := Type w)) φ
```

## Tag 04HA, a definition

[Tag 04HA](https://stacks.math.columbia.edu/tag/04HA) in the Stacks Project.

**`AlgebraicGeometry.RingedToposHom.IsLocallyRinged`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/Morphisms.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/Morphisms.lean#L100). The attribute's comment: “morphisms of locally ringed topoi”.

> A morphism of ringed topoi is locally ringed when its square of units subsheaves, over the
> structure map `fSharpSet f`, is cartesian.

```lean
abbrev IsLocallyRinged (f : RingedToposHom X Y) : Prop
```

**`AlgebraicGeometry.RingedSite.Hom.exists_associatedRingedToposHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/Morphisms.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/Morphisms.lean#L156). The attribute's comment: “associated ringed-topos morphism of a ringed-site morphism”. References: SGA 4 IV (13.3.1), “site ⇒ topos morphism”.

> A morphism of ringed sites induces a morphism of ringed topoi whose underlying morphism of
> topoi and whose structure map on underlying sheaves of sets are the given ones.

```lean
theorem exists_associatedRingedToposHom (f : RingedSite.Hom X Y) :
    ∃ g : RingedToposHom (toRingedTopos X) (toRingedTopos Y),
      (g.toToposHom = f.isMorphismOfSites.morphismOfTopoi) ∧
      HEq (RingedToposHom.fSharpSet g) (fSharpSet f)
```

**`AlgebraicGeometry.RingedSite.Hom.IsLocallyRinged`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/Morphisms.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/Morphisms.lean#L191). The attribute's comment: “morphisms of locally ringed sites”.

> A morphism of ringed sites is locally ringed when the units square for its associated morphism
> of ringed topoi is cartesian.

```lean
abbrev IsLocallyRinged (f : RingedSite.Hom X Y) : Prop
```

**`AlgebraicGeometry.RingedSite.HomGeneral.IsLocallyRinged`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/MorphismsGeneral.lean, line 239](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/MorphismsGeneral.lean#L239). The attribute's comment: “morphisms of locally ringed sites, independent universes”.

> **Stacks 04HA** at independent universes.  A morphism of ringed sites is *locally ringed*
> when its square
>
> ```
>   f⁻¹(O_Y^*) ---> O_X^*
>       |             |
>       v             v
>   f⁻¹(O_Y)  ---> O_X
> ```
>
> of units subsheaves is cartesian, the bottom arrow being the structure map on underlying sheaves
> of sets.  The top arrow is not part of the data: the inclusion of units is a monomorphism, so an
> arrow making the square commute is unique if it exists, which is
> `AlgebraicGeometry.RingedSite.HomGeneral.isLocallyRinged_iff_existsUnique`.

```lean
abbrev IsLocallyRinged (f : HomGeneral X Y) : Prop
```

**`AlgebraicGeometry.RingedSite.HomGeneral.exists_associatedRingedToposHom`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/MorphismsGeneral.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/MorphismsGeneral.lean#L291). The attribute's comment: “associated ringed-topos morphism, independent universes”. References: SGA 4 IV (13.3.1), “special case”.

> **Stacks 04HA** at independent universes.  A morphism of ringed sites induces a morphism of
> ringed topoi whose underlying morphism of topoi is `HomGeneral.toposHom` and whose structure map
> on underlying sheaves of sets is `HomGeneral.fSharpSet`.
>
> As in `AlgebraicGeometry.RingedSite.Hom.exists_associatedRingedToposHom`, the statement is
> existential rather than a construction: the structure map of a morphism of ringed sites lands in
> the *restriction* `u^s O_X` along the site functor, whereas a morphism of ringed topoi needs it
> in the direct image `f_* O_X` along the induced morphism of topoi, and those agree only up to
> `Stacks.Sheaves.ToposPullback.restrictionCommRingIso`, which is the identity on underlying
> sheaves of sets but not the identity map of sheaves of commutative rings.

```lean
theorem HomGeneral.exists_associatedRingedToposHom (f : HomGeneral X Y) :
    ∃ g : RingedToposHom (toRingedTopos X) (toRingedTopos Y),
      (g.toToposHom = f.toposHom) ∧ HEq (RingedToposHom.fSharpSet g) f.fSharpSet
```

## Tag 04IG, a lemma

[Tag 04IG](https://stacks.math.columbia.edu/tag/04IG) in the Stacks Project.

**`AlgebraicGeometry.RingedToposHom.isLocallyRinged_comp`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedTopoi/CompositionOfLocallyRingedMorphisms.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedTopoi/CompositionOfLocallyRingedMorphisms.lean#L87).

> **Stacks 04IG.** A composite of locally ringed morphisms of ringed topoi is locally
> ringed.

```lean
theorem isLocallyRinged_comp (g : RingedToposHom Y Z) (f : RingedToposHom X Y)
    (hg : IsLocallyRinged g) (hf : IsLocallyRinged f) :
    IsLocallyRinged (g.comp f)
```

## Tag 04KR, a lemma

[Tag 04KR](https://stacks.math.columbia.edu/tag/04KR) in the Stacks Project.

**`AlgebraicGeometry.inverseImage_units_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/UnitsSheafInverseImage.lean, line 432](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/UnitsSheafInverseImage.lean#L432). The attribute's comment: “inverse image of the units subsheaf”.

> **Stacks 04KR: the inverse image of the units subsheaf.** There is exactly one isomorphism
> of the inverse image of the units subsheaf of `Y` with the units subsheaf of the inverse-image
> ringed topos compatible with the inclusions into the structure sheaves; it is therefore the
> canonical one.

```lean
theorem inverseImage_units_iso :
    ∃! e : f.inverseImage.obj (RingedTopos.units Y) ≅
        RingedTopos.units (inverseImageRingedTopos C J Y f),
      e.hom ≫ RingedTopos.unitsι (inverseImageRingedTopos C J Y f) =
        f.inverseImage.map (RingedTopos.unitsι Y) ≫ (inverseImageForgetIso J Y f).hom
```

**`AlgebraicGeometry.inverseImageRingedToposHom_isLocallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/UnitsSheafInverseImage.lean, line 458](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/UnitsSheafInverseImage.lean#L458). The attribute's comment: “canonical morphism of locally ringed topoi”.

> **Stacks 04KR: the canonical morphism is a morphism of locally ringed topoi.** Its structure
> map on underlying sheaves of sets is an isomorphism, so its square of units subsheaves is
> cartesian as soon as the comparison of units subsheaves exists.

```lean
theorem inverseImageRingedToposHom_isLocallyRinged :
    RingedToposHom.IsLocallyRinged (inverseImageRingedToposHom C J Y f)
```

Declarations registered for the tag:

- [`AlgebraicGeometry.inverseImageRingedToposHom`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/InverseImage/RingedTopos.lean#L62), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Modules/UnitsSheafInverseImage.lean, line 480](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/UnitsSheafInverseImage.lean#L480) (StacksFrontier): “canonical ringed-topos morphism”.

## Tag 04IH, a lemma

[Tag 04IH](https://stacks.math.columbia.edu/tag/04IH) in the Stacks Project.

**`Stacks.Sheaves.LocalizedRingedTopos.isLocallyRingedSite_localizedRingedTopos`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalizedRingedToposLocallyRinged.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/LocalizedRingedToposLocallyRinged.lean#L75). The attribute's comment: “(5), first assertion: the localization at a sheaf is again locally ringed”.

> The localization of a locally ringed topos at a sheaf is again a locally ringed topos.

```lean
theorem isLocallyRingedSite_localizedRingedTopos (X :
  Stacks.Sheaves.LocallyRingedTopos.RingedTopos.{u})
    (F : X.Topos) (hX : IsLocallyRingedSite X) :
    IsLocallyRingedSite (localizedRingedTopos X F)
```

**`AlgebraicGeometry.RingedSite.localizationRingedToposHom_isLocallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Recovery04IH/LocalizationMorphismsLocallyRinged.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Recovery04IH/LocalizationMorphismsLocallyRinged.lean#L90). The attribute's comment: “(1), second assertion: the localization morphism `(j_U, j_U♯)` is a morphism of locally ringed topoi”.

> **Stacks 04IH (1), second assertion.** The localization morphism `(j_U, j_U♯)` of a ringed
> site at an object `U` is a morphism of locally ringed topoi: its structure map is the identity
> on underlying sheaves of sets, and the inverse image of the units subsheaf is the units
> subsheaf, so the units square is a square of identities.

```lean
theorem localizationRingedToposHom_isLocallyRinged (U : X.C) :
    (X.localizationRingedToposHom U).IsLocallyRinged
```

**`AlgebraicGeometry.RingedSite.relocalizationRingedToposHom_isLocallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Recovery04IH/LocalizationMorphismsLocallyRinged.lean, line 112](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Recovery04IH/LocalizationMorphismsLocallyRinged.lean#L112). The attribute's comment: “(2): the morphism `(j, j♯)` of 04IY is a morphism of locally ringed topoi”.

> **Stacks 04IH (2).** The morphism `(j, j♯) : (Sh(C/V), O_V) → (Sh(C/U), O_U)` of Stacks 04IY,
> the relocalization of a ringed site along a morphism `f : V ⟶ U` of its underlying category, is
> a morphism of locally ringed topoi. As for the localization morphism, the units square is a
> square of identities.

```lean
theorem relocalizationRingedToposHom_isLocallyRinged (f : V ⟶ U) :
    (X.relocalizationRingedToposHom f).IsLocallyRinged
```

**`AlgebraicGeometry.RingedTopos.localizationMorphism_isLocallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Recovery04IH/LocalizationMorphismsLocallyRinged.lean, line 139](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Recovery04IH/LocalizationMorphismsLocallyRinged.lean#L139). The attribute's comment: “(5), second assertion: the localization morphism `(j_F, j_F♯)` is a morphism of locally ringed topoi”.

> **Stacks 04IH (5), second assertion.** The localization morphism
> `(j_F, j_F♯) : (Sh(C)/F, O_F) → (Sh(C), O)` of a ringed topos at a sheaf is a morphism of
> locally ringed topoi: the site of elements carries the restriction of the structure sheaf, so
> the structure map is the identity on underlying sheaves of sets and the units square is a
> square of identities.

```lean
theorem localizationMorphism_isLocallyRinged :
    (localizationMorphism X F).IsLocallyRinged
```

**`AlgebraicGeometry.RingedSite.Hom.localized_isLocallyRinged_sites`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Recovery04IH/LocalizedMorphismLocallyRinged.lean, line 198](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Recovery04IH/LocalizedMorphismLocallyRinged.lean#L198). The attribute's comment: “part (3): the localization of a morphism of locally ringed sites”.

> For a morphism of *locally ringed* sites `(f, f^#)` and an
> object `V` of the target, the two localized sites `(C/U, O_U)` and `(D/V, O'_V)` are locally
> ringed sites and the localized morphism `(f', (f')^#)` of Stacks 04J0 is a locally ringed
> morphism.

```lean
theorem localized_isLocallyRinged_sites (hX : RingedSite.IsLocallyRinged X)
    (hY : RingedSite.IsLocallyRinged Y) (hf : f.IsLocallyRinged) :
    RingedSite.IsLocallyRinged (X.over (f.u.obj V)) ∧
      RingedSite.IsLocallyRinged (Y.over V) ∧ (f.localized V).IsLocallyRinged
```

**`AlgebraicGeometry.RingedSite.Hom.localizedRingedToposHom_isLocallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Recovery04IH/LocalizedMorphismsLocallyRinged.lean, line 203](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Recovery04IH/LocalizedMorphismsLocallyRinged.lean#L203). The attribute's comment: “(3): the localized morphism `f'` of 04J0 is a morphism of locally ringed sites”.

> **Stacks 04IH (3).** The localized morphism `(f', (f')♯)` of Stacks 04J0 is a morphism of
> locally ringed sites as soon as `(f, f♯)` is: its units square is the image under the exact
> functor `j_U^{-1}` of the units square of `f`, with the two bottom edges matched by Stacks 03CF's
> clause (b).
>
> The units subsheaf of a localization, and its inclusion, are the restrictions of those of the
> original ringed site on the nose, so the only comparison entering is clause (b), whose two
> components form a square of isomorphisms on the left of the pasting.

```lean
theorem Hom.localizedRingedToposHom_isLocallyRinged (V : Y.C)
    (hf : f.ringedToposHom.IsLocallyRinged) :
    (f.localizedRingedToposHom V).IsLocallyRinged
```

**`AlgebraicGeometry.RingedSite.Hom.relocalized_isLocallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Recovery04IH/LocalizedMorphismsLocallyRinged.lean, line 224](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Recovery04IH/LocalizedMorphismsLocallyRinged.lean#L224). The attribute's comment: “(4): the relocalized morphism `f_c` of 04J1 is a morphism of locally ringed topoi”.

> **Stacks 04IH (4).** The relocalized morphism `(f_c, f_c♯)` of Stacks 04J1 is a morphism of
> locally ringed topoi as soon as `(f, f♯)` is a morphism of locally ringed sites.
>
> This is Stacks' "follows formally on combining (2) and (3)": `f_c` is by definition the localized
> morphism of Stacks 04J0 composed with the relocalization morphism of Stacks 04IY along `c`, the
> first locally ringed by clause (3) and the second by clause (2), and a composite of locally ringed
> morphisms is locally ringed by Stacks 04IG.

```lean
theorem Hom.relocalized_isLocallyRinged {U : X.C} {V : Y.C} (c : U ⟶ f.u.obj V)
    (hf : f.ringedToposHom.IsLocallyRinged) :
    (f.relocalized c).IsLocallyRinged
```

**`AlgebraicGeometry.RingedToposHom.localized_isLocallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Recovery04IH/LocalizedMorphismsLocallyRinged.lean, line 282](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Recovery04IH/LocalizedMorphismsLocallyRinged.lean#L282). The attribute's comment: “(7): the localized morphism `f'` of 04IF is a morphism of locally ringed topoi”.

> **Stacks 04IH (7).** The localized morphism `(f', (f')♯)` of Stacks 04IF is a morphism of
> locally ringed topoi as soon as `(f, f♯)` is: its units square is the image under the exact
> functor `j_{f⁻¹G}⁻¹` of the units square of `f`, with the two bottom edges matched by 04IF's
> comparison of inverse images.
>
> The units subsheaf of a localization, and its inclusion, are the inverse image of those of the
> original ringed topos on the nose, so the only comparison entering is 04IF's, whose two
> components form a square of isomorphisms on the left of the pasting.

```lean
theorem localized_isLocallyRinged (hf : f.IsLocallyRinged) :
    (f.localized G).IsLocallyRinged
```

**`AlgebraicGeometry.RingedToposHom.relocalized_isLocallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Recovery04IH/LocalizedMorphismsLocallyRinged.lean, line 300](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Recovery04IH/LocalizedMorphismsLocallyRinged.lean#L300). The attribute's comment: “(8): the relocalized morphism `f_s` of 04J8 is a morphism of locally ringed topoi”.

> **Stacks 04IH (8).** The relocalized morphism `(f_s, f_s♯)` of Stacks 04J8 is a morphism of
> locally ringed topoi as soon as `(f, f♯)` is.
>
> Stacks 04J8 defines `f_s` as the morphism of 04IF composed with the relocalization morphism of
> 04J4 along `s`, the first locally ringed by clause (7) and the second by clause (6), and a
> composite of locally ringed morphisms is locally ringed by Stacks 04IG.

```lean
theorem relocalized_isLocallyRinged {F : X.Topos}
    (s : F ⟶ f.toToposHom.inverseImage.obj G) (hf : f.IsLocallyRinged) :
    (f.relocalized s).IsLocallyRinged
```

**`AlgebraicGeometry.RingedTopos.localizedRingedTopos_isLocallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Recovery04IH/ToposLocalizationLocallyRinged.lean, line 81](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Recovery04IH/ToposLocalizationLocallyRinged.lean#L81). The attribute's comment: “(5), first assertion: the localization `(Sh(C)/F, O_F)` of a locally ringed topos at a sheaf is again a locally ringed topos, in the categorical spelling of local ringedness”.

> **Stacks 04IH (5), first assertion.** The localization `(Sh(C)/F, O_F)` of a locally ringed
> topos at a sheaf of sets is again a locally ringed topos: its structure sheaf is the inverse
> image of `O` along the localization morphism of topoi, and local ringedness passes to an inverse
> image.

```lean
theorem localizedRingedTopos_isLocallyRinged (X : RingedTopos.{u, u, u}) (F : X.Topos)
    (hX : RingedSite.IsLocallyRinged (toRingedSite X)) :
    RingedSite.IsLocallyRinged (toRingedSite (localizedRingedTopos X F))
```

**`AlgebraicGeometry.RingedTopos.relocalizationMorphism_isLocallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Recovery04IH/ToposRelocalization.lean, line 206](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Recovery04IH/ToposRelocalization.lean#L206). The attribute's comment: “(6): the morphism `(j, j♯)` of 04J4 is a morphism of locally ringed topoi”.

> **Stacks 04IH (6).** The morphism
> `(j, j♯) : (Sh(C)/G, O_G) → (Sh(C)/F, O_F)` of Stacks 04J4, the relocalization of a ringed topos
> along a morphism `s : G ⟶ F` of sheaves, is a morphism of locally ringed topoi: its structure
> map is the identity on underlying sheaves of sets and the inverse image of the units subsheaf is
> the units subsheaf, so the units square is a square of identities.

```lean
theorem relocalizationMorphism_isLocallyRinged (s : G ⟶ F) :
    (X.relocalizationMorphism s).IsLocallyRinged
```

**`AlgebraicGeometry.RingedSite.isLocallyRinged_over`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/Localization.lean, line 140](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/Localization.lean#L140). The attribute's comment: “(1), first assertion: the localization `(C/U, O_U)` of a locally ringed site is again a locally ringed site”.

> **Stacks 04IH (1), first assertion.** A localization `(C/U, O_U)` of a locally ringed site
> is again a locally ringed site.

```lean
theorem isLocallyRinged_over (X : RingedSite.{u, v, w}) (U : X.C)
    (hX : IsLocallyRinged X) : IsLocallyRinged (X.over U)
```

**`Stacks.Sheaves.LocallyRingedSite.localizedRingedTopos_isLocallyRinged`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/OneIsNeverZero.lean, line 249](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Modules/LocallyRingedSites/OneIsNeverZero.lean#L249). The attribute's comment: “(5), first assertion, with condition (1) in the source's sheaf-level spelling of 05D7”.

> If the morphism of Tag 05D7 is an isomorphism for `X` and the conditions of Tag 04ES hold, then
> both hold for the localization of `X` at a sheaf `F`.

```lean
theorem localizedRingedTopos_isLocallyRinged (F : X.Topos)
    (hX : IsIso (oneIsNeverZero X.J X.O) ∧ Stacks.Sheaves.LocallyRingedSite.Condition1 X.O) :
    IsIso (oneIsNeverZero (LocalizedRingedTopos.localizedRingedTopos X F).J
        (LocalizedRingedTopos.localizedRingedTopos X F).O) ∧
      Stacks.Sheaves.LocallyRingedSite.Condition1 (LocalizedRingedTopos.localizedRingedTopos X F).O
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.40, Tag 04ER](https://stacks.math.columbia.edu/tag/04ER)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
