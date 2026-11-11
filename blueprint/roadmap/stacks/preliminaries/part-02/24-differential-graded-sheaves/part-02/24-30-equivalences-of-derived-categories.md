---
declaration: section
origin: cited
lean: SheafOfModules.DifferentialGradedModule.isEquivalence_derivedExtension
statement: formalized
proof: formalized
---

# 24.30 Equivalences of derived categories

Section 24.30 of the Stacks Project, [Tag 0FTY](https://stacks.math.columbia.edu/tag/0FTY). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0FTZ, a lemma

[Tag 0FTZ](https://stacks.math.columbia.edu/tag/0FTZ) in the Stacks Project.

**`SheafOfModules.DifferentialGradedModule.isEquivalence_derivedExtension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedQuasiIsoDerivedEquivalence.lean, line 307](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Category/ModuleCat/Sheaf/DifferentialGradedQuasiIsoDerivedEquivalence.lean#L307).

> Let `(C, O)` be a ringed site and let `φ : A ⟶ B` be a homomorphism of sheaves of
> differential graded `O`-algebras which induces an isomorphism on cohomology sheaves. Then derived
> extension of scalars
>
> `D(A, d) ⟶ D(B, d)`, `M ↦ M ⊗^𝐋_A B`
>
> is an equivalence of categories.
>
> The source's functor `M ↦ M ⊗^𝐋_A B` is defined only for a homomorphism `φ` preserving `1`,
> since `B` is made a left `A`-module through `φ`; so `PreservesOne` is implicit in the
> statement.

```lean
theorem isEquivalence_derivedExtension
    {A B : DifferentialGradedAlgebra.{u, u} (Stacks.SheafOfModules.Tensor.ringSheaf X.O)}
    (φ : A ⟶ B) (unital : φ.PreservesOne) (qis : φ.IsQuasiIso) :
    (derivedExtension φ unital).IsEquivalence
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 24.30, Tag 0FTY](https://stacks.math.columbia.edu/tag/0FTY)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
