---
declaration: section
origin: cited
lean: Stacks.Examples.exists_formallySmooth_not_flat
statement: formalized
proof: formalized
---

# 110.41 A formally smooth non-flat ring map

Section 110.41 of the Stacks Project, [Tag 057V](https://stacks.math.columbia.edu/tag/057V). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 057W, a lemma

[Tag 057W](https://stacks.math.columbia.edu/tag/057W) in the Stacks Project.

**`Stacks.Examples.exists_formallySmooth_not_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/FormallySmoothNotFlat.lean, line 202](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/FormallySmoothNotFlat.lean#L202).

> There exists a formally smooth ring map which is not flat.

```lean
public theorem exists_formallySmooth_not_flat :
    ∃ (R S : Type*) (_ : CommRing R) (_ : CommRing S) (f : R →+* S),
      f.FormallySmooth ∧ ¬ f.Flat
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.41, Tag 057V](https://stacks.math.columbia.edu/tag/057V)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
