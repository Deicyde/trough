---
declaration: section
origin: cited
lean: Max.max, Subalgebra.linearDisjoint_iff_injective, perfectClosure.isGalois, separableClosure_sup_perfectClosure, separableClosure.isPurelyInseparable, perfectClosure, perfectClosure.isPurelyInseparable, separableClosure_inf_perfectClosure
statement: formalized
proof: formalized
---

# 9.27 Linearly disjoint extensions

Section 9.27 of the Stacks Project, [Tag 09IC](https://stacks.math.columbia.edu/tag/09IC). 3 tags here are carried by 2 declarations of the repository (all in StacksCore) and 7 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09ID, a definition

[Tag 09ID](https://stacks.math.columbia.edu/tag/09ID) in the Stacks Project.

Declarations registered for the tag:

- [`Max.max`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Max.max#doc) registered with `add_to_stacks` in [StacksCore/Algebra/Algebra/Subalgebra/Disjoint.lean, line 9](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/Algebra/Subalgebra/Disjoint.lean#L9) (StacksCore): “The compositum of two `IntermediateField`s is just their supremum”.

## Tag 09IF, a definition

[Tag 09IF](https://stacks.math.columbia.edu/tag/09IF) in the Stacks Project.

Declarations registered for the tag:

- [`Subalgebra.linearDisjoint_iff_injective`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Subalgebra.linearDisjoint_iff_injective#doc) registered with `add_to_stacks` in [StacksCore/RingTheory/LinearDisjoint.lean, line 12](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/RingTheory/LinearDisjoint.lean#L12) (StacksCore).

## Tag 030M, a lemma

[Tag 030M](https://stacks.math.columbia.edu/tag/030M) in the Stacks Project.

**`perfectClosure.isGalois`**, an instance in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/PurelyInseparable/PerfectClosure.lean, line 64](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/PurelyInseparable/PerfectClosure.lean#L64). The attribute's comment: “Second part of 2”.

> **Stacks 030N** (second part of 2).
> For a normal field extension `E/F`, the extension `E` over the perfect closure of `F`
> in `E` is Galois.

```lean
instance perfectClosure.isGalois [Normal F E] : IsGalois (perfectClosure F E) E
```

**`separableClosure_sup_perfectClosure`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/PurelyInseparable/PerfectClosure.lean, line 97](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/PurelyInseparable/PerfectClosure.lean#L97). The attribute's comment: “Second part of 3”.

> **Stacks 030N** (second part of 3).
> For a normal field extension `E/F`, the separable closure and the perfect closure of
> `F` in `E` together generate the whole extension `E`.

```lean
theorem separableClosure_sup_perfectClosure [Normal F E] :
    separableClosure F E ⊔ perfectClosure F E = ⊤
```

Declarations registered for the tag:

- [`separableClosure.isPurelyInseparable`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=separableClosure.isPurelyInseparable#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/PurelyInseparable/Basic.lean, line 13](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/PurelyInseparable/Basic.lean#L13) (StacksCore): “Second part of 1”.
- [`perfectClosure`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=perfectClosure#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/PurelyInseparable/PerfectClosure.lean, line 13](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/PurelyInseparable/PerfectClosure.lean#L13) (StacksCore).
- [`perfectClosure.isPurelyInseparable`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=perfectClosure.isPurelyInseparable#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/PurelyInseparable/PerfectClosure.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/PurelyInseparable/PerfectClosure.lean#L15) (StacksCore): “First part of 2”.
- [`separableClosure_inf_perfectClosure`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=separableClosure_inf_perfectClosure#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/PurelyInseparable/PerfectClosure.lean, line 16](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/PurelyInseparable/PerfectClosure.lean#L16) (StacksCore): “First part of 3”.
- [`separableClosure.isGalois`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=separableClosure.isGalois#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/SeparableClosure.lean, line 11](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/SeparableClosure.lean#L11) (StacksCore): “First part of 1”.

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 9.27, Tag 09IC](https://stacks.math.columbia.edu/tag/09IC)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
