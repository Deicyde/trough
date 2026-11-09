---
declaration: theorem
origin: cited
lean: Chapter9.BddAbove.unbounded_iff, Chapter9.Filter.Tendsto.AtTop.iff
statement: formalized
---

# Section 9.10: Limits at infinity

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text.  When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter.  In particular, there will be places where
> the Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
> - Bare-bones API for the Mathlib versions of adherent at infinity, and limits at infinity.

*Quoted from [Analysis/Section_9_10.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_10.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 4 labelled items, carried by 4 declarations: 2 proved here and 2 stated without proof (2 of them exercises). It also has 3 declarations with no label, counted here but not shown.

## Definition 9.10.1

`Chapter9.BddAbove.unbounded_iff` (theorem, [line 18](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_10.lean#L18)). Proved here.

> Definition 9.10.1 (Infinite adherent point).  We use `¬ BddAbove X` as our notation for `+∞` being an adherent point

```lean
theorem BddAbove.unbounded_iff (X:Set ℝ) : ¬ BddAbove X ↔ ∀ M, ∃ x ∈ X, x > M
```

## Definition 9.10.13

`Chapter9.Filter.Tendsto.AtTop.iff` (theorem, [line 40](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_10.lean#L40)). Proved here.

> Definition 9.10.13 (Limit at infinity)

```lean
theorem Filter.Tendsto.AtTop.iff {X: Set ℝ} (f:ℝ → ℝ) (L:ℝ) : Filter.Tendsto f (.atTop ⊓ .principal X) (nhds L) ↔ ∀ ε > (0:ℝ), ∃ M, ∀ x ∈ X ∩ .Ici M, |f x - L| < ε
```

## Exercise 9.10.4

An `example` ([line 47](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_10.lean#L47)). An exercise, stated without proof.

> Exercise 9.10.4

```lean
example : Filter.Tendsto (fun x:ℝ ↦ 1/x) (.atTop ⊓ .principal (.Ioi 0)) (nhds 0)
```

## Exercise 9.10.1

An `example` ([line 52](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_10.lean#L52)). An exercise, stated without proof.

> Exercise 9.10.1

```lean
example (a:ℕ → ℝ) (L:ℝ) : Filter.Tendsto (fun x:ℝ ↦ (if h:(∃ n:ℕ, x = n) then a h.choose else 0)) (.atTop ⊓ .principal ((fun n:ℕ ↦ (n:ℝ)) '' .univ)) (nhds L) ↔ Filter.atTop.Tendsto a (nhds L)
```

## Depends on

Its Lean file imports no other section's file.

## Sources

- [Analysis/Section_9_10.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_10.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_9_10/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_9_10.html)
