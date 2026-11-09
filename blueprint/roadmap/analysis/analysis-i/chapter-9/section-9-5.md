---
declaration: abbrev
origin: cited
lean: Chapter9.RightLimitExists, Chapter9.ContinuousAt.iff_eq_left_right_limit
statement: formalized
---

# Section 9.5: Left and right limits

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text.  When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter.  In particular, there will be places where
> the Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
> - Left and right limits.

*Quoted from [Analysis/Section_9_5.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_5.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 3 labelled items, carried by 3 declarations: 2 stated without proof and 1 definition. It also has 11 declarations and 5 examples with no label, counted here but not shown.

## Definition 9.5.1

`Chapter9.RightLimitExists` (abbrev, [line 22](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_5.lean#L22)). A definition.

> Definition 9.5.1.  We give left and right limits the "junk" value of 0 if the limit does not exist.

```lean
abbrev RightLimitExists (X: Set ℝ) (f: ℝ → ℝ) (x₀:ℝ) : Prop
```

## Example 9.5.2

An `example` ([line 57](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_5.lean#L57)). Stated without proof.

> Example 9.5.2.  The second part of this example is no longer operative as we assign "junk" values to our functions instead of leaving them undefined.

```lean
example : right_limit .univ Real.sign 0 = 1
```

## Proposition 9.5.3

`Chapter9.ContinuousAt.iff_eq_left_right_limit` (theorem, [line 80](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_5.lean#L80)). Stated without proof.

> Proposition 9.5.3

```lean
theorem ContinuousAt.iff_eq_left_right_limit {X: Set ℝ} {f: ℝ → ℝ} {x₀:ℝ} (h: x₀ ∈ X)
  (had_left: AdherentPt x₀ (X ∩ .Iio x₀)) (had_right: AdherentPt x₀ (X ∩ .Ioi x₀)) :
  ContinuousWithinAt f X x₀ ↔ (RightLimitExists X f x₀ ∧ right_limit X f x₀ = f x₀) ∧ (LeftLimitExists X f x₀ ∧ left_limit X f x₀ = f x₀)
```

## Depends on

- [Section 9.3: Limiting values of functions](section-9-3.md)
- [Section 9.4: Continuous functions](section-9-4.md)

## Sources

- [Analysis/Section_9_5.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_5.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_9_5/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_9_5.html)
