---
declaration: theorem
origin: cited
lean: HasDerivWithinAt.iff, Chapter10.f_10_1_6, HasDerivWithinAt.iff_approx_linear, ContinuousWithinAt.of_differentiableWithinAt, ContinuousOn.of_differentiableOn, HasDerivWithinAt.of_const, HasDerivWithinAt.of_id, HasDerivWithinAt.of_add, HasDerivWithinAt.of_mul, HasDerivWithinAt.of_smul, HasDerivWithinAt.of_sub, HasDerivWithinAt.of_inv, HasDerivWithinAt.of_div, HasDerivWithinAt.of_comp, HasDerivWithinAt.of_pow, HasDerivWithinAt.of_zpow
statement: formalized
---

# Section 10.1: Basic definitions

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text.  When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter.  In particular, there will be places where
> the Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
> - API for Mathlib's `HasDerivWithinAt`, `derivWithin`, and `DifferentiableWithinAt`.
>
> Note that the Mathlib conventions differ slightly from that in the text, in that
> differentiability is defined even at points that are not limit points of the domain;
> derivatives in such cases may not be unique, but `derivWithin` still selects one such
> derivative in such cases (or `0`, if no derivative exists).

*Quoted from [Analysis/Section_10_1.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_1.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 18 labelled items, carried by 18 declarations: 3 proved here, 14 stated without proof (13 of them exercises) and 1 definition. It also has 4 declarations and 13 examples with no label, counted here but not shown.

## Definition 10.1.1

`HasDerivWithinAt.iff` (theorem, [line 28](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_1.lean#L28)). Proved here.

> Definition 10.1.1 (Differentiability at a point).  For the Mathlib notion `HasDerivWithinAt`, the
> hypothesis that `x₀` is a limit point is not needed.

```lean
theorem _root_.HasDerivWithinAt.iff (X: Set ℝ) (x₀ : ℝ) (f: ℝ → ℝ)
  (L:ℝ) :
  HasDerivWithinAt f L X x₀ ↔ (nhdsWithin x₀ (X \ {x₀})).Tendsto (fun x ↦ (f x - f x₀) / (x - x₀))
   (nhds L)
```

## Example 10.1.3

An `example` ([line 64](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_1.lean#L64)). Stated without proof.

> Example 10.1.3

```lean
example (x₀:ℝ) : HasDerivWithinAt (fun x ↦ x^2) (2 * x₀) .univ x₀
```

## Remark 10.1.4

An `example` ([line 74](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_1.lean#L74)). Proved here.

> Remark 10.1.4

```lean
example (X: Set ℝ) (x₀ : ℝ) {f g: ℝ → ℝ} (hfg: f = g):
  DifferentiableWithinAt ℝ f X x₀ ↔ DifferentiableWithinAt ℝ g X x₀
```

## Example 10.1.6

`Chapter10.f_10_1_6` (abbrev, [line 87](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_1.lean#L87)). A definition.

> Example 10.1.6

```lean
abbrev f_10_1_6 : ℝ → ℝ
```

## Proposition 10.1.7 / Exercise 10.1.2

`HasDerivWithinAt.iff_approx_linear` (theorem, [line 114](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_1.lean#L114)). An exercise, stated without proof.

> Proposition 10.1.7 (Newton's approximation) / Exercise 10.1.2

```lean
theorem _root_.HasDerivWithinAt.iff_approx_linear (X: Set ℝ) (x₀ :ℝ) (f: ℝ → ℝ) (L:ℝ) :
  HasDerivWithinAt f L X x₀ ↔
  ∀ ε > 0, ∃ δ > 0, ∀ x ∈ X, |x - x₀| < δ → |f x - f x₀ - L * (x - x₀)| ≤ ε * |x - x₀|
```

## Proposition 10.1.10 / Exercise 10.1.3

`ContinuousWithinAt.of_differentiableWithinAt` (theorem, [line 120](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_1.lean#L120)). An exercise, stated without proof.

> Proposition 10.1.10 / Exercise 10.1.3

```lean
theorem _root_.ContinuousWithinAt.of_differentiableWithinAt {X: Set ℝ} {x₀ : ℝ} {f: ℝ → ℝ}
  (h: DifferentiableWithinAt ℝ f X x₀) :
  ContinuousWithinAt f X x₀
```

## Corollary 10.1.12

`ContinuousOn.of_differentiableOn` (theorem, [line 129](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_1.lean#L129)). Proved here.

> Corollary 10.1.12

```lean
theorem _root_.ContinuousOn.of_differentiableOn {X: Set ℝ} {f: ℝ → ℝ}
  (h: DifferentiableOn ℝ f X) :
  ContinuousOn f X
```

## Theorem 10.1.13 (a) / Exercise 10.1.4

`HasDerivWithinAt.of_const` (theorem, [line 135](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_1.lean#L135)). An exercise, stated without proof.

> Theorem 10.1.13 (a) (Differential calculus) / Exercise 10.1.4

```lean
theorem _root_.HasDerivWithinAt.of_const (X: Set ℝ) (x₀ : ℝ) (c:ℝ) :
  HasDerivWithinAt (fun x ↦ c) 0 X x₀
```

## Theorem 10.1.13 (b) / Exercise 10.1.4

`HasDerivWithinAt.of_id` (theorem, [line 139](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_1.lean#L139)). An exercise, stated without proof.

> Theorem 10.1.13 (b) (Differential calculus) / Exercise 10.1.4

```lean
theorem _root_.HasDerivWithinAt.of_id (X: Set ℝ) (x₀ : ℝ) :
  HasDerivWithinAt (fun x ↦ x) 1 X x₀
```

## Theorem 10.1.13 (c) / Exercise 10.1.4

`HasDerivWithinAt.of_add` (theorem, [line 143](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_1.lean#L143)). An exercise, stated without proof.

> Theorem 10.1.13 (c) (Sum rule) / Exercise 10.1.4

```lean
theorem _root_.HasDerivWithinAt.of_add {X: Set ℝ} {x₀ f'x₀ g'x₀: ℝ}
  {f g: ℝ → ℝ} (hf: HasDerivWithinAt f f'x₀ X x₀) (hg: HasDerivWithinAt g g'x₀ X x₀) :
  HasDerivWithinAt (f + g) (f'x₀ + g'x₀) X x₀
```

## Theorem 10.1.13 (d) / Exercise 10.1.4

`HasDerivWithinAt.of_mul` (theorem, [line 149](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_1.lean#L149)). An exercise, stated without proof.

> Theorem 10.1.13 (d) (Product rule) / Exercise 10.1.4

```lean
theorem _root_.HasDerivWithinAt.of_mul {X: Set ℝ} {x₀ f'x₀ g'x₀: ℝ}
  {f g: ℝ → ℝ} (hf: HasDerivWithinAt f f'x₀ X x₀) (hg: HasDerivWithinAt g g'x₀ X x₀) :
  HasDerivWithinAt (f * g) (f'x₀ * (g x₀) + (f x₀) * g'x₀) X x₀
```

## Theorem 10.1.13 (e) / Exercise 10.1.4

`HasDerivWithinAt.of_smul` (theorem, [line 155](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_1.lean#L155)). An exercise, stated without proof.

> Theorem 10.1.13 (e) (Differential calculus) / Exercise 10.1.4

```lean
theorem _root_.HasDerivWithinAt.of_smul {X: Set ℝ} {x₀ f'x₀: ℝ} (c:ℝ)
  {f: ℝ → ℝ} (hf: HasDerivWithinAt f f'x₀ X x₀) :
  HasDerivWithinAt (c • f) (c * f'x₀) X x₀
```

## Theorem 10.1.13 (f) / Exercise 10.1.4

`HasDerivWithinAt.of_sub` (theorem, [line 161](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_1.lean#L161)). An exercise, stated without proof.

> Theorem 10.1.13 (f) (Difference rule) / Exercise 10.1.4

```lean
theorem _root_.HasDerivWithinAt.of_sub {X: Set ℝ} {x₀ f'x₀ g'x₀: ℝ}
  {f g: ℝ → ℝ} (hf: HasDerivWithinAt f f'x₀ X x₀) (hg: HasDerivWithinAt g g'x₀ X x₀) :
  HasDerivWithinAt (f - g) (f'x₀ - g'x₀) X x₀
```

## Theorem 10.1.13 (g) / Exercise 10.1.4

`HasDerivWithinAt.of_inv` (theorem, [line 167](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_1.lean#L167)). An exercise, stated without proof.

> Theorem 10.1.13 (g) (Differential calculus) / Exercise 10.1.4

```lean
theorem _root_.HasDerivWithinAt.of_inv {X: Set ℝ} {x₀ g'x₀: ℝ}
  {g: ℝ → ℝ} (hgx₀ : g x₀ ≠ 0) (hg: HasDerivWithinAt g g'x₀ X x₀) :
  HasDerivWithinAt (1/g) (-g'x₀ / (g x₀)^2) X x₀
```

## Theorem 10.1.13 (h) / Exercise 10.1.4

`HasDerivWithinAt.of_div` (theorem, [line 173](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_1.lean#L173)). An exercise, stated without proof.

> Theorem 10.1.13 (h) (Quotient rule) / Exercise 10.1.4

```lean
theorem _root_.HasDerivWithinAt.of_div {X: Set ℝ} {x₀ f'x₀ g'x₀: ℝ}
  {f g: ℝ → ℝ} (hgx₀ : g x₀ ≠ 0) (hf: HasDerivWithinAt f f'x₀ X x₀)
  (hg: HasDerivWithinAt g g'x₀ X x₀) :
  HasDerivWithinAt (f / g) ((f'x₀ * (g x₀) - (f x₀) * g'x₀) / (g x₀)^2) X x₀
```

## Theorem 10.1.15 / Exercise 10.1.7

`HasDerivWithinAt.of_comp` (theorem, [line 183](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_1.lean#L183)). An exercise, stated without proof.

> Theorem 10.1.15 (Chain rule) / Exercise 10.1.7

```lean
theorem _root_.HasDerivWithinAt.of_comp {X Y: Set ℝ} {x₀ y₀ f'x₀ g'y₀: ℝ}
  {f g: ℝ → ℝ} (hfx₀: f x₀ = y₀) (hfX : ∀ x ∈ X, f x ∈ Y)
  (hf: HasDerivWithinAt f f'x₀ X x₀) (hg: HasDerivWithinAt g g'y₀ Y y₀) :
  HasDerivWithinAt (g ∘ f) (g'y₀ * f'x₀) X x₀
```

## Exercise 10.1.5

`HasDerivWithinAt.of_pow` (theorem, [line 190](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_1.lean#L190)). An exercise, stated without proof.

> Exercise 10.1.5

```lean
theorem _root_.HasDerivWithinAt.of_pow (n:ℕ) (x₀:ℝ) : HasDerivWithinAt (fun x ↦ x^n)
(n * x₀^((n:ℤ)-1)) .univ x₀
```

## Exercise 10.1.6

`HasDerivWithinAt.of_zpow` (theorem, [line 195](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_1.lean#L195)). An exercise, stated without proof.

> Exercise 10.1.6

```lean
theorem _root_.HasDerivWithinAt.of_zpow (n:ℤ) (x₀:ℝ) (hx₀: x₀ ≠ 0) :
  HasDerivWithinAt (fun x ↦ x^n) (n * x₀^(n-1)) (.univ \ {0}) x₀
```

## Depends on

Its Lean file imports no other section's file.

## Sources

- [Analysis/Section_10_1.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_1.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_10_1/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_10_1.html)
