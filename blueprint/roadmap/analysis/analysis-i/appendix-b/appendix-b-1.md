---
declaration: def
origin: cited
lean: AppendixB.Digit, AppendixB.PosintDecimal, AppendixB.PosintDecimal.ten_eq_ten, AppendixB.PosintDecimal.exists_unique, AppendixB.PosintDecimal.sum_digit_lt
statement: formalized
---

# Appendix B.1: The decimal representation of natural numbers

> Am implementation of the decimal representation of Mathlib's natural numbers `ℕ`.
>
> This is separate from the way decimal numerals are already represenated in Mathlib via the `OfNat` typeclass.

*Quoted from [Analysis/Appendix_B_1.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_B_1.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 5 labelled items, carried by 5 declarations: 2 proved here, 1 stated without proof (1 of them exercises) and 2 definitions. It also has 51 declarations and 13 examples with no label, counted here but not shown.

## Definition B.1.1

`AppendixB.Digit` (def, [line 27](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_B_1.lean#L27)). A definition.

> Definition B.1.1

```lean
def Digit
```

## Definition B.1.2

`AppendixB.PosintDecimal` (structure, [line 78](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_B_1.lean#L78)). A definition.

> Definition B.1.2

```lean
structure PosintDecimal
```

## Remark B.1.3

`AppendixB.PosintDecimal.ten_eq_ten` (theorem, [line 133](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_B_1.lean#L133)). Proved here.

> Remark B.1.3

```lean
theorem PosintDecimal.ten_eq_ten : (mk' 1 [0] (by decide):ℕ) = 10
```

## Theorem B.1.4

`AppendixB.PosintDecimal.exists_unique` (theorem, [line 194](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_B_1.lean#L194)). Proved here.

> Theorem B.1.4 (Uniqueness and existence of decimal representations)

```lean
theorem PosintDecimal.exists_unique (n:ℕ) : n > 0 → ∃! p:PosintDecimal, (p:ℕ) = n
```

## Exercise B.1.1

`AppendixB.PosintDecimal.sum_digit_lt` (theorem, [line 320](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_B_1.lean#L320)). An exercise, stated without proof.

> Exercise B.1.1

```lean
theorem PosintDecimal.sum_digit_lt (p q:PosintDecimal) (i:ℕ) :
  p.sum_digit q i < 10
```

## Depends on

Its Lean file imports no other section's file.

## Sources

- [Analysis/Appendix_B_1.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Appendix_B_1.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Appendix_B_1/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Appendix_B_1.html)
