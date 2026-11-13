---
declaration: section
origin: cited
lean: AlgebraicGeometry.DerivedEquivalent, AlgebraicGeometry.countable_isomorphismClasses_derivedEquivalent
statement: formalized
proof: formalized
---

# 57.18 Countability of derived equivalent varieties

Section 57.18 of the Stacks Project, [Tag 0G0Z](https://stacks.math.columbia.edu/tag/0G0Z). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 0G10, a definition

[Tag 0G10](https://stacks.math.columbia.edu/tag/0G10) in the Stacks Project.

**`AlgebraicGeometry.DerivedEquivalent`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Perfect/DerivedEquivalence.lean, line 49](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/Perfect/DerivedEquivalence.lean#L49).

> Two schemes over a field `k` are *derived equivalent* if their categories of perfect
> complexes admit a `k`-linear exact equivalence.

```lean
abbrev DerivedEquivalent (k : Type u) [Field k] (X Y : Over (Spec (.of k))) : Prop
```

## Tag 0G11, a theorem

[Tag 0G11](https://stacks.math.columbia.edu/tag/0G11) in the Stacks Project.

**`AlgebraicGeometry.countable_isomorphismClasses_derivedEquivalent`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/DerivedVarieties/Countability/DerivedEquivalentPartners.lean, line 252](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/AlgebraicGeometry/DerivedVarieties/Countability/DerivedEquivalentPartners.lean#L252).

> **Stacks Project, Tag 0G11.** Let `K` be an algebraically closed field and let `X₀` be a
> smooth proper scheme over `K`. There are at most countably many isomorphism classes of smooth
> proper schemes `Y` over `K` which are derived equivalent to `X₀`, i.e. admit a `K`-linear exact
> equivalence `D_perf(𝒪_{X₀}) ⟶ D_perf(𝒪_Y)` ([Stacks, Tag 0G10]).
>
> Proof: [Stacks, Tag 0G0Y] (`exists_countable_relativeEquivalenceKernels`) produces the countable
> family of relative equivalences, and
> `countable_isomorphismClasses_derivedEquivalent_of_relativeEquivalenceFamilies` counts.

```lean
theorem countable_isomorphismClasses_derivedEquivalent
    (X₀ : Over (Spec (CommRingCat.of k))) [Smooth X₀.hom] [IsProper X₀.hom] :
    {c : IsomorphismClassOver k | ∃ Y : Over (Spec (CommRingCat.of k)),
      Smooth Y.hom ∧ IsProper Y.hom ∧
        (letI : Linear k X₀.left.Modules := modulesLinear k X₀
         letI : Linear k Y.left.Modules := modulesLinear k Y
         ∃ e : Stacks.Perfect.BoundedLocallyFreeComplexes.PerfectDerivedCategory X₀.left ≌
             Stacks.Perfect.BoundedLocallyFreeComplexes.PerfectDerivedCategory Y.left,
           e.functor.Linear k ∧
             ∃ h : e.functor.CommShift ℤ,
               letI := h
               e.functor.IsTriangulated) ∧
        c = isomorphismClassOver Y}.Countable
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 57.18, Tag 0G0Z](https://stacks.math.columbia.edu/tag/0G0Z)
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
