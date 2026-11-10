---
declaration: section
origin: cited
lean: Algebra.IsAlgebraic, Algebra.IsSeparable, IsPurelyInseparable, Normal, IsGalois, Polynomial.Separable.exists_pow_eq_of_coeff, exists_pow_eq_of_minpoly_coeff_of_separable
statement: formalized
proof: formalized
---

# 9.28 Review

Section 9.28 of the Stacks Project, [Tag 037H](https://stacks.math.columbia.edu/tag/037H). 2 tags here are carried by 2 declarations of the repository (all in StacksCore) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 030J, a definition

[Tag 030J](https://stacks.math.columbia.edu/tag/030J) in the Stacks Project.

Declarations registered for the tag:

- [`Algebra.IsAlgebraic`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.IsAlgebraic#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/PurelyInseparable/Basic.lean, line 16](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/PurelyInseparable/Basic.lean#L16) (StacksCore): “algebraic”.
- [`Algebra.IsSeparable`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.IsSeparable#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/PurelyInseparable/Basic.lean, line 17](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/PurelyInseparable/Basic.lean#L17) (StacksCore): “separable”.
- [`IsPurelyInseparable`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsPurelyInseparable#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/PurelyInseparable/Basic.lean, line 18](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/PurelyInseparable/Basic.lean#L18) (StacksCore): “purely inseparable”. References: EGA IV (4.3.1), “special case”; SGA 3 IX (5.4).
- [`Normal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Normal#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/PurelyInseparable/Basic.lean, line 19](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/PurelyInseparable/Basic.lean#L19) (StacksCore): “normal”.
- [`IsGalois`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsGalois#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/PurelyInseparable/Basic.lean, line 20](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/PurelyInseparable/Basic.lean#L20) (StacksCore): “Galois”.

## Tag 031V, a lemma

[Tag 031V](https://stacks.math.columbia.edu/tag/031V) in the Stacks Project.

**`Polynomial.Separable.exists_pow_eq_of_coeff`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Separable.lean, line 24](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/Separable.lean#L24). The attribute's comment: “2, without assuming L/K separable”.

> **Stacks 031V** (part 2 — the general statement).
> Let `K` be a field of characteristic `p > 0`, `L/K` a field extension, and `x ∈ L`.
> If `f ∈ K[X]` satisfies
>   (a) `x` is a root of `f`,
>   (b) `f` is a separable polynomial, and
>   (c) every coefficient of `f` is a `p`-th power in `K`,
> then `x` is a `p`-th power in `L`.

```lean
theorem Polynomial.Separable.exists_pow_eq_of_coeff {p : ℕ}
    {K L : Type*} [Field K] [CharP K p] [Field L] [Algebra K L] {x : L} {f : Polynomial K}
    (h₁ : f.Separable) (h₂ : f.aeval x = 0) (h₃ : ∀ i, ∃ b : K, b ^ p = f.coeff i) :
    ∃ y, y ^ p = x
```

**`exists_pow_eq_of_minpoly_coeff_of_separable`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Separable.lean, line 70](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/Separable.lean#L70). The attribute's comment: “1”.

> **Stacks 031V** (part 1).
> Let `K` be a field of characteristic `p > 0`, `L/K` a separable extension, and `x ∈ L`.
> If every coefficient of the minimal polynomial of `x` over `K` is a `p`-th power in `K`,
> then `x` is a `p`-th power in `L`.

```lean
theorem exists_pow_eq_of_minpoly_coeff_of_separable {p : ℕ}
    {K : Type*} [Field K] [CharP K p] {L : Type*} [Field L] [Algebra K L] [Algebra.IsSeparable K L]
    {x : L} (h₁ : ∀ i, ∃ b : K, b ^ p = (minpoly K x).coeff i) :
    ∃ y, y ^ p = x
```

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 9.28, Tag 037H](https://stacks.math.columbia.edu/tag/037H)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
