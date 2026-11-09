---
declaration: abbrev
origin: cited
lean: Chapter11.Constant, Chapter11.PiecewiseConstantWith, Chapter11.PiecewiseConstantOn, Chapter11.f_11_2_4, Chapter11.ConstantOn.piecewiseConstantOn, Chapter11.PiecewiseConstantWith.mono, Chapter11.PiecewiseConstantOn.add, Chapter11.PiecewiseConstantOn.sub, Chapter11.PiecewiseConstantOn.max, Chapter11.PiecewiseConstantOn.min, Chapter11.PiecewiseConstantOn.mul, Chapter11.PiecewiseConstantOn.smul, Chapter11.PiecewiseConstantOn.div, Chapter11.PiecewiseConstantWith.integ, Chapter11.f_11_2_12, Chapter11.PiecewiseConstantWith.integ_eq, Chapter11.PiecewiseConstantOn.integ, Chapter11.PiecewiseConstantOn.integ_add, Chapter11.PiecewiseConstantOn.integ_smul, Chapter11.PiecewiseConstantOn.integ_sub, Chapter11.PiecewiseConstantOn.integ_of_nonneg, Chapter11.PiecewiseConstantOn.integ_mono, Chapter11.PiecewiseConstantOn.integ_const, Chapter11.PiecewiseConstantOn.integ_const', Chapter11.PiecewiseConstantOn.of_extend, Chapter11.PiecewiseConstantOn.integ_of_extend, Chapter11.PiecewiseConstantOn.of_join, Chapter11.PiecewiseConstantOn.integ_of_join
statement: formalized
---

# Section 11.2: Piecewise constant functions

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
> - Piecewise constant functions.
> - The piecewise constant integral.

*Quoted from [Analysis/Section_11_2.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 23 labelled items, carried by 29 declarations: 22 stated without proof (20 of them exercises) and 7 definitions. It also has 26 declarations and 6 examples with no label, counted here but not shown.

## Definition 11.2.1

`Chapter11.Constant` (abbrev, [line 23](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L23)). A definition.

> Definition 11.2.1

```lean
abbrev Constant {X Y:Type} (f: X → Y) : Prop
```

## Definition 11.2.3

`Chapter11.PiecewiseConstantWith` (abbrev, [line 74](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L74)). A definition.

> Definition 11.2.3 (Piecewise constant functions I)

```lean
abbrev PiecewiseConstantWith (f:ℝ → ℝ) {I: BoundedInterval} (P: Partition I) : Prop
```

## Definition 11.2.5

`Chapter11.PiecewiseConstantOn` (abbrev, [line 87](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L87)). A definition.

> Definition 11.2.5 (Piecewise constant functions I)

```lean
abbrev PiecewiseConstantOn (f:ℝ → ℝ) (I: BoundedInterval) : Prop
```

## Example 11.2.4 / Example 11.2.6

`Chapter11.f_11_2_4` (abbrev, [line 99](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L99)). A definition.

> Example 11.2.4 / Example 11.2.6

```lean
noncomputable abbrev f_11_2_4 : ℝ → ℝ
```

## Example 11.2.6

`Chapter11.ConstantOn.piecewiseConstantOn` (theorem, [line 120](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L120)). Stated without proof.

> Example 11.2.6

```lean
theorem ConstantOn.piecewiseConstantOn {f:ℝ → ℝ} {I: BoundedInterval} (h: ConstantOn f (I:Set ℝ)) :
  PiecewiseConstantOn f I
```

## Lemma 11.2.7 / Exercise 11.2.1

`Chapter11.PiecewiseConstantWith.mono` (theorem, [line 124](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L124)). An exercise, stated without proof.

> Lemma 11.2.7 / Exercise 11.2.1

```lean
theorem PiecewiseConstantWith.mono {f:ℝ → ℝ} {I: BoundedInterval} {P P': Partition I} (hPP': P ≤ P')
  (hP: PiecewiseConstantWith f P) : PiecewiseConstantWith f P'
```

## Lemma 11.2.8 / Exercise 11.2.2

`Chapter11.PiecewiseConstantOn.add` (theorem, [line 129](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L129)). An exercise, stated without proof.

> Lemma 11.2.8 / Exercise 11.2.2 (add).

```lean
theorem PiecewiseConstantOn.add {f g: ℝ → ℝ} {I: BoundedInterval}
  (hf: PiecewiseConstantOn f I) (hg: PiecewiseConstantOn g I) : PiecewiseConstantOn (f + g) I
```

`Chapter11.PiecewiseConstantOn.sub` (theorem, [line 134](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L134)). An exercise, stated without proof.

> Lemma 11.2.8 / Exercise 11.2.2 (sub).

```lean
theorem PiecewiseConstantOn.sub {f g: ℝ → ℝ} {I: BoundedInterval}
  (hf: PiecewiseConstantOn f I) (hg: PiecewiseConstantOn g I) : PiecewiseConstantOn (f - g) I
```

`Chapter11.PiecewiseConstantOn.max` (theorem, [line 139](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L139)). An exercise, stated without proof.

> Lemma 11.2.8 / Exercise 11.2.2 (max).

```lean
theorem PiecewiseConstantOn.max {f g: ℝ → ℝ} {I: BoundedInterval}
  (hf: PiecewiseConstantOn f I) (hg: PiecewiseConstantOn g I) : PiecewiseConstantOn (max f g) I
```

`Chapter11.PiecewiseConstantOn.min` (theorem, [line 144](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L144)). An exercise, stated without proof.

> Lemma 11.2.8 / Exercise 11.2.2 (min).

```lean
theorem PiecewiseConstantOn.min {f g: ℝ → ℝ} {I: BoundedInterval}
  (hf: PiecewiseConstantOn f I) (hg: PiecewiseConstantOn g I) : PiecewiseConstantOn (min f g) I
```

`Chapter11.PiecewiseConstantOn.mul` (theorem, [line 149](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L149)). An exercise, stated without proof.

> Lemma 11.2.8 / Exercise 11.2.2 (mul).

```lean
theorem PiecewiseConstantOn.mul {f g: ℝ → ℝ} {I: BoundedInterval}
  (hf: PiecewiseConstantOn f I) (hg: PiecewiseConstantOn g I) : PiecewiseConstantOn (f * g) I
```

`Chapter11.PiecewiseConstantOn.smul` (theorem, [line 154](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L154)). An exercise, stated without proof.

> Lemma 11.2.8 / Exercise 11.2.2 (smul).

```lean
theorem PiecewiseConstantOn.smul {f: ℝ → ℝ} {I: BoundedInterval}
  (c:ℝ) (hf: PiecewiseConstantOn f I) : PiecewiseConstantOn (c • f) I
```

`Chapter11.PiecewiseConstantOn.div` (theorem, [line 159](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L159)). An exercise, stated without proof.

> Lemma 11.2.8 / Exercise 11.2.2 (div).

```lean
theorem PiecewiseConstantOn.div {f g: ℝ → ℝ} {I: BoundedInterval}
  (hf: PiecewiseConstantOn f I) (hg: PiecewiseConstantOn g I) (hg_ne : ∀ x ∈ I.toSet, g x ≠ 0) :
  PiecewiseConstantOn (f / g) I
```

## Definition 11.2.9

`Chapter11.PiecewiseConstantWith.integ` (abbrev, [line 165](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L165)). A definition.

> Definition 11.2.9 (Piecewise constant integral I).

```lean
noncomputable abbrev PiecewiseConstantWith.integ (f:ℝ → ℝ) {I: BoundedInterval} (P: Partition I)  :
  ℝ
```

## Example 11.2.12

`Chapter11.f_11_2_12` (abbrev, [line 174](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L174)). A definition.

> Example 11.2.12

```lean
noncomputable abbrev f_11_2_12 : ℝ → ℝ
```

## Proposition 11.2.13 / Exercise 11.2.3

`Chapter11.PiecewiseConstantWith.integ_eq` (theorem, [line 206](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L206)). An exercise, stated without proof.

> Proposition 11.2.13 (Piecewise constant integral is independent of partition) / Exercise 11.2.3

```lean
theorem PiecewiseConstantWith.integ_eq {f:ℝ → ℝ} {I: BoundedInterval} {P P': Partition I}
  (hP: PiecewiseConstantWith f P) (hP': PiecewiseConstantWith f P') : integ f P = integ f P'
```

## Definition 11.2.14

`Chapter11.PiecewiseConstantOn.integ` (abbrev, [line 212](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L212)). A definition.

> Definition 11.2.14 (Piecewise constant integral II)

```lean
noncomputable abbrev PiecewiseConstantOn.integ (f:ℝ → ℝ) (I: BoundedInterval) :
  ℝ
```

## Example 11.2.15

An `example` ([line 230](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L230)). Stated without proof.

> Example 11.2.15

```lean
example : PiecewiseConstantOn.integ f_11_2_12 (Icc 1 4) = 10
```

## Theorem 11.2.16 (a) / Exercise 11.2.4

`Chapter11.PiecewiseConstantOn.integ_add` (theorem, [line 234](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L234)). An exercise, stated without proof.

> Theorem 11.2.16 (a) (Laws of integration) / Exercise 11.2.4

```lean
theorem PiecewiseConstantOn.integ_add {f g: ℝ → ℝ} {I: BoundedInterval}
  (hf: PiecewiseConstantOn f I) (hg: PiecewiseConstantOn g I) :
  integ (f + g) I = integ f I + integ g I
```

## Theorem 11.2.16 (b) / Exercise 11.2.4

`Chapter11.PiecewiseConstantOn.integ_smul` (theorem, [line 240](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L240)). An exercise, stated without proof.

> Theorem 11.2.16 (b) (Laws of integration) / Exercise 11.2.4

```lean
theorem PiecewiseConstantOn.integ_smul {f: ℝ → ℝ} {I: BoundedInterval} (c:ℝ) (hf: PiecewiseConstantOn f I) :
  integ (c • f) I = c * integ f I
```

## Theorem 11.2.16 (c) / Exercise 11.2.4

`Chapter11.PiecewiseConstantOn.integ_sub` (theorem, [line 246](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L246)). An exercise, stated without proof.

> Theorem 11.2.16 (c) (Laws of integration) / Exercise 11.2.4

```lean
theorem PiecewiseConstantOn.integ_sub {f g: ℝ → ℝ} {I: BoundedInterval}
  (hf: PiecewiseConstantOn f I) (hg: PiecewiseConstantOn g I) :
  integ (f - g) I = integ f I - integ g I
```

## Theorem 11.2.16 (d) / Exercise 11.2.4

`Chapter11.PiecewiseConstantOn.integ_of_nonneg` (theorem, [line 252](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L252)). An exercise, stated without proof.

> Theorem 11.2.16 (d) (Laws of integration) / Exercise 11.2.4

```lean
theorem PiecewiseConstantOn.integ_of_nonneg {f: ℝ → ℝ} {I: BoundedInterval} (h: ∀ x ∈ I, 0 ≤ f x)
  (hf: PiecewiseConstantOn f I) :
  0 ≤ integ f I
```

## Theorem 11.2.16 (e) / Exercise 11.2.4

`Chapter11.PiecewiseConstantOn.integ_mono` (theorem, [line 258](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L258)). An exercise, stated without proof.

> Theorem 11.2.16 (e) (Laws of integration) / Exercise 11.2.4

```lean
theorem PiecewiseConstantOn.integ_mono {f g: ℝ → ℝ} {I: BoundedInterval} (h: ∀ x ∈ I, f x ≤ g x)
  (hf: PiecewiseConstantOn f I) (hg: PiecewiseConstantOn g I) :
  integ f I ≤ integ g I
```

## Theorem 11.2.16 (f) / Exercise 11.2.4

`Chapter11.PiecewiseConstantOn.integ_const` (theorem, [line 265](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L265)). An exercise, stated without proof.

> Theorem 11.2.16 (f) (Laws of integration) / Exercise 11.2.4

```lean
theorem PiecewiseConstantOn.integ_const (c: ℝ) (I: BoundedInterval) :
  integ (fun _ ↦ c) I = c * |I|ₗ
```

## Theorem 11.2.16 (f') / Exercise 11.2.4

`Chapter11.PiecewiseConstantOn.integ_const'` (theorem, [line 270](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L270)). An exercise, stated without proof.

> Theorem 11.2.16 (f') (Laws of integration) / Exercise 11.2.4

```lean
theorem PiecewiseConstantOn.integ_const' {f:ℝ → ℝ} {I: BoundedInterval} (h: ConstantOn f I) :
  integ f I = (constant_value_on f I) * |I|ₗ
```

## Theorem 11.2.16 (g) / Exercise 11.2.4

`Chapter11.PiecewiseConstantOn.of_extend` (theorem, [line 276](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L276)). An exercise, stated without proof.

> Theorem 11.2.16 (g) (Laws of integration) / Exercise 11.2.4

```lean
theorem PiecewiseConstantOn.of_extend {I J: BoundedInterval} (hIJ: I ⊆ J)
  {f: ℝ → ℝ} (h: PiecewiseConstantOn f I) :
  PiecewiseConstantOn (fun x ↦ if x ∈ I then f x else 0) J
```

## Theorem 11.2.16 (g') / Exercise 11.2.4

`Chapter11.PiecewiseConstantOn.integ_of_extend` (theorem, [line 283](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L283)). An exercise, stated without proof.

> Theorem 11.2.16 (g') (Laws of integration) / Exercise 11.2.4

```lean
theorem PiecewiseConstantOn.integ_of_extend {I J: BoundedInterval} (hIJ: I ⊆ J)
  {f: ℝ → ℝ} (h: PiecewiseConstantOn f I) :
  integ (fun x ↦ if x ∈ I then f x else 0) J = integ f I
```

## Theorem 11.2.16 (h) / Exercise 11.2.4

`Chapter11.PiecewiseConstantOn.of_join` (theorem, [line 289](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L289)). An exercise, stated without proof.

> Theorem 11.2.16 (h) (Laws of integration) / Exercise 11.2.4

```lean
theorem PiecewiseConstantOn.of_join {I J K: BoundedInterval} (hIJK: K.joins I J)
  (f: ℝ → ℝ) : PiecewiseConstantOn f K ↔ PiecewiseConstantOn f I ∧ PiecewiseConstantOn f J
```

## Theorem 11.2.16 (h') / Exercise 11.2.4

`Chapter11.PiecewiseConstantOn.integ_of_join` (theorem, [line 294](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean#L294)). An exercise, stated without proof.

> Theorem 11.2.16 (h') (Laws of integration) / Exercise 11.2.4

```lean
theorem PiecewiseConstantOn.integ_of_join {I J K: BoundedInterval} (hIJK: K.joins I J)
  {f: ℝ → ℝ} (h: PiecewiseConstantOn f K) :
  integ f K = integ f I + integ f J
```

## Depends on

- [Section 11.1: Partitions](section-11-1.md)

## Sources

- [Analysis/Section_11_2.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_2.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_11_2/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_11_2.html)
