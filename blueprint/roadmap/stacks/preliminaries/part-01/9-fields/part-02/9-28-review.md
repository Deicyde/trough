---
declaration: section
origin: cited
lean: IsPurelyInseparableStacks, isPurelyInseparableStacks_iff_isPurelyInseparable, not_isPurelyInseparableStacks_of_charZero, isPurelyInseparable_iff_surjective_algebraMap_of_charZero, isPurelyInseparableStacks_iff_isPurelyInseparable_and_ringChar_ne_zero, Algebra.IsAlgebraic, Algebra.IsSeparable, IsPurelyInseparable
statement: formalized
proof: formalized
---

# 9.28 Review

Section 9.28 of the Stacks Project, [Tag 037H](https://stacks.math.columbia.edu/tag/037H). 2 tags here are carried by 7 declarations of the repository (2 in StacksCore and 5 in StacksFrontier) and 5 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b).

## Tag 030J, a definition

[Tag 030J](https://stacks.math.columbia.edu/tag/030J) in the Stacks Project.

**`IsPurelyInseparableStacks`**, a def in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/PurelyInseparable/StacksDefinition.lean, line 33](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/PurelyInseparable/StacksDefinition.lean#L33). The attribute's comment: “item (3), purely inseparable, in Stacks' own form: algebraic, characteristic `p > 0`, and a `p`-power power of every element lies in `k`”.

> **Stacks 030J (3).** An algebraic extension `K/k` is *purely inseparable* in the sense of the
> Stacks Project if the characteristic of `k` is some `p > 0` and for every `α ∈ K` there is a
> power `q = p ^ n` of `p` with `α ^ q ∈ k`. Unlike Mathlib's `IsPurelyInseparable`, this is
> never satisfied in characteristic zero.

```lean
def IsPurelyInseparableStacks : Prop
```

**`isPurelyInseparableStacks_iff_isPurelyInseparable`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/PurelyInseparable/StacksDefinition.lean, line 42](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/PurelyInseparable/StacksDefinition.lean#L42). The attribute's comment: “item (3): in characteristic `p > 0` Stacks' notion is Mathlib's `IsPurelyInseparable`”.

> **Stacks 030J (3)**, bridge to Mathlib. If `k` has characteristic a prime `p`, then `K/k` is
> purely inseparable in the sense of the Stacks Project if and only if it is so in Mathlib's sense
> `IsPurelyInseparable k K`.

```lean
theorem isPurelyInseparableStacks_iff_isPurelyInseparable (p : ℕ) [hp : Fact p.Prime]
    [CharP k p] : IsPurelyInseparableStacks k K ↔ IsPurelyInseparable k K
```

**`not_isPurelyInseparableStacks_of_charZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/PurelyInseparable/StacksDefinition.lean, line 56](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/PurelyInseparable/StacksDefinition.lean#L56). The attribute's comment: “item (3): in characteristic zero Stacks' notion never holds”.

> **Stacks 030J (3)**, characteristic zero. Over a field of characteristic zero no extension is
> purely inseparable in the sense of the Stacks Project.

```lean
theorem not_isPurelyInseparableStacks_of_charZero [CharZero k] :
    ¬ IsPurelyInseparableStacks k K
```

**`isPurelyInseparable_iff_surjective_algebraMap_of_charZero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/PurelyInseparable/StacksDefinition.lean, line 65](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/PurelyInseparable/StacksDefinition.lean#L65). The attribute's comment: “item (3): in characteristic zero Mathlib's `IsPurelyInseparable` means `K = k`”.

> In characteristic zero, Mathlib's `IsPurelyInseparable k K` holds exactly when
> `algebraMap k K` is surjective, i.e. when `K = k`; compare
> `not_isPurelyInseparableStacks_of_charZero`.

```lean
theorem isPurelyInseparable_iff_surjective_algebraMap_of_charZero [CharZero k] :
    IsPurelyInseparable k K ↔ Function.Surjective (algebraMap k K)
```

**`isPurelyInseparableStacks_iff_isPurelyInseparable_and_ringChar_ne_zero`**, a theorem in StacksFrontier (drafted, not yet reviewed), declared in [StacksFrontier/FieldTheory/PurelyInseparable/StacksDefinition.lean, line 74](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksFrontier/FieldTheory/PurelyInseparable/StacksDefinition.lean#L74). The attribute's comment: “item (3): Stacks' notion is Mathlib's `IsPurelyInseparable` plus positive characteristic”.

> **Stacks 030J (3)**, in every characteristic: `K/k` is purely inseparable in the sense of
> the Stacks Project if and only if it is so in Mathlib's sense and `k` has positive
> characteristic.

```lean
theorem isPurelyInseparableStacks_iff_isPurelyInseparable_and_ringChar_ne_zero :
    IsPurelyInseparableStacks k K ↔ IsPurelyInseparable k K ∧ ringChar k ≠ 0
```

Declarations registered for the tag:

- [`Algebra.IsAlgebraic`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.IsAlgebraic#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/PurelyInseparable/Basic.lean, line 16](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/PurelyInseparable/Basic.lean#L16) (StacksCore): “algebraic”.
- [`Algebra.IsSeparable`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Algebra.IsSeparable#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/PurelyInseparable/Basic.lean, line 17](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/PurelyInseparable/Basic.lean#L17) (StacksCore): “separable”.
- [`IsPurelyInseparable`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsPurelyInseparable#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/PurelyInseparable/Basic.lean, line 18](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/PurelyInseparable/Basic.lean#L18) (StacksCore): “purely inseparable”. References: EGA IV (4.3.1), “special case”; SGA 3 IX (5.4).
- [`Normal`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Normal#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/PurelyInseparable/Basic.lean, line 19](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/PurelyInseparable/Basic.lean#L19) (StacksCore): “normal”.
- [`IsGalois`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=IsGalois#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/PurelyInseparable/Basic.lean, line 20](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/PurelyInseparable/Basic.lean#L20) (StacksCore): “Galois”.

## Tag 031V, a lemma

[Tag 031V](https://stacks.math.columbia.edu/tag/031V) in the Stacks Project.

**`Polynomial.Separable.exists_pow_eq_of_coeff`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Separable.lean, line 24](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Separable.lean#L24). The attribute's comment: “2, without assuming L/K separable”.

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

**`exists_pow_eq_of_minpoly_coeff_of_separable`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/FieldTheory/Separable.lean, line 70](https://github.com/AxiomMath/Stacks/blob/c496df0d9beea9deaeabcea8492605f9a0a2313b/StacksCore/FieldTheory/Separable.lean#L70). The attribute's comment: “1”.

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
- [AxiomMath/Stacks at c496df0d](https://github.com/AxiomMath/Stacks/tree/c496df0d9beea9deaeabcea8492605f9a0a2313b)
