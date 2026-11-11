---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.Decent.closure_iUnion_range_residuePairMap_meets_diagonal, AlgebraicGeometry.Space.isDecentSpace_of_isAbsolutelyLocallySeparated
statement: formalized
proof: formalized
---

# 68.15 Locally separated spaces

Section 68.15 of the Stacks Project, [Tag 088H](https://stacks.math.columbia.edu/tag/088H). 2 tags here are carried by 2 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 088I, a lemma

[Tag 088I](https://stacks.math.columbia.edu/tag/088I) in the Stacks Project.

**`AlgebraicGeometry.Space.Decent.closure_iUnion_range_residuePairMap_meets_diagonal`**, a lemma in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/InfiniteResidueFields.lean, line 225](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/InfiniteResidueFields.lean#L225).

> The closure of the union of the off-diagonal products of residue-field spectra
> meets the diagonal in `Spec(A ⊗ℤ A)`.

```lean
lemma closure_iUnion_range_residuePairMap_meets_diagonal (_hp : Function.Injective p) :
    (closure (⋃ n, ⋃ m, ⋃ (_ : n ≠ m),
        range (PrimeSpectrum.comap (residuePairMap A k p n m))) ∩
      range (PrimeSpectrum.comap (diagonalMap A))).Nonempty
```

## Tag 088J, a lemma

[Tag 088J](https://stacks.math.columbia.edu/tag/088J) in the Stacks Project.

**`AlgebraicGeometry.Space.isDecentSpace_of_isAbsolutelyLocallySeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocallySeparated.lean, line 1018](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocallySeparated.lean#L1018).

> **Stacks 088J.** A locally separated algebraic space is decent.

```lean
theorem isDecentSpace_of_isAbsolutelyLocallySeparated (hZ : B.Contains (⊤_ Scheme.{u}))
    (hX : IsAlgebraicSpace B S hS X) (hsep : IsAbsolutelyLocallySeparated B S hS hZ X) :
    IsDecentSpace B S hS X
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 68.15, Tag 088H](https://stacks.math.columbia.edu/tag/088H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
