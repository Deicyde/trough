---
declaration: section
origin: cited
lean: CategoryTheory.FilteredObject.IsFilteredInjective, CategoryTheory.FiniteFilteredObject, CochainComplex.filteredQuasiIso, CategoryTheory.FiniteFilteredObject.filteredAcyclic
statement: formalized
proof: formalized
---

# 111.30 Filtered derived category

Section 111.30 of the Stacks Project, [Tag 0287](https://stacks.math.columbia.edu/tag/0287). 4 tags here are carried by 1 declaration of the repository (in StacksFrontier) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 028A, a definition

[Tag 028A](https://stacks.math.columbia.edu/tag/028A) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.FilteredObject.IsFilteredInjective`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Defs.lean#L243), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Exercises/FilteredObject.lean, line 47](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Exercises/FilteredObject.lean#L47) (StacksFrontier).

## Tag 028B, a definition

[Tag 028B](https://stacks.math.columbia.edu/tag/028B) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.FiniteFilteredObject`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Defs.lean#L236), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Exercises/FilteredObject.lean, line 48](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Exercises/FilteredObject.lean#L48) (StacksFrontier).

## Tag 028D, a definition

[Tag 028D](https://stacks.math.columbia.edu/tag/028D) in the Stacks Project.

Declarations registered for the tag:

- [`CochainComplex.filteredQuasiIso`](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Algebra/Homology/DerivedCategory/Filtered/Defs.lean#L330), declared in the repository, registered with `add_to_stacks` in [StacksFrontier/Exercises/FilteredObject.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Exercises/FilteredObject.lean#L49) (StacksFrontier).

## Tag 028E, a definition

[Tag 028E](https://stacks.math.columbia.edu/tag/028E) in the Stacks Project.

**`CategoryTheory.FiniteFilteredObject.filteredAcyclic`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/Exercises/FilteredObject.lean, line 58](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/Exercises/FilteredObject.lean#L58).

> A complex of finite filtered objects is filtered acyclic when every graded-piece complex
> is acyclic.

```lean
abbrev filteredAcyclic (A : Type u) [Category.{v} A] [Abelian A]
    (K : CochainComplex (FiniteFilteredObject A) ℤ) : Prop
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 111.30, Tag 0287](https://stacks.math.columbia.edu/tag/0287)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
