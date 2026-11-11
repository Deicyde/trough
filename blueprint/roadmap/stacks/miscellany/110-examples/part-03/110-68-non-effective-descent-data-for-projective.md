---
declaration: section
origin: cited
lean: Stacks.Examples.NonEffectiveProjectiveDescent.exists_nonEffectiveDescentData_projective
statement: formalized
proof: formalized
---

# 110.68 Non-effective descent data for projective schemes

Section 110.68 of the Stacks Project, [Tag 08KE](https://stacks.math.columbia.edu/tag/08KE). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 08KF, a lemma

[Tag 08KF](https://stacks.math.columbia.edu/tag/08KF) in the Stacks Project.

**`Stacks.Examples.NonEffectiveProjectiveDescent.exists_nonEffectiveDescentData_projective`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Examples/NonEffectiveProjectiveDescent.lean, line 241](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Examples/NonEffectiveProjectiveDescent.lean#L241). The attribute's comment: “THE EXISTENCE IS NOT ASSERTED. What is proved is the reduction of the tag to its family form: given an étale covering family whose members are H-projective over the base and whose descent datum is not family-effective, the coproduct is a single étale morphism, is projective, and its datum is not effective. The witness itself is carried as `EtaleProjectiveNonEffectiveFamily`, which is what the chain of Tags 0D5E (existence half, blocked on Artin contraction), 0E6F (no library carrier at all) and 02W5 (fppf case, only the general-site halves are proved) would produce”.

> **[Stacks, Tag 08KF], granted the construction of the witness.** There are an étale covering
> of a scheme consisting of a single morphism `f : X ⟶ S` and a descent datum relative to `f` whose
> scheme over `X` is projective over `X` and which is not effective in the category of schemes.

```lean
theorem exists_nonEffectiveDescentData_projective
    (hW : EtaleProjectiveNonEffectiveFamily.{u}) :
    ∃ (S X : Scheme.{u}) (f : X ⟶ S)
      (D : DescentData (S := S) (X := fun _ : Unit ↦ X) (fun _ ↦ f)),
      Presieve.singleton f ∈ Scheme.etalePrecoverage S ∧
        IsProjective (D.obj ()).hom ∧ ¬ D.IsEffective
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.68, Tag 08KE](https://stacks.math.columbia.edu/tag/08KE)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
