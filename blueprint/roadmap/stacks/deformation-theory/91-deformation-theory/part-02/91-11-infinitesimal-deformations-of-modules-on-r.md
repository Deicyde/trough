---
declaration: section
origin: cited
lean: Deformation.ToposThickening.moduleMapLift_torsor, Deformation.ToposThickening.isFlat_iff_isIso_canonicalMap_of_isStrict, Deformation.ToposThickening.isFinitePresentation_iff_pullbackModules_of_isFlat, Deformation.ToposThickening.exists_addTorsor_moduleMapLift, Deformation.ToposThickening.moduleMapObstruction, Deformation.ToposThickening.moduleMapObstructionClass, Deformation.ToposThickening.moduleMapObstructionClass_eq_zero_iff, Deformation.ToposThickening.moduleMapLiftObstruction_eq_zero_iff
statement: formalized
proof: formalized
---

# 91.11 Infinitesimal deformations of modules on ringed topoi

Section 91.11 of the Stacks Project, [Tag 08MN](https://stacks.math.columbia.edu/tag/08MN). 8 tags here are carried by 12 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08MP, a lemma

[Tag 08MP](https://stacks.math.columbia.edu/tag/08MP) in the Stacks Project.

**`Deformation.ToposThickening.moduleMapLift_torsor`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/PushforwardComparison/ModuleMapLifts.lean, line 382](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/PushforwardComparison/ModuleMapLifts.lean#L382).

> **Stacks 08MP.** If a map of pullbacks across a first order thickening has a lift, then its
> lifts form a principal homogeneous space under the maps from the pullback of `F'` to the descent of
> the ideal product `I·G'`, with translation given by adding the corresponding map into `I·G'`
> followed by its inclusion into `G'`.

```lean
theorem moduleMapLift_torsor (hi : FirstOrderThickening i)
    (F' G' : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))
    (φ : (i.toRingedToposModulesHom.pullbackModules).obj F' ⟶
      (i.toRingedToposModulesHom.pullbackModules).obj G')
    (h : Nonempty (ModuleMapLift F' G' φ)) :
    ∃ t : AddTorsor
        ((i.toRingedToposModulesHom.pullbackModules).obj F' ⟶
          (idealProductModule hi G').val)
        (ModuleMapLift F' G' φ),
      ∀ (α : (i.toRingedToposModulesHom.pullbackModules).obj F' ⟶ (idealProductModule hi G').val)
        (c : ModuleMapLift F' G' φ),
        (t.vadd α c).val = c.val +
          idealProductHomEquiv hi F' G' α ≫ (idealProductSubmodule hi G').ι
```

## Tag 08MQ, a lemma

[Tag 08MQ](https://stacks.math.columbia.edu/tag/08MQ) in the Stacks Project.

**`Deformation.ToposThickening.isFlat_iff_isIso_canonicalMap_of_isStrict`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/FlatLiftFlatness.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/FlatLiftFlatness.lean#L113).

> **Stacks 08MQ.** Let `(f, f')` be a morphism of first order thickenings of ringed topoi as in
> Situation 08M7, let `ℱ'` be an `O'`-module and set `ℱ = i^*ℱ'`. Assume that `ℱ` is flat over
> `O_ℬ` and that `(f, f')` is a strict morphism of thickenings (Definition 08M9). Then the
> following are equivalent:
>
> 1. `ℱ'` is flat over `O_{ℬ'}`, and
> 2. the canonical map `f^*𝒥 ⊗_O ℱ ⟶ I·ℱ'` is an isomorphism.
>
> Moreover, in this case the maps `f^*𝒥 ⊗_O ℱ ⟶ I ⊗_O ℱ ⟶ I·ℱ'` are isomorphisms.
>
> How the source's objects are read:
>
> * the square is `Deformation.ToposThickening.MorphismOfThickenings.ofFirstOrderThickenings`,
>   built from the first order thickenings `hi` and `ht` and the commutativity `comm`;
> * `O`-modules live on the thickened topos as `i_*O`-modules, as throughout this tree, and
>   `ℱ = i^*ℱ'` is presented by the short exact sequence `0 ⟶ I·ℱ' ⟶ ℱ' ⟶ ℱ ⟶ 0` given by `q`,
>   `hq` and `hqex` (the form `Deformation.ToposThickening.HasFlatLift` uses); the statement holds
>   for every such presentation;
> * "`ℱ` flat over `O_ℬ`" is `Deformation.ToposThickening.IsFlatOverBase`, and "`ℱ'` flat over
>   `O_{ℬ'}`" is flatness of `Deformation.ToposThickening.baseModule`, that is, over `f⁻¹O_{ℬ'}`,
>   which is the definition the source's proof opens with;
> * strictness is `Deformation.ToposThickening.MorphismOfThickenings.IsStrict`, Definition 08M9;
> * the canonical map is `Deformation.ToposThickening.canonicalMap`, the composite of
>   `Deformation.ToposThickening.canonicalFirstFactor` (`f^*𝒥 ⊗_O ℱ ⟶ I ⊗_O ℱ`) and
>   `Deformation.ToposThickening.canonicalSecondFactor` (`I ⊗_O ℱ ⟶ I·ℱ'`). Its source is written
>   `f⁻¹𝒥 ⊗_{f⁻¹O_ℬ} ℱ`, which the source's proof identifies with `f^*𝒥 ⊗_O ℱ` ("observe that
>   `f^*𝒥 ⊗_O ℱ = f⁻¹𝒥 ⊗_{f⁻¹O_ℬ} ℱ`"; in this tree
>   `Stacks.FlatChangeOfRings.cancelExtendScalarsTensorSheafIso'`), and the composite is read
>   over `f⁻¹O_{ℬ'}`, the ring over which both factors are linear; being an isomorphism does not
>   depend on that reading.
>
> The proof is the source's: strictness gives `ℱ = ℱ'/(f⁻¹𝒥)ℱ'`, and the equivalence is the
> flatness criterion of Stacks 08M4 for the square-zero extension `f⁻¹O_{ℬ'} ⟶ f⁻¹O_ℬ`; see
> `Deformation.ToposThickening.isFlat_iff_isIso_canonicalMap`.

```lean
theorem isFlat_iff_isIso_canonicalMap_of_isStrict
    (i : RingedToposHom X X') (t : RingedToposHom S S') (f : RingedToposHom X S)
    (f' : RingedToposHom X' S') (hi : FirstOrderThickening i) (ht : FirstOrderThickening t)
    (comm : f'.comp i = t.comp f)
    (F : SheafOfModules.{w}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor i.toToposHom).obj X.O)))
    (F' : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X'.O))
    (q : F' ⟶ (SheafOfModules.restrictScalars (ringMap i.fSharp)).obj F)
    (hq : (idealProductSubmodule hi F').ι ≫ q = 0)
    (hqex : (ShortComplex.mk (idealProductSubmodule hi F').ι q hq).ShortExact)
    (hstrict : (MorphismOfThickenings.ofFirstOrderThickenings i t f f' hi ht comm).IsStrict)
    (hF : IsFlatOverBase i f F) :
    (AlgebraicGeometry.SheafOfModules.IsFlat (baseModule f' F') ↔
        IsIso (canonicalMap i t f f' hi ht comm F F' q hq hqex)) ∧
      (IsIso (canonicalMap i t f f' hi ht comm F F' q hq hqex) →
        IsIso (canonicalFirstFactor i t f f' hi ht comm F) ∧
          IsIso (canonicalSecondFactor i hi F F' q hq hqex))
```

## Tag 08VU, a lemma

[Tag 08VU](https://stacks.math.columbia.edu/tag/08VU) in the Stacks Project.

**`Deformation.ToposThickening.isFinitePresentation_iff_pullbackModules_of_isFlat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/FinitePresentationFlatLift.lean, line 809](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/FinitePresentationFlatLift.lean#L809).

> **Stacks 08VU.** Let `(f, f')` be a morphism of first order thickenings of ringed topoi as
> in Situation 08M7, let `ℱ'` be an `O'`-module and set `ℱ = i^*ℱ'`. Assume that `ℱ'` is flat
> over `O_{ℬ'}` and that `(f, f')` is a strict morphism of thickenings. Then `ℱ'` is an
> `O'`-module of finite presentation if and only if `ℱ` is an `O`-module of finite
> presentation.
>
> Flatness of `ℱ'` over `O_{ℬ'}` is flatness of `ℱ'` read as an `(f')^{-1}O_{ℬ'}`-module, as in
> `Deformation.ToposThickening.HasFlatLift`, and `ℱ = i^*ℱ'` is the pullback of Stacks 03D6.
>
> The direction (1) ⇒ (2) is Stacks 03DO and uses none of the hypotheses. For (2) ⇒ (1), Stacks
> 03DM moves `ℱ` to the site of the thickening, where each local presentation of it lifts to one of
> `ℱ'`; flatness and strictness enter only through the injectivity of the action of `I` on `ℱ'`
> (`Deformation.ToposThickening.isIdealActionMono`). See the module docstring.

```lean
theorem isFinitePresentation_iff_pullbackModules_of_isFlat
    (i : RingedToposHom X X') (t : RingedToposHom S S') (f : RingedToposHom X S)
    (f' : RingedToposHom X' S') (hi : FirstOrderThickening i) (ht : FirstOrderThickening t)
    (comm : f'.comp i = t.comp f) (F' : SheafOfModules.{w} (ringSheaf X'.O))
    (hflat : AlgebraicGeometry.SheafOfModules.IsFlat
      ((SheafOfModules.restrictScalars
        ((sheafCompose X'.J (forget₂ CommRingCat.{w} RingCat.{w})).map
          f'.fSharpInverseImage)).obj F'))
    (hstrict : (MorphismOfThickenings.ofFirstOrderThickenings i t f f' hi ht comm).IsStrict) :
    F'.IsFinitePresentation ↔
      (i.toRingedToposModulesHom.pullbackModules.obj F').IsFinitePresentation
```

## Tag 08MR, a lemma

[Tag 08MR](https://stacks.math.columbia.edu/tag/08MR) in the Stacks Project.

**`Deformation.ToposThickening.exists_addTorsor_moduleMapLift`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/IdealProductTensorIso.lean, line 342](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/IdealProductTensorIso.lean#L342). The attribute's comment: “The whole statement, under exactly the source's hypotheses (Situation 08M7, strict morphism, G' flat over O\_\{B'}), with the action of the source pinned: α sends φ' to φ' + ι ∘ α, read in I·G' through the canonical isomorphism of 08MQ.”.

> **Stacks 08MR.** Let `(f, f')` be a strict morphism of first order thickenings of ringed
> topoi as in Situation 08M7, let `ℱ'` and `𝒢'` be `O'`-modules with `𝒢'` flat over `O_{ℬ'}`, set
> `ℱ = i^*ℱ'` and `𝒢 = i^*𝒢'`, and let `φ : ℱ ⟶ 𝒢` be a map of `O`-modules. If `φ` has at least
> one lift to an `O'`-linear map `φ' : ℱ' ⟶ 𝒢'`, then its lifts form a principal homogeneous set
> under `Hom_O(ℱ, 𝒢 ⊗_O f^*J)`.
>
> The action is the one of the source's proof, "combine Lemmas 08MP and 08MQ": an element
> `α : ℱ ⟶ 𝒢 ⊗_O f^*J` sends a lift `φ'` to `φ' + ι ∘ α`, where `ι ∘ α : ℱ' ⟶ 𝒢'` is the
> `O'`-linear map corresponding to `α` followed by the symmetry `𝒢 ⊗_O f^*J ≅ f^*J ⊗_O 𝒢`, the
> canonical identification `f^*J ⊗_O 𝒢 ≅ I·𝒢'` of Stacks 08MQ
> (`Deformation.ToposThickening.idealProductTensorIso`) and the inclusion `I·𝒢' ⊂ 𝒢'`.
> Concretely, `α` composed with those identifications is a map into the descent of `I·𝒢'`, which
> `Deformation.ToposThickening.idealProductHomEquiv` (the adjunction `i^* ⊣ i_*`) reads as a map
> `ℱ' ⟶ I·𝒢'`.

```lean
theorem exists_addTorsor_moduleMapLift
    (F' : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X'.O))
    (hstrict : (MorphismOfThickenings.ofFirstOrderThickenings i t f f' hi ht comm).IsStrict)
    (hG : AlgebraicGeometry.SheafOfModules.IsFlat
      ((SheafOfModules.restrictScalars (ringMap f'.fSharpInverseImage)).obj G'))
    (φ : (pullbackModules i.toRingedToposModulesHom).obj F' ⟶
      (pullbackModules i.toRingedToposModulesHom).obj G')
    (hne : Nonempty (ModuleMapLift F' G' φ)) :
    ∃ T : AddTorsor
        ((pullbackModules i.toRingedToposModulesHom).obj F' ⟶
          ((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, w, w} X.O).flip.obj
              (basePullbackIdeal t f ht)).obj
            ((pullbackModules i.toRingedToposModulesHom).obj G'))
        (ModuleMapLift F' G' φ),
      ∀ (α : (pullbackModules i.toRingedToposModulesHom).obj F' ⟶
          ((Stacks.SheafOfModules.Tensor.sheafTensor.{u, v, w, w, w} X.O).flip.obj
              (basePullbackIdeal t f ht)).obj
            ((pullbackModules i.toRingedToposModulesHom).obj G'))
        (φ' : ModuleMapLift F' G' φ),
        (T.vadd α φ').val = φ'.val +
          idealProductHomEquiv hi F' G'
              (α ≫ ((Stacks.SheafOfModules.FlatSquareZero.tensorLeftIsoTensorRight X.O
                  (basePullbackIdeal t f ht)).app
                  ((pullbackModules i.toRingedToposModulesHom).obj G')).inv ≫
                (idealProductTensorIso i t f f' hi ht comm G' hstrict hG).hom) ≫
            (idealProductSubmodule hi G').ι
```

## Tag 08MS, a lemma

[Tag 08MS](https://stacks.math.columbia.edu/tag/08MS) in the Stacks Project.

**`Deformation.ToposThickening.moduleMapObstruction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ModuleMapObstruction.lean, line 240](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/ModuleMapObstruction.lean#L240).

> **Stacks 08MS.** There is a class `o(φ)` in `Ext¹_O(Li^*F', I·G')` whose vanishing is
> necessary and sufficient for the `O`-linear map `φ : i^*F' ⟶ i^*G'` to be the pullback of an
> `O'`-linear map `F' ⟶ G'`.
>
> The class is the connecting class of the sequence `0 ⟶ I·G' ⟶ G' ⟶ i_*i^*G' ⟶ 0` on the adjoint
> transpose of `φ`, read across `Li^* ⊣ Ri_*`.

```lean
noncomputable def moduleMapObstruction :
    { o : DerivedCategory.Ext
        (d.functor.obj ((DerivedCategory.singleFunctor
          (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) 0).obj F'))
        ((DerivedCategory.singleFunctor
          (SheafOfModules.{w} ((Stacks.SheafOfModules.Tensor.ringSheaf (J := X.J)) X.O)) 0).obj
            (idealProductModule hi G').val) 1 //
      o = 0 ↔ Nonempty (ModuleMapLift F' G' φ) }
```

**`Deformation.ToposThickening.moduleMapObstructionClass`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ModuleMapObstruction.lean, line 273](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/ModuleMapObstruction.lean#L273).

> **Stacks 08MS.** The obstruction class `o(φ) ∈ Ext¹_O(Li^*F', I·G')` itself.

```lean
noncomputable abbrev moduleMapObstructionClass :
    DerivedCategory.Ext
      (d.functor.obj ((DerivedCategory.singleFunctor
        (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O)) 0).obj F'))
      ((DerivedCategory.singleFunctor
        (SheafOfModules.{w} ((Stacks.SheafOfModules.Tensor.ringSheaf (J := X.J)) X.O)) 0).obj
          (idealProductModule hi G').val) 1
```

**`Deformation.ToposThickening.moduleMapObstructionClass_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ModuleMapObstruction.lean, line 284](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/ModuleMapObstruction.lean#L284).

> **Stacks 08MS.** The obstruction class vanishes exactly when `φ` lifts.

```lean
theorem moduleMapObstructionClass_eq_zero_iff :
    moduleMapObstructionClass hi d F' G' φ = 0 ↔ Nonempty (ModuleMapLift F' G' φ)
```

**`Deformation.ToposThickening.moduleMapLiftObstruction_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ModuleMapObstructionDerivedPullback.lean, line 113](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/ModuleMapObstructionDerivedPullback.lean#L113).

> **Stacks 08MS.** Let `i : (Sh(C), O) ⟶ (Sh(D), O')` be a first order thickening of ringed
> topoi, let `F'`, `G'` be `O'`-modules and let `φ : i^*F' ⟶ i^*G'` be `O`-linear. The element
> `o(φ) ∈ Ext¹_O(Li^*F', I·G')` vanishes if and only if `φ` lifts to an `O'`-linear map
> `φ' : F' ⟶ G'`, i.e. one with `i^*φ' = φ`.

```lean
theorem moduleMapLiftObstruction_eq_zero_iff (hi : FirstOrderThickening i)
    (F' G' : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))
    (φ : (i.toRingedToposModulesHom.pullbackModules).obj F' ⟶
      (i.toRingedToposModulesHom.pullbackModules).obj G') :
    moduleMapLiftObstruction hi F' G' φ = 0 ↔ Nonempty (ModuleMapLift F' G' φ)
```

## Tag 08MT, a lemma

[Tag 08MT](https://stacks.math.columbia.edu/tag/08MT) in the Stacks Project.

**`Deformation.ToposThickening.relativeModuleMapObstructionClass_eq_zero_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/IdealActionMono.lean, line 254](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/IdealActionMono.lean#L254).

> **Stacks 08MT.** Let `(f, f')` be a strict morphism of first order thickenings of ringed
> topoi as in Situation 08M7, let `ℱ'` and `𝒢'` be `O'`-modules flat over `O_{ℬ'}`, set
> `ℱ = i^*ℱ'` and `𝒢 = i^*𝒢'`, and let `φ : ℱ ⟶ 𝒢` be an `O`-linear map. The element
> `o(φ) ∈ Ext¹_O(ℱ, 𝒢 ⊗_O f^*𝒥)` of `Deformation.ToposThickening.relativeModuleMapObstructionClass`
> vanishes if and only if `φ` lifts to an `O'`-linear map `φ' : ℱ' ⟶ 𝒢'`.
>
> The class vanishes exactly when the pulled-back sequence it is the class of splits after `i^*`;
> a splitting descends to one before `i^*`, the unit of the adjunction being invertible on a direct
> image, and a splitting of the pulled-back sequence is a factorization of the transpose of `φ`
> through `𝒢' ⟶ i_*𝒢`, which is a lift of `φ`.

```lean
theorem relativeModuleMapObstructionClass_eq_zero_iff
    (F' G' : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X'.O))
    [HasExt.{e} (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))]
    (hstrict : (MorphismOfThickenings.ofFirstOrderThickenings i t f f' hi ht comm).IsStrict)
    (hF : AlgebraicGeometry.SheafOfModules.IsFlat
      ((SheafOfModules.restrictScalars
        ((sheafCompose X'.J (forget₂ CommRingCat.{w} RingCat.{w})).map
          f'.fSharpInverseImage)).obj F'))
    (hG : AlgebraicGeometry.SheafOfModules.IsFlat
      ((SheafOfModules.restrictScalars
        ((sheafCompose X'.J (forget₂ CommRingCat.{w} RingCat.{w})).map
          f'.fSharpInverseImage)).obj G'))
    (φ : (pullbackModules i.toRingedToposModulesHom).obj F' ⟶
      (pullbackModules i.toRingedToposModulesHom).obj G') :
    relativeModuleMapObstructionClass.{_, _, _, _, _, _, _, _, _, _, _, e} i t f f' hi ht comm F' G'
        hstrict hF hG φ = 0 ↔
      Nonempty (ModuleMapLift F' G' φ)
```

## Tag 08MU, a lemma

[Tag 08MU](https://stacks.math.columbia.edu/tag/08MU) in the Stacks Project.

**`Deformation.ToposThickening.nonempty_addTorsor_flatLiftClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/FlatLiftClassCorrespondence.lean, line 476](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/FlatLiftClassCorrespondence.lean#L476).

> **Stacks 08MU.** Let `(f, f')` be a strict morphism of first order thickenings of ringed
> topoi as in Situation 08M7 and let `ℱ` be an `O`-module flat over `O_ℬ`. If `ℱ` has at least one
> lift to an `O'`-module flat over `O_{ℬ'}`, then the isomorphism classes of such lifts form a
> principal homogeneous set under `Ext¹_O(ℱ, I ⊗_O ℱ)`.
>
> The proof is the source's: Stacks 08MQ makes the canonical map `f^*J ⊗ ℱ ⟶ I ⊗ ℱ` an
> isomorphism, which identifies the lifts with the extensions of `ℱ` by `I ⊗_O ℱ` whose action map
> is the identity (`Deformation.ToposThickening.isFlatLiftClassCorrespondence`), and those form a
> principal homogeneous set by Stacks 08ME (through
> `Deformation.ToposThickening.flatLiftClass_torsor`). The same statement with the action of the
> source's proof made explicit is `Deformation.ToposThickening.exists_addTorsor_flatLiftClass`.

```lean
theorem nonempty_addTorsor_flatLiftClass
    [HasExt.{e} (SheafOfModules.{w}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor i.toToposHom).obj X.O)))]
    [HasExt.{e} (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X'.O))]
    (hstrict : (MorphismOfThickenings.ofFirstOrderThickenings i t f f' hi ht comm).IsStrict)
    (hflat : IsFlatOverBase i f F) (hne : Nonempty (FlatLift i f' hi F)) :
    Nonempty (AddTorsor
      (Abelian.Ext.{e} F
        (((Stacks.SheafOfModules.Tensor.sheafTensor.{u', v', w, w, w}
          ((pushforwardCommRingFunctor i.toToposHom).obj X.O)).obj hi.I).obj F) 1)
      (FlatLiftClass i f' hi F))
```

**`Deformation.ToposThickening.exists_addTorsor_flatLiftClass`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/FlatLiftClassTorsor.lean, line 96](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/FlatLiftClassTorsor.lean#L96).

> **Stacks 08MU.** Let `(f, f')` be a strict morphism of first order thickenings of ringed
> topoi as in Situation 08M7 and let `ℱ` be an `O`-module flat over `O_ℬ`. If there is a pair
> `(ℱ', α)` consisting of an `O'`-module `ℱ'` flat over `O_{ℬ'}` and an isomorphism
> `α : i^*ℱ' ≅ ℱ`, then the isomorphism classes of such pairs form a principal homogeneous set
> under `Ext¹_O(ℱ, I ⊗_O ℱ)`.
>
> The action is the one of the source's proof. A pair `(ℱ', α)` gives the extension
> `0 ⟶ I ⊗_O ℱ ⟶ ℱ' ⟶ ℱ ⟶ 0` of `O'`-modules whose first map is the canonical map
> `I ⊗_O ℱ ≅ I·ℱ' ⊂ ℱ'` (`Deformation.ToposThickening.FlatLift.fixedActionExtension`; the canonical
> map is an isomorphism onto `I·ℱ'` by Stacks 08MQ), and `a ∈ Ext¹_O(ℱ, I ⊗_O ℱ)` sends the class
> of `(ℱ', α)` to the class of `(𝒢', β)` exactly when the `Ext¹_{O'}` class of the extension of
> `𝒢'` is that of `ℱ'` plus the image of `a`, which is the action of Stacks 08ME.

```lean
theorem exists_addTorsor_flatLiftClass (i : RingedToposHom X X') (t : RingedToposHom S S')
    (f : RingedToposHom X S) (f' : RingedToposHom X' S') (hi : FirstOrderThickening i)
    (ht : FirstOrderThickening t) (comm : f'.comp i = t.comp f)
    (F : SheafOfModules.{w}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor i.toToposHom).obj X.O)))
    [HasExt.{e} (SheafOfModules.{w}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor i.toToposHom).obj X.O)))]
    [HasExt.{e} (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X'.O))]
    (hstrict : (MorphismOfThickenings.ofFirstOrderThickenings i t f f' hi ht comm).IsStrict)
    (hflat : IsFlatOverBase i f F) (hne : Nonempty (FlatLift i f' hi F)) :
    ∃ T : AddTorsor
        (Abelian.Ext.{e} F
          (((Stacks.SheafOfModules.Tensor.sheafTensor
            ((pushforwardCommRingFunctor i.toToposHom).obj X.O)).flip.obj F).obj hi.I) 1)
        (FlatLiftClass i f' hi F),
      ∀ (a : Abelian.Ext.{e} F
          (((Stacks.SheafOfModules.Tensor.sheafTensor
            ((pushforwardCommRingFunctor i.toToposHom).obj X.O)).flip.obj F).obj hi.I) 1)
        (A B : FlatLift i f' hi F),
        T.vadd a (Quotient.mk (flatLiftSetoid i f' hi F) A) =
            Quotient.mk (flatLiftSetoid i f' hi F) B ↔
          extensionClass F
              (((Stacks.SheafOfModules.Tensor.sheafTensor
                ((pushforwardCommRingFunctor i.toToposHom).obj X.O)).flip.obj F).obj hi.I)
              (B.fixedActionExtension i t f f' hi ht comm F
                ((isStrictPullbackIdealMap_iff_isStrict i t f f' hi ht comm).mpr hstrict)
                (isFlat_reducedBaseModule_of_isFlatOverBase i t f f' hi ht comm F hflat)) =
            (SheafOfModules.restrictScalars (structureRingMap i)).mapExtAddHom F
                (((Stacks.SheafOfModules.Tensor.sheafTensor
                  ((pushforwardCommRingFunctor i.toToposHom).obj X.O)).flip.obj F).obj hi.I) 1 a +
              extensionClass F
                (((Stacks.SheafOfModules.Tensor.sheafTensor
                  ((pushforwardCommRingFunctor i.toToposHom).obj X.O)).flip.obj F).obj hi.I)
                (A.fixedActionExtension i t f f' hi ht comm F
                  ((isStrictPullbackIdealMap_iff_isStrict i t f f' hi ht comm).mpr hstrict)
                  (isFlat_reducedBaseModule_of_isFlatOverBase i t f f' hi ht comm F hflat))
```

## Tag 08MV, a lemma

[Tag 08MV](https://stacks.math.columbia.edu/tag/08MV) in the Stacks Project.

**`Deformation.ToposThickening.hasFlatLift_iff_isIso_and_obstruction_eq_zero'`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/FlatLiftCorrespondence.lean, line 234](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/FlatLiftCorrespondence.lean#L234). The attribute's comment: “in Situation 08M7, for a strict morphism and F flat over O\_B”.

> **Stacks 08MV, unconditionally.** Let `(f, f')` be a morphism of first order thickenings of
> ringed topoi as in Situation 08M7, strict, and let `ℱ` be an `O`-module flat over `O_ℬ`. Then
> `ℱ` has a lift to an `O'`-module flat over `O_{ℬ'}` if and only if the canonical map
> `f^*J ⊗ ℱ ⟶ I ⊗ ℱ` is an isomorphism and the obstruction class `o(ℱ, I ⊗_O ℱ, 1)` of
> Stacks 08MF vanishes.
>
> This is `Deformation.ToposThickening.hasFlatLift_iff_isIso_and_obstruction_eq_zero` with its
> `Deformation.ToposThickening.IsFlatLiftCorrespondence` hypothesis supplied by
> `Deformation.ToposThickening.isFlatLiftCorrespondence`.

```lean
theorem hasFlatLift_iff_isIso_and_obstruction_eq_zero'
    [HasExt.{e} (SheafOfModules.{w}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor i.toToposHom).obj X.O)))]
    [HasExt.{e} (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X'.O))]
    (hstrict : (MorphismOfThickenings.ofFirstOrderThickenings i t f f' hi ht comm).IsStrict)
    (hflat : IsFlatOverBase i f F) :
    HasFlatLift i f' hi F ↔
      IsIso (idealTensorComparison i t f f' hi ht comm F) ∧
        existenceObstructionClass hi F
            (((Stacks.SheafOfModules.Tensor.sheafTensor ((pushforwardCommRingFunctor
                i.toToposHom).obj X.O)).flip.obj F).obj hi.I)
            (𝟙 (((Stacks.SheafOfModules.Tensor.sheafTensor ((pushforwardCommRingFunctor
                i.toToposHom).obj X.O)).flip.obj F).obj
              hi.I)) = 0
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 91.11, Tag 08MN](https://stacks.math.columbia.edu/tag/08MN)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
