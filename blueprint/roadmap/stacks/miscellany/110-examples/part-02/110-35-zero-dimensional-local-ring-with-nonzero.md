---
declaration: section
origin: cited
lean: Stacks.Examples.exists_local_ring_unique_prime_nonzero_flat_ideal
statement: formalized
proof: formalized
---

# 110.35 Zero dimensional local ring with nonzero flat ideal

Section 110.35 of the Stacks Project, [Tag 05FZ](https://stacks.math.columbia.edu/tag/05FZ). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 05G0, a lemma

[Tag 05G0](https://stacks.math.columbia.edu/tag/05G0) in the Stacks Project.

**`Stacks.Examples.exists_local_ring_unique_prime_nonzero_flat_ideal`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Scheme/ZeroDimensionalFlatIdeal.lean, line 483](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Scheme/ZeroDimensionalFlatIdeal.lean#L483).

> **Stacks 05G0.** There is a local ring with a unique prime ideal and a nonzero proper
> flat ideal.

```lean
theorem exists_local_ring_unique_prime_nonzero_flat_ideal :
    ∃ (R : Type u) (_ : CommRing R) (_ : IsLocalRing R) (I : Ideal R),
      (∃! p : Ideal R, p.IsPrime) ∧ I ≠ ⊥ ∧ I ≠ ⊤ ∧ Module.Flat R I
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.35, Tag 05FZ](https://stacks.math.columbia.edu/tag/05FZ)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
