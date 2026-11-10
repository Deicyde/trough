---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.valuativeCriterion_uniqueness_of_isSeparated, AlgebraicGeometry.Space.isSeparated_of_isQuasiSeparated_of_valuativeCriterion_uniqueness, AlgebraicGeometry.Space.isSeparated_and_universallyClosed_tfae_of_isQuasiCompact_of_isQuasiSeparated
statement: formalized
proof: formalized
---

# 67.43 Valuative criterion of separatedness

Section 67.43 of the Stacks Project, [Tag 03KT](https://stacks.math.columbia.edu/tag/03KT). 3 tags here are carried by 3 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 03KU, a lemma

[Tag 03KU](https://stacks.math.columbia.edu/tag/03KU) in the Stacks Project.

**`AlgebraicGeometry.Space.valuativeCriterion_uniqueness_of_isSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ValuativeCriteria.lean, line 292](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ValuativeCriteria.lean#L292). References: EGA II (7.3.2), “more general”.

> **Stacks 03KU.** A separated morphism of algebraic spaces satisfies the uniqueness part
> of the valuative criterion.
>
> Two lifts of a valuative square assemble into a morphism `Spec R ⟶ X ×_Y X`; the base change
> of the relative diagonal along it is a closed immersion of schemes which is surjective on
> global sections, because the generic point of `Spec R` lifts through it, hence an
> isomorphism. The two lifts therefore agree.

```lean
theorem valuativeCriterion_uniqueness_of_isSeparated (f : X ⟶ Y)
    (hf : IsSeparated B S hS f) : ValuativeCriterion.Uniqueness f
```

## Tag 03KV, a lemma

[Tag 03KV](https://stacks.math.columbia.edu/tag/03KV) in the Stacks Project.

**`AlgebraicGeometry.Space.isSeparated_of_isQuasiSeparated_of_valuativeCriterion_uniqueness`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ValuativeCriteria.lean, line 1099](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Morphisms/ValuativeCriteria.lean#L1099).

> **Stacks 03KV.** A quasi-separated morphism of algebraic spaces over `S` which satisfies
> the uniqueness part of the valuative criterion is separated.
>
> Quasi-separatedness is quasi-compactness of the relative diagonal, and the diagonal satisfies
> the existence part of the criterion, so by Stacks 03KA it is universally closed. Being also
> separated, locally of finite type and locally quasi-finite (Stacks 03HK), every represented
> base change of it is a proper locally quasi-finite morphism of schemes, hence finite; being in
> addition a monomorphism, it is a closed immersion.

```lean
theorem isSeparated_of_isQuasiSeparated_of_valuativeCriterion_uniqueness
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hqs : IsQuasiSeparated B S hS f) (hu : ValuativeCriterion.Uniqueness f) :
    IsSeparated B S hS f
```

## Tag 0A3Z, a lemma

[Tag 0A3Z](https://stacks.math.columbia.edu/tag/0A3Z) in the Stacks Project.

**`AlgebraicGeometry.Space.isSeparated_and_universallyClosed_tfae_of_isQuasiCompact_of_isQuasiSeparated`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Valuative/SeparatedUniversallyClosed.lean, line 49](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Valuative/SeparatedUniversallyClosed.lean#L49).

> For a quasi-compact and quasi-separated morphism `f : X ⟶ Y` of algebraic spaces over `S`,
> being separated and universally closed, satisfying the valuative criterion of Stacks 03IX, and
> having exactly one dotted arrow in every valuative square over the given valuation ring are
> equivalent.

```lean
public theorem isSeparated_and_universallyClosed_tfae_of_isQuasiCompact_of_isQuasiSeparated
    (hX : IsAlgebraicSpace B S hS X) (hY : IsAlgebraicSpace B S hS Y) (f : X ⟶ Y)
    (hqc : IsQuasiCompact B S hS f) (hqs : IsQuasiSeparated B S hS f) :
    List.TFAE
      [IsSeparated B S hS f ∧ UniversallyClosed B S hS f,
        ValuativeCriterion f,
        ∀ q : ValuativeSquare f, Nonempty q.Lift ∧ Subsingleton q.Lift]
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 67.43, Tag 03KT](https://stacks.math.columbia.edu/tag/03KT)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
