---
declaration: theorem
origin: cited
lean: Chapter11.integ_of_monotone, Chapter11.integ_of_antitone, Chapter11.integ_of_bdd_monotone, Chapter11.integ_of_bdd_antitone, Chapter11.summable_iff_integ_of_antitone
statement: formalized
---

# Section 11.6: Riemann integrability of monotone functions

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
> - Riemann integrability of monotone functions.

*Quoted from [Analysis/Section_11_6.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_6.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 7 labelled items, carried by 7 declarations: 2 proved here and 5 stated without proof (4 of them exercises).

## Proposition 11.6.1 (i)

`Chapter11.integ_of_monotone` (theorem, [line 24](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_6.lean#L24)). Proved here.

> Proposition 11.6.1 (i)

```lean
theorem integ_of_monotone {a b:ℝ} {f:ℝ → ℝ} (hf: MonotoneOn f (Icc a b)) :
  IntegrableOn f (Icc a b)
```

## Proposition 11.6.1 (ii)

`Chapter11.integ_of_antitone` (theorem, [line 134](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_6.lean#L134)). Proved here.

> Proposition 11.6.1 (ii)

```lean
theorem integ_of_antitone {a b:ℝ} {f:ℝ → ℝ} (hf: AntitoneOn f (Icc a b)) :
  IntegrableOn f (Icc a b)
```

## Corollary 11.6.3 (i) / Exercise 11.6.1

`Chapter11.integ_of_bdd_monotone` (theorem, [line 139](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_6.lean#L139)). An exercise, stated without proof.

> Corollary 11.6.3 (i) / Exercise 11.6.1

```lean
theorem integ_of_bdd_monotone {I:BoundedInterval} {f:ℝ → ℝ} (hbound: BddOn f I)
  (hf: MonotoneOn f I) : IntegrableOn f I
```

## Corollary 11.6.3 (ii) / Exercise 11.6.1

`Chapter11.integ_of_bdd_antitone` (theorem, [line 144](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_6.lean#L144)). An exercise, stated without proof.

> Corollary 11.6.3 (ii) / Exercise 11.6.1

```lean
theorem integ_of_bdd_antitone {I:BoundedInterval} {f:ℝ → ℝ} (hbound: BddOn f I)
  (hf: AntitoneOn f I) : IntegrableOn f I
```

## Proposition 11.6.4

`Chapter11.summable_iff_integ_of_antitone` (theorem, [line 149](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_6.lean#L149)). Stated without proof.

> Proposition 11.6.4 (Integral test)

```lean
theorem summable_iff_integ_of_antitone {f:ℝ → ℝ} (hnon: ∀ x ≥ 0, f x ≥ 0)
  (hf: AntitoneOn f (.Ici 0)) :
  Summable (fun n:ℕ ↦ f n) ↔ ∃ M, ∀ N ≥ 0, integ f (Icc 0 N) ≤ M
```

## Exercise 11.6.4 (a)

An `example` ([line 158](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_6.lean#L158)). An exercise, stated without proof.

> Exercise 11.6.4 (a)

```lean
example : ∃ (f:ℝ → ℝ), (∀ x ≥ 0, f x ≥ 0) ∧ Summable (fun n:ℕ ↦ f n) ∧ ¬ ∃ M, ∀ N ≥ 0, integ f (Icc 0 N) ≤ M
```

## Exercise 11.6.4 (b)

An `example` ([line 162](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_6.lean#L162)). An exercise, stated without proof.

> Exercise 11.6.4 (b)

```lean
example : ∃ (f:ℝ → ℝ), (∀ x ≥ 0, f x ≥ 0) ∧ ¬ Summable (fun n:ℕ ↦ f n) ∧ ∃ M, ∀ N ≥ 0, integ f (Icc 0 N) ≤ M
```

## Depends on

- [Section 9.8: Monotonic functions](../chapter-9/section-9-8.md)
- [Section 11.5: Riemann integrability of continuous functions](section-11-5.md)

## Sources

- [Analysis/Section_11_6.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_6.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_11_6/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_11_6.html)
