---
declaration: section
origin: cited
lean: PresheafOfModules, PresheafOfModules.instModuleCarrierObjOppositeRingCatCarrierAbPresheaf, PresheafOfModules.Hom, PresheafOfModules.Hom.naturality, PresheafOfModules.instCategory, Stacks.Sheafify.ChangeOfRingsAdjunction.tensorPresheafHomEquiv, Stacks.Sheafify.ChangeOfRingsAdjunction.tensorPresheafAdjunction
statement: formalized
proof: formalized
---

# 6.6 Presheaves of modules

Section 6.6 of the Stacks Project, [Tag 006P](https://stacks.math.columbia.edu/tag/006P). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 006Q, a definition

[Tag 006Q](https://stacks.math.columbia.edu/tag/006Q) in the Stacks Project.

Declarations registered for the tag:

- [`PresheafOfModules`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/Module.lean, line 29](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Presheaf/Module.lean#L29) (StacksFrontier): “a presheaf of `O`-modules: an abelian presheaf with an `O(U)`-module structure on each `F(U)`, compatible with restriction”. References: SGA 3 I (4.7.1.1); SGA 4 II (6.7); SGA 3 I (3.1), “O-module definition”.
- [`PresheafOfModules.instModuleCarrierObjOppositeRingCatCarrierAbPresheaf`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.instModuleCarrierObjOppositeRingCatCarrierAbPresheaf#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/Module.lean, line 34](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Presheaf/Module.lean#L34) (StacksFrontier): “the `O(U)`-module structure on the sections over `U`”. References: SGA 3 I (3.1), “F(S) is an O(S)-module”.
- [`PresheafOfModules.Hom`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.Hom#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/Module.lean, line 38](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Presheaf/Module.lean#L38) (StacksFrontier): “a morphism of presheaves of `O`-modules; also the hom-set `Hom_O(F, G)`, which is the hom-type of `PMod(O)`”. References: SGA 3 I (3.1), “Hom\_O(F,F')”.
- [`PresheafOfModules.Hom.naturality`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.Hom.naturality#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/Module.lean, line 41](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Presheaf/Module.lean#L41) (StacksFrontier): “the compatibility square of a morphism with the actions, via restriction of scalars along `O(U) → O(V)`”. References: SGA 3 I (3.1), “morphism compatibility”.
- [`PresheafOfModules.instCategory`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.instCategory#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Presheaf/Module.lean, line 44](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Presheaf/Module.lean#L44) (StacksFrontier): “the category `PMod(O)`”. References: SGA 3 I (3.1), “category (O-Mod.)”.

## Tag 006R, a lemma

[Tag 006R](https://stacks.math.columbia.edu/tag/006R) in the Stacks Project.

**`Stacks.Sheafify.ChangeOfRingsAdjunction.tensorPresheafHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/ModuleChangeOfRingsSheaf.lean, line 157](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Sheafify/ModuleChangeOfRingsSheaf.lean#L157). The attribute's comment: “hom-set bijection `Hom_{O'}(O' ⊗_{p,O} G, F) ≃ Hom_O(G, F_O)` on the explicit sectionwise tensor product presheaf, presheaves on a topological space; natural in both variables via `tensorPresheafAdjunction`”.

> **The universal property of the tensor product presheaf.** For presheaves of commutative rings
> `α : O ⟶ O'` on `X`, a presheaf of `O`-modules `F` and a presheaf of `O'`-modules `M`, the
> morphisms `O' ⊗_{p,O} F ⟶ M` of presheaves of `O'`-modules are in canonical bijection with the
> morphisms `F ⟶ M_O` of presheaves of `O`-modules. The bijection sends `Φ` to `m ↦ Φ(1 ⊗ m)` and its
> inverse sends `g` to the sectionwise lift `s ⊗ m ↦ s • g(m)`. This is Stacks 006R
> (Lemma 6.6.2); the bijection is natural in both variables, being the hom-set bijection of the
> adjunction `tensorPresheafAdjunction`.

```lean
noncomputable def tensorPresheafHomEquiv :
    (tensorPresheafOfModules O O' α F ⟶ M) ≃ (F ⟶ restrictPresheaf O O' α M)
```

**`Stacks.Sheafify.ChangeOfRingsAdjunction.tensorPresheafAdjunction`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/ModuleChangeOfRingsSheaf.lean, line 228](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Topology/Sheaves/Sheafify/ModuleChangeOfRingsSheaf.lean#L228). The attribute's comment: “adjunction form: `O' ⊗_{p,O} (-) ⊣ (-)_O` on the explicit sectionwise tensor product presheaf `U ↦ O'(U) ⊗_{O(U)} G(U)`, presheaves on a topological space; its hom-set bijection is `tensorPresheafHomEquiv`”.

> **Stacks 006R (Lemma 6.6.2), adjunction form.** For a morphism `α : O ⟶ O'` of presheaves of
> commutative rings on a topological space `X`, the change of rings functor
> `O' ⊗_{p,O} (-) : PMod(O) ⥤ PMod(O')` on the sectionwise tensor product presheaf is left adjoint
> to restriction of scalars `(-)_O : PMod(O') ⥤ PMod(O)`. Its hom-set bijection is
> `tensorPresheafHomEquiv` (`tensorPresheafAdjunction_homEquiv`).

```lean
noncomputable def tensorPresheafAdjunction :
    tensorPresheafFunctor O O' α ⊣ PresheafOfModules.restrictScalars (ringPresheafMap O O' α)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.6, Tag 006P](https://stacks.math.columbia.edu/tag/006P)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
