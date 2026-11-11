---
declaration: section
origin: cited
lean: CategoryTheory.IsPullback, CategoryTheory.IsPullback.isoIsPullback, CategoryTheory.Functor.id_relativelyRepresentable_iff_hasPullbacksAlong, CategoryTheory.Functor.relativelyRepresentable, CategoryTheory.Limits.HasPullbacksAlong, CategoryTheory.Functor.relativelyRepresentable.isMultiplicative, CategoryTheory.Functor.relativelyRepresentable.isStableUnderBaseChange
statement: formalized
proof: formalized
---

# 4.6 Fibre products

Section 4.6 of the Stacks Project, [Tag 001U](https://stacks.math.columbia.edu/tag/001U). 5 tags here are carried by 1 declaration of the repository (in StacksCore) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 001V, a definition

[Tag 001V](https://stacks.math.columbia.edu/tag/001V) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.IsPullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.IsPullback#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Pullback.lean, line 17](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Pullback.lean#L17) (StacksCore). References: SGA 4 I (10.1).
- [`CategoryTheory.IsPullback.isoIsPullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.IsPullback.isoIsPullback#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Pullback.lean, line 18](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Pullback.lean#L18) (StacksCore): “Uniqueness”.

## Tag 08N0, a definition

[Tag 08N0](https://stacks.math.columbia.edu/tag/08N0) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.IsPullback`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.IsPullback#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Pullback.lean, line 20](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Pullback.lean#L20) (StacksCore). References: SGA 4 I (10.1).

## Tag 001X, a definition

[Tag 001X](https://stacks.math.columbia.edu/tag/001X) in the Stacks Project.

**`CategoryTheory.Functor.id_relativelyRepresentable_iff_hasPullbacksAlong`**, a lemma in StacksCore (human-reviewed), declared in [StacksCore/CategoryTheory/Pullback.lean, line 45](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Pullback.lean#L45). The attribute's comment: “equivalent conditions for representable morphisms”. References: SGA 3 IV (1.4.0); SGA 4 I (10.7).

> The following are equivalent:
> 1. `f : x ⟶ y` is representable in the sense of stacks tag 001X.
> 2. `f : x ⟶ y` is representable relative to the identity functor.
> 3. for any `g : z ⟶ y`, the pullback of `f` and `g` exists.

```lean
lemma CategoryTheory.Functor.id_relativelyRepresentable_iff_hasPullbacksAlong
    {x y : C} (f : x ⟶ y) :
    (𝟭 C).relativelyRepresentable f ↔ HasPullbacksAlong f
```

Declarations registered for the tag:

- [`CategoryTheory.Functor.relativelyRepresentable`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.relativelyRepresentable#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Pullback.lean, line 22](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Pullback.lean#L22) (StacksCore): “When the functor is the identity, we recover 001X”. References: SGA 3 XVIII (1.4); SGA 3 XXIV (7.1.9); SGA 4 II (1.3), “more general”.
- [`CategoryTheory.Limits.HasPullbacksAlong`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Limits.HasPullbacksAlong#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Pullback.lean, line 25](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Pullback.lean#L25) (StacksCore). References: SGA 4 I (10.7); SGA 4 II (1.3).

## Tag 001Y, a lemma

[Tag 001Y](https://stacks.math.columbia.edu/tag/001Y) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.relativelyRepresentable.isMultiplicative`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.relativelyRepresentable.isMultiplicative#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Pullback.lean, line 30](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Pullback.lean#L30) (StacksCore): “the id functor is multiplicative, hence representable morphisms are stable under composition”.

## Tag 001Z, a lemma

[Tag 001Z](https://stacks.math.columbia.edu/tag/001Z) in the Stacks Project.

Declarations registered for the tag:

- [`CategoryTheory.Functor.relativelyRepresentable.isStableUnderBaseChange`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CategoryTheory.Functor.relativelyRepresentable.isStableUnderBaseChange#doc) registered with `add_to_stacks` in [StacksCore/CategoryTheory/Pullback.lean, line 27](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/CategoryTheory/Pullback.lean#L27) (StacksCore): “Representable morphisms are stable under base change”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 4.6, Tag 001U](https://stacks.math.columbia.edu/tag/001U)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
