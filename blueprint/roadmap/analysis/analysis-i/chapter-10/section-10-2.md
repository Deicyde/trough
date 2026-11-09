---
declaration: theorem
origin: cited
lean: Chapter10.IsLocalMaxOn.iff, Chapter10.f_10_2_3, Chapter10.IsLocalMaxOn.of_restrict, Chapter10.IsLocalMaxOn.deriv_eq_zero, Chapter10.IsLocalMinOn.deriv_eq_zero, HasDerivWithinAt.exist_zero, HasDerivWithinAt.mean_value, Chapter10.lipschitz_bound, UniformContinuousOn.of_lipschitz
statement: formalized
---

# Section 10.2: Local maxima, local minima, and derivatives

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text.  When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter.  In particular, there will be places where
> the Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
> - Relation between local extrema and derivatives.
> - Rolle's theorem.
> - mean value theorem.

*Quoted from [Analysis/Section_10_2.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_2.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 12 labelled items, carried by 12 declarations: 1 proved here, 10 stated without proof (8 of them exercises) and 1 definition. It also has 3 declarations and 6 examples with no label, counted here but not shown.

## Definition 10.2.1

`Chapter10.IsLocalMaxOn.iff` (theorem, [line 23](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_2.lean#L23)). Proved here.

> Definition 10.2.1 (Local maxima and minima).  Here we use Mathlib's `IsLocalMaxOn` type.

```lean
theorem IsLocalMaxOn.iff (X:Set ℝ) (f:ℝ → ℝ) (x₀:ℝ) :
  IsLocalMaxOn f X x₀ ↔
  ∃ δ > 0, IsMaxOn f (X ∩ .Ioo (x₀ - δ) (x₀ + δ)) x₀
```

## Example 10.2.3

`Chapter10.f_10_2_3` (abbrev, [line 38](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_2.lean#L38)). A definition.

> Example 10.2.3

```lean
abbrev f_10_2_3 : ℝ → ℝ
```

## Example 10.2.4

An `example` ([line 47](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_2.lean#L47)). Stated without proof.

> Example 10.2.4

```lean
example : ¬ ∃ x, IsMaxOn (· : ℝ → ℝ)  ((↑· : ℤ → ℝ) '' .univ) x
```

## Remark 10.2.5

`Chapter10.IsLocalMaxOn.of_restrict` (theorem, [line 56](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_2.lean#L56)). Stated without proof.

> Remark 10.2.5

```lean
theorem IsLocalMaxOn.of_restrict {X Y:Set ℝ} (hXY: Y ⊆ X) (f:ℝ → ℝ) (x₀:ℝ)
  (h: IsLocalMaxOn f X x₀) : IsLocalMaxOn f Y x₀
```

## Proposition 10.2.6 (i) / Exercise 10.2.1

`Chapter10.IsLocalMaxOn.deriv_eq_zero` (theorem, [line 65](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_2.lean#L65)). An exercise, stated without proof.

> Proposition 10.2.6 (i) (Local extrema are stationary) / Exercise 10.2.1

```lean
theorem IsLocalMaxOn.deriv_eq_zero {a b:ℝ} {f:ℝ → ℝ} {x₀:ℝ}
  (hx₀: x₀ ∈ Set.Ioo a b) (h: IsLocalMaxOn f (.Ioo a b) x₀) {L:ℝ}
  (hderiv: HasDerivWithinAt f L (.Ioo a b) x₀) : L = 0
```

## Proposition 10.2.6 (ii) / Exercise 10.2.1

`Chapter10.IsLocalMinOn.deriv_eq_zero` (theorem, [line 71](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_2.lean#L71)). An exercise, stated without proof.

> Proposition 10.2.6 (ii) (Local extrema are stationary) / Exercise 10.2.1

```lean
theorem IsLocalMinOn.deriv_eq_zero {a b:ℝ} {f:ℝ → ℝ} {x₀:ℝ}
  (hx₀: x₀ ∈ Set.Ioo a b) (h: IsLocalMinOn f (.Ioo a b) x₀) {L:ℝ}
  (hderiv: HasDerivWithinAt f L (.Ioo a b) x₀) : L = 0
```

## Theorem 10.2.7 / Exercise 10.2.4

`HasDerivWithinAt.exist_zero` (theorem, [line 82](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_2.lean#L82)). An exercise, stated without proof.

> Theorem 10.2.7 (Rolle's theorem) / Exercise 10.2.4

```lean
theorem _root_.HasDerivWithinAt.exist_zero {a b:ℝ} (hab: a < b) {g:ℝ → ℝ}
  (hcont: ContinuousOn g (.Icc a b)) (hderiv: DifferentiableOn ℝ g (.Ioo a b))
  (hgab: g a = g b) : ∃ x ∈ Set.Ioo a b, HasDerivWithinAt g 0 (.Ioo a b) x
```

## Corollary 10.2.9 / Exercise 10.2.5

`HasDerivWithinAt.mean_value` (theorem, [line 88](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_2.lean#L88)). An exercise, stated without proof.

> Corollary 10.2.9 (Mean value theorem) / Exercise 10.2.5

```lean
theorem _root_.HasDerivWithinAt.mean_value {a b:ℝ} (hab: a < b) {f:ℝ → ℝ}
  (hcont: ContinuousOn f (.Icc a b)) (hderiv: DifferentiableOn ℝ f (.Ioo a b)) :
  ∃ x ∈ Set.Ioo a b, HasDerivWithinAt f ((f b - f a) / (b - a)) (.Ioo a b) x
```

## Exercise 10.2.2

An `example` ([line 94](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_2.lean#L94)). An exercise, stated without proof.

> Exercise 10.2.2

```lean
example : ∃ f:ℝ → ℝ, ContinuousOn f (.Icc (-1) 1) ∧
  IsMaxOn f (.Icc (-1) 1) 0 ∧ ¬ DifferentiableWithinAt ℝ f (.Icc (-1) 1) 0
```

## Exercise 10.2.3

An `example` ([line 99](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_2.lean#L99)). An exercise, stated without proof.

> Exercise 10.2.3

```lean
example : ∃ f:ℝ → ℝ, DifferentiableOn ℝ f (.Icc (-1) 1) ∧
  HasDerivWithinAt f 0 (.Ioo (-1) 1) 0 ∧
  ¬ IsLocalMaxOn f (.Icc (-1) 1) 0 ∧ ¬ IsLocalMinOn f (.Icc (-1) 1) 0
```

## Exercise 10.2.6

`Chapter10.lipschitz_bound` (theorem, [line 105](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_2.lean#L105)). An exercise, stated without proof.

> Exercise 10.2.6

```lean
theorem lipschitz_bound {M a b:ℝ} (hM: M > 0) (hab: a < b) {f:ℝ → ℝ}
  (hcont: ContinuousOn f (.Icc a b))
  (hderiv: DifferentiableOn ℝ f (.Ioo a b))
  (hlip: ∀ x ∈ Set.Ioo a b, |derivWithin f (.Ioo a b) x| ≤ M)
  {x y:ℝ} (hx: x ∈ Set.Icc a b) (hy: y ∈ Set.Icc a b) :
  |f x - f y| ≤ M * |x - y|
```

## Exercise 10.2.7

`UniformContinuousOn.of_lipschitz` (theorem, [line 114](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_2.lean#L114)). An exercise, stated without proof.

> Exercise 10.2.7

```lean
theorem _root_.UniformContinuousOn.of_lipschitz {f:ℝ → ℝ}
  (hcont: ContinuousOn f .univ)
  (hderiv: DifferentiableOn ℝ f .univ)
  (hlip: BddOn (deriv f) .univ) :
  UniformContinuousOn f (.univ)
```

## Depends on

- [Section 9.6: The maximum principle](../chapter-9/section-9-6.md)

## Sources

- [Analysis/Section_10_2.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_2.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_10_2/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_10_2.html)
