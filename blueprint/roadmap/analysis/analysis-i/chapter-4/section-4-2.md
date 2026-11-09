---
declaration: instance
origin: cited
lean: Section_4_2.PreRat.instSetoid, Section_4_2.Rat.eq, Section_4_2.Rat.eq_diff, Section_4_2.Rat.add_inst, Section_4_2.Rat.mul_inst, Section_4_2.Rat.neg_inst, Section_4_2.Rat.add_eq, Section_4_2.Rat.mul_eq, Section_4_2.Rat.neg_eq, Section_4_2.Rat.addGroup_inst, Section_4_2.Rat.instAddCommGroup, Section_4_2.Rat.instCommMonoid, Section_4_2.Rat.instCommRing, Section_4_2.Rat.instField, Section_4_2.Rat.isPos, Section_4_2.Rat.isNeg, Section_4_2.Rat.trichotomous, Section_4_2.Rat.not_zero_and_pos, Section_4_2.Rat.not_zero_and_neg, Section_4_2.Rat.not_pos_and_neg, Section_4_2.Rat.instLT, Section_4_2.Rat.instLE, Section_4_2.Rat.trichotomous', Section_4_2.Rat.not_gt_and_lt, Section_4_2.Rat.not_gt_and_eq, Section_4_2.Rat.not_lt_and_eq, Section_4_2.Rat.antisymm, Section_4_2.Rat.lt_trans, Section_4_2.Rat.add_lt_add_right, Section_4_2.Rat.mul_lt_mul_right, Section_4_2.Rat.mul_lt_mul_right_of_neg
statement: formalized
---

# Section 4.2: The rationals

> This file is a translation of Section 4.2 of Analysis I to Lean 4.
> All numbering refers to the original text.
>
> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Definition of the "Section 4.2" rationals, `Section_4_2.Rat`, as formal quotients `a // b` of
>   integers `a b:ℤ`, up to equivalence.  (This is a quotient of a scaffolding type
>   `Section_4_2.PreRat`, which consists of formal quotients without any equivalence imposed.)
>
> - Field operations and order on these rationals, as well as an embedding of `ℕ` and `ℤ`.
>
> - Equivalence with the Mathlib rationals `_root_.Rat` (or `ℚ`), which we will use going forward.
>
> Note: here (and in the sequel) we use Mathlib's natural numbers `ℕ` and integers `ℤ` rather than
> the Chapter 2 natural numbers and Section 4.1 integers.
>
> ## Tips from past users
>
> Users of the companion who have completed the exercises in this section are welcome to send their tips for future users in this section as PRs.
>
> - (Add tip here)

*Quoted from [Analysis/Section_4_2.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 14 labelled items, carried by 31 declarations: 5 proved here, 13 stated without proof (13 of them exercises) and 13 definitions (8 with a value left as `sorry`). It also has 37 declarations and 1 example with no label, counted here but not shown.

## Exercise 4.2.1

`Section_4_2.PreRat.instSetoid` (instance, [line 47](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L47)). A definition whose value is left as `sorry`.

> Exercise 4.2.1

```lean
instance PreRat.instSetoid : Setoid PreRat
```

## Definition 4.2.1

`Section_4_2.Rat.eq` (theorem, [line 68](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L68)). Proved here.

> Definition 4.2.1 (Rationals, equality)

```lean
theorem Rat.eq (a c:ℤ) {b d:ℤ} (hb: b ≠ 0) (hd: d ≠ 0): a // b = c // d ↔ a * d = c * b
```

`Section_4_2.Rat.eq_diff` (theorem, [line 72](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L72)). Proved here.

> Definition 4.2.1 (Rationals, existence of a representation)

```lean
theorem Rat.eq_diff (n:Rat) : ∃ a b, b ≠ 0 ∧ n = a // b
```

## Lemma 4.2.3

`Section_4_2.Rat.add_inst` (instance, [line 87](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L87)). A definition.

> Lemma 4.2.3 (Addition well-defined)

```lean
instance Rat.add_inst : Add Rat
```

`Section_4_2.Rat.mul_inst` (instance, [line 100](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L100)). A definition whose value is left as `sorry`.

> Lemma 4.2.3 (Multiplication well-defined)

```lean
instance Rat.mul_inst : Mul Rat
```

`Section_4_2.Rat.neg_inst` (instance, [line 109](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L109)). A definition whose value is left as `sorry`.

> Lemma 4.2.3 (Negation well-defined)

```lean
instance Rat.neg_inst : Neg Rat
```

## Definition 4.2.2

`Section_4_2.Rat.add_eq` (theorem, [line 95](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L95)). Proved here.

> Definition 4.2.2 (Addition of rationals)

```lean
theorem Rat.add_eq (a c:ℤ) {b d:ℤ} (hb: b ≠ 0) (hd: d ≠ 0) :
    (a // b) + (c // d) = (a*d + b*c) // (b*d)
```

`Section_4_2.Rat.mul_eq` (theorem, [line 104](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L104)). Proved here.

> Definition 4.2.2 (Multiplication of rationals)

```lean
theorem Rat.mul_eq (a c:ℤ) {b d:ℤ} (hb: b ≠ 0) (hd: d ≠ 0) :
    (a // b) * (c // d) = (a*c) // (b*d)
```

`Section_4_2.Rat.neg_eq` (theorem, [line 113](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L113)). Proved here.

> Definition 4.2.2 (Negation of rationals)

```lean
theorem Rat.neg_eq (a:ℤ) {b:ℤ} (hb: b ≠ 0) : - (a // b) = (-a) // b
```

## Proposition 4.2.4 / Exercise 4.2.3

`Section_4_2.Rat.addGroup_inst` (instance, [line 162](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L162)). A definition whose value is left as `sorry`.

> Proposition 4.2.4 (laws of algebra, additive group) / Exercise 4.2.3

```lean
instance Rat.addGroup_inst : AddGroup Rat
```

`Section_4_2.Rat.instAddCommGroup` (instance, [line 179](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L179)). A definition whose value is left as `sorry`.

> Proposition 4.2.4 (laws of algebra, additive commutative group) / Exercise 4.2.3

```lean
instance Rat.instAddCommGroup : AddCommGroup Rat
```

`Section_4_2.Rat.instCommMonoid` (instance, [line 183](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L183)). A definition whose value is left as `sorry`.

> Proposition 4.2.4 (laws of algebra, commutative monoid) / Exercise 4.2.3

```lean
instance Rat.instCommMonoid : CommMonoid Rat
```

`Section_4_2.Rat.instCommRing` (instance, [line 190](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L190)). A definition whose value is left as `sorry`.

> Proposition 4.2.4 (laws of algebra, commutative ring) / Exercise 4.2.3

```lean
instance Rat.instCommRing : CommRing Rat
```

`Section_4_2.Rat.instField` (instance, [line 223](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L223)). A definition whose value is left as `sorry`.

> Proposition 4.2.4 (laws of algebra, field) / Exercise 4.2.3

```lean
instance Rat.instField : Field Rat
```

## Definition 4.2.6

`Section_4_2.Rat.isPos` (def, [line 251](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L251)). A definition.

> Definition 4.2.6 (positivity)

```lean
def Rat.isPos (q:Rat) : Prop
```

`Section_4_2.Rat.isNeg` (def, [line 254](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L254)). A definition.

> Definition 4.2.6 (negativity)

```lean
def Rat.isNeg (q:Rat) : Prop
```

## Lemma 4.2.7 / Exercise 4.2.4

`Section_4_2.Rat.trichotomous` (theorem, [line 257](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L257)). An exercise, stated without proof.

> Lemma 4.2.7 (trichotomy of rationals, trichotomy) / Exercise 4.2.4

```lean
theorem Rat.trichotomous (x:Rat) : x = 0 ∨ x.isPos ∨ x.isNeg
```

`Section_4_2.Rat.not_zero_and_pos` (theorem, [line 260](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L260)). An exercise, stated without proof.

> Lemma 4.2.7 (trichotomy of rationals, zero vs positive) / Exercise 4.2.4

```lean
theorem Rat.not_zero_and_pos (x:Rat) : ¬(x = 0 ∧ x.isPos)
```

`Section_4_2.Rat.not_zero_and_neg` (theorem, [line 263](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L263)). An exercise, stated without proof.

> Lemma 4.2.7 (trichotomy of rationals, zero vs negative) / Exercise 4.2.4

```lean
theorem Rat.not_zero_and_neg (x:Rat) : ¬(x = 0 ∧ x.isNeg)
```

`Section_4_2.Rat.not_pos_and_neg` (theorem, [line 266](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L266)). An exercise, stated without proof.

> Lemma 4.2.7 (trichotomy of rationals, positive vs negative) / Exercise 4.2.4

```lean
theorem Rat.not_pos_and_neg (x:Rat) : ¬(x.isPos ∧ x.isNeg)
```

## Definition 4.2.8

`Section_4_2.Rat.instLT` (instance, [line 269](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L269)). A definition.

> Definition 4.2.8 (Ordering of the rationals, strict)

```lean
instance Rat.instLT : LT Rat
```

`Section_4_2.Rat.instLE` (instance, [line 273](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L273)). A definition.

> Definition 4.2.8 (Ordering of the rationals, non-strict)

```lean
instance Rat.instLE : LE Rat
```

## Proposition 4.2.9(a) / Exercise 4.2.5

`Section_4_2.Rat.trichotomous'` (theorem, [line 283](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L283)). An exercise, stated without proof.

> Proposition 4.2.9(a) (order trichotomy, trichotomy) / Exercise 4.2.5

```lean
theorem Rat.trichotomous' (x y:Rat) : x > y ∨ x < y ∨ x = y
```

`Section_4_2.Rat.not_gt_and_lt` (theorem, [line 286](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L286)). An exercise, stated without proof.

> Proposition 4.2.9(a) (order trichotomy, greater vs less) / Exercise 4.2.5

```lean
theorem Rat.not_gt_and_lt (x y:Rat) : ¬ (x > y ∧ x < y)
```

`Section_4_2.Rat.not_gt_and_eq` (theorem, [line 289](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L289)). An exercise, stated without proof.

> Proposition 4.2.9(a) (order trichotomy, greater vs equal) / Exercise 4.2.5

```lean
theorem Rat.not_gt_and_eq (x y:Rat) : ¬ (x > y ∧ x = y)
```

`Section_4_2.Rat.not_lt_and_eq` (theorem, [line 292](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L292)). An exercise, stated without proof.

> Proposition 4.2.9(a) (order trichotomy, less vs equal) / Exercise 4.2.5

```lean
theorem Rat.not_lt_and_eq (x y:Rat) : ¬ (x < y ∧ x = y)
```

## Proposition 4.2.9(b) / Exercise 4.2.5

`Section_4_2.Rat.antisymm` (theorem, [line 295](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L295)). An exercise, stated without proof.

> Proposition 4.2.9(b) (order is anti-symmetric) / Exercise 4.2.5

```lean
theorem Rat.antisymm (x y:Rat) : x < y ↔ y > x
```

## Proposition 4.2.9(c) / Exercise 4.2.5

`Section_4_2.Rat.lt_trans` (theorem, [line 298](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L298)). An exercise, stated without proof.

> Proposition 4.2.9(c) (order is transitive) / Exercise 4.2.5

```lean
theorem Rat.lt_trans {x y z:Rat} (hxy: x < y) (hyz: y < z) : x < z
```

## Proposition 4.2.9(d) / Exercise 4.2.5

`Section_4_2.Rat.add_lt_add_right` (theorem, [line 301](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L301)). An exercise, stated without proof.

> Proposition 4.2.9(d) (addition preserves order) / Exercise 4.2.5

```lean
theorem Rat.add_lt_add_right {x y:Rat} (z:Rat) (hxy: x < y) : x + z < y + z
```

## Proposition 4.2.9(e) / Exercise 4.2.5

`Section_4_2.Rat.mul_lt_mul_right` (theorem, [line 304](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L304)). An exercise, stated without proof.

> Proposition 4.2.9(e) (positive multiplication preserves order) / Exercise 4.2.5

```lean
theorem Rat.mul_lt_mul_right {x y z:Rat} (hxy: x < y) (hz: z.isPos) : x * z < y * z
```

## Exercise 4.2.6

`Section_4_2.Rat.mul_lt_mul_right_of_neg` (theorem, [line 353](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean#L353)). An exercise, stated without proof.

> Exercise 4.2.6

```lean
theorem Rat.mul_lt_mul_right_of_neg (x y z:Rat) (hxy: x < y) (hz: z.isNeg) : x * z > y * z
```

## Depends on

Its Lean file imports no other section's file.

## Sources

- [Analysis/Section_4_2.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_2.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_4_2/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_4_2.html)
