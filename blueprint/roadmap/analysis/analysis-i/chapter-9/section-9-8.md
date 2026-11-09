---
declaration: theorem
origin: cited
lean: Chapter9.MonotoneOn.iff, Chapter9.MonotoneOn.exist_inverse, Chapter9.IsMaxOn.of_monotone_on_compact, Chapter9.no_strictmono_intermediate_value, Chapter9.mono_of_continuous_inj, Chapter9.MonotoneOn.exist_inverse_without_continuity, Chapter9.MonotoneOn.exist_inverse_without_strictmono, Chapter9.StrictMonoOn.of_f_9_8_5, Chapter9.ContinuousAt.of_f_9_8_5', Chapter9.ContinuousAt.of_f_9_8_5
statement: formalized
---

# Section 9.8: Monotonic functions

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text.  When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter.  In particular, there will be places where
> the Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
> - Review of Mathlib monotonicity concepts.

*Quoted from [Analysis/Section_9_8.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_8.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 11 labelled items, carried by 12 declarations: 2 proved here, 8 stated without proof (7 of them exercises) and 2 definitions (2 with a value left as `sorry`). It also has 14 declarations and 10 examples with no label, counted here but not shown.

## Definition 9.8.1

`Chapter9.MonotoneOn.iff` (theorem, [line 20](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_8.lean#L20)). Proved here.

> Definition 9.8.1

```lean
theorem MonotoneOn.iff {X: Set ℝ} (f: ℝ → ℝ) : MonotoneOn f X  ↔ ∀ x ∈ X, ∀ y ∈ X, y > x → f y ≥ f x
```

## Examples 9.8.2

An `example` ([line 41](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_8.lean#L41)). Stated without proof.

> Examples 9.8.2

```lean
example : StrictMonoOn (fun x:ℝ ↦ x^2) (.Ici 0)
```

## Proposition 9.8.3 / Exercise 9.8.4

`Chapter9.MonotoneOn.exist_inverse` (theorem, [line 66](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_8.lean#L66)). An exercise, stated without proof.

> Proposition 9.8.3 / Exercise 9.8.4

```lean
theorem MonotoneOn.exist_inverse {a b:ℝ} (h: a < b) (f: ℝ → ℝ) (hcont: ContinuousOn f (.Icc a b)) (hmono: StrictMonoOn f (.Icc a b)) :
  f '' (.Icc a b) = .Icc (f a) (f b) ∧
  ∃ finv: ℝ → ℝ, ContinuousOn finv (.Icc (f a) (f b)) ∧ StrictMonoOn finv (.Icc (f a) (f b)) ∧
  finv '' (.Icc (f a) (f b)) = .Icc a b ∧
  (∀ x ∈ Set.Icc a b, finv (f x) = x) ∧
  ∀ y ∈ Set.Icc (f a) (f b), f (finv y) = y
```

## Example 9.8.4

An `example` ([line 76](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_8.lean#L76)). Proved here.

> Example 9.8.4

```lean
example {R :ℝ} (hR: R > 0) {n:ℕ} (hn: n > 0) : ∃ g : ℝ → ℝ, ∀ x ∈ Set.Icc 0 (R^n), (g x)^n = x
```

## Exercise 9.8.1

`Chapter9.IsMaxOn.of_monotone_on_compact` (theorem, [line 86](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_8.lean#L86)). An exercise, stated without proof.

> Exercise 9.8.1

```lean
theorem IsMaxOn.of_monotone_on_compact {a b:ℝ} (h:a < b) {f:ℝ → ℝ} (hf: MonotoneOn f (.Icc a b)) :
  ∃ xmax ∈ Set.Icc a b, IsMaxOn f (.Icc a b) xmax
```

## Exercise 9.8.2

`Chapter9.no_strictmono_intermediate_value` (theorem, [line 110](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_8.lean#L110)). An exercise, stated without proof.

> Exercise 9.8.2

```lean
theorem no_strictmono_intermediate_value :
    ∃ (a b:ℝ) (hab: a < b) (f:ℝ → ℝ) (hf: StrictMonoOn f (.Icc a b)),
      ∃ y, (y ∈ Set.Icc (f a) (f b) ∨ y ∈ Set.Icc (f b) (f a)) ∧
      ¬ ∃ c ∈ Set.Icc a b, f c = y
```

## Exercise 9.8.3

`Chapter9.mono_of_continuous_inj` (theorem, [line 131](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_8.lean#L131)). An exercise, stated without proof.

> Exercise 9.8.3

```lean
theorem mono_of_continuous_inj {a b:ℝ} (h: a < b) {f:ℝ → ℝ}
  (hf: ContinuousOn f (.Icc a b))
  (hinj: Function.Injective (fun x: Set.Icc a b ↦ f x )) :
  StrictMonoOn f (.Icc a b) ∨ StrictAntiOn f (.Icc a b)
```

## Exercise 9.8.4

`Chapter9.MonotoneOn.exist_inverse_without_continuity` (def, [line 138](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_8.lean#L138)). A definition whose value is left as `sorry`.

> Exercise 9.8.4 (without continuity)

```lean
def MonotoneOn.exist_inverse_without_continuity :
    Decidable (∀ (a b : ℝ) (_ : a < b) (f : ℝ → ℝ) (_ : StrictMonoOn f (.Icc a b)),
      f '' (.Icc a b) = .Icc (f a) (f b) ∧
      ∃ finv : ℝ → ℝ, ContinuousOn finv (.Icc (f a) (f b)) ∧ StrictMonoOn finv (.Icc (f a) (f b)) ∧
        finv '' (.Icc (f a) (f b)) = .Icc a b ∧
        (∀ x ∈ Set.Icc a b, finv (f x) = x) ∧
        ∀ y ∈ Set.Icc (f a) (f b), f (finv y) = y)
```

`Chapter9.MonotoneOn.exist_inverse_without_strictmono` (def, [line 149](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_8.lean#L149)). A definition whose value is left as `sorry`.

> Exercise 9.8.4 (without strict monotonicity)

```lean
def MonotoneOn.exist_inverse_without_strictmono :
    Decidable (∀ (a b : ℝ) (_ : a < b) (f : ℝ → ℝ) (_ : ContinuousOn f (.Icc a b))
        (_ : MonotoneOn f (.Icc a b)),
      f '' (.Icc a b) = .Icc (f a) (f b) ∧
      ∃ finv : ℝ → ℝ, ContinuousOn finv (.Icc (f a) (f b)) ∧ StrictMonoOn finv (.Icc (f a) (f b)) ∧
        finv '' (.Icc (f a) (f b)) = .Icc a b ∧
        (∀ x ∈ Set.Icc a b, finv (f x) = x) ∧
        ∀ y ∈ Set.Icc (f a) (f b), f (finv y) = y)
```

## Exercise 9.8.5(a)

`Chapter9.StrictMonoOn.of_f_9_8_5` (theorem, [line 175](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_8.lean#L175)). An exercise, stated without proof.

> Exercise 9.8.5(a)

```lean
theorem StrictMonoOn.of_f_9_8_5 : StrictMonoOn f_9_8_5 .univ
```

## Exercise 9.8.5(b)

`Chapter9.ContinuousAt.of_f_9_8_5'` (theorem, [line 179](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_8.lean#L179)). An exercise, stated without proof.

> Exercise 9.8.5(b)

```lean
theorem ContinuousAt.of_f_9_8_5' (r:ℚ) : ¬ ContinuousAt f_9_8_5 r
```

## Exercise 9.8.5(c)

`Chapter9.ContinuousAt.of_f_9_8_5` (theorem, [line 183](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_8.lean#L183)). An exercise, stated without proof.

> Exercise 9.8.5(c)

```lean
theorem ContinuousAt.of_f_9_8_5 {x:ℝ} (hx: ¬ ∃ r:ℚ, x = r) : ContinuousAt f_9_8_5 x
```

## Depends on

- [Section 9.6: The maximum principle](section-9-6.md)

## Sources

- [Analysis/Section_9_8.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_8.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_9_8/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_9_8.html)
