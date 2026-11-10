---
declaration: section
origin: cited
lean: SheafOfModules.restrictScalars, Stacks.Sheafify.ModuleStalkTensor.tensorSheaf, Stacks.Sheaves.ModuleAdjunction.extendScalars, PresheafOfModules.sheafify, PresheafOfModules.toSheafify, PresheafOfModules.sheafifyHomEquiv, Stacks.Sheafify.ChangeOfRingsAdjunction.tensorSheafHomEquiv, Stacks.Sheafify.ChangeOfRingsAdjunction.nonempty_tensorSheafHomEquiv
statement: formalized
proof: formalized
---

# 6.20 Sheafification of presheaves of modules

Section 6.20 of the Stacks Project, [Tag 0088](https://stacks.math.columbia.edu/tag/0088). 4 tags here are carried by 3 declarations of the repository (all in StacksFrontier) and 6 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0088, the section

[Tag 0088](https://stacks.math.columbia.edu/tag/0088) in the Stacks Project.

Declarations registered for the tag:

- [`SheafOfModules.restrictScalars`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=SheafOfModules.restrictScalars#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheafify/ModuleChangeOfRingsFunctor.lean, line 65](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/ModuleChangeOfRingsFunctor.lean#L65) (StacksFrontier): “the restriction functor `Mod(O₂) ⥤ Mod(O₁)`”. References: SGA 4 IV (11.1.4); SGA 4 IV (11.1.5); SGA 4 IV (13.2.1), “special case”; SGA 4 XVIII (3.1.12.1).
- [`Stacks.Sheafify.ModuleStalkTensor.tensorSheaf`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/ModuleStalkTensor.lean#L1099), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheafify/ModuleChangeOfRingsFunctor.lean, line 72](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/ModuleChangeOfRingsFunctor.lean#L72) (StacksFrontier): “the tensor product sheaf `O₂ ⊗_{O₁} G = (O₂ ⊗_{p,O₁} G)^#`, at the explicit sectionwise model of the presheaf tensor product”.
- [`Stacks.Sheaves.ModuleAdjunction.extendScalars`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/ToposModuleAdjunction.lean#L135), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheafify/ModuleChangeOfRingsFunctor.lean, line 76](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/ModuleChangeOfRingsFunctor.lean#L76) (StacksFrontier): “the change of rings functor `Mod(O₁) ⥤ Mod(O₂)`”.

## Tag 0089, a lemma

[Tag 0089](https://stacks.math.columbia.edu/tag/0089) in the Stacks Project.

Declarations registered for the tag:

- [`PresheafOfModules.sheafify`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.sheafify#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheafify/Module.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/Module.lean#L25) (StacksFrontier): “the sheafification `F^#` as a sheaf of `O^#`-modules”. References: EGA I (1.3.13), “more general”; SGA 4 IV (12.4).
- [`PresheafOfModules.toSheafify`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.toSheafify#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheafify/Module.lean, line 29](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/Module.lean#L29) (StacksFrontier): “the canonical map `F → F^#` of presheaves of `O`-modules”.
- [`PresheafOfModules.sheafifyHomEquiv`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=PresheafOfModules.sheafifyHomEquiv#doc) registered with `add_to_stacks` in [StacksFrontier/Topology/Sheaves/Sheafify/Module.lean, line 31](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/Module.lean#L31) (StacksFrontier): “the universal property: morphisms out of `F^#` correspond to morphisms out of `F`”.

## Tag 008A, a lemma

[Tag 008A](https://stacks.math.columbia.edu/tag/008A) in the Stacks Project.

**`Stacks.Sheafify.ChangeOfRingsAdjunction.tensorSheafHomEquiv`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/ModuleChangeOfRingsSheaf.lean, line 195](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/ModuleChangeOfRingsSheaf.lean#L195).

> Let `α : O ⟶ O'` be a morphism of sheaves of commutative rings on a topological space `X`,
> let `G` be a sheaf of `O`-modules and let `F` be a sheaf of `O'`-modules. There is a canonical
> bijection `Hom_{O'}(O' ⊗_O G, F) ≃ Hom_O(G, F_O)`, where `O' ⊗_O G = (O' ⊗_{p,O} G)^#` is
> `Stacks.Sheafify.ModuleStalkTensor.tensorSheaf`, the sheafification of the sectionwise tensor
> product presheaf, and `F_O` is restriction of scalars along `α`.

```lean
noncomputable def tensorSheafHomEquiv :
    (tensorSheaf O O' α G ⟶ F) ≃
      (G ⟶ (SheafOfModules.restrictScalars (ringSheafMap O O' α)).obj F)
```

**`Stacks.Sheafify.ChangeOfRingsAdjunction.nonempty_tensorSheafHomEquiv`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/ModuleChangeOfRingsSheaf.lean, line 207](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/ModuleChangeOfRingsSheaf.lean#L207).

> Existence form of `tensorSheafHomEquiv`: the sets `Hom_{O'}(O' ⊗_O G, F)` and
> `Hom_O(G, F_O)` are in bijection.

```lean
theorem nonempty_tensorSheafHomEquiv :
    Nonempty ((tensorSheaf O O' α G ⟶ F) ≃
      (G ⟶ (SheafOfModules.restrictScalars (ringSheafMap O O' α)).obj F))
```

## Tag 008B, a lemma

[Tag 008B](https://stacks.math.columbia.edu/tag/008B) in the Stacks Project.

**`Stacks.Sheafify.ModuleStalkTensor.mainIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/ModuleStalkTensor.lean, line 1170](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/ModuleStalkTensor.lean#L1170). References: EGA 0 (4.1.5), “special case”.

> The canonical isomorphism of `O'_x`-modules
> `F_x ⊗_{O_x} O'_x ≃ₗ (F ⊗_O O')_x`, in the orientation of the tag.  The left-hand side is the
> tensor product of the `O_x`-module `F_x` with the `O_x`-algebra `O'_x`, carrying the
> `O'_x`-module structure of `rightTensorModule` in which `O'_x` acts on the right factor; the
> right-hand side is the stalk at `x` of the tensor product *sheaf* with its canonical
> `O'_x`-module structure.  The equivalence is the composite of the presheaf comparison
> (`tensorPresheafStalkIso`, Tag 007K) with the fact that sheafification commutes with stalks
> (`tensorSheafStalkIso`).

```lean
noncomputable def mainIso :
    letI := (stalkHomOfSheaves O O' α x).hom.toAlgebra
    letI := rightTensorModule (O.presheaf.stalk x) (O'.presheaf.stalk x)
      (TopCat.Presheaf.stalk (C := Ab.{u}) F.val.presheaf x)
    (TensorProduct (O.presheaf.stalk x) (TopCat.Presheaf.stalk (C := Ab.{u}) F.val.presheaf x)
        (O'.presheaf.stalk x))
      ≃ₗ[O'.presheaf.stalk x]
        (TopCat.Presheaf.stalk (C := Ab.{u}) (tensorSheaf O O' α F).val.presheaf x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.20, Tag 0088](https://stacks.math.columbia.edu/tag/0088)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
