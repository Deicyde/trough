---
declaration: section
origin: cited
lean: Stacks.Injectives.continuousModule_hasFunctorialInjectiveEmbeddings
statement: formalized
proof: formalized
---

# 19.3 G-modules

Section 19.3 of the Stacks Project, [Tag 04JE](https://stacks.math.columbia.edu/tag/04JE). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf).

## Tag 04JF, a lemma

[Tag 04JF](https://stacks.math.columbia.edu/tag/04JF) in the Stacks Project.

**`Stacks.Injectives.continuousModule_hasFunctorialInjectiveEmbeddings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Module/ContinuousGroupModules.lean, line 752](https://github.com/AxiomMath/Stacks/blob/f56a316ddf7a930906d88b78d6f9a2668cffd0cf/StacksFrontier/Homology/Injectives/Module/ContinuousGroupModules.lean#L752).

> **Stacks Project, Tag 04JF.** The category of `R`-modules with continuous
> `G`-action has functorial injective embeddings. In particular, taking
> `R = ℤ` gives this result for discrete `G`-modules.

```lean
theorem continuousModule_hasFunctorialInjectiveEmbeddings
    (R : Type u) [Ring R]
    (G : Type v) [Group G] [TopologicalSpace G] [IsTopologicalGroup G] :
    HasFunctorialInjectiveEmbeddings (ContinuousModule.{u, v, max u v w} R G)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 19.3, Tag 04JE](https://stacks.math.columbia.edu/tag/04JE)
- [AxiomMath/Stacks at f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf)
