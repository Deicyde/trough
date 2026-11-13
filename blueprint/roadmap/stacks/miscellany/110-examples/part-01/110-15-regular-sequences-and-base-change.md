---
declaration: section
origin: cited
lean: Stacks.Examples.exists_regularSequence_with_common_annihilator_mod_last, Stacks.Examples.exists_regular_sequence_flat_quotient_not_koszulRegular_fiber
statement: formalized
proof: formalized
---

# 110.15 Regular sequences and base change

Section 110.15 of the Stacks Project, [Tag 063Z](https://stacks.math.columbia.edu/tag/063Z). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0640, a lemma

[Tag 0640](https://stacks.math.columbia.edu/tag/0640) in the Stacks Project.

**`Stacks.Examples.exists_regularSequence_with_common_annihilator_mod_last`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Flatness/StrangeRegularSequence.lean, line 922](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Flatness/StrangeRegularSequence.lean#L922).

> A regular sequence in a local ring can have its first two terms annihilate a common nonzero
> element modulo its last term.

```lean
theorem exists_regularSequence_with_common_annihilator_mod_last :
    ∃ (R : Type u) (_ : CommRing R) (_ : IsLocalRing R) (x y z : R),
      x ∈ maximalIdeal R ∧ y ∈ maximalIdeal R ∧ z ∈ maximalIdeal R ∧
        RingTheory.Sequence.IsRegular R [x, y, z] ∧
        ∃ δ : R ⧸ Ideal.span {z},
          δ ≠ 0 ∧
            (Ideal.Quotient.mk (Ideal.span {z}) x) * δ = 0 ∧
            (Ideal.Quotient.mk (Ideal.span {z}) y) * δ = 0
```

## Tag 0641, a lemma

[Tag 0641](https://stacks.math.columbia.edu/tag/0641) in the Stacks Project.

**`Stacks.Examples.exists_regular_sequence_flat_quotient_not_koszulRegular_fiber`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Flatness/RegularSequenceClosedFibre.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/Examples/Flatness/RegularSequenceClosedFibre.lean#L65).

> A regular sequence in a local ring can give a flat quotient over a local
> base while its closed-fiber sequence fails even Koszul regularity.

```lean
theorem exists_regular_sequence_flat_quotient_not_koszulRegular_fiber :
    ∃ (A : Type u) (B : Type v) (_ : CommRing A) (_ : CommRing B)
      (_ : IsLocalRing A) (_ : IsLocalRing B) (_ : Algebra A B)
      (_ : IsLocalHom (algebraMap A B)) (x y : B),
      let I : Ideal B := (IsLocalRing.maximalIdeal A).map (algebraMap A B)
      x ∈ IsLocalRing.maximalIdeal B ∧
      y ∈ IsLocalRing.maximalIdeal B ∧
      RingTheory.Sequence.IsRegular B [x, y] ∧
      Module.Flat A (B ⧸ Ideal.ofList [x, y]) ∧
      ¬ RingTheory.Sequence.IsRegular (B ⧸ I)
        [Ideal.Quotient.mk I x, Ideal.Quotient.mk I y] ∧
      ¬ Koszul.IsKoszulRegular
        (fun i : Fin 2 =>
          if i = 0 then Ideal.Quotient.mk I x else Ideal.Quotient.mk I y)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.15, Tag 063Z](https://stacks.math.columbia.edu/tag/063Z)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
