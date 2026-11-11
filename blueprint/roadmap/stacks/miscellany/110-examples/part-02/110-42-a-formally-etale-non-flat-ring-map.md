---
declaration: section
origin: cited
lean: Stacks.Examples.exists_formallyEtale_not_flat
statement: formalized
proof: formalized
---

# 110.42 A formally étale non-flat ring map

Section 110.42 of the Stacks Project, [Tag 060H](https://stacks.math.columbia.edu/tag/060H). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 060I, a lemma

[Tag 060I](https://stacks.math.columbia.edu/tag/060I) in the Stacks Project.

**`Stacks.Examples.exists_formallyEtale_not_flat`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/FormallyEtaleNotFlat.lean, line 180](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/FormallyEtaleNotFlat.lean#L180).

> There exists a formally étale map of commutative rings which is not flat.

```lean
public theorem exists_formallyEtale_not_flat :
    ∃ (R S : Type*) (_ : CommRing R) (_ : CommRing S) (f : R →+* S),
      f.FormallyEtale ∧ ¬ f.Flat
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.42, Tag 060H](https://stacks.math.columbia.edu/tag/060H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
