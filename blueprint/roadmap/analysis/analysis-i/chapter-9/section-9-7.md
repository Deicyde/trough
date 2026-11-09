---
declaration: theorem
origin: cited
lean: Chapter9.intermediate_value, Chapter9.f_9_7_2, Chapter9.continuous_image_Icc, Chapter9.exists_fixed_pt
statement: formalized
---

# Section 9.7: The intermediate value theorem

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text.  When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter.  In particular, there will be places where
> the Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
> - The intermediate value theorem.

*Quoted from [Analysis/Section_9_7.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_7.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 5 labelled items, carried by 5 declarations: 4 stated without proof (2 of them exercises) and 1 definition. It also has 2 declarations and 6 examples with no label, counted here but not shown.

## Theorem 9.7.1

`Chapter9.intermediate_value` (theorem, [line 22](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_7.lean#L22)). Stated without proof.

> Theorem 9.7.1 (Intermediate value theorem)

```lean
theorem intermediate_value {a b:ℝ} (hab: a < b) {f:ℝ → ℝ} (hf: ContinuousOn f (.Icc a b)) {y:ℝ} (hy: y ∈ Set.Icc (f a) (f b) ∨ y ∈ Set.Icc (f b) (f a)) :
  ∃ c ∈ Set.Icc a b, f c = y
```

## Remark 9.7.2

`Chapter9.f_9_7_2` (abbrev, [line 104](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_7.lean#L104)). A definition.

> Remark 9.7.2

```lean
abbrev f_9_7_2 : ℝ → ℝ
```

## Remark 9.7.3

An `example` ([line 113](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_7.lean#L113)). Stated without proof.

> Remark 9.7.3

```lean
example : ∃ x:ℝ, 0 ≤ x ∧ x ≤ 2 ∧ x^2 = 2
```

## Corollary 9.7.4 / Exercise 9.7.1

`Chapter9.continuous_image_Icc` (theorem, [line 116](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_7.lean#L116)). An exercise, stated without proof.

> Corollary 9.7.4 (Images of continuous functions) / Exercise 9.7.1

```lean
theorem continuous_image_Icc {a b:ℝ} (hab: a < b) {f:ℝ → ℝ} (hf: ContinuousOn f (.Icc a b)) {y:ℝ} (hy: sInf (f '' .Icc a b) ≤ y ∧ y ≤ sSup (f '' .Icc a b)) : ∃ c ∈ Set.Icc a b, f c = y
```

## Exercise 9.7.2

`Chapter9.exists_fixed_pt` (theorem, [line 123](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_7.lean#L123)). An exercise, stated without proof.

> Exercise 9.7.2

```lean
theorem exists_fixed_pt {f:ℝ → ℝ} (hf: ContinuousOn f (.Icc 0 1)) (hmap: f '' .Icc 0 1 ⊆ .Icc 0 1) : ∃ x ∈ Set.Icc 0 1, f x = x
```

## Depends on

- [Section 9.3: Limiting values of functions](section-9-3.md)
- [Section 9.4: Continuous functions](section-9-4.md)

## Sources

- [Analysis/Section_9_7.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_7.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_9_7/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_9_7.html)
