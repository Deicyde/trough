---
declaration: section
origin: cited
lean: stalk_module_structure, Stacks.Sheafify.ModuleStalkTensor.tensorPresheafStalkIso
statement: formalized
proof: formalized
---

# 6.14 Stalks of presheaves of modules

Section 6.14 of the Stacks Project, [Tag 007I](https://stacks.math.columbia.edu/tag/007I). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 007J, a lemma

[Tag 007J](https://stacks.math.columbia.edu/tag/007J) in the Stacks Project.

**`stalk_module_structure`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Stalk/Module.lean, line 80](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Stalk/Module.lean#L80).

> The canonical `Module (R.stalk x)`-structure on `TopCat.Presheaf.stalk M.presheaf x`.

```lean
noncomputable def stalk_module_structure :
    Module ↑(R.stalk x) ↑(TopCat.Presheaf.stalk M.presheaf x)
```

## Tag 007K, a lemma

[Tag 007K](https://stacks.math.columbia.edu/tag/007K) in the Stacks Project.

**`Stacks.Sheafify.ModuleStalkTensor.tensorPresheafStalkIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Sheafify/ModuleStalkTensor.lean, line 997](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Sheafify/ModuleStalkTensor.lean#L997).

> The canonical isomorphism of `O'_x`-modules
> `F_x ⊗_{O_x} O'_x ≃ₗ (F ⊗_{p,O} O')_x`, for a morphism `α : O ⟶ O'` of *presheaves* of
> commutative rings on `X` and a *presheaf* `F` of `O`-modules.  The left-hand side is the tensor
> product of the `O_x`-module `F_x` with the `O_x`-algebra `O'_x`, carrying the `O'_x`-module
> structure of `rightTensorModule` in which `O'_x` acts on the right factor; the right-hand side is
> the stalk at `x` of the tensor product presheaf.

```lean
noncomputable def tensorPresheafStalkIso :
    letI := (stalkHom O O' α x).hom.toAlgebra
    letI := rightTensorModule (O.stalk x) (O'.stalk x)
      (TopCat.Presheaf.stalk (C := Ab.{u}) F.presheaf x)
    (TensorProduct (O.stalk x) (TopCat.Presheaf.stalk (C := Ab.{u}) F.presheaf x)
        (O'.stalk x))
      ≃ₗ[O'.stalk x]
        (TopCat.Presheaf.stalk (C := Ab.{u}) (tensorPresheafOfModules O O' α F).presheaf x)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 6.14, Tag 007I](https://stacks.math.columbia.edu/tag/007I)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
