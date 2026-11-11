---
declaration: section
origin: cited
lean: Stacks.Injectives.sheafOfModules_hasFunctorialInjectiveEmbeddings_of_space, Stacks.Injectives.sheafOfModules_enoughInjectives_of_space
statement: formalized
proof: formalized
---

# 19.5 Sheaves of modules on a ringed space

Section 19.5 of the Stacks Project, [Tag 01DH](https://stacks.math.columbia.edu/tag/01DH). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01DI, a lemma

[Tag 01DI](https://stacks.math.columbia.edu/tag/01DI) in the Stacks Project.

**`Stacks.Injectives.sheafOfModules_hasFunctorialInjectiveEmbeddings_of_space`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Sheaf/ModulesOnRingedSpace.lean, line 39](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Sheaf/ModulesOnRingedSpace.lean#L39). The attribute's comment: “functorial injective embeddings”.

> The category of sheaves of modules over a sheaf of rings on a topological space has functorial
> injective embeddings.

```lean
theorem sheafOfModules_hasFunctorialInjectiveEmbeddings_of_space :
    HasFunctorialInjectiveEmbeddings (SheafOfModules.{u} O)
```

**`Stacks.Injectives.sheafOfModules_enoughInjectives_of_space`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Sheaf/ModulesOnRingedSpace.lean, line 46](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Sheaf/ModulesOnRingedSpace.lean#L46). The attribute's comment: “enough injectives”.

> The category of sheaves of modules over a sheaf of rings on a topological space has enough
> injectives.

```lean
theorem sheafOfModules_enoughInjectives_of_space : EnoughInjectives (SheafOfModules.{u} O)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 19.5, Tag 01DH](https://stacks.math.columbia.edu/tag/01DH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
