---
declaration: section
origin: cited
lean: Stacks.Examples.exists_infinite_flat_family_moduleDescentEqualizer, Stacks.AlgebraicGeometry.SpecIntQuasiCompactCounterexample.specInt_not_isQuasiCompactObject_canonicalTopology
statement: formalized
proof: formalized
---

# 110.82 The spectrum of the integers is not quasi-compact

Section 110.82 of the Stacks Project, [Tag 0EUE](https://stacks.math.columbia.edu/tag/0EUE). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0EUF, a lemma

[Tag 0EUF](https://stacks.math.columbia.edu/tag/0EUF) in the Stacks Project.

**`Stacks.Examples.exists_infinite_flat_family_moduleDescentEqualizer`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Algebra/NonFpqcDescent.lean, line 557](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Algebra/NonFpqcDescent.lean#L557).

> An infinite family of flat algebra maps satisfies module descent, but no finite subfamily
> satisfies it.

```lean
public theorem exists_infinite_flat_family_moduleDescentEqualizer :
    ∃ (A : CommRingCat.{u}) (I : Type v) (_ : Infinite I)
      (B : I → CommAlgCat.{u} A),
      (∀ i, Module.Flat A (B i)) ∧
        IsModuleDescentEqualizer A B Set.univ ∧
          (∀ J : Set I, J.Finite → ¬ IsModuleDescentEqualizer A B J)
```

## Tag 0EUG, a lemma

[Tag 0EUG](https://stacks.math.columbia.edu/tag/0EUG) in the Stacks Project.

**`Stacks.AlgebraicGeometry.SpecIntQuasiCompactCounterexample.specInt_not_isQuasiCompactObject_canonicalTopology`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/SpecIntQuasiCompactCounterexample.lean, line 982](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/SpecIntQuasiCompactCounterexample.lean#L982).

> The spectrum of the integers is not quasi-compact in the canonical topology
> on the category of schemes.

```lean
public theorem specInt_not_isQuasiCompactObject_canonicalTopology :
    ¬(Sheaf.canonicalTopology Scheme.{0}).IsQuasiCompactObject
      (Spec (CommRingCat.of ℤ))
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.82, Tag 0EUE](https://stacks.math.columbia.edu/tag/0EUE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
