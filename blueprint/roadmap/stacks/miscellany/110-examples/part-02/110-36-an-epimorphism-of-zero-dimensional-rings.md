---
declaration: section
origin: cited
lean: Stacks.Examples.exists_epi_localRing_not_surjective
statement: formalized
proof: formalized
---

# 110.36 An epimorphism of zero-dimensional rings which is not surjective

Section 110.36 of the Stacks Project, [Tag 06RH](https://stacks.math.columbia.edu/tag/06RH). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 06RI, a lemma

[Tag 06RI](https://stacks.math.columbia.edu/tag/06RI) in the Stacks Project.

**`Stacks.Examples.exists_epi_localRing_not_surjective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Scheme/EpiNotSurjective.lean, line 625](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Scheme/EpiNotSurjective.lean#L625).

> **Stacks 06RI.** There is a nonsurjective epimorphism of zero-dimensional local
> rings.

```lean
theorem exists_epi_localRing_not_surjective :
    ∃ (A B : Type u) (_ : CommRing A) (_ : CommRing B)
      (_ : IsLocalRing A) (_ : IsLocalRing B) (f : A →+* B),
      ringKrullDim A = 0 ∧
        ringKrullDim B = 0 ∧
        IsLocalHom f ∧
        Epi (CommRingCat.ofHom f) ∧
        ¬ Function.Surjective f
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.36, Tag 06RH](https://stacks.math.columbia.edu/tag/06RH)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
