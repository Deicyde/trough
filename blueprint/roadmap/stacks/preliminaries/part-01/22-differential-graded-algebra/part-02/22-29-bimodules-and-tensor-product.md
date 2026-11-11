---
declaration: section
origin: cited
lean: DifferentialGraded.Bimodule.tensorDGFunctor, DifferentialGraded.Bimodule.tensorCompFunctor, DifferentialGraded.Bimodule.tensorHomotopyFunctor, DifferentialGraded.Bimodule.tensorCompFunctor_quotient, DifferentialGraded.Bimodule.tensorShiftIso
statement: formalized
proof: formalized
---

# 22.29 Bimodules and tensor product

Section 22.29 of the Stacks Project, [Tag 0FQM](https://stacks.math.columbia.edu/tag/0FQM). 2 tags here are carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09LM, a lemma

[Tag 09LM](https://stacks.math.columbia.edu/tag/09LM) in the Stacks Project.

**`DifferentialGraded.Bimodule.tensorDGFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensor.lean, line 1264](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensor.lean#L1264). The attribute's comment: “the DG functor”.

> **Stacks 09LM.** Tensoring with a differential graded `(A, B)`-bimodule is a functor of
> differential graded categories.

```lean
noncomputable def tensorDGFunctor (N : Bimodule A B) : TensorDGFunctorData N
```

**`DifferentialGraded.Bimodule.tensorCompFunctor`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensor.lean, line 1270](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensor.lean#L1270). The attribute's comment: “the ordinary functor”.

> **Stacks 09LM.** The induced functor on the categories of differential graded modules.

```lean
noncomputable abbrev tensorCompFunctor (N : Bimodule A B) :
    DifferentialGradedModule A ⥤ DifferentialGradedModule B
```

**`DifferentialGraded.Bimodule.tensorHomotopyFunctor`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensor.lean, line 1277](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensor.lean#L1277). The attribute's comment: “the homotopy functor”.

> **Stacks 09LM.** The induced functor on the homotopy categories.

```lean
noncomputable def tensorHomotopyFunctor (N : Bimodule A B) :
    HomotopyCategory A ⥤ HomotopyCategory B
```

**`DifferentialGraded.Bimodule.tensorCompFunctor_quotient`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensor.lean, line 1298](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensor.lean#L1298). The attribute's comment: “compatibility with the quotient”.

> **Stacks 09LM.** Passing the ordinary tensor functor to homotopy classes yields the tensor
> functor on the homotopy categories.

```lean
noncomputable def tensorCompFunctor_quotient (N : Bimodule A B) :
    (tensorCompFunctor N ⋙ toHomotopyCategory B) ≅
      (toHomotopyCategory A ⋙ tensorHomotopyFunctor N)
```

## Tag 0FQN, a remark

[Tag 0FQN](https://stacks.math.columbia.edu/tag/0FQN) in the Stacks Project.

**`DifferentialGraded.Bimodule.tensorShiftIso`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensorShift.lean, line 229](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/DifferentialGraded/Module/BimoduleTensorShift.lean#L229).

> **Stacks 0FQN.** The canonical, sign-free identification `(M ⊗_A N)[k] ≅ M[k] ⊗_A N`: it
> sends each pure tensor to the same pure tensor.

```lean
noncomputable def tensorShiftIso (N : Bimodule A B) (M : DifferentialGradedModule A) (k : ℤ) :
    { e : shift ((tensorDGFunctor N).functor.obj M) k ≅
        (tensorDGFunctor N).functor.obj (shift M k) //
      ∀ (x : M.M) (y : N.rightModule.M),
        e.hom.toFun (((tensorDGFunctor N).pure M).toLinearMap x y) =
          ((tensorDGFunctor N).pure (shift M k)).toLinearMap x y }
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 22.29, Tag 0FQM](https://stacks.math.columbia.edu/tag/0FQM)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
