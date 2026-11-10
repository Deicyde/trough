---
declaration: section
origin: cited
lean: PresheafOfModules, PresheafOfModules.instModuleCarrierObjOppositeRingCatCarrierAbPresheaf, PresheafOfModules.Hom, PresheafOfModules.Hom.naturality, PresheafOfModules.instCategory, tensorPresheafAdj, tensorHomEquiv
statement: formalized
proof: formalized
---

# 6.6 Presheaves of modules

Section 6.6 of the Stacks Project, [Tag 006P](https://stacks.math.columbia.edu/tag/006P). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 006Q, a definition

[Tag 006Q](https://stacks.math.columbia.edu/tag/006Q) in the Stacks Project.

Declarations registered for the tag:

- [`PresheafOfModules`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/Module.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/Module.lean#L29) (StacksFrontier): “a presheaf of `O`-modules: an abelian presheaf with an `O(U)`-module structure on each `F(U)`, compatible with restriction”. References: SGA 3 I (4.7.1.1); SGA 4 II (6.7); SGA 3 I (3.1), “O-module definition”.
- [`PresheafOfModules.instModuleCarrierObjOppositeRingCatCarrierAbPresheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.instModuleCarrierObjOppositeRingCatCarrierAbPresheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/Module.lean, line 34](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/Module.lean#L34) (StacksFrontier): “the `O(U)`-module structure on the sections over `U`”. References: SGA 3 I (3.1), “F(S) is an O(S)-module”.
- [`PresheafOfModules.Hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.Hom#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/Module.lean, line 38](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/Module.lean#L38) (StacksFrontier): “a morphism of presheaves of `O`-modules; also the hom-set `Hom_O(F, G)`, which is the hom-type of `PMod(O)`”. References: SGA 3 I (3.1), “Hom_O(F,F')”.
- [`PresheafOfModules.Hom.naturality`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.Hom.naturality#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/Module.lean, line 41](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/Module.lean#L41) (StacksFrontier): “the compatibility square of a morphism with the actions, via restriction of scalars along `O(U) → O(V)`”. References: SGA 3 I (3.1), “morphism compatibility”.
- [`PresheafOfModules.instCategory`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.instCategory#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/Module.lean, line 44](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/Module.lean#L44) (StacksFrontier): “the category `PMod(O)`”. References: SGA 3 I (3.1), “category (O-Mod.)”.

## Tag 006R, a lemma

[Tag 006R](https://stacks.math.columbia.edu/tag/006R) in the Stacks Project.

**`tensorPresheafAdj`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Presheaf/ModuleChangeOfRings.lean, line 143](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/ModuleChangeOfRings.lean#L143).

> **Stacks Project, tag 006R (Lemma 6.6.2), adjunction form.**
>
> Given a morphism `α : 𝒪₁ ⟶ 𝒪₂` of presheaves of commutative rings on a small
> category `C`, the change-of-rings functor `tensorPresheaf α = 𝒪₂ ⊗_{p, 𝒪₁} (-)`
> is left adjoint to the restriction-of-scalars functor
> `restrictionFunctor α = (-)_{𝒪₁}`.
>
> This is the *canonical adjunction* asserted by Lemma 6.6.2. It is provided by
> Mathlib's `PresheafOfModules.pullbackPushforwardAdjunction`, specialised to
> `F = 𝟭 C`.

```lean
noncomputable def tensorPresheafAdj
    {𝒪₁ 𝒪₂ : Cᵒᵖ ⥤ CommRingCat.{u}} (α : 𝒪₁ ⟶ 𝒪₂) :
    PresheafOfModules.pullback.{u} (F := 𝟭 C) (toRingCatMap α) ⊣
      PresheafOfModules.pushforward.{u} (F := 𝟭 C) (toRingCatMap α)
```

**`tensorHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Presheaf/ModuleChangeOfRings.lean, line 156](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Presheaf/ModuleChangeOfRings.lean#L156).

> **Stacks Project, tag 006R, hom-set bijection form.**
>
> The canonical bijection
> `Hom_{𝒪₂}(𝒪₂ ⊗_{p, 𝒪₁} 𝒢, ℱ) ≃ Hom_{𝒪₁}(𝒢, ℱ_{𝒪₁})`,
> which is the hom-set bijection of the adjunction `tensorPresheafAdj`. By
> construction, this bijection is natural in both variables `𝒢` and `ℱ`.

```lean
noncomputable def tensorHomEquiv
    {𝒪₁ 𝒪₂ : Cᵒᵖ ⥤ CommRingCat.{u}} (α : 𝒪₁ ⟶ 𝒪₂)
    (𝒢 : PModuleStruct 𝒪₁) (ℱ : PModuleStruct 𝒪₂) :
    ((tensorPresheaf α).obj 𝒢 ⟶ ℱ) ≃ (𝒢 ⟶ (restrictionFunctor α).obj ℱ)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.6, Tag 006P](https://stacks.math.columbia.edu/tag/006P)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
