---
declaration: lemma
origin: cited
lean: Chapter6.ratPow_continuous, Chapter6.Real.rpow, Chapter6.Real.ratPow_nonneg, Chapter6.Real.ratPow_add, Chapter6.Real.ratPow_ratPow, Chapter6.Real.ratPow_neg, Chapter6.Real.ratPow_mono, Chapter6.Real.ratPow_mono_of_gt_one, Chapter6.Real.ratPow_mono_of_lt_one, Chapter6.Real.ratPow_mul
statement: formalized
---

# Section 6.7: Real exponentiation, part II

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Real exponentiation.
>
> Because the Chapter 5 reals have been deprecated in favor of the Mathlib reals, and Mathlib real
> exponentiation is defined without first going through rational exponentiation, we will adopt a
> somewhat awkward compromise, in that we will initially accept the Mathlib exponentiation operation
> (with all its API) when the exponent is a rational, and use this to define a notion of real
> exponentiation which in the epilogue to this chapter we will show is identical to the Mathlib operation.

*Quoted from [Analysis/Section_6_7.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_7.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 9 labelled items, carried by 10 declarations: 1 proved here, 8 stated without proof (7 of them exercises) and 1 definition. It also has 5 declarations with no label, counted here but not shown.

## Lemma 6.7.1

`Chapter6.ratPow_continuous` (lemma, [line 30](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_7.lean#L30)). Stated without proof.

> Lemma 6.7.1 (Continuity of exponentiation)

```lean
lemma ratPow_continuous {x α:ℝ} (hx: x > 0) {q: ℕ → ℚ}
 (hq: ((fun n ↦ (q n:ℝ)):Sequence).TendsTo α) :
 ((fun n ↦ x^(q n:ℝ)):Sequence).Convergent
```

## Definition 6.7.2

`Chapter6.Real.rpow` (abbrev, [line 130](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_7.lean#L130)). A definition.

> Definition 6.7.2 (Exponentiation to a real exponent)

```lean
noncomputable abbrev Real.rpow (x:ℝ) (α:ℝ) :ℝ
```

## Proposition 6.7.3(a) / Exercise 6.7.1

`Chapter6.Real.ratPow_nonneg` (theorem, [line 149](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_7.lean#L149)). An exercise, stated without proof.

> Proposition 6.7.3(a) / Exercise 6.7.1

```lean
theorem Real.ratPow_nonneg {x:ℝ} (hx: x > 0) (q:ℝ) : rpow x q ≥ 0
```

## Proposition 6.7.3(b)

`Chapter6.Real.ratPow_add` (theorem, [line 153](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_7.lean#L153)). Proved here.

> Proposition 6.7.3(b)

```lean
theorem Real.ratPow_add {x:ℝ} (hx: x > 0) (q r:ℝ) : rpow x (q+r) = rpow x q * rpow x r
```

## Proposition 6.7.3(b) / Exercise 6.7.1

`Chapter6.Real.ratPow_ratPow` (theorem, [line 167](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_7.lean#L167)). An exercise, stated without proof.

> Proposition 6.7.3(b) / Exercise 6.7.1

```lean
theorem Real.ratPow_ratPow {x:ℝ} (hx: x > 0) (q r:ℝ) : rpow (rpow x q) r = rpow x (q*r)
```

## Proposition 6.7.3(c) / Exercise 6.7.1

`Chapter6.Real.ratPow_neg` (theorem, [line 171](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_7.lean#L171)). An exercise, stated without proof.

> Proposition 6.7.3(c) / Exercise 6.7.1

```lean
theorem Real.ratPow_neg {x:ℝ} (hx: x > 0) (q:ℝ) : rpow x (-q) = 1 / rpow x q
```

## Proposition 6.7.3(d) / Exercise 6.7.1

`Chapter6.Real.ratPow_mono` (theorem, [line 175](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_7.lean#L175)). An exercise, stated without proof.

> Proposition 6.7.3(d) / Exercise 6.7.1

```lean
theorem Real.ratPow_mono {x y:ℝ} (hx: x > 0) (hy: y > 0) {q:ℝ} (h: q > 0) : x > y ↔ rpow x q > rpow y q
```

## Proposition 6.7.3(e) / Exercise 6.7.1

`Chapter6.Real.ratPow_mono_of_gt_one` (theorem, [line 179](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_7.lean#L179)). An exercise, stated without proof.

> Proposition 6.7.3(e) (base greater than one) / Exercise 6.7.1

```lean
theorem Real.ratPow_mono_of_gt_one {x:ℝ} (hx: x > 1) {q r:ℝ} : rpow x q > rpow x r ↔ q > r
```

`Chapter6.Real.ratPow_mono_of_lt_one` (theorem, [line 183](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_7.lean#L183)). An exercise, stated without proof.

> Proposition 6.7.3(e) (base less than one) / Exercise 6.7.1

```lean
theorem Real.ratPow_mono_of_lt_one {x:ℝ} (hx0: 0 < x) (hx: x < 1) {q r:ℝ} : rpow x q > rpow x r ↔ q < r
```

## Proposition 6.7.3(f) / Exercise 6.7.1

`Chapter6.Real.ratPow_mul` (theorem, [line 187](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_7.lean#L187)). An exercise, stated without proof.

> Proposition 6.7.3(f) / Exercise 6.7.1

```lean
theorem Real.ratPow_mul {x y:ℝ} (hx: x > 0) (hy: y > 0) (q:ℝ) : rpow (x*y) q = rpow x q * rpow y q
```

## Depends on

- [Chapter 5 epilogue: Isomorphism with the Mathlib real numbers](../chapter-5/section-5-epilogue.md)
- [Section 6.6: Subsequences](section-6-6.md)

## Sources

- [Analysis/Section_6_7.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_7.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_6_7/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_6_7.html)
