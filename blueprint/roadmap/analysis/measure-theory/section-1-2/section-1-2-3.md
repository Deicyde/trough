---
declaration: theorem
origin: cited
lean: LebesgueMeasurable.nonmeasurable
statement: formalized
---

# Section 1.2.3: Non-measurable sets

> A companion to (the introduction to) Section 1.2.3 of the book "An introduction to Measure Theory".

*Quoted from [Analysis/MeasureTheory/Section_1_2_3.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_3.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 3 labelled items, carried by 3 declarations: 1 proved here and 2 stated without proof (2 of them exercises). It also has 9 declarations with no label, counted here but not shown.

## Proposition 1.2.18

`LebesgueMeasurable.nonmeasurable` (theorem, [line 347](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_3.lean#L347)). Proved here.

> Proposition 1.2.18

```lean
theorem LebesgueMeasurable.nonmeasurable : ∃ E : Set (EuclideanSpace' 1), E ⊆ Real.equiv_EuclideanSpace' '' (Set.Icc 0 1) ∧ ¬ LebesgueMeasurable E
```

## Exercise 1.2.26

An `example` ([line 357](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_3.lean#L357)). An exercise, stated without proof.

> Exercise 1.2.26 (Outer measure is not finitely additive).

```lean
example : ∃ E F : Set (EuclideanSpace' 1), E ∩ F = ∅ ∧ Bornology.IsBounded E ∧ Bornology.IsBounded F ∧ Lebesgue_outer_measure (E ∪ F) ≠ Lebesgue_outer_measure E + Lebesgue_outer_measure F
```

## Exercise 1.2.27

An `example` ([line 361](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_3.lean#L361)). An exercise, stated without proof.

> Exercise 1.2.27 (Projections of measurable sets need not be measurable)

```lean
example : ∃ E : Set (EuclideanSpace' 2), LebesgueMeasurable E ∧ ¬ LebesgueMeasurable ((fun x ↦ Real.equiv_EuclideanSpace' (x 0: ℝ)) '' E)
```

## Depends on

- [Section 1.2.2: Lebesgue measurability](section-1-2-2.md)

## Sources

- [Analysis/MeasureTheory/Section_1_2_3.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_3.lean)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/MeasureTheory/Section_1_2_3.html)
