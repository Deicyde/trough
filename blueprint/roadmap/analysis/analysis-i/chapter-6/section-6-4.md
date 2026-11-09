---
declaration: theorem
origin: cited
lean: Chapter6.Sequence.limit_point_of_limit, Chapter6.Sequence.limit_point_of_limit_unique, Chapter6.Sequence.gt_limsup_bounds, Chapter6.Sequence.lt_liminf_bounds, Chapter6.Sequence.lt_limsup_bounds, Chapter6.Sequence.gt_liminf_bounds, Chapter6.Sequence.inf_le_liminf, Chapter6.Sequence.liminf_le_limsup, Chapter6.Sequence.limsup_le_sup, Chapter6.Sequence.limit_point_between_liminf_limsup, Chapter6.Sequence.limit_point_of_limsup, Chapter6.Sequence.limit_point_of_liminf, Chapter6.Sequence.tendsTo_iff_eq_limsup_liminf, Chapter6.Sequence.sup_mono, Chapter6.Sequence.inf_mono, Chapter6.Sequence.limsup_mono, Chapter6.Sequence.liminf_mono, Chapter6.Sequence.lim_of_between, Chapter6.Sequence.tendsTo_zero_iff, Chapter6.Sequence.Cauchy_iff_convergent, Chapter6.Sequence.sup_not_strict_mono, Chapter6.Sequence.tendsTo_real_iff, Chapter6.Sequence.extended_limit_point_of_limsup, Chapter6.Sequence.extended_limit_point_of_liminf, Chapter6.Sequence.exists_three_limit_points, Chapter6.Sequence.limit_points_of_limit_points
statement: formalized
---

# Section 6.4: Limsup, liminf, and limit points

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Lim sup and lim inf of sequences
> - Limit points of sequences
> - Comparison and squeeze tests
> - Completeness of the reals

*Quoted from [Analysis/Section_6_4.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 36 labelled items, carried by 39 declarations: 3 proved here, 35 stated without proof (20 of them exercises) and 1 definition (1 with a value left as `sorry`). It also has 19 declarations and 18 examples with no label, counted here but not shown.

## Example 6.4.3 (a)

An `example` ([line 42](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L42)). Stated without proof.

> Example 6.4.3 (a)

```lean
example : (0.1:ℝ).Adherent Example_6_4_3 0.8
```

## Example 6.4.3 (b)

An `example` ([line 45](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L45)). Stated without proof.

> Example 6.4.3 (b)

```lean
example : ¬ (0.1:ℝ).ContinuallyAdherent Example_6_4_3 0.8
```

## Example 6.4.3 (c)

An `example` ([line 48](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L48)). Stated without proof.

> Example 6.4.3 (c)

```lean
example : (0.1:ℝ).ContinuallyAdherent Example_6_4_3 1
```

## Example 6.4.3 (d)

An `example` ([line 51](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L51)). Stated without proof.

> Example 6.4.3 (d)

```lean
example : Example_6_4_3.LimitPoint 1
```

## Example 6.4.4 (a)

An `example` ([line 57](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L57)). Stated without proof.

> Example 6.4.4 (a)

```lean
example : (0.1:ℝ).Adherent Example_6_4_4 1
```

## Example 6.4.4 (b)

An `example` ([line 60](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L60)). Stated without proof.

> Example 6.4.4 (b)

```lean
example : (0.1:ℝ).ContinuallyAdherent Example_6_4_4 1
```

## Example 6.4.4 (c)

An `example` ([line 63](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L63)). Stated without proof.

> Example 6.4.4 (c)

```lean
example : Example_6_4_4.LimitPoint 1
```

## Example 6.4.4 (d)

An `example` ([line 66](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L66)). Stated without proof.

> Example 6.4.4 (d)

```lean
example : Example_6_4_4.LimitPoint (-1)
```

## Example 6.4.4 (e)

An `example` ([line 69](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L69)). Stated without proof.

> Example 6.4.4 (e)

```lean
example : ¬ Example_6_4_4.LimitPoint 0
```

## Proposition 6.4.5 (a) / Exercise 6.4.1

`Chapter6.Sequence.limit_point_of_limit` (theorem, [line 72](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L72)). An exercise, stated without proof.

> Proposition 6.4.5 (a) / Exercise 6.4.1

```lean
theorem Sequence.limit_point_of_limit {a:Sequence} {x:ℝ} (h: a.TendsTo x) : a.LimitPoint x
```

## Proposition 6.4.5 (b) / Exercise 6.4.1

`Chapter6.Sequence.limit_point_of_limit_unique` (theorem, [line 76](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L76)). An exercise, stated without proof.

> Proposition 6.4.5 (b) / Exercise 6.4.1

```lean
theorem Sequence.limit_point_of_limit_unique {a:Sequence} {x y:ℝ} (h: a.TendsTo x) (hy: a.LimitPoint y) : x = y
```

## Proposition 6.4.12(a)

`Chapter6.Sequence.gt_limsup_bounds` (theorem, [line 145](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L145)). Proved here.

> Proposition 6.4.12(a)

```lean
theorem Sequence.gt_limsup_bounds {a:Sequence} {x:EReal} (h: x > a.limsup) :
    ∃ N ≥ a.m, ∀ n ≥ N, a n < x
```

## Proposition 6.4.12(a')

`Chapter6.Sequence.lt_liminf_bounds` (theorem, [line 158](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L158)). Stated without proof.

> Proposition 6.4.12(a')

```lean
theorem Sequence.lt_liminf_bounds {a:Sequence} {y:EReal} (h: y < a.liminf) :
    ∃ N ≥ a.m, ∀ n ≥ N, a n > y
```

## Proposition 6.4.12(b)

`Chapter6.Sequence.lt_limsup_bounds` (theorem, [line 163](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L163)). Proved here.

> Proposition 6.4.12(b)

```lean
theorem Sequence.lt_limsup_bounds {a:Sequence} {x:EReal} (h: x < a.limsup) {N:ℤ} (hN: N ≥ a.m) :
    ∃ n ≥ N, a n > x
```

## Proposition 6.4.12(b')

`Chapter6.Sequence.gt_liminf_bounds` (theorem, [line 171](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L171)). Stated without proof.

> Proposition 6.4.12(b')

```lean
theorem Sequence.gt_liminf_bounds {a:Sequence} {x:EReal} (h: x > a.liminf) {N:ℤ} (hN: N ≥ a.m) :
    ∃ n ≥ N, a n < x
```

## Proposition 6.4.12(c) / Exercise 6.4.3

`Chapter6.Sequence.inf_le_liminf` (theorem, [line 176](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L176)). An exercise, stated without proof.

> Proposition 6.4.12(c) / Exercise 6.4.3

```lean
theorem Sequence.inf_le_liminf (a:Sequence) : a.inf ≤ a.liminf
```

## Proposition 6.4.12(c') / Exercise 6.4.3

`Chapter6.Sequence.liminf_le_limsup` (theorem, [line 179](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L179)). An exercise, stated without proof.

> Proposition 6.4.12(c') / Exercise 6.4.3

```lean
theorem Sequence.liminf_le_limsup (a:Sequence) : a.liminf ≤ a.limsup
```

## Proposition 6.4.12(c'') / Exercise 6.4.3

`Chapter6.Sequence.limsup_le_sup` (theorem, [line 182](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L182)). An exercise, stated without proof.

> Proposition 6.4.12(c'') / Exercise 6.4.3

```lean
theorem Sequence.limsup_le_sup (a:Sequence) : a.limsup ≤ a.sup
```

## Proposition 6.4.12(d) / Exercise 6.4.3

`Chapter6.Sequence.limit_point_between_liminf_limsup` (theorem, [line 185](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L185)). An exercise, stated without proof.

> Proposition 6.4.12(d) / Exercise 6.4.3

```lean
theorem Sequence.limit_point_between_liminf_limsup {a:Sequence} {c:ℝ} (h: a.LimitPoint c) :
  a.liminf ≤ c ∧ c ≤ a.limsup
```

## Proposition 6.4.12(e) / Exercise 6.4.3

`Chapter6.Sequence.limit_point_of_limsup` (theorem, [line 190](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L190)). An exercise, stated without proof.

> Proposition 6.4.12(e) / Exercise 6.4.3

```lean
theorem Sequence.limit_point_of_limsup {a:Sequence} {L_plus:ℝ} (h: a.limsup = L_plus) :
    a.LimitPoint L_plus
```

## Proposition 6.4.12(e') / Exercise 6.4.3

`Chapter6.Sequence.limit_point_of_liminf` (theorem, [line 195](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L195)). An exercise, stated without proof.

> Proposition 6.4.12(e') / Exercise 6.4.3

```lean
theorem Sequence.limit_point_of_liminf {a:Sequence} {L_minus:ℝ} (h: a.liminf = L_minus) :
    a.LimitPoint L_minus
```

## Proposition 6.4.12(f) / Exercise 6.4.3

`Chapter6.Sequence.tendsTo_iff_eq_limsup_liminf` (theorem, [line 200](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L200)). An exercise, stated without proof.

> Proposition 6.4.12(f) / Exercise 6.4.3

```lean
theorem Sequence.tendsTo_iff_eq_limsup_liminf {a:Sequence} (c:ℝ) :
  a.TendsTo c ↔ a.liminf = c ∧ a.limsup = c
```

## Lemma 6.4.13 / Exercise 6.4.4

`Chapter6.Sequence.sup_mono` (theorem, [line 205](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L205)). An exercise, stated without proof.

> Lemma 6.4.13 (Comparison principle, sup) / Exercise 6.4.4

```lean
theorem Sequence.sup_mono {a b:Sequence} (hm: a.m = b.m) (hab: ∀ n ≥ a.m, a n ≤ b n) :
    a.sup ≤ b.sup
```

`Chapter6.Sequence.inf_mono` (theorem, [line 209](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L209)). An exercise, stated without proof.

> Lemma 6.4.13 (Comparison principle, inf) / Exercise 6.4.4

```lean
theorem Sequence.inf_mono {a b:Sequence} (hm: a.m = b.m) (hab: ∀ n ≥ a.m, a n ≤ b n) :
    a.inf ≤ b.inf
```

`Chapter6.Sequence.limsup_mono` (theorem, [line 213](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L213)). An exercise, stated without proof.

> Lemma 6.4.13 (Comparison principle, limsup) / Exercise 6.4.4

```lean
theorem Sequence.limsup_mono {a b:Sequence} (hm: a.m = b.m) (hab: ∀ n ≥ a.m, a n ≤ b n) :
    a.limsup ≤ b.limsup
```

`Chapter6.Sequence.liminf_mono` (theorem, [line 217](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L217)). An exercise, stated without proof.

> Lemma 6.4.13 (Comparison principle, liminf) / Exercise 6.4.4

```lean
theorem Sequence.liminf_mono {a b:Sequence} (hm: a.m = b.m) (hab: ∀ n ≥ a.m, a n ≤ b n) :
    a.liminf ≤ b.liminf
```

## Corollary 6.4.14 / Exercise 6.4.5

`Chapter6.Sequence.lim_of_between` (theorem, [line 221](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L221)). An exercise, stated without proof.

> Corollary 6.4.14 (Squeeze test) / Exercise 6.4.5

```lean
theorem Sequence.lim_of_between {a b c:Sequence} {L:ℝ} (hm: b.m = a.m ∧ c.m = a.m)
  (hab: ∀ n ≥ a.m, a n ≤ b n ∧ b n ≤ c n) (ha: a.TendsTo L) (hb: c.TendsTo L) :
    b.TendsTo L
```

## Example 6.4.15 (a)

An `example` ([line 226](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L226)). Stated without proof.

> Example 6.4.15 (a)

```lean
example : ((fun (n:ℕ) ↦ 2/(n+1:ℝ)):Sequence).TendsTo 0
```

## Example 6.4.15 (b)

An `example` ([line 230](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L230)). Stated without proof.

> Example 6.4.15 (b)

```lean
example : ((fun (n:ℕ) ↦ -2/(n+1:ℝ)):Sequence).TendsTo 0
```

## Example 6.4.15 (c)

An `example` ([line 234](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L234)). Stated without proof.

> Example 6.4.15 (c)

```lean
example : ((fun (n:ℕ) ↦ (-1)^n/(n+1:ℝ) + 1 / (n+1)^2):Sequence).TendsTo 0
```

## Example 6.4.15 (d)

An `example` ([line 238](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L238)). Stated without proof.

> Example 6.4.15 (d)

```lean
example : ((fun (n:ℕ) ↦ (2:ℝ)^(-(n:ℤ))):Sequence).TendsTo 0
```

## Corollary 6.4.17 / Exercise 6.4.7

`Chapter6.Sequence.tendsTo_zero_iff` (theorem, [line 248](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L248)). An exercise, stated without proof.

> Corollary 6.4.17 (Zero test for sequences) / Exercise 6.4.7

```lean
theorem Sequence.tendsTo_zero_iff (a:Sequence) :
  a.TendsTo (0:ℝ) ↔ a.abs.TendsTo (0:ℝ)
```

## Theorem 6.4.18

`Chapter6.Sequence.Cauchy_iff_convergent` (theorem, [line 279](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L279)). Proved here.

> Theorem 6.4.18 (Completeness of the reals)

```lean
theorem Sequence.Cauchy_iff_convergent (a:Sequence) :
  a.IsCauchy ↔ a.Convergent
```

## Exercise 6.4.6

`Chapter6.Sequence.sup_not_strict_mono` (theorem, [line 308](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L308)). An exercise, stated without proof.

> Exercise 6.4.6

```lean
theorem Sequence.sup_not_strict_mono : ∃ (a b:ℕ → ℝ), (∀ n, a n < b n) ∧ ¬ (a:Sequence).sup < (b:Sequence).sup
```

## Exercise 6.4.7

`Chapter6.Sequence.tendsTo_real_iff` (def, [line 312](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L312)). A definition whose value is left as `sorry`.

> Exercise 6.4.7

```lean
def Sequence.tendsTo_real_iff :
  Decidable (∀ (a:Sequence) (x:ℝ), a.TendsTo x ↔ a.abs.TendsTo x)
```

## Exercise 6.4.8 (i)

`Chapter6.Sequence.extended_limit_point_of_limsup` (theorem, [line 321](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L321)). An exercise, stated without proof.

> Exercise 6.4.8 (i)

```lean
theorem Sequence.extended_limit_point_of_limsup (a:Sequence) : a.ExtendedLimitPoint a.limsup
```

## Exercise 6.4.8 (ii)

`Chapter6.Sequence.extended_limit_point_of_liminf` (theorem, [line 324](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L324)). An exercise, stated without proof.

> Exercise 6.4.8 (ii)

```lean
theorem Sequence.extended_limit_point_of_liminf (a:Sequence) : a.ExtendedLimitPoint a.liminf
```

## Exercise 6.4.9

`Chapter6.Sequence.exists_three_limit_points` (theorem, [line 331](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L331)). An exercise, stated without proof.

> Exercise 6.4.9

```lean
theorem Sequence.exists_three_limit_points : ∃ a:Sequence, ∀ L:EReal, a.ExtendedLimitPoint L ↔ L = ⊥ ∨ L = 0 ∨ L = ⊤
```

## Exercise 6.4.10

`Chapter6.Sequence.limit_points_of_limit_points` (theorem, [line 334](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean#L334)). An exercise, stated without proof.

> Exercise 6.4.10

```lean
theorem Sequence.limit_points_of_limit_points {a b:Sequence} {c:ℝ} (hab: ∀ n ≥ b.m, a.LimitPoint (b n)) (hbc: b.LimitPoint c) : a.LimitPoint c
```

## Depends on

- [Section 6.3: Suprema and infima of sequences](section-6-3.md)

## Sources

- [Analysis/Section_6_4.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_4.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_6_4/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_6_4.html)
