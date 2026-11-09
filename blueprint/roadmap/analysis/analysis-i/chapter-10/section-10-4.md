---
declaration: theorem
origin: cited
lean: HasDerivWithinAt.of_inverse, Chapter10.inverse_function_theorem
statement: formalized
---

# Section 10.4: Inverse functions and derivatives

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text.  When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter.  In particular, there will be places where
> the Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
> - The inverse function theorem.

*Quoted from [Analysis/Section_10_4.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_4.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 8 labelled items, carried by 8 declarations: 1 proved here and 7 stated without proof (6 of them exercises). It also has 2 declarations and 1 example with no label, counted here but not shown.

## Lemma 10.4.1

`HasDerivWithinAt.of_inverse` (theorem, [line 24](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_4.lean#L24)). Proved here.

> Lemma 10.4.1

```lean
theorem _root_.HasDerivWithinAt.of_inverse {X Y: Set ℝ} {f: ℝ → ℝ} {g:ℝ → ℝ}
  (hfXY: ∀ x ∈ X, f x ∈ Y) (hgf: ∀ x ∈ X, g (f x) = x)
  {x₀ y₀ f'x₀ g'y₀: ℝ} (hx₀: x₀ ∈ X) (hfx₀: f x₀ = y₀)
  (hcluster: ClusterPt x₀ (.principal (X \ {x₀})))
  (hf: HasDerivWithinAt f f'x₀ X x₀) (hg: HasDerivWithinAt g g'y₀ Y y₀) :
  g'y₀ * f'x₀ = 1
```

## Theorem 10.4.2

`Chapter10.inverse_function_theorem` (theorem, [line 56](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_4.lean#L56)). Stated without proof.

> Theorem 10.4.2 (Inverse function theorem)

```lean
theorem inverse_function_theorem {X Y: Set ℝ} {f: ℝ → ℝ} {g:ℝ → ℝ}
  (hfXY: ∀ x ∈ X, f x ∈ Y) (hgYX: ∀ y ∈ Y, g y ∈ X)
  (hgf: ∀ x ∈ X, g (f x) = x) (hfg: ∀ y ∈ Y, f (g y) = y)
  {x₀ y₀ f'x₀: ℝ} (hx₀: x₀ ∈ X) (hfx₀: f x₀ = y₀) (hne : f'x₀ ≠ 0)
  (hf: HasDerivWithinAt f f'x₀ X x₀) (hg: ContinuousWithinAt g Y y₀) :
    HasDerivWithinAt g (1/f'x₀) Y y₀
```

## Exercise 10.4.1(a)

An `example` ([line 76](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_4.lean#L76)). An exercise, stated without proof.

> Exercise 10.4.1(a)

```lean
example {n:ℕ} : ContinuousOn (fun x:ℝ ↦ x^(1/(n:ℝ))) (.Ioi 0)
```

## Exercise 10.4.1(b)

An `example` ([line 79](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_4.lean#L79)). An exercise, stated without proof.

> Exercise 10.4.1(b)

```lean
example {n:ℕ} {x:ℝ} (hx: x ∈ Set.Ioi 0) : HasDerivWithinAt (fun x:ℝ ↦ x^(1/(n:ℝ)))
  ((n:ℝ)⁻¹ * x^((n:ℝ)⁻¹-1)) (.Ioi 0) x
```

## Exercise 10.4.2(a)

An `example` ([line 83](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_4.lean#L83)). An exercise, stated without proof.

> Exercise 10.4.2(a)

```lean
example (q:ℚ) {x:ℝ} (hx: x ∈ Set.Ioi 0) :
  HasDerivWithinAt (fun x:ℝ ↦ x^(q:ℝ)) (q * x^(q-1:ℝ)) (.Ioi 0) x
```

## Exercise 10.4.2(b)

An `example` ([line 88](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_4.lean#L88)). An exercise, stated without proof.

> Exercise 10.4.2(b)

```lean
example (q:ℚ) : (nhdsWithin 1 (.Ioi 0 \ {1})).Tendsto (fun x:ℝ ↦ (x^(q:ℝ)-1)/(x-1)) (nhds q)
```

## Exercise 10.4.3(a)

An `example` ([line 92](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_4.lean#L92)). An exercise, stated without proof.

> Exercise 10.4.3(a)

```lean
example (α:ℝ) : (nhdsWithin 1 (.Ioi 0 \ {1})).Tendsto (fun x:ℝ ↦ (x^α-1^α)/(x-1)) (nhds α)
```

## Exercise 10.4.3(b)

An `example` ([line 96](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_4.lean#L96)). An exercise, stated without proof.

> Exercise 10.4.3(b)

```lean
example (α:ℝ) {x:ℝ} (hx: x ∈ Set.Ioi 0) : HasDerivWithinAt (fun x:ℝ ↦ x^α) (α * x^(α-1)) (.Ioi 0) x
```

## Depends on

- [Section 9.3: Limiting values of functions](../chapter-9/section-9-3.md)
- [Section 9.4: Continuous functions](../chapter-9/section-9-4.md)
- [Section 10.1: Basic definitions](section-10-1.md)

## Sources

- [Analysis/Section_10_4.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_10_4.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_10_4/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_10_4.html)
