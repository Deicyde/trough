---
declaration: lemma
origin: cited
lean: exercise_1_2_1_union, Ex_1_2_2b
statement: formalized
---

# Section 1.2: Lebesgue measure

> A companion to (the introduction to) Section 1.2 of the book "An introduction to Measure Theory".

*Quoted from [Analysis/MeasureTheory/Section_1_2_0.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_0.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 4 labelled items, carried by 6 declarations: 3 proved here, 2 stated without proof (1 of them exercises) and 1 definition (1 with a value left as `sorry`). It also has 11 declarations and 2 examples with no label, counted here but not shown.

## Exercise 1.2.1

`exercise_1_2_1_union` (lemma, [line 15](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_0.lean#L15)). Proved here.

> Exercise 1.2.1 (countable union)

```lean
lemma exercise_1_2_1_union :
    ∃ E: ℕ → Set ℝ, (∀ n, Bornology.IsBounded (E n)) ∧
      (∀ n, JordanMeasurable (Real.equiv_EuclideanSpace' '' (E n))) ∧
      (∀ n, E n ⊆ Set.Icc 0 1) ∧
      ¬ JordanMeasurable (⋃ n, Real.equiv_EuclideanSpace' '' (E n))
```

An `example` ([line 415](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_0.lean#L415)). Proved here.

> Exercise 1.2.1 (countable union)

```lean
example :
    ∃ E: ℕ → Set ℝ, (∀ n, Bornology.IsBounded (E n)) ∧
      (∀ n, JordanMeasurable (Real.equiv_EuclideanSpace' '' (E n)))
      ∧ ¬ JordanMeasurable (⋃ n, Real.equiv_EuclideanSpace' '' (E n))
```

An `example` ([line 423](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_0.lean#L423)). Proved here.

> Exercise 1.2.1 (countable intersection)

```lean
example :
    ∃ E: ℕ → Set ℝ, (∀ n, Bornology.IsBounded (E n)) ∧
      (∀ n, JordanMeasurable (Real.equiv_EuclideanSpace' '' (E n))) ∧
      ¬ JordanMeasurable (⋂ n, Real.equiv_EuclideanSpace' '' (E n))
```

## Exercise 1.2.2

An `example` ([line 578](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_0.lean#L578)). An exercise, stated without proof.

> Exercise 1.2.2

```lean
example : ∃ f: ℕ → ℝ → ℝ, ∃ F: ℝ → ℝ,
    (∃ M, ∀ n, ∀ x ∈ Set.Icc 0 1, |f n x| ≤ M) ∧
    (∀ x ∈ Set.Icc 0 1, Filter.atTop.Tendsto (fun n ↦ f n x) (nhds (F x))) ∧
    (∀ n, RiemannIntegrableOn (f n) (Icc 0 1)) ∧
    ¬ RiemannIntegrableOn F (Icc 0 1)
```

## Exercise 1.2.2'

`Ex_1_2_2b` (def, [line 587](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_0.lean#L587)). A definition whose value is left as `sorry`.

> Exercise 1.2.2'

```lean
def Ex_1_2_2b : Decidable ( ∀ f: ℕ → ℝ → ℝ, ∀ F: ℝ → ℝ,
    (∃ M, ∀ n, ∀ x ∈ Set.Icc 0 1, |f n x| ≤ M) →
    TendstoUniformlyOn f F Filter.atTop (Set.Icc 0 1) →
    (∀ n, RiemannIntegrableOn (f n) (Icc 0 1)) → RiemannIntegrableOn F (Icc 0 1) )
```

## Example 1.2.1

An `example` ([line 1487](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_0.lean#L1487)). Stated without proof.

> Example 1.2.1.  With the junk value conventions of this companion, the Jordan outer measure of the rationals is zero rather than infinite (I think).

```lean
example {R:ℝ} (hR: 0 < R) : Jordan_outer_measure (Real.equiv_EuclideanSpace' '' (Set.Icc (-R) R ∩ Set.range (fun q:ℚ ↦ (q:ℝ)))) = 2*R
```

## Depends on

- [Section 1.1.3: Connections with the Riemann integral](../section-1-1/section-1-1-3.md)

## Sources

- [Analysis/MeasureTheory/Section_1_2_0.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Section_1_2_0.lean)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/MeasureTheory/Section_1_2_0.html)
