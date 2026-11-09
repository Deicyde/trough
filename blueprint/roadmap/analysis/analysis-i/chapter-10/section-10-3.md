---
declaration: theorem
origin: cited
lean: Chapter10.derivative_of_monotone, Chapter10.strictMono_of_positive_derivative
statement: formalized
---

# Section 10.3: Monotone functions and derivatives

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text.  When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter.  In particular, there will be places where
> the Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
> - Relations between monotonicity and differentiability.

*Quoted from [Analysis/Section_10_3.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_3.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 5 labelled items, carried by 5 declarations: 5 stated without proof (4 of them exercises). It also has 2 declarations with no label, counted here but not shown.

## Proposition 10.3.1 / Exercise 10.3.1

`Chapter10.derivative_of_monotone` (theorem, [line 20](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_3.lean#L20)). An exercise, stated without proof.

> Proposition 10.3.1 / Exercise 10.3.1

```lean
theorem derivative_of_monotone (X:Set ℝ) {x₀:ℝ} (hx₀: ClusterPt x₀ (.principal (X \ {x₀})))
  {f:ℝ → ℝ} (hmono: Monotone f) (hderiv: DifferentiableWithinAt ℝ f X x₀) :
    derivWithin f X x₀ ≥ 0
```

## Proposition 10.3.3 / Exercise 10.3.4

`Chapter10.strictMono_of_positive_derivative` (theorem, [line 31](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_3.lean#L31)). An exercise, stated without proof.

> Proposition 10.3.3 / Exercise 10.3.4

```lean
theorem strictMono_of_positive_derivative {a b:ℝ} {f:ℝ → ℝ}
  (hderiv: DifferentiableOn ℝ f (.Icc a b)) (hpos: ∀ x ∈ Set.Ioo a b, derivWithin f (.Icc a b) x > 0) :
    StrictMonoOn f (.Icc a b)
```

## Example 10.3.2

An `example` ([line 42](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_3.lean#L42)). Stated without proof.

> Example 10.3.2

```lean
example : ∃ f : ℝ → ℝ, Continuous f ∧ StrictMono f ∧ ¬ DifferentiableAt ℝ f 0
```

## Exercise 10.3.3

An `example` ([line 45](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_3.lean#L45)). An exercise, stated without proof.

> Exercise 10.3.3

```lean
example : ∃ f: ℝ → ℝ, StrictMono f ∧ Differentiable ℝ f ∧ deriv f 0 = 0
```

## Exercise 10.3.5

An `example` ([line 48](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_3.lean#L48)). An exercise, stated without proof.

> Exercise 10.3.5

```lean
example : ∃ (X : Set ℝ) (f : ℝ → ℝ), DifferentiableOn ℝ f X ∧
  (∀ x ∈ X, derivWithin f X x > 0) ∧ ¬ StrictMonoOn f X
```

## Depends on

Its Lean file imports no other section's file.

## Sources

- [Analysis/Section_10_3.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_3.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_10_3/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_10_3.html)
