---
declaration: section
origin: cited
lean: AlgebraicGeometry.Space.forall_existsUnique_minimalPrimes_iff_forall_existsUnique_component, AlgebraicGeometry.Space.forall_existsUnique_component_iff_forall_isUnibranchAt, AlgebraicGeometry.Space.tfae_localIrreducibility, AlgebraicGeometry.Space.IsUnibranchAt, AlgebraicGeometry.Space.IsUnibranch, AlgebraicGeometry.Space.hasMinimalPrimeCount_iff_hasComponentCount, AlgebraicGeometry.Space.hasComponentCount_iff_hasBranchCount, AlgebraicGeometry.Space.tfae_hasBranchCount
statement: formalized
proof: formalized
---

# 68.24 Local irreducibility

Section 68.24 of the Stacks Project, [Tag 0DQ5](https://stacks.math.columbia.edu/tag/0DQ5). 4 tags here are carried by 11 declarations of the repository (all in StacksFrontier), quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 0DQ6, a lemma

[Tag 0DQ6](https://stacks.math.columbia.edu/tag/0DQ6) in the Stacks Project.

**`AlgebraicGeometry.Space.forall_existsUnique_minimalPrimes_iff_forall_existsUnique_component`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocalIrreducibility.lean, line 220](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocalIrreducibility.lean#L220). The attribute's comment: “conditions (1) and (2)”.

> **Stacks 0DQ6, conditions (1) and (2).** The local ring of every elementary étale
> neighbourhood of `x` at its distinguished point has a unique minimal prime exactly when exactly
> one irreducible component of every such neighbourhood passes through its distinguished point.

```lean
theorem forall_existsUnique_minimalPrimes_iff_forall_existsUnique_component :
    (∀ U : ElementaryEtaleNeighborhood B S hS X hX x,
        ∃! q : Ideal (U.scheme.left.1.presheaf.stalk U.point),
          q ∈ minimalPrimes (U.scheme.left.1.presheaf.stalk U.point)) ↔
      ∀ U : ElementaryEtaleNeighborhood B S hS X hX x,
        ∃! Z : irreducibleComponents U.scheme.left.1,
          U.point ∈ (Z : Set U.scheme.left.1)
```

**`AlgebraicGeometry.Space.forall_existsUnique_component_iff_forall_isUnibranchAt`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocalIrreducibility.lean, line 238](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocalIrreducibility.lean#L238). The attribute's comment: “conditions (2) and (3)”.

> **Stacks 0DQ6, conditions (2) and (3).** Exactly one irreducible component of every
> elementary étale neighbourhood of `x` passes through its distinguished point exactly when the
> local ring of every such neighbourhood at its distinguished point is unibranch.

```lean
theorem forall_existsUnique_component_iff_forall_isUnibranchAt :
    (∀ U : ElementaryEtaleNeighborhood B S hS X hX x,
        ∃! Z : irreducibleComponents U.scheme.left.1,
          U.point ∈ (Z : Set U.scheme.left.1)) ↔
      ∀ U : ElementaryEtaleNeighborhood B S hS X hX x,
        _root_.AlgebraicGeometry.IsUnibranchAt U.scheme.left.1 U.point
```

**`AlgebraicGeometry.Space.tfae_localIrreducibility`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocalIrreducibility.lean, line 414](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocalIrreducibility.lean#L414). The attribute's comment: “(1)-(4) equivalent”.

> **Stacks 0DQ6.** For a point of a decent algebraic space the four conditions of the source are
> equivalent: every elementary étale neighbourhood has a local ring with a unique minimal prime, has
> a unique irreducible component through its distinguished point, and has a unibranch local ring;
> and the henselian local ring at the point has a unique minimal prime.

```lean
theorem tfae_localIrreducibility (hDecent : IsDecentSpace B S hS X) :
    List.TFAE
      [∀ U : ElementaryEtaleNeighborhood B S hS X hX x,
          ∃! q : Ideal (U.scheme.left.1.presheaf.stalk U.point),
            q ∈ minimalPrimes (U.scheme.left.1.presheaf.stalk U.point),
        ∀ U : ElementaryEtaleNeighborhood B S hS X hX x,
          ∃! Z : irreducibleComponents U.scheme.left.1,
            U.point ∈ (Z : Set U.scheme.left.1),
        ∀ U : ElementaryEtaleNeighborhood B S hS X hX x,
          _root_.AlgebraicGeometry.IsUnibranchAt U.scheme.left.1 U.point,
        ∃! p : Ideal (henselianLocalRing B S hS X hX x hDecent : Type (u + 1)),
          p ∈ minimalPrimes (henselianLocalRing B S hS X hX x hDecent : Type (u + 1))]
```

## Tag 0DQ7, a definition

[Tag 0DQ7](https://stacks.math.columbia.edu/tag/0DQ7) in the Stacks Project.

**`AlgebraicGeometry.Space.IsUnibranchAt`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocalIrreducibility.lean, line 476](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocalIrreducibility.lean#L476). The attribute's comment: “unibranch at a point”.

> **Stacks 0DQ7, unibranch at a point.** A decent algebraic space is *unibranch at `x`* when
> the local ring of every elementary étale neighbourhood of `x` at its distinguished point is
> unibranch, which is condition (3) of Tag 0DQ6.

```lean
abbrev IsUnibranchAt (_hDecent : IsDecentSpace B S hS X) : Prop
```

**`AlgebraicGeometry.Space.IsUnibranch`**, an abbrev in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocalIrreducibility.lean, line 483](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocalIrreducibility.lean#L483). The attribute's comment: “unibranch”.

> **Stacks 0DQ7, unibranch.** A decent algebraic space is *unibranch* when it is unibranch at
> every one of its points.

```lean
abbrev IsUnibranch (hDecent : IsDecentSpace B S hS X) : Prop
```

## Tag 0DQ8, a lemma

[Tag 0DQ8](https://stacks.math.columbia.edu/tag/0DQ8) in the Stacks Project.

**`AlgebraicGeometry.Space.hasMinimalPrimeCount_iff_hasComponentCount`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocalIrreducibility.lean, line 291](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocalIrreducibility.lean#L291). The attribute's comment: “conditions (1) and (2)”.

> **Stacks 0DQ8, conditions (1) and (2).** A point of a presheaf on the big fppf site has
> minimal-prime count `n` on its elementary étale neighbourhoods exactly when it has
> irreducible-component count `n` on them: the two counts agree neighbourhood by
> neighbourhood.

```lean
theorem hasMinimalPrimeCount_iff_hasComponentCount (n : ℕ) :
    HasMinimalPrimeCountOnElementaryNeighborhoods B S hS X hX x n ↔
      HasComponentCountOnElementaryNeighborhoods B S hS X hX x n
```

**`AlgebraicGeometry.Space.hasComponentCount_iff_hasBranchCount`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocalIrreducibility.lean, line 348](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocalIrreducibility.lean#L348). The attribute's comment: “conditions (2) and (3)”.

> **Stacks 0DQ8, conditions (2) and (3).** A point of a presheaf on the big fppf site has
> irreducible-component count `n` on its elementary étale neighbourhoods exactly when it has
> branch count `n` on them.

```lean
theorem hasComponentCount_iff_hasBranchCount (n : ℕ) :
    HasComponentCountOnElementaryNeighborhoods B S hS X hX x n ↔
      HasBranchCountOnElementaryNeighborhoods B S hS X hX x n
```

**`AlgebraicGeometry.Space.tfae_hasBranchCount`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocalIrreducibility.lean, line 457](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocalIrreducibility.lean#L457). The attribute's comment: “(1)-(4) equivalent”.

> **Stacks 0DQ8.** For a point of a decent algebraic space and a natural number `n` the four
> conditions of the source are equivalent: the minimal primes of the local ring, the irreducible
> components through the distinguished point, and the branches each number at most `n` over all
> elementary étale neighbourhoods with `n` attained at one of them; and the henselian local ring at
> the point has exactly `n` minimal primes.

```lean
theorem tfae_hasBranchCount (hDecent : IsDecentSpace B S hS X) (n : ℕ) :
    List.TFAE
      [HasMinimalPrimeCountOnElementaryNeighborhoods B S hS X hX x n,
        HasComponentCountOnElementaryNeighborhoods B S hS X hX x n,
        HasBranchCountOnElementaryNeighborhoods B S hS X hX x n,
        Set.encard (minimalPrimes (henselianLocalRing B S hS X hX x hDecent : Type (u + 1))) =
          (n : ℕ∞)]
```

## Tag 0DQ9, a definition

[Tag 0DQ9](https://stacks.math.columbia.edu/tag/0DQ9) in the Stacks Project.

**`AlgebraicGeometry.Space.numberOfBranches`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocalIrreducibility.lean, line 511](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocalIrreducibility.lean#L511).

> **Stacks 0DQ9.** The number of branches of a decent algebraic space at a point: the natural
> number satisfying the equivalent conditions of Tag 0DQ8 if there is one, and `⊤` otherwise.

```lean
def numberOfBranches (_hDecent : IsDecentSpace B S hS X) : ℕ∞
```

**`AlgebraicGeometry.Space.numberOfBranches_eq_top_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocalIrreducibility.lean, line 518](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocalIrreducibility.lean#L518). The attribute's comment: “infinite value”.

> The number of branches of a decent algebraic space at a point is infinite exactly when no
> natural number satisfies the equivalent conditions of Tag 0DQ8.

```lean
theorem numberOfBranches_eq_top_iff (hDecent : IsDecentSpace B S hS X) :
    numberOfBranches B S hS X hX x hDecent = ⊤ ↔
      ∀ n : ℕ, ¬ HasBranchCountOnElementaryNeighborhoods B S hS X hX x n
```

**`AlgebraicGeometry.Space.numberOfBranches_eq_nat_iff`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocalIrreducibility.lean, line 528](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksFrontier/AlgebraicGeometry/Spaces/Decent/LocalIrreducibility.lean#L528). The attribute's comment: “finite value”.

> A finite value of the number of branches of a decent algebraic space at a point is exactly
> the value appearing in the equivalent conditions of Tag 0DQ8.

```lean
theorem numberOfBranches_eq_nat_iff (hDecent : IsDecentSpace B S hS X) (n : ℕ) :
    numberOfBranches B S hS X hX x hDecent = (n : ℕ∞) ↔
      HasBranchCountOnElementaryNeighborhoods B S hS X hX x n
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 68.24, Tag 0DQ5](https://stacks.math.columbia.edu/tag/0DQ5)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
