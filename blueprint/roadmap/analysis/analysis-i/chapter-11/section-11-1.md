---
declaration: theorem
origin: cited
lean: Chapter11.Bornology.IsBounded.of_boundedInterval, Chapter11.BoundedInterval.inter, Chapter11.Partition.exist_right, Chapter11.Partition.sum_of_length, Chapter11.Partition.instLE, Chapter11.Partition.instMax, Chapter11.BoundedInterval.le_max
statement: formalized
---

# Section 11.1: Partitions

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Bounded intervals and partitions.
> - Length of an interval; the lengths of a partition sum to the length of the interval.

*Quoted from [Analysis/Section_11_1.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_1.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 10 labelled items, carried by 10 declarations: 8 stated without proof (4 of them exercises) and 2 definitions. It also has 50 declarations and 13 examples with no label, counted here but not shown.

## Examples 11.1.3

An `example` ([line 67](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_1.lean#L67)). Stated without proof.

> Examples 11.1.3

```lean
example : (Set.Icc 1 2 : Set ℝ).OrdConnected
```

## Lemma 11.1.4 / Exercise 11.1.1

`Chapter11.Bornology.IsBounded.of_boundedInterval` (theorem, [line 78](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_1.lean#L78)). An exercise, stated without proof.

> Lemma 11.1.4 / Exercise 11.1.1

```lean
theorem Bornology.IsBounded.of_boundedInterval (I: BoundedInterval) : Bornology.IsBounded (I:Set ℝ)
```

## Corollary 11.1.6 / Exercise 11.1.2

`Chapter11.BoundedInterval.inter` (theorem, [line 85](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_1.lean#L85)). An exercise, stated without proof.

> Corollary 11.1.6 / Exercise 11.1.2

```lean
theorem BoundedInterval.inter (I J: BoundedInterval) : ∃ K : BoundedInterval, (I:Set ℝ) ∩ (J:Set ℝ) = (K:Set ℝ)
```

## Exercise 11.1.3

`Chapter11.Partition.exist_right` (theorem, [line 303](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_1.lean#L303)). An exercise, stated without proof.

> Exercise 11.1.3.  The exercise only claims c ≤ b, but the stronger claim c < b is true and useful.

```lean
theorem Partition.exist_right {I: BoundedInterval} (hI: I.a < I.b) (hI': I.b ∉ I)
  {P: Partition I}
  : ∃ c ∈ Set.Ico I.a I.b, Ioo c I.b ∈ P ∨ Ico c I.b ∈ P
```

## Theorem 11.1.13

`Chapter11.Partition.sum_of_length` (theorem, [line 309](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_1.lean#L309)). Stated without proof.

> Theorem 11.1.13 (Length is finitely additive).

```lean
theorem Partition.sum_of_length  (I: BoundedInterval) (P: Partition I) :
  ∑ J ∈ P.intervals, |J|ₗ = |I|ₗ
```

## Definition 11.1.14

`Chapter11.Partition.instLE` (instance, [line 393](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_1.lean#L393)). A definition.

> Definition 11.1.14 (Finer and coarser partitions)

```lean
instance Partition.instLE (I: BoundedInterval) : LE (Partition I)
```

## Example 11.1.15

An `example` ([line 407](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_1.lean#L407)). Stated without proof.

> Example 11.1.15

```lean
example : ∃ P P' : Partition (Icc 1 4),
  P.intervals = {Ico 1 2, Icc 2 2, Ioo 2 3,
                 Icc 3 4} ∧
  P'.intervals = {Icc 1 2, Ioc 2 4} ∧
  P' ≤ P
```

## Definition 11.1.16

`Chapter11.Partition.instMax` (instance, [line 415](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_1.lean#L415)). A definition.

> Definition 11.1.16 (Common refinement).

```lean
noncomputable instance Partition.instMax (I: BoundedInterval) : Max (Partition I)
```

## Example 11.1.17

An `example` ([line 433](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_1.lean#L433)). Stated without proof.

> Example 11.1.17.

```lean
example : ∃ P P' : Partition (Icc 1 4),
    P.intervals = {Ico 1 3, Icc 3 4} ∧
    P'.intervals = {Icc 1 2, Ioc 2 4} ∧
    (P' ⊔ P).intervals.image toSet =
      {Set.Icc 1 2, Set.Ioo 2 3, Set.Icc 3 4, ∅}
```

## Lemma 11.1.8 / Exercise 11.1.4

`Chapter11.BoundedInterval.le_max` (theorem, [line 441](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_1.lean#L441)). An exercise, stated without proof.

> Lemma 11.1.8 / Exercise 11.1.4

```lean
theorem BoundedInterval.le_max {I: BoundedInterval} (P P': Partition I) :
  P ≤ P ⊔ P' ∧ P' ≤ P ⊔ P'
```

## Depends on

Its Lean file imports no other section's file.

## Sources

- [Analysis/Section_11_1.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_1.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_11_1/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_11_1.html)
