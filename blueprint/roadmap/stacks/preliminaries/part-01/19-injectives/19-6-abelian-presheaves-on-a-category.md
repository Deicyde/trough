---
declaration: section
origin: cited
lean: Stacks.Injectives.presheaf_hasFunctorialInjectiveEmbeddings
statement: formalized
proof: formalized
---

# 19.6 Abelian presheaves on a category

Section 19.6 of the Stacks Project, [Tag 01DJ](https://stacks.math.columbia.edu/tag/01DJ). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 01DK, a proposition

[Tag 01DK](https://stacks.math.columbia.edu/tag/01DK) in the Stacks Project.

**`Stacks.Injectives.presheaf_hasFunctorialInjectiveEmbeddings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Sheaf/AbelianPresheaves.lean, line 40](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Homology/Injectives/Sheaf/AbelianPresheaves.lean#L40).

> The category of abelian presheaves on a category has functorial injective embeddings.

```lean
theorem presheaf_hasFunctorialInjectiveEmbeddings (C : Type u) [Category.{v} C] :
    HasFunctorialInjectiveEmbeddings (Cᵒᵖ ⥤ AddCommGrpCat.{max u v t})
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 19.6, Tag 01DJ](https://stacks.math.columbia.edu/tag/01DJ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
