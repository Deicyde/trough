---
declaration: section
origin: cited
lean: AlgebraicGeometry.isSheaf_fpqc_projectiveLinePow, AlgebraicGeometry.relativelyRepresentable_diag_projectiveLinePow
statement: formalized
proof: formalized
---

# 110.56 Sheaf with quasi-compact flat covering which is not algebraic

Section 110.56 of the Stacks Project, [Tag 078E](https://stacks.math.columbia.edu/tag/078E). 1 tag here is carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 078F, a lemma

[Tag 078F](https://stacks.math.columbia.edu/tag/078F) in the Stacks Project.

**`AlgebraicGeometry.isSheaf_fpqc_projectiveLinePow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/ProductOfProjectiveLines.lean, line 382](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Spaces/ProductOfProjectiveLines.lean#L382). The attribute's comment: “the witness (P^1)^∞ is a sheaf for the fpqc topology”.

> `(ℙ¹)^∞` satisfies the sheaf condition for the fpqc topology.

```lean
theorem isSheaf_fpqc_projectiveLinePow :
    Presheaf.IsSheaf Scheme.fpqcTopology.{u} projectiveLinePow.{u}
```

**`AlgebraicGeometry.relativelyRepresentable_diag_projectiveLinePow`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/ProductOfProjectiveLines.lean, line 388](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Spaces/ProductOfProjectiveLines.lean#L388). The attribute's comment: “the witness (P^1)^∞ has representable diagonal”.

> The diagonal of `(ℙ¹)^∞` is representable.

```lean
theorem relativelyRepresentable_diag_projectiveLinePow :
    yoneda.relativelyRepresentable (diag projectiveLinePow.{u})
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.56, Tag 078E](https://stacks.math.columbia.edu/tag/078E)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
