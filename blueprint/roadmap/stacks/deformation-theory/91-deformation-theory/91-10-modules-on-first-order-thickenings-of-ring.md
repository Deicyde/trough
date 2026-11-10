---
declaration: section
origin: cited
lean: Deformation.ToposThickening.extensionActionMap, CategoryTheory.Abelian.YonedaExtension, Deformation.ToposThickening.compatibleMap_add_quotientKernel, Deformation.ToposThickening.compatibleMap_unique_quotientKernel_difference, idealActionMap_naturality, Deformation.ToposThickening.obstructionClass, Deformation.ToposThickening.obstructionClass_eq_zero_iff, Deformation.ToposThickening.fixedActionExtensionClass_torsor
statement: formalized
proof: formalized
---

# 91.10 Modules on first order thickenings of ringed topoi

Section 91.10 of the Stacks Project, [Tag 08MA](https://stacks.math.columbia.edu/tag/08MA). 12 tags here are carried by 35 declarations of the repository (all in StacksFrontier) and 2 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08MB, an equation

[Tag 08MB](https://stacks.math.columbia.edu/tag/08MB) in the Stacks Project.

**`Deformation.ToposThickening.extensionActionMap`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/Basic.lean, line 1391](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/Basic.lean#L1391). The attribute's comment: “canonical action map”.

> The canonical map `I ⊗[O] F → K`, characterized by multiplication by an
> ideal section after lifting a section of `F` to the middle module.

```lean
public noncomputable def extensionActionMap
    [X.J.HasSheafCompose (forget RingCat.{w})]
    [Y.J.HasSheafCompose (forget RingCat.{w'})]
    [X.J.HasSheafCompose (forget₂ CommRingCat.{w} RingCat.{w})]
    [Y.J.HasSheafCompose (forget₂ CommRingCat.{w'} RingCat.{w'})]
    {i : RingedToposHom X Y}
    [Y.J.WEqualsLocallyBijective AddCommGrpCat.{w'}]
    [HasSheafify Y.J AddCommGrpCat.{w'}]
    [HasWeakSheafify Y.J AddCommGrpCat.{w'}]
    (hi : FirstOrderThickening i)
    {F K : SheafOfModules.{w'}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor i.toToposHom).obj X.O))}
    (E : Abelian.YonedaExtension
      ((SheafOfModules.restrictScalars
        (show Stacks.SheafOfModules.Tensor.ringSheaf Y.O ⟶
            Stacks.SheafOfModules.Tensor.ringSheaf
              ((pushforwardCommRingFunctor i.toToposHom).obj X.O) from
          (sheafCompose Y.J (forget₂ CommRingCat RingCat)).map i.fSharp)).obj F)
      ((SheafOfModules.restrictScalars
        (show Stacks.SheafOfModules.Tensor.ringSheaf Y.O ⟶
            Stacks.SheafOfModules.Tensor.ringSheaf
              ((pushforwardCommRingFunctor i.toToposHom).obj X.O) from
          (sheafCompose Y.J (forget₂ CommRingCat RingCat)).map i.fSharp)).obj K) 0) :
    { c : ((Stacks.SheafOfModules.Tensor.sheafTensor
        ((pushforwardCommRingFunctor i.toToposHom).obj X.O)).obj hi.I).obj F ⟶ K //
      ∀ (U : Y.Cᵒᵖ) (a : hi.I.val.obj U) (x : E.Z.left.val.obj U),
        E.f.val.app U
            (c.val.app U
              (((PresheafOfModules.sheafificationAdjunction
                (R := Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor
                  i.toToposHom).obj X.O))
                (𝟙 (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor
                  i.toToposHom).obj X.O)).obj)).unit.app
                (PresheafOfModules.tensorObj hi.I.val F.val)).app U
                (a ⊗ₜ[((pushforwardCommRingFunctor i.toToposHom).obj X.O).obj.obj U]
                  E.g.val.app U x))) =
          (show (Stacks.SheafOfModules.Tensor.ringSheaf Y.O).obj.obj U from
            hi.incl.val.app U a) • x }
```

Declarations registered for the tag:

- [`CategoryTheory.Abelian.YonedaExtension`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Ext/Basic/ExtAndYonedaExtensions.lean#L82), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Deformation/ToposThickening/Basic.lean, line 1386](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/Basic.lean#L1386) (StacksFrontier).

## Tag 08MC, a lemma

[Tag 08MC](https://stacks.math.columbia.edu/tag/08MC) in the Stacks Project.

**`Deformation.ToposThickening.compatibleMap_add_quotientKernel`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CompatibleLifts.lean, line 89](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/CompatibleLifts.lean#L89). The attribute's comment: “compatible_lifts_torsor”.

> Adding a map which factors through the first quotient and the second kernel preserves
> compatibility.

```lean
theorem compatibleMap_add_quotientKernel
    (D : TwoExtensions i) (c : CompatibleMap D) (α : D.F ⟶ D.L) :
    ∃ d : CompatibleMap D,
      d.hom = c.hom +
        (D.firstExtension.g ≫
          (SheafOfModules.restrictScalars
            ((sheafCompose Y.J (forget₂ CommRingCat RingCat)).map i.fSharp)).map α ≫
          D.secondExtension.f)
```

**`Deformation.ToposThickening.compatibleMap_unique_quotientKernel_difference`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/CompatibleLifts.lean, line 111](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/CompatibleLifts.lean#L111). The attribute's comment: “compatible_lifts_torsor”.

> Any two compatible maps differ by a unique map from the first quotient to the second kernel.
> Together with closure under those translations, this is the torsor assertion.

```lean
theorem compatibleMap_unique_quotientKernel_difference
    (D : TwoExtensions i) (c d : CompatibleMap D) :
    ∃! α : D.F ⟶ D.L,
      d.hom = c.hom +
        (D.firstExtension.g ≫
      (SheafOfModules.restrictScalars
        ((sheafCompose Y.J (forget₂ CommRingCat RingCat)).map i.fSharp)).map α ≫
          D.secondExtension.f)
```

Declarations registered for the tag:

- [`idealActionMap_naturality`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=idealActionMap_naturality#doc) registered with `add_to_stacks` in [StacksFrontier/Deformation/ToposThickening/CompatibleLifts.lean, line 162](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/CompatibleLifts.lean#L162) (StacksFrontier): “ideal_action_compatible”.

## Tag 08MD, a lemma

[Tag 08MD](https://stacks.math.columbia.edu/tag/08MD) in the Stacks Project.

**`Deformation.ToposThickening.obstructionClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ExtensionObstruction.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ExtensionObstruction.lean#L270). The attribute's comment: “obstruction class”.

> The obstruction class in the first Ext group over the quotient structure sheaf. Its
> vanishing characterizes lifts of the prescribed end maps.

```lean
noncomputable def obstructionClass
    [HasExt.{e} (SheafOfModules.{w'}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor i.toToposHom).obj X.O)))]
    (D : TwoExtensions i) (h : CompatibleActions D) :
    Abelian.Ext D.F D.L 1
```

**`Deformation.ToposThickening.obstructionClass_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ExtensionObstruction.lean, line 280](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ExtensionObstruction.lean#L280). The attribute's comment: “vanishing criterion”.

> The obstruction vanishes exactly when the end maps extend to a map of the two
> extensions.

```lean
theorem obstructionClass_eq_zero_iff
    [HasExt.{e} (SheafOfModules.{w'}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor i.toToposHom).obj X.O)))]
    (D : TwoExtensions i) (h : CompatibleActions D) :
    obstructionClass D h = 0 ↔
      ∃ φ' : D.firstExtension.Z.left ⟶ D.secondExtension.Z.left,
        IsExtensionLift D φ'
```

## Tag 08ME, a lemma

[Tag 08ME](https://stacks.math.columbia.edu/tag/08ME) in the Stacks Project.

**`Deformation.ToposThickening.fixedActionExtensionClass_torsor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ModulesOnThickening/FixedAction/Torsor.lean, line 685](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ModulesOnThickening/FixedAction/Torsor.lean#L685).

> **Stacks 08ME.** If some extension over a first order thickening of ringed topoi induces the
> prescribed action `c` of the square-zero ideal, then the isomorphism classes of extensions
> inducing `c` form a principal homogeneous space under the first `Ext` group over the quotient
> structure sheaf.

```lean
theorem fixedActionExtensionClass_torsor
    [HasExt.{e} (SheafOfModules.{w'}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor i.toToposHom).obj X.O)))]
    [HasExt.{e} (SheafOfModules.{w'} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))]
    (hi : FirstOrderThickening i)
    (F K : SheafOfModules.{w'}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor i.toToposHom).obj X.O)))
    (c : ((Stacks.SheafOfModules.Tensor.sheafTensor
      ((pushforwardCommRingFunctor i.toToposHom).obj X.O)).obj hi.I).obj F ⟶ K)
    (h : Nonempty (FixedActionExtensionClass.{_, _, _, _, _, _, e} hi F K c)) :
    Nonempty (AddTorsor (Abelian.Ext F K 1)
      (FixedActionExtensionClass.{_, _, _, _, _, _, e} hi F K c))
```

**`Deformation.ToposThickening.exists_addTorsor_fixedActionExtensionIsoClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ModulesOnThickening/FixedActionIsoClasses.lean, line 170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ModulesOnThickening/FixedActionIsoClasses.lean#L170).

> **Stacks 08ME.** Let `i` be a first order thickening of ringed topoi, `F`, `K` modules over
> the quotient structure sheaf and `c : I ⊗ F ⟶ K` linear. If there is an extension
> `0 → K → F' → F → 0` of `O'`-modules with `c_{F'} = c`, then the set of isomorphism classes of
> these extensions is a principal homogeneous space under `Ext¹_O(F, K)`: there is a torsor
> structure in which `a` sends the class of `F'₁` to the class of `F'₂` exactly when the
> `Ext¹_{O'}` class of `F'₂` is the Baer sum of that of `F'₁` with the image of `a`.

```lean
theorem exists_addTorsor_fixedActionExtensionIsoClass
    [HasExt.{e} (SheafOfModules.{w'}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor i.toToposHom).obj X.O)))]
    [HasExt.{e} (SheafOfModules.{w'} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))]
    (hi : FirstOrderThickening i)
    (F K : SheafOfModules.{w'}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor i.toToposHom).obj X.O)))
    (c : ((Stacks.SheafOfModules.Tensor.sheafTensor
      ((pushforwardCommRingFunctor i.toToposHom).obj X.O)).obj hi.I).obj F ⟶ K)
    (h : Nonempty (FixedActionExtension hi F K c)) :
    ∃ T : AddTorsor (Abelian.Ext.{e} F K 1) (FixedActionExtensionIsoClass hi F K c),
      ∀ (a : Abelian.Ext.{e} F K 1) (E E' : FixedActionExtension hi F K c),
        (T.vadd a ⟦E⟧ = ⟦E'⟧) ↔
          extensionClass F K E'.1 =
            (SheafOfModules.restrictScalars (structureRingMap i)).mapExtAddHom F K 1 a +
              extensionClass F K E.1
```

## Tag 08MF, a lemma

[Tag 08MF](https://stacks.math.columbia.edu/tag/08MF) in the Stacks Project.

**`Deformation.ToposThickening.existenceObstructionClass`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ModulesOnThickening/FixedAction/ExistenceObstruction.lean, line 618](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ModulesOnThickening/FixedAction/ExistenceObstruction.lean#L618). The attribute's comment: “obstruction class”.

> **Stacks 08MF.** The obstruction to the existence of an extension over a first order
> thickening of ringed topoi inducing a prescribed action `c` of the square-zero ideal: a class in
> the second `Ext` group over the quotient structure sheaf.

```lean
noncomputable def existenceObstructionClass
    [HasExt.{e} (SheafOfModules.{w'}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor i.toToposHom).obj X.O)))]
    [HasExt.{e} (SheafOfModules.{w'} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))]
    (hi : FirstOrderThickening i)
    (F K : SheafOfModules.{w'}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor i.toToposHom).obj X.O)))
    (c : ((Stacks.SheafOfModules.Tensor.sheafTensor
      ((pushforwardCommRingFunctor i.toToposHom).obj X.O)).obj hi.I).obj F ⟶ K) :
    Abelian.Ext F K 2
```

**`Deformation.ToposThickening.existenceObstructionClass_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ModulesOnThickening/FixedAction/ExistenceObstruction.lean, line 636](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ModulesOnThickening/FixedAction/ExistenceObstruction.lean#L636). The attribute's comment: “vanishing criterion”.

> **Stacks 08MF.** The obstruction class vanishes exactly when there is an extension of `F` by
> `K` over the first order thickening whose canonical action of the square-zero ideal is `c`.

```lean
theorem existenceObstructionClass_eq_zero_iff
    [HasExt.{e} (SheafOfModules.{w'}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor i.toToposHom).obj X.O)))]
    [HasExt.{e} (SheafOfModules.{w'} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))]
    (hi : FirstOrderThickening i)
    (F K : SheafOfModules.{w'}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor i.toToposHom).obj X.O)))
    (c : ((Stacks.SheafOfModules.Tensor.sheafTensor
      ((pushforwardCommRingFunctor i.toToposHom).obj X.O)).obj hi.I).obj F ⟶ K) :
    existenceObstructionClass hi F K c = 0 ↔
      ∃ E : Abelian.YonedaExtension
        ((SheafOfModules.restrictScalars
          (structureRingMap i)).obj F)
        ((SheafOfModules.restrictScalars
          (structureRingMap i)).obj K) 0,
        (extensionActionMap hi E).1 = c
```

## Tag 08MG, a remark

[Tag 08MG](https://stacks.math.columbia.edu/tag/08MG) in the Stacks Project.

**`Deformation.ToposThickening.Trivialization`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/Trivialization/Basic.lean, line 68](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/Trivialization/Basic.lean#L68). The attribute's comment: “trivial_first_order_thickening_and_trivialization”.

> A retraction of a morphism of ringed topoi: a morphism in the reverse direction whose
> composite direct-image functor is identified with the identity, compatibly with the
> structure-sheaf map.

```lean
structure Trivialization (i : RingedToposHom X Y)
```

**`Deformation.ToposThickening.IsTrivial`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/Trivialization/Basic.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/Trivialization/Basic.lean#L87). The attribute's comment: “trivial_first_order_thickening_and_trivialization”.

> A morphism of ringed topoi is trivial if it admits a trivialization.

```lean
abbrev IsTrivial (i : RingedToposHom X Y) : Prop
```

**`Deformation.ToposThickening.TrivializedThickening.moduleEquivalence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/Trivialization/ModuleEquivalence.lean, line 532](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/Trivialization/ModuleEquivalence.lean#L532). The attribute's comment: “trivialized first order thickenings are the O-modules; morphisms of thickenings run in the algebraic direction (A_T ⟶ A_S of sheaves of rings, the opposite of the source's ringed-topos morphisms of Stacks 08MK), so the module side carries no ᵒᵖ; stated at a single universe (site C : Type u with Category.{u} C, sheaves valued in Type u), which is the source's own setting since the Stacks Project fixes one universe throughout”.

> **Stacks 08MG.** The category of trivialized first order thickenings of a ringed topos
> `(Sh(C), O)` is equivalent to the category of `O`-modules: a module goes to the square-zero
> extension `O ⊕ M`, and a trivialized thickening goes to its ideal.
>
> There is no `ᵒᵖ` on the module side because the Hom of
> `Deformation.ToposThickening.TrivializedThickening O` runs in the algebraic direction, a
> morphism `T ⟶ S` being a morphism `A_T ⟶ A_S` of sheaves of rings, so that this category is the
> opposite of the source's category of trivialized thickenings (whose morphisms are morphisms of
> ringed topoi, Stacks 08MK) and `M ↦ O ⊕ M` is covariant. The ringed space form of this remark,
> `AlgebraicGeometry.RingedSpaceThickening.trivializedThickeningEquivalence` (**Stacks 08L9**),
> keeps the geometric Hom and so *does* carry an `ᵒᵖ`; the two statements agree. See the
> "## Variance" section of this module.

```lean
noncomputable def moduleEquivalence :
    SheafOfModules.{u} (Stacks.SheafOfModules.Tensor.ringSheaf O) ≌ TrivializedThickening O
```

**`Deformation.ToposThickening.trivializationOfSplitting`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/Trivialization/OfSplitting.lean, line 59](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/Trivialization/OfSplitting.lean#L59). The attribute's comment: “splitting_determines_trivialization”.

> A splitting of the structure sheaf of a first order thickening determines a trivialization
> whose structure map is the given section.

```lean
noncomputable def trivializationOfSplitting (i : RingedToposHom X Y)
    (_hi : FirstOrderThickening i)
    (split : X.O ⟶ (inverseImageCommRingFunctor i.toToposHom).obj Y.O)
    (split_comp : split ≫ i.fSharpInverseImage = 𝟙 X.O) :
    { π : Trivialization i //
      ∃ α : pushforwardCommRingFunctor π.retraction.toToposHom ≅
          inverseImageCommRingFunctor i.toToposHom,
        π.retraction.fSharp ≫ α.hom.app Y.O = split }
```

**`Deformation.ToposThickening.splittingFromTrivialization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/Trivialization/SplittingOf.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/Trivialization/SplittingOf.lean#L55). The attribute's comment: “splitting_from_trivialization”.

> A trivialization splits the structure map of a first order thickening. The natural
> equivalence identifies the ring sheaf with the square-zero extension of its quotient by its
> kernel.

```lean
noncomputable def splittingFromTrivialization (i : RingedToposHom X Y)
    (hi : FirstOrderThickening i) (π : Trivialization i) :
    Σ' split : ((pushforwardCommRingFunctor i.toToposHom).obj X.O).obj ⟶ Y.O.obj,
      Σ' hs : SplitMono split,
        { _e : PresheafTrivialSquareZeroEquiv Y.O.obj
            ((pushforwardCommRingFunctor i.toToposHom).obj X.O).obj
            i.fSharp.hom split // hs.retraction = i.fSharp.hom }
```

**`Deformation.ToposThickening.TrivializedThickening`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/Trivialization/TrivializedCategory.lean, line 98](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/Trivialization/TrivializedCategory.lean#L98). The attribute's comment: “the category of trivialized first order thickenings: objects”.

> A trivialized first order thickening of the ringed topos `(Sh(C), O)`, presented on the
> site `C`: a sheaf of commutative rings `A` with a surjection onto `O` whose kernel has square
> zero, together with a chosen splitting of that surjection.

```lean
structure TrivializedThickening (O : Sheaf J CommRingCat.{u})
```

**`Deformation.ToposThickening.TrivializedThickening.Hom`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/Trivialization/TrivializedCategory.lean, line 131](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/Trivialization/TrivializedCategory.lean#L131). The attribute's comment: “the category of trivialized first order thickenings: morphisms, in the algebraic direction A_T ⟶ A_S (the opposite of the source's ringed-topos morphisms of Stacks 08MK)”.

> A morphism of trivialized first order thickenings: a morphism of the structure sheaves
> compatible with both the surjections and the trivializations.
>
> This runs in the algebraic direction, that of `h^♯`. The source's morphism of trivialized
> thickenings is a morphism of ringed topoi `h : (Sh(D₁), O'₁) ⟶ (Sh(D₂), O'₂)` over
> `(Sh(C), O)` (Stacks 08MK), so a `Hom T S` here is such an `h` with `T` the *target* of `h` and
> `S` its source, and this category is the opposite of the source's. See the "## Variance"
> section of this module.

```lean
structure Hom (T S : TrivializedThickening O)
```

**`Deformation.ToposThickening.trivializedThickeningOfTrivialization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/Trivialization/TrivializedComparison.lean, line 153](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/Trivialization/TrivializedComparison.lean#L153). The attribute's comment: “a trivialized thickening is an object of the category; the target ringed topos is at a single universe, forced by Deformation.ToposThickening.TrivializedThickening, whose category is declared over a site C : Type u with Category.{u} C and sheaves valued in Type u — the source's own setting, since the Stacks Project fixes one universe throughout”.

> A trivialization of a first order thickening of ringed topoi exhibits the thickening as an
> object of the category of trivialized first order thickenings of `(Sh(D), i_*O)`, which is the
> ringed topos `(Sh(C), O)` read through the equivalence of underlying topoi.

```lean
noncomputable def trivializedThickeningOfTrivialization (i : RingedToposHom X Y)
    (hi : FirstOrderThickening i) (π : Trivialization i) :
    TrivializedThickening ((pushforwardCommRingFunctor i.toToposHom).obj X.O)
```

**`Deformation.ToposThickening.TrivializedThickening.exists_thickening_trivialization_iso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/Trivialization/TrivializedComparison.lean, line 638](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/Trivialization/TrivializedComparison.lean#L638). The attribute's comment: “clause (4) for the source's objects: every object of the category of trivialized first order thickenings of (Sh(C), O) is the trivialized thickening of a first order thickening of ringed topoi (Sh(C), O) ⟶ (Sh(C), A) with a trivialization of it, up to the isomorphism of objects supplied here and the equivalence of categories Deformation.ToposThickening.TrivializedThickening.baseIsoEquivalence that reads the base through the comparison of the direct image along the identity morphism of topoi with the identity functor; together with Deformation.ToposThickening.trivializedThickeningOfTrivialization in the other direction this identifies the objects of the two presentations, which is what makes Deformation.ToposThickening.TrivializedThickening.moduleEquivalence the source's sentence about the source's objects; the thickening is presented on the site of the base, which loses nothing because the direct image of a first order thickening is an equivalence of topoi, and at a single universe, the Stacks Project's own convention”.

> **Stacks 08MG, clause (4), for the source's objects.** Every object of the category of
> trivialized first order thickenings of `(Sh(C), O)` is, up to isomorphism, the trivialized
> thickening of a first order thickening of ringed topoi `(Sh(C), O) ⟶ (Sh(C), A)` together with
> a trivialization of it. With
> `Deformation.ToposThickening.trivializedThickeningOfTrivialization` in the other direction this
> identifies the objects of the two presentations, so that
> `Deformation.ToposThickening.TrivializedThickening.moduleEquivalence` reads as the source's
> sentence about the source's objects: the category of trivialized first order thickenings of
> `(Sh(C), O)` is equivalent to the category of `O`-modules.

```lean
theorem exists_thickening_trivialization_iso :
    ∃ (hi : FirstOrderThickening T.toRingedToposHom) (π : Trivialization T.toRingedToposHom),
      Nonempty (trivializedThickeningOfTrivialization T.toRingedToposHom hi π ≅
        (baseIsoFunctor (pushforwardIdIso O).symm).obj T)
```

## Tag 08MI, a remark

[Tag 08MI](https://stacks.math.columbia.edu/tag/08MI) in the Stacks Project.

**`Deformation.ToposThickening.trivialExtension_bijective_underlyingExtensionClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/TrivialExtension.lean, line 887](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/TrivialExtension.lean#L887).

> **Stacks 08MI.** Let `i : (Sh(C), O) ⟶ (Sh(D), O')` be a first order thickening of ringed
> topoi with square-zero ideal `I`, and `π` a trivialization of it. Let `F`, `K` be `O`-modules and
> `c : I ⊗_O F ⟶ K` a map.
>
> * The trivial extension `F'_{c,triv} = F ⊕ K` (`trivialExtensionModule`, `trivialExtension`)
>   carries the `O'`-module structure `r · (m, k) = (q r · m, q r · k + c(d r ⊗ m))` built from
>   the splitting `O' = O ⊕ I` of `π` and from `c`, and it is an extension
>   `0 ⟶ K ⟶ F'_{c,triv} ⟶ F ⟶ 0` as in Stacks 08MB with `c_{F'_{c,triv}} = c`.
> * The class `ξ_{F'} ∈ Ext¹_O(F, K)` of an extension `F'`, obtained by reading `F'` as an
>   `O`-module through `π^♯` (`underlyingExtensionClass`), only depends on the class of `F'`
>   (through `splitRestrictionExtHom`), and `F' ↦ ξ_{F'}` is a bijection from the isomorphism
>   classes of extensions with `c_{F'} = c` onto `Ext¹_O(F, K)`. The isomorphism classes are
>   represented by their classes in `Ext¹_{O'}(F, K)` (`FixedActionExtensionClass`); the bijection is
>   also stated on extensions: every class is `ξ_{F'}` of an extension with `c_{F'} = c`, and two
>   such extensions with the same `ξ` are isomorphic as extensions.
> * The trivial extension maps to the zero class.

```lean
theorem trivialExtension_bijective_underlyingExtensionClass
    (c : ((Stacks.SheafOfModules.Tensor.sheafTensor
      ((pushforwardCommRingFunctor i.toToposHom).obj X.O)).obj hi.I).obj F ⟶ K) :
    (∀ (U : Y.Cᵒᵖ) (r : (Stacks.SheafOfModules.Tensor.ringSheaf Y.O).obj.obj U)
        (z : (trivialExtensionModule hi π F K c).val.obj U),
        r • z = (structureApp i U r • z.1, structureApp i U r • z.2 +
          extensionPairing hi F K c U (trivializationDerivation hi π U r) z.1)) ∧
      (extensionActionMap hi (trivialExtension hi π F K c)).1 = c ∧
      (∀ E : Abelian.YonedaExtension
          ((SheafOfModules.restrictScalars
            (show Stacks.SheafOfModules.Tensor.ringSheaf Y.O ⟶
      Stacks.SheafOfModules.Tensor.ringSheaf
        ((pushforwardCommRingFunctor i.toToposHom).obj X.O) from
    (sheafCompose Y.J (forget₂ CommRingCat RingCat)).map i.fSharp)).obj F)
          ((SheafOfModules.restrictScalars
            (show Stacks.SheafOfModules.Tensor.ringSheaf Y.O ⟶
      Stacks.SheafOfModules.Tensor.ringSheaf
        ((pushforwardCommRingFunctor i.toToposHom).obj X.O) from
    (sheafCompose Y.J (forget₂ CommRingCat RingCat)).map i.fSharp)).obj K) 0,
        underlyingExtensionClass i hi π F K E =
          splitRestrictionExtHom hi π F K (extensionClass F K E)) ∧
      Function.Bijective (fun ξ : FixedActionExtensionClass.{_, _, _, _, _, _, e} hi F K c =>
        splitRestrictionExtHom hi π F K ξ.1) ∧
      (∀ η : Abelian.Ext F K 1, ∃ E : Abelian.YonedaExtension
          ((SheafOfModules.restrictScalars
            (show Stacks.SheafOfModules.Tensor.ringSheaf Y.O ⟶
      Stacks.SheafOfModules.Tensor.ringSheaf
        ((pushforwardCommRingFunctor i.toToposHom).obj X.O) from
    (sheafCompose Y.J (forget₂ CommRingCat RingCat)).map i.fSharp)).obj F)
          ((SheafOfModules.restrictScalars
            (show Stacks.SheafOfModules.Tensor.ringSheaf Y.O ⟶
      Stacks.SheafOfModules.Tensor.ringSheaf
        ((pushforwardCommRingFunctor i.toToposHom).obj X.O) from
    (sheafCompose Y.J (forget₂ CommRingCat RingCat)).map i.fSharp)).obj K) 0,
        (extensionActionMap hi E).1 = c ∧ underlyingExtensionClass i hi π F K E = η) ∧
      (∀ E E' : Abelian.YonedaExtension
          ((SheafOfModules.restrictScalars
            (show Stacks.SheafOfModules.Tensor.ringSheaf Y.O ⟶
      Stacks.SheafOfModules.Tensor.ringSheaf
        ((pushforwardCommRingFunctor i.toToposHom).obj X.O) from
    (sheafCompose Y.J (forget₂ CommRingCat RingCat)).map i.fSharp)).obj F)
          ((SheafOfModules.restrictScalars
            (show Stacks.SheafOfModules.Tensor.ringSheaf Y.O ⟶
      Stacks.SheafOfModules.Tensor.ringSheaf
        ((pushforwardCommRingFunctor i.toToposHom).obj X.O) from
    (sheafCompose Y.J (forget₂ CommRingCat RingCat)).map i.fSharp)).obj K) 0,
        (extensionActionMap hi E).1 = c → (extensionActionMap hi E').1 = c →
        underlyingExtensionClass i hi π F K E = underlyingExtensionClass i hi π F K E' →
        ∃ φ : E.Z.left ≅ E'.Z.left, E.f ≫ φ.hom = E'.f ∧ φ.hom ≫ E'.g = E.g) ∧
      underlyingExtensionClass i hi π F K (trivialExtension hi π F K c) = 0
```

## Tag 08MJ, a remark

[Tag 08MJ](https://stacks.math.columbia.edu/tag/08MJ) in the Stacks Project.

**`Deformation.ToposThickening.MorphismOfFirstOrderThickenings.PushoutExtensionData.extensionOne`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ExtensionPushout/TwistedDescent.lean, line 425](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ExtensionPushout/TwistedDescent.lean#L425). The attribute's comment: “the canonical map on extensions, by pushout along the map of kernel modules”.

> **Stacks Project, Tag 08MJ.** The extension over the first thickening produced from an
> extension over the second: the pushout `F'₂ ⊔_{K₂} K₁` carries an `O'₁`-module structure, built
> by descending the action of `T = O'₂ ⋉ I₁` twisted by `c₁` along the locally surjective
> `q : T ⟶ O'₁`, and sits in a short exact sequence `0 → K₁ → F'₂ ⊔_{K₂} K₁ → F → 0` of
> `O'₁`-modules. Its middle term restricted along `q` is identified with the pushout by
> `middleIso`, compatibly with the two maps by `restrictScalars_extInclOne` and
> `restrictScalars_extQuotOne`.

```lean
noncomputable def extensionOne :
    Abelian.YonedaExtension
      ((SheafOfModules.restrictScalars (structureRingMap i)).obj dat.F)
      ((SheafOfModules.restrictScalars (structureRingMap i)).obj dat.K₁) 0
```

**`Deformation.ToposThickening.MorphismOfFirstOrderThickenings.PushoutExtensionData.extensionOne_actionMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ExtensionPushout/TwistedDescent.lean, line 506](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ExtensionPushout/TwistedDescent.lean#L506). The attribute's comment: “the action map of the pushed-out extension is c₁”.

> **Stacks Project, Tag 08MJ.** The canonical action map of the extension produced over the
> first thickening is the prescribed `c₁`.

```lean
theorem extensionOne_actionMap :
    (extensionActionMap D.first (dat.extensionOne E₂ hE₂)).1 = dat.c₁
```

## Tag 08MK, a remark

[Tag 08MK](https://stacks.math.columbia.edu/tag/08MK) in the Stacks Project.

**`Deformation.ToposThickening.underlyingExtensionClass_eq_comp_mk₀`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/TrivializedThickeningComparison.lean, line 266](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/TrivializedThickeningComparison.lean#L266). The attribute's comment: “the commutative square: the extension class of the image extension is the image of the extension class under functoriality of `Ext` in the map of kernel modules”.

> If `h` is a morphism of trivialized first order thickenings of `(Sh(C), O)` and an extension
> `F'₂` of `F` by `K₂` over the second thickening maps to an extension `F'₁` of `F` by `K₁` over
> the first, inducing `κ : K₂ ⟶ K₁` on the kernels and the identity on `F`, then the class
> `ξ_{F'₁}` is the image of `ξ_{F'₂}` under the map `Ext¹_O(F, K₂) ⟶ Ext¹_O(F, K₁)` given by
> functoriality of `Ext` in `κ`.

```lean
theorem underlyingExtensionClass_eq_comp_mk₀
    [HasExt.{e} (SheafOfModules.{w'}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor ι).obj X.O)))]
    (h : O₂ ⟶ O₁) (hh : h ≫ s₁ = s₂)
    (hπ : splittingRingHom (homOn ι s₁) hi₁ π₁ =
      splittingRingHom (homOn ι s₂) hi₂ π₂ ≫ morphismRingHom h)
    (F K₁ K₂ : SheafOfModules.{w'}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor ι).obj X.O)))
    (κ : K₂ ⟶ K₁)
    (E₂ : Abelian.YonedaExtension
      ((SheafOfModules.restrictScalars (structureRingHom s₂)).obj F)
      ((SheafOfModules.restrictScalars (structureRingHom s₂)).obj K₂) 0)
    (E₁ : Abelian.YonedaExtension
      ((SheafOfModules.restrictScalars (structureRingHom s₁)).obj F)
      ((SheafOfModules.restrictScalars (structureRingHom s₁)).obj K₁) 0)
    (φ : E₂.Z.left ⟶
      (SheafOfModules.restrictScalars (morphismRingHom h)).obj E₁.Z.left)
    (hφf : E₂.f ≫ φ = (SheafOfModules.restrictScalars (structureRingHom s₂)).map κ ≫
      (presentationCompIso s₁ s₂ h hh K₁).hom ≫
        (SheafOfModules.restrictScalars (morphismRingHom h)).map E₁.f)
    (hφg : φ ≫ (SheafOfModules.restrictScalars (morphismRingHom h)).map E₁.g =
      E₂.g ≫ (presentationCompIso s₁ s₂ h hh F).hom) :
    underlyingExtensionClass (homOn ι s₁) hi₁ π₁ F K₁ E₁ =
      (underlyingExtensionClass (homOn ι s₂) hi₂ π₂ F K₂ E₂).comp
        (Abelian.Ext.mk₀ κ) (add_zero 1)
```

## Tag 0CYC, a remark

[Tag 0CYC](https://stacks.math.columbia.edu/tag/0CYC) in the Stacks Project.

**`Deformation.ToposThickening.MorphismOfFirstOrderThickenings.existenceObstructionClass_first`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ObstructionCompatibility.lean, line 405](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ObstructionCompatibility.lean#L405).

> The obstruction classes of the two thickenings are compatible: the map
> `Ext²_O(F, K₂) ⟶ Ext²_O(F, K₁)` induced by `κ` carries `o(F, K₂, c₂)` to `o(F, K₁, c₁)`.

```lean
theorem existenceObstructionClass_first
    [HasExt.{e} (SheafOfModules.{w₂} (Stacks.SheafOfModules.Tensor.ringSheaf D.O₂))]
    (F K₁ K₂ : SheafOfModules.{w₂} (Stacks.SheafOfModules.Tensor.ringSheaf (baseRing i)))
    (c₁ : ((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).obj D.first.I).obj F ⟶ K₁)
    (c₂ : ((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).obj D.second.I).obj F ⟶ K₂)
    (κ : K₂ ⟶ K₁)
    (hκ : c₂ ≫ κ =
      ((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).map D.idealMap).app F ≫ c₁) :
    existenceObstructionClass D.first F K₁ c₁ =
      (existenceObstructionClass D.second F K₂ c₂).comp (Abelian.Ext.mk₀ κ) (add_zero 2)
```

## Tag 08ML, a remark

[Tag 08ML](https://stacks.math.columbia.edu/tag/08ML) in the Stacks Project.

**`Deformation.ToposThickening.FirstOrderThickeningSequence`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/FirstOrderThickeningSequence.lean, line 109](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/FirstOrderThickeningSequence.lean#L109). The attribute's comment: “the sequence of morphisms of first order thickenings being classified”.

> **Stacks 08ML.** A sequence of morphisms of first order thickenings of a ringed topos
> `X`: three first order thickenings `i₁`, `i₂`, `i₃` of `X`, with their defining ideals, and two
> composable morphisms `f₁₂`, `f₂₃` between them lying over the identity of `X`.

```lean
structure FirstOrderThickeningSequence
```

**`Deformation.ToposThickening.FirstOrderThickeningSequence.IsComplex`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/FirstOrderThickeningSequence.lean, line 205](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/FirstOrderThickeningSequence.lean#L205). The attribute's comment: “paragraph (1), the definition: the complex condition on the ideal maps”.

> **Stacks 08ML.** A sequence of morphisms of first order thickenings of a ringed topos is a
> *complex* when the induced maps of its defining ideals compose to zero, so that
> `I₃ ⟶ I₂ ⟶ I₁` is a complex of modules.

```lean
def IsComplex : Prop
```

**`Deformation.ToposThickening.FirstOrderThickeningSequence.IsShortExactSequence`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/FirstOrderThickeningSequence.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/FirstOrderThickeningSequence.lean#L225). The attribute's comment: “paragraph (2): the short exact sequence condition on the ideal maps”.

> **Stacks 08ML.** A sequence of morphisms of first order thickenings of a ringed topos is a
> *short exact sequence* when its induced maps of defining ideals form a short exact sequence
> `0 ⟶ I₃ ⟶ I₂ ⟶ I₁ ⟶ 0` of modules: the sequence is a complex, the map `I₃ ⟶ I₂` is a
> monomorphism, the map `I₂ ⟶ I₁` is an epimorphism, and the complex is exact in the middle.

```lean
def IsShortExactSequence : Prop
```

**`Deformation.ToposThickening.FirstOrderThickeningComplex.fSharp₃_comp_splitting`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ThickeningComplexTrivialization.lean, line 175](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ThickeningComplexTrivialization.lean#L175). The attribute's comment: “the composition D₁ ⟶ D₃ factors through the base”.

> **Stacks 08ML.** For a complex of first order thickenings, the composition
> `(Sh(D₁), O'₁) ⟶ (Sh(D₃), O'₃)` factors through `(Sh(C), O) ⟶ (Sh(D₃), O'₃)`: on structure
> sheaves, the composite `O'₃ ⟶ O'₁` is `O'₃ ⟶ O ⟶ O'₁`.

```lean
theorem fSharp₃_comp_splitting : S.fSharp₃ ≫ S.splitting hS = S.whole.hSharp
```

**`Deformation.ToposThickening.FirstOrderThickeningComplex.trivialization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ThickeningComplexTrivialization.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ThickeningComplexTrivialization.lean#L207). The attribute's comment: “the canonical trivialization of the smallest thickening”.

> **Stacks 08ML.** The canonical trivialization `π : (Sh(D₁), O'₁) ⟶ (Sh(C), O)` of the
> smallest thickening of a complex of first order thickenings.

```lean
noncomputable def trivialization : Trivialization i
```

**`Deformation.ToposThickening.FirstOrderThickeningComplex.isTrivial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ThickeningComplexTrivialization.lean, line 213](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ThickeningComplexTrivialization.lean#L213). The attribute's comment: “the smallest thickening of a complex is trivial”.

> **Stacks 08ML.** The smallest thickening of a complex of first order thickenings is a
> trivial first order thickening of the base.

```lean
theorem isTrivial (S : FirstOrderThickeningComplex i) (hS : S.IsComplex) : IsTrivial i
```

**`Deformation.ToposThickening.FirstOrderThickeningSequence.i₃_fSharp_comp_splitting`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ThickeningSequenceTrivialization.lean, line 465](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ThickeningSequenceTrivialization.lean#L465). The attribute's comment: “the composition D₁ ⟶ D₃ factors through the base”.

> **Stacks 08ML.** For a complex of first order thickenings, the composition
> `(Sh(D₁), O'₁) ⟶ (Sh(D₃), O'₃)` factors through `(Sh(C), O) ⟶ (Sh(D₃), O'₃)`: on structure
> sheaves, the composite `O'₃ ⟶ O'₁` is `O'₃ ⟶ O ⟶ O'₁`, the second map being the canonical map
> carried to the topos of the third thickening.

```lean
theorem i₃_fSharp_comp_splitting (hS : S.IsComplex) :
    S.i₃.fSharp ≫ S.baseIso.inv ≫ (pushforwardCommRingFunctor S.f₂₃.toToposHom).map
        ((pushforwardCommRingFunctor S.f₁₂.toToposHom).map (S.splitting hS)) =
      S.wholeSharp
```

**`Deformation.ToposThickening.FirstOrderThickeningSequence.trivialization`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ThickeningSequenceTrivialization.lean, line 509](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ThickeningSequenceTrivialization.lean#L509). The attribute's comment: “the canonical trivialization of the smallest thickening”.

> **Stacks 08ML.** The canonical trivialization `π : (Sh(D₁), O'₁) ⟶ (Sh(C), O)` of the
> smallest thickening of a complex of first order thickenings.

```lean
noncomputable def trivialization (hS : S.IsComplex) : Trivialization S.i₁
```

**`Deformation.ToposThickening.FirstOrderThickeningSequence.isTrivial`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ThickeningSequenceTrivialization.lean, line 516](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ThickeningSequenceTrivialization.lean#L516). The attribute's comment: “the smallest thickening of a complex is trivial”.

> **Stacks 08ML.** The smallest thickening of a complex of first order thickenings is a
> trivial first order thickening of the base.

```lean
theorem isTrivial (hS : S.IsComplex) : IsTrivial S.i₁
```

## Tag 08MM, a remark

[Tag 08MM](https://stacks.math.columbia.edu/tag/08MM) in the Stacks Project.

**`Deformation.ToposThickening.FirstOrderThickeningComplex.boundary_underlyingExtensionClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ThickeningComplexBoundary.lean, line 199](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ThickeningComplexBoundary.lean#L199). The attribute's comment: “the claim: the boundary of the extension class is the obstruction class”.

> Let `(Sh(C), O)` be a ringed topos, `F` an `O`-module, and let `O'₃ ⟶ O'₂ ⟶ O'₁` be a
> complex of first order thickenings of `(Sh(C), O)` presented on one site, with `π` a
> trivialization of `O'₁`. Let `(Kₖ, cₖ)` be pairs with `cₖ : Iₖ ⊗_O F ⟶ Kₖ` and let
> `0 ⟶ K₃ ⟶ K₂ ⟶ K₁ ⟶ 0` be a short exact sequence of `O`-modules making the two squares `_hc₂₁`
> and `hc₃₂` of the remark commute. Let `F'₂` be an extension as in Stacks 08MB over `O'₂` with
> `c_{F'₂} = c₂` and let `F'₁` be the extension over `O'₁` that Stacks 08MJ produces from it.
>
> Then the boundary map `∂ : Ext¹_O(F, K₁) ⟶ Ext²_O(F, K₃)` of `0 ⟶ K₃ ⟶ K₂ ⟶ K₁ ⟶ 0` — Yoneda
> composition with the class of that sequence — carries the class `ξ_{F'₁}` of Stacks 08MI to the
> obstruction class `o(F, K₃, c₃)` of Stacks 08MF, for comparison data `Q₃`, `E₃`, `presentation`,
> `w`, `hw` and `χ` at the third thickening.

```lean
theorem boundary_underlyingExtensionClass (_hS : S.IsComplex) (π : Trivialization i)
    (F K₁ K₂ K₃ : SheafOfModules.{w'} (Stacks.SheafOfModules.Tensor.ringSheaf (baseRing i)))
    (c₁ : ((Stacks.SheafOfModules.Tensor.sheafTensor.{u', v', w', w', w'}
      (baseRing i)).obj S.lower.first.I).obj F ⟶ K₁)
    (c₂ : ((Stacks.SheafOfModules.Tensor.sheafTensor.{u', v', w', w', w'}
      (baseRing i)).obj S.lower.second.I).obj F ⟶ K₂)
    (c₃ : ((Stacks.SheafOfModules.Tensor.sheafTensor.{u', v', w', w', w'}
      (baseRing i)).obj S.third.I).obj F ⟶ K₃)
    (k₃₂ : K₃ ⟶ K₂) (k₂₁ : K₂ ⟶ K₁) (hk : k₃₂ ≫ k₂₁ = 0)
    (hK : (ShortComplex.mk k₃₂ k₂₁ hk).ShortExact)
    (_hc₂₁ : c₂ ≫ k₂₁ = ((Stacks.SheafOfModules.Tensor.sheafTensor.{u', v', w', w', w'}
      (baseRing i)).map S.idealMap₂₁).app F ≫ c₁)
    (hc₃₂ : c₃ ≫ k₃₂ = ((Stacks.SheafOfModules.Tensor.sheafTensor.{u', v', w', w', w'}
      (baseRing i)).map S.idealMap₃₂).app F ≫ c₂)
    (E₂ : Abelian.YonedaExtension ((structureRestrict (reshapeHom i S.lower.O₂
        S.lower.fSharp₂)).obj F)
      ((structureRestrict (reshapeHom i S.lower.O₂ S.lower.fSharp₂)).obj K₂) 0)
    (_hE₂ : (extensionActionMap S.lower.second E₂).1 = c₂)
    (E₁ : Abelian.YonedaExtension ((structureRestrict i).obj F)
      ((structureRestrict i).obj K₁) 0)
    (_hE₁ : (extensionActionMap S.lower.first E₁).1 = c₁)
    {Q₃ : SheafOfModules.{w'} (Stacks.SheafOfModules.Tensor.ringSheaf (baseRing i))}
    {E₃ : Abelian.YonedaExtension ((structureRestrict S.thirdHom).obj F)
      ((structureRestrict S.thirdHom).obj Q₃) 0}
    (presentation : MonoActionPresentation S.third E₃) (w : Q₃ ⟶ K₂)
    (hw : (extensionActionMap S.third E₃).1 ≫ w =
      ((Stacks.SheafOfModules.Tensor.sheafTensor.{u', v', w', w', w'}
        (baseRing i)).map S.idealMap₃₂).app F ≫ c₂)
    (χ : E₃.Z.left ⟶
      (structureRestrict S.thirdHom).obj ((splitRestriction i S.lower.first π).obj E₁.Z.left))
    (hχf : E₃.f ≫ χ = (structureRestrict S.thirdHom).map (w ≫ k₂₁) ≫
      (structureRestrict S.thirdHom).map (splitExtension i S.lower.first π F K₁ E₁).f)
    (hχg : χ ≫ (structureRestrict S.thirdHom).map
      (splitExtension i S.lower.first π F K₁ E₁).g = E₃.g) :
    (underlyingExtensionClass i S.lower.first π F K₁ E₁).comp hK.extClass (by decide) =
      existenceObstructionClass S.third F K₃ c₃
```

**`Deformation.ToposThickening.FirstOrderThickeningComplex.boundary_underlyingExtensionClass_eq_obstructionClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ThickeningComplexBoundaryCanonical.lean, line 247](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ThickeningComplexBoundaryCanonical.lean#L247).

> **Stacks Project, Tag 08MM.** Let `(Sh(C), O)` be a ringed topos, `F` an `O`-module and
> `O'₃ ⟶ O'₂ ⟶ O'₁` a complex of first order thickenings of `(Sh(C), O)` (Stacks 08ML), presented
> on one site. Let `cₖ : Iₖ ⊗_O F ⟶ Kₖ` be maps and `0 ⟶ K₃ ⟶ K₂ ⟶ K₁ ⟶ 0` a short exact sequence
> of `O`-modules for which the second square `hc₃₂` of the remark commutes. Let `F'₂` be an
> extension `0 ⟶ K₂ ⟶ F'₂ ⟶ F ⟶ 0` over `O'₂` as in Stacks 08MB with `c_{F'₂} = c₂`, and let
> `F'₁` be the extension over `O'₁` that the functoriality of Stacks 08MJ produces from it. That
> functoriality carries `F'₂` to an extension of `F` by `K₁` over `O'₁` together with a map of
> extensions `u` from `F'₂`, which is `K₂ ⟶ K₁` on kernel modules and the identity on `F`; the
> statement is made for every extension `F'₁` receiving such a map, so in particular for the one
> of Stacks 08MJ (`boundary_underlyingExtensionClass_extensionOne_eq_obstructionClass`).
>
> Then the boundary map `∂ : Ext¹_O(F, K₁) ⟶ Ext²_O(F, K₃)` of `0 ⟶ K₃ ⟶ K₂ ⟶ K₁ ⟶ 0` — Yoneda
> composition with the class of that sequence — sends the class `ξ_{F'₁}` of Stacks 08MI, formed
> with the canonical splitting `π = S.trivialization hS` of Stacks 08ML, to the obstruction class
> `o(F, K₃, c₃)` of Stacks 08MF.
>
> The map `c₁` and the first compatibility square of the remark are what make Stacks 08MJ
> applicable; once `F'₁` and `u` are given they are not needed for the identity of classes, so they
> are not hypotheses here. They are hypotheses of the version for the extension that Stacks 08MJ
> constructs.

```lean
theorem boundary_underlyingExtensionClass_eq_obstructionClass
    (F K₁ K₂ K₃ : SheafOfModules.{w'} (Stacks.SheafOfModules.Tensor.ringSheaf (baseRing i)))
    (k₃₂ : K₃ ⟶ K₂) (k₂₁ : K₂ ⟶ K₁) (hk : k₃₂ ≫ k₂₁ = 0)
    (hK : (ShortComplex.mk k₃₂ k₂₁ hk).ShortExact)
    (c₂ : ((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).obj S.lower.second.I).obj F ⟶
      K₂)
    (c₃ : ((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).obj S.third.I).obj F ⟶ K₃)
    (hc₃₂ : c₃ ≫ k₃₂ =
      ((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).map S.idealMap₃₂).app F ≫ c₂)
    (E₂ : Abelian.YonedaExtension
      ((structureRestrict (reshapeHom i S.lower.O₂ S.lower.fSharp₂)).obj F)
      ((structureRestrict (reshapeHom i S.lower.O₂ S.lower.fSharp₂)).obj K₂) 0)
    (hE₂ : (extensionActionMap S.lower.second E₂).1 = c₂)
    (E₁ : Abelian.YonedaExtension ((structureRestrict i).obj F)
      ((structureRestrict i).obj K₁) 0)
    (u : E₂.Z.left ⟶ (S.lower.restrictedExtension E₁).Z.left)
    (hu : E₂.f ≫ u =
      (structureRestrict (reshapeHom i S.lower.O₂ S.lower.fSharp₂)).map k₂₁ ≫
        (S.lower.restrictedExtension E₁).f)
    (hug : u ≫ (S.lower.restrictedExtension E₁).g = E₂.g) :
    (underlyingExtensionClass i S.lower.first (S.trivialization hS) F K₁ E₁).comp hK.extClass
        (by decide) =
      existenceObstructionClass S.third F K₃ c₃
```

**`Deformation.ToposThickening.FirstOrderThickeningComplex.boundary_underlyingExtensionClass_extensionOne_eq_obstructionClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ThickeningComplexBoundaryCanonical.lean, line 337](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ThickeningComplexBoundaryCanonical.lean#L337).

> **Stacks Project, Tag 08MM**, for the extension `F'₁` that Stacks 08MJ constructs. Let
> `(Sh(C), O)` be a ringed topos, `F` an `O`-module and `O'₃ ⟶ O'₂ ⟶ O'₁` a complex of first order
> thickenings of `(Sh(C), O)` (Stacks 08ML), presented on one site. Let `(Kₖ, cₖ)`,
> `k = 1, 2, 3`, be pairs of an `O`-module `Kₖ` and a map `cₖ : Iₖ ⊗_O F ⟶ Kₖ`, and let
> `0 ⟶ K₃ ⟶ K₂ ⟶ K₁ ⟶ 0` be a short exact sequence of `O`-modules making the two squares `hc₂₁`
> and `hc₃₂` of the remark commute. Let `F'₂` be an extension `0 ⟶ K₂ ⟶ F'₂ ⟶ F ⟶ 0` of
> `O'₂`-modules as in Stacks 08MB with `c_{F'₂} = c₂`, and let `F'₁` be the extension of
> `O'₁`-modules that the functoriality of Stacks 08MJ produces from it
> (`MorphismOfFirstOrderThickenings.PushoutExtensionData.extensionOne`, built on the data
> `(F, K₁, K₂, c₁, c₂, K₂ ⟶ K₁)` and the first square).
>
> Then the boundary map `∂ : Ext¹_O(F, K₁) ⟶ Ext²_O(F, K₃)` of `0 ⟶ K₃ ⟶ K₂ ⟶ K₁ ⟶ 0` sends the
> class `ξ_{F'₁}` of Stacks 08MI, formed with the canonical splitting `π = S.trivialization hS` of
> Stacks 08ML, to the obstruction class `o(F, K₃, c₃)` of Stacks 08MF.

```lean
theorem boundary_underlyingExtensionClass_extensionOne_eq_obstructionClass
    (F K₁ K₂ K₃ :
      SheafOfModules.{max v₂ u₂} (Stacks.SheafOfModules.Tensor.ringSheaf (baseRing i)))
    (c₁ : ((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).obj S.lower.first.I).obj F ⟶
      K₁)
    (c₂ : ((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).obj S.lower.second.I).obj F ⟶
      K₂)
    (c₃ : ((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).obj S.third.I).obj F ⟶ K₃)
    (k₃₂ : K₃ ⟶ K₂) (k₂₁ : K₂ ⟶ K₁) (hk : k₃₂ ≫ k₂₁ = 0)
    (hK : (ShortComplex.mk k₃₂ k₂₁ hk).ShortExact)
    (hc₂₁ : c₂ ≫ k₂₁ =
      ((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).map S.idealMap₂₁).app F ≫ c₁)
    (hc₃₂ : c₃ ≫ k₃₂ =
      ((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).map S.idealMap₃₂).app F ≫ c₂)
    (E₂ : Abelian.YonedaExtension
      ((structureRestrict (reshapeHom i S.lower.O₂ S.lower.fSharp₂)).obj F)
      ((structureRestrict (reshapeHom i S.lower.O₂ S.lower.fSharp₂)).obj K₂) 0)
    (hE₂ : (extensionActionMap S.lower.second E₂).1 = c₂) :
    (underlyingExtensionClass i S.lower.first (S.trivialization hS) F K₁
        ((S.lower.pushoutDataOfPushout c₂ c₁ k₂₁ hc₂₁).extensionOne E₂ hE₂)).comp
        hK.extClass (by decide) =
      existenceObstructionClass S.third F K₃ c₃
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 91.10, Tag 08MA](https://stacks.math.columbia.edu/tag/08MA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
