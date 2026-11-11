---
declaration: section
origin: cited
lean: Stacks.Examples.exists_isSchemeTheoreticallyDense_open_notMem_weaklyAssociatedPoint
statement: formalized
proof: formalized
---

# 110.64 Weakly associated points and scheme theoretic density

Section 110.64 of the Stacks Project, [Tag 084J](https://stacks.math.columbia.edu/tag/084J). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 084K, a lemma

[Tag 084K](https://stacks.math.columbia.edu/tag/084K) in the Stacks Project.

**`Stacks.Examples.exists_isSchemeTheoreticallyDense_open_notMem_weaklyAssociatedPoint`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Schemes/SchemeTheoreticallyDenseOpenMissingWeaklyAssociatedPoint.lean, line 193](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Schemes/SchemeTheoreticallyDenseOpenMissingWeaklyAssociatedPoint.lean#L193).

> **Stacks 084K.** A reduced scheme can have a scheme-theoretically dense open subscheme that
> omits a weakly associated point.

```lean
theorem exists_isSchemeTheoreticallyDense_open_notMem_weaklyAssociatedPoint :
    ∃ (X : Scheme.{u}) (U : X.Opens) (x : X),
      IsReduced X ∧ Scheme.Opens.IsSchemeTheoreticallyDense U ∧
        x ∈ Stacks.Divisors.schemeWeaklyAssociatedPoints X ∧ x ∉ (U : Set X)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.64, Tag 084J](https://stacks.math.columbia.edu/tag/084J)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
