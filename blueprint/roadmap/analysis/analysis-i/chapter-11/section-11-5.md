---
declaration: theorem
origin: cited
lean: Chapter11.integ_of_uniform_cts, Chapter11.integ_of_cts, Chapter11.integ_of_bdd_cts, Chapter11.PiecewiseContinuousOn, Chapter11.f_11_5_5, Chapter11.integ_of_bdd_piecewise_cts, Chapter11.integ_zero
statement: formalized
---

# Section 11.5: Riemann integrability of continuous functions

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
> - Riemann integrability of uniformly continuous functions.
> - Riemann integrability of bounded continuous functions.

*Quoted from [Analysis/Section_11_5.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_5.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 12 labelled items, carried by 14 declarations: 2 proved here, 10 stated without proof (2 of them exercises) and 2 definitions.

## Theorem 11.5.1

`Chapter11.integ_of_uniform_cts` (theorem, [line 25](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_5.lean#L25)). Stated without proof.

> Theorem 11.5.1

```lean
theorem integ_of_uniform_cts {I: BoundedInterval} {f:ℝ → ℝ} (hf: UniformContinuousOn f I) :
  IntegrableOn f I
```

## Corollary 11.5.2

`Chapter11.integ_of_cts` (theorem, [line 83](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_5.lean#L83)). Proved here.

> Corollary 11.5.2

```lean
theorem integ_of_cts {a b:ℝ} {f:ℝ → ℝ} (hf: ContinuousOn f (Icc a b)) :
  IntegrableOn f (Icc a b)
```

An `example` ([line 87](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_5.lean#L87)). Stated without proof.

> Corollary 11.5.2 (sharpness) (a)

```lean
example : ¬ ContinuousOn (fun x:ℝ ↦ 1/x) (Icc 0 1)
```

An `example` ([line 90](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_5.lean#L90)). Stated without proof.

> Corollary 11.5.2 (sharpness) (b)

```lean
example : ¬ IntegrableOn (fun x:ℝ ↦ 1/x) (Icc 0 1)
```

## Proposition 11.5.3

`Chapter11.integ_of_bdd_cts` (theorem, [line 95](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_5.lean#L95)). Proved here.

> Proposition 11.5.3

```lean
theorem integ_of_bdd_cts {I: BoundedInterval} {f:ℝ → ℝ} (hbound: BddOn f I)
  (hf: ContinuousOn f I) : IntegrableOn f I
```

## Definition 11.5.4

`Chapter11.PiecewiseContinuousOn` (abbrev, [line 199](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_5.lean#L199)). A definition.

> Definition 11.5.4

```lean
abbrev PiecewiseContinuousOn (f:ℝ → ℝ) (I:BoundedInterval) : Prop
```

## Example 11.5.5

`Chapter11.f_11_5_5` (abbrev, [line 203](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_5.lean#L203)). A definition.

> Example 11.5.5

```lean
noncomputable abbrev f_11_5_5 : ℝ → ℝ
```

## Example 11.5.5 (a)

An `example` ([line 209](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_5.lean#L209)). Stated without proof.

> Example 11.5.5 (a)

```lean
example : ¬ ContinuousOn f_11_5_5 (Icc 1 3)
```

## Example 11.5.5 (b)

An `example` ([line 212](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_5.lean#L212)). Stated without proof.

> Example 11.5.5 (b)

```lean
example : ContinuousOn f_11_5_5 (Ico 1 2)
```

## Example 11.5.5 (c)

An `example` ([line 215](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_5.lean#L215)). Stated without proof.

> Example 11.5.5 (c)

```lean
example : ContinuousOn f_11_5_5 (Icc 2 2)
```

## Example 11.5.5 (d)

An `example` ([line 218](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_5.lean#L218)). Stated without proof.

> Example 11.5.5 (d)

```lean
example : ContinuousOn f_11_5_5 (Ioc 2 3)
```

## Example 11.5.5 (e)

An `example` ([line 221](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_5.lean#L221)). Stated without proof.

> Example 11.5.5 (e)

```lean
example : PiecewiseContinuousOn f_11_5_5 (Icc 1 3)
```

## Proposition 11.5.6 / Exercise 11.5.1

`Chapter11.integ_of_bdd_piecewise_cts` (theorem, [line 224](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_5.lean#L224)). An exercise, stated without proof.

> Proposition 11.5.6 / Exercise 11.5.1

```lean
theorem integ_of_bdd_piecewise_cts {I: BoundedInterval} {f:ℝ → ℝ}
  (hbound: BddOn f I) (hf: PiecewiseContinuousOn f I) : IntegrableOn f I
```

## Exercise 11.5.2

`Chapter11.integ_zero` (theorem, [line 229](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_5.lean#L229)). An exercise, stated without proof.

> Exercise 11.5.2

```lean
theorem integ_zero {a b:ℝ} (hab: a < b) (f: ℝ → ℝ) (hf: ContinuousOn f (Icc a b))
  (hnonneg: MajorizesOn f (fun _ ↦ 0) (Icc a b)) (hinteg : integ f (Icc a b) = 0) :
  ∀ x ∈ Icc a b, f x = 0
```

## Depends on

- [Section 9.9: Uniform continuity](../chapter-9/section-9-9.md)
- [Section 11.4: Basic properties of the Riemann integral](section-11-4.md)

## Sources

- [Analysis/Section_11_5.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_5.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_11_5/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_11_5.html)
