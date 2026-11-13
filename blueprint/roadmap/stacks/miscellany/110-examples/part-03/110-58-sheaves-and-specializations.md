---
declaration: section
origin: cited
lean: Stacks.Examples.DimensionSheaf.exists_sheaf_detecting_dimension
statement: formalized
proof: formalized
---

# 110.58 Sheaves and specializations

Section 110.58 of the Stacks Project, [Tag 05LD](https://stacks.math.columbia.edu/tag/05LD). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05LE, a lemma

[Tag 05LE](https://stacks.math.columbia.edu/tag/05LE) in the Stacks Project.

**`Stacks.Examples.DimensionSheaf.exists_sheaf_detecting_dimension`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Sheaves/DimensionDetectingEtaleSheaf.lean, line 1005](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Sheaves/DimensionDetectingEtaleSheaf.lean#L1005).

> **Stacks 05LE.** For every big étale site and every natural number `n` there is a sheaf of
> abelian groups `G` on it whose sections over `X` are zero when `\dim(X) < n`, are nonzero when
> `\dim(X) \ge n`, and restrict isomorphically along a thickening `X \subset X'`.

```lean
public theorem exists_sheaf_detecting_dimension (B : BigEtaleSite.{u}) (n : ℕ) :
    ∃ G : Sheaf B.topology AddCommGrpCat.{u + 1},
      (∀ X : B.Scheme, topologicalKrullDim ((B.inclusion).obj X) < (n : WithBot ℕ∞) →
          Subsingleton (G.obj.obj (Opposite.op X))) ∧
        (∀ X : B.Scheme, (n : WithBot ℕ∞) ≤ topologicalKrullDim ((B.inclusion).obj X) →
          Nontrivial (G.obj.obj (Opposite.op X))) ∧
        (∀ (X X' : B.Scheme) (i : X ⟶ X'),
          Stacks.Thickenings.IsThickening ((B.inclusion).map i) →
            IsIso (G.obj.map i.op))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.58, Tag 05LD](https://stacks.math.columbia.edu/tag/05LD)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
