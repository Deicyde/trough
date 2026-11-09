---
declaration: structure
origin: cited
lean: Chapter5.Sequence, Chapter5.Sequence.squares, Chapter5.Sequence.three, Chapter5.Sequence.squares_from_three, Chapter5.Rat.Steady.coe, Rat.EventuallySteady, Chapter5.Sequence.ex_5_1_7_a, Chapter5.Sequence.ex_5_1_7_b, Chapter5.Sequence.ex_5_1_7_c, Chapter5.Sequence.ex_5_1_7_d, Chapter5.Sequence.ex_5_1_10_a, Chapter5.Sequence.ex_5_1_10_b, Chapter5.Sequence.IsCauchy.harmonic, Chapter5.boundedBy_def, Chapter5.Sequence.boundedBy_def, Chapter5.Sequence.isBounded_def, Chapter5.IsBounded.finite, Chapter5.Sequence.isBounded_of_isCauchy, Chapter5.Sequence.isBounded_add
statement: formalized
---

# Section 5.1: Cauchy sequences

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Notion of a sequence of rationals
> - Notions of `ε`-steadiness, eventual `ε`-steadiness, and Cauchy sequences
>
> ## Tips from past users
>
> Users of the companion who have completed the exercises in this section are welcome to send their tips for future users in this section as PRs.
>
> - (Add tip here)

*Quoted from [Analysis/Section_5_1.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 21 labelled items, carried by 32 declarations: 19 proved here, 8 stated without proof (2 of them exercises) and 5 definitions. It also has 23 declarations and 4 examples with no label, counted here but not shown.

## Definition 5.1.1

`Chapter5.Sequence` (structure, [line 35](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L35)). A definition.

> Definition 5.1.1 (Sequence). To avoid some technicalities involving dependent types, we extend
> sequences by zero to the left of the starting point `n₀`.

```lean
structure Sequence
```

## Example 5.1.2 (a)

`Chapter5.Sequence.squares` (abbrev, [line 82](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L82)). A definition.

> Example 5.1.2 (a)

```lean
abbrev Sequence.squares : Sequence
```

## Example 5.1.2 (b)

An `example` ([line 85](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L85)). Proved here.

> Example 5.1.2 (b)

```lean
example (n:ℕ) : Sequence.squares n = n^2
```

## Example 5.1.2 (c)

`Chapter5.Sequence.three` (abbrev, [line 88](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L88)). A definition.

> Example 5.1.2 (c)

```lean
abbrev Sequence.three : Sequence
```

## Example 5.1.2 (d)

An `example` ([line 91](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L91)). Proved here.

> Example 5.1.2 (d)

```lean
example (n:ℕ) : Sequence.three n = 3
```

## Example 5.1.2 (e)

`Chapter5.Sequence.squares_from_three` (abbrev, [line 94](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L94)). A definition.

> Example 5.1.2 (e)

```lean
abbrev Sequence.squares_from_three : Sequence
```

## Example 5.1.2 (f)

An `example` ([line 97](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L97)). Proved here.

> Example 5.1.2 (f)

```lean
example (n:ℤ) (hn: n ≥ 3) : Sequence.squares_from_three n = n^2
```

## Definition 5.1.3

`Chapter5.Rat.Steady.coe` (lemma, [line 118](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L118)). Proved here.

> Definition 5.1.3 - definition of `ε`-steadiness for a sequence starting at 0

```lean
lemma Rat.Steady.coe (ε : ℚ) (a:ℕ → ℚ) :
    ε.Steady a ↔ ∀ n m : ℕ, ε.Close (a n) (a m)
```

## Example 5.1.5

An `example` ([line 145](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L145)). Proved here.

> Example 5.1.5: The sequence `1, 0, 1, 0, ...` is 1-steady.

```lean
example : (1:ℚ).Steady ((fun n:ℕ ↦ if Even n then (1:ℚ) else (0:ℚ)):Sequence)
```

An `example` ([line 155](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L155)). Proved here.

> Example 5.1.5: The sequence `1, 0, 1, 0, ...` is not ½-steady.

```lean
example : ¬ (0.5:ℚ).Steady ((fun n:ℕ ↦ if Even n then (1:ℚ) else (0:ℚ)):Sequence)
```

An `example` ([line 163](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L163)). Proved here.

> Example 5.1.5: The sequence 0.1, 0.01, 0.001, ... is 0.1-steady.

```lean
example : (0.1:ℚ).Steady ((fun n:ℕ ↦ (10:ℚ) ^ (-(n:ℤ)-1) ):Sequence)
```

An `example` ([line 177](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L177)). Stated without proof.

> Example 5.1.5: The sequence 0.1, 0.01, 0.001, ... is not 0.01-steady. Left as an exercise.

```lean
example : ¬(0.01:ℚ).Steady ((fun n:ℕ ↦ (10:ℚ) ^ (-(n:ℤ)-1) ):Sequence)
```

An `example` ([line 181](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L181)). Stated without proof.

> Example 5.1.5: The sequence 1, 2, 4, 8, ... is not ε-steady for any ε. Left as an exercise.

```lean
example (ε:ℚ) : ¬ ε.Steady ((fun n:ℕ ↦ (2 ^ (n+1):ℚ) ):Sequence)
```

An `example` ([line 185](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L185)). Proved here.

> Example 5.1.5:The sequence 2, 2, 2, ... is ε-steady for any ε > 0.

```lean
example (ε:ℚ) (hε: ε>0) : ε.Steady ((fun _:ℕ ↦ (2:ℚ) ):Sequence)
```

## Definition 5.1.6

`Rat.EventuallySteady` (abbrev, [line 215](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L215)). A definition.

> Definition 5.1.6 (Eventually ε-steady)

```lean
abbrev Rat.EventuallySteady (ε: ℚ) (a: Chapter5.Sequence) : Prop
```

## Example 5.1.7

`Chapter5.Sequence.ex_5_1_7_a` (lemma, [line 225](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L225)). Proved here.

> Example 5.1.7: The sequence 1, 1/2, 1/3, ... is not 0.1-steady

```lean
lemma Sequence.ex_5_1_7_a : ¬ (0.1:ℚ).Steady ((fun n:ℕ ↦ (n+1:ℚ)⁻¹ ):Sequence)
```

`Chapter5.Sequence.ex_5_1_7_b` (lemma, [line 231](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L231)). Proved here.

> Example 5.1.7: The sequence `a_10, a_11, a_12, ...` is 0.1-steady

```lean
lemma Sequence.ex_5_1_7_b : (0.1:ℚ).Steady (((fun n:ℕ ↦ (n+1:ℚ)⁻¹ ):Sequence).from 10)
```

`Chapter5.Sequence.ex_5_1_7_c` (lemma, [line 250](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L250)). Proved here.

> Example 5.1.7: The sequence 1, 1/2, 1/3, ... is eventually 0.1-steady

```lean
lemma Sequence.ex_5_1_7_c : (0.1:ℚ).EventuallySteady ((fun n:ℕ ↦ (n+1:ℚ)⁻¹ ):Sequence)
```

`Chapter5.Sequence.ex_5_1_7_d` (lemma, [line 258](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L258)). Stated without proof.

> Example 5.1.7
>
> The sequence 10, 0, 0, ... is eventually ε-steady for every ε > 0. Left as an exercise.

```lean
lemma Sequence.ex_5_1_7_d {ε:ℚ} (hε:ε>0) :
    ε.EventuallySteady ((fun n:ℕ ↦ if n=0 then (10:ℚ) else (0:ℚ) ):Sequence)
```

## Example 5.1.10

`Chapter5.Sequence.ex_5_1_10_a` (theorem, [line 304](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L304)). Stated without proof.

> Example 5.1.10. (This requires extensive familiarity with Mathlib's API for the real numbers.)

```lean
theorem Sequence.ex_5_1_10_a : (1:ℚ).Steady sqrt_two
```

`Chapter5.Sequence.ex_5_1_10_b` (theorem, [line 309](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L309)). Stated without proof.

> Example 5.1.10. (This requires extensive familiarity with Mathlib's API for the real numbers.)

```lean
theorem Sequence.ex_5_1_10_b : (0.1:ℚ).Steady (sqrt_two.from 1)
```

## Proposition 5.1.11

`Chapter5.Sequence.IsCauchy.harmonic` (theorem, [line 314](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L314)). Proved here.

> Proposition 5.1.11. The harmonic sequence, defined as a₁ = 1, a₂ = 1/2, ... is a Cauchy sequence.

```lean
theorem Sequence.IsCauchy.harmonic : (mk' 1 (fun n ↦ (1:ℚ)/n)).IsCauchy
```

## Definition 5.1.12

`Chapter5.boundedBy_def` (lemma, [line 353](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L353)). Proved here.

> Definition 5.1.12 (bounded sequences). Here we start sequences from `0` rather than `1` to align
> better with Mathlib conventions.

```lean
lemma boundedBy_def {n:ℕ} (a: Fin n → ℚ) (M:ℚ) : BoundedBy a M ↔ ∀ i, |a i| ≤ M
```

`Chapter5.Sequence.boundedBy_def` (lemma, [line 358](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L358)). Proved here.

> Definition 5.1.12 (bounded sequences)

```lean
lemma Sequence.boundedBy_def (a:Sequence) (M:ℚ) : a.BoundedBy M ↔ ∀ n, |a n| ≤ M
```

`Chapter5.Sequence.isBounded_def` (lemma, [line 363](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L363)). Proved here.

> Definition 5.1.12 (bounded sequences)

```lean
lemma Sequence.isBounded_def (a:Sequence) : a.IsBounded ↔ ∃ M ≥ 0, a.BoundedBy M
```

## Example 5.1.13 (a)

An `example` ([line 366](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L366)). Proved here.

> Example 5.1.13 (a)

```lean
example : BoundedBy ![1,-2,3,-4] 4
```

## Example 5.1.13 (b)

An `example` ([line 369](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L369)). Stated without proof.

> Example 5.1.13 (b)

```lean
example : ¬((fun n:ℕ ↦ (-1)^n * (n+1:ℚ)):Sequence).IsBounded
```

## Example 5.1.13 (c)

An `example` ([line 372](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L372)). Proved here.

> Example 5.1.13 (c)

```lean
example : ((fun n:ℕ ↦ (-1:ℚ)^n):Sequence).IsBounded
```

## Example 5.1.13 (d)

An `example` ([line 376](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L376)). Proved here.

> Example 5.1.13 (d)

```lean
example : ¬((fun n:ℕ ↦ (-1:ℚ)^n):Sequence).IsCauchy
```

## Lemma 5.1.14

`Chapter5.IsBounded.finite` (lemma, [line 389](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L389)). Proved here.

> Lemma 5.1.14

```lean
lemma IsBounded.finite {n:ℕ} (a: Fin n → ℚ) : ∃ M ≥ 0,  BoundedBy a M
```

## Lemma 5.1.15 / Exercise 5.1.1

`Chapter5.Sequence.isBounded_of_isCauchy` (lemma, [line 403](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L403)). An exercise, stated without proof.

> Lemma 5.1.15 (Cauchy sequences are bounded) / Exercise 5.1.1

```lean
lemma Sequence.isBounded_of_isCauchy {a:Sequence} (h: a.IsCauchy) : a.IsBounded
```

## Exercise 5.1.2

`Chapter5.Sequence.isBounded_add` (theorem, [line 407](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean#L407)). An exercise, stated without proof.

> Exercise 5.1.2

```lean
theorem Sequence.isBounded_add {a b:ℕ → ℚ} (ha: (a:Sequence).IsBounded) (hb: (b:Sequence).IsBounded):
    (a + b:Sequence).IsBounded
```

## Depends on

- [Section 4.3: Absolute value and exponentiation](../chapter-4/section-4-3.md)

## Sources

- [Analysis/Section_5_1.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_1.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_5_1/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_5_1.html)
