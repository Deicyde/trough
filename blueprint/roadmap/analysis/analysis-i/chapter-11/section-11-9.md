---
declaration: theorem
origin: cited
lean: Chapter11.cts_of_integ, Chapter11.IntegrableOn.of_f_9_8_5, Chapter11.DifferentiableOn.of_F_11_9_2', Chapter11.AntiderivOn, Chapter11.integ_eq_antideriv_sub, Chapter11.antideriv_eq_antideriv_add_const, Chapter7.Series.converges_qseries'
statement: formalized
---

# Section 11.9: The two fundamental theorems of calculus

> I have attempted to make the translation as faithful a paraphrasing as possible of the
> original text. When there is a choice between a more idiomatic Lean solution and a
> more faithful translation, I have generally chosen the latter. In particular, there will
> be places where the Lean code could be "golfed" to be more elegant and idiomatic, but I
> have consciously avoided doing so.
>
> Main constructions and results of this section:
> - The fundamental theorems of calculus.

*Quoted from [Analysis/Section_11_9.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_9.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 8 labelled items, carried by 8 declarations: 2 proved here, 5 stated without proof (4 of them exercises) and 1 definition. It also has 7 declarations and 3 examples with no label, counted here but not shown.

## Theorem 11.9.1

`Chapter11.cts_of_integ` (theorem, [line 29](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_9.lean#L29)). Proved here.

> Theorem 11.9.1 (First Fundamental Theorem of Calculus).

```lean
theorem cts_of_integ {a b:ℝ} {f:ℝ → ℝ} (hf: IntegrableOn f (Icc a b)) :
  ContinuousOn (fun x => integ f (Icc a x)) (.Icc a b)
```

## Example 11.9.2

`Chapter11.IntegrableOn.of_f_9_8_5` (theorem, [line 92](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_9.lean#L92)). Proved here.

> Example 11.9.2

```lean
theorem IntegrableOn.of_f_9_8_5 : IntegrableOn f_9_8_5 (Icc 0 1)
```

## Exercise 11.9.1

`Chapter11.DifferentiableOn.of_F_11_9_2'` (theorem, [line 106](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_9.lean#L106)). An exercise, stated without proof.

> Exercise 11.9.1

```lean
theorem DifferentiableOn.of_F_11_9_2' {q:ℚ} (hq: (q:ℝ) ∈ Set.Ioo 0 1) : ¬ DifferentiableWithinAt ℝ F_11_9_2 (.Icc 0 1) q
```

## Definition 11.9.3

`Chapter11.AntiderivOn` (abbrev, [line 110](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_9.lean#L110)). A definition.

> Definition 11.9.3.  We drop the requirement that x be a limit point as this makes
> the Lean arguments slightly cleaner

```lean
abbrev AntiderivOn (F f: ℝ → ℝ) (I: BoundedInterval)
```

## Theorem 11.9.4

`Chapter11.integ_eq_antideriv_sub` (theorem, [line 118](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_9.lean#L118)). Stated without proof.

> Theorem 11.9.4 (Second Fundamental Theorem of Calculus)

```lean
theorem integ_eq_antideriv_sub {a b:ℝ} (h:a ≤ b) {f F: ℝ → ℝ}
  (hf: IntegrableOn f (Icc a b)) (hF: AntiderivOn F f (Icc a b)) :
  integ f (Icc a b) = F b - F a
```

## Lemma 11.9.5 / Exercise 11.9.2

`Chapter11.antideriv_eq_antideriv_add_const` (theorem, [line 226](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_9.lean#L226)). An exercise, stated without proof.

> Lemma 11.9.5 / Exercise 11.9.2

```lean
theorem antideriv_eq_antideriv_add_const {I:BoundedInterval} {f F G : ℝ → ℝ}
  (hfF: AntiderivOn F f I) (hfG: AntiderivOn G f I) :
   ∃ C, ∀ x ∈ (I:Set ℝ), F x = G x + C
```

## Exercise 11.9.3

An `example` ([line 232](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_9.lean#L232)). An exercise, stated without proof.

> Exercise 11.9.3

```lean
example {a b x₀:ℝ} (hab: a < b) (hx₀: x₀ ∈ Ioo a b) {f: ℝ → ℝ} (hf: MonotoneOn f (Icc a b)) :
  DifferentiableWithinAt ℝ (fun x => integ f (Icc a x)) (Icc a b) x₀ ↔
  ContinuousWithinAt f (Icc a b) x₀
```

## Exercise 11.6.5

`Chapter7.Series.converges_qseries'` (theorem, [line 240](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_9.lean#L240)). An exercise, stated without proof.

> Exercise 11.6.5, moved to Section 11.9

```lean
theorem Chapter7.Series.converges_qseries' (p:ℝ) : (mk' (m := 1) fun n ↦ 1 / (n:ℝ) ^ p : Series).converges ↔ (p>1)
```

## Depends on

- [Section 7.3: Sums of non-negative numbers](../chapter-7/section-7-3.md)
- [Section 9.4: Continuous functions](../chapter-9/section-9-4.md)
- [Section 9.8: Monotonic functions](../chapter-9/section-9-8.md)
- [Section 10.1: Basic definitions](../chapter-10/section-10-1.md)
- [Section 10.2: Local maxima, local minima, and derivatives](../chapter-10/section-10-2.md)
- [Section 11.6: Riemann integrability of monotone functions](section-11-6.md)
- [Section 11.8: The Riemann-Stieltjes integral](section-11-8.md)

## Sources

- [Analysis/Section_11_9.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_9.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_11_9/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_11_9.html)
