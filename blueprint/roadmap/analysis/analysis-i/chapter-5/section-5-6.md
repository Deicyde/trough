---
declaration: lemma
origin: cited
lean: Chapter5.Real.pow_zero, Chapter5.Real.pow_eq_pow, Chapter5.Real.root, Chapter5.Real.rootset_nonempty, Chapter5.Real.eq_root_iff_pow_eq, Chapter5.Real.root_nonneg, Chapter5.Real.root_pos, Chapter5.Real.root_mono, Chapter5.Real.root_mono_of_gt_one, Chapter5.Real.root_mono_of_lt_one, Chapter5.Real.root_of_one, Chapter5.Real.root_mul, Chapter5.Real.root_root, Chapter5.Real.ratPow, Chapter5.Real.pow_root_eq_pow_root, Chapter5.Real.ratPow_pos, Chapter5.Real.ratPow_add, Chapter5.Real.ratPow_ratPow, Chapter5.Real.ratPow_neg, Chapter5.Real.ratPow_mono, Chapter5.Real.ratPow_mono_of_gt_one, Chapter5.Real.ratPow_mono_of_lt_one, Chapter5.Real.ratPow_mul, Chapter5.Real.pow_even, Chapter5.Real.max_ratPow, Chapter5.Real.min_ratPow
statement: formalized
---

# Section 5.6: Real exponentiation, part I

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text.  When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter.  In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Exponentiating reals to natural numbers and integers.
> - nth roots.
> - Raising a real to a rational number.
>
> ## Tips from past users
>
> Users of the companion who have completed the exercises in this section are welcome to send their tips for future users in this section as PRs.
>
> - (Add tip here)

*Quoted from [Analysis/Section_5_6.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 20 labelled items, carried by 26 declarations: 2 proved here, 22 stated without proof (20 of them exercises) and 2 definitions. It also has 32 declarations and 1 example with no label, counted here but not shown.

## Definition 5.6.1

`Chapter5.Real.pow_zero` (lemma, [line 33](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L33)). Proved here.

> Definition 5.6.1 (Exponentiating a real by a natural number). Here we use the
> Mathlib definition coming from `Monoid`.

```lean
lemma Real.pow_zero (x: Real) : x ^ 0 = 1
```

## Definition 5.6.2

`Chapter5.Real.pow_eq_pow` (lemma, [line 71](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L71)). Proved here.

> Definition 5.6.2 (Exponentiating a real by an integer). Here we use the Mathlib definition coming from `DivInvMonoid`.

```lean
lemma Real.pow_eq_pow (x: Real) (n:ℕ): x ^ (n:ℤ) = x ^ n
```

`Chapter5.Real.root` (abbrev, [line 104](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L104)). A definition.

> Definition 5.6.2. We permit "junk values" when `x` is negative or `n` vanishes.

```lean
noncomputable abbrev Real.root (x:Real) (n:ℕ) : Real
```

## Lemma 5.6.5

`Chapter5.Real.rootset_nonempty` (theorem, [line 109](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L109)). Stated without proof.

> Lemma 5.6.5 (Existence of n^th roots)

```lean
theorem Real.rootset_nonempty {x:Real} (hx: x ≥ 0) (n:ℕ) (hn: n ≥ 1) : { y:Real | y ≥ 0 ∧ y^n ≤ x }.Nonempty
```

## Lemma 5.6.6 / Exercise 5.6.1

`Chapter5.Real.eq_root_iff_pow_eq` (theorem, [line 129](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L129)). An exercise, stated without proof.

> Lemma 5.6.6 (ab) / Exercise 5.6.1

```lean
theorem Real.eq_root_iff_pow_eq {x y:Real} (hx: x ≥ 0) (hy: y ≥ 0) {n:ℕ} (hn: n ≥ 1) :
  y = x.root n ↔ y^n = x
```

## Lemma 5.6.6 (c) / Exercise 5.6.1

`Chapter5.Real.root_nonneg` (theorem, [line 133](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L133)). An exercise, stated without proof.

> Lemma 5.6.6 (c) (nonnegativity) / Exercise 5.6.1

```lean
theorem Real.root_nonneg {x:Real} (hx: x ≥ 0) {n:ℕ} (hn: n ≥ 1) : x.root n ≥ 0
```

`Chapter5.Real.root_pos` (theorem, [line 136](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L136)). An exercise, stated without proof.

> Lemma 5.6.6 (c) (positivity) / Exercise 5.6.1

```lean
theorem Real.root_pos {x:Real} (hx: x ≥ 0) {n:ℕ} (hn: n ≥ 1) : x.root n > 0 ↔ x > 0
```

## Lemma 5.6.6 (d) / Exercise 5.6.1

`Chapter5.Real.root_mono` (theorem, [line 145](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L145)). An exercise, stated without proof.

> Lemma 5.6.6 (d) / Exercise 5.6.1

```lean
theorem Real.root_mono {x y:Real} (hx: x ≥ 0) (hy: y ≥ 0) {n:ℕ} (hn: n ≥ 1) : x > y ↔ x.root n > y.root n
```

## Lemma 5.6.6 (e) / Exercise 5.6.1

`Chapter5.Real.root_mono_of_gt_one` (theorem, [line 148](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L148)). An exercise, stated without proof.

> Lemma 5.6.6 (e) (base greater than one) / Exercise 5.6.1

```lean
theorem Real.root_mono_of_gt_one {x : Real} (hx: x > 1) {k l: ℕ} (hkl: k > l) (hl: l ≥ 1) : x.root k < x.root l
```

`Chapter5.Real.root_mono_of_lt_one` (theorem, [line 151](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L151)). An exercise, stated without proof.

> Lemma 5.6.6 (e) (base less than one) / Exercise 5.6.1

```lean
theorem Real.root_mono_of_lt_one {x : Real} (hx0: 0 < x) (hx: x < 1) {k l: ℕ} (hkl: k > l) (hl: l ≥ 1) : x.root k > x.root l
```

`Chapter5.Real.root_of_one` (theorem, [line 154](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L154)). An exercise, stated without proof.

> Lemma 5.6.6 (e) (base one) / Exercise 5.6.1

```lean
theorem Real.root_of_one {k: ℕ} (hk: k ≥ 1): (1:Real).root k = 1
```

## Lemma 5.6.6 (f) / Exercise 5.6.1

`Chapter5.Real.root_mul` (theorem, [line 157](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L157)). An exercise, stated without proof.

> Lemma 5.6.6 (f) / Exercise 5.6.1

```lean
theorem Real.root_mul {x y:Real} (hx: x ≥ 0) (hy: y ≥ 0) {n:ℕ} (hn: n ≥ 1) : (x*y).root n = (x.root n) * (y.root n)
```

## Lemma 5.6.6 (g) / Exercise 5.6.1

`Chapter5.Real.root_root` (theorem, [line 160](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L160)). An exercise, stated without proof.

> Lemma 5.6.6 (g) / Exercise 5.6.1

```lean
theorem Real.root_root {x:Real} (hx: x ≥ 0) {n m:ℕ} (hn: n ≥ 1) (hm: m ≥ 1): (x.root n).root m = x.root (n*m)
```

## Definition 5.6.7

`Chapter5.Real.ratPow` (abbrev, [line 171](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L171)). A definition.

> Definition 5.6.7

```lean
noncomputable abbrev Real.ratPow (x:Real) (q:ℚ) : Real
```

## Lemma 5.6.8

`Chapter5.Real.pow_root_eq_pow_root` (theorem, [line 181](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L181)). Stated without proof.

> Lemma 5.6.8

```lean
theorem Real.pow_root_eq_pow_root {a a':ℤ} {b b':ℕ} (hb: b > 0) (hb' : b' > 0)
  (hq : (a/b:ℚ) = (a'/b':ℚ)) {x:Real} (hx: x > 0) :
    (x.root b')^(a') = (x.root b)^(a)
```

## Lemma 5.6.9(a) / Exercise 5.6.2

`Chapter5.Real.ratPow_pos` (theorem, [line 217](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L217)). An exercise, stated without proof.

> Lemma 5.6.9(a) / Exercise 5.6.2

```lean
theorem Real.ratPow_pos {x:Real} (hx: x > 0) (q:ℚ) : x^q > 0
```

## Lemma 5.6.9(b) / Exercise 5.6.2

`Chapter5.Real.ratPow_add` (theorem, [line 221](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L221)). An exercise, stated without proof.

> Lemma 5.6.9(b) (sum of exponents) / Exercise 5.6.2

```lean
theorem Real.ratPow_add {x:Real} (hx: x > 0) (q r:ℚ) : x^(q+r) = x^q * x^r
```

`Chapter5.Real.ratPow_ratPow` (theorem, [line 225](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L225)). An exercise, stated without proof.

> Lemma 5.6.9(b) (product of exponents) / Exercise 5.6.2

```lean
theorem Real.ratPow_ratPow {x:Real} (hx: x > 0) (q r:ℚ) : (x^q)^r = x^(q*r)
```

## Lemma 5.6.9(c) / Exercise 5.6.2

`Chapter5.Real.ratPow_neg` (theorem, [line 229](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L229)). An exercise, stated without proof.

> Lemma 5.6.9(c) / Exercise 5.6.2

```lean
theorem Real.ratPow_neg {x:Real} (hx: x > 0) (q:ℚ) : x^(-q) = 1 / x^q
```

## Lemma 5.6.9(d) / Exercise 5.6.2

`Chapter5.Real.ratPow_mono` (theorem, [line 233](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L233)). An exercise, stated without proof.

> Lemma 5.6.9(d) / Exercise 5.6.2

```lean
theorem Real.ratPow_mono {x y:Real} (hx: x > 0) (hy: y > 0) {q:ℚ} (h: q > 0) : x > y ↔ x^q > y^q
```

## Lemma 5.6.9(e) / Exercise 5.6.2

`Chapter5.Real.ratPow_mono_of_gt_one` (theorem, [line 237](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L237)). An exercise, stated without proof.

> Lemma 5.6.9(e) (base greater than one) / Exercise 5.6.2

```lean
theorem Real.ratPow_mono_of_gt_one {x:Real} (hx: x > 1) {q r:ℚ} : x^q > x^r ↔ q > r
```

`Chapter5.Real.ratPow_mono_of_lt_one` (theorem, [line 241](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L241)). An exercise, stated without proof.

> Lemma 5.6.9(e) (base less than one) / Exercise 5.6.2

```lean
theorem Real.ratPow_mono_of_lt_one {x:Real} (hx0: 0 < x) (hx: x < 1) {q r:ℚ} : x^q > x^r ↔ q < r
```

## Lemma 5.6.9(f) / Exercise 5.6.2

`Chapter5.Real.ratPow_mul` (theorem, [line 245](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L245)). An exercise, stated without proof.

> Lemma 5.6.9(f) / Exercise 5.6.2

```lean
theorem Real.ratPow_mul {x y:Real} (hx: x > 0) (hy: y > 0) (q:ℚ) : (x*y)^q = x^q * y^q
```

## Exercise 5.6.3

`Chapter5.Real.pow_even` (theorem, [line 249](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L249)). An exercise, stated without proof.

> Exercise 5.6.3

```lean
theorem Real.pow_even (x:Real) {n:ℕ} (hn: Even n) : x^n ≥ 0
```

## Exercise 5.6.5 (a)

`Chapter5.Real.max_ratPow` (theorem, [line 252](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L252)). An exercise, stated without proof.

> Exercise 5.6.5 (a)

```lean
theorem Real.max_ratPow {x y:Real} (hx: x > 0) (hy: y > 0) {q:ℚ} (hq: q > 0) :
  max (x^q) (y^q) = (max x y)^q
```

## Exercise 5.6.5 (b)

`Chapter5.Real.min_ratPow` (theorem, [line 257](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean#L257)). An exercise, stated without proof.

> Exercise 5.6.5 (b)

```lean
theorem Real.min_ratPow {x y:Real} (hx: x > 0) (hy: y > 0) {q:ℚ} (hq: q > 0) :
  min (x^q) (y^q) = (min x y)^q
```

## Depends on

- [Section 5.5: The least upper bound property](section-5-5.md)

## Sources

- [Analysis/Section_5_6.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_6.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_5_6/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_5_6.html)
