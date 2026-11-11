---
declaration: section
origin: cited
lean: AlgebraicGeometry.GroupoidInAlgebraicSpaces.sourceFibersIsoOfTargetEq
statement: formalized
proof: formalized
---

# 79.7 Comparing fibres

Section 79.7 of the Stacks Project, [Tag 04PA](https://stacks.math.columbia.edu/tag/04PA). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0452, a lemma

[Tag 0452](https://stacks.math.columbia.edu/tag/0452) in the Stacks Project.

**`AlgebraicGeometry.GroupoidInAlgebraicSpaces.sourceFibersIsoOfTargetEq`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Fibres.lean, line 50](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Groupoids/More/Fibres.lean#L50).

> **Stacks 0452.** Two arrows of a groupoid in algebraic spaces over a test algebraic space
> `X` with the same target have isomorphic source fibres over `X`.

```lean
theorem sourceFibersIsoOfTargetEq (C : BigFppfSite.{u}) (S : Scheme.{u}) (hS : C.Contains S)
    (B : AlgebraicSpaces C S hS) (G : GroupoidInAlgebraicSpaces C S hS B)
    (X : AlgebraicSpaces C S hS) (r r' : X ⟶ G.arrows)
    (h : r ≫ G.target = r' ≫ G.target) :
    Nonempty
      ((Over.mk
          (ObjectProperty.homMk (pullback.fst (r ≫ G.source).hom G.source.hom) :
            AlgebraicSpaces.fiberProduct C S hS (r ≫ G.source) G.source ⟶ X) :
          Over X) ≅
       (Over.mk
          (ObjectProperty.homMk (pullback.fst (r' ≫ G.source).hom G.source.hom) :
            AlgebraicSpaces.fiberProduct C S hS (r' ≫ G.source) G.source ⟶ X) :
          Over X))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 79.7, Tag 04PA](https://stacks.math.columbia.edu/tag/04PA)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
