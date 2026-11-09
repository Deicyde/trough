---
declaration: abbrev
origin: cited
lean: Real.CloseFn, Real.CloseNear, Chapter9.Convergesto, Chapter9.Convergesto.iff_conv, Chapter9.Convergesto.uniq, Chapter9.Convergesto.add, Chapter9.Convergesto.sub, Chapter9.Convergesto.max, Chapter9.Convergesto.min, Chapter9.Convergesto.smul, Chapter9.Convergesto.mul, Chapter9.Convergesto.div, Chapter9.Convergesto.sign_right, Chapter9.Convergesto.sign_left, Chapter9.Convergesto.sign_all, Chapter9.Convergesto.local, Chapter9.f_9_3_21, Chapter9.Convergesto.squeeze
statement: formalized
---

# Section 9.3: Limiting values of functions

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text.  When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter.  In particular, there will be places where
> the Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Limits of continuous functions
> - Connection with Mathlib's filter convergence concepts
> - Limit laws for functions
>
> Technical point: in the text, the functions `f` studied are defined only on subsets `X` of `ℝ`, and
> left undefined elsewhere.  However, in Lean, this then creates some fiddly conversions when trying
> to restrict `f` to various subsets of `X` (which, technically, are not precisely subsets of `ℝ`,
> though they can be coerced to such).  To avoid this issue we will deviate from the text by having
> our functions defined on all of `ℝ` (with the understanding that they are assigned "junk" values
> outside of the domain `X` of interest).

*Quoted from [Analysis/Section_9_3.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 19 labelled items, carried by 27 declarations: 2 proved here, 21 stated without proof (9 of them exercises) and 4 definitions. It also has 12 declarations and 3 examples with no label, counted here but not shown.

## Definition 9.3.1

`Real.CloseFn` (abbrev, [line 33](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L33)). A definition.

> Definition 9.3.1
> Note the books uses ≤ instead of <, but < matches mathlib's definition of neighborhood.

```lean
abbrev Real.CloseFn (ε:ℝ) (X:Set ℝ) (f: ℝ → ℝ) (L:ℝ) : Prop
```

## Definition 9.3.3

`Real.CloseNear` (abbrev, [line 37](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L37)). A definition.

> Definition 9.3.3

```lean
abbrev Real.CloseNear (ε:ℝ) (X:Set ℝ) (f: ℝ → ℝ) (L:ℝ) (x₀:ℝ) : Prop
```

## Example 9.3.2

An `example` ([line 45](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L45)). Stated without proof.

> Example 9.3.2
> Slight change from the book to accomodate the change to `Real.CloseFn`

```lean
example : (5.1:ℝ).CloseFn (.Icc 1 3) (fun x ↦ x^2) 4
```

An `example` ([line 50](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L50)). Stated without proof.

> Example 9.3.2
> Slight change from the book to accomodate the change to `Real.CloseFn`

```lean
example : (0.42:ℝ).CloseFn (.Icc 1.9 2.1) (fun x ↦ x^2) 4
```

## Example 9.3.4

An `example` ([line 53](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L53)). Stated without proof.

> Example 9.3.4

```lean
example: ¬(0.1:ℝ).CloseFn (.Icc 1 3) (fun x ↦ x^2) 4
```

An `example` ([line 57](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L57)). Stated without proof.

> Example 9.3.4

```lean
example: (0.1:ℝ).CloseNear (.Icc 1 3) (fun x ↦ x^2) 4 2
```

## Example 9.3.5

An `example` ([line 61](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L61)). Stated without proof.

> Example 9.3.5

```lean
example: ¬(0.1:ℝ).CloseFn (.Icc 1 3) (fun x ↦ x^2) 9
```

An `example` ([line 65](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L65)). Stated without proof.

> Example 9.3.5

```lean
example: (0.1:ℝ).CloseNear (.Icc 1 3) (fun x ↦ x^2) 9 3
```

## Definition 9.3.6

`Chapter9.Convergesto` (abbrev, [line 69](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L69)). A definition.

> Definition 9.3.6 (Convergence of functions at a point).

```lean
abbrev Convergesto (X:Set ℝ) (f: ℝ → ℝ) (L:ℝ) (x₀:ℝ) : Prop
```

## Example 9.3.8

An `example` ([line 93](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L93)). Stated without proof.

> Example 9.3.8

```lean
example: Convergesto (.Icc 1 3) (fun x ↦ x^2) 4 2
```

## Proposition 9.3.9 / Exercise 9.3.1

`Chapter9.Convergesto.iff_conv` (theorem, [line 97](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L97)). An exercise, stated without proof.

> Proposition 9.3.9 / Exercise 9.3.1

```lean
theorem Convergesto.iff_conv {E:Set ℝ} (f: ℝ → ℝ) (L:ℝ) {x₀:ℝ} :
  Convergesto E f L x₀ ↔ ∀ a:ℕ → ℝ, (∀ n:ℕ, a n ∈ E) →
  Filter.atTop.Tendsto a (nhds x₀) →
  Filter.atTop.Tendsto (fun n ↦ f (a n)) (nhds L)
```

## Corollary 9.3.13

`Chapter9.Convergesto.uniq` (theorem, [line 112](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L112)). Proved here.

> Corollary 9.3.13

```lean
theorem Convergesto.uniq {E:Set ℝ} {f: ℝ → ℝ} {L L':ℝ} {x₀:ℝ} (h: AdherentPt x₀ E)
  (hf: Convergesto E f L x₀) (hf': Convergesto E f L' x₀) : L = L'
```

## Proposition 9.3.14

`Chapter9.Convergesto.add` (theorem, [line 119](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L119)). Proved here.

> Proposition 9.3.14 (Limit laws for functions, add)

```lean
theorem Convergesto.add {E:Set ℝ} {f g: ℝ → ℝ} {L M:ℝ} {x₀:ℝ}
  (hf: Convergesto E f L x₀) (hg: Convergesto E g M x₀) :
  Convergesto E (f + g) (L + M) x₀
```

## Proposition 9.3.14 / Exercise 9.3.2

`Chapter9.Convergesto.sub` (theorem, [line 128](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L128)). An exercise, stated without proof.

> Proposition 9.3.14 (Limit laws for functions, sub) / Exercise 9.3.2

```lean
theorem Convergesto.sub {E:Set ℝ} {f g: ℝ → ℝ} {L M:ℝ} {x₀:ℝ}
  (hf: Convergesto E f L x₀) (hg: Convergesto E g M x₀) :
  Convergesto E (f - g) (L - M) x₀
```

`Chapter9.Convergesto.max` (theorem, [line 134](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L134)). An exercise, stated without proof.

> Proposition 9.3.14 (Limit laws for functions, max) / Exercise 9.3.2

```lean
theorem Convergesto.max {E:Set ℝ} {f g: ℝ → ℝ} {L M:ℝ} {x₀:ℝ}
  (hf: Convergesto E f L x₀) (hg: Convergesto E g M x₀) :
  Convergesto E (max f g) (max L M) x₀
```

`Chapter9.Convergesto.min` (theorem, [line 140](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L140)). An exercise, stated without proof.

> Proposition 9.3.14 (Limit laws for functions, min) / Exercise 9.3.2

```lean
theorem Convergesto.min {E:Set ℝ} {f g: ℝ → ℝ} {L M:ℝ} {x₀:ℝ}
  (hf: Convergesto E f L x₀) (hg: Convergesto E g M x₀) :
  Convergesto E (min f g) (min L M) x₀
```

`Chapter9.Convergesto.smul` (theorem, [line 146](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L146)). An exercise, stated without proof.

> Proposition 9.3.14 (Limit laws for functions, smul) / Exercise 9.3.2

```lean
theorem Convergesto.smul {E:Set ℝ} {f: ℝ → ℝ} {L:ℝ} {x₀:ℝ}
  (hf: Convergesto E f L x₀) (c:ℝ) :
  Convergesto E (c • f) (c * L) x₀
```

`Chapter9.Convergesto.mul` (theorem, [line 152](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L152)). An exercise, stated without proof.

> Proposition 9.3.14 (Limit laws for functions, mul) / Exercise 9.3.2

```lean
theorem Convergesto.mul {E:Set ℝ} {f g: ℝ → ℝ} {L M:ℝ} {x₀:ℝ}
  (hf: Convergesto E f L x₀) (hg: Convergesto E g M x₀) :
  Convergesto E (f * g) (L * M) x₀
```

`Chapter9.Convergesto.div` (theorem, [line 158](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L158)). An exercise, stated without proof.

> Proposition 9.3.14 (Limit laws for functions, div) / Exercise 9.3.2.  The hypothesis in the book that g is non-vanishing on E can be dropped.

```lean
theorem Convergesto.div {E:Set ℝ} {f g: ℝ → ℝ} {L M:ℝ} {x₀:ℝ} (hM: M ≠ 0)
  (hf: Convergesto E f L x₀) (hg: Convergesto E g M x₀) :
  Convergesto E (f / g) (L / M) x₀
```

## Example 9.3.16 (a)

`Chapter9.Convergesto.sign_right` (theorem, [line 189](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L189)). Stated without proof.

> Example 9.3.16 (a)

```lean
theorem Convergesto.sign_right : Convergesto (.Ioi 0) Real.sign 1 0
```

## Example 9.3.16 (b)

`Chapter9.Convergesto.sign_left` (theorem, [line 192](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L192)). Stated without proof.

> Example 9.3.16 (b)

```lean
theorem Convergesto.sign_left : Convergesto (.Iio 0) Real.sign (-1) 0
```

## Example 9.3.16 (c)

`Chapter9.Convergesto.sign_all` (theorem, [line 195](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L195)). Stated without proof.

> Example 9.3.16 (c)

```lean
theorem Convergesto.sign_all : ¬ ∃ L, Convergesto (.univ) Real.sign L 0
```

## Proposition 9.3.18 / Exercise 9.3.3

`Chapter9.Convergesto.local` (theorem, [line 204](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L204)). An exercise, stated without proof.

> Proposition 9.3.18 / Exercise 9.3.3

```lean
theorem Convergesto.local {E:Set ℝ} {f: ℝ → ℝ} {L:ℝ} {x₀:ℝ} {δ:ℝ} (hδ: δ > 0) :
  Convergesto E f L x₀ ↔ Convergesto (E ∩ .Ioo (x₀-δ) (x₀+δ)) f L x₀
```

## Example 9.3.19

An `example` ([line 209](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L209)). Stated without proof.

> Example 9.3.19.  The point of this example is somewhat blunted by the ability to remove the hypothesis that `g` is non-zero from the relevant part of Proposition 9.3.14

```lean
example : Convergesto .univ (fun x ↦ (x+2)/(x+1)) (4/3:ℝ) 2
```

## Example 9.3.20

An `example` ([line 212](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L212)). Stated without proof.

> Example 9.3.20

```lean
example : Convergesto (.univ \ {1}) (fun x ↦ (x^2-1)/(x-1)) 2 1
```

## Example 9.3.21

`Chapter9.f_9_3_21` (abbrev, [line 216](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L216)). A definition.

> Example 9.3.21

```lean
noncomputable abbrev f_9_3_21 : ℝ → ℝ
```

## Exercise 9.3.5

`Chapter9.Convergesto.squeeze` (theorem, [line 227](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean#L227)). An exercise, stated without proof.

> Exercise 9.3.5 (Continuous version of squeeze test)

```lean
theorem Convergesto.squeeze {E:Set ℝ} {f g h: ℝ → ℝ} {L:ℝ} {x₀:ℝ}
  (hfg: ∀ x ∈ E, f x ≤ g x) (hgh: ∀ x ∈ E, g x ≤ h x)
  (hf: Convergesto E f L x₀) (hh: Convergesto E h L x₀) :
  Convergesto E g L x₀
```

## Depends on

- [Section 9.1: Subsets of the real line](section-9-1.md)

## Sources

- [Analysis/Section_9_3.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_3.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_9_3/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_9_3.html)
