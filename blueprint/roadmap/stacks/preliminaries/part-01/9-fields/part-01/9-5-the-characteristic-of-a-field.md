---
declaration: section
origin: cited
lean: CharZero.of_intCast_injective, CharP.charP_iff_prime_eq_zero, Subfield.bot_eq_of_charZero, Subfield.bot_eq_of_zMod_algebra
statement: formalized
proof: formalized
---

# 9.5 The characteristic of a field

Section 9.5 of the Stacks Project, [Tag 09FQ](https://stacks.math.columbia.edu/tag/09FQ). 1 tag here is carried by 1 declaration of the repository (in StacksCore) and 3 registered declarations, quoted below from [AxiomMath/Stacks](https://github.com/AxiomMath/Stacks) at commit [5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7).

## Tag 09FR, a definition

[Tag 09FR](https://stacks.math.columbia.edu/tag/09FR) in the Stacks Project.

**`CharZero.of_intCast_injective`**, a theorem in StacksCore (human-reviewed), declared in [StacksCore/Data/Int/Cast/Lemmas.lean, line 13](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Data/Int/Cast/Lemmas.lean#L13). The attribute's comment: “for the literal formulation of `ringChar R = 0`, use `ringChar.eq_zero`”.

> **Stacks 09FR** (for the literal formulation of `ringChar R = 0`, use `ringChar.eq_zero`).
> A ring `R` has characteristic zero whenever the canonical map `ℤ → R` is injective; that is, the
> condition `ℤ ⊂ R` from the Stacks definition of characteristic is equivalent to `CharZero R`.

```lean
theorem CharZero.of_intCast_injective {R : Type*} [AddGroupWithOne R]
    (h : (Int.cast : ℤ → R).Injective) : CharZero R
```

Declarations registered for the tag:

- [`CharP.charP_iff_prime_eq_zero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=CharP.charP_iff_prime_eq_zero#doc) registered with `add_to_stacks` in [StacksCore/Algebra/CharP/Basic.lean, line 11](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/Algebra/CharP/Basic.lean#L11) (StacksCore): “for the literal formulation of `ringChar R = 0`, use `ringChar.eq_zero`”. References: EGA 0 (21.1.2), “special case”.
- [`Subfield.bot_eq_of_charZero`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Subfield.bot_eq_of_charZero#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/PrimeField.lean, line 14](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/PrimeField.lean#L14) (StacksCore).
- [`Subfield.bot_eq_of_zMod_algebra`](https://leanprover-community.github.io/mathlib4_docs/find/?pattern=Subfield.bot_eq_of_zMod_algebra#doc) registered with `add_to_stacks` in [StacksCore/FieldTheory/PrimeField.lean, line 15](https://github.com/AxiomMath/Stacks/blob/5ed82d14634e8d9576bb844c7bd4e3da66d450e7/StacksCore/FieldTheory/PrimeField.lean#L15) (StacksCore).

## Depends on

No dependencies are recorded: this chapter reads the repository's source text without running Lean, which edges between declarations need.

## Sources

- [Section 9.5, Tag 09FQ](https://stacks.math.columbia.edu/tag/09FQ)
- [AxiomMath/Stacks at 5ed82d14](https://github.com/AxiomMath/Stacks/tree/5ed82d14634e8d9576bb844c7bd4e3da66d450e7)
