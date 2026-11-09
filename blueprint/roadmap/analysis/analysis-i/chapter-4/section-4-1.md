---
declaration: instance
origin: cited
lean: Section_4_1.PreInt.instSetoid, Section_4_1.Int.eq, Section_4_1.Int.eq_diff, Section_4_1.Int.instAdd, Section_4_1.Int.mul_congr_left, Section_4_1.Int.mul_congr_right, Section_4_1.Int.mul_congr, Section_4_1.Int.add_eq, Section_4_1.Int.mul_eq, Section_4_1.Int.instNeg, Section_4_1.Int.trichotomous, Section_4_1.Int.not_pos_zero, Section_4_1.Int.not_neg_zero, Section_4_1.Int.not_pos_neg, Section_4_1.Int.instAddGroup, Section_4_1.Int.instAddCommGroup, Section_4_1.Int.instCommMonoid, Section_4_1.Int.instCommRing, Section_4_1.Int.mul_eq_zero, Section_4_1.Int.mul_right_cancel₀, Section_4_1.Int.instLE, Section_4_1.Int.instLT, Section_4_1.Int.lt_iff_exists_positive_difference, Section_4_1.Int.add_lt_add_right, Section_4_1.Int.mul_lt_mul_of_pos_right, Section_4_1.Int.neg_gt_neg, Section_4_1.Int.neg_ge_neg, Section_4_1.Int.lt_trans, Section_4_1.Int.trichotomous', Section_4_1.Int.not_gt_and_lt, Section_4_1.Int.not_gt_and_eq, Section_4_1.Int.not_lt_and_eq, Section_4_1.Int.neg_one_mul, Section_4_1.Int.no_induction, Section_4_1.Int.sq_nonneg, Section_4_1.Int.sq_nonneg'
statement: formalized
---

# Section 4.1: The integers

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Definition of the "Section 4.1" integers, `Section_4_1.Int`, as formal differences `a —— b` of
>   natural numbers `a b:ℕ`, up to equivalence.  (This is a quotient of a scaffolding type
>   `Section_4_1.PreInt`, which consists of formal differences without any equivalence imposed.)
>
> - ring operations and order these integers, as well as an embedding of `ℕ`.
>
> - Equivalence with the Mathlib integers `_root_.Int` (or `ℤ`), which we will use going forward.
>
> ## Tips from past users
>
> Users of the companion who have completed the exercises in this section are welcome to send their tips for future users in this section as PRs.
>
> - (Add tip here)

*Quoted from [Analysis/Section_4_1.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 18 labelled items, carried by 36 declarations: 11 proved here, 16 stated without proof (16 of them exercises) and 9 definitions (6 with a value left as `sorry`). It also has 27 declarations and 3 examples with no label, counted here but not shown.

## Definition 4.1.1

`Section_4_1.PreInt.instSetoid` (instance, [line 40](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L40)). A definition whose value is left as `sorry`.

> Definition 4.1.1

```lean
instance PreInt.instSetoid : Setoid PreInt
```

`Section_4_1.Int.eq` (theorem, [line 66](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L66)). Proved here.

> Definition 4.1.1 (Integers, equality)

```lean
theorem Int.eq (a b c d:ℕ): a —— b = c —— d ↔ a + d = c + b
```

`Section_4_1.Int.eq_diff` (theorem, [line 80](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L80)). Proved here.

> Definition 4.1.1 (Integers, existence of a representation)

```lean
theorem Int.eq_diff (n:Int) : ∃ a b, n = a —— b
```

## Lemma 4.1.3

`Section_4_1.Int.instAdd` (instance, [line 83](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L83)). A definition.

> Lemma 4.1.3 (Addition well-defined)

```lean
instance Int.instAdd : Add Int
```

`Section_4_1.Int.mul_congr_left` (theorem, [line 93](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L93)). Proved here.

> Lemma 4.1.3 (Multiplication well-defined, left argument)

```lean
theorem Int.mul_congr_left (a b a' b' c d : ℕ) (h: a —— b = a' —— b') :
    (a*c+b*d) —— (a*d+b*c) = (a'*c+b'*d) —— (a'*d+b'*c)
```

`Section_4_1.Int.mul_congr_right` (theorem, [line 102](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L102)). Proved here.

> Lemma 4.1.3 (Multiplication well-defined, right argument)

```lean
theorem Int.mul_congr_right (a b c d c' d' : ℕ) (h: c —— d = c' —— d') :
    (a*c+b*d) —— (a*d+b*c) = (a*c'+b*d') —— (a*d'+b*c')
```

`Section_4_1.Int.mul_congr` (theorem, [line 111](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L111)). Proved here.

> Lemma 4.1.3 (Multiplication well-defined, both arguments)

```lean
theorem Int.mul_congr {a b c d a' b' c' d' : ℕ} (h1: a —— b = a' —— b') (h2: c —— d = c' —— d') :
  (a*c+b*d) —— (a*d+b*c) = (a'*c'+b'*d') —— (a'*d'+b'*c')
```

## Definition 4.1.2

`Section_4_1.Int.add_eq` (theorem, [line 90](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L90)). Proved here.

> Definition 4.1.2 (Definition of addition)

```lean
theorem Int.add_eq (a b c d:ℕ) : a —— b + c —— d = (a+c)——(b+d)
```

`Section_4_1.Int.mul_eq` (theorem, [line 122](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L122)). Proved here.

> Definition 4.1.2 (Multiplication of integers)

```lean
theorem Int.mul_eq (a b c d:ℕ) : a —— b * c —— d = (a*c+b*d) —— (a*d+b*c)
```

## Definition 4.1.4 / Exercise 4.1.2

`Section_4_1.Int.instNeg` (instance, [line 153](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L153)). A definition whose value is left as `sorry`.

> Definition 4.1.4 (Negation of integers) / Exercise 4.1.2

```lean
instance Int.instNeg : Neg Int
```

## Lemma 4.1.5

`Section_4_1.Int.trichotomous` (theorem, [line 164](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L164)). Proved here.

> Lemma 4.1.5 (trichotomy of integers).

```lean
theorem Int.trichotomous (x:Int) : x = 0 ∨ x.IsPos ∨ x.IsNeg
```

`Section_4_1.Int.not_pos_zero` (theorem, [line 177](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L177)). Proved here.

> Lemma 4.1.5 (zero is not positive).

```lean
theorem Int.not_pos_zero (x:Int) : x = 0 ∧ x.IsPos → False
```

`Section_4_1.Int.not_neg_zero` (theorem, [line 181](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L181)). Proved here.

> Lemma 4.1.5 (zero is not negative).

```lean
theorem Int.not_neg_zero (x:Int) : x = 0 ∧ x.IsNeg → False
```

`Section_4_1.Int.not_pos_neg` (theorem, [line 186](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L186)). Proved here.

> Lemma 4.1.5 (positive and negative are disjoint).

```lean
theorem Int.not_pos_neg (x:Int) : x.IsPos ∧ x.IsNeg → False
```

## Proposition 4.1.6 / Exercise 4.1.4

`Section_4_1.Int.instAddGroup` (instance, [line 191](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L191)). A definition whose value is left as `sorry`.

> Proposition 4.1.6 (laws of algebra, additive group) / Exercise 4.1.4

```lean
instance Int.instAddGroup : AddGroup Int
```

`Section_4_1.Int.instAddCommGroup` (instance, [line 195](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L195)). A definition whose value is left as `sorry`.

> Proposition 4.1.6 (laws of algebra, additive commutative group) / Exercise 4.1.4

```lean
instance Int.instAddCommGroup : AddCommGroup Int
```

`Section_4_1.Int.instCommMonoid` (instance, [line 199](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L199)). A definition whose value is left as `sorry`.

> Proposition 4.1.6 (laws of algebra, commutative monoid) / Exercise 4.1.4

```lean
instance Int.instCommMonoid : CommMonoid Int
```

`Section_4_1.Int.instCommRing` (instance, [line 212](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L212)). A definition whose value is left as `sorry`.

> Proposition 4.1.6 (laws of algebra, commutative ring) / Exercise 4.1.4

```lean
instance Int.instCommRing : CommRing Int
```

## Proposition 4.1.8 / Exercise 4.1.5

`Section_4_1.Int.mul_eq_zero` (theorem, [line 224](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L224)). An exercise, stated without proof.

> Proposition 4.1.8 (No zero divisors) / Exercise 4.1.5

```lean
theorem Int.mul_eq_zero {a b:Int} (h: a * b = 0) : a = 0 ∨ b = 0
```

## Corollary 4.1.9 / Exercise 4.1.6

`Section_4_1.Int.mul_right_cancel₀` (theorem, [line 227](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L227)). An exercise, stated without proof.

> Corollary 4.1.9 (Cancellation law) / Exercise 4.1.6

```lean
theorem Int.mul_right_cancel₀ (a b c:Int) (h: a*c = b*c) (hc: c ≠ 0) : a = b
```

## Definition 4.1.10

`Section_4_1.Int.instLE` (instance, [line 230](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L230)). A definition.

> Definition 4.1.10 (Ordering of the integers, non-strict)

```lean
instance Int.instLE : LE Int
```

`Section_4_1.Int.instLT` (instance, [line 234](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L234)). A definition.

> Definition 4.1.10 (Ordering of the integers, strict)

```lean
instance Int.instLT : LT Int
```

## Lemma 4.1.11(a) / Exercise 4.1.7

`Section_4_1.Int.lt_iff_exists_positive_difference` (theorem, [line 242](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L242)). An exercise, stated without proof.

> Lemma 4.1.11(a) (Properties of order) / Exercise 4.1.7

```lean
theorem Int.lt_iff_exists_positive_difference (a b:Int) : a < b ↔ ∃ n:ℕ, n ≠ 0 ∧ b = a + n
```

## Lemma 4.1.11(b) / Exercise 4.1.7

`Section_4_1.Int.add_lt_add_right` (theorem, [line 245](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L245)). An exercise, stated without proof.

> Lemma 4.1.11(b) (Addition preserves order) / Exercise 4.1.7

```lean
theorem Int.add_lt_add_right {a b:Int} (c:Int) (h: a < b) : a+c < b+c
```

## Lemma 4.1.11(c) / Exercise 4.1.7

`Section_4_1.Int.mul_lt_mul_of_pos_right` (theorem, [line 248](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L248)). An exercise, stated without proof.

> Lemma 4.1.11(c) (Positive multiplication preserves order) / Exercise 4.1.7

```lean
theorem Int.mul_lt_mul_of_pos_right {a b c:Int} (hab : a < b) (hc: 0 < c) : a*c < b*c
```

## Lemma 4.1.11(d) / Exercise 4.1.7

`Section_4_1.Int.neg_gt_neg` (theorem, [line 251](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L251)). An exercise, stated without proof.

> Lemma 4.1.11(d) (Negation reverses order, strict) / Exercise 4.1.7

```lean
theorem Int.neg_gt_neg {a b:Int} (h: b < a) : -a < -b
```

`Section_4_1.Int.neg_ge_neg` (theorem, [line 254](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L254)). An exercise, stated without proof.

> Lemma 4.1.11(d) (Negation reverses order, non-strict) / Exercise 4.1.7

```lean
theorem Int.neg_ge_neg {a b:Int} (h: b ≤ a) : -a ≤ -b
```

## Lemma 4.1.11(e) / Exercise 4.1.7

`Section_4_1.Int.lt_trans` (theorem, [line 257](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L257)). An exercise, stated without proof.

> Lemma 4.1.11(e) (Order is transitive) / Exercise 4.1.7

```lean
theorem Int.lt_trans {a b c:Int} (hab: a < b) (hbc: b < c) : a < c
```

## Lemma 4.1.11(f) / Exercise 4.1.7

`Section_4_1.Int.trichotomous'` (theorem, [line 260](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L260)). An exercise, stated without proof.

> Lemma 4.1.11(f) (Order trichotomy, trichotomy) / Exercise 4.1.7

```lean
theorem Int.trichotomous' (a b:Int) : a > b ∨ a < b ∨ a = b
```

`Section_4_1.Int.not_gt_and_lt` (theorem, [line 263](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L263)). An exercise, stated without proof.

> Lemma 4.1.11(f) (Order trichotomy, greater vs less) / Exercise 4.1.7

```lean
theorem Int.not_gt_and_lt (a b:Int) : ¬ (a > b ∧ a < b)
```

`Section_4_1.Int.not_gt_and_eq` (theorem, [line 266](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L266)). An exercise, stated without proof.

> Lemma 4.1.11(f) (Order trichotomy, greater vs equal) / Exercise 4.1.7

```lean
theorem Int.not_gt_and_eq (a b:Int) : ¬ (a > b ∧ a = b)
```

`Section_4_1.Int.not_lt_and_eq` (theorem, [line 269](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L269)). An exercise, stated without proof.

> Lemma 4.1.11(f) (Order trichotomy, less vs equal) / Exercise 4.1.7

```lean
theorem Int.not_lt_and_eq (a b:Int) : ¬ (a < b ∧ a = b)
```

## Exercise 4.1.3

`Section_4_1.Int.neg_one_mul` (theorem, [line 300](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L300)). An exercise, stated without proof.

> Exercise 4.1.3

```lean
theorem Int.neg_one_mul (a:Int) : -1 * a = -a
```

## Exercise 4.1.8

`Section_4_1.Int.no_induction` (theorem, [line 303](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L303)). An exercise, stated without proof.

> Exercise 4.1.8

```lean
theorem Int.no_induction : ∃ P: Int → Prop, (P 0 ∧ ∀ n, P n → P (n+1)) ∧ ¬ ∀ n, P n
```

## Exercise 4.1.9

`Section_4_1.Int.sq_nonneg` (theorem, [line 309](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L309)). An exercise, stated without proof.

> Exercise 4.1.9. The square of any integer is nonnegative.

```lean
theorem Int.sq_nonneg (n:Int) : 0 ≤ n*n
```

`Section_4_1.Int.sq_nonneg'` (theorem, [line 312](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean#L312)). An exercise, stated without proof.

> Exercise 4.1.9

```lean
theorem Int.sq_nonneg' (n:Int) : ∃ (m:Nat), n*n = m
```

## Depends on

Its Lean file imports no other section's file.

## Sources

- [Analysis/Section_4_1.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_1.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_4_1/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_4_1.html)
