---
declaration: section
origin: cited
lean: Stacks.Examples.exists_flat_closedImmersion_not_isOpenMap, Module.Finite.quotient, Stacks.FiniteFlatNotProjective.quotientModule_flat, Stacks.FiniteFlatNotProjective.quotientModule_not_projective
statement: formalized
proof: formalized
---

# 110.33 A finite flat module which is not projective

Section 110.33 of the Stacks Project, [Tag 052H](https://stacks.math.columbia.edu/tag/052H). 1 tag here is carried by 1 declaration of the repository (in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 05FY, a lemma

[Tag 05FY](https://stacks.math.columbia.edu/tag/05FY) in the Stacks Project.

**`Stacks.Examples.exists_flat_closedImmersion_not_isOpenMap`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Examples/Flatness/StrangeFlatModules.lean, line 119](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Flatness/StrangeFlatModules.lean#L119). The attribute's comment: “part (2)”.

> A flat closed immersion of schemes need not be an open map.

```lean
theorem exists_flat_closedImmersion_not_isOpenMap :
    ∃ (X Y : Scheme.{u}) (f : X ⟶ Y),
      IsClosedImmersion f ∧ Flat f ∧ ¬ IsOpenMap f
```

Declarations registered for the tag:

- [`Module.Finite.quotient`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Module.Finite.quotient#doc) registered with `add_to_stacks` in [StacksFrontier/Examples/Flatness/StrangeFlatModules.lean, line 53](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Flatness/StrangeFlatModules.lean#L53) (StacksFrontier): “part (1): finite”. References: EGA 0 (5.2.1), “special case”; SGA 6 I (3.2), “special case”.
- [`Stacks.FiniteFlatNotProjective.quotientModule_flat`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/LocallyFree/Basic.lean#L179), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Examples/Flatness/StrangeFlatModules.lean, line 54](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Flatness/StrangeFlatModules.lean#L54) (StacksFrontier): “part (1): flat”.
- [`Stacks.FiniteFlatNotProjective.quotientModule_not_projective`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/RingTheory/Module/LocallyFree/Basic.lean#L214), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Examples/Flatness/StrangeFlatModules.lean, line 55](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Examples/Flatness/StrangeFlatModules.lean#L55) (StacksFrontier): “part (1): not projective”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 110.33, Tag 052H](https://stacks.math.columbia.edu/tag/052H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
