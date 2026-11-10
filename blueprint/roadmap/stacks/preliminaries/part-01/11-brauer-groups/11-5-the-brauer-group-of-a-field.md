---
declaration: section
origin: cited
lean: IsSimpleRing.wedderburn_artin_divisionring_unique, IsBrauerEquivalent, BrauerGroup.instCommGroup, BrauerGroup.instUniqueOfIsAlgClosed, Algebra.IsCentralSimple.isSquare_finrank
statement: formalized
proof: formalized
---

# 11.5 The Brauer group of a field

Section 11.5 of the Stacks Project, [Tag 074J](https://stacks.math.columbia.edu/tag/074J). 4 tags here are carried by 4 declarations of the repository (all in StacksCore) and 1 registered declaration, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 074K, a lemma

[Tag 074K](https://stacks.math.columbia.edu/tag/074K) in the Stacks Project.

**`IsSimpleRing.wedderburn_artin_divisionring_unique`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/RingTheory/SimpleModule/WedderburnArtin.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/SimpleModule/WedderburnArtin.lean#L25). The attribute's comment: “part (ii) and (iii)”.

```lean
theorem wedderburn_artin_divisionring_unique {n n' : ℕ} [NeZero n] [NeZero n']
    {D : Type w} [DivisionRing D] [Algebra k D] {D' : Type w} [DivisionRing D'] [Algebra k D']
    (wdb : A ≃ₐ[k] Matrix (Fin n) (Fin n) D) (wdb' : A ≃ₐ[k] Matrix (Fin n') (Fin n') D') :
    Nonempty (D ≃ₐ[k] D')
```

Declarations registered for the tag:

- [`IsBrauerEquivalent`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsBrauerEquivalent#doc) registered with `add_to_stacks` in [StacksCore/Algebra/BrauerGroup/Basic.lean, line 24](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/BrauerGroup/Basic.lean#L24) (StacksCore): “part i”.

## Tag 074L, a definition

[Tag 074L](https://stacks.math.columbia.edu/tag/074L) in the Stacks Project.

**`BrauerGroup.instCommGroup`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/Algebra/BrauerGroup/Basic.lean, line 214](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/BrauerGroup/Basic.lean#L214). References: SGA 4½ Arcata (3.1), “abelian group structure”.

```lean
instance instCommGroup : CommGroup (BrauerGroup k)
```

## Tag 074M, a lemma

[Tag 074M](https://stacks.math.columbia.edu/tag/074M) in the Stacks Project.

**`BrauerGroup.instUniqueOfIsAlgClosed`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/Algebra/BrauerGroup/AlgClosed.lean, line 28](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/BrauerGroup/AlgClosed.lean#L28). References: SGA 4½ Arcata (3.2.2), “special case”.

```lean
instance instUniqueOfIsAlgClosed : Unique (BrauerGroup k)
```

## Tag 074N, a lemma

[Tag 074N](https://stacks.math.columbia.edu/tag/074N) in the Stacks Project.

**`Algebra.IsCentralSimple.isSquare_finrank`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Algebra/Split/Basic.lean, line 155](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Split/Basic.lean#L155).

> The dimension of a central simple algebra is a perfect square.

```lean
theorem isSquare_finrank [IsSimpleRing A] [Algebra.IsCentral K A] [FiniteDimensional K A] :
    IsSquare (Module.finrank K A)
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 11.5, Tag 074J](https://stacks.math.columbia.edu/tag/074J)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
