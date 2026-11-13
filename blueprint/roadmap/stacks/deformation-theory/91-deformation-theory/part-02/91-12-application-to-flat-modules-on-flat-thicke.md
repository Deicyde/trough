---
declaration: section
origin: cited
lean: Deformation.ToposThickening.hasFlatLift_iff_basePullbackIdeal_obstruction_eq_zero, Deformation.ToposThickening.exists_addTorsor_flatLiftClass_basePullbackIdeal, Deformation.ToposThickening.autOverIdentityExtZeroEquiv_spec, Deformation.ToposThickening.FlatThickeningMorphismSituation, Deformation.ToposThickening.MorphismOfFirstOrderThickenings.existenceObstructionClass_first_basePullbackIdeal, Deformation.ToposThickening.FlatThickeningComplexSituation, Deformation.ToposThickening.FlatThickeningComplexSituation.π, Deformation.ToposThickening.FlatThickeningComplexSituation.reduction
statement: formalized
proof: formalized
---

# 91.12 Application to flat modules on flat thickenings of ringed topoi

Section 91.12 of the Stacks Project, [Tag 08VV](https://stacks.math.columbia.edu/tag/08VV). 5 tags here are carried by 9 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 08VW, a lemma

[Tag 08VW](https://stacks.math.columbia.edu/tag/08VW) in the Stacks Project.

**`Deformation.ToposThickening.hasFlatLift_iff_basePullbackIdeal_obstruction_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/FlatThickeningFlatLifts.lean, line 242](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/FlatThickeningFlatLifts.lean#L242). The attribute's comment: “part (1): a flat lift exists iff o(ℱ, f^*J ⊗\_O ℱ, 1) vanishes”.

> **Stacks 08VW, part (1).** In Situation 08VV — `(f, f')` a strict morphism of first order
> thickenings of ringed topoi with `f'` flat, and `ℱ` an `O`-module flat over `O_ℬ` — there is an
> `O'`-module `ℱ'` flat over `O_{ℬ'}` with `i^*ℱ' ≅ ℱ` if and only if the class
> `o(ℱ, f^*J ⊗_O ℱ, 1) ∈ Ext²_O(ℱ, f^*J ⊗_O ℱ)` of Stacks 08MF vanishes.
>
> Here `1` is the action `I ⊗_O ℱ ⟶ f^*J ⊗_O ℱ` which is the identity under the identification
> `I = f^*J` of Situation 08VV, i.e. the inverse of
> `Deformation.ToposThickening.basePullbackIdealTensorIso`.

```lean
theorem hasFlatLift_iff_basePullbackIdeal_obstruction_eq_zero
    (F : SheafOfModules.{w}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor i.toToposHom).obj X.O)))
    [HasExt.{e} (SheafOfModules.{w}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor i.toToposHom).obj X.O)))]
    [HasExt.{e} (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X'.O))]
    (hstrict : (MorphismOfThickenings.ofFirstOrderThickenings i t f f' hi ht comm).IsStrict)
    (hf' : f'.IsFlat) (hflat : IsFlatOverBase i f F) :
    HasFlatLift i f' hi F ↔
      existenceObstructionClass hi F
        (((Stacks.SheafOfModules.Tensor.sheafTensor
          ((pushforwardCommRingFunctor i.toToposHom).obj X.O)).flip.obj F).obj
          (basePullbackIdealOverThickened i t f ht))
        (basePullbackIdealTensorIso i t f f' hi ht comm hf' hstrict F).inv = 0
```

**`Deformation.ToposThickening.exists_addTorsor_flatLiftClass_basePullbackIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/FlatThickeningFlatLifts.lean, line 274](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/FlatThickeningFlatLifts.lean#L274). The attribute's comment: “part (2): the lift classes are a torsor under Ext¹\_O(ℱ, f^*J ⊗\_O ℱ)”.

> **Stacks 08VW, part (2).** In Situation 08VV, if `ℱ` has a lift to an `O'`-module flat over
> `O_{ℬ'}`, then the isomorphism classes of such lifts form a principal homogeneous set under
> `Ext¹_O(ℱ, f^*J ⊗_O ℱ)`.
>
> The action is the one of Stacks 08MU, read through the identification `f^*J ⊗_O ℱ ≅ I ⊗_O ℱ`
> (`Deformation.ToposThickening.basePullbackIdealTensorIso`): a lift `ℱ'` gives the extension
> `0 ⟶ I ⊗_O ℱ ⟶ ℱ' ⟶ ℱ ⟶ 0` of `O'`-modules
> (`Deformation.ToposThickening.FlatLift.fixedActionExtension`), and `a` sends the class of `ℱ'` to
> the class of `𝒢'` exactly when the `Ext¹_{O'}` class of the extension of `𝒢'` is that of `ℱ'` plus
> the image of `a` in `Ext¹_{O'}(ℱ, I ⊗_O ℱ)`.

```lean
theorem exists_addTorsor_flatLiftClass_basePullbackIdeal
    (F : SheafOfModules.{w}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor i.toToposHom).obj X.O)))
    [HasExt.{e} (SheafOfModules.{w}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor i.toToposHom).obj X.O)))]
    [HasExt.{e} (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X'.O))]
    (hstrict : (MorphismOfThickenings.ofFirstOrderThickenings i t f f' hi ht comm).IsStrict)
    (hf' : f'.IsFlat) (hflat : IsFlatOverBase i f F) (hne : Nonempty (FlatLift i f' hi F)) :
    ∃ T : AddTorsor
        (Abelian.Ext.{e} F
          (((Stacks.SheafOfModules.Tensor.sheafTensor
            ((pushforwardCommRingFunctor i.toToposHom).obj X.O)).flip.obj F).obj
            (basePullbackIdealOverThickened i t f ht)) 1)
        (FlatLiftClass i f' hi F),
      ∀ (a : Abelian.Ext.{e} F
          (((Stacks.SheafOfModules.Tensor.sheafTensor
            ((pushforwardCommRingFunctor i.toToposHom).obj X.O)).flip.obj F).obj
            (basePullbackIdealOverThickened i t f ht)) 1)
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
                  ((pushforwardCommRingFunctor i.toToposHom).obj X.O)).flip.obj F).obj hi.I) 1
                (a.comp (Abelian.Ext.mk₀
                  (basePullbackIdealTensorIso i t f f' hi ht comm hf' hstrict F).hom)
                  (add_zero 1)) +
              extensionClass F
                (((Stacks.SheafOfModules.Tensor.sheafTensor
                  ((pushforwardCommRingFunctor i.toToposHom).obj X.O)).flip.obj F).obj hi.I)
                (A.fixedActionExtension i t f f' hi ht comm F
                  ((isStrictPullbackIdealMap_iff_isStrict i t f f' hi ht comm).mpr hstrict)
                  (isFlat_reducedBaseModule_of_isFlatOverBase i t f f' hi ht comm F hflat))
```

**`Deformation.ToposThickening.autOverIdentityExtZeroEquiv_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/FlatThickeningFlatLifts.lean, line 351](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/FlatThickeningFlatLifts.lean#L351). The attribute's comment: “part (3): automorphisms of a lift over id\_ℱ are Ext⁰\_O(ℱ, f^*J ⊗\_O ℱ)”.

> **Stacks 08VW, part (3).** In Situation 08VV, given a lift `ℱ'` of `ℱ` to an `O'`-module flat
> over `O_{ℬ'}`, the set of automorphisms of `ℱ'` which pull back to the identity of `ℱ` is
> canonically isomorphic to `Ext⁰_O(ℱ, f^*J ⊗_O ℱ)` (with `ℱ` written as `i^*ℱ'`): the bijection
> `Deformation.ToposThickening.autOverIdentityExtZeroEquiv` sends `α` to `1 + α`, and it carries
> addition to composition, so it is an isomorphism of groups.

```lean
theorem autOverIdentityExtZeroEquiv_spec
    (F : SheafOfModules.{w}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor i.toToposHom).obj X.O)))
    [HasExt.{e} (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O))]
    (hstrict : (MorphismOfThickenings.ofFirstOrderThickenings i t f f' hi ht comm).IsStrict)
    (L : FlatLift i f' hi F) :
    (∀ α, (autOverIdentityExtZeroEquiv.{_, _, _, _, _, _, _, _, _, _, _, e} i t f f' hi ht comm F
        hstrict L α).val.hom =
      𝟙 L.module' + idealProductHomEquiv hi L.module' L.module'
          (Abelian.Ext.addEquiv₀ α ≫
            (idealProductTensorIso i t f f' hi ht comm L.module' hstrict L.isFlat).hom) ≫
        (idealProductSubmodule hi L.module').ι) ∧
    ∀ α β, autOverIdentityExtZeroEquiv i t f f' hi ht comm F hstrict L (α + β) =
      autOverIdentityExtZeroEquiv i t f f' hi ht comm F hstrict L α *
        autOverIdentityExtZeroEquiv i t f f' hi ht comm F hstrict L β
```

## Tag 0CYD, a situation

[Tag 0CYD](https://stacks.math.columbia.edu/tag/0CYD) in the Stacks Project.

**`Deformation.ToposThickening.FlatThickeningMorphismSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/MorphismOfFlatThickenings.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/MorphismOfFlatThickenings.lean#L107). The attribute's comment: “the situation”.

> **Stacks 0CYD.** Two strict flat morphisms of first order thickenings of one morphism of
> ringed topoi `f : (Sh(C), O) ⟶ (Sh(B), O_B)`, related by a morphism of the thickenings they
> deform `f` by, together with an `O`-module flat over `O_B`.

```lean
structure FlatThickeningMorphismSituation
    (D₁ : MorphismOfThickenings X X₁ S S₁) (D₂ : MorphismOfThickenings X X₂ S S₂)
```

## Tag 0CYE, a lemma

[Tag 0CYE](https://stacks.math.columbia.edu/tag/0CYE) in the Stacks Project.

**`Deformation.ToposThickening.MorphismOfFirstOrderThickenings.existenceObstructionClass_first_basePullbackIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/FlatObstructionCompatibilityBaseIdeal.lean, line 127](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/FlatObstructionCompatibilityBaseIdeal.lean#L127).

> **Stacks 0CYE.** In Situation 0CYD — a morphism `h` of first order thickenings
> `(Sh(C), O) ⟶ (Sh(C'₁), O'₁) ⟶ (Sh(C'₂), O'₂)` (the data `U`, with `h^♯ = U.hSharp`), a
> morphism `k` of first order thickenings `(Sh(B), O_ℬ) ⟶ (Sh(B'₁), O_{ℬ'₁}) ⟶ (Sh(B'₂), O_{ℬ'₂})`
> (the data `E`, with `k^♯ = E.hSharp`), morphisms `f'₁, f'₂` restricting to
> `f : (Sh(C), O) ⟶ (Sh(B), O_ℬ)` (`r₁`, `r₂`) with `f'₂ ∘ h = k ∘ f'₁` (`comm`), both pairs
> `(f, f'ₖ)` strict (`hs₁`, `hs₂`), both `f'ₖ` flat (`hf₁`, `hf₂`), and an `O`-module `ℱ` flat
> over `O_ℬ` (`_hF`) — the obstruction class `o(ℱ, f^*𝒥₂ ⊗_O ℱ, 1)` maps to the obstruction class
> `o(ℱ, f^*𝒥₁ ⊗_O ℱ, 1)` under the canonical map
> `Ext²_O(ℱ, f^*𝒥₂ ⊗_O ℱ) ⟶ Ext²_O(ℱ, f^*𝒥₁ ⊗_O ℱ)`.
>
> Here `𝒥ₖ` is the defining ideal of the `k`-th thickening of `(Sh(B), O_ℬ)`, the coefficient
> module of the `k`-th column is `f^*𝒥ₖ ⊗_O ℱ`
> (`Deformation.ToposThickening.basePullbackIdealOverThickened`), the action `1` of the `k`-th
> column is the map `Iₖ ⊗_O ℱ ⟶ f^*𝒥ₖ ⊗_O ℱ` that is the identity under the identification
> `f^*𝒥ₖ = Iₖ` of Situation 08VV (the inverse of
> `Deformation.ToposThickening.basePullbackIdealTensorIso`), exactly as in Stacks 08VW, and the
> canonical map is the one induced by `f^*𝒥₂ ⟶ f^*𝒥₁`, the pullback along `f` of the map
> `𝒥₂ ⟶ 𝒥₁` of the lower row (`Deformation.ToposThickening.basePullbackIdealOverThickenedMap`).
> The two thickenings of each row are presented on one site, as in Stacks 0CYC.
>
> The proof is the source's: Stacks 0CYC at `Kₖ = f^*𝒥ₖ ⊗_O ℱ`, whose commutation hypothesis is
> that `I₂ ⟶ I₁` is `f^*𝒥₂ ⟶ f^*𝒥₁` under the identifications `f^*𝒥ₖ = Iₖ`
> (`Deformation.ToposThickening.basePullbackIdealIsoIdeal_hom_comp_idealMap`). The flatness of `ℱ`
> over `O_ℬ` is part of the source's situation and is not needed for the conclusion.

```lean
theorem MorphismOfFirstOrderThickenings.existenceObstructionClass_first_basePullbackIdeal
    (U : MorphismOfFirstOrderThickenings i) (E : MorphismOfFirstOrderThickenings t)
    (f : RingedToposHom X B) (f₁ : RingedToposHom Y B')
    (f₂ : RingedToposHom (reshape Y U.O₂) (reshape B' E.O₂))
    (r₁ : f₁.comp i = t.comp f)
    (r₂ : f₂.comp (reshapeHom i U.O₂ U.fSharp₂) = (reshapeHom t E.O₂ E.fSharp₂).comp f)
    (comm : f₂.comp (RingedToposHom.coefficientMorphism (O := U.O₂) (O' := Y.O) Y.J U.hSharp) =
      (RingedToposHom.coefficientMorphism (O := E.O₂) (O' := B'.O) B'.J E.hSharp).comp f₁)
    (hs₁ : (MorphismOfThickenings.ofFirstOrderThickenings i t f f₁ U.first E.first r₁).IsStrict)
    (hs₂ : (MorphismOfThickenings.ofFirstOrderThickenings (reshapeHom i U.O₂ U.fSharp₂)
      (reshapeHom t E.O₂ E.fSharp₂) f f₂ U.second E.second r₂).IsStrict)
    (hf₁ : f₁.IsFlat) (hf₂ : f₂.IsFlat)
    [HasExt.{e} (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf (baseRing i)))]
    [HasExt.{e} (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))]
    [HasExt.{e} (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf U.O₂))]
    (F : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf (baseRing i)))
    (_hF : IsFlatOverBase i f F) :
    existenceObstructionClass U.first F
        (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj F).obj
          (basePullbackIdealOverThickened i t f E.first))
        (basePullbackIdealTensorIso i t f f₁ U.first E.first r₁ hf₁ hs₁ F).inv =
      (existenceObstructionClass U.second F
          (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj F).obj
            (basePullbackIdealOverThickened i (reshapeHom t E.O₂ E.fSharp₂) f E.second))
          (basePullbackIdealTensorIso (reshapeHom i U.O₂ U.fSharp₂)
            (reshapeHom t E.O₂ E.fSharp₂) f f₂ U.second E.second r₂ hf₂ hs₂ F).inv).comp
        (Abelian.Ext.mk₀ (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj F).map
          (basePullbackIdealOverThickenedMap i E f)))
        (add_zero 2)
```

## Tag 08VX, a situation

[Tag 08VX](https://stacks.math.columbia.edu/tag/08VX) in the Stacks Project.

**`Deformation.ToposThickening.FlatThickeningComplexSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/FlatThickeningComplexSituation.lean, line 107](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/FlatThickeningComplexSituation.lean#L107). The attribute's comment: “the situation: both rows short exact sequences of first order thickenings in the sense of 08ML (exactness of `0 ⟶ I₃ ⟶ I₂ ⟶ I₁ ⟶ 0` of defining ideals as modules over the base), each `f'ᵢ` restricting to `f`, each `(f, f'ᵢ)` strict, each `f'ᵢ` flat, and `ℱ'₂` an `O'₂`-module flat over `O_{ℬ'₂}`”.

> **Stacks 08VX.** A short exact sequence of first order thickenings `O'₃ ⟶ O'₂ ⟶ O'₁` of a
> ringed topos `(Sh(C), O)`, over a short exact sequence of first order thickenings of a ringed
> topos `(Sh(B), O_ℬ)`, by three strict flat deformations `f'₁, f'₂, f'₃` of one morphism
> `f : (Sh(C), O) ⟶ (Sh(B), O_ℬ)` compatible with the two rows, together with an `O'₂`-module
> `ℱ'₂` flat over `O_{ℬ'₂}`.
>
> The first thickening of each row is `i : (Sh(C), O) ⟶ (Sh(C'₁), O'₁)`, respectively
> `t : (Sh(B), O_ℬ) ⟶ (Sh(B'₁), O_{ℬ'₁})`, and the other two are presented on its site, as in
> `Deformation.ToposThickening.FirstOrderThickeningComplex`.
>
> Short exactness of each row is that of Stacks 08ML: the maps `I₃ ⟶ I₂ ⟶ I₁` of defining ideals
> are the restrictions of the ring maps `O'₃ ⟶ O'₂ ⟶ O'₁`, and `0 ⟶ I₃ ⟶ I₂ ⟶ I₁ ⟶ 0` is a short
> exact sequence of `O`-modules, read through the equivalence of topoi of the thickening as
> modules over `i_*O` (respectively `t_*O_ℬ`) on the common underlying site. The squares of the
> diagram are equalities of morphisms of ringed topoi: the horizontal arrows are the identity on
> underlying topoi, so this is the source's identification of the underlying topoi of a
> thickening and of its base (Stacks 08M7, `f = f'` on underlying topoi).

```lean
structure FlatThickeningComplexSituation (i : RingedToposHom X Y) (t : RingedToposHom B B')
```

**`Deformation.ToposThickening.FlatThickeningComplexSituation.π`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/FlatThickeningComplexSituation.lean, line 231](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/FlatThickeningComplexSituation.lean#L231). The attribute's comment: “the canonical splitting `π` of the upper row (Remark 08ML)”.

> **The canonical splitting `π : (Sh(C'₁), O'₁) ⟶ (Sh(C), O)` of Remark Stacks 08ML**, the
> trivialization of the first thickening of the upper row through which the composite
> `(Sh(C'₁), O'₁) ⟶ (Sh(C'₃), O'₃)` factors.

```lean
noncomputable def π : Trivialization i
```

**`Deformation.ToposThickening.FlatThickeningComplexSituation.reduction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/FlatThickeningComplexSituation.lean, line 245](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/FlatThickeningComplexSituation.lean#L245). The attribute's comment: “the module `ℱ = ℱ'₂ ⊗ O`”.

> **The `O`-module `ℱ = ℱ'₂ ⊗ O` of Stacks 08VX**: the pullback `i₂^*ℱ'₂` of `ℱ'₂` along the
> second thickening of the upper row.

```lean
noncomputable def reduction : SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
```

## Tag 08VY, a lemma

[Tag 08VY](https://stacks.math.columbia.edu/tag/08VY) in the Stacks Project.

**`Deformation.ToposThickening.FlatThickeningComplexSituation.boundary_difference_trivialLift_pulledLift_eq_obstruction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/FlatThickeningComplexBoundaryObstruction.lean, line 230](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Deformation/ToposThickening/FlatThickeningComplexBoundaryObstruction.lean#L230). The attribute's comment: “the full statement in Situation 08VX: π^*ℱ and h^*ℱ'₂ are flat over O\_\{ℬ'₁} and restrict to ℱ, their difference lies in the Ext¹\_O(ℱ, f^*𝒥₁ ⊗ ℱ)-torsor of 08VW (2), and its boundary along the short exact sequence of the f^*𝒥ₖ ⊗ ℱ is the 08VW obstruction for the third column, which vanishes exactly when ℱ lifts to an O'₃-module flat over O\_\{ℬ'₃}.”.

> **Stacks Project, Tag 08VY.** In Situation **Stacks 08VX** — a short exact sequence of first
> order thickenings `O'₃ ⟶ O'₂ ⟶ O'₁` of `(Sh(C), O)` over a short exact sequence of first order
> thickenings of `(Sh(B), O_ℬ)`, every `(f, f'ₖ)` strict and every `f'ₖ` flat, and an `O'₂`-module
> `ℱ'₂` flat over `O_{ℬ'₂}`, with `ℱ = ℱ'₂ ⊗ O` — let `π : (Sh(C'₁), O'₁) ⟶ (Sh(C), O)` be the
> canonical splitting of Remark Stacks 08ML.
>
> * `π^*ℱ` and `h^*ℱ'₂` are `O'₁`-modules flat over `O_{ℬ'₁}` (the first two conjuncts) restricting
>   to `ℱ` on `(Sh(C), O)`: they are the flat lifts `trivialLift` and `pulledLift` of `ℱ` across the
>   first column (the third and fourth conjuncts record their modules), whose maps to `i₁_*ℱ` are
>   the canonical identifications (the fifth and sixth conjuncts): for `π^*ℱ = k^*ι_*ℱ`, with
>   `π = ι^{-1} ∘ k` the canonical splitting, the transpose under `k^* ⊣ s^*` of `ι_*ℱ = s^*q^*ι_*ℱ`;
>   for `h^*ℱ'₂`, the transpose under `h^* ⊣ h_*` of the unit `ℱ'₂ ⟶ i₂_*i₂^*ℱ'₂ = h_*i₁_*ℱ`.
> * The maps `f^*𝒥₃ ⟶ f^*𝒥₂ ⟶ f^*𝒥₁` of the coefficient sequence below, defined as the maps
>   `I₃ ⟶ I₂ ⟶ I₁` of the upper row read through the identifications `f^*𝒥ₖ = Iₖ`, are the maps
>   induced by the maps `𝒥₃ ⟶ 𝒥₂ ⟶ 𝒥₁` of the lower row (the seventh and eighth conjuncts), as in
>   Stacks 08VT.
> * The isomorphism classes of flat lifts of `ℱ` across the first column form a principal
>   homogeneous set under `Ext¹_O(ℱ, f^*𝒥₁ ⊗_O ℱ)` with the action of Stacks 08VW (2)
>   (`Deformation.ToposThickening.exists_addTorsor_flatLiftClass_basePullbackIdeal`), and the
>   difference `θ = [h^*ℱ'₂] - [π^*ℱ]` has for boundary along
>   `0 ⟶ f^*𝒥₃ ⊗_O ℱ ⟶ f^*𝒥₂ ⊗_O ℱ ⟶ f^*𝒥₁ ⊗_O ℱ ⟶ 0` (short exact by
>   `baseIdealTensor_shortExact`) the class `o(ℱ, f^*𝒥₃ ⊗_O ℱ, 1)` of Stacks 08VW (1) for the third
>   column, which vanishes exactly when `ℱ` lifts to an `O'₃`-module flat over `O_{ℬ'₃}` (the last
>   conjunct).

```lean
theorem boundary_difference_trivialLift_pulledLift_eq_obstruction
    [HasExt.{e} (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf (baseRing i)))]
    [HasExt.{e} (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))]
    [HasExt.{e} (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf D.upper.O₃))] :
    AlgebraicGeometry.SheafOfModules.IsFlat
        ((SheafOfModules.restrictScalars
          ((sheafCompose Y.J (forget₂ CommRingCat.{w} RingCat.{w})).map
            D.f₁.fSharpInverseImage)).obj D.trivialModule) ∧
      AlgebraicGeometry.SheafOfModules.IsFlat
        ((SheafOfModules.restrictScalars
          ((sheafCompose Y.J (forget₂ CommRingCat.{w} RingCat.{w})).map
            D.f₁.fSharpInverseImage)).obj D.pulledModule) ∧
      D.trivialLift.module' = D.trivialModule ∧ D.pulledLift.module' = D.pulledModule ∧
      D.trivialLift.π = D.trivialModuleIsoPullback.hom ≫
        (D.splittingChangeAdjunction.homEquiv _ _).symm
          (splitRestrictionRestrictScalarsIso i D.upper.lower.first D.π D.F).inv ∧
      D.pulledLift.π = (D.adjH.homEquiv _ _).symm
        (D.i₂.pullbackAdjPushforwardModulesViaComparison.unit.app D.F' ≫
          (D.upper.lower.restrictHIso D.F).inv) ∧
      D.baseIdealMap₃₂ = D.inducedBaseIdealMap₃₂ ∧ D.baseIdealMap₂₁ = D.inducedBaseIdealMap₂₁ ∧
      ∃ T : AddTorsor
          (Abelian.Ext.{e} D.F
            (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj D.F).obj
              (basePullbackIdealOverThickened i t D.f D.lower.lower.first)) 1)
          (FlatLiftClass i D.f₁ D.upper.lower.first D.F),
        (∀ (a : Abelian.Ext.{e} D.F
            (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj D.F).obj
              (basePullbackIdealOverThickened i t D.f D.lower.lower.first)) 1)
          (A B : FlatLift i D.f₁ D.upper.lower.first D.F),
          T.vadd a (Quotient.mk (flatLiftSetoid i D.f₁ D.upper.lower.first D.F) A) =
              Quotient.mk (flatLiftSetoid i D.f₁ D.upper.lower.first D.F) B ↔
            extensionClass D.F
                (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj D.F).obj
                  D.upper.lower.first.I)
                (B.fixedActionExtension i t D.f D.f₁ D.upper.lower.first D.lower.lower.first
                  D.restrict₁ D.F D.isStrictPullbackIdealMap₁ D.isFlat_reducedBaseModule₁) =
              (SheafOfModules.restrictScalars (structureRingMap i)).mapExtAddHom D.F
                  (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj D.F).obj
                    D.upper.lower.first.I) 1
                  (a.comp (Abelian.Ext.mk₀
                    (basePullbackIdealTensorIso i t D.f D.f₁ D.upper.lower.first D.lower.lower.first
                      D.restrict₁ D.flat₁ D.strict₁ D.F).hom) (add_zero 1)) +
                extensionClass D.F
                  (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj D.F).obj
                    D.upper.lower.first.I)
                  (A.fixedActionExtension i t D.f D.f₁ D.upper.lower.first D.lower.lower.first
                    D.restrict₁ D.F D.isStrictPullbackIdealMap₁ D.isFlat_reducedBaseModule₁)) ∧
        (@VSub.vsub _ _ T.toVSub
            (Quotient.mk (flatLiftSetoid i D.f₁ D.upper.lower.first D.F) D.pulledLift)
            (Quotient.mk (flatLiftSetoid i D.f₁ D.upper.lower.first D.F) D.trivialLift)).comp
            D.baseIdealTensor_shortExact.extClass (by decide) =
          existenceObstructionClass D.upper.third D.F
            (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj D.F).obj
              (basePullbackIdealOverThickened D.upper.thirdHom D.lower.thirdHom D.f D.lower.third))
            (basePullbackIdealTensorIso D.upper.thirdHom D.lower.thirdHom D.f D.f₃ D.upper.third
              D.lower.third D.restrict₃ D.flat₃ D.strict₃ D.F).inv ∧
        (HasFlatLift D.upper.thirdHom D.f₃ D.upper.third D.F ↔
          existenceObstructionClass D.upper.third D.F
            (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj D.F).obj
              (basePullbackIdealOverThickened D.upper.thirdHom D.lower.thirdHom D.f D.lower.third))
            (basePullbackIdealTensorIso D.upper.thirdHom D.lower.thirdHom D.f D.f₃ D.upper.third
              D.lower.third D.restrict₃ D.flat₃ D.strict₃ D.F).inv = 0)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 91.12, Tag 08VV](https://stacks.math.columbia.edu/tag/08VV)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
