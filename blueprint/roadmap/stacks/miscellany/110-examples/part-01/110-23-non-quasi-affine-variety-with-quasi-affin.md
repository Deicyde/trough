---
declaration: section
origin: cited
lean: Stacks.Examples.exists_isVariety_normalization_isQuasiAffine_not_isQuasiAffine
statement: formalized
proof: formalized
---

# 110.23 Non-quasi-affine variety with quasi-affine normalization

Section 110.23 of the Stacks Project, [Tag 0271](https://stacks.math.columbia.edu/tag/0271). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0272, a lemma

[Tag 0272](https://stacks.math.columbia.edu/tag/0272) in the Stacks Project.

**`Stacks.Examples.exists_isVariety_normalization_isQuasiAffine_not_isQuasiAffine`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Scheme/PinchedPlane/Variety.lean, line 430](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Scheme/PinchedPlane/Variety.lean#L430).

> **Stacks Project, Tag 0272.** Over any field there is a variety whose normalization is
> quasi-affine but which is itself not quasi-affine: the punctured plane with its two punctured
> coordinate axes glued to one another.

```lean
theorem exists_isVariety_normalization_isQuasiAffine_not_isQuasiAffine
    (k : Type u) [Field k] :
    ∃ (X : Scheme.{u}) (f : X ⟶ Spec (.of k))
      (hX : ∀ U : X.Opens, IsCompact (U : Set X) → (irreducibleComponents U).Finite),
      AlgebraicGeometry.IsVariety k f ∧
        Scheme.IsQuasiAffine (Scheme.normalizationScheme X hX) ∧
        ¬ Scheme.IsQuasiAffine X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.23, Tag 0271](https://stacks.math.columbia.edu/tag/0271)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
