---
declaration: section
origin: cited
lean: AlgebraicGeometry.exists_isFiniteType_idealSheafData_support_eq_compl, AlgebraicGeometry.isCompact_iff_exists_finset_affineOpens, AlgebraicGeometry.isCompact_of_isFiniteType_idealSheafData, QuasiSeparatedSpace.isRetrocompact_iff_isCompact, AlgebraicGeometry.isCompact_iff_finite_and_eq_biUnion_affineOpens, Stacks.AlgebraicGeometry.AnnihilatorQcoh.isAnnihilatorSubsheaf_sSup, Stacks.AlgebraicGeometry.AnnihilatorQcoh.IsAnnihilatorSubsheaf.mem_iff_of_isAffineOpen, Stacks.AlgebraicGeometry.AnnihilatorQcoh.IsAnnihilatorSubsheaf.isQuasicoherent
statement: formalized
proof: formalized
---

# 28.25 Sections with support in a closed subset

Section 28.25 of the Stacks Project, [Tag 07ZM](https://stacks.math.columbia.edu/tag/07ZM). 7 tags here are carried by 22 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01PH, a lemma

[Tag 01PH](https://stacks.math.columbia.edu/tag/01PH) in the Stacks Project.

**`AlgebraicGeometry.exists_isFiniteType_idealSheafData_support_eq_compl`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/QuasiCompactOpenIdeal.lean, line 320](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/QuasiCompactOpenIdeal.lean#L320). The attribute's comment: “(2) ⟹ (4)”.

> **A quasi-compact open of a quasi-compact quasi-separated scheme is the complement of the
> vanishing locus of a finite type quasi-coherent sheaf of ideals.**

```lean
theorem exists_isFiniteType_idealSheafData_support_eq_compl
    [CompactSpace X] [QuasiSeparatedSpace X] (U : X.Opens) (hU : IsCompact (U : Set X)) :
    ∃ I : X.IdealSheafData, I.IsFiniteType ∧ (I.support : Set X) = (U : Set X)ᶜ
```

**`AlgebraicGeometry.isCompact_iff_exists_finset_affineOpens`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/RetrocompactOpen.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/RetrocompactOpen.lean#L65). The attribute's comment: “(2) ↔ (3)”. References: EGA IV (1.8.1), “qc open ⟺ finite ∪ aff”.

> **An open of a scheme is quasi-compact exactly when it is a finite union of affine
> opens.**

```lean
theorem isCompact_iff_exists_finset_affineOpens (U : X.Opens) :
    IsCompact (U : Set X) ↔ ∃ s : Finset X.affineOpens, U = s.sup fun V => (V : X.Opens)
```

**`AlgebraicGeometry.isCompact_of_isFiniteType_idealSheafData`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/RetrocompactOpen.lean, line 116](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/RetrocompactOpen.lean#L116). The attribute's comment: “(4) ⟹ (2)”.

> **An open subscheme of a quasi-compact scheme whose complement is the vanishing locus of a
> finite type quasi-coherent sheaf of ideals is quasi-compact.**

```lean
theorem isCompact_of_isFiniteType_idealSheafData [CompactSpace X] (U : X.Opens)
    (I : X.IdealSheafData) (hI : I.IsFiniteType)
    (hsupp : (I.support : Set X) = (U : Set X)ᶜ) : IsCompact (U : Set X)
```

Declarations registered for the tag:

- [`QuasiSeparatedSpace.isRetrocompact_iff_isCompact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=QuasiSeparatedSpace.isRetrocompact_iff_isCompact#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/RetrocompactOpen.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/ExtendFiniteType/RetrocompactOpen.lean#L50) (StacksFrontier): “(1) ↔ (2)”. References: EGA 0 (9.1.6); SGA 3 VIA (2.6.3), “special case”.
- [`QuasiSeparatedSpace.isRetrocompact_iff_isCompact`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=QuasiSeparatedSpace.isRetrocompact_iff_isCompact#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Sheaves/SectionsWithSupport/QuasiCompactOpenIdealSheaf.lean, line 36](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Sheaves/SectionsWithSupport/QuasiCompactOpenIdealSheaf.lean#L36) (StacksFrontier): “retrocompact iff quasi-compact”. References: EGA 0 (9.1.6); SGA 3 VIA (2.6.3), “special case”.
- [`AlgebraicGeometry.isCompact_iff_finite_and_eq_biUnion_affineOpens`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=AlgebraicGeometry.isCompact_iff_finite_and_eq_biUnion_affineOpens#doc) registered with `add_to_stacks` in [StacksFrontier/AlgebraicGeometry/Sheaves/SectionsWithSupport/QuasiCompactOpenIdealSheaf.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Sheaves/SectionsWithSupport/QuasiCompactOpenIdealSheaf.lean#L38) (StacksFrontier): “quasi-compact iff finite union of affine opens”. References: EGA I (1.1.10), “more general”; EGA IV (1.8.1).

## Tag 01PO, a lemma

[Tag 01PO](https://stacks.math.columbia.edu/tag/01PO) in the Stacks Project.

**`Stacks.AlgebraicGeometry.AnnihilatorQcoh.isAnnihilatorSubsheaf_sSup`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AnnihilatorQcoh/Basic.lean, line 169](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AnnihilatorQcoh/Basic.lean#L169). The attribute's comment: “the subsheaf”.

> **The subsheaf of [Stacks, Tag 01PO]: the largest submodule sheaf of `F` that `I`
> annihilates, and its sections.** The supremum is taken in the complete lattice of submodule
> sheaves of `F`, and the conclusion unfolds to the statement that a section over `U` belongs to
> it exactly when every restriction of it is annihilated by the sections of `I` there.
>
> That this supremum is the *only* submodule sheaf with those sections is
> `IsAnnihilatorSubsheaf.unique`, and `isAnnihilatorSubsheaf_annihilatorSubmodule` exhibits a
> second, explicit model of it. Neither quasi-coherence nor finiteness is used.

```lean
theorem isAnnihilatorSubsheaf_sSup
    (I : (SheafOfModules.unit.{u} X.ringCatSheaf).Submodule) (F : X.Modules) :
    IsAnnihilatorSubsheaf I F
      (sSup {N : F.Submodule | ∀ (U : X.Opens) (s : Γ(F, U)),
        s ∈ N.toSubmodule.obj (op U) →
          ∀ a : Γ(X, U), a ∈ I.toSubmodule.obj (op U) → a • s = 0})
```

**`Stacks.AlgebraicGeometry.AnnihilatorQcoh.IsAnnihilatorSubsheaf.mem_iff_of_isAffineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AnnihilatorQcoh/Basic.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AnnihilatorQcoh/Basic.lean#L345). The attribute's comment: “part (2)”.

> **Part (2) of [Stacks, Tag 01PO].** Over an affine open `U`, the sections of the annihilator
> subsheaf are exactly the sections of `F` annihilated by `Γ(I, U)`; no restriction has to be
> tested.

```lean
theorem IsAnnihilatorSubsheaf.mem_iff_of_isAffineOpen {N : F.Submodule}
    (hN : IsAnnihilatorSubsheaf I F N) [I.toSheafOfModules.IsQuasicoherent]
    {U : X.Opens} (hU : IsAffineOpen U) (s : Γ(F, U)) :
    s ∈ N.toSubmodule.obj (op U) ↔
      ∀ a : Γ(X, U), a ∈ I.toSubmodule.obj (op U) → a • s = 0
```

**`Stacks.AlgebraicGeometry.AnnihilatorQcoh.IsAnnihilatorSubsheaf.isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AnnihilatorQcoh/Qcoh.lean, line 160](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AnnihilatorQcoh/Qcoh.lean#L160). The attribute's comment: “part (1)”.

> **Part (1) of [Stacks, Tag 01PO].** The subsheaf of sections of a quasi-coherent module
> annihilated by a quasi-coherent ideal sheaf of finite type is quasi-coherent.
>
> Such a subsheaf exists for every `I` and `F` (`isAnnihilatorSubsheaf_annihilatorSubmodule`) and
> is unique (`IsAnnihilatorSubsheaf.unique`), so the hypothesis `hN` is not a restriction.

```lean
theorem IsAnnihilatorSubsheaf.isQuasicoherent (hN : IsAnnihilatorSubsheaf I F N)
    [I.toSheafOfModules.IsQuasicoherent] [I.toSheafOfModules.IsFiniteType] [F.IsQuasicoherent] :
    N.toSheafOfModules.IsQuasicoherent
```

**`Stacks.AlgebraicGeometry.AnnihilatorQcoh.IsAnnihilatorSubsheaf.exists_stalk_eq_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/AnnihilatorQcoh/Stalk.lean, line 172](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/AnnihilatorQcoh/Stalk.lean#L172). The attribute's comment: “part (3)”.

> **Part (3) of [Stacks, Tag 01PO].** A germ of `F` at `x` lies in the image of the stalk of
> the annihilator subsheaf exactly when every section of `I` over a neighbourhood of `x`
> annihilates every representative of that germ, to first order at `x`.
>
> Quasi-coherence of `F` is not needed: the forward implication uses no hypothesis beyond the
> sheaf axiom, and the backward one goes through the affine description of the sections of `N`,
> which needs only `I`.

```lean
theorem IsAnnihilatorSubsheaf.exists_stalk_eq_iff (hN : IsAnnihilatorSubsheaf I F N)
    [I.toSheafOfModules.IsQuasicoherent] [I.toSheafOfModules.IsFiniteType]
    (x : X) (s : F.presheaf.stalk x) :
    (∃ t : (Scheme.Modules.presheaf N.toSheafOfModules).stalk x,
        (TopCat.Presheaf.stalkFunctor Ab.{u} x).map
          (Scheme.Modules.Hom.mapPresheaf N.ι) t = s) ↔
      ∀ (U : X.Opens) (hx : x ∈ U) (t : Γ(F, U)), F.presheaf.germ U x hx t = s →
        ∀ r : Γ(X, U), r ∈ I.toSubmodule.obj (op U) →
          F.presheaf.germ U x hx (r • t) = 0
```

**`Stacks.AlgebraicGeometry.IdealPowerColimit.isQuasicoherent_idealAnnihilator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/AnnihilatorQuasicoherent.lean, line 314](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/AnnihilatorQuasicoherent.lean#L314). The attribute's comment: “(1)”.

> **[Stacks, Tag 01PO] (1).** For a quasi-coherent sheaf of ideals `I` of finite type on a
> scheme and a quasi-coherent `𝒪_X`-module `F`, the subsheaf of sections annihilated by `I` is
> quasi-coherent.
>
> Assertion (2) of the tag is `mem_idealAnnihilator_affineOpen` below.  Assertion (3), the
> description of the stalks, is not proved, so this is a clause tag.

```lean
theorem isQuasicoherent_idealAnnihilator (I : X.IdealSheafData) (F : X.Modules)
    [F.IsQuasicoherent] (hFG : ∀ U : X.affineOpens, (I.ideal U).FG) :
    (idealPowerAnnihilator I.unitSubmodule F 1).toSheafOfModules.IsQuasicoherent
```

**`Stacks.AlgebraicGeometry.IdealPowerColimit.mem_idealAnnihilator_affineOpen`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/AnnihilatorQuasicoherent.lean, line 326](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Coherent/HomColimit/AnnihilatorQuasicoherent.lean#L326). The attribute's comment: “(2)”.

> **[Stacks, Tag 01PO] (2).** On an affine open `U` the subsheaf of sections annihilated by `I`
> consists of the sections of `F` over `U` annihilated by `I(U)`.
>
> No finiteness hypothesis is needed for this half: it is
> `mem_idealPowerAnnihilator_affineOpen` at `n = 1`, and `idealPower_unitSubmodule_one` identifies
> the ideal sheaf being annihilated with `I` rather than its first power.

```lean
theorem mem_idealAnnihilator_affineOpen (I : X.IdealSheafData) (F : X.Modules)
    (V : X.affineOpens) (s : Γ(F, V.1)) :
    s ∈ (idealPowerAnnihilator I.unitSubmodule F 1).toSubmodule.obj (op V.1) ↔
      ∀ a ∈ (I.ideal V : Ideal Γ(X, V.1)), a • s = 0
```

**`AlgebraicGeometry.mem_annihilatorSubsheaf_iff`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Extend/IdealAnnihilator.lean, line 138](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Extend/IdealAnnihilator.lean#L138). The attribute's comment: “the subsheaf”.

> Membership in the annihilator subsheaf means that, on every smaller open,
> every section of the ideal annihilates the restricted section.

```lean
lemma mem_annihilatorSubsheaf_iff [Mono i] (U : X.Opens) (s : Γ(F, U)) :
    s ∈ (annihilatorSubsheaf I F i).toSubmodule.obj (op U) ↔
      ∀ (V : X.Opens) (f : V ⟶ U) (r : Γ(I, V)),
        (show Γ(X, V) from i.app V r) • F.presheaf.map f.op s = 0
```

**`AlgebraicGeometry.mem_annihilatorSubsheaf_iff_of_isAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Extend/IdealAnnihilatorQuasicoherent.lean, line 327](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Extend/IdealAnnihilatorQuasicoherent.lean#L327). The attribute's comment: “part (2)”.

> **Stacks, Tag 01PO (2).** On an affine open it suffices to test annihilation by the sections
> of the ideal over that open itself.

```lean
theorem mem_annihilatorSubsheaf_iff_of_isAffine [I.IsQuasicoherent] (U : X.affineOpens)
    (s : Γ(F, U.1)) :
    s ∈ (annihilatorSubsheaf I F i).toSubmodule.obj (op U.1) ↔
      ∀ r : Γ(I, U.1), (show Γ(X, U.1) from i.app U.1 r) • s = 0
```

**`AlgebraicGeometry.annihilatorSubsheaf_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Extend/IdealAnnihilatorQuasicoherent.lean, line 415](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Extend/IdealAnnihilatorQuasicoherent.lean#L415). The attribute's comment: “part (1)”.

> **Stacks, Tag 01PO (1).** The subsheaf of sections annihilated by a quasi-coherent ideal
> sheaf of finite type is quasi-coherent.

```lean
theorem annihilatorSubsheaf_isQuasicoherent [I.IsQuasicoherent] [I.IsFiniteType]
    [F.IsQuasicoherent] :
    (annihilatorSubsheaf I F i).toSheafOfModules.IsQuasicoherent
```

**`AlgebraicGeometry.mem_range_stalk_annihilatorSubsheaf_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Extend/IdealAnnihilatorQuasicoherent.lean, line 509](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Extend/IdealAnnihilatorQuasicoherent.lean#L509). The attribute's comment: “part (3)”.

> **Stacks, Tag 01PO (3).** The germs of the annihilator subsheaf at a point are exactly the
> germs of `F` annihilated by the stalk of the ideal.

```lean
theorem mem_range_stalk_annihilatorSubsheaf_iff [I.IsQuasicoherent] [I.IsFiniteType]
    [F.IsQuasicoherent] (x : X) (s : F.presheaf.stalk x) :
    (∃ t : (Scheme.Modules.presheaf (annihilatorSubsheaf I F i).toSheafOfModules).stalk x,
      ((TopCat.Presheaf.stalkFunctor Ab x).map
        (Scheme.Modules.Hom.mapPresheaf (annihilatorSubsheaf I F i).ι)).hom t = s) ↔
      ∀ (U : X.Opens) (hx : x ∈ U) (t : Γ(F, U)), F.presheaf.germ U x hx t = s →
        ∀ r : Γ(I, U), F.presheaf.germ U x hx ((show Γ(X, U) from i.app U r) • t) = 0
```

## Tag 01PP, a definition

[Tag 01PP](https://stacks.math.columbia.edu/tag/01PP) in the Stacks Project.

**`AlgebraicGeometry.annihilatorSubsheaf`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Extend/IdealAnnihilator.lean, line 129](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Extend/IdealAnnihilator.lean#L129). The attribute's comment: “the subsheaf of sections annihilated by I”.

> The subsheaf of `F` whose sections are annihilated by the ideal sheaf `I`: the largest
> submodule all of whose sections are killed by the sections of `I` over the same open.

```lean
noncomputable def annihilatorSubsheaf [Mono i] : F.Submodule
```

## Tag 07ZN, a lemma

[Tag 07ZN](https://stacks.math.columbia.edu/tag/07ZN) in the Stacks Project.

**`AlgebraicGeometry.pushforward_annihilatorSubsheaf_range_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/QuasiCoherent/Extend/IdealAnnihilatorPushforward.lean, line 322](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/QuasiCoherent/Extend/IdealAnnihilatorPushforward.lean#L322).

> **Stacks Project, Tag 07ZN.** Pushing forward the annihilator of the extended ideal gives
> the annihilator of the original ideal, as subobjects of the pushed-forward module.

```lean
theorem pushforward_annihilatorSubsheaf_range_eq
    {X Y : Scheme.{u}} (f : X ⟶ Y) (I : Y.Modules)
    (i : I ⟶ SheafOfModules.unit Y.ringCatSheaf) [Mono i]
    (F : X.Modules) (U : Y.Opens) :
    Set.range (((Scheme.Modules.pushforward f).map
      (annihilatorSubsheaf
        (extendedIdealSheaf f I i) F
        (extendedIdealSheafι f I i)).ι).app U) =
    Set.range (((annihilatorSubsheaf I
      ((Scheme.Modules.pushforward f).obj F) i).ι).val.app (op U))
```

## Tag 07ZP, a lemma

[Tag 07ZP](https://stacks.math.columbia.edu/tag/07ZP) in the Stacks Project.

**`AlgebraicGeometry.supportedSectionsSubmodule_isQuasicoherent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/SupportedSections/Basic.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/SupportedSections/Basic.lean#L82). The attribute's comment: “supported\_sections\_is\_quasicoherent”.

> The subsheaf of sections supported on a closed subset with retrocompact complement is
> quasicoherent.

```lean
public theorem supportedSectionsSubmodule_isQuasicoherent {X : Scheme.{u}} (Z : Set X)
    (hZ : IsClosed Z) (hZc : IsRetrocompact Zᶜ) (F : X.Modules) [F.IsQuasicoherent] :
    (AlgebraicGeometry.Scheme.Modules.supportedSectionsSubmodule Z
      F).toSheafOfModules.IsQuasicoherent
```

**`AlgebraicGeometry.mem_supportedSectionsSubmodule_iff_exists_pow_le_annihilator`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Divisors/SupportedSections/Basic.lean, line 171](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Divisors/SupportedSections/Basic.lean#L171). The attribute's comment: “the supported sections over an affine open are the ideal-power torsion”.

> **Stacks 07ZP, the torsion description of the supported sections.** Let `Z` be a subset of
> a scheme `X`, let `U` be an affine open and let `I ⊆ 𝒪_X(U)` be a finitely generated ideal
> whose zero locus meets `U` in `Z`. A section of a quasi-coherent `𝒪_X`-module over `U` has all
> its germs outside `Z` equal to zero exactly when some power of `I` annihilates it.
>
> Such an `I` exists for every closed `Z` with retrocompact complement, by
> `AlgebraicGeometry.exists_fg_ideal_zeroLocus_eq_inter`; so the two together are the tag's
> description of the sections of the supported-section subsheaf over an affine open.

```lean
theorem mem_supportedSectionsSubmodule_iff_exists_pow_le_annihilator {X : Scheme.{u}}
    (Z : Set X) (F : X.Modules) [F.IsQuasicoherent] {U : X.Opens} (hU : IsAffineOpen U)
    {I : Ideal Γ(X, U)} (hIfg : I.FG)
    (hI : Z ∩ (U : Set X) = X.zeroLocus (U := U) (I : Set Γ(X, U)) ∩ (U : Set X))
    (s : Γ(F, U)) :
    s ∈ (supportedSectionsSubmodule Z F).toSubmodule.obj (op U) ↔
      ∃ n : ℕ, ∀ a ∈ I ^ n, a • s = 0
```

**`AlgebraicGeometry.exists_fg_ideal_zeroLocus_eq_inter`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Properties/ClosedSubsetIdeal.lean, line 35](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Properties/ClosedSubsetIdeal.lean#L35). The attribute's comment: “finite\_ideal\_for\_closed\_subset\_on\_affine”.

> On an affine open of a scheme, a closed subset with retrocompact complement is the
> zero locus of a finitely generated ideal of the ring of sections.

```lean
lemma exists_fg_ideal_zeroLocus_eq_inter (X : Scheme.{u}) (Z : Set X)
    (hZ : IsClosed Z) (hZc : IsRetrocompact Zᶜ) (U : X.Opens) (hU : IsAffineOpen U) :
    ∃ I : Ideal Γ(X, U), I.FG ∧
      Z ∩ (U : Set X) = X.zeroLocus (U := U) I ∩ (U : Set X)
```

**`AlgebraicGeometry.mem_supportedSectionsSubmodule_zeroLocus_span_singleton_iff`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/StrictTransform/AffinePrincipalTorsion.lean, line 136](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/StrictTransform/AffinePrincipalTorsion.lean#L136). The attribute's comment: “the sections supported on V(a) are the a-power torsion”.

> **The sections supported on a principal zero locus are the torsion for the powers of its
> generator.** A global section of a quasi-coherent module on `Spec R` has all its germs outside
> `V(a)` zero exactly when some power of `a` kills it.
>
> This is the affine-open description of [Stacks, Tag 07ZP] at the ideal `(a)`, which is finitely
> generated; the passage from a power of the ideal to a power of the element is
> `Ideal.span_singleton_pow`.

```lean
public lemma mem_supportedSectionsSubmodule_zeroLocus_span_singleton_iff
    (F : (Spec R).Modules) [F.IsQuasicoherent] (a : R) (s : Γ(F, ⊤)) :
    s ∈ (supportedSectionsSubmodule (principalZeroLocus R a) F).toSubmodule.obj (op ⊤) ↔
      ∃ n : ℕ, a ^ n • s = 0
```

## Tag 084L, a definition

[Tag 084L](https://stacks.math.columbia.edu/tag/084L) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.supportedSectionsSubmodule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Modules/SupportedSections.lean, line 66](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Modules/SupportedSections.lean#L66).

> The sub-`𝒪`-module sheaf of `F` whose local sections have all their germs outside `Z`
> equal to zero.

```lean
public noncomputable def supportedSectionsSubmodule (Z : Set X)
    (F : X.Modules) : F.Submodule
```

**`AlgebraicGeometry.SheafOfModules.supportedSectionsSubmodule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Modules/SupportedSubmodule.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Modules/SupportedSubmodule.lean#L64).

> The submodule of sections of `F` supported on `Z`: its sections over an open `U` are the
> sections of `F` over `U` all of whose germs at points of `U` outside `Z` vanish.

```lean
public noncomputable def supportedSectionsSubmodule (Z : Set X)
    (F : _root_.SheafOfModules.{u} R) : F.Submodule
```

## Tag 07ZQ, a lemma

[Tag 07ZQ](https://stacks.math.columbia.edu/tag/07ZQ) in the Stacks Project.

**`AlgebraicGeometry.Scheme.Modules.range_pushforward_supportedSectionsSubmodule_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Modules/SupportedSectionsPushforward.lean, line 154](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Modules/SupportedSectionsPushforward.lean#L154).

> The pushforward of the subsheaf supported over `Z` is the subsheaf of
> the pushforward supported on `Z`, as subobjects of the pushforward sheaf.

```lean
theorem range_pushforward_supportedSectionsSubmodule_eq
    {X Y : Scheme.{u}} (f : X ⟶ Y)
    (Z : Set Y) (hZ : IsClosed Z) (F : X.Modules) (U : Y.Opens) :
    Set.range (((Scheme.Modules.pushforward f).map
      (supportedSectionsSubmodule (f.base ⁻¹' Z) F).ι).app U) =
      Set.range (((supportedSectionsSubmodule Z
      ((Scheme.Modules.pushforward f).obj F)).ι).val.app (op U))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 28.25, Tag 07ZM](https://stacks.math.columbia.edu/tag/07ZM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
