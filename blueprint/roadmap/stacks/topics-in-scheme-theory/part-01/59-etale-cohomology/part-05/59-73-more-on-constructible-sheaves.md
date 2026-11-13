---
declaration: section
origin: cited
lean: AlgebraicGeometry.isConstructibleAbelianSheaf_abelianShriekConstant, AlgebraicGeometry.abelianShriekZModIsConstructible, AlgebraicGeometry.isConstructible_sheafifiedYoneda_and_abelianShriekConstant_and_moduleShriek_of_qcqs, AlgebraicGeometry.isConstructibleModuleSheaf_moduleShriek, AlgebraicGeometry.isConstructibleSetSheaf_sheafifiedYoneda_of_qcqs, AlgebraicGeometry.isConstructibleModuleSheaf_moduleShriekConstant, AlgebraicGeometry.exists_isFilteredColimit_isConstructibleAbelianSheaf_of_qcqs, AlgebraicGeometry.exists_isFilteredColimit_isConstructibleSetSheaf_of_qcqs
statement: formalized
proof: formalized
---

# 59.73 More on constructible sheaves

Section 59.73 of the Stacks Project, [Tag 095M](https://stacks.math.columbia.edu/tag/095M). 14 tags here are carried by 59 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03S8, a lemma

[Tag 03S8](https://stacks.math.columbia.edu/tag/03S8) in the Stacks Project.

**`AlgebraicGeometry.isConstructibleAbelianSheaf_abelianShriekConstant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/AbelianShriekConstructible.lean, line 412](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/AbelianShriekConstructible.lean#L412). The attribute's comment: “part (2), abelian sheaves: an extension by zero of the constant sheaf at a finite abelian group at a quasi-compact quasi-separated etale object is a constructible abelian sheaf”.

> **Stacks 03S8, part (2).** For an étale morphism `j : U ⟶ X` of quasi-compact and
> quasi-separated schemes, presented as an object `U` of the small étale site of `X`, and `M` a
> finite abelian group, the extension by zero `j_!\underline{M}` is a constructible abelian sheaf
> on `X_étale`.
>
> By `AlgebraicGeometry.abelianShriekConstantIsoCopower` this sheaf is the copower sheaf by `M` on
> the sheaf `h_U^#` of sets, which is constructible by part (1) of the same tag; and the copower
> sheaf by a finite abelian group carries a constructible sheaf of sets to a constructible abelian
> sheaf. No input beyond part (1) of the tag is used.

```lean
public theorem isConstructibleAbelianSheaf_abelianShriekConstant [Finite M]
    [CompactSpace X.obj] [QuasiSeparatedSpace X.obj] (U : SmallEtale B X.obj X.property)
    [CompactSpace U.obj.left.obj] [QuasiSeparatedSpace U.obj.left.obj] :
    IsConstructibleAbelianSheaf B X
      ((abelianExtensionByZero B X.obj X.property U).obj
        ((constantSheaf (SmallEtale.topology B U.obj.left.obj U.obj.left.property)
          AddCommGrpCat.{u + 1}).obj M))
```

**`AlgebraicGeometry.abelianShriekZModIsConstructible`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/AbelianShriekConstructible.lean, line 437](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/AbelianShriekConstructible.lean#L437). The attribute's comment: “part (2) at the finite groups Z/nZ, the form AbelianShriekZModIsConstructible”.

> **Stacks 03S8, part (2), at the finite abelian groups `Z/nZ`.** The predicate
> `AlgebraicGeometry.AbelianShriekZModIsConstructible` holds: for every scheme `Y` of `B` that is
> quasi-compact and quasi-separated, every quasi-compact quasi-separated étale object `U` of
> `Y_étale` and every positive integer `n`, the abelian sheaf `j_{U!}(Z/nZ)` is constructible.
>
> `ZMod n` is finite exactly because `n` is positive, so this is
> `AlgebraicGeometry.isConstructibleAbelianSheaf_abelianShriekConstant` at
> `M = ULift (ZMod n)`.

```lean
public theorem abelianShriekZModIsConstructible : AbelianShriekZModIsConstructible B
```

**`AlgebraicGeometry.isConstructible_sheafifiedYoneda_and_abelianShriekConstant_and_moduleShriek_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ShriekAndRepresentableConstructible.lean, line 90](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ShriekAndRepresentableConstructible.lean#L90). The attribute's comment: “the whole tag: part (1) the sheaf of sets represented by a quasi-compact quasi-separated etale object is constructible, part (2) an extension by zero of the constant sheaf at a finite abelian group is a constructible abelian sheaf, part (3) an extension by zero of the constant sheaf at a finite module over a Noetherian commutative ring is a constructible sheaf of modules. Assumed, as in the source: quasi-compactness and quasi-separatedness of X and of U, and for part (3) a Noetherian commutative ring. No IsRightAdjoint or HasWeakSheafify assumption is carried, those instances being inferred here. The single-part registrations of the tag are kept beside it.”.

> **Stacks 03S8.** Let `X` be a quasi-compact and quasi-separated scheme of a big étale site,
> `R` a Noetherian commutative ring and `U` a quasi-compact quasi-separated object of the small
> étale site of `X`, so that `j : U ⟶ X` is an étale morphism of quasi-compact quasi-separated
> schemes. Then
>
> 1. the sheaf `h_U^#` of sets represented by `U` is a constructible sheaf of sets on `X_étale`;
> 2. for every finite abelian group `M` the extension by zero `j_!\underline{M}` is a constructible
>    abelian sheaf on `X_étale`; and
> 3. for every finite `R`-module `M` the extension by zero `j_{U!}\underline{M}` is a constructible
>    sheaf of `R`-modules on `X_étale`.
>
> This is the whole tag in one statement, under the source's quasi-compactness and
> quasi-separatedness of `X` and of `U` and no other hypothesis. Each part is proved by the theorem
> that states it alone: `AlgebraicGeometry.isConstructibleSetSheaf_sheafifiedYoneda_of_qcqs` for
> part (1), `AlgebraicGeometry.isConstructibleAbelianSheaf_abelianShriekConstant` for part (2), and
> `AlgebraicGeometry.isConstructibleModuleSheaf_moduleShriek` for part (3). The other registrations
> of the tag each state one part, or a case of one, without further hypotheses.
>
> The ring `R`, its commutativity and its Noetherianness are hypotheses of part (3) alone: parts
> (1) and (2) do not mention `R` and are proved without it. Part (1) is used in proving parts (2)
> and (3), so the conjunction asserts no more than parts (2) and (3) together do; it is the
> statement of the tag rather than a new fact.
>
> No instance beyond the source's hypotheses is assumed, although the components appear to assume
> four families of them; see the implementation notes above.

```lean
public theorem isConstructible_sheafifiedYoneda_and_abelianShriekConstant_and_moduleShriek_of_qcqs
    (B : BigEtaleSite.{u}) (X : B.Scheme) (R : Type (u + 1)) [CommRing R] [IsNoetherianRing R]
    [CompactSpace X.obj] [QuasiSeparatedSpace X.obj] (U : SmallEtale B X.obj X.property)
    [CompactSpace U.obj.left.obj] [QuasiSeparatedSpace U.obj.left.obj] :
    IsConstructibleSetSheaf B X
        ((Sheaf.sheafifiedYoneda (SmallEtale.topology B X.obj X.property)).obj U) ∧
      (∀ (M : AddCommGrpCat.{u + 1}) [Finite M],
        IsConstructibleAbelianSheaf B X
          ((abelianExtensionByZero B X.obj X.property U).obj
            ((constantSheaf (SmallEtale.topology B U.obj.left.obj U.obj.left.property)
              AddCommGrpCat.{u + 1}).obj M))) ∧
      (∀ (M : ModuleCat.{u + 1} R) [Module.Finite R M],
        IsConstructibleModuleSheaf B X R (moduleShriek.{u, u + 1, u + 1} B X R U M))
```

**`AlgebraicGeometry.isConstructibleModuleSheaf_moduleShriek`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ShriekFiniteModuleConstructible.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ShriekFiniteModuleConstructible.lean#L234). The attribute's comment: “part (3)”.

> **Stacks 03S8, part (3).** Let `X` be a quasi-compact and quasi-separated scheme, `Λ` a
> Noetherian ring and `M` a finite `Λ`-module. For `U` a quasi-compact and quasi-separated object of
> the small étale site of `X`, the extension by zero `j_{U!}\underline{M}` is a constructible sheaf
> of `Λ`-modules on `X_étale`.
>
> By `ModuleCat.exists_cokernel_finFreeSigma_of_finite` the module `M` is the cokernel of a map
> between finite direct sums of copies of `Λ`. Extension by zero of the constant sheaf is a left
> adjoint, so it carries that presentation to one of `j_{U!}\underline{M}` as the cokernel of a map
> between finite direct sums of copies of `j_{U!}\underline{Λ}`, which are constructible.

```lean
public theorem isConstructibleModuleSheaf_moduleShriek
    [CompactSpace X.obj] [QuasiSeparatedSpace X.obj] (U : SmallEtale B X.obj X.property)
    [CompactSpace U.obj.left.obj] [QuasiSeparatedSpace U.obj.left.obj]
    (M : ModuleCat.{u + 1} R) [Module.Finite R M] :
    IsConstructibleModuleSheaf B X R (moduleShriek.{u, u + 1, u + 1} B X R U M)
```

**`AlgebraicGeometry.isConstructibleSetSheaf_sheafifiedYoneda_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ShriekGeneratorConstructible.lean, line 137](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ShriekGeneratorConstructible.lean#L137). The attribute's comment: “part (1), sheaves of sets”.

> **Stacks 03S8, part (1).** For an étale morphism `j : U ⟶ X` of quasi-compact and
> quasi-separated schemes, presented as an object `U` of the small étale site of `X`, the sheaf
> `h_U` represented by `U` is a constructible sheaf of sets on `X_étale`.
>
> This is `AlgebraicGeometry.isConstructibleSetSheaf_sheafifiedYoneda` with its hypothesis, the
> conclusion of Stacks 03S0, discharged by `AlgebraicGeometry.hasFiniteEtaleStratification`.

```lean
public theorem isConstructibleSetSheaf_sheafifiedYoneda_of_qcqs
    [CompactSpace X.obj] [QuasiSeparatedSpace X.obj] (U : SmallEtale B X.obj X.property)
    [CompactSpace U.obj.left.obj] [QuasiSeparatedSpace U.obj.left.obj] :
    IsConstructibleSetSheaf B X
      ((Sheaf.sheafifiedYoneda (SmallEtale.topology B X.obj X.property)).obj U)
```

**`AlgebraicGeometry.isConstructibleModuleSheaf_moduleShriekConstant`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ShriekGeneratorConstructible.lean, line 201](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ShriekGeneratorConstructible.lean#L201). The attribute's comment: “sheaves of modules over a Noetherian commutative ring in an arbitrary universe: an extension by zero of a constant free rank-one module sheaf at a quasi-compact quasi-separated etale object is constructible”.

> **Stacks 03S8 for sheaves of modules.** For `U` a quasi-compact quasi-separated object of the
> small étale site of a quasi-compact quasi-separated scheme `X` and `Λ` a Noetherian commutative
> ring in an arbitrary universe `r`, the extension by zero `j_{U!}\underline{\Lambda}_U` of the
> constant free rank-one module sheaf is a constructible sheaf of `Λ`-modules in
> `ModuleCat.{max (u + 1) r} Λ`.
>
> By `AlgebraicGeometry.moduleShriekConstantIsoCopower` this sheaf is the copower module sheaf by
> the free rank-one module on the sheaf `h_U^#` of sets, which is constructible as a sheaf of sets
> in the module universe by
> `AlgebraicGeometry.isConstructibleFiniteSheaf_sheafifiedUliftYoneda_of_qcqs`, part (1) of the same
> tag. The copower stands in for `ModuleCat.free Λ`, whose source `Type r ⥤ ModuleCat.{r} Λ` would
> force the ring into the module universe.

```lean
public theorem isConstructibleModuleSheaf_moduleShriekConstant
    [CompactSpace X.obj] [QuasiSeparatedSpace X.obj] (U : SmallEtale B X.obj X.property)
    [CompactSpace U.obj.left.obj] [QuasiSeparatedSpace U.obj.left.obj] :
    IsConstructibleModuleSheaf B X Λ (moduleShriekConstant.{u, r, r} B X Λ U)
```

## Tag 03SA, a lemma

[Tag 03SA](https://stacks.math.columbia.edu/tag/03SA) in the Stacks Project.

**`AlgebraicGeometry.exists_isFilteredColimit_isConstructibleAbelianSheaf_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/LocalTorsionColimitOfConstructibles.lean, line 452](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/LocalTorsionColimitOfConstructibles.lean#L452). The attribute's comment: “part (2), torsion abelian sheaves, torsion in the local sense of Stacks 0DD7”. References: SGA 4½ Arcata (4.3.3), “more general”.

> **Stacks 03SA (2).** Let `X` be a quasi-compact and quasi-separated scheme and let `F` be a
> torsion abelian sheaf on `X_étale`. Then `F` is a filtered colimit of constructible abelian
> sheaves.
>
> The torsion condition is the local one of Stacks 0DD7, `Stacks.Torsion.torsionSheafProperty`:
> every section is annihilated by a positive integer after restriction along the arrows of a
> covering sieve. The colimit is taken in the category of abelian sheaves on `X_étale`, over a small
> filtered index category, and the terms are constructible in the sense of Stacks 03RW (2). This is
> `AlgebraicGeometry.ind_isConstructibleAbelianSheaf_of_torsionSheafProperty` in the
> diagram-and-cocone spelling of parts (1) and (3).

```lean
public theorem exists_isFilteredColimit_isConstructibleAbelianSheaf_of_qcqs
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1})
    (hF : Stacks.Torsion.torsionSheafProperty (SmallEtale.topology B X.obj X.property) F) :
    ∃ (I : Type (u + 1)) (_ : SmallCategory I) (_ : IsFiltered I)
      (D : I ⥤ Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1})
      (ι : D ⟶ (Functor.const I).obj F), Nonempty (IsColimit (Cocone.mk F ι)) ∧
        ∀ i, IsConstructibleAbelianSheaf B X (D.obj i)
```

**`AlgebraicGeometry.exists_isFilteredColimit_isConstructibleSetSheaf_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ModuleColimitOfConstructibles.lean, line 100](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ModuleColimitOfConstructibles.lean#L100). The attribute's comment: “part (1), sheaves of sets, with 093C (1) and 03S0 discharged”.

> **Stacks 03SA, part (1).** Let `X` be a quasi-compact and quasi-separated scheme and `F` a
> sheaf of sets on `X_étale`. Then `F` is a filtered colimit of constructible sheaves of sets.
>
> This is `AlgebraicGeometry.exists_isFilteredColimit_isConstructibleSetSheaf` with both of its
> hypotheses discharged: Stacks 093C (1) by
> `AlgebraicGeometry.setSheavesAreFilteredColimitsOfPresentations` and Stacks 03S0 by
> `AlgebraicGeometry.etaleFiniteStratificationExists`.

```lean
public theorem exists_isFilteredColimit_isConstructibleSetSheaf_of_qcqs
    (F : Sheaf (SmallEtale.topology B X.obj X.property) (Type (u + 1))) :
    ∃ (I : Type (u + 1)) (_ : SmallCategory I) (_ : IsFiltered I)
      (D : I ⥤ Sheaf (SmallEtale.topology B X.obj X.property) (Type (u + 1)))
      (ι : D ⟶ (Functor.const I).obj F), Nonempty (IsColimit (Cocone.mk F ι)) ∧
        ∀ i, IsConstructibleSetSheaf B X (D.obj i)
```

**`AlgebraicGeometry.exists_isFilteredColimit_isConstructibleModuleSheaf_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ModuleColimitOfConstructibles.lean, line 120](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ModuleColimitOfConstructibles.lean#L120). The attribute's comment: “part (3), sheaves of modules, with 093C (2) and 03S8 discharged”. References: SGA 4 XVII (5.5.25.4), “more general”.

> **Stacks 03SA, part (3).** Let `X` be a quasi-compact and quasi-separated scheme, `Λ` a
> Noetherian ring and `F` a sheaf of `Λ`-modules on `X_étale`. Then `F` is a filtered colimit of
> constructible sheaves of `Λ`-modules.
>
> This is `AlgebraicGeometry.exists_isFilteredColimit_isConstructibleModuleSheaf` with both of its
> hypotheses discharged: Stacks 093C (2) by
> `AlgebraicGeometry.moduleSheavesAreFilteredColimitsOfPresentations` and Stacks 03S8 for sheaves of
> modules by `AlgebraicGeometry.isConstructibleModuleSheaf_moduleShriekConstant`.

```lean
public theorem exists_isFilteredColimit_isConstructibleModuleSheaf_of_qcqs
    (F : Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{u + 1} Λ)) :
    ∃ (I : Type (u + 1)) (_ : SmallCategory I) (_ : IsFiltered I)
      (D : I ⥤ Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{u + 1} Λ))
      (ι : D ⟶ (Functor.const I).obj F), Nonempty (IsColimit (Cocone.mk F ι)) ∧
        ∀ i, IsConstructibleModuleSheaf B X Λ (D.obj i)
```

**`AlgebraicGeometry.exists_isFilteredColimit_isConstructibleModuleSheaf_of_small`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ModuleColimitOfConstructibles.lean, line 214](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ModuleColimitOfConstructibles.lean#L214). The attribute's comment: “part (3), sheaves of modules over a Noetherian ring in any universe”.

> **Stacks 03SA, part (3), for a coefficient ring in any universe.** Let `X` be a quasi-compact
> and quasi-separated scheme, `R` a Noetherian ring and `F` a sheaf of `R`-modules on `X_étale`.
> Then `F` is a filtered colimit of constructible sheaves of `R`-modules.
>
> `AlgebraicGeometry.exists_isFilteredColimit_isConstructibleModuleSheaf_of_qcqs` is the same
> statement for a ring in `Type (u + 1)`. Here `R` need only be small in that universe: `F` is
> carried to a sheaf of `Shrink.{u + 1} R`-modules by
> `AlgebraicGeometry.SmallEtale.sheafShrinkEquivalence`, presented there, and the presentation is
> carried back by the inverse equivalence, which preserves colimits; constructibility of the terms
> comes back by `AlgebraicGeometry.isConstructibleModuleSheaf_of_shrink`. The two sheafification
> side conditions at `R` are theorems of the library,
> `AlgebraicGeometry.SmallEtale.isRightAdjointPushforward_moduleCatSucc` and
> `AlgebraicGeometry.SmallEtale.hasWeakSheafifyOver_moduleCatSucc`, so the only hypotheses are
> those of the tag and the smallness of `R`.

```lean
public theorem exists_isFilteredColimit_isConstructibleModuleSheaf_of_small
    (F : Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{u + 1} R)) :
    ∃ (I : Type (u + 1)) (_ : SmallCategory I) (_ : IsFiltered I)
      (D : I ⥤ Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{u + 1} R))
      (ι : D ⟶ (Functor.const I).obj F), Nonempty (IsColimit (Cocone.mk F ι)) ∧
        ∀ i, IsConstructibleModuleSheaf B X R (D.obj i)
```

## Tag 095Q, a lemma

[Tag 095Q](https://stacks.math.columbia.edu/tag/095Q) in the Stacks Project.

**`AlgebraicGeometry.isConstructibleAbelianSheaf_pullback_iff_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/AbelianSurjectiveDescent.lean, line 616](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/AbelianSurjectiveDescent.lean#L616). The attribute's comment: “part (2), abelian sheaves”.

> **Stacks 095Q, part (2).** Let `f : X ⟶ Y` be a surjective morphism of quasi-compact and
> quasi-separated schemes and let `ℱ` be an abelian sheaf on `Y_étale` — arbitrary, with no torsion
> assumption. Then `ℱ` is constructible if and only if `f⁻¹ℱ` is constructible.
>
> The forward implication is Stacks 095G, `AlgebraicGeometry.isConstructibleFiniteSheaf_pullback`,
> and needs neither surjectivity of `f` nor quasi-compactness. The converse is carried out in the
> category of sheaves of `ℤ`-modules, where Stacks 095Q is already unconditional:
> `AlgebraicGeometry.isConstructibleModuleSheaf_pullback_iff_of_surjective`. Only the
> quasi-compactness and quasi-separatedness of `X` and `Y`, which the source's statement assumes,
> are hypotheses.
>
> The passage between the two categories is the one place with content. Going out is immediate,
> `AlgebraicGeometry.isConstructibleModuleSheaf_moduleCatIntEquivalence`, a finite abelian group
> being a finitely generated `ℤ`-module; the module development is pinned to a Noetherian ring in
> `Type (u + 1)`, so the descent happens at `ULift ℤ` and is transported back by
> `AlgebraicGeometry.isConstructibleModuleSheaf_int_of_uliftIntRestrictScalars`. Coming back is
> `AlgebraicGeometry.isConstructibleAbelianSheaf_of_isConstructibleModuleSheaf_int`, which needs
> `ℱ` to be torsion — and that is exactly what the constructibility of `f⁻¹ℱ` supplies, through the
> stalk criterion `AlgebraicGeometry.torsionSheafProperty_of_isConstructibleAbelianSheaf_pullback`.
> Stacks 093C for torsion abelian sheaves is not used: the module form of Stacks 093C, which the
> library proves, is what the descent above consumes.

```lean
public theorem isConstructibleAbelianSheaf_pullback_iff_of_surjective
    (hf : Function.Surjective (B.inclusion.map f).base)
    (F : Sheaf (SmallEtale.topology B Y.obj Y.property) AddCommGrpCat.{u + 1}) :
    IsConstructibleAbelianSheaf B Y F ↔
      IsConstructibleAbelianSheaf B X ((smallEtaleAbelianPullbackFunctor B f).obj F)
```

**`AlgebraicGeometry.isConstructibleAbelianSheaf_pullback_iff_of_surjective_general`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/AbelianSurjectiveDescentUnconditional.lean, line 178](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/AbelianSurjectiveDescentUnconditional.lean#L178). The attribute's comment: “part (2), abelian sheaves”.

> Let `f : X ⟶ Y` be a surjective morphism of quasi-compact and quasi-separated schemes and let
> `ℱ` be an abelian sheaf on `Y_étale`, with no torsion assumption. Then `ℱ` is constructible if and
> only if `f⁻¹ℱ` is constructible.

```lean
public theorem isConstructibleAbelianSheaf_pullback_iff_of_surjective_general
    (hf : Function.Surjective (B.inclusion.map f).base)
    (𝓕 : Sheaf (SmallEtale.topology B Y.obj Y.property) AddCommGrpCat.{u + 1}) :
    IsConstructibleAbelianSheaf B Y 𝓕 ↔
      IsConstructibleAbelianSheaf B X ((smallEtaleAbelianPullbackFunctor B f).obj 𝓕)
```

**`AlgebraicGeometry.isConstructibleModuleSheaf_pullback_iff_of_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ModuleSurjectiveDescent.lean, line 269](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ModuleSurjectiveDescent.lean#L269). The attribute's comment: “sheaves of modules”.

> **Stacks 095Q for sheaves of modules.** Let `f : X ⟶ Y` be a surjective morphism of
> quasi-compact and quasi-separated schemes, `Λ` a Noetherian ring and `ℱ` a sheaf of `Λ`-modules on
> `Y_étale`. Then `ℱ` is constructible if and only if `f⁻¹ℱ` is constructible.
>
> The forward implication is Stacks 095G, `AlgebraicGeometry.isConstructibleModuleSheaf_pullback`,
> and needs neither surjectivity of `f` nor quasi-compactness. The converse is
> `AlgebraicGeometry.isConstructibleModuleSheaf_of_isConstructibleModuleSheaf_pullback`.
>
> Nothing is granted. The two statements of the source that were once hypotheses here are both
> proved in the library, and both are supplied from `hXc`, `hXq`, `hYc` and `hYq`, the
> quasi-compactness and quasi-separatedness of `X` and `Y` that the source's statement assumes:
> Stacks 095N on the quasi-compact quasi-separated schemes of `B`, from the unconditional
> `AlgebraicGeometry.isConstructibleModuleSheaf_iff_qcqsShriekPresentation`, and Stacks 093C (2) on
> `Y`, from `AlgebraicGeometry.moduleSheavesAreFilteredColimitsOfPresentations`.

```lean
public theorem isConstructibleModuleSheaf_pullback_iff_of_surjective
    (hf : Function.Surjective (B.inclusion.map f).base)
    (F : Sheaf (SmallEtale.topology B Y.1 Y.property) (ModuleCat.{u + 1} Λ)) :
    IsConstructibleModuleSheaf B Y Λ F ↔
      IsConstructibleModuleSheaf B X Λ ((smallEtaleModulePullbackFunctor B Λ f).obj F)
```

**`AlgebraicGeometry.isConstructibleSetSheaf_pullback_iff_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/SurjectiveDescent.lean, line 352](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/SurjectiveDescent.lean#L352). The attribute's comment: “part (1), sheaves of sets”.

> **Stacks 095Q, part (1).** Let `f : X ⟶ Y` be a surjective morphism of quasi-compact and
> quasi-separated schemes and let `ℱ` be a sheaf of sets on `Y_étale`. Then `ℱ` is constructible
> if and only if `f⁻¹ℱ` is constructible.
>
> Nothing is assumed. The forward implication is Stacks 095G,
> `AlgebraicGeometry.isConstructibleFiniteSheaf_pullback`, and needs neither surjectivity of `f`
> nor quasi-compactness. The converse is
> `AlgebraicGeometry.isConstructibleSetSheaf_of_isConstructibleSetSheaf_pullback`, whose Stacks 09Y9
> is supplied from
> `isConstructibleSetSheaf_iff_hasFiniteQCSRepresentableCoequalizerPresentation_unconditional`,
> which assumes nothing beyond quasi-compactness and quasi-separatedness of `X` and does not use
> Stacks 0245. Both hypotheses of the library's Stacks 03SA (1) are discharged as described above.
>
> Parts (2) and (3) of the tag are not proved here.

```lean
public theorem isConstructibleSetSheaf_pullback_iff_unconditional
    (hf : Function.Surjective (B.inclusion.map f).base)
    (hXc : CompactSpace X.obj) (hXq : QuasiSeparatedSpace X.obj)
    (hYc : CompactSpace Y.obj) (hYq : QuasiSeparatedSpace Y.obj)
    (F : Sheaf (SmallEtale.topology B Y.obj Y.property) (Type (u + 1))) :
    IsConstructibleSetSheaf B Y F ↔
      IsConstructibleSetSheaf B X ((smallEtaleSetPullback B f).obj F)
```

## Tag 095H, a lemma

[Tag 095H](https://stacks.math.columbia.edu/tag/095H) in the Stacks Project.

**`AlgebraicGeometry.isConstructibleModuleSheaf_pushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FiniteEtalePushforwardConstructible.lean, line 476](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FiniteEtalePushforwardConstructible.lean#L476). The attribute's comment: “sheaves of modules over a Noetherian ring; no hypothesis on S or T”. References: SGA 4 IX (2.14), “(i), special case”; SGA 5 I (1.14), “b)”.

> **Stacks 095H for sheaves of modules over a Noetherian ring.** Let `p : T ⟶ S` be a finite
> étale morphism of a big étale site, let `Λ` be a Noetherian ring and let `ℱ` be a constructible
> sheaf of `Λ`-modules on `T_étale`. Then `p_*ℱ` is a constructible sheaf of `Λ`-modules on
> `S_étale`. No hypothesis is imposed on `S` or `T`.
>
> By Stacks 095F constructibility may be checked on an open covering of `S`, and the affine opens
> of `S` are such a covering; the restriction of `p_*ℱ` to an affine open `U` is the direct image,
> along the base change of `p` to `U`, of the restriction of `ℱ`
> (`AlgebraicGeometry.smallEtaleRestrictionPushforwardBaseChangeIso`), that base change is again
> finite étale, the restriction of `ℱ` is constructible by Stacks 095G, and `U` is quasi-compact
> and quasi-separated, so
> `AlgebraicGeometry.isConstructibleModuleSheaf_pushforward_of_compactSpace` applies.

```lean
public theorem isConstructibleModuleSheaf_pushforward
    [IsFinite (B.inclusion.map p)] [Etale (B.inclusion.map p)]
    (F : Sheaf (SmallEtale.topology B T.1 T.property) (ModuleCat.{u + 1} Λ))
    (hF : IsConstructibleModuleSheaf B T Λ F) :
    IsConstructibleModuleSheaf B S Λ
      ((B.smallPushforward p (ModuleCat.{u + 1} Λ)).obj F)
```

**`AlgebraicGeometry.isConstructibleSetSheaf_pushforward_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FiniteEtalePushforwardConstructibleUnconditional.lean, line 149](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FiniteEtalePushforwardConstructibleUnconditional.lean#L149). The attribute's comment: “sheaves of sets; no hypothesis on S or T”. References: SGA 4 IX (2.14), “(i), special case”; SGA 4 XIV (1.1), “special case”; SGA 4 XIV (1.11), “partial”; SGA 4 XIV (1.5), “special case”.

> Let `p : T ⟶ S` be a finite étale morphism of a big étale site and let `ℱ` be a
> constructible sheaf of sets on `T_étale`. Then `p_*ℱ` is a constructible sheaf of sets on
> `S_étale`.

```lean
public theorem isConstructibleSetSheaf_pushforward_unconditional
    [IsFinite (B.inclusion.map p)] [Etale (B.inclusion.map p)]
    (F : Sheaf (SmallEtale.topology B T.1 T.property) (Type (u + 1)))
    (hF : IsConstructibleSetSheaf B T F) :
    IsConstructibleSetSheaf B S ((B.smallPushforward p (Type (u + 1))).obj F)
```

**`AlgebraicGeometry.isConstructibleAbelianSheaf_pushforward_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FiniteEtalePushforwardConstructibleUnconditional.lean, line 226](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FiniteEtalePushforwardConstructibleUnconditional.lean#L226). The attribute's comment: “sheaves of abelian groups; no hypothesis on S or T, no torsion hypothesis”.

> Let `p : T ⟶ S` be a finite étale morphism of a big étale site and let `ℱ` be a
> constructible abelian sheaf on `T_étale`. Then `p_*ℱ` is a constructible abelian sheaf on
> `S_étale`.

```lean
public theorem isConstructibleAbelianSheaf_pushforward_unconditional
    [IsFinite (B.inclusion.map p)] [Etale (B.inclusion.map p)]
    (F : Sheaf (SmallEtale.topology B T.1 T.property) AddCommGrpCat.{u + 1})
    (hF : IsConstructibleAbelianSheaf B T F) :
    IsConstructibleAbelianSheaf B S
      ((B.smallPushforward p AddCommGrpCat.{u + 1}).obj F)
```

## Tag 09Y9, a lemma

[Tag 09Y9](https://stacks.math.columbia.edu/tag/09Y9) in the Stacks Project.

**`AlgebraicGeometry.isConstructibleSetSheaf_of_hasFiniteQCSRepresentableCoequalizerPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/CoequalizerPresentationConstructible.lean, line 88](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/CoequalizerPresentationConstructible.lean#L88). The attribute's comment: “the implication from a finite coequalizer presentation by representables of quasi-compact quasi-separated etale objects to constructibility, for sheaves of sets; the reverse implication, from constructibility to the existence of such a presentation, is not part of this statement”. References: SGA 4 IX (2.7), “Sheaves of sets”; SGA 4 IX (2.7.1), “Sufficiency”.

> **Stacks 09Y9, the implication from a presentation to constructibility.** Let `X` be a
> quasi-compact and quasi-separated scheme of a big étale site and let `F` be a sheaf of sets on
> `X_étale` which is a coequalizer of two maps between finite coproducts of sheaves represented by
> quasi-compact and quasi-separated objects of `X_étale`. Then `F` is a constructible sheaf of
> sets.

```lean
public theorem isConstructibleSetSheaf_of_hasFiniteQCSRepresentableCoequalizerPresentation
    (B : BigEtaleSite.{u}) (X : B.Scheme) [CompactSpace X.obj] [QuasiSeparatedSpace X.obj]
    {F : Sheaf (SmallEtale.topology B X.obj X.property) (Type (u + 1))}
    (hF : HasFiniteQCSRepresentableCoequalizerPresentation B X F) :
    IsConstructibleSetSheaf B X F
```

**`AlgebraicGeometry.exists_finite_representable_epi_of_isConstructibleSetSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ConstructibleQuasiCompact.lean, line 328](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ConstructibleQuasiCompact.lean#L328). The attribute's comment: “the surjection half: a constructible sheaf of sets on a quasi-compact quasi-separated scheme is the target of an epimorphism from a finite coproduct of sheaves represented by quasi-compact quasi-separated objects”.

> **Stacks 09Y9, the surjection half.** A constructible sheaf of sets on the small étale site
> of a quasi-compact and quasi-separated scheme receives an epimorphism from a finite coproduct of
> sheaves represented by quasi-compact and quasi-separated objects of the site.
>
> This is `AlgebraicGeometry.isQuasiCompact_of_isConstructibleSetSheaf_unconditional` followed by
> the presentation of a quasi-compact sheaf by finitely many affine representables; both the
> conservativity of geometric points and the finite affine covering it uses are theorems of the
> library, so nothing is assumed.

```lean
public theorem exists_finite_representable_epi_of_isConstructibleSetSheaf
    (B : BigEtaleSite.{u}) (X : B.Scheme) [CompactSpace X.obj] [QuasiSeparatedSpace X.obj]
    (F : Sheaf (SmallEtale.topology B X.obj X.property) (Type (u + 1)))
    (hF : IsConstructibleSetSheaf B X F) :
    ∃ (n : ℕ) (U : Fin n → SmallEtale B X.obj X.property),
      (∀ i, CompactSpace ((SmallEtale.toScheme B X.obj X.property).obj (U i)) ∧
        QuasiSeparatedSpace ((SmallEtale.toScheme B X.obj X.property).obj (U i))) ∧
      ∃ p : (∐ fun i ↦ (Sheaf.sheafifiedYoneda
        (SmallEtale.topology B X.obj X.property)).obj (U i)) ⟶ F, Epi p
```

**`AlgebraicGeometry.isConstructibleSetSheaf_iff_hasFiniteQCSRepresentableCoequalizerPresentation_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ConstructibleQuasiCompact.lean, line 353](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ConstructibleQuasiCompact.lean#L353). The attribute's comment: “both directions”. References: SGA 4 IX (2.7); SGA 4 IX (2.7.1), “Sufficiency”.

> **Stacks Project, Tag 09Y9.** On a quasi-compact and quasi-separated scheme the
> constructible sheaves of sets on the small étale site are exactly the sheaves admitting a
> coequalizer presentation by finite coproducts of sheaves represented by quasi-compact and
> quasi-separated étale objects.
>
> Nothing beyond quasi-compactness and quasi-separatedness of `X` is assumed. Stacks 03S0 is
> `AlgebraicGeometry.etaleFiniteStratificationExists` and the conservativity of geometric points of
> Stacks 03PU is `AlgebraicGeometry.jointlyFaithful_smallEtaleSetPullback`, both theorems of the
> library. Stacks 0245 is not used at all: the quasi-compactness step is
> `AlgebraicGeometry.isQuasiCompact_of_isConstructibleSetSheaf_unconditional` above, which refines
> the covering produced by étale-local representability instead of descending along it.

```lean
public theorem
    isConstructibleSetSheaf_iff_hasFiniteQCSRepresentableCoequalizerPresentation_unconditional
    (B : BigEtaleSite.{u}) (X : B.Scheme) [CompactSpace X.obj] [QuasiSeparatedSpace X.obj]
    (F : Sheaf (SmallEtale.topology B X.obj X.property) (Type (u + 1))) :
    IsConstructibleSetSheaf B X F ↔
      HasFiniteQCSRepresentableCoequalizerPresentation B X F
```

## Tag 095N, a lemma

[Tag 095N](https://stacks.math.columbia.edu/tag/095N) in the Stacks Project.

**`AlgebraicGeometry.isConstructibleModuleSheaf_iff_qcqsShriekPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ModuleShriekFiniteGeneration.lean, line 674](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ModuleShriekFiniteGeneration.lean#L674). The attribute's comment: “quasi-compact quasi-separated presentation”. References: SGA 4 IX (2.7), “special case”; SGA 4 IX (2.9), “(ii)”.

> **Stacks 095N, the quasi-compact quasi-separated presentation.** Let `X` be a quasi-compact and
> quasi-separated scheme and `Λ` a Noetherian ring. A sheaf of `Λ`-modules on `X_étale` is
> constructible exactly when it is the cokernel of a map between finite direct sums of extensions by
> zero of constant free rank-one module sheaves at quasi-compact and quasi-separated objects of
> `X_étale`.
>
> Nothing is granted. The two inputs of
> `AlgebraicGeometry.isConstructibleModuleSheaf_iff_hasFiniteShriekPresentation` are discharged:
> constructibility of the generators is
> `AlgebraicGeometry.isConstructibleModuleSheaf_moduleShriekConstant` (Stacks 03S8 for modules) and
> the finite generation step of the proof is
> `AlgebraicGeometry.exists_finite_epi_sigma_moduleShriekConstant_of_isConstructibleModuleSheaf`.
> This theorem and the affine one below carry the registration of 095N; the assembly steps with
> those inputs as arguments carry none.

```lean
public theorem isConstructibleModuleSheaf_iff_qcqsShriekPresentation
    (F : Sheaf (SmallEtale.topology B X.1 X.property) (ModuleCat.{u + 1} Λ)) :
    IsConstructibleModuleSheaf B X Λ F ↔
      HasFiniteShriekPresentation.{u, u + 1, u + 1} B X Λ
        (fun W ↦ CompactSpace ((SmallEtale.toScheme B X.1 X.property).obj W) ∧
          QuasiSeparatedSpace ((SmallEtale.toScheme B X.1 X.property).obj W)) F
```

**`AlgebraicGeometry.isConstructibleModuleSheaf_iff_hasFiniteAffineShriekPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ModuleShriekFiniteGeneration.lean, line 693](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ModuleShriekFiniteGeneration.lean#L693). The attribute's comment: “affine presentation”. References: SGA 4 IX (2.7), “Module sheaves”; SGA 4 IX (2.9), “(ii)”.

> **Stacks 095N, the affine presentation.** Let `X` be a quasi-compact and quasi-separated
> scheme and `Λ` a Noetherian ring. A sheaf of `Λ`-modules on `X_étale` is constructible exactly
> when it is the cokernel of a map between finite direct sums of extensions by zero of constant free
> rank-one module sheaves at *affine* objects of `X_étale`.
>
> Nothing is granted: this is
> `AlgebraicGeometry.isConstructibleModuleSheaf_iff_affineShriekPresentation_of_gen` with its
> hypothesis discharged by the affine form of the finite generation step proved just above.

```lean
public theorem isConstructibleModuleSheaf_iff_hasFiniteAffineShriekPresentation
    (F : Sheaf (SmallEtale.topology B X.1 X.property) (ModuleCat.{u + 1} Λ)) :
    IsConstructibleModuleSheaf B X Λ F ↔
      HasFiniteShriekPresentation.{u, u + 1, u + 1} B X Λ
        (SmallEtale.IsAffine B X.1 X.property) F
```

## Tag 09YT, a lemma

[Tag 09YT](https://stacks.math.columbia.edu/tag/09YT) in the Stacks Project.

**`AlgebraicGeometry.isConstructibleAbelianSheaf_iff_hasFiniteZModShriekPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/AbelianShriekPresentation.lean, line 674](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/AbelianShriekPresentation.lean#L674). The attribute's comment: “a constructible abelian sheaf on a quasi-compact quasi-separated scheme is exactly a cokernel of a map between finite direct sums of the sheaves j\_\{U!}(Z/nZ) at quasi-compact quasi-separated etale objects and positive integers n”.

> **Stacks 09YT.** Let `X` be a quasi-compact and quasi-separated scheme. An abelian sheaf on the
> small étale site of `X` is constructible exactly when it is of the form
> `Coker(⨁_j j_{V_j!}(Z/m_jZ) → ⨁_i j_{U_i!}(Z/n_iZ))` with the `V_j` and `U_i` quasi-compact
> quasi-separated objects of `X_étale` and the `m_j`, `n_i` positive integers.
>
> Both inclusions are proved. A cokernel of that form is constructible because constructibility of
> abelian sheaves is a weak Serre condition, Stacks 03RZ (2), and the summands are constructible by
> Stacks 03S8 (2) at the finite groups `Z/nZ`, which is
> `AlgebraicGeometry.abelianShriekZModIsConstructible`. Conversely a constructible abelian sheaf is
> annihilated by a positive integer `N` and has a presentation by extensions by zero of the constant
> sheaf `ℤ` from Stacks 095N at `Λ = ℤ`; quotienting that presentation by `N` turns it into one of
> the displayed form.

```lean
public theorem isConstructibleAbelianSheaf_iff_hasFiniteZModShriekPresentation
    (hXc : CompactSpace X.obj) (hXq : QuasiSeparatedSpace X.obj)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1}) :
    IsConstructibleAbelianSheaf B X F ↔
      HasFiniteZModShriekPresentation B X (IsQCQSEtaleObject B X) F
```

**`AlgebraicGeometry.isConstructibleAbelianSheaf_iff_affineZModShriekPresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/AbelianShriekPresentation.lean, line 689](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/AbelianShriekPresentation.lean#L689). The attribute's comment: “the same characterization with the etale objects of the presentation affine, which is the tag's concluding sentence”.

> **Stacks 09YT, the affine form.** "In fact, we can even assume `U_i` and `V_j` affine": the
> étale objects of the presentation of a constructible abelian sheaf may be taken affine, and a
> presentation by affine objects still has a constructible cokernel.

```lean
public theorem isConstructibleAbelianSheaf_iff_affineZModShriekPresentation
    (hXc : CompactSpace X.obj) (hXq : QuasiSeparatedSpace X.obj)
    (F : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1}) :
    IsConstructibleAbelianSheaf B X F ↔
      HasFiniteZModShriekPresentation B X (SmallEtale.IsAffine B X.obj X.property) F
```

## Tag 09Z4, a lemma

[Tag 09Z4](https://stacks.math.columbia.edu/tag/09Z4) in the Stacks Project.

**`AlgebraicGeometry.IsConstructibleAbelianSheaf.isFinitelyPresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Restriction/CompactConstructibleAbelianViaShriekPresentation.lean, line 67](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Restriction/CompactConstructibleAbelianViaShriekPresentation.lean#L67). The attribute's comment: “sheaves of abelian groups”.

> **The sheaves-of-abelian-groups case of Stacks 09Z4.** Let `X` be a quasi-compact and
> quasi-separated scheme and let `F` be a constructible abelian sheaf on `X_étale`. Then morphisms
> out of `F` commute with filtered colimits of abelian sheaves:
> `Mor(F, colim G_i) = colim Mor(F, G_i)`.
>
> A constructible abelian sheaf is a constructible sheaf of `ℤ`-modules and `ℤ` is Noetherian, so
> this is the module case at `Λ = ℤ`. Stacks 095N at `ℤ`, the presentation of a constructible sheaf
> of `ℤ`-modules as the cokernel of a map between finite direct sums of extensions by zero of the
> constant sheaf `ℤ` at quasi-compact and quasi-separated étale objects, is supplied by
> `AlgebraicGeometry.hasFiniteShriekPresentation_of_isConstructibleModuleSheaf_int`.

```lean
public theorem IsConstructibleAbelianSheaf.isFinitelyPresentable
    (B : BigEtaleSite.{u}) (X : B.Scheme) [CompactSpace X.1] [QuasiSeparatedSpace X.1]
    (F : Sheaf (SmallEtale.topology B X.1 X.property) AddCommGrpCat.{u + 1})
    (hF : IsConstructibleAbelianSheaf B X F) :
    IsFinitelyPresentable.{u + 1} F
```

**`AlgebraicGeometry.IsConstructibleModuleSheaf.isFinitelyPresentable_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Restriction/CompactConstructibleModulesUnconditional.lean, line 78](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Restriction/CompactConstructibleModulesUnconditional.lean#L78). The attribute's comment: “sheaves of Λ-modules over an arbitrary Noetherian ring, with the inverse image along small étale base change and the sheafification on the slices proved rather than assumed”.

> **The sheaves-of-`Λ`-modules case of Stacks 09Z4, with nothing assumed.** Let `X` be a
> quasi-compact and quasi-separated scheme, let `Λ` be a Noetherian ring and let `F` be a
> constructible sheaf of `Λ`-modules on `X_étale`. Then morphisms out of `F` commute with filtered
> colimits of sheaves of `Λ`-modules: `Mor(F, colim G_i) = colim Mor(F, G_i)`.
>
> The inverse image along small étale base change and the sheafification of presheaves of
> `Λ`-modules on the slices of the small étale sites, through which constructibility of a sheaf of
> `Λ`-modules is stated, are found here by instance search rather than taken as arguments.

```lean
public theorem IsConstructibleModuleSheaf.isFinitelyPresentable_unconditional
    (B : BigEtaleSite.{u}) (X : B.Scheme) (R : Type (u + 1)) [CommRing R] [IsNoetherianRing R]
    [CompactSpace X.1] [QuasiSeparatedSpace X.1]
    (F : Sheaf (SmallEtale.topology B X.1 X.property) (ModuleCat.{u + 1} R))
    (hF : IsConstructibleModuleSheaf B X R F) :
    IsFinitelyPresentable.{u + 1} F
```

**`AlgebraicGeometry.IsConstructibleModuleSheaf.isFinitelyPresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Restriction/CompactConstructibleModulesViaShriekPresentation.lean, line 71](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Restriction/CompactConstructibleModulesViaShriekPresentation.lean#L71). The attribute's comment: “sheaves of Λ-modules”.

> **The sheaves-of-`Λ`-modules case of Stacks 09Z4.** Let `X` be a quasi-compact and
> quasi-separated scheme, let `Λ` be a Noetherian ring and let `F` be a constructible sheaf of
> `Λ`-modules on `X_étale`. Then morphisms out of `F` commute with filtered colimits of sheaves of
> `Λ`-modules: `Mor(F, colim G_i) = colim Mor(F, G_i)`.
>
> Stacks 095N, the presentation of a constructible sheaf of `Λ`-modules as the cokernel of a map
> between finite direct sums of extensions by zero of constant free rank-one module sheaves at
> quasi-compact and quasi-separated étale objects, is supplied by
> `AlgebraicGeometry.isConstructibleModuleSheaf_iff_qcqsShriekPresentation`.

```lean
public theorem IsConstructibleModuleSheaf.isFinitelyPresentable
    (B : BigEtaleSite.{u}) (X : B.Scheme) (R : Type (u + 1)) [CommRing R] [IsNoetherianRing R]
    [CompactSpace X.1] [QuasiSeparatedSpace X.1]
    [∀ (S T : B.Scheme) (f : T ⟶ S),
      ((smallEtaleBaseChange B f).sheafPushforwardContinuous (ModuleCat.{u + 1} R)
        (SmallEtale.topology B S.1 S.property)
        (SmallEtale.topology B T.1 T.property)).IsRightAdjoint]
    [∀ (T : B.Scheme) (V : SmallEtale B T.1 T.property),
      HasWeakSheafify ((SmallEtale.topology B T.1 T.property).over V) (ModuleCat.{u + 1} R)]
    (F : Sheaf (SmallEtale.topology B X.1 X.property) (ModuleCat.{u + 1} R))
    (hF : IsConstructibleModuleSheaf B X R F) :
    IsFinitelyPresentable.{u + 1} F
```

**`AlgebraicGeometry.IsConstructibleSetSheaf.isFinitelyPresentable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Restriction/CompactConstructibleSetsViaPresentation.lean, line 59](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Restriction/CompactConstructibleSetsViaPresentation.lean#L59). The attribute's comment: “sheaves of sets”.

> Let `X` be a quasi-compact and quasi-separated scheme and let `F` be a constructible sheaf of
> sets on `X_étale`. Then morphisms out of `F` commute with filtered colimits of sheaves of sets:
> `Mor(F, colim G_i) = colim Mor(F, G_i)`.

```lean
public theorem IsConstructibleSetSheaf.isFinitelyPresentable
    (B : BigEtaleSite.{u}) (X : B.Scheme) [CompactSpace X.1] [QuasiSeparatedSpace X.1]
    (F : Sheaf (SmallEtale.topology B X.1 X.property) (Type (u + 1)))
    (hF : IsConstructibleSetSheaf B X F) :
    IsFinitelyPresentable.{u + 1} F
```

## Tag 095R, a lemma

[Tag 095R](https://stacks.math.columbia.edu/tag/095R) in the Stacks Project.

**`AlgebraicGeometry.isConstructibleSetSheaf_pushforward_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FinitePresentationPushforward.lean, line 153](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FinitePresentationPushforward.lean#L153). The attribute's comment: “sheaves of sets”. References: SGA 4 IX (2.14), “(i), sets variant”; SGA 4 XIV (1.1), “special case”; SGA 4 XIV (1.11), “partial”; SGA 4 XIV (1.5), “special case”.

> **Stacks 095R for sheaves of sets.** Let `p : T ⟶ S` be a finite morphism of finite
> presentation of a big étale site and let `ℱ` be a constructible sheaf of sets on `T_étale`. Then
> `p_*ℱ` is a constructible sheaf of sets on `S_étale`. No hypothesis is imposed on `S` or `T`.
>
> By Stacks 095F constructibility may be checked on the covering of `S` by its affine opens, and
> over an affine open `U` the restriction of `p_*ℱ` is the direct image of the restriction of `ℱ`
> along the base change of `p` to `U`, which is again finite and of finite presentation; there the
> source's reduction applies: base change along the surjection of Stacks 095K (1) (Stacks 095Q (1)
> and 0959), replace the pullback by its finite étale thickening (the unit of a finite universal
> homeomorphism is an isomorphism), and conclude by Stacks 095H.
>
> The special case of a finite universal homeomorphism,
> `AlgebraicGeometry.isConstructibleSetSheaf_pushforward_of_universalHomeomorphism`, carries no
> registration.

```lean
public theorem isConstructibleSetSheaf_pushforward_of_isFinite {T S : B.Scheme} (p : T ⟶ S)
    [IsFinite (B.inclusion.map p)] (hfp : FinitePresentation (B.inclusion.map p))
    (F : Sheaf (SmallEtale.topology B T.1 T.property) (Type (u + 1)))
    (hF : IsConstructibleSetSheaf B T F) :
    IsConstructibleSetSheaf B S ((B.smallPushforward p (Type (u + 1))).obj F)
```

**`AlgebraicGeometry.isConstructibleAbelianSheaf_pushforward_of_isFinite_of_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FinitePresentationPushforwardModules.lean, line 432](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FinitePresentationPushforwardModules.lean#L432). The attribute's comment: “abelian groups”.

> **[Stacks, Tag 095R], abelian sheaves.** Let `f : T ⟶ S` be a finite and finitely presented
> morphism of a big étale site. If `ℱ` is a constructible abelian sheaf on `T_étale`, then `f_*ℱ`
> is a constructible abelian sheaf on `S_étale`.

```lean
theorem isConstructibleAbelianSheaf_pushforward_of_isFinite_of_finitePresentation {T S : B.Scheme}
    (f : T ⟶ S) [IsFinite (B.inclusion.map f)] (hfp : FinitePresentation (B.inclusion.map f))
    (F : Sheaf (SmallEtale.topology B T.1 T.property) AddCommGrpCat.{u + 1})
    (hF : IsConstructibleAbelianSheaf B T F) :
    IsConstructibleAbelianSheaf B S ((B.smallPushforward f AddCommGrpCat.{u + 1}).obj F)
```

**`AlgebraicGeometry.isConstructibleModuleSheaf_pushforward_of_isFinite_of_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FinitePresentationPushforwardModules.lean, line 509](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FinitePresentationPushforwardModules.lean#L509). The attribute's comment: “sheaves of Λ-modules, Λ Noetherian”. References: SGA 4 IX (2.14), “(i), A-module variant”; SGA 5 I (1.14), “b)”.

> **[Stacks, Tag 095R], sheaves of modules.** Let `f : T ⟶ S` be a finite and finitely
> presented morphism of a big étale site and let `Λ` be a Noetherian ring. If `ℱ` is a
> constructible sheaf of `Λ`-modules on `T_étale`, then `f_*ℱ` is a constructible sheaf of
> `Λ`-modules on `S_étale`.

```lean
theorem isConstructibleModuleSheaf_pushforward_of_isFinite_of_finitePresentation {T S : B.Scheme}
    (f : T ⟶ S) [IsFinite (B.inclusion.map f)] (hfp : FinitePresentation (B.inclusion.map f))
    (F : Sheaf (SmallEtale.topology B T.1 T.property) (ModuleCat.{u + 1} Λ))
    (hF : IsConstructibleModuleSheaf B T Λ F) :
    IsConstructibleModuleSheaf B S Λ ((B.smallPushforward f (ModuleCat.{u + 1} Λ)).obj F)
```

**`Stacks.EtaleCohomology.isConstructibleEtaleModule_directImage_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleSheaves/FiniteDirectImage.lean, line 241](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstructibleSheaves/FiniteDirectImage.lean#L241). The attribute's comment: “sheaves of Λ-modules, Λ a Noetherian ring in Type, on Mathlib's small étale site (IsBigSiteConstructibleEtaleModule); f finite and of finite presentation, no hypothesis on X or Y”.

> **Finite direct image preserves constructibility.** Let `Λ : Type` be a Noetherian ring and
> `f : X ⟶ Y` a finite morphism of finite presentation of `B`. If `ℱ` is a constructible sheaf of
> `Λ`-modules on Mathlib's small étale site of `X`, then `f_*ℱ` is constructible.

```lean
theorem isConstructibleEtaleModule_directImage_of_isFinite {X Y : B.Scheme} (f : X ⟶ Y)
    [IsFinite (B.inclusion.map f)] [LocallyOfFinitePresentation (B.inclusion.map f)]
    {F : EtaleModules.{u, 0} Λ X.obj} (hF : IsBigSiteConstructibleEtaleModule B X Λ F) :
    IsBigSiteConstructibleEtaleModule B Y Λ
      ((etaleModuleDirectImage.{u, 0} Λ (B.inclusion.map f)).obj F)
```

**`Stacks.EtaleCohomology.isConstructibleEtaleModule_etaleModuleDirectImage_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/LowerShriekAffineLine/ConstructibleDescent.lean, line 275](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/LowerShriekAffineLine/ConstructibleDescent.lean#L275). The attribute's comment: “sheaves of modules over a Noetherian ring”.

> **Stacks 095R for sheaves of modules, in the model `EtaleModules`.** Let `f : X ⟶ Y` be a
> finite morphism of finite presentation, `Λ` a Noetherian ring and `ℱ` a constructible sheaf of
> `Λ`-modules on `X_étale`. Then `f_* ℱ` is constructible.
>
> By Stacks 095F it suffices to work over the affine opens of `Y`, the direct image commuting with
> restriction to an open by Stacks 0959. Over an affine `Y`, Stacks 095K (1) gives a
> surjective affine `Y' ⟶ Y` and a thickening `Z' ⊆ Y' ×_Y X` with `Z' ⟶ Y'` finite étale; by
> Stacks 095Q and 0959 it suffices to treat the base change, where the direct image is that along
> the finite étale `Z' ⟶ Y'` of the inverse image to `Z'` (a thickening induces an equivalence of
> small étale topoi), constructible by Stacks 095H.
>
> The coefficient ring lives in `Type (u + 1)`, the universe of the library's Stacks 095Q and 095H
> for sheaves of modules.

```lean
theorem isConstructibleEtaleModule_etaleModuleDirectImage_of_isFinite {X Y : Scheme.{u}}
    (f : X ⟶ Y) [IsFinite f] (hfp : FinitePresentation f) (F : EtaleModules.{u, u + 1} Λ X)
    (hF : IsConstructibleEtaleModule Λ F) :
    IsConstructibleEtaleModule Λ ((etaleModuleDirectImage.{u, u + 1} Λ f).obj F)
```

**`Stacks.EtaleCohomology.isConstructibleEtaleAbelianSheaf_etaleAbelianDirectImage_of_isFinite`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/AbelianConstructibleImages.lean, line 119](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ProperBaseChange/AbelianConstructibleImages.lean#L119). The attribute's comment: “sheaves of abelian groups”.

> **[Stacks, Tag 095R], for sheaves of abelian groups.** Let `f : X ⟶ Y` be a finite morphism
> of finite presentation and `F` a constructible abelian sheaf on `X_étale`. Then `f_* F` is
> constructible.
>
> As a sheaf of `ULift ℤ`-modules, `F` is constructible, so `f_* F` is a constructible sheaf of
> `ULift ℤ`-modules by the module case of the tag
> (`Stacks.EtaleCohomology.isConstructibleEtaleModule_etaleModuleDirectImage_of_isFinite`). It is
> moreover torsion: `F` is torsion, being constructible
> (`Stacks.EtaleCohomology.torsionSheafProperty_of_isConstructibleEtaleAbelianSheaf`), and the
> direct image along the quasi-compact quasi-separated `f` of a torsion sheaf is torsion
> (`Stacks.EtaleCohomology.torsionSheafProperty_smallEtaleDirectImageAb`, Tag 0DDD (1) in degree
> zero). A constructible torsion sheaf of `ULift ℤ`-modules has constructible underlying abelian
> sheaf. No torsion hypothesis is imposed on `F`.

```lean
theorem isConstructibleEtaleAbelianSheaf_etaleAbelianDirectImage_of_isFinite {X Y : Scheme.{u}}
    (f : X ⟶ Y) [IsFinite f] (hfp : FinitePresentation f)
    (F : Sheaf X.smallEtaleTopology AddCommGrpCat.{u + 1})
    (hF : _root_.Stacks.EtaleCohomology.IsConstructibleSmallEtaleAbelianSheaf.{u, 0} F) :
    _root_.Stacks.EtaleCohomology.IsConstructibleSmallEtaleAbelianSheaf.{u, 0}
      ((etaleAbelianDirectImage.{u, 0} f).obj F)
```

## Tag 09YU, a lemma

[Tag 09YU](https://stacks.math.columbia.edu/tag/09YU) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleStagesFull_isConstructibleAbelianSheaf_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/LimitCategory/AbelianLimit.lean, line 62](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/LimitCategory/AbelianLimit.lean#L62). The attribute's comment: “clause (2), the fullness assertion”.

> **Stacks 09YU, clause (2), the fullness assertion.**

```lean
theorem smallEtaleStagesFull_isConstructibleAbelianSheaf_unconditional (hc : IsLimit c)
    (haff : ∀ {p q : Iᵒᵖ} (e : p ⟶ q), IsAffineHom (B.inclusion.map (Dg.map e)))
    (hqc : ∀ p : I, CompactSpace (Dg.obj (op p)).obj)
    (hqs : ∀ p : I, QuasiSeparatedSpace (Dg.obj (op p)).obj) :
    SmallEtaleStagesFull B AddCommGrpCat.{u + 1} Dg c hX
      (fun Y => IsConstructibleAbelianSheaf B Y)
```

**`AlgebraicGeometry.smallEtaleStagesEssSurj_isConstructibleAbelianSheaf_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/LimitCategory/AbelianLimit.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/LimitCategory/AbelianLimit.lean#L77). The attribute's comment: “clause (2), the essential surjectivity assertion”.

> **Stacks 09YU, clause (2), the essential surjectivity assertion.** Every constructible abelian
> sheaf on `X_étale` is isomorphic to the inverse image of a constructible abelian sheaf on some
> `(X_i)_étale`.

```lean
theorem smallEtaleStagesEssSurj_isConstructibleAbelianSheaf_unconditional (hc : IsLimit c)
    (haff : ∀ {p q : Iᵒᵖ} (e : p ⟶ q), IsAffineHom (B.inclusion.map (Dg.map e)))
    (hqc : ∀ p : I, CompactSpace (Dg.obj (op p)).obj)
    (hqs : ∀ p : I, QuasiSeparatedSpace (Dg.obj (op p)).obj) :
    SmallEtaleStagesEssSurj B AddCommGrpCat.{u + 1} Dg c hX
      (fun Y => IsConstructibleAbelianSheaf B Y)
```

**`AlgebraicGeometry.smallEtaleStagesColimit_isConstructibleAbelianSheaf_unconditional`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/LimitCategory/AbelianLimit.lean, line 126](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/LimitCategory/AbelianLimit.lean#L126). The attribute's comment: “clause (2)”.

> **Stacks 09YU, clause (2).** Let `X = lim X_i` be the limit of a directed inverse system of
> schemes with affine transition morphisms, each `X_i` quasi-compact and quasi-separated. The
> category of constructible abelian sheaves on `X_étale` is the colimit of the categories of
> constructible abelian sheaves on the `(X_i)_étale`: the comparison is faithful, full and
> essentially surjective.

```lean
theorem smallEtaleStagesColimit_isConstructibleAbelianSheaf_unconditional (hc : IsLimit c)
    (haff : ∀ {p q : Iᵒᵖ} (e : p ⟶ q), IsAffineHom (B.inclusion.map (Dg.map e)))
    (hqc : ∀ p : I, CompactSpace (Dg.obj (op p)).obj)
    (hqs : ∀ p : I, QuasiSeparatedSpace (Dg.obj (op p)).obj) :
    SmallEtaleStagesColimit B AddCommGrpCat.{u + 1} Dg c hX
      (fun Y => IsConstructibleAbelianSheaf B Y)
```

**`AlgebraicGeometry.smallEtaleStagesEssSurj_isConstructibleModuleSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/LimitCategory/ModuleEssSurj.lean, line 77](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/LimitCategory/ModuleEssSurj.lean#L77). The attribute's comment: “clause (3), the essential surjectivity assertion”. References: SGA 4 IX (2.7.4), “partial, special case”.

> **Stacks 09YU, clause (3), the essential surjectivity assertion.** Let `X = lim X_i` be the
> limit of a directed inverse system of quasi-compact and quasi-separated schemes with affine
> transition morphisms and let `Λ` be a Noetherian ring. Every constructible sheaf of `Λ`-modules on
> `X_étale` is isomorphic to the inverse image of a constructible sheaf of `Λ`-modules on some
> `(X_i)_étale`.
>
> A constructible sheaf is the cokernel of a map between finite direct sums of sheaves `j_{U!}Λ`
> with `U` affine (Stacks 095N); the affine `U` are base changed from a stage (Stacks 0EYL for
> objects, which is Stacks 01ZM and 07RP), extension by zero commutes with base change, and the map
> comes from a later stage by the fullness assertion; its cokernel there is constructible and
> pulls back to the given sheaf, inverse image being right exact.

```lean
theorem smallEtaleStagesEssSurj_isConstructibleModuleSheaf [IsNoetherianRing Λ] (hc : IsLimit c)
    (haff : ∀ {p q : Iᵒᵖ} (e : p ⟶ q), IsAffineHom (B.inclusion.map (Dg.map e)))
    (hqc : ∀ p : I, CompactSpace (Dg.obj (op p)).obj)
    (hqs : ∀ p : I, QuasiSeparatedSpace (Dg.obj (op p)).obj) :
    SmallEtaleStagesEssSurj B (ModuleCat.{u + 1} Λ) Dg c hX
      (fun Y => IsConstructibleModuleSheaf B Y Λ)
```

**`AlgebraicGeometry.smallEtaleStagesColimit_isConstructibleModuleSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/LimitCategory/ModuleEssSurj.lean, line 173](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/LimitCategory/ModuleEssSurj.lean#L173). The attribute's comment: “clause (3)”.

> **Stacks 09YU, clause (3).** Let `X = lim X_i` be the limit of a directed inverse system of
> schemes with affine transition morphisms, each `X_i` quasi-compact and quasi-separated, and let `Λ`
> be a Noetherian ring. The category of constructible sheaves of `Λ`-modules on `X_étale` is the
> colimit of the categories of constructible sheaves of `Λ`-modules on the `(X_i)_étale`: the
> comparison, built from the inverse images and the canonical comparisons of iterated inverse
> images, is faithful, full and essentially surjective. For a directed index these three conditions
> are exactly the assertion that the canonical functor from the filtered colimit of the categories
> is an equivalence.
>
> Nothing is assumed beyond the source's hypotheses: a nonempty directed index, a limit cone,
> affine transition morphisms, and quasi-compact quasi-separated stages.

```lean
theorem smallEtaleStagesColimit_isConstructibleModuleSheaf [IsNoetherianRing Λ] (hc : IsLimit c)
    (haff : ∀ {p q : Iᵒᵖ} (e : p ⟶ q), IsAffineHom (B.inclusion.map (Dg.map e)))
    (hqc : ∀ p : I, CompactSpace (Dg.obj (op p)).obj)
    (hqs : ∀ p : I, QuasiSeparatedSpace (Dg.obj (op p)).obj) :
    SmallEtaleStagesColimit B (ModuleCat.{u + 1} Λ) Dg c hX
      (fun Y => IsConstructibleModuleSheaf B Y Λ)
```

**`AlgebraicGeometry.smallEtaleStagesFull_isConstructibleModuleSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/LimitCategory/ModuleFullness.lean, line 217](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/LimitCategory/ModuleFullness.lean#L217). The attribute's comment: “clause (3), the fullness assertion”. References: SGA 4 IX (2.7.4), “partial”.

> **Stacks 09YU, clause (3), the fullness assertion.** Let `X = lim X_i` be the limit of a
> directed inverse system of quasi-compact and quasi-separated schemes with affine transition
> morphisms and let `Λ` be a Noetherian ring. Every map between the inverse images to `X_étale` of
> two constructible sheaves of `Λ`-modules on `(X_i)_étale` is the inverse image of a map at some
> later stage, read through the canonical comparison of inverse images.
>
> A constructible sheaf is a quotient of a finite direct sum of sheaves `j_{U!}Λ` with `U` affine by
> Stacks 095N; the map on the sum comes from a stage by the degree zero case of Stacks 09YQ, its
> restriction to the kernel vanishes on `X` and hence, by the faithfulness assertion, at a later
> stage, where the map descends to the quotient.

```lean
theorem smallEtaleStagesFull_isConstructibleModuleSheaf [IsNoetherianRing Λ] (hc : IsLimit c)
    (haff : ∀ {p q : Iᵒᵖ} (e : p ⟶ q), IsAffineHom (B.inclusion.map (Dg.map e)))
    (hqc : ∀ p : I, CompactSpace (Dg.obj (op p)).obj)
    (hqs : ∀ p : I, QuasiSeparatedSpace (Dg.obj (op p)).obj) :
    SmallEtaleStagesFull B (ModuleCat.{u + 1} Λ) Dg c hX
      (fun Y => IsConstructibleModuleSheaf B Y Λ)
```

**`AlgebraicGeometry.smallEtaleStagesFaithful_isConstructibleAbelianSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StageColimitCompletion.lean, line 166](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StageColimitCompletion.lean#L166). The attribute's comment: “clause (2), the faithfulness assertion”.

> **Stacks 09YU, clause (2), the faithfulness assertion.** Let `X = lim X_i` be the limit of a
> directed inverse system of quasi-compact and quasi-separated schemes with affine transition
> morphisms. Two maps of constructible sheaves of abelian groups on `(X_i)_étale` whose inverse
> images to `X_étale` agree agree after inverse image to some later stage.
>
> The image of the difference of the two maps is constructible by Tag 03RZ, so the locus where it
> has a nonzero geometric stalk is constructible by Tag 09YS (2); inverse image to `X` is exact and
> kills the difference, hence the image, so by Tag 03Q1 that locus misses the image of `X` and by
> Tag 05F4 the image of a later stage, where Tag 03PU makes the inverse image of the image sheaf
> zero.

```lean
public theorem smallEtaleStagesFaithful_isConstructibleAbelianSheaf (hc : IsLimit c)
    (haff : ∀ {p q : Iᵒᵖ} (e : p ⟶ q), IsAffineHom (B.inclusion.map (Dg.map e)))
    (hqc : ∀ p : I, CompactSpace (Dg.obj (op p)).obj)
    (hqs : ∀ p : I, QuasiSeparatedSpace (Dg.obj (op p)).obj) :
    SmallEtaleStagesFaithful B AddCommGrpCat.{u + 1} Dg c hX
      (fun Y => IsConstructibleAbelianSheaf B Y)
```

**`AlgebraicGeometry.smallEtaleStagesEssSurj_isConstructibleSetSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StageConstructibleSetSheafDescent.lean, line 454](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StageConstructibleSetSheafDescent.lean#L454). The attribute's comment: “clause (1), the essential surjectivity assertion”. References: SGA 4 IX (2.7.4), “partial, special case”.

> **Stacks 09YU, clause (1), the essential surjectivity assertion.** Let `X = lim X_i` be the
> limit of a directed inverse system of quasi-compact and quasi-separated schemes with affine
> transition morphisms inside a big étale site. Every constructible sheaf of sets on `X_étale` is
> isomorphic to the inverse image of a constructible sheaf of sets on `(X_i)_étale` for some `i`.
>
> Tag 09Y9 presents the sheaf as a coequalizer of two maps between finite coproducts of sheaves
> represented by quasi-compact and quasi-separated objects; those coproducts are represented by the
> disjoint unions of the objects, so the two maps are a parallel pair of morphisms of the site,
> which descends to a stage by
> `AlgebraicGeometry.exists_stage_smallEtaleModel_parallelPair_of_qcqs`. The coequalizer of the
> descended pair of representable sheaves is constructible at that stage by Tag 03RZ and Tag 03S8
> part (1), and inverse image, a left adjoint commuting with the sheafified Yoneda embedding,
> carries it to the given sheaf.

```lean
public theorem smallEtaleStagesEssSurj_isConstructibleSetSheaf (hc : IsLimit c)
    (haff : ∀ {p q : Iᵒᵖ} (e : p ⟶ q), IsAffineHom (B.inclusion.map (Dg.map e)))
    (hqc : ∀ p : I, CompactSpace (Dg.obj (op p)).obj)
    (hqs : ∀ p : I, QuasiSeparatedSpace (Dg.obj (op p)).obj) :
    SmallEtaleStagesEssSurj B (Type (u + 1)) Dg c hX
      (fun X => IsConstructibleSetSheaf B X)
```

**`AlgebraicGeometry.smallEtaleStagesFaithful_isConstructibleSetSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StageFaithfulness.lean, line 218](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StageFaithfulness.lean#L218). The attribute's comment: “clause (1), the faithfulness assertion”.

> **Stacks 09YU, clause (1), the faithfulness assertion.** Let `X = lim X_i` be the limit of a
> directed inverse system of quasi-compact and quasi-separated schemes with affine transition
> morphisms. Two maps of constructible sheaves of sets on `(X_i)_étale` whose inverse images to
> `X_étale` agree agree after inverse image to some later stage.
>
> The locus in `X_i` where the two maps have the same geometric stalk is the locus where the
> geometric stalk of the inclusion of their equalizer is surjective; the equalizer is constructible
> by Tag 03RZ, so that locus is constructible by Tag 09YS and contains the image of `X`, hence by
> Tag 05F4 the image of a later stage, where Tag 03PU turns the inverse image of the inclusion into
> an isomorphism.

```lean
public theorem smallEtaleStagesFaithful_isConstructibleSetSheaf (hc : IsLimit c)
    (haff : ∀ {p q : Iᵒᵖ} (e : p ⟶ q), IsAffineHom (B.inclusion.map (Dg.map e)))
    (hqc : ∀ p : I, CompactSpace (Dg.obj (op p)).obj)
    (hqs : ∀ p : I, QuasiSeparatedSpace (Dg.obj (op p)).obj) :
    SmallEtaleStagesFaithful B (Type (u + 1)) Dg c hX
      (fun Y => IsConstructibleSetSheaf B Y)
```

**`AlgebraicGeometry.smallEtaleStagesFaithful_isConstructibleModuleSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StageFaithfulnessModules.lean, line 172](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StageFaithfulnessModules.lean#L172). The attribute's comment: “clause (3), the faithfulness assertion”.

> **Stacks 09YU, clause (3), the faithfulness assertion.** Let `X = lim X_i` be the limit of a
> directed inverse system of quasi-compact and quasi-separated schemes with affine transition
> morphisms and let `Λ` be a Noetherian ring. Two maps of constructible sheaves of `Λ`-modules on
> `(X_i)_étale` whose inverse images to `X_étale` agree agree after inverse image to some later
> stage.
>
> The image of the difference of the two maps is constructible by Tag 03RZ (3), so its support is
> constructible by Tag 09YS (3); inverse image to `X` is exact and kills the difference, hence the
> image, so by Tag 03Q1 that support misses the image of `X` and by Tag 05F4 the image of a later
> stage, where Tag 03PU makes the inverse image of the image sheaf zero.

```lean
public theorem smallEtaleStagesFaithful_isConstructibleModuleSheaf (hc : IsLimit c)
    (haff : ∀ {p q : Iᵒᵖ} (e : p ⟶ q), IsAffineHom (B.inclusion.map (Dg.map e)))
    (hqc : ∀ p : I, CompactSpace (Dg.obj (op p)).obj)
    (hqs : ∀ p : I, QuasiSeparatedSpace (Dg.obj (op p)).obj) :
    SmallEtaleStagesFaithful B (ModuleCat.{u + 1} Λ) Dg c hX
      (fun Y => IsConstructibleModuleSheaf B Y Λ)
```

**`AlgebraicGeometry.smallEtaleStagesColimit_isConstructibleSetSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StageFullness.lean, line 1073](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StageFullness.lean#L1073). The attribute's comment: “clause (1)”.

> **Stacks 09YU, clause (1).** Let `X = lim X_i` be the limit of a directed inverse system of
> quasi-compact and quasi-separated schemes with affine transition morphisms inside a big étale
> site. The category of constructible sheaves of sets on `X_étale` is the colimit of the categories
> of constructible sheaves of sets on the `(X_i)_étale`, along étale inverse image: the comparison
> is faithful (`AlgebraicGeometry.smallEtaleStagesFaithful_isConstructibleSetSheaf`), full
> (`AlgebraicGeometry.smallEtaleStagesFull_isConstructibleSetSheaf`) and essentially surjective
> (`AlgebraicGeometry.smallEtaleStagesEssSurj_isConstructibleSetSheaf`), which over a directed index
> is the assertion that the category on the limit is the filtered colimit of the categories at the
> stages.

```lean
public theorem smallEtaleStagesColimit_isConstructibleSetSheaf (hc : IsLimit c)
    (haff : ∀ {p q : Iᵒᵖ} (e : p ⟶ q), IsAffineHom (B.inclusion.map (Dg.map e)))
    (hqc : ∀ p : I, CompactSpace (Dg.obj (op p)).obj)
    (hqs : ∀ p : I, QuasiSeparatedSpace (Dg.obj (op p)).obj) :
    SmallEtaleStagesColimit B (Type (u + 1)) Dg c hX (fun X => IsConstructibleSetSheaf B X)
```

**`AlgebraicGeometry.smallEtaleStagesColimit_isConstructibleAbelianSheaf`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StageFullnessAbelian.lean, line 1049](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StageFullnessAbelian.lean#L1049). The attribute's comment: “clause (2)”.

> **Stacks 09YU, clause (2).** Let `X = lim X_i` be the limit of a directed inverse system of
> quasi-compact and quasi-separated schemes with affine transition morphisms inside a big étale
> site. The category of constructible abelian sheaves on `X_étale` is the colimit of the categories
> of constructible abelian sheaves on the `(X_i)_étale`, along étale inverse image: the comparison is
> faithful (`AlgebraicGeometry.smallEtaleStagesFaithful_isConstructibleAbelianSheaf`), full
> (`AlgebraicGeometry.smallEtaleStagesFull_isConstructibleAbelianSheaf`) and essentially surjective
> (`AlgebraicGeometry.smallEtaleStagesEssSurj_isConstructibleAbelianSheaf`), which over a directed
> index is the assertion that the category on the limit is the filtered colimit of the categories at
> the stages.

```lean
public theorem smallEtaleStagesColimit_isConstructibleAbelianSheaf [Nonempty I]
    [IsDirected I (· ≤ ·)] (hc : IsLimit c)
    (haff : ∀ {p q : Iᵒᵖ} (e : p ⟶ q), IsAffineHom (B.inclusion.map (Dg.map e)))
    (hqc : ∀ p : I, CompactSpace (Dg.obj (op p)).obj)
    (hqs : ∀ p : I, QuasiSeparatedSpace (Dg.obj (op p)).obj) :
    SmallEtaleStagesColimit B AddCommGrpCat.{u + 1} Dg c hX
      (fun Y => IsConstructibleAbelianSheaf B Y)
```

**`AlgebraicGeometry.exists_stage_isConstructibleSetSheaf_iso_sheafifiedYoneda`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StageRepresentableEssSurj.lean, line 152](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/StageRepresentableEssSurj.lean#L152). The attribute's comment: “clause (1), the essential surjectivity assertion for the sheaves represented by a quasi-compact and quasi-separated object of the small etale site, which is the case the source's proof reduces that assertion to”.

> **Stacks 09YU, clause (1), the essential surjectivity assertion for a representable sheaf.**
> Let `X = lim X_i` be the limit of a directed inverse system of quasi-compact and quasi-separated
> schemes with affine transition morphisms inside a big étale site. For every quasi-compact and
> quasi-separated object `U` of `X_étale` there is a stage `i` and a *constructible* sheaf of sets
> on `(X_i)_étale` whose inverse image to `X_étale` is the sheaf `h_U` represented by `U`.
>
> This is the case of the essential surjectivity assertion of clause (1) to which the source
> reduces it through Tag 09Y9. The object `U` is descended to the stage by
> `AlgebraicGeometry.exists_stage_smallEtaleModel_of_qcqs`; inverse image carries the representable
> sheaf of the descended object to the representable sheaf of its base change, because inverse
> image along a continuous functor commutes with the sheafified Yoneda embedding; and the
> representable sheaf of a quasi-compact and quasi-separated object is constructible by Tag 03S8
> part (1).

```lean
public theorem exists_stage_isConstructibleSetSheaf_iso_sheafifiedYoneda (hc : IsLimit c)
    (haff : ∀ {p q : Iᵒᵖ} (e : p ⟶ q), IsAffineHom (B.inclusion.map (Dg.map e)))
    (hqc : ∀ p : I, CompactSpace (Dg.obj (op p)).obj)
    (hqs : ∀ p : I, QuasiSeparatedSpace (Dg.obj (op p)).obj)
    (U : SmallEtale B c.pt hX)
    (hUc : CompactSpace U.obj.left.obj) (hUq : QuasiSeparatedSpace U.obj.left.obj) :
    ∃ (i : I) (Fi : Sheaf (SmallEtale.topology B (Dg.obj (op i)).obj
        (Dg.obj (op i)).property) (Type (u + 1))),
      IsConstructibleSetSheaf B (Dg.obj (op i)) Fi ∧
        Nonempty ((smallEtaleStageProjection B (Type (u + 1)) Dg c hX i).obj Fi ≅
          (Sheaf.sheafifiedYoneda (SmallEtale.topology B c.pt hX)).obj U)
```

## Tag 0GL2, a lemma

[Tag 0GL2](https://stacks.math.columbia.edu/tag/0GL2) in the Stacks Project.

**`AlgebraicGeometry.smallEtaleStagesColimit_isFiniteLocallyConstant_type`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FiniteLocallyConstantLimitColimit.lean, line 68](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FiniteLocallyConstantLimitColimit.lean#L68). The attribute's comment: “part (1)”.

> **Stacks Tag 0GL2, clause (1).** Let `X = lim X_i` be the limit of a directed inverse system
> of quasi-compact, quasi-separated schemes with affine transition morphisms. The category of
> finite locally constant sheaves of sets on `X_étale` is the colimit of the categories of finite
> locally constant sheaves of sets on the `(X_i)_étale`: the comparison is faithful, full and
> essentially surjective.

```lean
public theorem smallEtaleStagesColimit_isFiniteLocallyConstant_type (hc : IsLimit c)
    (haff : ∀ {p q : Iᵒᵖ} (e : p ⟶ q), IsAffineHom (B.inclusion.map (Dg.map e)))
    (hqc : ∀ p : I, CompactSpace (Dg.obj (op p)).obj)
    (hqs : ∀ p : I, QuasiSeparatedSpace (Dg.obj (op p)).obj) :
    SmallEtaleStagesColimit B (Type (u + 1)) Dg c hX
      (isFiniteLocallyConstantSmallEtaleSheaf B (Type (u + 1)))
```

**`AlgebraicGeometry.smallEtaleStagesColimit_isFiniteLocallyConstant_addCommGrpCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FiniteLocallyConstantLimitColimit.lean, line 83](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FiniteLocallyConstantLimitColimit.lean#L83). The attribute's comment: “part (2)”.

> **Stacks Tag 0GL2, clause (2).** Let `X = lim X_i` be the limit of a directed inverse system
> of quasi-compact, quasi-separated schemes with affine transition morphisms. The category of
> finite locally constant abelian sheaves on `X_étale` is the colimit of the categories of finite
> locally constant abelian sheaves on the `(X_i)_étale`.

```lean
public theorem smallEtaleStagesColimit_isFiniteLocallyConstant_addCommGrpCat (hc : IsLimit c)
    (haff : ∀ {p q : Iᵒᵖ} (e : p ⟶ q), IsAffineHom (B.inclusion.map (Dg.map e)))
    (hqc : ∀ p : I, CompactSpace (Dg.obj (op p)).obj)
    (hqs : ∀ p : I, QuasiSeparatedSpace (Dg.obj (op p)).obj) :
    SmallEtaleStagesColimit B AddCommGrpCat.{u + 1} Dg c hX
      (isFiniteLocallyConstantSmallEtaleSheaf B AddCommGrpCat.{u + 1})
```

**`AlgebraicGeometry.smallEtaleStagesColimit_isFiniteTypeLocallyConstant_moduleCat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FiniteLocallyConstantLimitColimit.lean, line 101](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/FiniteLocallyConstantLimitColimit.lean#L101). The attribute's comment: “part (3)”.

> **Stacks Tag 0GL2, clause (3).** Let `X = lim X_i` be the limit of a directed inverse system
> of quasi-compact, quasi-separated schemes with affine transition morphisms and let `Λ` be a
> commutative ring (the source assumes `Λ` Noetherian; that is not needed). The category of finite
> type, locally constant sheaves of `Λ`-modules on `X_étale` is the colimit of the categories of
> finite type, locally constant sheaves of `Λ`-modules on the `(X_i)_étale`.

```lean
public theorem smallEtaleStagesColimit_isFiniteTypeLocallyConstant_moduleCat
    (Λ : Type (u + 1)) [CommRing Λ] (hc : IsLimit c)
    (haff : ∀ {p q : Iᵒᵖ} (e : p ⟶ q), IsAffineHom (B.inclusion.map (Dg.map e)))
    (hqc : ∀ p : I, CompactSpace (Dg.obj (op p)).obj)
    (hqs : ∀ p : I, QuasiSeparatedSpace (Dg.obj (op p)).obj) :
    SmallEtaleStagesColimit B (ModuleCat.{u + 1} Λ) Dg c hX
      (isFiniteTypeLocallyConstantSmallEtaleSheaf B Λ)
```

## Tag 09BG, a lemma

[Tag 09BG](https://stacks.math.columbia.edu/tag/09BG) in the Stacks Project.

**`AlgebraicGeometry.constantSetSubsheaf_eq_of_genericStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstantSubsheafGenericStalk.lean, line 161](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstantSubsheafGenericStalk.lean#L161). The attribute's comment: “part (1)”.

> **Stacks 09BG (1).** A subsheaf of a constant sheaf of sets on an irreducible scheme which
> contains the constant subsheaf on its geometric generic stalk is that constant subsheaf.

```lean
public theorem constantSetSubsheaf_eq_of_genericStalk
    [HasWeakSheafify (SmallEtale.topology B X hX) (Type (u + 1))]
    {T' T : Type (u + 1)} (m : T' ⟶ T) [Mono m]
    (G : Sheaf (SmallEtale.topology B X hX) (Type (u + 1)))
    (i : (constantSheaf (SmallEtale.topology B X hX) (Type (u + 1))).obj T' ⟶ G)
    (j : G ⟶ (constantSheaf (SmallEtale.topology B X hX) (Type (u + 1))).obj T) [Mono j]
    (hij : i ≫ j = (constantSheaf (SmallEtale.topology B X hX) (Type (u + 1))).map m)
    (hstalk : IsIso (colimMap (Functor.whiskerLeft
      (Functor.Elements.π (geometricPointFiber B X hX s)).op i.hom))) :
    IsIso i
```

**`AlgebraicGeometry.constantAbelianSubsheaf_eq_of_genericStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstantSubsheafGenericStalk.lean, line 180](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstantSubsheafGenericStalk.lean#L180). The attribute's comment: “part (2)”.

> **Stacks 09BG (2).** A subsheaf of a constant sheaf of abelian groups on an irreducible
> scheme which contains the constant subsheaf on its geometric generic stalk is that constant
> subsheaf.

```lean
public theorem constantAbelianSubsheaf_eq_of_genericStalk
    [HasWeakSheafify (SmallEtale.topology B X hX) AddCommGrpCat.{u + 1}]
    {A' A : AddCommGrpCat.{u + 1}} (m : A' ⟶ A) [Mono m]
    (G : Sheaf (SmallEtale.topology B X hX) AddCommGrpCat.{u + 1})
    (i : (constantSheaf (SmallEtale.topology B X hX) AddCommGrpCat.{u + 1}).obj A' ⟶ G)
    (j : G ⟶ (constantSheaf (SmallEtale.topology B X hX) AddCommGrpCat.{u + 1}).obj A) [Mono j]
    (hij : i ≫ j = (constantSheaf (SmallEtale.topology B X hX) AddCommGrpCat.{u + 1}).map m)
    (hstalk : IsIso (colimMap (Functor.whiskerLeft
      (Functor.Elements.π (geometricPointFiber B X hX s)).op i.hom))) :
    IsIso i
```

**`AlgebraicGeometry.constantModuleSubsheaf_eq_of_genericStalk`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstantSubsheafGenericStalk.lean, line 198](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstantSubsheafGenericStalk.lean#L198). The attribute's comment: “part (3)”.

> **Stacks 09BG (3).** A subsheaf of a constant sheaf of modules on an irreducible scheme which
> contains the constant subsheaf on its geometric generic stalk is that constant subsheaf.

```lean
public theorem constantModuleSubsheaf_eq_of_genericStalk (Λ : Type (u + 1)) [Ring Λ]
    [HasWeakSheafify (SmallEtale.topology B X hX) (ModuleCat.{u + 1} Λ)]
    {M' M : ModuleCat.{u + 1} Λ} (m : M' ⟶ M) [Mono m]
    (G : Sheaf (SmallEtale.topology B X hX) (ModuleCat.{u + 1} Λ))
    (i : (constantSheaf (SmallEtale.topology B X hX) (ModuleCat.{u + 1} Λ)).obj M' ⟶ G)
    (j : G ⟶ (constantSheaf (SmallEtale.topology B X hX) (ModuleCat.{u + 1} Λ)).obj M) [Mono j]
    (hij : i ≫ j = (constantSheaf (SmallEtale.topology B X hX) (ModuleCat.{u + 1} Λ)).map m)
    (hstalk : IsIso (colimMap (Functor.whiskerLeft
      (Functor.Elements.π (geometricPointFiber B X hX s)).op i.hom))) :
    IsIso i
```

## Tag 09Z5, a lemma

[Tag 09Z5](https://stacks.math.columbia.edu/tag/09Z5) in the Stacks Project.

**`Stacks.EtaleCohomology.isIso_constantSheafPushforwardComparison_genericPointInclusion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstantSheafPushforwardNormal.lean, line 419](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstantSheafPushforwardNormal.lean#L419). The attribute's comment: “part (1)”. References: SGA 4 IX (2.14.1), “special case”; SGA 7 VIII (5.1), “special case”.

> On an integral normal scheme the direct image of a constant sheaf
> of sets along the inclusion of the generic point is the constant sheaf: the canonical comparison
> morphism is an isomorphism.

```lean
theorem isIso_constantSheafPushforwardComparison_genericPointInclusion (X : Scheme.{u})
    [AlgebraicGeometry.IsIntegral X] [IsNormal X] (E : Type (max (u + 1) v)) :
    IsIso (constantSheafPushforwardComparison.{u, v} (genericPointInclusion X) E)
```

**`Stacks.EtaleCohomology.constantSheafGenericPointPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstantSheafPushforwardNormal.lean, line 435](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstantSheafPushforwardNormal.lean#L435). The attribute's comment: “part (1)”. References: SGA 4 IX (2.14.1), “special case”; SGA 7 VIII (5.1), “special case”.

> The identification `g_* E̲ = E̲` of the direct image of a constant
> sheaf of sets along the inclusion `g : Spec K ⟶ X` of the generic point of an integral normal
> scheme with the constant sheaf, given by the canonical comparison morphism.

```lean
def constantSheafGenericPointPushforwardIso (X : Scheme.{u})
    [AlgebraicGeometry.IsIntegral X] [IsNormal X] (E : Type (max (u + 1) v)) :
    (constantSheaf X.smallEtaleTopology (Type (max (u + 1) v))).obj E ≅
      (smallEtaleDirectImage.{u, v} (genericPointInclusion X)).obj
        ((constantSheaf (Spec X.functionField).smallEtaleTopology
          (Type (max (u + 1) v))).obj E)
```

**`Stacks.EtaleCohomology.isIso_constantSheafPushforwardComparison_opensIota`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstantSheafPushforwardNormal.lean, line 448](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstantSheafPushforwardNormal.lean#L448). The attribute's comment: “part (2)”.

> On an integral normal scheme the direct image of a constant sheaf
> of sets along the inclusion of a nonempty open subscheme is the constant sheaf: the canonical
> comparison morphism is an isomorphism.

```lean
theorem isIso_constantSheafPushforwardComparison_opensIota {X : Scheme.{u}}
    [AlgebraicGeometry.IsIntegral X] [IsNormal X] (U : X.Opens) (hU : (U : Set X).Nonempty)
    (E : Type (max (u + 1) v)) :
    IsIso (constantSheafPushforwardComparison.{u, v} U.ι E)
```

**`Stacks.EtaleCohomology.constantSheafOpensPushforwardIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstantSheafPushforwardNormal.lean, line 463](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/ConstantSheafPushforwardNormal.lean#L463). The attribute's comment: “part (2)”.

> The identification `j_* E̲ = E̲` of the direct image of a constant
> sheaf of sets along the inclusion `j : U ⟶ X` of a nonempty open subscheme of an integral normal
> scheme with the constant sheaf, given by the canonical comparison morphism.

```lean
def constantSheafOpensPushforwardIso {X : Scheme.{u}} [AlgebraicGeometry.IsIntegral X]
    [IsNormal X] (U : X.Opens) (hU : (U : Set X).Nonempty) (E : Type (max (u + 1) v)) :
    (constantSheaf X.smallEtaleTopology (Type (max (u + 1) v))).obj E ≅
      (smallEtaleDirectImage.{u, v} U.ι).obj
        ((constantSheaf U.toScheme.smallEtaleTopology (Type (max (u + 1) v))).obj E)
```

## Tag 0F0M, a lemma

[Tag 0F0M](https://stacks.math.columbia.edu/tag/0F0M) in the Stacks Project.

**`AlgebraicGeometry.exists_isFilteredColimit_isConstructibleAbelianSheaf_support_notMem_of_torsion`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ZeroStalkAtGenericPointColimit.lean, line 195](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ZeroStalkAtGenericPointColimit.lean#L195). The attribute's comment: “part (1), torsion abelian sheaves: every local section is locally annihilated by a positive integer”.

> **Stacks 0F0M (1).** Let `X` be a quasi-compact and quasi-separated scheme and let `η` be a
> generic point of an irreducible component of `X`. Let `ℱ` be a torsion abelian sheaf on `X_étale`
> whose stalk at a geometric point `η̄` above `η` is zero. Then `ℱ` is a filtered colimit of
> constructible abelian sheaves, each of whose supports is contained in a closed subset of `X` —
> equivalently a closed subscheme of `X` — not containing `η`.
>
> Torsion is `Stacks.Torsion.torsionSheafProperty`: every local section of `ℱ` is, locally on
> `X_étale`, annihilated by a positive integer, that is `ℱ` is the union of its subsheaves `ℱ[n]`.
> This is the notion of torsion abelian sheaf of the source (Stacks 0DD7, 03SA (2)), and it is
> implied by asking every section over every étale `U → X` to be torsion. This is
> `AlgebraicGeometry.exists_isFilteredColimit_isConstructibleAbelianSheaf_support_notMem` with its
> two inputs proved: Stacks 03SA (2) is
> `AlgebraicGeometry.exists_isFilteredColimit_isConstructibleAbelianSheaf_of_qcqs`, and Stacks 095P
> in the form the source uses is
> `AlgebraicGeometry.exists_smallEtaleGeometricStalkFunctor_map_eq_zero`.

```lean
public theorem exists_isFilteredColimit_isConstructibleAbelianSheaf_support_notMem_of_torsion
    [CompactSpace X.obj] [QuasiSeparatedSpace X.obj]
    (η : X.obj) (hη : η ∈ genericPoints X.obj)
    (p : GeometricPoint X.obj) (hp : GeometricPoint.LiesOver p η)
    (ℱ : Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1})
    (hℱ : Stacks.Torsion.torsionSheafProperty (SmallEtale.topology B X.obj X.property) ℱ)
    (hstalk : IsZero ((smallEtaleGeometricStalkFunctor B X p).obj ℱ)) :
    ∃ (J : Type (u + 1)) (_ : SmallCategory J) (_ : IsFiltered J)
      (G : J ⥤ Sheaf (SmallEtale.topology B X.obj X.property) AddCommGrpCat.{u + 1})
      (κ : G ⟶ (Functor.const J).obj ℱ),
      Nonempty (IsColimit (Cocone.mk ℱ κ)) ∧
        (∀ j, IsConstructibleAbelianSheaf B X (G.obj j)) ∧
          ∀ j, ∃ Z : Set X.obj, IsClosed Z ∧ η ∉ Z ∧
            supportSheaf.{u, u + 1} B X.obj X.property (G.obj j) ⊆ Z
```

**`AlgebraicGeometry.exists_isFilteredColimit_isConstructibleModuleSheaf_support_notMem`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ZeroStalkAtGenericPointColimit.lean, line 301](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/EtaleCohomology/Constructible/ZeroStalkAtGenericPointColimit.lean#L301). The attribute's comment: “part (2), sheaves of modules over a Noetherian ring”.

> **Stacks 0F0M (2).** Let `X` be a quasi-compact and quasi-separated scheme, let `η` be a
> generic point of an irreducible component of `X` and let `Λ` be a Noetherian ring. Let `ℱ` be a
> sheaf of `Λ`-modules on `X_étale` whose stalk at a geometric point `η̄` above `η` is zero. Then
> `ℱ` is a filtered colimit of constructible sheaves of `Λ`-modules, each of whose supports is
> contained in a closed subset of `X` — equivalently a closed subscheme of `X` — not containing
> `η`.
>
> The proof is the source's proof of part (1), which it says carries over verbatim. Write
> `ℱ = colim ℱᵢ` with `ℱᵢ` constructible by Stacks 03SA (3); out of every `i` choose a transition
> map `ℱᵢ ⟶ ℱ_{i'(i)}` whose stalk at `η̄` vanishes, by Stacks 095P in the stalkwise form
> `AlgebraicGeometry.exists_smallEtaleGeometricStalkModuleFunctor_map_eq_zero`; the images of these
> transition maps form a filtered system with colimit `ℱ`
> (`CategoryTheory.Limits.isColimitArrowImageCocone`), each image is constructible by Stacks 03RZ
> and has vanishing stalk at `η̄`, its support is constructible by Stacks 09YS (3), and the closure
> of a constructible set avoiding the generic point `η` avoids `η`.

```lean
public theorem exists_isFilteredColimit_isConstructibleModuleSheaf_support_notMem
    [CompactSpace X.obj] [QuasiSeparatedSpace X.obj]
    (η : X.obj) (hη : η ∈ genericPoints X.obj)
    (p : GeometricPoint X.obj) (hp : GeometricPoint.LiesOver p η)
    (ℱ : Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{u + 1} Λ))
    (hstalk : IsZero (etaleStalk B X.obj X.property p ℱ.obj)) :
    ∃ (J : Type (u + 1)) (_ : SmallCategory J) (_ : IsFiltered J)
      (G : J ⥤ Sheaf (SmallEtale.topology B X.obj X.property) (ModuleCat.{u + 1} Λ))
      (κ : G ⟶ (Functor.const J).obj ℱ),
      Nonempty (IsColimit (Cocone.mk ℱ κ)) ∧
        (∀ j, IsConstructibleModuleSheaf B X Λ (G.obj j)) ∧
          ∀ j, ∃ Z : Set X.obj, IsClosed Z ∧ η ∉ Z ∧ supportModuleSheaf B X Λ (G.obj j) ⊆ Z
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 59.73, Tag 095M](https://stacks.math.columbia.edu/tag/095M)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
