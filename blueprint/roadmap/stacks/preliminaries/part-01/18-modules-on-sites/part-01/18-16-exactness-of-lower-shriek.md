---
declaration: section
origin: cited
lean: CategoryTheory.Functor.lan, CategoryTheory.Functor.sheafPullbackConstruction.sheafPullback, CategoryTheory.Functor.lanAdjunction, CategoryTheory.Functor.sheafAdjunctionContinuous, CategoryTheory.Functor.sheafPullback, CategoryTheory.Functor.sheafPullbackConstruction.sheafAdjunctionContinuous, Stacks.Sites.LowerShriek.gShriek_preservesFiniteLimits, Stacks.Sites.LowerShriek.gShriek_preservesFiniteColimits
statement: formalized
proof: formalized
---

# 18.16 Exactness of lower shriek

Section 18.16 of the Stacks Project, [Tag 04BE](https://stacks.math.columbia.edu/tag/04BE). 6 tags here are carried by 12 declarations of the repository (all in StacksFrontier) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 04BF, a definition

[Tag 04BF](https://stacks.math.columbia.edu/tag/04BF) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.lan`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.lan#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Pullback.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Pullback.lean#L80) (StacksFrontier): “g_{p!} = u_p, the left Kan extension along `u.op`”.
- [`CategoryTheory.Functor.sheafPullbackConstruction.sheafPullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.sheafPullbackConstruction.sheafPullback#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Pullback.lean, line 82](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Pullback.lean#L82) (StacksFrontier): “g_! F = (g_{p!} F)^#”.

## Tag 04BG, a lemma

[Tag 04BG](https://stacks.math.columbia.edu/tag/04BG) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.lanAdjunction`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.lanAdjunction#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Pullback.lean, line 71](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Pullback.lean#L71) (StacksFrontier): “(1) g_p! ⊣ u^p”. References: SGA 4 IV (4.6.1), “partial”.
- [`CategoryTheory.Functor.sheafAdjunctionContinuous`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.sheafAdjunctionContinuous#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Pullback.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Pullback.lean#L72) (StacksFrontier): “(2) g_! ⊣ g^{-1}”.
- [`CategoryTheory.Functor.sheafPullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.sheafPullback#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Pullback.lean, line 73](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Pullback.lean#L73) (StacksFrontier): “g_!”.
- [`CategoryTheory.Functor.sheafPullbackConstruction.sheafAdjunctionContinuous`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.sheafPullbackConstruction.sheafAdjunctionContinuous#doc) registered with `add_to_stacks` in [StacksFrontier/CategoryTheory/Sites/Pullback.lean, line 74](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Pullback.lean#L74) (StacksFrontier): “(2) g_! = (g_p! -)^#”. References: SGA 4 III (1.3), “more general”; SGA 4 III (2.6); SGA 4 IV (4.7), “partial”; SGA 4 IV (4.9.1), “partial”; SGA 4 VI (7.4.13.4).

## Tag 04BH, a lemma

[Tag 04BH](https://stacks.math.columbia.edu/tag/04BH) in the Stacks Project.

**`Stacks.Sites.LowerShriek.gShriek_preservesFiniteLimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekExactness.lean, line 115](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekExactness.lean#L115). The attribute's comment: “preservation of finite limits”. References: SGA 4 III (1.3), “5), Ab-valued”.

> If a continuous functor between sites has a source with fibre products and equalizers which
> it preserves, then lower shriek on abelian sheaves preserves finite limits.

```lean
public theorem gShriek_preservesFiniteLimits
    {C : Type uC} [Category.{vC} C] {D : Type uD} [Category.{vD} D]
    (u : C ⥤ D) (J : GrothendieckTopology C) (K : GrothendieckTopology D)
    [u.IsContinuous J K]
    [HasPullbacks C] [HasEqualizers C]
    [PreservesLimitsOfShape WalkingCospan u]
    [PreservesLimitsOfShape WalkingParallelPair u]
    [∀ F : Cᵒᵖ ⥤ Ab.{w}, u.op.HasPointwiseLeftKanExtension F]
    [HasSheafify K Ab.{w}] :
    PreservesFiniteLimits
      (Functor.sheafPullbackConstruction.sheafPullback u Ab.{w} J K)
```

**`Stacks.Sites.LowerShriek.gShriek_preservesFiniteColimits`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekExactness.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekExactness.lean#L135). The attribute's comment: “preservation of finite colimits”. References: SGA 4 III (1.3), “4), finite colimits”.

> Lower shriek along a continuous functor `u` preserves finite colimits, for sheaves valued in
> any category `A` for which the left Kan extensions along `u.op` and weak sheafification on the
> target site exist.

```lean
public theorem gShriek_preservesFiniteColimits
    {C : Type uC} [Category.{vC} C] {D : Type uD} [Category.{vD} D]
    (A : Type uA) [Category.{vA} A]
    (u : C ⥤ D) (J : GrothendieckTopology C) (K : GrothendieckTopology D)
    [u.IsContinuous J K]
    [∀ F : Cᵒᵖ ⥤ A, u.op.HasLeftKanExtension F]
    [HasWeakSheafify K A] :
    PreservesFiniteColimits
      (Functor.sheafPullbackConstruction.sheafPullback u A J K)
```

**`Stacks.Sites.LowerShriek.gShriek_preservesFiniteLimits_module`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekModuleExactness.lean, line 121](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekModuleExactness.lean#L121). The attribute's comment: “preservation of finite limits, module coefficients”.

> **Stacks 04BH for module coefficients.** If a continuous functor between sites has a source
> with fibre products and equalizers which it preserves, then lower shriek on sheaves of
> `R`-modules preserves finite limits. Being a left adjoint it preserves finite colimits, so it is
> exact.

```lean
public theorem gShriek_preservesFiniteLimits_module
    {C : Type uC} [Category.{vC} C] {D : Type uD} [Category.{vD} D]
    (u : C ⥤ D) (R : Type r) [Ring R]
    (J : GrothendieckTopology C) (K : GrothendieckTopology D)
    [u.IsContinuous J K]
    [UnivLE.{max uC uD, w}] [UnivLE.{max vC vD, w}] [UnivLE.{max uC vD, w}]
    [HasPullbacks C] [HasEqualizers C]
    [PreservesLimitsOfShape WalkingCospan u]
    [PreservesLimitsOfShape WalkingParallelPair u]
    [∀ F : Cᵒᵖ ⥤ ModuleCat.{w} R, u.op.HasPointwiseLeftKanExtension F]
    [HasSheafify K (ModuleCat.{w} R)] :
    PreservesFiniteLimits
      (Functor.sheafPullbackConstruction.sheafPullback u (ModuleCat.{w} R) J K)
```

## Tag 077I, a lemma

[Tag 077I](https://stacks.math.columbia.edu/tag/077I) in the Stacks Project.

**`stacks077I_counit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekFullyFaithful.lean, line 211](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekFullyFaithful.lean#L211). The attribute's comment: “counit”. References: SGA 4 III (2.6), “u ff ⇒ u_* ff, abelian”.

> If `u : C ⥤ D` is continuous, cocontinuous and fully faithful, then for every abelian sheaf
> `F` on `C` the counit `ε_F : g⁻¹ (g_* F) → F` of the adjunction `g⁻¹ ⊣ g_*` is an isomorphism.

```lean
theorem stacks077I_counit_isIso
    [u.IsContinuous J K] [u.IsCocontinuous J K] [u.Full] [u.Faithful]
    (F : Sheaf J (AbCat.{v₁, u₁})) :
    IsIso ((adjStar u J K).counit.app F)
```

**`stacks077I_unit_isIso`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekFullyFaithful.lean, line 221](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekFullyFaithful.lean#L221). The attribute's comment: “unit”. References: SGA 4 III (2.6), “u ff ⇒ u_! ff, abelian”; SGA 4 VII (4.1), “Clause (i)”.

> If `u : C ⥤ D` is continuous, cocontinuous and fully faithful, then for every abelian sheaf
> `F` on `C` the unit `η_F : F → g⁻¹ (g_! F)` of the adjunction `g_! ⊣ g⁻¹` is an isomorphism.

```lean
theorem stacks077I_unit_isIso
    [u.IsContinuous J K] [u.IsCocontinuous J K] [u.Full] [u.Faithful]
    (F : Sheaf J (AbCat.{v₁, u₁})) :
    IsIso ((adjShriek u J K).unit.app F)
```

## Tag 04BI, a remark

[Tag 04BI](https://stacks.math.columbia.edu/tag/04BI) in the Stacks Project.

**`Stacks.ChangeOfRings.hasRightAdjoint_extendScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/ExtendScalarsNoLeftAdjoint.lean, line 56](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/ExtendScalarsNoLeftAdjoint.lean#L56). The attribute's comment: “base change has a right adjoint, namely restriction of scalars”.

> Base change `M ↦ S ⊗_R M` along a ring map `f : R →+* S` always has a right adjoint, namely
> restriction of scalars along `f`.

```lean
theorem hasRightAdjoint_extendScalars :
    (ModuleCat.extendScalars.{u₁, u₂, max v u₂} f).IsLeftAdjoint
```

**`Stacks.ChangeOfRings.flat_of_isRightAdjoint_extendScalars`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/ExtendScalarsNoLeftAdjoint.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/ExtendScalarsNoLeftAdjoint.lean#L78). The attribute's comment: “a left adjoint of base change forces flatness”.

> If base change `M ↦ S ⊗_R M` along a ring map `f : R →+* S` has a left adjoint, then `f` is
> flat.

```lean
theorem flat_of_isRightAdjoint_extendScalars [Small.{v} R]
    (h : (ModuleCat.extendScalars.{u₁, u₂, v} f).IsRightAdjoint) : f.Flat
```

**`Stacks.ChangeOfRings.not_isRightAdjoint_extendScalars_zmodTwo`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/ExtendScalarsNoLeftAdjoint.lean, line 100](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/ExtendScalarsNoLeftAdjoint.lean#L100). The attribute's comment: “no left adjoint in general”.

> Base change `M ↦ ℤ/2ℤ ⊗_ℤ M` along the ring map `ℤ → ℤ/2ℤ` has no left adjoint.

```lean
theorem not_isRightAdjoint_extendScalars_zmodTwo :
    ¬ (ModuleCat.extendScalars.{0, 0, v} (Int.castRingHom (ZMod 2))).IsRightAdjoint
```

Declarations registered for the tag:

- [`ModuleCat.extendRestrictScalarsAdj`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=ModuleCat.extendRestrictScalarsAdj#doc) registered with `add_to_stacks` in [StacksFrontier/Algebra/Category/ModuleCat/ExtendScalarsNoLeftAdjoint.lean, line 60](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/ExtendScalarsNoLeftAdjoint.lean#L60) (StacksFrontier): “the right adjoint of base change is restriction of scalars, as an adjunction”.

## Tag 08P3, a lemma

[Tag 08P3](https://stacks.math.columbia.edu/tag/08P3) in the Stacks Project.

**`Stacks.Sites.LowerShriek.lowerShriek_comp_forget_iso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekOfLeftAdjoint.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekOfLeftAdjoint.lean#L119). The attribute's comment: “part (1), compatibility with underlying sheaves of sets”.

> **Stacks 08P3 (1), compatibility with underlying sheaves.** When `G` has a left adjoint,
> lower shriek on abelian sheaves agrees naturally, on underlying sheaves of sets, with lower
> shriek on sheaves of sets.

```lean
noncomputable def lowerShriek_comp_forget_iso [G.IsRightAdjoint] :
    Functor.sheafPullbackConstruction.sheafPullback G AddCommGrpCat.{max u₂ v₂} J K ⋙
          sheafCompose K (forget AddCommGrpCat.{max u₂ v₂}) ≅
        sheafCompose J (forget AddCommGrpCat.{max u₂ v₂}) ⋙
        Functor.sheafPullbackConstruction.sheafPullback G (Type (max u₂ v₂)) J K
```

**`Stacks.Sites.LowerShriek.lowerShriek_iso_sheafPullbackCocontinuous`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekOfLeftAdjoint.lean, line 161](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekOfLeftAdjoint.lean#L161). The attribute's comment: “part (2), lower shriek equals inverse image”.

> **Stacks 08P3 (2), the lower shriek.** If the left adjoint `W` is cocontinuous, lower
> shriek along `G` is naturally isomorphic to the inverse-image functor associated to `W`.

```lean
noncomputable def lowerShriek_iso_sheafPullbackCocontinuous [G.IsRightAdjoint]
    [W.IsCocontinuous K J] (adj : W ⊣ G) :
    Functor.sheafPullbackConstruction.sheafPullback G AddCommGrpCat.{max u₂ v₂} J K ≅
      W.sheafPullbackCocontinuous AddCommGrpCat.{max u₂ v₂} K J
```

**`Stacks.Sites.LowerShriek.sheafPushforwardContinuous_iso_sheafPushforwardCocontinuous`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekOfLeftAdjoint.lean, line 174](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekOfLeftAdjoint.lean#L174). The attribute's comment: “part (2), inverse image equals direct image”.

> **Stacks 08P3 (2), the inverse image.** If the left adjoint `W` is cocontinuous, inverse
> image along `G` is naturally isomorphic to the direct-image functor associated to `W`.

```lean
noncomputable def sheafPushforwardContinuous_iso_sheafPushforwardCocontinuous [W.IsLeftAdjoint]
    [W.IsCocontinuous K J] (adj : W ⊣ G) :
    G.sheafPushforwardContinuous AddCommGrpCat.{max u₂ v₂} J K ≅
      W.sheafPushforwardCocontinuous AddCommGrpCat.{max u₂ v₂} K J
```

**`Stacks.Sites.LowerShriek.lowerShriek_exact`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekOfLeftAdjoint.lean, line 184](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/CategoryTheory/Sites/Cocontinuous/LowerShriekOfLeftAdjoint.lean#L184). The attribute's comment: “part (1), exactness”.

> **Stacks 08P3 (1), exactness.** The lower-shriek functor on abelian sheaves associated to
> `G` is exact.

```lean
theorem lowerShriek_exact [G.IsRightAdjoint] :
    exactFunctor (Sheaf J AddCommGrpCat.{max u₂ v₂}) (Sheaf K AddCommGrpCat.{max u₂ v₂})
      (Functor.sheafPullbackConstruction.sheafPullback G AddCommGrpCat.{max u₂ v₂} J K)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.16, Tag 04BE](https://stacks.math.columbia.edu/tag/04BE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
