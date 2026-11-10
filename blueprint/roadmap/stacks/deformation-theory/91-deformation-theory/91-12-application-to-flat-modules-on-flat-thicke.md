---
declaration: section
origin: cited
lean: Deformation.ToposThickening.hasFlatLift_iff_obstruction_eq_zero, Deformation.ToposThickening.hasFlatLift_iff_basePullbackIdeal_obstruction_eq_zero, Deformation.ToposThickening.exists_addTorsor_flatLiftClass_basePullbackIdeal, Deformation.ToposThickening.autOverIdentityExtZeroEquiv_spec, Deformation.ToposThickening.FlatThickeningMorphismSituation, Deformation.ToposThickening.MorphismOfFirstOrderThickenings.existenceObstructionClass_first_tensorIdeal, Deformation.ToposThickening.ShortExactFlatThickeningSituation, Deformation.ToposThickening.ShortExactFlatThickeningSituation.F
statement: formalized
proof: formalized
---

# 91.12 Application to flat modules on flat thickenings of ringed topoi

Section 91.12 of the Stacks Project, [Tag 08VV](https://stacks.math.columbia.edu/tag/08VV). 5 tags here are carried by 10 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08VW, a lemma

[Tag 08VW](https://stacks.math.columbia.edu/tag/08VW) in the Stacks Project.

**`Deformation.ToposThickening.hasFlatLift_iff_obstruction_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/FlatLiftObstruction.lean, line 343](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/FlatLiftObstruction.lean#L343). The attribute's comment: “part (1) only; (2) and (3) are not proved; granting 08MQ as hypotheses”.

> **Stacks 08VW, part (1).** In the situation of Stacks 08VV — a strict morphism `(f, f')` of
> first order thickenings of ringed topoi with `f'` flat, and an `O`-module `ℱ` flat over `O_ℬ` —
> the module `ℱ` has a lift to an `O'`-module flat over `O_{ℬ'}` if and only if the obstruction
> class `o(ℱ, f^*J ⊗_O ℱ, 1)` of Stacks 08MF vanishes. The class is written here for
> `I ⊗_O ℱ`, the two agreeing because `I = f^*J` under these hypotheses.

```lean
theorem hasFlatLift_iff_obstruction_eq_zero
    (i : RingedToposHom X X') (t : RingedToposHom S S') (f : RingedToposHom X S)
    (f' : RingedToposHom X' S') (hi : FirstOrderThickening i) (ht : FirstOrderThickening t)
    (comm : f'.comp i = t.comp f)
    (F : SheafOfModules.{w}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor i.toToposHom).obj X.O)))
    [HasExt.{e} (SheafOfModules.{w}
      (Stacks.SheafOfModules.Tensor.ringSheaf ((pushforwardCommRingFunctor i.toToposHom).obj X.O)))]
    [HasExt.{e} (SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X'.O))]
    (hstrict : (MorphismOfThickenings.ofFirstOrderThickenings i t f f' hi ht comm).IsStrict)
    (hf' : f'.IsFlat) (hflat : IsFlatOverBase i f F)
    (hMQ : IsFlatLiftCorrespondence i t f f' hi ht comm F)
    (hMQ' : IsIdealComparisonIsoOfFlat i t f f' hi ht comm F) :
    HasFlatLift i f' hi F ↔
      existenceObstructionClass hi F
          (((sheafTensor.{u', v', w, w, w}
            ((pushforwardCommRingFunctor i.toToposHom).obj X.O)).obj hi.I).obj F)
          (𝟙 (((sheafTensor.{u', v', w, w, w}
            ((pushforwardCommRingFunctor i.toToposHom).obj X.O)).obj hi.I).obj F)) = 0
```

**`Deformation.ToposThickening.hasFlatLift_iff_basePullbackIdeal_obstruction_eq_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/FlatThickeningFlatLifts.lean, line 236](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/FlatThickeningFlatLifts.lean#L236).

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

**`Deformation.ToposThickening.exists_addTorsor_flatLiftClass_basePullbackIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/FlatThickeningFlatLifts.lean, line 268](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/FlatThickeningFlatLifts.lean#L268).

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

**`Deformation.ToposThickening.autOverIdentityExtZeroEquiv_spec`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/FlatThickeningFlatLifts.lean, line 345](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/FlatThickeningFlatLifts.lean#L345).

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

**`Deformation.ToposThickening.FlatThickeningMorphismSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/MorphismOfFlatThickenings.lean, line 107](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/MorphismOfFlatThickenings.lean#L107). The attribute's comment: “the situation”.

> **Stacks 0CYD.** Two strict flat morphisms of first order thickenings of one morphism of
> ringed topoi `f : (Sh(C), O) ⟶ (Sh(B), O_B)`, related by a morphism of the thickenings they
> deform `f` by, together with an `O`-module flat over `O_B`.

```lean
structure FlatThickeningMorphismSituation
    (D₁ : MorphismOfThickenings X X₁ S S₁) (D₂ : MorphismOfThickenings X X₂ S S₂)
```

## Tag 0CYE, a lemma

[Tag 0CYE](https://stacks.math.columbia.edu/tag/0CYE) in the Stacks Project.

**`Deformation.ToposThickening.MorphismOfFirstOrderThickenings.existenceObstructionClass_first_tensorIdeal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/FlatObstructionCompatibility.lean, line 142](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/FlatObstructionCompatibility.lean#L142). The attribute's comment: “coefficients and Ext map written through the ideals Iₖ, which are f^*Jₖ by 08MQ”.

> **Stacks 0CYE.** In the situation of Stacks 0CYD the canonical map
> `Ext²_O(ℱ, f^*J₂ ⊗_O ℱ) ⟶ Ext²_O(ℱ, f^*J₁ ⊗_O ℱ)` carries the obstruction class
> `o(ℱ, f^*J₂ ⊗_O ℱ, 1)` of the second column to the obstruction class `o(ℱ, f^*J₁ ⊗_O ℱ, 1)` of
> the first.
>
> The coefficient module of the `k`-th column is written `Iₖ ⊗_O ℱ` and the map on `Ext²` is the
> one induced by the map `I₂ ⟶ I₁` of square-zero ideals of the upper row; under the hypotheses of
> Stacks 0CYD the comparison `f^*Jₖ ⟶ Iₖ` is an isomorphism, which is the reading under which
> `Deformation.ToposThickening.hasFlatLift_iff_obstruction_eq_zero` states Stacks 08VW. See the
> implementation notes.
>
> This is Stacks 0CYC at `Kₖ = Iₖ ⊗_O ℱ` and `cₖ = 1`.

```lean
theorem existenceObstructionClass_first_tensorIdeal :
    existenceObstructionClass D.first F
        (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).obj D.first.I).obj F)
        (𝟙 (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).obj D.first.I).obj F)) =
      (existenceObstructionClass D.second F
          (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).obj D.second.I).obj F)
          (𝟙 (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).obj D.second.I).obj F))).comp
        (Abelian.Ext.mk₀
          (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).map D.idealMap).app F))
        (add_zero 2)
```

## Tag 08VX, a situation

[Tag 08VX](https://stacks.math.columbia.edu/tag/08VX) in the Stacks Project.

**`Deformation.ToposThickening.ShortExactFlatThickeningSituation`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ShortExactFlatThickenings.lean, line 176](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ShortExactFlatThickenings.lean#L176). The attribute's comment: “the situation”.

> **Stacks 08VX.** A short exact sequence of first order thickenings of a ringed topos
> `(Sh(C), O)` mapping to a short exact sequence of first order thickenings of a ringed topos
> `(Sh(B), O_B)`, by three strict flat deformations of one morphism `f : (Sh(C), O) ⟶
> (Sh(B), O_B)`, together with an `O'₂`-module flat over `O_{B'₂}` and the canonical splitting
> of the upper row.

```lean
structure ShortExactFlatThickeningSituation
    (upper : FirstOrderThickeningSequence X X₁ X₂ X₃)
    (lower : FirstOrderThickeningSequence S S₁ S₂ S₃)
```

**`Deformation.ToposThickening.ShortExactFlatThickeningSituation.F`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/ShortExactFlatThickenings.lean, line 243](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/ShortExactFlatThickenings.lean#L243). The attribute's comment: “the module `ℱ = ℱ'₂ ⊗ O`”.

> **Stacks 08VX.** The `O`-module `ℱ = ℱ'₂ ⊗ O`: the pullback of `ℱ'₂` along the middle
> thickening of the upper row.

```lean
noncomputable def F (D : ShortExactFlatThickeningSituation upper lower) :
    SheafOfModules.{w} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)
```

## Tag 08VY, a lemma

[Tag 08VY](https://stacks.math.columbia.edu/tag/08VY) in the Stacks Project.

**`Deformation.ToposThickening.FirstOrderThickeningComplex.boundary_underlyingExtensionClass_eq_obstruction_pushout`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/FlatThickeningBoundaryPushout.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/FlatThickeningBoundaryPushout.lean#L221). The attribute's comment: “the tag's own statement, at the two lifts the source names: the trivial extension of 08MI for π^*ℱ and the 08MJ pushout of ℱ'₂ for h^*ℱ'₂. UNCONDITIONAL on Stacks 08MQ: this declaration assumes none of 08MQ's consequences. All of them that it needs are proved and supplied -- `IsIdealTensorShortExact` by `FirstOrderThickeningComplex.isIdealTensorShortExact`, `IsFlatOfFixedActionIdentity` by `isFlatOfFixedActionIdentity`, `IsFlatLiftCorrespondence` by `isFlatLiftCorrespondence`, and `IsIdealComparisonIsoOfFlat` by `isIdealComparisonIsoOfFlat`. `IsIdealTensorShortExact` was FALSE as first stated -- refuted -- and is repaired with Situation 08VX's two horizontal squares, which its proof consumes twice each. The general form `boundary_underlyingExtensionClass_eq_obstruction` in `FlatThickeningBoundary.lean` still carries the binders, because the producer's module imports that file and discharging there would cycle; coefficients are written through the ideals Iₖ, which are f^*𝒥ₖ by 08MQ.”.

> **Stacks Project, Tag 08VY.** In Situation 08VX the modules `π^*ℱ` and `h^*ℱ'₂` are
> `O'₁`-modules flat over `O_{ℬ'₁}` restricting to `ℱ` on `(Sh(C), O)`. Their difference
> (Stacks 08VW) is an element `θ` of `Ext¹_O(ℱ, f^*𝒥₁ ⊗_O ℱ)` whose boundary in
> `Ext²_O(ℱ, f^*𝒥₃ ⊗_O ℱ)` equals the obstruction (Stacks 08VW) to lifting `ℱ` to an `O'₃`-module
> flat over `O_{ℬ'₃}`.
>
> This is
> `Deformation.ToposThickening.FirstOrderThickeningComplex`
> `.boundary_underlyingExtensionClass_eq_obstruction'` at the two lifts of the source: `π^*ℱ` is the
> trivial extension of Stacks 08MI attached to the canonical splitting `π`, and `h^*ℱ'₂` is the
> extension `S.coefficientExtensionOne` that Stacks 08MJ produces from `ℱ'₂`, which receives from
> `ℱ'₂` the canonical map `S.coefficientComparisonMap` satisfying the pushout identities. The
> seven clauses of the conclusion are, in order: the canonical action map of `h^*ℱ'₂` and of
> `π^*ℱ` is the identity, so the kernel of each of `h^*ℱ'₂ ⟶ ℱ` and `π^*ℱ ⟶ ℱ` is
> `I₁ ⊗_O ℱ = f^*𝒥₁ ⊗_O ℱ` and each restricts to `ℱ`; each of `π^*ℱ` and `h^*ℱ'₂` is flat over
> `O_{ℬ'₁}`; the class `θ = ξ_{h^*ℱ'₂}` is the difference of the two lifts under the bijection
> `ℱ' ↦ ξ_{ℱ'}` of Stacks 08MI; the obstruction class is, by Stacks 08VW for the third column, the
> obstruction to lifting `ℱ` to an `O'₃`-module flat over `O_{ℬ'₃}`; and the boundary of `θ` for
> the coefficient sequence equals that obstruction class.
>
> See the implementation notes for the two readings inherited from the general form: the
> coefficient modules are written through the ideals `Iₖ`, which are `f^*𝒥ₖ` by Stacks 08MQ, and
> every consequence of Stacks 08MQ that the proof consumes is now supplied rather than
> assumed: this statement carries no stand-in hypothesis.

```lean
theorem boundary_underlyingExtensionClass_eq_obstruction_pushout
    [HasExt.{e} (SheafOfModules.{max v₂ u₂} (Stacks.SheafOfModules.Tensor.ringSheaf (baseRing i)))]
    [HasExt.{e} (SheafOfModules.{max v₂ u₂} (Stacks.SheafOfModules.Tensor.ringSheaf Y.O))]
    [HasExt.{e} (SheafOfModules.{max v₂ u₂} (Stacks.SheafOfModules.Tensor.ringSheaf S.O₃))]
    (hS : S.IsComplex) (hT : T.IsComplex)
    (hTSE : (ShortComplex.mk T.idealMap₃₂ T.idealMap₂₁ hT).ShortExact)
    (π : Trivialization i)
    (hπ : S.upper.ringMapH ≫ S.lower.ringMapH =
      S.whole.ringMap₂ ≫ splittingRingHom i S.lower.first π)
    (hstrict₁ : (MorphismOfThickenings.ofFirstOrderThickenings i t f f₁
      S.lower.first T.lower.first commf₁).IsStrict)
    (hstrict₂ : (MorphismOfThickenings.ofFirstOrderThickenings
      (reshapeHom i S.lower.O₂ S.lower.fSharp₂) (reshapeHom t T.lower.O₂ T.lower.fSharp₂) f f₂
      S.lower.second T.lower.second commf₂).IsStrict)
    (hstrict₃ : (MorphismOfThickenings.ofFirstOrderThickenings S.thirdHom T.thirdHom f f₃
      S.third T.third commf₃).IsStrict)
    (hf₁ : f₁.IsFlat) (hf₂ : f₂.IsFlat) (hf₃ : f₃.IsFlat)
    (commh : f₂.comp S.lowerHorizontalHom = T.lowerHorizontalHom.comp f₁)
    (commh₃₂ : f₃.comp S.upperHorizontalHom = T.upperHorizontalHom.comp f₂)
    (hF : IsFlatOverBase i f F) :
    (extensionActionMap S.lower.first (S.coefficientExtensionOne F E₂ hE₂)).1 =
        𝟙 (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj F).obj
            S.lower.first.I) ∧
      (extensionActionMap S.lower.first (trivialExtension S.lower.first π F
          (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj F).obj S.lower.first.I)
          (𝟙 (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj F).obj
              S.lower.first.I)))).1 =
        𝟙 (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj F).obj
            S.lower.first.I) ∧
      AlgebraicGeometry.SheafOfModules.IsFlat
          ((SheafOfModules.restrictScalars
            ((sheafCompose Y.J (forget₂ CommRingCat.{max v₂ u₂} RingCat.{max v₂ u₂})).map
              f₁.fSharpInverseImage)).obj
            (trivialExtension S.lower.first π F
              (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj F).obj
                  S.lower.first.I)
              (𝟙 (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj F).obj
                  S.lower.first.I))).Z.left) ∧
      AlgebraicGeometry.SheafOfModules.IsFlat
          ((SheafOfModules.restrictScalars
            ((sheafCompose Y.J (forget₂ CommRingCat.{max v₂ u₂} RingCat.{max v₂ u₂})).map
              f₁.fSharpInverseImage)).obj (S.coefficientExtensionOne F E₂ hE₂).Z.left) ∧
      underlyingExtensionClass.{e} i S.lower.first π F
            (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj F).obj
                S.lower.first.I)
            (S.coefficientExtensionOne F E₂ hE₂) =
          splitRestrictionExtHom.{e} S.lower.first π F
              (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj F).obj
                  S.lower.first.I)
              (extensionClass.{_, _, _, _, _, _, e} F
                (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj F).obj
                    S.lower.first.I)
                (S.coefficientExtensionOne F E₂ hE₂)) -
            splitRestrictionExtHom.{e} S.lower.first π F
              (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj F).obj
                  S.lower.first.I)
              (extensionClass.{_, _, _, _, _, _, e} F
                (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj F).obj
                    S.lower.first.I)
                (trivialExtension S.lower.first π F
                  (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj F).obj
                      S.lower.first.I)
                  (𝟙 (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj F).obj
                      S.lower.first.I)))) ∧
      (HasFlatLift S.thirdHom f₃ S.third F ↔
          existenceObstructionClass S.third F
              (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj F).obj S.third.I)
              (𝟙 (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj F).obj
                  S.third.I)) = 0) ∧
      (underlyingExtensionClass.{e} i S.lower.first π F
            (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj F).obj
                S.lower.first.I)
            (S.coefficientExtensionOne F E₂ hE₂)).comp
          (S.isIdealTensorShortExact T hS f f₁ f₂ f₃ commf₁ commf₂ commf₃ F
            hT hTSE hF hstrict₁ hstrict₂ hstrict₃ hf₁ hf₂ hf₃ commh commh₃₂).extClass
          (by decide) =
        existenceObstructionClass S.third F
          (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj F).obj S.third.I)
          (𝟙 (((Stacks.SheafOfModules.Tensor.sheafTensor (baseRing i)).flip.obj F).obj
            S.third.I))
```

**`Deformation.ToposThickening.FlatThickeningComplexSituation.boundary_difference_trivialLift_pulledLift_eq_obstruction`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Deformation/ToposThickening/FlatThickeningComplexBoundaryObstruction.lean, line 227](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Deformation/ToposThickening/FlatThickeningComplexBoundaryObstruction.lean#L227).

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
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
