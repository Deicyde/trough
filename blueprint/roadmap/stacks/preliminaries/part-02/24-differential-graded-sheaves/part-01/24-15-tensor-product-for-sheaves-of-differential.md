---
declaration: section
origin: cited
lean: SheafOfModules.RelativeTensor.dgTensorOpIso, SheafOfModules.RelativeTensor.dgTensorSumDiff_balance, SheafOfModules.RelativeTensor.dgTensorDiffPre, SheafOfModules.RelativeTensor.dgTensor, SheafOfModules.RelativeTensor.dgTensorFunctor, SheafOfModules.RelativeTensor.dgUnitorIso, SheafOfModules.LocalBalancedBilinear
statement: formalized
proof: formalized
---

# 24.15 Tensor product for sheaves of differential graded modules

Section 24.15 of the Stacks Project, [Tag 0FRM](https://stacks.math.columbia.edu/tag/0FRM). 1 tag here is carried by 7 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FRM, the section

[Tag 0FRM](https://stacks.math.columbia.edu/tag/0FRM) in the Stacks Project.

**`SheafOfModules.RelativeTensor.dgTensorOpIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedOppositeTensor.lean, line 324](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedOppositeTensor.lean#L324). The attribute's comment: “the relative tensor product of the opposite algebra, interchanged”.

> **The relative tensor product read over the opposite algebra.** Interchanging the two
> factors and twisting by the Koszul sign identifies `P ⊗_{A.op} M.opLeft` with
> `M ⊗_A P.unopLeft`.

```lean
noncomputable def dgTensorOpIso : dgTensor P M.opLeft ≅ dgTensor M P.unopLeft
```

**`SheafOfModules.RelativeTensor.dgTensorSumDiff_balance`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedRelativeTensor.lean, line 301](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedRelativeTensor.lean#L301). The attribute's comment: “the differential is well defined: it kills `xa ⊗ y - x ⊗ ay`”.

> The signed differential of the direct sums is compatible with the balance maps: this is the
> two Leibniz rules, and it is what makes the differential descend to `P ⊗_A N`.

```lean
theorem dgTensorSumDiff_balance (n : ℤ) :
    balanceMap (gP P) (gN N) n ≫ dgTensorSumDiff P N n =
      relationSumDiff P N n ≫ balanceMap (gP P) (gN N) (n + 1)
```

**`SheafOfModules.RelativeTensor.dgTensorDiffPre`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedRelativeTensor.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedRelativeTensor.lean#L382). The attribute's comment: “the differential `d (x ⊗ y) = dx ⊗ y + (-1)^{deg x} x ⊗ dy`”.

> The differential of degree `n` of the relative tensor product `P ⊗_A N`, as a morphism of
> presheaves of modules: the descent of the signed differential to the cokernel of the balance
> map.

```lean
noncomputable def dgTensorDiffPre (n : ℤ) :
    gradedTensorPre (gP P) (gN N) n ⟶ gradedTensorPre (gP P) (gN N) (n + 1)
```

**`SheafOfModules.RelativeTensor.dgTensor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedRelativeTensor.lean, line 419](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedRelativeTensor.lean#L419). The attribute's comment: “the relative tensor product as a complex of `O`-modules”.

> The relative tensor product `P ⊗_A N` of a right differential graded `A`-module with a left
> differential graded `A`-module, as a cochain complex of sheaves of modules.

```lean
noncomputable def dgTensor : CochainComplex (SheafOfModules.{m} (toRingCat J Osharp)) ℤ
```

**`SheafOfModules.RelativeTensor.dgTensorFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedRelativeTensor.lean, line 585](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedRelativeTensor.lean#L585). The attribute's comment: “the functor `- ⊗_A N` to complexes of `O`-modules”.

> The functor `- ⊗_A N` from right differential graded `A`-modules to complexes of
> `O`-modules, for a fixed left differential graded `A`-module `N`.

```lean
noncomputable def dgTensorFunctor :
    DifferentialGradedModule.{t, m, m} A ⥤
      CochainComplex (SheafOfModules.{m} (toRingCat J Osharp)) ℤ
```

**`SheafOfModules.RelativeTensor.dgUnitorIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedRelativeTensorUnitor.lean, line 135](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedRelativeTensorUnitor.lean#L135). The attribute's comment: “the unit isomorphism A ⊗\_A N ≅ N of complexes, for A the regular right module”.

> **The unit isomorphism of the relative tensor product of differential graded modules**:
> `A ⊗_A N ≅ N` as cochain complexes of sheaves of modules, for `A` a sheaf of differential graded
> algebras acting on itself on the right and `N` a left differential graded `A`-module.

```lean
noncomputable def dgUnitorIso :
    dgTensor (DifferentialGradedModule.regularModule A) N ≅ N.complex
```

**`SheafOfModules.LocalBalancedBilinear`**, a structure in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensor.lean, line 270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedTensor.lean#L270). The attribute's comment: “local balanced bilinear families, the universal property of the tensor product”.

> An `A`-balanced bilinear family of degree `n` over `U`, from a right differential graded
> `A`-module `M` and a differential graded `(A, B)`-bimodule `N` to a right differential graded
> `B`-module `L`: maps `M^i|_U × N^j|_U → L^{i + j + n}|_U` which are bilinear over the sheaf of
> rings, compatible with restriction, `A`-balanced and `B`-linear in the second variable.

```lean
structure LocalBalancedBilinear (M : DifferentialGradedModule.{t, a, w} A)
    (N : DifferentialGradedBimodule.{t, a, z} A B)
    (L : DifferentialGradedModule.{t, a, s} B) (n : ℤ) (U : C)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.15, Tag 0FRM](https://stacks.math.columbia.edu/tag/0FRM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
