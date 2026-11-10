---
declaration: section
origin: cited
lean: AlgebraicGeometry.LimitDescent.exists_model_of_finitePresentation_of_essentiallySmall, AlgebraicGeometry.exists_morphism_after_baseChange, AlgebraicGeometry.eventually_eq_of_baseChange_eq, AlgebraicGeometry.Scheme.eventually_eq_of_baseChange_eq, AlgebraicGeometry.LimitFPObjectDescent.exists_model_of_finitePresentation, Stacks.AlgebraicGeometry.ModuleLimits.exists_pullback_map_eq_of_isLimit, Stacks.AlgebraicGeometry.ModuleLimits.exists_map_of_pullback_of_isLimit, Stacks.AlgebraicGeometry.ModuleLimits.exists_isFinitePresentation_pullback_iso_of_qcqs
statement: formalized
proof: formalized
---

# 32.10 Descending relative objects

Section 32.10 of the Stacks Project, [Tag 01ZL](https://stacks.math.columbia.edu/tag/01ZL). 5 tags here are carried by 15 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01ZM, a lemma

[Tag 01ZM](https://stacks.math.columbia.edu/tag/01ZM) in the Stacks Project.

**`AlgebraicGeometry.LimitDescent.exists_model_of_finitePresentation_of_essentiallySmall`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LimitDescentGlueing/Glueing.lean, line 626](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LimitDescentGlueing/Glueing.lean#L626). The attribute's comment: “part (1)”. References: EGA IV (8.1.1), “more general”; EGA IV (8.8.3), “essential surjectivity”; SGA 3 VIB (10.0), “(ii)”; SGA 4 VII (5.2), “(b)”; SGA 4 VII (5.3), “essential surjectivity”.

> Let `S = lim Sᵢ` be a cofiltered limit of quasi-compact, quasi-separated schemes with affine
> transition morphisms. Every scheme of finite presentation over `S` is isomorphic, over `S`, to the
> base change of a scheme of finite presentation over one of the stages `Sᵢ`.
>
> This is
> `AlgebraicGeometry.LimitDescent.exists_isPullback_of_finitePresentation_of_essentiallySmall`
> stated with `CategoryTheory.Over.pullback`. The index hypothesis
> `CategoryTheory.EssentiallySmall.{u} I` is relative to the universe of the schemes.

```lean
public theorem exists_model_of_finitePresentation_of_essentiallySmall {I : Type v}
    [Category.{w} I] [IsCofiltered I] [EssentiallySmall.{u} I] (D : I ⥤ Scheme.{u}) (c : Cone D)
    (hc : IsLimit c) [∀ {i j : I} (g : i ⟶ j), IsAffineHom (D.map g)]
    [∀ i : I, CompactSpace (D.obj i)] [∀ i : I, QuasiSeparatedSpace (D.obj i)]
    (X : Over c.pt) (hX : FinitePresentation X.hom) :
    ∃ (i : I) (Xᵢ : Over (D.obj i)), FinitePresentation Xᵢ.hom ∧
      Nonempty (X ≅ (Over.pullback (c.π.app i)).obj Xᵢ)
```

**`AlgebraicGeometry.exists_morphism_after_baseChange`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Relative.lean, line 302](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Relative.lean#L302). The attribute's comment: “part (2)”.

> A morphism between the base changes of two schemes of finite presentation
> descends after passing to a later stage of a cofiltered inverse system.

```lean
theorem exists_morphism_after_baseChange
    {I : Type v} [Category.{w} I] [IsCofiltered I] [EssentiallySmall.{u} I]
    (D : I ⥤ Scheme.{u}) (c : Cone D) (hc : IsLimit c)
    [∀ {i j : I} (e : i ⟶ j), IsAffineHom (D.map e)]
    [∀ i : I, CompactSpace (D.obj i)]
    [∀ i : I, QuasiSeparatedSpace (D.obj i)]
    (i : I) (X Y : Over (D.obj i))
    (hX : FinitePresentation X.hom) (hY : FinitePresentation Y.hom)
    (f : (Over.pullback (c.π.app i)).obj X ⟶ (Over.pullback (c.π.app i)).obj Y) :
    ∃ (j : I) (e : j ⟶ i)
      (g : (Over.pullback (D.map e)).obj X ⟶ (Over.pullback (D.map e)).obj Y)
      (α : (Over.pullback (c.π.app j)).obj ((Over.pullback (D.map e)).obj X) ≅
        (Over.pullback (c.π.app i)).obj X)
      (β : (Over.pullback (c.π.app j)).obj ((Over.pullback (D.map e)).obj Y) ≅
        (Over.pullback (c.π.app i)).obj Y),
      α.hom.left ≫ pullback.fst X.hom (c.π.app i) =
          pullback.fst ((Over.pullback (D.map e)).obj X).hom (c.π.app j) ≫
            pullback.fst X.hom (D.map e) ∧
        β.hom.left ≫ pullback.fst Y.hom (c.π.app i) =
          pullback.fst ((Over.pullback (D.map e)).obj Y).hom (c.π.app j) ≫
            pullback.fst Y.hom (D.map e) ∧
        α.hom ≫ f = (Over.pullback (c.π.app j)).map g ≫ β.hom
```

**`AlgebraicGeometry.eventually_eq_of_baseChange_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Relative.lean, line 329](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/DescendingMorphisms/Relative.lean#L329). The attribute's comment: “part (3)”.

> Two morphisms at one stage which become equal after base change to the
> inverse limit are equal after passing to a later stage.

```lean
theorem eventually_eq_of_baseChange_eq
    {I : Type v} [Category.{w} I] [IsCofiltered I] [EssentiallySmall.{u} I]
    (D : I ⥤ Scheme.{u}) (c : Cone D) (hc : IsLimit c)
    [∀ {i j : I} (e : i ⟶ j), IsAffineHom (D.map e)]
    [∀ i : I, CompactSpace (D.obj i)]
    [∀ i : I, QuasiSeparatedSpace (D.obj i)]
    (i : I) (X Y : Over (D.obj i))
    (hX : FinitePresentation X.hom) (hY : FinitePresentation Y.hom) (f g : X ⟶ Y)
    (hfg : (Over.pullback (c.π.app i)).map f = (Over.pullback (c.π.app i)).map g) :
    ∃ (j : I) (e : j ⟶ i),
      (Over.pullback (D.map e)).map f = (Over.pullback (D.map e)).map g
```

**`AlgebraicGeometry.Scheme.eventually_eq_of_baseChange_eq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/FinitePresentationDescent.lean, line 346](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/FinitePresentationDescent.lean#L346). The attribute's comment: “part (3)”. References: EGA IV (8.13.1), “special case, uniqueness”; SGA 3 VIB (10.0), “(i) injectivity”; SGA 4 VII (5.2), “(a) injectivity”; SGA 4 VII (5.3), “faithfulness”.

> **Stacks Project, Tag 01ZM, part (3).** Two morphisms between schemes of finite presentation
> at one stage of a cofiltered inverse system of quasi-compact and quasi-separated schemes with
> affine transition morphisms, which become equal after base change to the limit, are equal after
> passing to a later stage.

```lean
theorem eventually_eq_of_baseChange_eq
    [IsCofiltered I] [EssentiallySmall.{u} I]
    (D : I ⥤ Scheme.{u}) (c : Cone D) (hc : IsLimit c)
    [∀ {i j : I} (e : i ⟶ j), IsAffineHom (D.map e)]
    [∀ i : I, CompactSpace (D.obj i)]
    [∀ i : I, QuasiSeparatedSpace (D.obj i)]
    (i : I) (X Y : Over (D.obj i))
    (hX : FinitePresentation X.hom) (hY : FinitePresentation Y.hom) (f g : X ⟶ Y)
    (hfg : (Over.pullback (c.π.app i)).map f = (Over.pullback (c.π.app i)).map g) :
    ∃ (j : I) (e : j ⟶ i),
      (Over.pullback (D.map e)).map f = (Over.pullback (D.map e)).map g
```

**`AlgebraicGeometry.LimitFPObjectDescent.exists_model_of_finitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ObjectDescent/Basic.lean, line 367](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ObjectDescent/Basic.lean#L367). The attribute's comment: “part (1)”. References: SGA 3 VIB (10.0), “(ii)”; SGA 4 VII (5.2), “(b)”; SGA 4 VII (5.3), “essential surjectivity”.

> **Stacks Project, Tag 01ZM, part (1).** A scheme of finite presentation over the limit of a
> cofiltered system of quasi-compact and quasi-separated schemes with affine transition morphisms is
> obtained by base change from some stage.

```lean
theorem exists_model_of_finitePresentation {I : Type v} [Category.{w} I] [IsCofiltered I]
    [EssentiallySmall.{u} I] (D : I ⥤ Scheme.{u}) (c : Cone D) (hc : IsLimit c)
    [∀ {i j : I} (f : i ⟶ j), IsAffineHom (D.map f)] [∀ i : I, CompactSpace (D.obj i)]
    [∀ i : I, QuasiSeparatedSpace (D.obj i)] (X : Over c.pt) (hX : FinitePresentation X.hom) :
    ∃ (i : I) (Xᵢ : Over (D.obj i)),
      FinitePresentation Xᵢ.hom ∧ Nonempty (X ≅ (Over.pullback (c.π.app i)).obj Xᵢ)
```

## Tag 01ZR, a lemma

[Tag 01ZR](https://stacks.math.columbia.edu/tag/01ZR) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ModuleLimits.exists_pullback_map_eq_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ModuleLimits/EventualMapEq.lean, line 178](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ModuleLimits/EventualMapEq.lean#L178). The attribute's comment: “eventual_equality”.

> Let `c` be a limit cone on a cofiltered diagram `D` of
> schemes with affine transition morphisms and let `ψ₁, ψ₂ : F ⟶ G` be morphisms of sheaves of
> modules of finite presentation on a quasi-compact stage `D.obj i`.  If the pullbacks of `ψ₁` and
> `ψ₂` to `c.pt` agree, then their pullbacks to `D.obj j` agree for some `j` over `i`.

```lean
theorem exists_pullback_map_eq_of_isLimit (hc : IsLimit c) (i : I) [CompactSpace (D.obj i)]
    (F G : (D.obj i).Modules) [F.IsFinitePresentation] [G.IsFinitePresentation]
    (ψ₁ ψ₂ : F ⟶ G)
    (h : (Scheme.Modules.pullback (c.π.app i)).map ψ₁ =
      (Scheme.Modules.pullback (c.π.app i)).map ψ₂) :
    ∃ (j : I) (e : j ⟶ i),
      (Scheme.Modules.pullback (D.map e)).map ψ₁ =
        (Scheme.Modules.pullback (D.map e)).map ψ₂
```

**`Stacks.AlgebraicGeometry.ModuleLimits.exists_map_of_pullback_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ModuleLimits/MorphismDescentGlue.lean, line 503](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ModuleLimits/MorphismDescentGlue.lean#L503). The attribute's comment: “descend_morphisms”.

> **[Stacks Project, Tag 01ZR] (2), with the canonical identifications written out.**  This is
> the statement of the clause of the tag verbatim, obtained from
> `exists_map_of_pullback_canonical_of_isLimit'` by unfolding the canonical identification.

```lean
theorem exists_map_of_pullback_of_isLimit (hc : IsLimit c) (i : I)
    [CompactSpace (D.obj i)] [QuasiSeparatedSpace (D.obj i)]
    (F G : (D.obj i).Modules) [F.IsFinitePresentation] [G.IsFinitePresentation]
    (φ : (Scheme.Modules.pullback (c.π.app i)).obj F ⟶
      (Scheme.Modules.pullback (c.π.app i)).obj G) :
    ∃ (j : I) (e : j ⟶ i)
      (φj : (Scheme.Modules.pullback (D.map e)).obj F ⟶
        (Scheme.Modules.pullback (D.map e)).obj G),
      (Scheme.Modules.pullback (c.π.app j)).map φj ≫
          (Scheme.Modules.pullbackComp (c.π.app j) (D.map e)).hom.app G ≫
            (Scheme.Modules.pullbackCongr (c.w e)).hom.app G =
        (Scheme.Modules.pullbackComp (c.π.app j) (D.map e)).hom.app F ≫
          (Scheme.Modules.pullbackCongr (c.w e)).hom.app F ≫ φ
```

**`Stacks.AlgebraicGeometry.ModuleLimits.exists_isFinitePresentation_pullback_iso_of_qcqs`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ModuleLimits/MorphismDescentGlue.lean, line 528](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ModuleLimits/MorphismDescentGlue.lean#L528). The attribute's comment: “descend_modules”.

> **[Stacks Project, Tag 01ZR] (1) for a cofiltered limit of quasi-compact quasi-separated
> schemes with affine transition morphisms.**  A sheaf of modules of finite presentation on the
> limit is the pullback of one on a stage.  This is
> `Stacks.AlgebraicGeometry.ModuleLimits.exists_isFinitePresentation_pullback_iso_of_map` with its
> hypothesis `hmap` discharged by `exists_map_of_pullback_of_isLimit`, and it is the statement
> [Stacks Project, Tag 0ASY] calls.

```lean
theorem exists_isFinitePresentation_pullback_iso_of_qcqs (hc : IsLimit c)
    [∀ j : I, CompactSpace (D.obj j)] [∀ j : I, QuasiSeparatedSpace (D.obj j)]
    (F : c.pt.Modules) [F.IsFinitePresentation] :
    ∃ (i : I) (Fᵢ : (D.obj i).Modules),
      Fᵢ.IsFinitePresentation ∧
        Nonempty (F ≅ (Scheme.Modules.pullback (c.π.app i)).obj Fᵢ)
```

## Tag 0B8W, a lemma

[Tag 0B8W](https://stacks.math.columbia.edu/tag/0B8W) in the Stacks Project.

**`Stacks.AlgebraicGeometry.ModuleLimits.exists_isFiniteLocallyFree_pullback_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ModuleLimits/FiniteLocallyFreeUnconditional.lean, line 216](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ModuleLimits/FiniteLocallyFreeUnconditional.lean#L216). The attribute's comment: “(1)”.

> **Stacks Project, Tag 0B8W (1).**  Let `S = lim Sᵢ` be the limit of a cofiltered system of
> quasi-compact quasi-separated schemes with affine transition morphisms.  Then every finite
> locally free `𝒪_S`-module is the pullback of a finite locally free `𝒪_{Sᵢ}`-module for some
> `i`.
>
> This is `exists_isFiniteLocallyFree_pullback_iso_of_eventually` with its remaining
> hypothesis — the conjunction of Algebra, Lemmas 02JO and 00NX in the form the source's proof
> uses them — supplied by `exists_isFiniteLocallyFree_pullback_of_isLimit_qcqs'`.

```lean
theorem exists_isFiniteLocallyFree_pullback_iso (hc : IsLimit c)
    [∀ i : I, CompactSpace (D.obj i)] [∀ i : I, QuasiSeparatedSpace (D.obj i)]
    (E : c.pt.Modules) (hE : SheafOfModules.IsFiniteLocallyFree.{u, u, u} E) :
    ∃ (i : I) (Eᵢ : (D.obj i).Modules),
      SheafOfModules.IsFiniteLocallyFree.{u, u, u} Eᵢ ∧
        Nonempty (E ≅ (Scheme.Modules.pullback (c.π.app i)).obj Eᵢ)
```

**`Stacks.AlgebraicGeometry.ModuleLimits.exists_ideal_pullback_epi_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ModuleLimits/FiniteTypeIdealDescent.lean, line 332](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ModuleLimits/FiniteTypeIdealDescent.lean#L332). The attribute's comment: “finite_type_ideal_descent”.

> **Stacks Project, Tag 0B8W.**  A finite type quasi-coherent ideal of the structure sheaf of
> the limit of a cofiltered system of quasi-compact and quasi-separated schemes with affine
> transition morphisms is the image of the pullback of such an ideal at some stage.
>
> An ideal is given as a quasi-coherent module `I` of finite type together with a monomorphism
> `inclusion : I ⟶ 𝒪`.  The epimorphism `descend` of the conclusion is compatible with the two
> inclusions; it need not be invertible, because the pullback of a monomorphism of modules need not
> be one.

```lean
theorem exists_ideal_pullback_epi_of_isLimit (hc : IsLimit c) (I : c.pt.Modules)
    [I.IsQuasicoherent] [I.IsFiniteType]
    (inclusion : I ⟶ SheafOfModules.unit c.pt.ringCatSheaf) [Mono inclusion] :
    ∃ i : J,
      letI : (SheafOfModules.pushforward
        (c.π.app i).toRingCatSheafHom).IsRightAdjoint :=
        Scheme.Modules.instIsRightAdjointPushforward (c.π.app i)
      ∃ Iᵢ : (D.obj i).Modules,
        Iᵢ.IsQuasicoherent ∧ Iᵢ.IsFiniteType ∧
          ∃ inclusionᵢ : Iᵢ ⟶ SheafOfModules.unit (D.obj i).ringCatSheaf,
            Mono inclusionᵢ ∧
              ∃ descend : (Scheme.Modules.pullback (c.π.app i)).obj Iᵢ ⟶ I,
                Epi descend ∧
                  descend ≫ inclusion =
                    (Scheme.Modules.pullback (c.π.app i)).map inclusionᵢ ≫
                      SheafOfModules.pullbackObjUnitToUnit
                        (c.π.app i).toRingCatSheafHom
```

**`Stacks.AlgebraicGeometry.ModuleLimits.exists_isInvertible_pullback_iso_of_isLimit`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ModuleLimits/InvertibleUnconditional.lean, line 191](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ModuleLimits/InvertibleUnconditional.lean#L191). The attribute's comment: “(2)”.

> **Stacks Project, Tag 0B8W (2).**  Let `S = lim Sᵢ` be the limit of a cofiltered system of
> quasi-compact quasi-separated schemes with affine transition morphisms.  Then every invertible
> `𝒪_S`-module is the pullback of an invertible `𝒪_{Sᵢ}`-module for some `i`.
>
> This is `exists_isInvertible_pullback_iso_of_isLimit_of_descent` with its two hypotheses
> discharged: `hDescend` by Tag 01ZR (1), `hFullyFaithful` by `exists_iso_pullback_of_isLimit`,
> which rests on Tag 01ZR (2) and (3).

```lean
theorem exists_isInvertible_pullback_iso_of_isLimit
    [∀ i : I, CompactSpace (D.obj i)] [∀ i : I, QuasiSeparatedSpace (D.obj i)]
    (hc : IsLimit c)
    (L : c.pt.Modules)
    (hL : IsInvertible c.pt.sheaf.obj c.pt.ringCatSheaf.property L) :
    ∃ (i : I) (Lᵢ : (D.obj i).Modules),
      IsInvertible (D.obj i).sheaf.obj (D.obj i).ringCatSheaf.property Lᵢ ∧
        Nonempty (L ≅ (Scheme.Modules.pullback (c.π.app i)).obj Lᵢ)
```

## Tag 05LY, a lemma

[Tag 05LY](https://stacks.math.columbia.edu/tag/05LY) in the Stacks Project.

**`AlgebraicGeometry.eventually_isFlatOver_modulePullback`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Limits/RelativeApproximation/FlatDescent.lean, line 903](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Limits/RelativeApproximation/FlatDescent.lean#L903). References: EGA IV (11.2.6), “(ii)”.

> If a finitely presented quasi-coherent module at one stage of a cofiltered
> inverse system becomes flat over the base-changed target at the limit, it is
> flat over that target after passing to some later stage.

```lean
theorem eventually_isFlatOver_modulePullback
    {I : Type v} [Category.{w} I] [IsCofiltered I] [EssentiallySmall.{u} I]
    (D : I ⥤ Scheme.{u}) (c : Cone D) (hc : IsLimit c)
    [∀ {i j : I} (e : i ⟶ j), IsAffineHom (D.map e)]
    [∀ i : I, CompactSpace (D.obj i)]
    [∀ i : I, QuasiSeparatedSpace (D.obj i)]
    (i : I) (X Y : Over (D.obj i))
    (hX : FinitePresentation X.hom) (hY : FinitePresentation Y.hom)
    (f : X ⟶ Y)
    (F : SheafOfModules.{u} (structureSheafRing X.left.toRingedSpace))
    [F.IsQuasicoherent] [F.IsFinitePresentation]
    (hflat : IsFlatOver
      ((Over.pullback (c.π.app i)).map f).left.toLRSHom.toShHom
      ((modulePullback
        (pullback.fst X.hom (c.π.app i)).toLRSHom.toShHom).obj F)) :
    ∃ (j : I) (e : j ⟶ i), IsFlatOver
      ((Over.pullback (D.map e)).map f).left.toLRSHom.toShHom
      ((modulePullback
        (pullback.fst X.hom (D.map e)).toLRSHom.toShHom).obj F)
```

## Tag 0EY1, a lemma

[Tag 0EY1](https://stacks.math.columbia.edu/tag/0EY1) in the Stacks Project.

**`AlgebraicGeometry.LimitDescent.exists_model_of_locallyOfFinitePresentation`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LimitDescentGlueing/GeneralStages.lean, line 351](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LimitDescentGlueing/GeneralStages.lean#L351). The attribute's comment: “essential surjectivity, arbitrary stages”. References: EGA IV (8.1.1), “more general”; EGA IV (8.8.2), “more general”; EGA IV (8.8.3), “essential surjectivity”; SGA 4 VII (5.3), “essential surjectivity”; SGA 3 VIB (10.0), “more general”; SGA 4 VII (5.2), “more general”.

> **Essential surjectivity in Stacks Tag 0EY1, at the generality the source states.**
>
> Let `S = lim Sᵢ` be a directed inverse limit of schemes with affine transition morphisms — **no
> finiteness hypothesis whatsoever is made on the stages `Sᵢ`** — and let `X` be a quasi-compact,
> quasi-separated scheme locally of finite presentation over `S`.  Then `X` is isomorphic, over `S`,
> to the base change of a quasi-compact, quasi-separated scheme locally of finite presentation over
> one of the stages `Sᵢ`.
>
> This is `AlgebraicGeometry.LimitDescent.exists_model_of_finitePresentation` with the stage
> hypotheses `CompactSpace (D.obj i)` and `QuasiSeparatedSpace (D.obj i)` removed, so that that
> result is the special case of this one in which the stages are quasi-compact and quasi-separated;
> over such a stage the conclusion is `AlgebraicGeometry.FinitePresentation` of the model, by
> `AlgebraicGeometry.finitePresentation_of_compactSpace`.  The source assumes nothing about the
> stages, which is why the statement is in terms of a quasi-compact, quasi-separated source and a
> morphism locally of finite presentation rather than in terms of finite presentation.
>
> The index hypothesis `CategoryTheory.FinallySmall.{u} I` asks that `I` have a `u`-small cofinal
> set of objects; it is automatic for the directed *set* of the source, and is needed because the
> comparison of the sections of the limit with the sections at the stages is a statement about an
> index category at the scheme universe.

```lean
public theorem exists_model_of_locallyOfFinitePresentation
    {I : Type v} [Preorder I] [Nonempty I] [IsDirected I (· ≤ ·)] [FinallySmall.{u} I]
    (D : Iᵒᵖ ⥤ Scheme.{u}) [∀ {i j : Iᵒᵖ} (a : i ⟶ j), IsAffineHom (D.map a)]
    (c : Cone D) (hc : IsLimit c) (X : Over c.pt)
    (hXqc : CompactSpace X.left) (hXqs : QuasiSeparatedSpace X.left)
    (hX : LocallyOfFinitePresentation X.hom) :
    ∃ (i : I) (Xᵢ : Over (D.obj (.op i))),
      CompactSpace Xᵢ.left ∧ QuasiSeparatedSpace Xᵢ.left ∧
        LocallyOfFinitePresentation Xᵢ.hom ∧
        Nonempty (X ≅ (Over.pullback (c.π.app (.op i))).obj Xᵢ)
```

**`AlgebraicGeometry.LimitDescent.isEquivalence_baseChangeComparison`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LimitDescentGlueing/GeneralStagesEquivalence.lean, line 925](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LimitDescentGlueing/GeneralStagesEquivalence.lean#L925). References: EGA IV (8.1.1), “more general”; EGA IV (8.8.3), “more general”; SGA 3 VIB (10.0), “more general”; SGA 4 VII (5.2), “more general”; SGA 4 VII (5.3), “more general”.

> For a scheme `T` let `C_T` be the full subcategory of schemes `W` over `T` such that `W` is
> quasi-compact and quasi-separated and such that the structure morphism `W ⟶ T` is locally of
> finite presentation. Let `S = lim Sᵢ` be a directed inverse limit of schemes with affine
> transition morphisms, indexed by a finally `u`-small `I`, with no finiteness hypothesis on the
> stages `Sᵢ`. Then the base change functors induce an equivalence of categories
> `colim C_{Sᵢ} ⥤ C_S`.
>
> The colimit is the colimit in `CategoryTheory.Cat` of the strict model
> `AlgebraicGeometry.LimitDescent.stageDiagram` of the diagram `i ↦ C_{Sᵢ}`, and the functor is
> `AlgebraicGeometry.LimitDescent.baseChangeComparison`, the colimit descent of the base change
> functors `C_{Sᵢ} ⥤ C_S`.

```lean
public theorem isEquivalence_baseChangeComparison :
    (baseChangeComparison D c hc).IsEquivalence
```

**`AlgebraicGeometry.LimitDescent.isEquivalence_baseChangeComparison_of_directedSet`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/LimitDescentGlueing/GeneralStagesEquivalence.lean, line 946](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/LimitDescentGlueing/GeneralStagesEquivalence.lean#L946). References: EGA IV (8.8.3), “more general”; SGA 3 VIB (10.0), “more general”; SGA 4 VII (5.3), “more general”.

> Let `S = lim Sᵢ` be the limit of an inverse system of schemes indexed by a directed set `I`
> in the universe of the schemes, with affine transition morphisms. Then the base change functors
> induce an equivalence of categories `colim C_{Sᵢ} ⥤ C_S`, where `C_T` is the category of
> quasi-compact, quasi-separated schemes locally of finite presentation over `T`.

```lean
public theorem isEquivalence_baseChangeComparison_of_directedSet
    {I : Type u} [Preorder I] [Nonempty I] [IsDirected I (· ≤ ·)]
    (D : Iᵒᵖ ⥤ Scheme.{u}) [∀ {a b : Iᵒᵖ} (t : a ⟶ b), IsAffineHom (D.map t)]
    (c : Cone D) (hc : IsLimit c) :
    (baseChangeComparison D c hc).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 32.10, Tag 01ZL](https://stacks.math.columbia.edu/tag/01ZL)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
