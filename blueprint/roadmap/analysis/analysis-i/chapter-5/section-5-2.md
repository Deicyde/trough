---
declaration: lemma
origin: cited
lean: Chapter5.Rat.closeSeq_def, Chapter5.Rat.eventuallyClose_def, Chapter5.Rat.eventuallyClose_iff, Chapter5.Sequence.Equiv, Chapter5.Sequence.equiv_def, Chapter5.Sequence.equiv_iff, Chapter5.Sequence.equiv_example, Chapter5.Sequence.isCauchy_of_equiv, Chapter5.Sequence.isBounded_of_eventuallyClose
statement: formalized
---

# Section 5.2: Equivalent Cauchy sequences

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided doing so.
>
> Main constructions and results of this section:
>
> - Notion of an ε-close and eventually ε-close sequences of rationals.
> - Notion of an equivalent Cauchy sequence of rationals.
>
> ## Tips from past users
>
> Users of the companion who have completed the exercises in this section are welcome to send their tips for future users in this section as PRs.
>
> - (Add tip here)

*Quoted from [Analysis/Section_5_2.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_2.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 10 labelled items, carried by 13 declarations: 4 proved here, 8 stated without proof (2 of them exercises) and 1 definition. It also has 2 declarations and 2 examples with no label, counted here but not shown.

## Definition 5.2.1

`Chapter5.Rat.closeSeq_def` (lemma, [line 36](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_2.lean#L36)). Proved here.

> Definition 5.2.1 ($ε$-close sequences)

```lean
lemma Rat.closeSeq_def (ε: ℚ) (a b: Sequence) :
    ε.CloseSeq a b ↔ ∀ n, n ≥ a.n₀ → n ≥ b.n₀ → ε.Close (a n) (b n)
```

## Example 5.2.2 (a)

An `example` ([line 40](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_2.lean#L40)). Stated without proof.

> Example 5.2.2 (a)

```lean
example : (0.1:ℚ).CloseSeq ((fun n:ℕ ↦ ((-1)^n:ℚ)):Sequence)
((fun n:ℕ ↦ ((1.1:ℚ) * (-1)^n)):Sequence)
```

## Example 5.2.2 (b)

An `example` ([line 44](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_2.lean#L44)). Stated without proof.

> Example 5.2.2 (b)

```lean
example : ¬ (0.1:ℚ).Steady ((fun n:ℕ ↦ ((-1)^n:ℚ)):Sequence)
```

## Example 5.2.2 (c)

An `example` ([line 47](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_2.lean#L47)). Stated without proof.

> Example 5.2.2 (c)

```lean
example : ¬ (0.1:ℚ).Steady ((fun n:ℕ ↦ ((1.1:ℚ) * (-1)^n)):Sequence)
```

## Definition 5.2.3

`Chapter5.Rat.eventuallyClose_def` (lemma, [line 50](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_2.lean#L50)). Proved here.

> Definition 5.2.3 (Eventually ε-close sequences)

```lean
lemma Rat.eventuallyClose_def (ε: ℚ) (a b: Sequence) :
    ε.EventuallyClose a b ↔ ∃ N, ε.CloseSeq (a.from N) (b.from N)
```

`Chapter5.Rat.eventuallyClose_iff` (lemma, [line 54](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_2.lean#L54)). Stated without proof.

> Definition 5.2.3 (Eventually ε-close sequences)

```lean
lemma Rat.eventuallyClose_iff (ε: ℚ) (a b: ℕ → ℚ) :
    ε.EventuallyClose (a:Sequence) (b:Sequence) ↔ ∃ N, ∀ n ≥ N, |a n - b n| ≤ ε
```

## Example 5.2.5

An `example` ([line 58](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_2.lean#L58)). Stated without proof.

> Example 5.2.5

```lean
example : ¬ (0.1:ℚ).CloseSeq ((fun n:ℕ ↦ (1:ℚ)+10^(-(n:ℤ)-1)):Sequence)
  ((fun n:ℕ ↦ (1:ℚ)-10^(-(n:ℤ)-1)):Sequence)
```

## Definition 5.2.6

`Chapter5.Sequence.Equiv` (abbrev, [line 68](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_2.lean#L68)). A definition.

> Definition 5.2.6 (Equivalent sequences)

```lean
abbrev Sequence.Equiv (a b: ℕ → ℚ) : Prop
```

`Chapter5.Sequence.equiv_def` (lemma, [line 72](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_2.lean#L72)). Proved here.

> Definition 5.2.6 (Equivalent sequences)

```lean
lemma Sequence.equiv_def (a b: ℕ → ℚ) :
    Equiv a b ↔ ∀ (ε:ℚ), ε > 0 → ε.EventuallyClose (a:Sequence) (b:Sequence)
```

`Chapter5.Sequence.equiv_iff` (lemma, [line 76](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_2.lean#L76)). Stated without proof.

> Definition 5.2.6 (Equivalent sequences)

```lean
lemma Sequence.equiv_iff (a b: ℕ → ℚ) : Equiv a b ↔ ∀ ε > 0, ∃ N, ∀ n ≥ N, |a n - b n| ≤ ε
```

## Proposition 5.2.8

`Chapter5.Sequence.equiv_example` (lemma, [line 80](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_2.lean#L80)). Proved here.

> Proposition 5.2.8

```lean
lemma Sequence.equiv_example :
  -- This proof is perhaps more complicated than it needs to be; a shorter version may be
  -- possible that is still faithful to the original text.
  Equiv (fun n:ℕ ↦ (1:ℚ)+10^(-(n:ℤ)-1)) (fun n:ℕ ↦ (1:ℚ)-10^(-(n:ℤ)-1))
```

## Exercise 5.2.1

`Chapter5.Sequence.isCauchy_of_equiv` (theorem, [line 114](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_2.lean#L114)). An exercise, stated without proof.

> Exercise 5.2.1

```lean
theorem Sequence.isCauchy_of_equiv {a b: ℕ → ℚ} (hab: Equiv a b) :
    (a:Sequence).IsCauchy ↔ (b:Sequence).IsCauchy
```

## Exercise 5.2.2

`Chapter5.Sequence.isBounded_of_eventuallyClose` (theorem, [line 118](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_2.lean#L118)). An exercise, stated without proof.

> Exercise 5.2.2

```lean
theorem Sequence.isBounded_of_eventuallyClose {ε:ℚ} {a b: ℕ → ℚ} (hab: ε.EventuallyClose a b) :
    (a:Sequence).IsBounded ↔ (b:Sequence).IsBounded
```

## Depends on

- [Section 5.1: Cauchy sequences](section-5-1.md)

## Sources

- [Analysis/Section_5_2.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_2.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_5_2/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_5_2.html)
