---
declaration: abbrev
origin: cited
lean: Chapter9.BddAboveOn, Chapter9.BddOn.iff, Chapter9.BddOn.of_continuous_on_compact, Chapter9.BddAboveOn.isMaxOn, Chapter9.IsMaxOn.of_continuous_on_compact, Chapter9.BddOn.add
statement: formalized
---

# Section 9.6: The maximum principle

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text.  When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter.  In particular, there will be places where
> the Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
> - Continuous functions on closed and bounded intervals are bounded.
> - Continuous functions on closed and bounded intervals attain their maximum and minimum.

*Quoted from [Analysis/Section_9_6.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_6.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 7 labelled items, carried by 10 declarations: 1 proved here, 8 stated without proof (5 of them exercises) and 1 definition. It also has 14 declarations and 7 examples with no label, counted here but not shown.

## Definition 9.6.1

`Chapter9.BddAboveOn` (abbrev, [line 23](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_6.lean#L23)). A definition.

> Definition 9.6.1

```lean
abbrev BddAboveOn (f:ℝ → ℝ) (X:Set ℝ) : Prop
```

## Remark 9.6.2

`Chapter9.BddOn.iff` (theorem, [line 30](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_6.lean#L30)). Stated without proof.

> Remark 9.6.2

```lean
theorem BddOn.iff (f:ℝ → ℝ) (X:Set ℝ) : BddOn f X ↔ BddAboveOn f X ∧ BddBelowOn f X
```

## Lemma 9.6.3

`Chapter9.BddOn.of_continuous_on_compact` (theorem, [line 51](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_6.lean#L51)). Proved here.

> Lemma 9.6.3

```lean
theorem BddOn.of_continuous_on_compact {a b:ℝ} (_h:a < b) {f:ℝ → ℝ} (hf: ContinuousOn f (.Icc a b) ) :
  BddOn f (.Icc a b)
```

## Remark 9.6.6

`Chapter9.BddAboveOn.isMaxOn` (theorem, [line 81](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_6.lean#L81)). Stated without proof.

> Remark 9.6.6

```lean
theorem BddAboveOn.isMaxOn {f:ℝ → ℝ} {X:Set ℝ} {x₀:ℝ} (h: IsMaxOn f X x₀): BddAboveOn f X
```

## Proposition 9.6.7

`Chapter9.IsMaxOn.of_continuous_on_compact` (theorem, [line 86](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_6.lean#L86)). Stated without proof.

> Proposition 9.6.7 (Maximum principle)

```lean
theorem IsMaxOn.of_continuous_on_compact {a b:ℝ} (h:a < b) {f:ℝ → ℝ} (hf: ContinuousOn f (.Icc a b)) :
  ∃ xmax ∈ Set.Icc a b, IsMaxOn f (.Icc a b) xmax
```

## Exercise 9.6.1

An `example` ([line 158](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_6.lean#L158)). An exercise, stated without proof.

> Exercise 9.6.1 a)

```lean
example : ∃ f: ℝ → ℝ, ContinuousOn f (.Ioo 1 2) ∧ BddOn f (.Ioo 1 2) ∧
  ∃ x₀ ∈ Set.Ioo 1 2, IsMinOn f (.Ioo 1 2) x₀ ∧
  ¬ ∃ x₀ ∈ Set.Ioo 1 2, IsMaxOn f (.Ioo 1 2) x₀
```

An `example` ([line 164](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_6.lean#L164)). An exercise, stated without proof.

> Exercise 9.6.1 b)

```lean
example : ∃ f: ℝ → ℝ, ContinuousOn f (.Ici 0) ∧ BddOn f (.Ici 0) ∧
  ∃ x₀ ∈ Set.Ici 0, IsMaxOn f (.Ici 0) x₀ ∧
  ¬ ∃ x₀ ∈ Set.Ici 0, IsMinOn f (.Ici 0) x₀
```

An `example` ([line 170](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_6.lean#L170)). An exercise, stated without proof.

> Exercise 9.6.1 c)

```lean
example : ∃ f: ℝ → ℝ, BddOn f (.Icc (-1) 1) ∧
  (¬ ∃ x₀ ∈ Set.Icc (-1) 1, IsMinOn f (.Icc (-1) 1) x₀) ∧
  (¬ ∃ x₀ ∈ Set.Icc (-1) 1, IsMaxOn f (.Icc (-1) 1) x₀)
```

An `example` ([line 176](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_6.lean#L176)). An exercise, stated without proof.

> Exercise 9.6.1 d)

```lean
example : ∃ f: ℝ → ℝ, ¬ BddAboveOn f (.Icc (-1) 1) ∧ ¬ BddBelowOn f (.Icc (-1) 1)
```

## Exercise 9.6.2

`Chapter9.BddOn.add` (theorem, [line 179](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_6.lean#L179)). An exercise, stated without proof.

> Exercise 9.6.2

```lean
theorem BddOn.add (f g : ℝ → ℝ) (X : Set ℝ) (hf : BddOn f X) (hg : BddOn g X) :
    BddOn (f + g) X
```

## Depends on

- [Section 9.3: Limiting values of functions](section-9-3.md)
- [Section 9.4: Continuous functions](section-9-4.md)

## Sources

- [Analysis/Section_9_6.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_6.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_9_6/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_9_6.html)
