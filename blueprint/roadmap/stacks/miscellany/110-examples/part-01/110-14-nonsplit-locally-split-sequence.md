---
declaration: section
origin: cited
lean: Stacks.Examples.exists_nonsplit_shortExact_locally_split
statement: formalized
proof: formalized
---

# 110.14 Nonsplit locally split sequence

Section 110.14 of the Stacks Project, [Tag 0H7F](https://stacks.math.columbia.edu/tag/0H7F). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf).

## Tag 0H7G, a lemma

[Tag 0H7G](https://stacks.math.columbia.edu/tag/0H7G) in the Stacks Project.

**`Stacks.Examples.exists_nonsplit_shortExact_locally_split`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Flatness/NonsplitLocallySplit.lean, line 329](https://github.com/AxiomMath/Stacks/blob/f56a316ddf7a930906d88b78d6f9a2668cffd0cf/StacksFrontier/Examples/Flatness/NonsplitLocallySplit.lean#L329).

> A short exact sequence of integer modules that is nonsplit but splits Zariski locally.

```lean
theorem exists_nonsplit_shortExact_locally_split.{u} :
    ∃ S : ShortComplex (ModuleCat.{u} ℤ),
      S.ShortExact ∧
        (¬ Nonempty S.Splitting) ∧
        ∀ p : PrimeSpectrum ℤ,
          ∃ f : ℤ, f ∉ p.asIdeal ∧
            Nonempty
              ((S.map (ModuleCat.localizedModuleFunctor.{u} (Submonoid.powers f))).Splitting)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.14, Tag 0H7F](https://stacks.math.columbia.edu/tag/0H7F)
- [AxiomMath/Stacks at f56a316d](https://github.com/AxiomMath/Stacks/tree/f56a316ddf7a930906d88b78d6f9a2668cffd0cf)
