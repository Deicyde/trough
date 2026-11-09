---
declaration: abbrev
origin: cited
lean: Chapter5.BoundedAwayPos, Chapter5.BoundedAwayNeg, Chapter5.boundedAwayPos_def, Chapter5.boundedAwayNeg_def, Chapter5.Real.trichotomous, Chapter5.Real.not_zero_pos, Chapter5.Real.not_zero_neg, Chapter5.Real.not_pos_neg, Chapter5.Real.neg_iff_pos_of_neg, Chapter5.Real.pos_add, Chapter5.Real.pos_mul, Chapter5.Real.abs_of_pos, Chapter5.Real.abs_of_neg, Chapter5.Real.abs_of_zero, Chapter5.Real.instLT, Chapter5.Real.instLE, Chapter5.Real.trichotomous', Chapter5.Real.not_gt_and_lt, Chapter5.Real.not_gt_and_eq, Chapter5.Real.not_lt_and_eq, Chapter5.Real.antisymm, Chapter5.Real.lt_trans, Chapter5.Real.add_lt_add_right, Chapter5.Real.mul_lt_mul_right, Chapter5.Real.mul_le_mul_left, Chapter5.Real.inv_of_pos, Chapter5.Real.LIM_of_nonneg, Chapter5.Real.LIM_mono, Chapter5.Real.LIM_mono_fail, Chapter5.Real.exists_rat_le_and_nat_gt, Chapter5.Real.le_mul, Chapter5.Real.rat_between, Chapter5.Real.floor_exist, Chapter5.Real.exist_inv_nat_le, Chapter5.Real.dist_lt_iff, Chapter5.Real.dist_le_iff, Chapter5.Real.le_add_eps_iff, Chapter5.Real.dist_le_eps_iff, Chapter5.Real.LIM_of_le, Chapter5.Real.LIM_of_ge, Chapter5.Real.neg_max, Chapter5.Real.neg_min, Chapter5.Real.max_comm, Chapter5.Real.max_self, Chapter5.Real.max_add, Chapter5.Real.max_mul, Chapter5.Real.min_comm, Chapter5.Real.min_self, Chapter5.Real.min_add, Chapter5.Real.min_mul, Chapter5.Real.inv_max, Chapter5.Real.inv_min
statement: formalized
---

# Section 5.4: Ordering the reals

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Ordering on the real line
>
> ## Tips from past users
>
> Users of the companion who have completed the exercises in this section are welcome to send their tips for future users in this section as PRs.
>
> - (Add tip here)

*Quoted from [Analysis/Section_5_4.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 37 labelled items, carried by 57 declarations: 16 proved here, 37 stated without proof (36 of them exercises) and 4 definitions. It also has 29 declarations with no label, counted here but not shown.

## Definition 5.4.1

`Chapter5.BoundedAwayPos` (abbrev, [line 32](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L32)). A definition.

> Definition 5.4.1 (sequences bounded away from zero with sign). Sequences are indexed to start
> from zero as this is more convenient for Mathlib purposes.

```lean
abbrev BoundedAwayPos (a:ℕ → ℚ) : Prop
```

`Chapter5.BoundedAwayNeg` (abbrev, [line 36](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L36)). A definition.

> Definition 5.4.1 (sequences bounded away from zero with sign).

```lean
abbrev BoundedAwayNeg (a:ℕ → ℚ) : Prop
```

`Chapter5.boundedAwayPos_def` (theorem, [line 40](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L40)). Proved here.

> Definition 5.4.1 (sequences bounded away from zero with sign).

```lean
theorem boundedAwayPos_def (a:ℕ → ℚ) : BoundedAwayPos a ↔ ∃ (c:ℚ), c > 0 ∧ ∀ n, a n ≥ c
```

`Chapter5.boundedAwayNeg_def` (theorem, [line 44](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L44)). Proved here.

> Definition 5.4.1 (sequences bounded away from zero with sign).

```lean
theorem boundedAwayNeg_def (a:ℕ → ℚ) : BoundedAwayNeg a ↔ ∃ (c:ℚ), c > 0 ∧ ∀ n, a n ≤ -c
```

## Examples 5.4.2

An `example` ([line 48](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L48)). Proved here.

> Examples 5.4.2

```lean
example : BoundedAwayPos (fun n ↦ 1 + 10^(-(n:ℤ)-1))
```

An `example` ([line 51](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L51)). Proved here.

> Examples 5.4.2

```lean
example : BoundedAwayNeg (fun n ↦ -1 - 10^(-(n:ℤ)-1))
```

An `example` ([line 54](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L54)). Proved here.

> Examples 5.4.2

```lean
example : ¬ BoundedAwayPos (fun n ↦ (-1)^n)
```

An `example` ([line 58](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L58)). Proved here.

> Examples 5.4.2

```lean
example : ¬ BoundedAwayNeg (fun n ↦ (-1)^n)
```

An `example` ([line 62](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L62)). Proved here.

> Examples 5.4.2

```lean
example : BoundedAwayZero (fun n ↦ (-1)^n)
```

## Proposition 5.4.4 / Exercise 5.4.1

`Chapter5.Real.trichotomous` (theorem, [line 86](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L86)). An exercise, stated without proof.

> Proposition 5.4.4 (basic properties of positive reals) / Exercise 5.4.1

```lean
theorem Real.trichotomous (x:Real) : x = 0 ∨ x.IsPos ∨ x.IsNeg
```

`Chapter5.Real.not_zero_pos` (theorem, [line 89](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L89)). An exercise, stated without proof.

> Proposition 5.4.4 (basic properties of positive reals) / Exercise 5.4.1

```lean
theorem Real.not_zero_pos (x:Real) : ¬(x = 0 ∧ x.IsPos)
```

`Chapter5.Real.not_zero_neg` (theorem, [line 96](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L96)). An exercise, stated without proof.

> Proposition 5.4.4 (basic properties of positive reals) / Exercise 5.4.1

```lean
theorem Real.not_zero_neg (x:Real) : ¬(x = 0 ∧ x.IsNeg)
```

`Chapter5.Real.not_pos_neg` (theorem, [line 103](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L103)). An exercise, stated without proof.

> Proposition 5.4.4 (basic properties of positive reals) / Exercise 5.4.1

```lean
theorem Real.not_pos_neg (x:Real) : ¬(x.IsPos ∧ x.IsNeg)
```

`Chapter5.Real.neg_iff_pos_of_neg` (theorem, [line 107](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L107)). An exercise, stated without proof.

> Proposition 5.4.4 (basic properties of positive reals) / Exercise 5.4.1

```lean
theorem Real.neg_iff_pos_of_neg (x:Real) : x.IsNeg ↔ (-x).IsPos
```

`Chapter5.Real.pos_add` (theorem, [line 110](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L110)). An exercise, stated without proof.

> Proposition 5.4.4 (basic properties of positive reals) / Exercise 5.4.1

```lean
theorem Real.pos_add {x y:Real} (hx: x.IsPos) (hy: y.IsPos) : (x+y).IsPos
```

`Chapter5.Real.pos_mul` (theorem, [line 113](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L113)). An exercise, stated without proof.

> Proposition 5.4.4 (basic properties of positive reals) / Exercise 5.4.1

```lean
theorem Real.pos_mul {x y:Real} (hx: x.IsPos) (hy: y.IsPos) : (x*y).IsPos
```

## Definition 5.4.5

`Chapter5.Real.abs_of_pos` (theorem, [line 125](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L125)). Proved here.

> Definition 5.4.5 (absolute value)

```lean
theorem Real.abs_of_pos (x:Real) (hx: x.IsPos) : abs x = x
```

`Chapter5.Real.abs_of_neg` (theorem, [line 130](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L130)). Proved here.

> Definition 5.4.5 (absolute value)

```lean
theorem Real.abs_of_neg (x:Real) (hx: x.IsNeg) : abs x = -x
```

`Chapter5.Real.abs_of_zero` (theorem, [line 136](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L136)). Proved here.

> Definition 5.4.5 (absolute value)

```lean
theorem Real.abs_of_zero : abs 0 = 0
```

## Definition 5.4.6

`Chapter5.Real.instLT` (instance, [line 142](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L142)). A definition.

> Definition 5.4.6 (Ordering of the reals)

```lean
instance Real.instLT : LT Real
```

`Chapter5.Real.instLE` (instance, [line 146](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L146)). A definition.

> Definition 5.4.6 (Ordering of the reals)

```lean
instance Real.instLE : LE Real
```

## Proposition 5.4.7(a) / Exercise 5.4.2

`Chapter5.Real.trichotomous'` (theorem, [line 163](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L163)). An exercise, stated without proof.

> Proposition 5.4.7(a) (order trichotomy) / Exercise 5.4.2

```lean
theorem Real.trichotomous' (x y:Real) : x > y ∨ x < y ∨ x = y
```

`Chapter5.Real.not_gt_and_lt` (theorem, [line 166](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L166)). An exercise, stated without proof.

> Proposition 5.4.7(a) (order trichotomy) / Exercise 5.4.2

```lean
theorem Real.not_gt_and_lt (x y:Real) : ¬ (x > y ∧ x < y)
```

`Chapter5.Real.not_gt_and_eq` (theorem, [line 169](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L169)). An exercise, stated without proof.

> Proposition 5.4.7(a) (order trichotomy) / Exercise 5.4.2

```lean
theorem Real.not_gt_and_eq (x y:Real) : ¬ (x > y ∧ x = y)
```

`Chapter5.Real.not_lt_and_eq` (theorem, [line 172](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L172)). An exercise, stated without proof.

> Proposition 5.4.7(a) (order trichotomy) / Exercise 5.4.2

```lean
theorem Real.not_lt_and_eq (x y:Real) : ¬ (x < y ∧ x = y)
```

## Proposition 5.4.7(b) / Exercise 5.4.2

`Chapter5.Real.antisymm` (theorem, [line 175](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L175)). An exercise, stated without proof.

> Proposition 5.4.7(b) (order is anti-symmetric) / Exercise 5.4.2

```lean
theorem Real.antisymm (x y:Real) : x < y ↔ y > x
```

## Proposition 5.4.7(c) / Exercise 5.4.2

`Chapter5.Real.lt_trans` (theorem, [line 178](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L178)). An exercise, stated without proof.

> Proposition 5.4.7(c) (order is transitive) / Exercise 5.4.2

```lean
theorem Real.lt_trans {x y z:Real} (hxy: x < y) (hyz: y < z) : x < z
```

## Proposition 5.4.7(d) / Exercise 5.4.2

`Chapter5.Real.add_lt_add_right` (theorem, [line 181](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L181)). An exercise, stated without proof.

> Proposition 5.4.7(d) (addition preserves order) / Exercise 5.4.2

```lean
theorem Real.add_lt_add_right {x y:Real} (z:Real) (hxy: x < y) : x + z < y + z
```

## Proposition 5.4.7(e) / Exercise 5.4.2

`Chapter5.Real.mul_lt_mul_right` (theorem, [line 184](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L184)). Proved here.

> Proposition 5.4.7(e) (positive multiplication preserves order) / Exercise 5.4.2

```lean
theorem Real.mul_lt_mul_right {x y z:Real} (hxy: x < y) (hz: z.IsPos) : x * z < y * z
```

`Chapter5.Real.mul_le_mul_left` (theorem, [line 188](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L188)). An exercise, stated without proof.

> Proposition 5.4.7(e) (positive multiplication preserves order) / Exercise 5.4.2

```lean
theorem Real.mul_le_mul_left {x y z:Real} (hxy: x ≤ y) (hz: z.IsPos) : z * x ≤ z * y
```

## Proposition 5.4.8

`Chapter5.Real.inv_of_pos` (theorem, [line 213](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L213)). Proved here.

> Proposition 5.4.8

```lean
theorem Real.inv_of_pos {x:Real} (hx: x.IsPos) : x⁻¹.IsPos
```

## Proposition 5.4.9

`Chapter5.Real.LIM_of_nonneg` (theorem, [line 250](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L250)). Proved here.

> Proposition 5.4.9 (The non-negative reals are closed)

```lean
theorem Real.LIM_of_nonneg {a: ℕ → ℚ} (ha: ∀ n, a n ≥ 0) (hcauchy: (a:Sequence).IsCauchy) :
    LIM a ≥ 0
```

## Corollary 5.4.10

`Chapter5.Real.LIM_mono` (theorem, [line 271](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L271)). Proved here.

> Corollary 5.4.10

```lean
theorem Real.LIM_mono {a b:ℕ → ℚ} (ha: (a:Sequence).IsCauchy) (hb: (b:Sequence).IsCauchy)
  (hmono: ∀ n, a n ≤ b n) :
    LIM a ≤ LIM b
```

## Remark 5.4.11

`Chapter5.Real.LIM_mono_fail` (theorem, [line 279](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L279)). Stated without proof.

> Remark 5.4.11

```lean
theorem Real.LIM_mono_fail :
    ∃ (a b:ℕ → ℚ), (a:Sequence).IsCauchy
    ∧ (b:Sequence).IsCauchy
    ∧ (∀ n, a n > b n)
    ∧ ¬LIM a > LIM b
```

## Proposition 5.4.12

`Chapter5.Real.exists_rat_le_and_nat_gt` (theorem, [line 289](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L289)). Proved here.

> Proposition 5.4.12 (Bounding reals by rationals)

```lean
theorem Real.exists_rat_le_and_nat_gt {x:Real} (hx: x.IsPos) :
    (∃ q:ℚ, q > 0 ∧ (q:Real) ≤ x) ∧ ∃ N:ℕ, x < (N:Real)
```

## Corollary 5.4.13

`Chapter5.Real.le_mul` (theorem, [line 311](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L311)). Proved here.

> Corollary 5.4.13 (Archimedean property )

```lean
theorem Real.le_mul {ε:Real} (hε: ε.IsPos) (x:Real) : ∃ M:ℕ, M > 0 ∧ M * ε > x
```

## Proposition 5.4.14 / Exercise 5.4.5

`Chapter5.Real.rat_between` (theorem, [line 324](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L324)). An exercise, stated without proof.

> Proposition 5.4.14 / Exercise 5.4.5

```lean
theorem Real.rat_between {x y:Real} (hxy: x < y) : ∃ q:ℚ, x < (q:Real) ∧ (q:Real) < y
```

## Exercise 5.4.3

`Chapter5.Real.floor_exist` (theorem, [line 327](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L327)). An exercise, stated without proof.

> Exercise 5.4.3

```lean
theorem Real.floor_exist (x:Real) : ∃! n:ℤ, (n:Real) ≤ x ∧ x < (n:Real)+1
```

## Exercise 5.4.4

`Chapter5.Real.exist_inv_nat_le` (theorem, [line 330](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L330)). An exercise, stated without proof.

> Exercise 5.4.4

```lean
theorem Real.exist_inv_nat_le {x:Real} (hx: x.IsPos) : ∃ N:ℤ, N>0 ∧ (N:Real)⁻¹ < x
```

## Exercise 5.4.6 (a)

`Chapter5.Real.dist_lt_iff` (theorem, [line 333](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L333)). An exercise, stated without proof.

> Exercise 5.4.6 (a)

```lean
theorem Real.dist_lt_iff (ε x y:Real) : |x-y| < ε ↔ y-ε < x ∧ x < y+ε
```

## Exercise 5.4.6 (b)

`Chapter5.Real.dist_le_iff` (theorem, [line 336](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L336)). An exercise, stated without proof.

> Exercise 5.4.6 (b)

```lean
theorem Real.dist_le_iff (ε x y:Real) : |x-y| ≤ ε ↔ y-ε ≤ x ∧ x ≤ y+ε
```

## Exercise 5.4.7 (a)

`Chapter5.Real.le_add_eps_iff` (theorem, [line 339](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L339)). An exercise, stated without proof.

> Exercise 5.4.7 (a)

```lean
theorem Real.le_add_eps_iff (x y:Real) : (∀ ε > 0, x ≤ y+ε) ↔ x ≤ y
```

## Exercise 5.4.7 (b)

`Chapter5.Real.dist_le_eps_iff` (theorem, [line 342](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L342)). An exercise, stated without proof.

> Exercise 5.4.7 (b)

```lean
theorem Real.dist_le_eps_iff (x y:Real) : (∀ ε > 0, |x-y| ≤ ε) ↔ x = y
```

## Exercise 5.4.8 (a)

`Chapter5.Real.LIM_of_le` (theorem, [line 345](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L345)). An exercise, stated without proof.

> Exercise 5.4.8 (a)

```lean
theorem Real.LIM_of_le {x:Real} {a:ℕ → ℚ} (hcauchy: (a:Sequence).IsCauchy) (h: ∀ n, a n ≤ x) :
    LIM a ≤ x
```

## Exercise 5.4.8 (b)

`Chapter5.Real.LIM_of_ge` (theorem, [line 349](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L349)). An exercise, stated without proof.

> Exercise 5.4.8 (b)

```lean
theorem Real.LIM_of_ge {x:Real} {a:ℕ → ℚ} (hcauchy: (a:Sequence).IsCauchy) (h: ∀ n, a n ≥ x) :
    LIM a ≥ x
```

## Exercise 5.4.9 (a)

`Chapter5.Real.neg_max` (theorem, [line 357](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L357)). An exercise, stated without proof.

> Exercise 5.4.9 (a)

```lean
theorem Real.neg_max (x y:Real) : max x y = - min (-x) (-y)
```

## Exercise 5.4.9 (b)

`Chapter5.Real.neg_min` (theorem, [line 360](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L360)). An exercise, stated without proof.

> Exercise 5.4.9 (b)

```lean
theorem Real.neg_min (x y:Real) : min x y = - max (-x) (-y)
```

## Exercise 5.4.9 (c)

`Chapter5.Real.max_comm` (theorem, [line 363](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L363)). An exercise, stated without proof.

> Exercise 5.4.9 (c)

```lean
theorem Real.max_comm (x y:Real) : max x y = max y x
```

## Exercise 5.4.9 (d)

`Chapter5.Real.max_self` (theorem, [line 366](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L366)). An exercise, stated without proof.

> Exercise 5.4.9 (d)

```lean
theorem Real.max_self (x:Real) : max x x = x
```

## Exercise 5.4.9 (e)

`Chapter5.Real.max_add` (theorem, [line 369](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L369)). An exercise, stated without proof.

> Exercise 5.4.9 (e)

```lean
theorem Real.max_add (x y z:Real) : max (x + z) (y + z) = max x y + z
```

## Exercise 5.4.9 (f)

`Chapter5.Real.max_mul` (theorem, [line 372](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L372)). An exercise, stated without proof.

> Exercise 5.4.9 (f)

```lean
theorem Real.max_mul (x y :Real) {z:Real} (hz: z.IsPos) : max (x * z) (y * z) = max x y * z
```

## Exercise 5.4.9 (g)

`Chapter5.Real.min_comm` (theorem, [line 377](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L377)). An exercise, stated without proof.

> Exercise 5.4.9 (g)

```lean
theorem Real.min_comm (x y:Real) : min x y = min y x
```

## Exercise 5.4.9 (h)

`Chapter5.Real.min_self` (theorem, [line 380](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L380)). An exercise, stated without proof.

> Exercise 5.4.9 (h)

```lean
theorem Real.min_self (x:Real) : min x x = x
```

## Exercise 5.4.9 (i)

`Chapter5.Real.min_add` (theorem, [line 383](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L383)). An exercise, stated without proof.

> Exercise 5.4.9 (i)

```lean
theorem Real.min_add (x y z:Real) : min (x + z) (y + z) = min x y + z
```

## Exercise 5.4.9 (j)

`Chapter5.Real.min_mul` (theorem, [line 386](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L386)). An exercise, stated without proof.

> Exercise 5.4.9 (j)

```lean
theorem Real.min_mul (x y :Real) {z:Real} (hz: z.IsPos) : min (x * z) (y * z) = min x y * z
```

## Exercise 5.4.9 (k)

`Chapter5.Real.inv_max` (theorem, [line 390](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L390)). An exercise, stated without proof.

> Exercise 5.4.9 (k)

```lean
theorem Real.inv_max {x y :Real} (hx:x.IsPos) (hy:y.IsPos) : (max x y)⁻¹ = min x⁻¹ y⁻¹
```

## Exercise 5.4.9 (l)

`Chapter5.Real.inv_min` (theorem, [line 393](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean#L393)). An exercise, stated without proof.

> Exercise 5.4.9 (l)

```lean
theorem Real.inv_min {x y :Real} (hx:x.IsPos) (hy:y.IsPos) : (min x y)⁻¹ = max x⁻¹ y⁻¹
```

## Depends on

- [Section 5.3: The construction of the real numbers](section-5-3.md)

## Sources

- [Analysis/Section_5_4.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_4.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_5_4/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_5_4.html)
