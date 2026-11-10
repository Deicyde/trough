---
declaration: section
origin: cited
lean: Stacks.Cohomology.abelianSheaf_enoughInjectives, Stacks.Cohomology.abelianSheaf_hasFunctorialInjectiveEmbeddings, Stacks.Injectives.abelianSheaf_enoughInjectives, Stacks.Injectives.abelianSheaf_hasFunctorialInjectiveEmbeddings, Stacks.Cohomology.LerayLowDegree.abelianSheafEnoughInjectives
statement: formalized
proof: formalized
---

# 19.4 Abelian sheaves on a space

Section 19.4 of the Stacks Project, [Tag 01DF](https://stacks.math.columbia.edu/tag/01DF). 1 tag here is carried by 5 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 01DG, a lemma

[Tag 01DG](https://stacks.math.columbia.edu/tag/01DG) in the Stacks Project.

**`Stacks.Cohomology.abelianSheaf_enoughInjectives`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/GlobalSectionsDerived.lean, line 67](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/GlobalSectionsDerived.lean#L67). The attribute's comment: “enough injectives”. References: SGA 4 II (6.9), “site of opens of a space”; SGA 4 V (0.1.1), “sheaves on a space”.

> The category of abelian sheaves on a topological space has enough injectives.

```lean
instance abelianSheaf_enoughInjectives (X : TopCat.{u}) :
    EnoughInjectives (TopCat.Sheaf AddCommGrpCat.{max u v} X)
```

**`Stacks.Cohomology.abelianSheaf_hasFunctorialInjectiveEmbeddings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Cohomology/GlobalSectionsDerived.lean, line 75](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Cohomology/GlobalSectionsDerived.lean#L75). The attribute's comment: “functorial injective embeddings”. References: SGA 4 II (6.9), “site of opens of a space”; SGA 4 V (0.1.1), “sheaves on a space”.

> Abelian sheaves on a topological space admit functorial injective embeddings.

```lean
theorem abelianSheaf_hasFunctorialInjectiveEmbeddings (X : TopCat.{u}) :
    HasFunctorialInjectiveEmbeddings (TopCat.Sheaf AddCommGrpCat.{max u v} X)
```

**`Stacks.Injectives.abelianSheaf_enoughInjectives`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Sheaf/AbelianSheavesOnSpace.lean, line 62](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Sheaf/AbelianSheavesOnSpace.lean#L62). The attribute's comment: “enough injectives”.

> **Stacks 01DG.** The category of abelian sheaves on a topological space has enough
> injectives.

```lean
instance abelianSheaf_enoughInjectives (X : TopCat.{u}) :
    EnoughInjectives (TopCat.Sheaf AddCommGrpCat.{max u v} X)
```

**`Stacks.Injectives.abelianSheaf_hasFunctorialInjectiveEmbeddings`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Homology/Injectives/Sheaf/AbelianSheavesOnSpace.lean, line 78](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Homology/Injectives/Sheaf/AbelianSheavesOnSpace.lean#L78). The attribute's comment: “functorial injective embeddings”.

> **Stacks 01DG.** Abelian sheaves on a topological space admit functorial injective
> embeddings.

```lean
theorem abelianSheaf_hasFunctorialInjectiveEmbeddings (X : TopCat.{u}) :
    HasFunctorialInjectiveEmbeddings (TopCat.Sheaf AddCommGrpCat.{max u v} X)
```

**`Stacks.Cohomology.LerayLowDegree.abelianSheafEnoughInjectives`**, an instance in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Topology/Sheaves/Cohomology/Leray/LowDegreeSequence.lean, line 87](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Topology/Sheaves/Cohomology/Leray/LowDegreeSequence.lean#L87). The attribute's comment: “enough injectives”. References: SGA 4 II (6.9), “site of opens of a space”; SGA 4 V (0.1.1), “sheaves on a space”.

> **Abelian sheaves have enough injectives** ([Stacks, Tag 01DG]), in any coefficient universe
> containing that of the space.  The site `Opens X` is `u`-small, hence essentially small in the
> larger universe, and `AddCommGrpCat` is a Grothendieck abelian category there, so the sheaf
> category is Grothendieck abelian and therefore has enough injectives.

```lean
instance abelianSheafEnoughInjectives (X : TopCat.{u}) :
    EnoughInjectives (Sheaf (Opens.grothendieckTopology X) AddCommGrpCat.{max u v})
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 19.4, Tag 01DF](https://stacks.math.columbia.edu/tag/01DF)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
