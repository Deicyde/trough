---
declaration: abbrev
origin: cited
lean: Chapter2.Nat.mul, Chapter2.Nat.zero_mul, Chapter2.Nat.succ_mul, Chapter2.Nat.mul_comm, Chapter2.Nat.mul_eq_zero, Chapter2.Nat.mul_add, Chapter2.Nat.add_mul, Chapter2.Nat.mul_assoc, Chapter2.Nat.mul_lt_mul_of_pos_right, Chapter2.Nat.mul_gt_mul_of_pos_right, Chapter2.Nat.mul_lt_mul_of_pos_left, Chapter2.Nat.mul_gt_mul_of_pos_left, Chapter2.Nat.mul_cancel_right, Chapter2.Nat.exists_div_mod, Chapter2.Nat.pow, Chapter2.Nat.pow_zero, Chapter2.Nat.zero_pow_zero, Chapter2.Nat.pow_succ, Chapter2.Nat.sq_add_eq
statement: formalized
---

# Section 2.3: Multiplication

> This file is a translation of Section 2.3 of Analysis I to Lean 4. All numbering refers to the
> original text.
>
> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter.  In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Definition of multiplication and exponentiation for the "Chapter 2" natural numbers,
>   `Chapter2.Nat`.
>
> Note: at the end of this chapter, the `Chapter2.Nat` class will be deprecated in favor of the
> standard Mathlib class `_root_.Nat`, or `ℕ`.  However, we will develop the properties of
> `Chapter2.Nat` "by hand" for pedagogical purposes.
>
> ## Tips from past users
>
> Users of the companion who have completed the exercises in this section are welcome to send their tips for future users in this section as PRs.
>
> - (Add tip here)

*Quoted from [Analysis/Section_2_3.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_3.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 10 labelled items, carried by 19 declarations: 12 proved here, 5 stated without proof (5 of them exercises) and 2 definitions. It also has 12 declarations and 2 examples with no label, counted here but not shown.

## Definition 2.3.1

`Chapter2.Nat.mul` (abbrev, [line 36](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_3.lean#L36)). A definition.

> Definition 2.3.1 (Multiplication of natural numbers)

```lean
abbrev Nat.mul (n m : Nat) : Nat
```

`Chapter2.Nat.zero_mul` (theorem, [line 44](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_3.lean#L44)). Proved here.

> Definition 2.3.1 (Multiplication of natural numbers)
> Compare with Mathlib's `Nat.zero_mul`

```lean
theorem Nat.zero_mul (m: Nat) : 0 * m = 0
```

`Chapter2.Nat.succ_mul` (theorem, [line 48](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_3.lean#L48)). Proved here.

> Definition 2.3.1 (Multiplication of natural numbers)
> Compare with Mathlib's `Nat.succ_mul`

```lean
theorem Nat.succ_mul (n m: Nat) : (n++) * m = n * m + m
```

## Lemma 2.3.2 / Exercise 2.3.1

`Chapter2.Nat.mul_comm` (lemma, [line 72](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_3.lean#L72)). An exercise, stated without proof.

> Lemma 2.3.2 (Multiplication is commutative) / Exercise 2.3.1
> Compare with Mathlib's `Nat.mul_comm`

```lean
lemma Nat.mul_comm (n m: Nat) : n * m = m * n
```

## Lemma 2.3.3 / Exercise 2.3.2

`Chapter2.Nat.mul_eq_zero` (lemma, [line 86](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_3.lean#L86)). An exercise, stated without proof.

> Lemma 2.3.3 (Positive natural numbers have no zero divisors) / Exercise 2.3.2.
> Compare with Mathlib's `Nat.mul_eq_zero`.

```lean
lemma Nat.mul_eq_zero (n m: Nat) : n * m = 0 ↔ n = 0 ∨ m = 0
```

## Proposition 2.3.4

`Chapter2.Nat.mul_add` (theorem, [line 91](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_3.lean#L91)). Proved here.

> Proposition 2.3.4 (Distributive law)
> Compare with Mathlib's `Nat.mul_add`

```lean
theorem Nat.mul_add (a b c: Nat) : a * (b + c) = a * b + a * c
```

`Chapter2.Nat.add_mul` (theorem, [line 102](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_3.lean#L102)). Proved here.

> Proposition 2.3.4 (Distributive law)
> Compare with Mathlib's `Nat.add_mul`

```lean
theorem Nat.add_mul (a b c: Nat) : (a + b)*c = a*c + b*c
```

## Proposition 2.3.5 / Exercise 2.3.3

`Chapter2.Nat.mul_assoc` (theorem, [line 107](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_3.lean#L107)). An exercise, stated without proof.

> Proposition 2.3.5 (Multiplication is associative) / Exercise 2.3.3
> Compare with Mathlib's `Nat.mul_assoc`

```lean
theorem Nat.mul_assoc (a b c: Nat) : (a * b) * c = a * (b * c)
```

## Proposition 2.3.6

`Chapter2.Nat.mul_lt_mul_of_pos_right` (theorem, [line 129](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_3.lean#L129)). Proved here.

> Proposition 2.3.6 (Multiplication preserves order)
> Compare with Mathlib's `Nat.mul_lt_mul_of_pos_right`

```lean
theorem Nat.mul_lt_mul_of_pos_right {a b c: Nat} (h: a < b) (hc: c.IsPos) : a * c < b * c
```

`Chapter2.Nat.mul_gt_mul_of_pos_right` (theorem, [line 140](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_3.lean#L140)). Proved here.

> Proposition 2.3.6 (Multiplication preserves order)

```lean
theorem Nat.mul_gt_mul_of_pos_right {a b c: Nat} (h: a > b) (hc: c.IsPos) :
    a * c > b * c
```

`Chapter2.Nat.mul_lt_mul_of_pos_left` (theorem, [line 145](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_3.lean#L145)). Proved here.

> Proposition 2.3.6 (Multiplication preserves order)
> Compare with Mathlib's `Nat.mul_lt_mul_of_pos_left`

```lean
theorem Nat.mul_lt_mul_of_pos_left {a b c: Nat} (h: a < b) (hc: c.IsPos) : c * a < c * b
```

`Chapter2.Nat.mul_gt_mul_of_pos_left` (theorem, [line 150](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_3.lean#L150)). Proved here.

> Proposition 2.3.6 (Multiplication preserves order)

```lean
theorem Nat.mul_gt_mul_of_pos_left {a b c: Nat} (h: a > b) (hc: c.IsPos) :
    c * a > c * b
```

## Corollary 2.3.7

`Chapter2.Nat.mul_cancel_right` (lemma, [line 155](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_3.lean#L155)). Proved here.

> Corollary 2.3.7 (Cancellation law)
> Compare with Mathlib's `Nat.mul_right_cancel`

```lean
lemma Nat.mul_cancel_right {a b c: Nat} (h: a * c = b * c) (hc: c.IsPos) : a = b
```

## Proposition 2.3.9 / Exercise 2.3.5

`Chapter2.Nat.exists_div_mod` (theorem, [line 183](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_3.lean#L183)). An exercise, stated without proof.

> Proposition 2.3.9 (Euclid's division lemma) / Exercise 2.3.5
> Compare with Mathlib's `Nat.mod_eq_iff`

```lean
theorem Nat.exists_div_mod (n:Nat) {q: Nat} (hq: q.IsPos) :
    ∃ m r: Nat, 0 ≤ r ∧ r < q ∧ n = m * q + r
```

## Definition 2.3.11

`Chapter2.Nat.pow` (abbrev, [line 188](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_3.lean#L188)). A definition.

> Definition 2.3.11 (Exponentiation for natural numbers)

```lean
abbrev Nat.pow (m n: Nat) : Nat
```

`Chapter2.Nat.pow_zero` (theorem, [line 196](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_3.lean#L196)). Proved here.

> Definition 2.3.11 (Exponentiation for natural numbers)
> Compare with Mathlib's `Nat.pow_zero`

```lean
theorem Nat.pow_zero (m: Nat) : m ^ (0:Nat) = 1
```

`Chapter2.Nat.zero_pow_zero` (theorem, [line 200](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_3.lean#L200)). Proved here.

> Definition 2.3.11 (Exponentiation for natural numbers)

```lean
theorem Nat.zero_pow_zero : (0:Nat) ^ 0 = 1
```

`Chapter2.Nat.pow_succ` (theorem, [line 204](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_3.lean#L204)). Proved here.

> Definition 2.3.11 (Exponentiation for natural numbers)
> Compare with Mathlib's `Nat.pow_succ`

```lean
theorem Nat.pow_succ (m n: Nat) : (m:Nat) ^ n++ = m^n * m
```

## Exercise 2.3.4

`Chapter2.Nat.sq_add_eq` (theorem, [line 213](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_3.lean#L213)). An exercise, stated without proof.

> Exercise 2.3.4

```lean
theorem Nat.sq_add_eq (a b: Nat) :
    (a + b) ^ (2 : Nat) = a ^ (2 : Nat) + 2 * a * b + b ^ (2 : Nat)
```

## Depends on

- [Section 2.2: Addition](section-2-2.md)

## Sources

- [Analysis/Section_2_3.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_3.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_2_3/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_2_3.html)
