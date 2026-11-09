---
declaration: theorem
origin: cited
lean: Chapter9.UniformContinuousOn.iff, Real.CloseSeqs, Chapter6.Sequence.equiv_iff_rat, Chapter6.Sequence.equiv_iff, Chapter9.UniformContinuousOn.iff_preserves_equiv, Chapter9.Chapter6.Sequence.equiv_const, Chapter9.f_9_9_10, Chapter9.f_9_9_11, Chapter9.UniformContinuousOn.ofCauchy, Chapter9.UniformContinuousOn.limit_at_adherent, Chapter9.UniformContinuousOn.of_bounded, Chapter9.UniformContinuousOn.of_continuousOn, Chapter9.UniformContinuousOn.comp
statement: formalized
---

# Section 9.9: Uniform continuity

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text.  When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter.  In particular, there will be places where
> the Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
> - API for Mathlib's `UniformContinuousOn`.
> - Continuous functions on compact intervals are uniformly continuous.

*Quoted from [Analysis/Section_9_9.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_9.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 15 labelled items, carried by 15 declarations: 1 proved here, 11 stated without proof (6 of them exercises) and 3 definitions. It also has 3 declarations and 17 examples with no label, counted here but not shown.

## Example 9.9.1

An `example` ([line 31](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_9.lean#L31)). Stated without proof.

> Example 9.9.1

```lean
example (x : ℝ) :
  let f : ℝ → ℝ := fun x ↦ 1/x
  let ε : ℝ := 0.1
  let x₀ : ℝ := 1
  let δ : ℝ := 1/11
  |x-x₀| ≤ δ → |f x - f x₀| ≤ ε
```

## Definition 9.9.2

`Chapter9.UniformContinuousOn.iff` (theorem, [line 67](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_9.lean#L67)). Proved here.

> Definition 9.9.2.  Here we use the Mathlib term `UniformContinuousOn`

```lean
theorem UniformContinuousOn.iff (f: ℝ → ℝ) (X:Set ℝ) : UniformContinuousOn f X  ↔
  ∀ ε > (0:ℝ), ∃ δ > (0:ℝ), ∀ x₀ ∈ X, ∀ x ∈ X, δ.Close x x₀ → ε.Close (f x) (f x₀)
```

## Definition 9.9.5

`Real.CloseSeqs` (abbrev, [line 85](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_9.lean#L85)). A definition.

> Definition 9.9.5.  This is similar but not identical to `Real.CloseSeq` from
> Section 6.1.

```lean
abbrev Real.CloseSeqs (ε:ℝ) (a b: Chapter6.Sequence) : Prop
```

## Remark 9.9.6

`Chapter6.Sequence.equiv_iff_rat` (theorem, [line 95](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_9.lean#L95)). Stated without proof.

> Remark 9.9.6

```lean
theorem Chapter6.Sequence.equiv_iff_rat (a b: Sequence) :
  a.equiv b ↔ ∀ ε > (0:ℚ), (ε:ℝ).EventuallyCloseSeqs a b
```

## Lemma 9.9.7 / Exercise 9.9.1

`Chapter6.Sequence.equiv_iff` (theorem, [line 100](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_9.lean#L100)). An exercise, stated without proof.

> Lemma 9.9.7 / Exercise 9.9.1

```lean
theorem Chapter6.Sequence.equiv_iff (a b: Sequence) :
  a.equiv b ↔ atTop.Tendsto (fun n ↦ a n - b n) (nhds 0)
```

## Proposition 9.9.8 / Exercise 9.9.2

`Chapter9.UniformContinuousOn.iff_preserves_equiv` (theorem, [line 109](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_9.lean#L109)). An exercise, stated without proof.

> Proposition 9.9.8 / Exercise 9.9.2

```lean
theorem UniformContinuousOn.iff_preserves_equiv {X:Set ℝ} (f: ℝ → ℝ) :
  UniformContinuousOn f X ↔
  ∀ x y: ℕ → ℝ, (∀ n, x n ∈ X) → (∀ n, y n ∈ X) →
  (x:Sequence).equiv (y:Sequence) →
  (f ∘ x:Sequence).equiv (f ∘ y:Sequence)
```

## Remark 9.9.9

`Chapter9.Chapter6.Sequence.equiv_const` (theorem, [line 117](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_9.lean#L117)). Stated without proof.

> Remark 9.9.9

```lean
theorem Chapter6.Sequence.equiv_const (x₀: ℝ) (x:ℕ → ℝ) : atTop.Tendsto x (nhds x₀) ↔
  (x:Sequence).equiv (fun n:ℕ ↦ x₀:Sequence)
```

## Example 9.9.10

`Chapter9.f_9_9_10` (abbrev, [line 122](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_9.lean#L122)). A definition.

> Example 9.9.10

```lean
noncomputable abbrev f_9_9_10 : ℝ → ℝ
```

## Example 9.9.11

`Chapter9.f_9_9_11` (abbrev, [line 136](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_9.lean#L136)). A definition.

> Example 9.9.11

```lean
abbrev f_9_9_11 : ℝ → ℝ
```

## Proposition 9.9.12 / Exercise 9.9.3

`Chapter9.UniformContinuousOn.ofCauchy` (theorem, [line 148](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_9.lean#L148)). An exercise, stated without proof.

> Proposition 9.9.12 / Exercise 9.9.3

```lean
theorem UniformContinuousOn.ofCauchy  {X:Set ℝ} (f: ℝ → ℝ)
  (hf: UniformContinuousOn f X) {x: ℕ → ℝ} (hx: (x:Sequence).IsCauchy) (hmem : ∀ n, x n ∈ X) :
  (f ∘ x:Sequence).IsCauchy
```

## Example 9.9.13

An `example` ([line 154](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_9.lean#L154)). Stated without proof.

> Example 9.9.13

```lean
example : ((fun n:ℕ ↦ 1/(n+1:ℝ)):Sequence).IsCauchy
```

## Corollary 9.9.14 / Exercise 9.9.4

`Chapter9.UniformContinuousOn.limit_at_adherent` (theorem, [line 167](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_9.lean#L167)). An exercise, stated without proof.

> Corollary 9.9.14 / Exercise 9.9.4

```lean
theorem UniformContinuousOn.limit_at_adherent  {X:Set ℝ} (f: ℝ → ℝ)
  (hf: UniformContinuousOn f X) {x₀:ℝ} (hx₀: AdherentPt x₀ X) :
  ∃ L:ℝ, (nhdsWithin x₀ X).Tendsto f (nhds L)
```

## Proposition 9.9.15 / Exercise 9.9.5

`Chapter9.UniformContinuousOn.of_bounded` (theorem, [line 173](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_9.lean#L173)). An exercise, stated without proof.

> Proposition 9.9.15 / Exercise 9.9.5

```lean
theorem UniformContinuousOn.of_bounded {E X:Set ℝ} {f: ℝ → ℝ}
  (hf: UniformContinuousOn f X) (hEX: E ⊆ X) (hE: Bornology.IsBounded E) :
  Bornology.IsBounded (f '' E)
```

## Theorem 9.9.16

`Chapter9.UniformContinuousOn.of_continuousOn` (theorem, [line 179](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_9.lean#L179)). Stated without proof.

> Theorem 9.9.16

```lean
theorem UniformContinuousOn.of_continuousOn {a b:ℝ} {f:ℝ → ℝ}
  (hcont: ContinuousOn f (.Icc a b)) :
  UniformContinuousOn f (.Icc a b)
```

## Exercise 9.9.6

`Chapter9.UniformContinuousOn.comp` (theorem, [line 225](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_9.lean#L225)). An exercise, stated without proof.

> Exercise 9.9.6

```lean
theorem UniformContinuousOn.comp {X Y: Set ℝ} {f g:ℝ → ℝ}
  (hf: UniformContinuousOn f X) (hg: UniformContinuousOn g Y)
  (hrange: f '' X ⊆ Y) : UniformContinuousOn (g ∘ f) X
```

## Depends on

- [Section 6.1: Convergence and limit laws](../chapter-6/section-6-1.md)
- [Section 9.6: The maximum principle](section-9-6.md)

## Sources

- [Analysis/Section_9_9.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_9.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_9_9/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_9_9.html)
