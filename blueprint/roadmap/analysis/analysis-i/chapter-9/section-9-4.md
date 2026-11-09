---
declaration: theorem
origin: cited
lean: Chapter9.ContinuousWithinAt.iff, Chapter9.f_9_4_6, Chapter9.ContinuousWithinAt.tfae, Filter.Tendsto.comp_of_continuous, Chapter9.ContinuousWithinAt.add, Chapter9.Continuous.exp, Chapter9.Continuous.exp', Chapter9.Continuous.abs, Chapter9.ContinuousWithinAt.comp, Chapter9.ContinuousOn.restrict, Chapter9.Continuous.polynomial
statement: formalized
---

# Section 9.4: Continuous functions

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text.  When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter.  In particular, there will be places where
> the Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
> - Continuity of functions, using the Mathlib notions

*Quoted from [Analysis/Section_9_4.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_4.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 16 labelled items, carried by 16 declarations: 3 proved here, 12 stated without proof (6 of them exercises) and 1 definition. It also has 5 declarations and 10 examples with no label, counted here but not shown.

## Definition 9.4.1

`Chapter9.ContinuousWithinAt.iff` (theorem, [line 24](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_4.lean#L24)). Proved here.

> Definition 9.4.1.  Here we use the Mathlib definition of continuity.  The hypothesis `x₀ ∈ X` is not needed!

```lean
theorem ContinuousWithinAt.iff (X:Set ℝ) (f: ℝ → ℝ)  (x₀:ℝ) :
  ContinuousWithinAt f X x₀ ↔ Convergesto X f (f x₀) x₀
```

## Example 9.4.2

An `example` ([line 33](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_4.lean#L33)). Stated without proof.

> Example 9.4.2.

```lean
example (c x₀:ℝ) : ContinuousWithinAt (fun x ↦ c) .univ x₀
```

## Example 9.4.3

An `example` ([line 42](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_4.lean#L42)). Stated without proof.

> Example 9.4.3.

```lean
example : Continuous (fun x:ℝ ↦ x)
```

## Example 9.4.4

An `example` ([line 45](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_4.lean#L45)). Stated without proof.

> Example 9.4.4.

```lean
example {x₀:ℝ} (h: x₀ ≠ 0) : ContinuousAt Real.sign x₀
```

## Example 9.4.5

An `example` ([line 50](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_4.lean#L50)). Stated without proof.

> Example 9.4.5.

```lean
example (x₀:ℝ) : ¬ ContinuousAt f_9_3_21 x₀
```

## Example 9.4.6

`Chapter9.f_9_4_6` (abbrev, [line 53](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_4.lean#L53)). A definition.

> Example 9.4.6.

```lean
noncomputable abbrev f_9_4_6 (x:ℝ) : ℝ
```

## Proposition 9.4.7 / Exercise 9.4.1

`Chapter9.ContinuousWithinAt.tfae` (theorem, [line 62](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_4.lean#L62)). An exercise, stated without proof.

> Proposition 9.4.7 / Exercise 9.4.1.

```lean
theorem ContinuousWithinAt.tfae (X:Set ℝ) (f: ℝ → ℝ) (x₀:ℝ) :
  [
    ContinuousWithinAt f X x₀,
    ∀ a:ℕ → ℝ, (∀ n, a n ∈ X) → Filter.atTop.Tendsto a (nhds x₀) → Filter.atTop.Tendsto (fun n ↦ f (a n)) (nhds (f x₀)),
    ∀ ε > 0, ∃ δ > 0, ∀ x ∈ X, |x-x₀| < δ → |f x - f x₀| < ε,
    ∀ ε > 0, ∃ δ > 0, ∀ x ∈ X, |x-x₀| ≤ δ → |f x - f x₀| ≤ ε
  ].TFAE
```

## Remark 9.4.8

`Filter.Tendsto.comp_of_continuous` (theorem, [line 72](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_4.lean#L72)). Proved here.

> Remark 9.4.8.

```lean
theorem _root_.Filter.Tendsto.comp_of_continuous {X:Set ℝ} {f: ℝ → ℝ} {x₀:ℝ}
  (h_cont: ContinuousWithinAt f X x₀) {a: ℕ → ℝ} (ha: ∀ n, a n ∈ X)
  (hconv: Filter.atTop.Tendsto a (nhds x₀)):
  Filter.atTop.Tendsto (fun n ↦ f (a n)) (nhds (f x₀))
```

## Proposition 9.4.9

`Chapter9.ContinuousWithinAt.add` (theorem, [line 80](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_4.lean#L80)). Proved here.

> Proposition 9.4.9

```lean
theorem ContinuousWithinAt.add {X:Set ℝ} (f g: ℝ → ℝ) {x₀:ℝ}
  (hf: ContinuousWithinAt f X x₀) (hg: ContinuousWithinAt g X x₀) :
  ContinuousWithinAt (f + g) X x₀
```

## Proposition 9.4.10 / Exercise 9.4.3

`Chapter9.Continuous.exp` (theorem, [line 114](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_4.lean#L114)). An exercise, stated without proof.

> Proposition 9.4.10 / Exercise 9.4.3

```lean
theorem Continuous.exp {a:ℝ} (ha: a>0) : Continuous (fun x:ℝ ↦ a ^ x)
```

## Proposition 9.4.11 / Exercise 9.4.4

`Chapter9.Continuous.exp'` (theorem, [line 118](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_4.lean#L118)). An exercise, stated without proof.

> Proposition 9.4.11 / Exercise 9.4.4

```lean
theorem Continuous.exp' (p:ℝ) : ContinuousOn (fun x:ℝ ↦ x ^ p) (.Ioi 0)
```

## Proposition 9.4.12

`Chapter9.Continuous.abs` (theorem, [line 122](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_4.lean#L122)). Stated without proof.

> Proposition 9.4.12

```lean
theorem Continuous.abs : Continuous (fun x:ℝ ↦ |x|)
```

## Proposition 9.4.13 / Exercise 9.4.5

`Chapter9.ContinuousWithinAt.comp` (theorem, [line 126](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_4.lean#L126)). An exercise, stated without proof.

> Proposition 9.4.13 / Exercise 9.4.5

```lean
theorem ContinuousWithinAt.comp {X Y: Set ℝ} {f g:ℝ → ℝ} (hf: ∀ x ∈ X, f x ∈ Y) (x₀:ℝ)
  (hf_cont: ContinuousWithinAt f X x₀) (hg_cont: ContinuousWithinAt g Y (f x₀)):
  ContinuousWithinAt (g ∘ f) X x₀
```

## Example 9.4.14

An `example` ([line 131](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_4.lean#L131)). Stated without proof.

> Example 9.4.14

```lean
example : Continuous (fun x:ℝ ↦ 3*x + 1)
```

## Exercise 9.4.6

`Chapter9.ContinuousOn.restrict` (theorem, [line 144](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_4.lean#L144)). An exercise, stated without proof.

> Exercise 9.4.6

```lean
theorem ContinuousOn.restrict {X Y:Set ℝ} {f: ℝ → ℝ} (hY: Y ⊆ X) (hf: ContinuousOn f X) : ContinuousOn f Y
```

## Exercise 9.4.7

`Chapter9.Continuous.polynomial` (theorem, [line 148](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_4.lean#L148)). An exercise, stated without proof.

> Exercise 9.4.7

```lean
theorem Continuous.polynomial {n:ℕ} (c: Fin n → ℝ) : Continuous (fun x:ℝ ↦ ∑ i, c i * x ^ (i:ℕ))
```

## Depends on

- [Section 9.3: Limiting values of functions](section-9-3.md)

## Sources

- [Analysis/Section_9_4.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_4.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_9_4/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_9_4.html)
