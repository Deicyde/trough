---
declaration: theorem
origin: cited
lean: Chapter11.IntegrableOn.add, Chapter11.IntegrableOn.smul, Chapter11.IntegrableOn.sub, Chapter11.IntegrableOn.nonneg, Chapter11.IntegrableOn.mono, Chapter11.IntegrableOn.const, Chapter11.IntegrableOn.const', Chapter11.IntegrableOn.of_extend, Chapter11.IntegrableOn.of_extend', Chapter11.IntegrableOn.join, Chapter11.IntegrableOn.max, Chapter11.IntegrableOn.min, Chapter11.IntegrableOn.abs, Chapter11.integ_of_mul_nonneg, Chapter11.IntegrableOn.split
statement: formalized
---

# Section 11.4: Basic properties of the Riemann integral

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
> - Basic properties of the Riemann integral.

*Quoted from [Analysis/Section_11_4.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_4.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 15 labelled items, carried by 15 declarations: 2 proved here and 13 stated without proof (12 of them exercises). It also has 5 declarations with no label, counted here but not shown.

## Theorem 11.4.1(a) / Exercise 11.4.1

`Chapter11.IntegrableOn.add` (theorem, [line 23](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_4.lean#L23)). An exercise, stated without proof.

> Theorem 11.4.1(a) / Exercise 11.4.1

```lean
theorem IntegrableOn.add {I: BoundedInterval} {f g:ℝ → ℝ} (hf: IntegrableOn f I) (hg: IntegrableOn g I) :
  IntegrableOn (f + g) I ∧ integ (f + g) I = integ f I + integ g I
```

## Theorem 11.4.1(b) / Exercise 11.4.1

`Chapter11.IntegrableOn.smul` (theorem, [line 28](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_4.lean#L28)). An exercise, stated without proof.

> Theorem 11.4.1(b) / Exercise 11.4.1

```lean
theorem IntegrableOn.smul {I: BoundedInterval} (c:ℝ) {f:ℝ → ℝ} (hf: IntegrableOn f I) :
  IntegrableOn (c • f) I ∧ integ (c • f) I = c * integ f I
```

## Theorem 11.4.1(c) / Exercise 11.4.1

`Chapter11.IntegrableOn.sub` (theorem, [line 36](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_4.lean#L36)). An exercise, stated without proof.

> Theorem 11.4.1(c) / Exercise 11.4.1

```lean
theorem IntegrableOn.sub {I: BoundedInterval} {f g:ℝ → ℝ} (hf: IntegrableOn f I) (hg: IntegrableOn g I) :
  IntegrableOn (f - g) I ∧ integ (f - g) I = integ f I - integ g I
```

## Theorem 11.4.1(d) / Exercise 11.4.1

`Chapter11.IntegrableOn.nonneg` (theorem, [line 41](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_4.lean#L41)). An exercise, stated without proof.

> Theorem 11.4.1(d) / Exercise 11.4.1

```lean
theorem IntegrableOn.nonneg {I: BoundedInterval} {f:ℝ → ℝ} (hf: IntegrableOn f I) (hf_nonneg: ∀ x ∈ I, 0 ≤ f x) :
  0 ≤ integ f I
```

## Theorem 11.4.1(e) / Exercise 11.4.1

`Chapter11.IntegrableOn.mono` (theorem, [line 46](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_4.lean#L46)). An exercise, stated without proof.

> Theorem 11.4.1(e) / Exercise 11.4.1

```lean
theorem IntegrableOn.mono {I: BoundedInterval} {f g:ℝ → ℝ} (hf: IntegrableOn f I) (hg: IntegrableOn g I)
  (h: MajorizesOn g f I) :
  integ f I ≤ integ g I
```

## Theorem 11.4.1(f) / Exercise 11.4.1

`Chapter11.IntegrableOn.const` (theorem, [line 52](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_4.lean#L52)). An exercise, stated without proof.

> Theorem 11.4.1(f) / Exercise 11.4.1

```lean
theorem IntegrableOn.const (c:ℝ) (I: BoundedInterval) :
  IntegrableOn (fun _ ↦ c) I ∧ integ (fun _ ↦ c) I = c * |I|ₗ
```

## Theorem 11.4.1(f') / Exercise 11.4.1

`Chapter11.IntegrableOn.const'` (theorem, [line 57](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_4.lean#L57)). An exercise, stated without proof.

> Theorem 11.4.1(f') / Exercise 11.4.1

```lean
theorem IntegrableOn.const' {I: BoundedInterval} {f:ℝ → ℝ} (hf: ConstantOn f I) :
  IntegrableOn f I ∧ integ f I = (constant_value_on f I) * |I|ₗ
```

## Theorem 11.4.1(g) / Exercise 11.4.1

`Chapter11.IntegrableOn.of_extend` (theorem, [line 64](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_4.lean#L64)). An exercise, stated without proof.

> Theorem 11.4.1(g) / Exercise 11.4.1

```lean
theorem IntegrableOn.of_extend {I J: BoundedInterval} (hIJ: I ⊆ J)
  {f: ℝ → ℝ} (h: IntegrableOn f I) :
  IntegrableOn (fun x ↦ if x ∈ I then f x else 0) J
```

## Theorem 11.4.1(g') / Exercise 11.4.1

`Chapter11.IntegrableOn.of_extend'` (theorem, [line 71](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_4.lean#L71)). An exercise, stated without proof.

> Theorem 11.4.1(g') / Exercise 11.4.1

```lean
theorem IntegrableOn.of_extend' {I J: BoundedInterval} (hIJ: I ⊆ J)
  {f: ℝ → ℝ} (h: IntegrableOn f I) :
  integ (fun x ↦ if x ∈ I then f x else 0) J = integ f I
```

## Theorem 11.4.1 (h) / Exercise 11.4.1

`Chapter11.IntegrableOn.join` (theorem, [line 77](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_4.lean#L77)). An exercise, stated without proof.

> Theorem 11.4.1 (h) (Laws of integration) / Exercise 11.4.1

```lean
theorem IntegrableOn.join {I J K: BoundedInterval} (hIJK: K.joins I J)
  {f: ℝ → ℝ} (h: IntegrableOn f K) :
  IntegrableOn f I ∧ IntegrableOn f J ∧ integ f K = integ f I + integ f J
```

## Theorem 11.4.3

`Chapter11.IntegrableOn.max` (theorem, [line 102](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_4.lean#L102)). Stated without proof.

> Theorem 11.4.3 (Max and min preserve integrability).

```lean
theorem IntegrableOn.max {I: BoundedInterval} {f g:ℝ → ℝ} (hf: IntegrableOn f I) (hg: IntegrableOn g I) :
  IntegrableOn (f ⊔ g) I
```

## Theorem 11.4.5 / Exercise 11.4.3

`Chapter11.IntegrableOn.min` (theorem, [line 148](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_4.lean#L148)). An exercise, stated without proof.

> Theorem 11.4.5 / Exercise 11.4.3.  The objective here is to create a shorter proof than the one above.

```lean
theorem IntegrableOn.min {I: BoundedInterval} {f g:ℝ → ℝ} (hf: IntegrableOn f I) (hg: IntegrableOn g I) :
  IntegrableOn (f ⊓ g) I
```

## Corollary 11.4.4

`Chapter11.IntegrableOn.abs` (theorem, [line 153](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_4.lean#L153)). Proved here.

> Corollary 11.4.4

```lean
theorem IntegrableOn.abs {I: BoundedInterval} {f:ℝ → ℝ} (hf: IntegrableOn f I) :
  IntegrableOn (abs f) I
```

## Theorem 11.4.5

`Chapter11.integ_of_mul_nonneg` (theorem, [line 161](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_4.lean#L161)). Proved here.

> Theorem 11.4.5 (Products preserve Riemann integrability).
> It is convenient to first establish the non-negative case.

```lean
theorem integ_of_mul_nonneg {I: BoundedInterval} {f g:ℝ → ℝ} (hf: IntegrableOn f I) (hg: IntegrableOn g I)
  (hf_nonneg: MajorizesOn f 0 I) (hg_nonneg: MajorizesOn g 0 I) :
  IntegrableOn (f * g) I
```

## Exercise 11.4.2

`Chapter11.IntegrableOn.split` (theorem, [line 290](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_4.lean#L290)). An exercise, stated without proof.

> Exercise 11.4.2

```lean
theorem IntegrableOn.split {I: BoundedInterval} {f: ℝ → ℝ} (hf: IntegrableOn f I) (P: Partition I) :
  integ f I = ∑ J ∈ P.intervals, integ f J
```

## Depends on

- [Section 9.6: The maximum principle](../chapter-9/section-9-6.md)
- [Section 11.3: Upper and lower Riemann integrals](section-11-3.md)

## Sources

- [Analysis/Section_11_4.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_4.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_11_4/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_11_4.html)
