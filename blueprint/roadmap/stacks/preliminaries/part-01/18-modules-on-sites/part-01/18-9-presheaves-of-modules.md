---
declaration: section
origin: cited
lean: PresheafOfModules, PresheafOfModules.Hom, PresheafOfModules.instCategory, Stacks.PresheafOfModules.ChangeOfRings.homEquivCore, Stacks.PresheafOfModules.ChangeOfRings.changeOfRingsAdjunction
statement: formalized
proof: formalized
---

# 18.9 Presheaves of modules

Section 18.9 of the Stacks Project, [Tag 03CS](https://stacks.math.columbia.edu/tag/03CS). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 03CT, a definition

[Tag 03CT](https://stacks.math.columbia.edu/tag/03CT) in the Stacks Project.

Declarations registered for the tag:

- [`PresheafOfModules`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch18.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch18.lean#L49) (StacksFrontier): “(1) presheaf of O-modules”. References: SGA 3 I (4.7.1.1); SGA 4 II (6.7); SGA 3 I (3.1), “O-module definition”.
- [`PresheafOfModules.Hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.Hom#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch18.lean, line 50](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch18.lean#L50) (StacksFrontier): “(2) and (3) morphisms of presheaves of O-modules”. References: SGA 3 I (3.1), “Hom\_O(F,F')”.
- [`PresheafOfModules.instCategory`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.instCategory#doc) registered with `add_to_stacks` in [StacksFrontier/MathlibRegistrations/Ch18.lean, line 51](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/MathlibRegistrations/Ch18.lean#L51) (StacksFrontier): “(4) the category PMod(O)”. References: SGA 3 I (3.1), “category (O-Mod.)”.

## Tag 03CU, a lemma

[Tag 03CU](https://stacks.math.columbia.edu/tag/03CU) in the Stacks Project.

**`Stacks.PresheafOfModules.ChangeOfRings.homEquivCore`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/ChangeOfRingsAdjunction.lean, line 535](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/ChangeOfRingsAdjunction.lean#L535). The attribute's comment: “the canonical bijection of Hom-sets”.

> **The canonical bijection of Tag 03CU.**
>
> For `θ : O₁ ⟶ O₂` a morphism of presheaves of commutative rings, `G` a presheaf of
> `O₁`-modules and `F` a presheaf of `O₂`-modules, the bijection
> `Hom_{O₂}(O₂ ⊗_{p,O₁} G, F) ≃ Hom_{O₁}(G, F_{O₁})`.
>
> It sends `ψ` to `x ↦ ψ_X(1 ⊗ x)` and its inverse sends `φ` to `a ⊗ x ↦ a • φ_X(x)`;
> objectwise these are the two directions of the ring-theoretic extension/restriction of
> scalars bijection `ModuleCat.extendRestrictScalarsAdj`.

```lean
noncomputable def homEquivCore (θ : O₁ ⟶ O₂) (G : PMod O₁) (F : PMod O₂) :
    ((changeOfRings θ).obj G ⟶ F) ≃ (G ⟶ (restrictScalars θ).obj F)
```

**`Stacks.PresheafOfModules.ChangeOfRings.changeOfRingsAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Presheaf/ChangeOfRingsAdjunction.lean, line 577](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Algebra/Category/ModuleCat/Presheaf/ChangeOfRingsAdjunction.lean#L577). The attribute's comment: “the adjunction: restriction and change of rings are adjoint”.

> **Main statement of Tag 03CU.**
>
> The change-of-rings functor is left adjoint to restriction of scalars,
> `changeOfRings θ ⊣ restrictScalars θ`.  It is obtained from the bijection
> `homEquivCore`, which it exhibits as natural in both variables.
>
> The unit is `unitHom θ (𝟙 _)`, so it is `x ↦ 1 ⊗ x` on sections; see
> `changeOfRingsAdjunction_unit_app_apply`.

```lean
noncomputable def changeOfRingsAdjunction (θ : O₁ ⟶ O₂) :
    changeOfRings θ ⊣ restrictScalars θ
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 18.9, Tag 03CS](https://stacks.math.columbia.edu/tag/03CS)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
