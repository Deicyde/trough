---
declaration: section
origin: cited
lean: Stacks.Sheaves.ToposPushforward.pushforwardModule, Stacks.Sheaves.ToposPullback.pullbackModule, Stacks.Sheaves.RingedToposModules.toposModulesHomEquiv, Stacks.Sheaves.RingedToposModules.inverseImageAdjDirectImageModules, Stacks.Sheaves.RingedToposModules.tensorInverseImageAdjDirectImageModules, Stacks.Sheaves.RingedToposModules.adjointPullPushModulesHomEquiv
statement: formalized
proof: formalized
---

# 18.12 Morphisms of topoi and sheaves of modules

Section 18.12 of the Stacks Project, [Tag 03D0](https://stacks.math.columbia.edu/tag/03D0). 4 tags here are carried by 6 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03D1, a lemma

[Tag 03D1](https://stacks.math.columbia.edu/tag/03D1) in the Stacks Project.

**`Stacks.Sheaves.ToposPushforward.pushforwardModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ToposPushforward.lean, line 1020](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ToposPushforward.lean#L1020).

> **Stacks 03D1.** The direct image of a sheaf of `O`-modules under a morphism of topoi is
> naturally a sheaf of modules over the direct-image ring, with scalar multiplication the direct
> image of the original scalar multiplication read through the product comparison, and this
> construction is functorial in the module.

```lean
noncomputable def pushforwardModule
    (f : MorphismOfTopoi (Sheaf J (Type ww)) (Sheaf K (Type ww')))
    (O : Sheaf J RingCat.{ww}) : PushforwardModuleData J K f O
```

## Tag 03D2, a lemma

[Tag 03D2](https://stacks.math.columbia.edu/tag/03D2) in the Stacks Project.

**`Stacks.Sheaves.ToposPullback.pullbackModule`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ToposPullback/InverseImage.lean, line 605](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ToposPullback/InverseImage.lean#L605).

> The inverse image of a sheaf of `O`-modules under a morphism of topoi is naturally a sheaf of
> modules over the inverse-image ring, and this construction is functorial in the module.

```lean
noncomputable def pullbackModule
    (f : MorphismOfTopoi (Sheaf J (Type ww)) (Sheaf K (Type ww')))
    (O : Sheaf K RingCat.{ww'}) : PullbackModuleData J K f O
```

## Tag 03D3, a lemma

[Tag 03D3](https://stacks.math.columbia.edu/tag/03D3) in the Stacks Project.

**`Stacks.Sheaves.RingedToposModules.toposModulesHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposModules.lean, line 578](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposModules.lean#L578). The attribute's comment: “the canonical bijection `Hom_{f⁻¹O}(f⁻¹G, F) = Hom_O(G, f_*F)` itself”.

> **Stacks 03D3**: the canonical bijection between morphisms out of an inverse-image sheaf
> of modules and morphisms into the direct image, the latter read as a sheaf of `O`-modules by
> restriction of scalars along the unit `O ⟶ f_*f⁻¹O`.

```lean
noncomputable def toposModulesHomEquiv (G : SheafOfModules.{w'} O)
    (F : SheafOfModules.{w} (inverseImageRingSheaf f O)) :
    ((inverseImageModules f O).obj G ⟶ F) ≃ (G ⟶ (directImageModules f O).obj F)
```

**`Stacks.Sheaves.RingedToposModules.inverseImageAdjDirectImageModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposModules.lean, line 609](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/RingedToposModules.lean#L609). The attribute's comment: “the bijection as an adjunction, hence natural in both variables”.

> **Stacks 03D3** as an adjunction: the inverse image of sheaves of modules along a
> morphism of topoi is left adjoint to the direct image, read as a sheaf of `O`-modules by
> restriction of scalars along the unit `O ⟶ f_*f⁻¹O`.

```lean
noncomputable def inverseImageAdjDirectImageModules :
    inverseImageModules f O ⊣ directImageModules f O
```

## Tag 03D4, a lemma

[Tag 03D4](https://stacks.math.columbia.edu/tag/03D4) in the Stacks Project.

**`Stacks.Sheaves.RingedToposModules.tensorInverseImageAdjDirectImageModules`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ToposModuleAdjointPullPush.lean, line 211](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ToposModuleAdjointPullPush.lean#L211).

> **Stacks 03D4** as an adjunction: for a morphism of topoi `f : Sh(C) ⟶ Sh(D)` and a sheaf
> of rings `O` on `C`, the functor `G ↦ O ⊗_{f⁻¹f_*O} f⁻¹G` from sheaves of `f_*O`-modules to
> sheaves of `O`-modules is left adjoint to the direct image `F ↦ f_*F`.

```lean
noncomputable def tensorInverseImageAdjDirectImageModules :
    tensorInverseImageModules f O ⊣ directImageModulesOverPushforwardRing f O
```

**`Stacks.Sheaves.RingedToposModules.adjointPullPushModulesHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ToposModuleAdjointPullPush.lean, line 219](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ToposModuleAdjointPullPush.lean#L219).

> **Stacks 03D4** as the displayed bijection
> `Mor_{Mod(O)}(O ⊗_{f⁻¹f_*O} f⁻¹G, F) = Mor_{Mod(f_*O)}(G, f_*F)`.

```lean
noncomputable def adjointPullPushModulesHomEquiv
    (G : SheafOfModules.{w'} (pushforwardRingSheaf f O)) (F : SheafOfModules.{u} O) :
    ((tensorInverseImageModules f O).obj G ⟶ F) ≃
      (G ⟶ (directImageModulesOverPushforwardRing f O).obj F)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.12, Tag 03D0](https://stacks.math.columbia.edu/tag/03D0)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
