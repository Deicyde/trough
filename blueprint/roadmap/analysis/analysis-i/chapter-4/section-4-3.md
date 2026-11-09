---
declaration: abbrev
origin: cited
lean: Section_4_3.abs, Section_4_3.abs_of_pos, Section_4_3.abs_of_neg, Section_4_3.abs_of_zero, Section_4_3.dist_eq, Section_4_3.abs_nonneg, Section_4_3.abs_eq_zero_iff, Section_4_3.abs_add, Section_4_3.abs_le_iff, Section_4_3.le_abs, Section_4_3.abs_mul, Section_4_3.abs_neg, Section_4_3.dist_nonneg, Section_4_3.dist_eq_zero_iff, Section_4_3.dist_symm, Section_4_3.dist_le, Section_4_3.close_iff, Section_4_3.eq_if_close, Section_4_3.close_symm, Section_4_3.close_trans, Section_4_3.add_close, Section_4_3.sub_close, Section_4_3.close_mono, Section_4_3.close_between, Section_4_3.close_mul_right, Section_4_3.close_mul_mul, Section_4_3.pow_zero, Section_4_3.pow_succ, Section_4_3.pow_add, Section_4_3.pow_mul, Section_4_3.mul_pow, Section_4_3.pow_eq_zero, Section_4_3.pow_nonneg, Section_4_3.pow_pos, Section_4_3.pow_ge_pow, Section_4_3.pow_gt_pow, Section_4_3.pow_abs, Section_4_3.zpow_neg, Section_4_3.zpow_add, Section_4_3.zpow_mul, Section_4_3.mul_zpow, Section_4_3.zpow_pos, Section_4_3.zpow_ge_zpow, Section_4_3.zpow_inj, Section_4_3.zpow_abs, Section_4_3.two_pow_geq
statement: formalized
---

# Section 4.3: Absolute value and exponentiation

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter.  In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Basic properties of absolute value and exponentiation on the rational numbers (here we use the
>   Mathlib rational numbers `ℚ` rather than the Section 4.2 rational numbers).
>
> Note: to avoid notational conflict, we are using the standard Mathlib definitions of absolute
> value and exponentiation.  As such, it is possible to solve several of the exercises here rather
> easily using the Mathlib API for these operations.  However, the spirit of the exercises is to
> solve these instead using the API provided in this section, as well as more basic Mathlib API for
> the rational numbers that does not reference either absolute value or exponentiation.
>
> ## Tips from past users
>
> Users of the companion who have completed the exercises in this section are welcome to send their tips for future users in this section as PRs.
>
> - (Add tip here)

*Quoted from [Analysis/Section_4_3.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 32 labelled items, carried by 49 declarations: 9 proved here, 39 stated without proof (36 of them exercises) and 1 definition. It also has 7 declarations and 3 examples with no label, counted here but not shown.

## Definition 4.3.1

`Section_4_3.abs` (abbrev, [line 41](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L41)). A definition.

> Definition 4.3.1 (Absolute value)

```lean
abbrev abs (x:ℚ) : ℚ
```

`Section_4_3.abs_of_pos` (theorem, [line 44](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L44)). Proved here.

> Definition 4.3.1 (Absolute value) (positive case)

```lean
theorem abs_of_pos {x: ℚ} (hx: 0 < x) : abs x = x
```

`Section_4_3.abs_of_neg` (theorem, [line 47](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L47)). Proved here.

> Definition 4.3.1 (Absolute value) (negative case)

```lean
theorem abs_of_neg {x: ℚ} (hx: x < 0) : abs x = -x
```

`Section_4_3.abs_of_zero` (theorem, [line 50](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L50)). Proved here.

> Definition 4.3.1 (Absolute value) (zero case)

```lean
theorem abs_of_zero : abs 0 = 0
```

## Definition 4.3.2

`Section_4_3.dist_eq` (theorem, [line 65](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L65)). Proved here.

> Definition 4.3.2 (Distance).
> We avoid the Mathlib notion of distance here because it is real-valued.

```lean
theorem dist_eq (x y: ℚ) : dist x y = |x-y|
```

## Proposition 4.3.3(a) / Exercise 4.3.1

`Section_4_3.abs_nonneg` (theorem, [line 68](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L68)). An exercise, stated without proof.

> Proposition 4.3.3(a) (non-negativity) / Exercise 4.3.1

```lean
theorem abs_nonneg (x: ℚ) : |x| ≥ 0
```

`Section_4_3.abs_eq_zero_iff` (theorem, [line 71](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L71)). An exercise, stated without proof.

> Proposition 4.3.3(a) (vanishing iff zero) / Exercise 4.3.1

```lean
theorem abs_eq_zero_iff (x: ℚ) : |x| = 0 ↔ x = 0
```

## Proposition 4.3.3(b) / Exercise 4.3.1

`Section_4_3.abs_add` (theorem, [line 74](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L74)). An exercise, stated without proof.

> Proposition 4.3.3(b) / Exercise 4.3.1

```lean
theorem abs_add (x y:ℚ) : |x + y| ≤ |x| + |y|
```

## Proposition 4.3.3(c) / Exercise 4.3.1

`Section_4_3.abs_le_iff` (theorem, [line 77](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L77)). An exercise, stated without proof.

> Proposition 4.3.3(c) (two-sided bound) / Exercise 4.3.1

```lean
theorem abs_le_iff (x y:ℚ) : -y ≤ x ∧ x ≤ y ↔ |x| ≤ y
```

`Section_4_3.le_abs` (theorem, [line 80](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L80)). An exercise, stated without proof.

> Proposition 4.3.3(c) (bounded by own absolute value) / Exercise 4.3.1

```lean
theorem le_abs (x:ℚ) : -|x| ≤ x ∧ x ≤ |x|
```

## Proposition 4.3.3(d) / Exercise 4.3.1

`Section_4_3.abs_mul` (theorem, [line 83](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L83)). An exercise, stated without proof.

> Proposition 4.3.3(d) (multiplicativity) / Exercise 4.3.1

```lean
theorem abs_mul (x y:ℚ) : |x * y| = |x| * |y|
```

`Section_4_3.abs_neg` (theorem, [line 86](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L86)). An exercise, stated without proof.

> Proposition 4.3.3(d) (negation) / Exercise 4.3.1

```lean
theorem abs_neg (x:ℚ) : |-x| = |x|
```

## Proposition 4.3.3(e) / Exercise 4.3.1

`Section_4_3.dist_nonneg` (theorem, [line 89](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L89)). An exercise, stated without proof.

> Proposition 4.3.3(e) (non-negativity) / Exercise 4.3.1

```lean
theorem dist_nonneg (x y:ℚ) : dist x y ≥ 0
```

`Section_4_3.dist_eq_zero_iff` (theorem, [line 92](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L92)). An exercise, stated without proof.

> Proposition 4.3.3(e) (vanishing iff equal) / Exercise 4.3.1

```lean
theorem dist_eq_zero_iff (x y:ℚ) : dist x y = 0 ↔ x = y
```

## Proposition 4.3.3(f) / Exercise 4.3.1

`Section_4_3.dist_symm` (theorem, [line 96](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L96)). An exercise, stated without proof.

> Proposition 4.3.3(f) / Exercise 4.3.1

```lean
theorem dist_symm (x y:ℚ) : dist x y = dist y x
```

## Proposition 4.3.3(g) / Exercise 4.3.1

`Section_4_3.dist_le` (theorem, [line 99](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L99)). An exercise, stated without proof.

> Proposition 4.3.3(g) / Exercise 4.3.1

```lean
theorem dist_le (x y z:ℚ) : dist x z ≤ dist x y + dist y z
```

## Definition 4.3.4

`Section_4_3.close_iff` (theorem, [line 106](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L106)). Proved here.

> Definition 4.3.4 (eps-closeness).  In the text the notion is undefined for ε zero or negative,
> but it is more convenient in Lean to assign a "junk" definition in this case.  But this also
> allows some relaxations of hypotheses in the lemmas that follow.

```lean
theorem close_iff (ε x y:ℚ): ε.Close x y ↔ |x - y| ≤ ε
```

## Examples 4.3.6 (a)

An `example` ([line 109](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L109)). Stated without proof.

> Examples 4.3.6 (a)

```lean
example : (0.1:ℚ).Close (0.99:ℚ) (1.01:ℚ)
```

## Examples 4.3.6 (b)

An `example` ([line 112](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L112)). Stated without proof.

> Examples 4.3.6 (b)

```lean
example : ¬ (0.01:ℚ).Close (0.99:ℚ) (1.01:ℚ)
```

## Examples 4.3.6 (c)

An `example` ([line 115](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L115)). Stated without proof.

> Examples 4.3.6 (c)

```lean
example (ε : ℚ) (hε : ε > 0) : ε.Close 2 2
```

## Proposition 4.3.7(a) / Exercise 4.3.2

`Section_4_3.eq_if_close` (theorem, [line 120](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L120)). An exercise, stated without proof.

> Proposition 4.3.7(a) / Exercise 4.3.2

```lean
theorem eq_if_close (x y:ℚ) : x = y ↔ ∀ ε:ℚ, ε > 0 → ε.Close x y
```

## Proposition 4.3.7(b) / Exercise 4.3.2

`Section_4_3.close_symm` (theorem, [line 123](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L123)). An exercise, stated without proof.

> Proposition 4.3.7(b) / Exercise 4.3.2

```lean
theorem close_symm (ε x y:ℚ) : ε.Close x y ↔ ε.Close y x
```

## Proposition 4.3.7(c) / Exercise 4.3.2

`Section_4_3.close_trans` (theorem, [line 126](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L126)). An exercise, stated without proof.

> Proposition 4.3.7(c) / Exercise 4.3.2

```lean
theorem close_trans {ε δ x y z:ℚ} (hxy: ε.Close x y) (hyz: δ.Close y z) :
    (ε + δ).Close x z
```

## Proposition 4.3.7(d) / Exercise 4.3.2

`Section_4_3.add_close` (theorem, [line 130](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L130)). An exercise, stated without proof.

> Proposition 4.3.7(d) (addition) / Exercise 4.3.2

```lean
theorem add_close {ε δ x y z w:ℚ} (hxy: ε.Close x y) (hzw: δ.Close z w) :
    (ε + δ).Close (x+z) (y+w)
```

`Section_4_3.sub_close` (theorem, [line 134](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L134)). An exercise, stated without proof.

> Proposition 4.3.7(d) (subtraction) / Exercise 4.3.2

```lean
theorem sub_close {ε δ x y z w:ℚ} (hxy: ε.Close x y) (hzw: δ.Close z w) :
    (ε + δ).Close (x-z) (y-w)
```

## Proposition 4.3.7(e) / Exercise 4.3.2

`Section_4_3.close_mono` (theorem, [line 138](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L138)). An exercise, stated without proof.

> Proposition 4.3.7(e) / Exercise 4.3.2, slightly strengthened

```lean
theorem close_mono {ε ε' x y:ℚ} (hxy: ε.Close x y) (hε: ε' ≥  ε) :
    ε'.Close x y
```

## Proposition 4.3.7(f) / Exercise 4.3.2

`Section_4_3.close_between` (theorem, [line 142](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L142)). An exercise, stated without proof.

> Proposition 4.3.7(f) / Exercise 4.3.2

```lean
theorem close_between {ε x y z w:ℚ} (hxy: ε.Close x y) (hxz: ε.Close x z)
  (hbetween: (y ≤ w ∧ w ≤ z) ∨ (z ≤ w ∧ w ≤ y)) : ε.Close x w
```

## Proposition 4.3.7(g) / Exercise 4.3.2

`Section_4_3.close_mul_right` (theorem, [line 146](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L146)). An exercise, stated without proof.

> Proposition 4.3.7(g) / Exercise 4.3.2

```lean
theorem close_mul_right {ε x y z:ℚ} (hxy: ε.Close x y) :
    (ε*|z|).Close (x * z) (y * z)
```

## Proposition 4.3.7(h) / Exercise 4.3.2

`Section_4_3.close_mul_mul` (theorem, [line 150](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L150)). Proved here.

> Proposition 4.3.7(h) / Exercise 4.3.2

```lean
theorem close_mul_mul {ε δ x y z w:ℚ} (hxy: ε.Close x y) (hzw: δ.Close z w) :
    (ε*|z|+δ*|x|+ε*δ).Close (x * z) (y * w)
```

## Definition 4.3.9

`Section_4_3.pow_zero` (lemma, [line 178](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L178)). Proved here.

> Definition 4.3.9 (exponentiation) (base case).  Here we use the Mathlib definition.

```lean
lemma pow_zero (x:ℚ) : x^0 = 1
```

`Section_4_3.pow_succ` (lemma, [line 183](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L183)). Proved here.

> Definition 4.3.9 (exponentiation) (inductive step).  Here we use the Mathlib definition.

```lean
lemma pow_succ (x:ℚ) (n:ℕ) : x^(n+1) = x^n * x
```

## Proposition 4.3.10(a) / Exercise 4.3.3

`Section_4_3.pow_add` (theorem, [line 186](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L186)). An exercise, stated without proof.

> Proposition 4.3.10(a) (Properties of exponentiation, I) (exponent sum) / Exercise 4.3.3

```lean
theorem pow_add (x:ℚ) (m n:ℕ) : x^n * x^m = x^(n+m)
```

`Section_4_3.pow_mul` (theorem, [line 189](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L189)). An exercise, stated without proof.

> Proposition 4.3.10(a) (Properties of exponentiation, I) (exponent product) / Exercise 4.3.3

```lean
theorem pow_mul (x:ℚ) (m n:ℕ) : (x^n)^m = x^(n*m)
```

`Section_4_3.mul_pow` (theorem, [line 192](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L192)). An exercise, stated without proof.

> Proposition 4.3.10(a) (Properties of exponentiation, I) (product base) / Exercise 4.3.3

```lean
theorem mul_pow (x y:ℚ) (n:ℕ) : (x*y)^n = x^n * y^n
```

## Proposition 4.3.10(b) / Exercise 4.3.3

`Section_4_3.pow_eq_zero` (theorem, [line 195](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L195)). An exercise, stated without proof.

> Proposition 4.3.10(b) (Properties of exponentiation, I) / Exercise 4.3.3

```lean
theorem pow_eq_zero (x:ℚ) (n:ℕ) (hn : 0 < n) : x^n = 0 ↔ x = 0
```

## Proposition 4.3.10(c) / Exercise 4.3.3

`Section_4_3.pow_nonneg` (theorem, [line 198](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L198)). An exercise, stated without proof.

> Proposition 4.3.10(c) (Properties of exponentiation, I) (non-negativity) / Exercise 4.3.3

```lean
theorem pow_nonneg {x:ℚ} (n:ℕ) (hx: x ≥ 0) : x^n ≥ 0
```

`Section_4_3.pow_pos` (theorem, [line 201](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L201)). An exercise, stated without proof.

> Proposition 4.3.10(c) (Properties of exponentiation, I) (positivity) / Exercise 4.3.3

```lean
theorem pow_pos {x:ℚ} (n:ℕ) (hx: x > 0) : x^n > 0
```

`Section_4_3.pow_ge_pow` (theorem, [line 204](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L204)). An exercise, stated without proof.

> Proposition 4.3.10(c) (Properties of exponentiation, I) (monotonicity) / Exercise 4.3.3

```lean
theorem pow_ge_pow (x y:ℚ) (n:ℕ) (hxy: x ≥ y) (hy: y ≥ 0) : x^n ≥ y^n
```

`Section_4_3.pow_gt_pow` (theorem, [line 207](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L207)). An exercise, stated without proof.

> Proposition 4.3.10(c) (Properties of exponentiation, I) (strict inequality) / Exercise 4.3.3

```lean
theorem pow_gt_pow (x y:ℚ) (n:ℕ) (hxy: x > y) (hy: y ≥ 0) (hn: n > 0) : x^n > y^n
```

## Proposition 4.3.10(d) / Exercise 4.3.3

`Section_4_3.pow_abs` (theorem, [line 210](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L210)). An exercise, stated without proof.

> Proposition 4.3.10(d) (Properties of exponentiation, I) / Exercise 4.3.3

```lean
theorem pow_abs (x:ℚ) (n:ℕ) : |x|^n = |x^n|
```

## Definition 4.3.11

`Section_4_3.zpow_neg` (theorem, [line 216](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L216)). Proved here.

> Definition 4.3.11 (Exponentiation to a negative number).
> Here we use the Mathlib notion of integer exponentiation

```lean
theorem zpow_neg (x:ℚ) (n:ℕ) : x^(-(n:ℤ)) = 1/(x^n)
```

## Proposition 4.3.12(a) / Exercise 4.3.4

`Section_4_3.zpow_add` (theorem, [line 225](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L225)). An exercise, stated without proof.

> Proposition 4.3.12(a) (Properties of exponentiation, II) (exponent sum) / Exercise 4.3.4

```lean
theorem zpow_add (x:ℚ) (n m:ℤ) (hx: x ≠ 0): x^n * x^m = x^(n+m)
```

`Section_4_3.zpow_mul` (theorem, [line 228](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L228)). An exercise, stated without proof.

> Proposition 4.3.12(a) (Properties of exponentiation, II) (exponent product) / Exercise 4.3.4

```lean
theorem zpow_mul (x:ℚ) (n m:ℤ) : (x^n)^m = x^(n*m)
```

`Section_4_3.mul_zpow` (theorem, [line 231](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L231)). An exercise, stated without proof.

> Proposition 4.3.12(a) (Properties of exponentiation, II) (product base) / Exercise 4.3.4

```lean
theorem mul_zpow (x y:ℚ) (n:ℤ) : (x*y)^n = x^n * y^n
```

## Proposition 4.3.12(b) / Exercise 4.3.4

`Section_4_3.zpow_pos` (theorem, [line 234](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L234)). An exercise, stated without proof.

> Proposition 4.3.12(b) (Properties of exponentiation, II) (positivity) / Exercise 4.3.4

```lean
theorem zpow_pos {x:ℚ} (n:ℤ) (hx: x > 0) : x^n > 0
```

`Section_4_3.zpow_ge_zpow` (theorem, [line 237](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L237)). An exercise, stated without proof.

> Proposition 4.3.12(b) (Properties of exponentiation, II) (monotonicity) / Exercise 4.3.4

```lean
theorem zpow_ge_zpow {x y:ℚ} {n:ℤ} (hxy: x ≥ y) (hy: y > 0) (hn: n > 0): x^n ≥ y^n
```

## Proposition 4.3.12(c) / Exercise 4.3.4

`Section_4_3.zpow_inj` (theorem, [line 243](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L243)). An exercise, stated without proof.

> Proposition 4.3.12(c) (Properties of exponentiation, II) / Exercise 4.3.4

```lean
theorem zpow_inj {x y:ℚ} {n:ℤ} (hx: x > 0) (hy : y > 0) (hn: n ≠ 0) (hxy: x^n = y^n) : x = y
```

## Proposition 4.3.12(d) / Exercise 4.3.4

`Section_4_3.zpow_abs` (theorem, [line 247](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L247)). An exercise, stated without proof.

> Proposition 4.3.12(d) (Properties of exponentiation, II) / Exercise 4.3.4

```lean
theorem zpow_abs (x:ℚ) (n:ℤ) : |x|^n = |x^n|
```

## Exercise 4.3.5

`Section_4_3.two_pow_geq` (theorem, [line 250](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean#L250)). An exercise, stated without proof.

> Exercise 4.3.5

```lean
theorem two_pow_geq (N:ℕ) : 2^N ≥ N
```

## Depends on

Its Lean file imports no other section's file.

## Sources

- [Analysis/Section_4_3.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_4_3.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_4_3/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_4_3.html)
