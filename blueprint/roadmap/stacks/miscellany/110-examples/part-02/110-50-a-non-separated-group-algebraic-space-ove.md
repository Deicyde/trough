---
declaration: section
origin: cited
lean: Stacks.Examples.NonSeparatedGroupSpace.exists_isFiniteType_groupAlgebraicSpace_not_isSeparatedOver
statement: formalized
proof: formalized
---

# 110.50 A non-separated group algebraic space over a field

Section 110.50 of the Stacks Project, [Tag 06E9](https://stacks.math.columbia.edu/tag/06E9). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06EA, a lemma

[Tag 06EA](https://stacks.math.columbia.edu/tag/06EA) in the Stacks Project.

**`Stacks.Examples.NonSeparatedGroupSpace.exists_isFiniteType_groupAlgebraicSpace_not_isSeparatedOver`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Spaces/NonSeparatedGroupSpace.lean, line 823](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Spaces/NonSeparatedGroupSpace.lean#L823).

> **Stacks Project, Tag 06EA.** Over a field of characteristic zero there is a group
> algebraic space of finite type over the field which is neither separated, nor quasi-separated,
> nor locally separated.
>
> The witness is the quotient `𝔸¹_k/ℤ` of the affine line by the integer translations, realized
> as the fppf sheafification of the presheaf of global sections modulo the integers: addition of
> sections makes that sheafification a group object, while the quotient fails to be decent, and a
> quasi-separated or locally separated algebraic space is decent.

```lean
theorem exists_isFiniteType_groupAlgebraicSpace_not_isSeparatedOver
    (k : Type u) [Field k] [CharZero k] (B : BigFppfSite.{u})
    (hS : B.Contains (Spec (.of k))) (hG : B.Contains (Spec (.of (RatFunc k)))) :
    ∃ G : Space.GroupAlgebraicSpace B (Spec (.of k)) hS
        (yoneda.obj (Over.mk (𝟙 (B.obj hS))))
        (isAlgebraicSpace_yoneda B (Spec (.of k)) hS (Over.mk (𝟙 (B.obj hS)))),
      Space.IsFiniteType B (Spec (.of k)) hS G.obj.X.hom ∧
      ¬ Space.IsSeparatedOver B (Spec (.of k)) hS G.obj.X.left ∧
      ¬ Space.IsQuasiSeparatedOver B (Spec (.of k)) hS G.obj.X.left ∧
      ¬ Space.IsLocallySeparatedOver B (Spec (.of k)) hS G.obj.X.left
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.50, Tag 06E9](https://stacks.math.columbia.edu/tag/06E9)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
