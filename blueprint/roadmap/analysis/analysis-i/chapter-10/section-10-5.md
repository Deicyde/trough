---
declaration: theorem
origin: cited
lean: Filter.Tendsto.of_div, Filter.Tendsto.of_div'
statement: formalized
---

# Section 10.5: L'Hôpital's rule

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text.  When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter.  In particular, there will be places where
> the Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
> - L'Hôpital's rule.

*Quoted from [Analysis/Section_10_5.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_5.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 2 labelled items, carried by 2 declarations: 1 proved here and 1 stated without proof (1 of them exercises).

## Proposition 10.5.1 / Exercise 10.5.1

`Filter.Tendsto.of_div` (theorem, [line 24](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_5.lean#L24)). An exercise, stated without proof.

> Proposition 10.5.1 (L'Hôpital's rule, I) / Exercise 10.5.1

```lean
theorem _root_.Filter.Tendsto.of_div {X: Set ℝ} {f g: ℝ → ℝ} {x₀ f'x₀ g'x₀:ℝ}
  (hfx₀: f x₀ = 0) (hgx₀: g x₀ = 0) (hg_non: g'x₀ ≠ 0)
  (hf'x₀: HasDerivWithinAt f f'x₀ X x₀) (hg'x₀: HasDerivWithinAt g g'x₀ X x₀) :
  (∃ δ > 0, ∀ x ∈ X \ {x₀} ∩ .Ioo (x₀ - δ) (x₀ + δ), g x ≠ 0) ∧
  (nhdsWithin x₀ (X \ {x₀})).Tendsto (fun x ↦ f x / g x) (nhds (f'x₀ / g'x₀))
```

## Proposition 10.5.2

`Filter.Tendsto.of_div'` (theorem, [line 33](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_5.lean#L33)). Proved here.

> Proposition 10.5.2 (L'Hôpital's rule, II)

```lean
theorem _root_.Filter.Tendsto.of_div' {a b L:ℝ} (hab: a < b) {f g f' g': ℝ → ℝ}
  (hf: DifferentiableOn ℝ f (.Icc a b)) (hg: DifferentiableOn ℝ g (.Icc a b))
  (hf': f' = derivWithin f (.Icc a b)) (hg': g' = derivWithin g (.Icc a b))
  (hfa: f a = 0) (hga: g a = 0) (hgnon: ∀ x ∈ Set.Icc a b, g' x ≠ 0)
  (hderiv: (nhdsWithin a (.Icc a b)).Tendsto (fun x ↦ f' x / g' x) (nhds L)) :
  (∀ x ∈ Set.Ioc a b, g x ≠ 0) ∧
  (nhdsWithin a (.Ioc a b)).Tendsto (fun x ↦ f x / g x) (nhds L)
```

## Depends on

- [Section 9.1: Subsets of the real line](../chapter-9/section-9-1.md)
- [Section 10.1: Basic definitions](section-10-1.md)
- [Section 10.2: Local maxima, local minima, and derivatives](section-10-2.md)

## Sources

- [Analysis/Section_10_5.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_5.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_10_5/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_10_5.html)
