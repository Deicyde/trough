---
declaration: abbrev
origin: cited
lean: Chapter11.α_length, Chapter11.α_len_of_id, Chapter11.Partition.sum_of_α_length, Chapter11.PiecewiseConstantWith.RS_integ, Chapter11.f_11_8_6, Chapter11.PiecewiseConstantWith.RS_integ_eq_integ, Chapter11.PiecewiseConstantOn.RS_integ_sub, Chapter11.PiecewiseConstantOn.RS_integ_of_nonneg, Chapter11.PiecewiseConstantOn.RS_integ_mono, Chapter11.PiecewiseConstantOn.RS_integ_const, Chapter11.PiecewiseConstantOn.RS_integ_const', Chapter11.PiecewiseConstantOn.RS_of_extend, Chapter11.PiecewiseConstantOn.RS_integ_of_extend, Chapter11.PiecewiseConstantOn.RS_integ_of_join, Chapter11.RS_integ_of_uniform_cts, Chapter11.RS_integ_with_sign
statement: formalized
---

# Section 11.8: The Riemann-Stieltjes integral

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
> - Definition of `α_length`.
> - The piecewise constant Riemann-Stieltjes integral.
> - The full Riemann-Stieltjes integral.
>
> {open Set}
>
> Technical notes:
> - In Lean it is more convenient to make definitions such as `α_length` and the Riemann-Stieltjes
>   integral totally defined, thus assigning "junk" values to the cases where the definition is
>   not intended to be applied. For the definition of `α_length`, the definition is intended to be
>   applied in contexts where left and right limits exist, and the function is extended by
>   constants to the left and right of its intended domain of definition; for instance, if a
>   function `x` `f` is defined on `Icc 0 1`, then it is intended that `f x = f 1` for all `x ≥ 1`
>   and `f x = f 0` for all `x ≤ 0`; in particular, at a right endpoint, the value of a function
>   is intended to agree with its right limit, and similarly for the left endpoint, although we
>   do not enforce this in our definition of `α_length`. (For functions defined on open intervals,
>   the extension is immaterial.)
> - The notion of `α_length` and piecewise constant Riemann-Stieltjes integral is intended for
>   situations where left and right limits exist, such as for monotone functions or continuous
>   functions, though technically they make sense without these hypotheses. The full Riemann-Stieltjes
>   integral is intended for functions that are of bounded variation, though we shall restrict
>   attention to the special case of monotone increasing functions for the most part.

*Quoted from [Analysis/Section_11_8.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_8.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 17 labelled items, carried by 17 declarations: 14 stated without proof (11 of them exercises) and 3 definitions. It also has 57 declarations and 2 examples with no label, counted here but not shown.

## Definition 11.8.1

`Chapter11.α_length` (abbrev, [line 153](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_8.lean#L153)). A definition.

> Definition 11.8.1

```lean
noncomputable abbrev α_length (α: ℝ → ℝ) (I: BoundedInterval) : ℝ
```

## Example 11.8.2

An `example` ([line 195](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_8.lean#L195)). Stated without proof.

> Example 11.8.2

```lean
example : (fun x ↦ x^2)[Icc 2 3]ₗ = 5
```

## Example 11.8.3

`Chapter11.α_len_of_id` (theorem, [line 206](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_8.lean#L206)). Stated without proof.

> Example 11.8.3

```lean
theorem α_len_of_id (I: BoundedInterval) : (fun x ↦ x)[I]ₗ = |I|ₗ
```

## Theorem 11.8.4 / Exercise 11.8.1

`Chapter11.Partition.sum_of_α_length` (theorem, [line 238](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_8.lean#L238)). An exercise, stated without proof.

> Theorem 11.8.4 / Exercise 11.8.1

```lean
theorem Partition.sum_of_α_length  {I: BoundedInterval} (P: Partition I) (α: ℝ → ℝ) :
  ∑ J ∈ P.intervals, α[J]ₗ = α[I]ₗ
```

## Definition 11.8.5

`Chapter11.PiecewiseConstantWith.RS_integ` (abbrev, [line 243](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_8.lean#L243)). A definition.

> Definition 11.8.5 (Piecewise constant RS integral).

```lean
noncomputable abbrev PiecewiseConstantWith.RS_integ (f:ℝ → ℝ) {I: BoundedInterval} (P: Partition I) (α: ℝ → ℝ)   :
  ℝ
```

## Example 11.8.6

`Chapter11.f_11_8_6` (abbrev, [line 247](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_8.lean#L247)). A definition.

> Example 11.8.6

```lean
noncomputable abbrev f_11_8_6 (x:ℝ) : ℝ
```

## Example 11.8.7

`Chapter11.PiecewiseConstantWith.RS_integ_eq_integ` (theorem, [line 257](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_8.lean#L257)). Stated without proof.

> Example 11.8.7

```lean
theorem PiecewiseConstantWith.RS_integ_eq_integ {f:ℝ → ℝ} {I: BoundedInterval} (P: Partition I) :RS_integ f P (fun x ↦ x) = integ f P
```

## Theorem 11.8.8 (c) / Exercise 11.8.3

`Chapter11.PiecewiseConstantOn.RS_integ_sub` (theorem, [line 293](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_8.lean#L293)). An exercise, stated without proof.

> Theorem 11.8.8 (c) (Laws of RS integration) / Exercise 11.8.3

```lean
theorem PiecewiseConstantOn.RS_integ_sub {f g: ℝ → ℝ} {I: BoundedInterval}
  {α:ℝ → ℝ} (hα: Monotone α)
  (hf: PiecewiseConstantOn f I) (hg: PiecewiseConstantOn g I) :
  RS_integ (f - g) I α = RS_integ f I α - RS_integ g I α
```

## Theorem 11.8.8 (d) / Exercise 11.8.3

`Chapter11.PiecewiseConstantOn.RS_integ_of_nonneg` (theorem, [line 300](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_8.lean#L300)). An exercise, stated without proof.

> Theorem 11.8.8 (d) (Laws of RS integration) / Exercise 11.8.3

```lean
theorem PiecewiseConstantOn.RS_integ_of_nonneg {f: ℝ → ℝ} {I: BoundedInterval}
  {α:ℝ → ℝ} (hα: Monotone α)
  (h: ∀ x ∈ I, 0 ≤ f x) (hf: PiecewiseConstantOn f I) :
  0 ≤ RS_integ f I α
```

## Theorem 11.8.8 (e) / Exercise 11.8.3

`Chapter11.PiecewiseConstantOn.RS_integ_mono` (theorem, [line 307](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_8.lean#L307)). An exercise, stated without proof.

> Theorem 11.8.8 (e) (Laws of RS integration) / Exercise 11.8.3

```lean
theorem PiecewiseConstantOn.RS_integ_mono {f g: ℝ → ℝ} {I: BoundedInterval}
  {α:ℝ → ℝ} (hα: Monotone α)
  (h: ∀ x ∈ I, f x ≤ g x) (hf: PiecewiseConstantOn f I) (hg: PiecewiseConstantOn g I) :
  RS_integ f I α ≤ RS_integ g I α
```

## Theorem 11.8.8 (f) / Exercise 11.8.3

`Chapter11.PiecewiseConstantOn.RS_integ_const` (theorem, [line 314](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_8.lean#L314)). An exercise, stated without proof.

> Theorem 11.8.8 (f) (Laws of RS integration) / Exercise 11.8.3

```lean
theorem PiecewiseConstantOn.RS_integ_const (c: ℝ) (I: BoundedInterval) {α:ℝ → ℝ} (hα: Monotone α) :
  RS_integ (fun _ ↦ c) I α = c * α[I]ₗ
```

## Theorem 11.8.8 (f') / Exercise 11.8.3

`Chapter11.PiecewiseConstantOn.RS_integ_const'` (theorem, [line 319](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_8.lean#L319)). An exercise, stated without proof.

> Theorem 11.8.8 (f') (Laws of RS integration) / Exercise 11.8.3

```lean
theorem PiecewiseConstantOn.RS_integ_const' {f:ℝ → ℝ} {I: BoundedInterval}
  {α:ℝ → ℝ} (hα: Monotone α) (h: ConstantOn f I) :
  RS_integ f I α = (constant_value_on f I) * α[I]ₗ
```

## Theorem 11.8.8 (g) / Exercise 11.8.3

`Chapter11.PiecewiseConstantOn.RS_of_extend` (theorem, [line 326](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_8.lean#L326)). An exercise, stated without proof.

> Theorem 11.8.8 (g) (Laws of RS integration) / Exercise 11.8.3

```lean
theorem PiecewiseConstantOn.RS_of_extend {I J: BoundedInterval} (hIJ: I ⊆ J)
  {f: ℝ → ℝ} (h: PiecewiseConstantOn f I) {α:ℝ → ℝ} (hα: Monotone α):
  PiecewiseConstantOn (fun x ↦ if x ∈ I then f x else 0) J
```

## Theorem 11.8.8 (g') / Exercise 11.8.3

`Chapter11.PiecewiseConstantOn.RS_integ_of_extend` (theorem, [line 333](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_8.lean#L333)). An exercise, stated without proof.

> Theorem 11.8.8 (g') (Laws of RS integration) / Exercise 11.8.3

```lean
theorem PiecewiseConstantOn.RS_integ_of_extend {I J: BoundedInterval} (hIJ: I ⊆ J)
  {f: ℝ → ℝ} (h: PiecewiseConstantOn f I) {α:ℝ → ℝ} (hα: Monotone α):
  RS_integ (fun x ↦ if x ∈ I then f x else 0) J α = RS_integ f I α
```

## Theorem 11.8.8 (h) / Exercise 11.8.3

`Chapter11.PiecewiseConstantOn.RS_integ_of_join` (theorem, [line 339](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_8.lean#L339)). An exercise, stated without proof.

> Theorem 11.8.8 (h) (Laws of RS integration) / Exercise 11.8.3

```lean
theorem PiecewiseConstantOn.RS_integ_of_join {I J K: BoundedInterval} (hIJK: K.joins' I J)
  {f: ℝ → ℝ} (h: PiecewiseConstantOn f K) {α:ℝ → ℝ} (hα: Monotone α):
  RS_integ f K α = RS_integ f I α + RS_integ f J α
```

## Exercise 11.8.4

`Chapter11.RS_integ_of_uniform_cts` (theorem, [line 465](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_8.lean#L465)). An exercise, stated without proof.

> Exercise 11.8.4

```lean
theorem RS_integ_of_uniform_cts {I: BoundedInterval} {f:ℝ → ℝ} (hf: UniformContinuousOn f I)
 {α:ℝ → ℝ} (hα: Monotone α):
  RS_IntegrableOn f I α
```

## Exercise 11.8.5

`Chapter11.RS_integ_with_sign` (theorem, [line 471](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_8.lean#L471)). An exercise, stated without proof.

> Exercise 11.8.5

```lean
theorem RS_integ_with_sign (f:ℝ → ℝ) (hf: ContinuousOn f (.Icc (-1) 1)) : RS_IntegrableOn f (Icc (-1) 1) Real.sign ∧ RS_integ f (Icc (-1) 1) Real.sign = 2 * f 0
```

## Depends on

- [Section 11.6: Riemann integrability of monotone functions](section-11-6.md)

## Sources

- [Analysis/Section_11_8.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_8.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_11_8/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_11_8.html)
