---
declaration: section
origin: cited
lean: AlgebraicGeometry.ProEtale.exact_smallProetalePushforward
statement: formalized
proof: formalized
---

# 61.24 Finite morphisms and pro-étale sites

Section 61.24 of the Stacks Project, [Tag 09A7](https://stacks.math.columbia.edu/tag/09A7). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09A8, a lemma

[Tag 09A8](https://stacks.math.columbia.edu/tag/09A8) in the Stacks Project.

**`AlgebraicGeometry.ProEtale.exact_smallProetalePushforward`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/FinitePushforwardExact.lean, line 90](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/ProEtale/SiteFunctoriality/FinitePushforwardExact.lean#L90).

> **Stacks 09A8.** For a finite morphism of schemes which is locally of finite presentation,
> direct image of abelian sheaves along the induced morphism of small pro-étale sites is exact.

```lean
theorem exact_smallProetalePushforward
    [IsFinite (B.inclusion.map f)] [LocallyOfFinitePresentation (B.inclusion.map f)] :
    exactFunctor
      (Sheaf (SmallProetale.topology B Z.obj Z.property) AddCommGrpCat.{u + 1})
      (Sheaf (SmallProetale.topology B X.obj X.property) AddCommGrpCat.{u + 1})
      ((smallProetaleBaseChange B Z X f).sheafPushforwardContinuous AddCommGrpCat.{u + 1}
        (SmallProetale.topology B X.obj X.property)
        (SmallProetale.topology B Z.obj Z.property))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 61.24, Tag 09A7](https://stacks.math.columbia.edu/tag/09A7)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
