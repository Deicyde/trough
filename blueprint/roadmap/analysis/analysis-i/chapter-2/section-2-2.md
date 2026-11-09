---
declaration: abbrev
origin: cited
lean: Chapter2.Nat.add, Chapter2.Nat.add_zero, Chapter2.Nat.add_succ, Chapter2.Nat.add_comm, Chapter2.Nat.add_assoc, Chapter2.Nat.add_left_cancel, Chapter2.Nat.IsPos, Chapter2.Nat.add_pos_left, Chapter2.Nat.add_eq_zero, Chapter2.Nat.uniq_succ_eq, Chapter2.Nat.instLE, Chapter2.Nat.instLT, Chapter2.Nat.ge_refl, Chapter2.Nat.trichotomous, Chapter2.Nat.strong_induction, Chapter2.Nat.backwards_induction, Chapter2.Nat.induction_from
statement: formalized
---

# Section 2.2: Addition

> This file is a translation of Section 2.2 of Analysis I to Lean 4.  All numbering refers to the
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
> - Definition of addition and order for the "Chapter 2" natural numbers, `Chapter2.Nat`.
> - Establishment of basic properties of addition and order.
>
> Note: at the end of this chapter, the `Chapter2.Nat` class will be deprecated in favor of the
> standard Mathlib class `_root_.Nat`, or `ℕ`.  However, we will develop the properties of
> `Chapter2.Nat` "by hand" for pedagogical purposes.
>
> ## Tips from past users
>
> Users of the companion who have completed the exercises in this section are welcome to send their
> tips for future users in this section as PRs.
>
> - (Add tip here)

*Quoted from [Analysis/Section_2_2.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_2.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 16 labelled items, carried by 17 declarations: 6 proved here, 7 stated without proof (7 of them exercises) and 4 definitions. It also has 36 declarations and 7 examples with no label, counted here but not shown.

## Definition 2.2.1

`Chapter2.Nat.add` (abbrev, [line 38](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_2.lean#L38)). A definition.

> Definition 2.2.1. (Addition of natural numbers).
> Compare with Mathlib's `Nat.add`

```lean
abbrev Nat.add (n m : Nat) : Nat
```

## Lemma 2.2.2

`Chapter2.Nat.add_zero` (lemma, [line 66](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_2.lean#L66)). Proved here.

> Lemma 2.2.2 (`n + 0 = n`). Compare with Mathlib's `Nat.add_zero`.

```lean
lemma Nat.add_zero (n:Nat) : n + 0 = n
```

## Lemma 2.2.3

`Chapter2.Nat.add_succ` (lemma, [line 76](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_2.lean#L76)). Proved here.

> Lemma 2.2.3 (`n+(m++) = (n+m)++`). Compare with Mathlib's `Nat.add_succ`.

```lean
lemma Nat.add_succ (n m:Nat) : n + (m++) = (n + m)++
```

## Proposition 2.2.4

`Chapter2.Nat.add_comm` (theorem, [line 90](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_2.lean#L90)). Proved here.

> Proposition 2.2.4 (Addition is commutative). Compare with Mathlib's `Nat.add_comm`

```lean
theorem Nat.add_comm (n m:Nat) : n + m = m + n
```

## Proposition 2.2.5 / Exercise 2.2.1

`Chapter2.Nat.add_assoc` (theorem, [line 100](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_2.lean#L100)). An exercise, stated without proof.

> Proposition 2.2.5 (Addition is associative) / Exercise 2.2.1
> Compare with Mathlib's `Nat.add_assoc`.

```lean
theorem Nat.add_assoc (a b c:Nat) : (a + b) + c = a + (b + c)
```

## Proposition 2.2.6

`Chapter2.Nat.add_left_cancel` (theorem, [line 105](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_2.lean#L105)). Proved here.

> Proposition 2.2.6 (Cancellation law).
> Compare with Mathlib's `Nat.add_left_cancel`.

```lean
theorem Nat.add_left_cancel (a b c:Nat) (habc: a + b = a + c) : b = c
```

## Definition 2.2.7

`Chapter2.Nat.IsPos` (def, [line 130](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_2.lean#L130)). A definition.

> Definition 2.2.7 (Positive natural numbers).

```lean
def Nat.IsPos (n:Nat) : Prop
```

## Proposition 2.2.8

`Chapter2.Nat.add_pos_left` (theorem, [line 136](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_2.lean#L136)). Proved here.

> Proposition 2.2.8 (positive plus natural number is positive).
> Compare with Mathlib's `Nat.add_pos_left`.

```lean
theorem Nat.add_pos_left {a:Nat} (b:Nat) (ha: a.IsPos) : (a + b).IsPos
```

## Corollary 2.2.9

`Chapter2.Nat.add_eq_zero` (theorem, [line 154](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_2.lean#L154)). Proved here.

> Corollary 2.2.9 (if sum vanishes, then summands vanish).
> Compare with Mathlib's `Nat.add_eq_zero`.

```lean
theorem Nat.add_eq_zero (a b:Nat) (hab: a + b = 0) : a = 0 ∧ b = 0
```

## Lemma 2.2.10 / Exercise 2.2.2

`Chapter2.Nat.uniq_succ_eq` (lemma, [line 176](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_2.lean#L176)). An exercise, stated without proof.

> Lemma 2.2.10 (unique predecessor) / Exercise 2.2.2

```lean
lemma Nat.uniq_succ_eq (a:Nat) (ha: a.IsPos) : ∃! b, b++ = a
```

## Definition 2.2.11

`Chapter2.Nat.instLE` (instance, [line 181](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_2.lean#L181)). A definition.

> Definition 2.2.11 (Ordering of the natural numbers).
> This defines the `≤` notation on the natural numbers.

```lean
instance Nat.instLE : LE Nat
```

`Chapter2.Nat.instLT` (instance, [line 186](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_2.lean#L186)). A definition.

> Definition 2.2.11 (Ordering of the natural numbers).
> This defines the `<` notation on the natural numbers.

```lean
instance Nat.instLT : LT Nat
```

## Proposition 2.2.12 / Exercise 2.2.3

`Chapter2.Nat.ge_refl` (theorem, [line 229](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_2.lean#L229)). An exercise, stated without proof.

> Proposition 2.2.12 (Basic properties of order for natural numbers) / Exercise 2.2.3
>
> (a) (Order is reflexive). Compare with Mathlib's `Nat.le_refl`.

```lean
theorem Nat.ge_refl (a:Nat) : a ≥ a
```

## Proposition 2.2.13 / Exercise 2.2.4

`Chapter2.Nat.trichotomous` (theorem, [line 307](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_2.lean#L307)). An exercise, stated without proof.

> Proposition 2.2.13 (Trichotomy of order for natural numbers) / Exercise 2.2.4
> Compare with Mathlib's `trichotomous`.  Parts of this theorem have been placed
> in the preceding Lean theorems.

```lean
theorem Nat.trichotomous (a b:Nat) : a < b ∨ a = b ∨ a > b
```

## Proposition 2.2.14 / Exercise 2.2.5

`Chapter2.Nat.strong_induction` (theorem, [line 406](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_2.lean#L406)). An exercise, stated without proof.

> Proposition 2.2.14 (Strong principle of induction) / Exercise 2.2.5
> Compare with Mathlib's `Nat.strong_induction_on`.

```lean
theorem Nat.strong_induction {m₀:Nat} {P: Nat → Prop}
  (hind: ∀ m, m ≥ m₀ → (∀ m', m₀ ≤ m' ∧ m' < m → P m') → P m) :
    ∀ m, m ≥ m₀ → P m
```

## Exercise 2.2.6

`Chapter2.Nat.backwards_induction` (theorem, [line 413](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_2.lean#L413)). An exercise, stated without proof.

> Exercise 2.2.6 (backwards induction)
> Compare with Mathlib's `Nat.decreasingInduction`.

```lean
theorem Nat.backwards_induction {n:Nat} {P: Nat → Prop}
  (hind: ∀ m, P (m++) → P m) (hn: P n) :
    ∀ m, m ≤ n → P m
```

## Exercise 2.2.7

`Chapter2.Nat.induction_from` (theorem, [line 420](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_2.lean#L420)). An exercise, stated without proof.

> Exercise 2.2.7 (induction from a starting point)
> Compare with Mathlib's `Nat.le_induction`.

```lean
theorem Nat.induction_from {n:Nat} {P: Nat → Prop} (hind: ∀ m, P m → P (m++)) :
    P n → ∀ m, m ≥ n → P m
```

## Depends on

- [Section 2.1: The Peano Axioms](section-2-1.md)

## Sources

- [Analysis/Section_2_2.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_2_2.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_2_2/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_2_2.html)
