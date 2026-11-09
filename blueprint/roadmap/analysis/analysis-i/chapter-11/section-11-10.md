---
declaration: theorem
origin: cited
lean: Chapter11.integ_of_mul_deriv, Chapter11.PiecewiseConstantOn.RS_integ_eq_integ_of_mul_deriv, Chapter11.RS_integ_eq_integ_of_mul_deriv, Chapter11.PiecewiseConstantOn.RS_integ_of_comp, Chapter11.RS_integ_of_comp, Chapter11.integ_of_comp
statement: formalized
---

# Section 11.10: Consequences of the fundamental theorems

> I have attempted to make the translation as faithful a paraphrasing as possible of the
> original text. When there is a choice between a more idiomatic Lean solution and a
> more faithful translation, I have generally chosen the latter. In particular, there will
> be places where the Lean code could be "golfed" to be more elegant and idiomatic, but I
> have consciously avoided doing so.
>
> Main constructions and results of this section:
> - Integration by parts

*Quoted from [Analysis/Section_11_10.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_10.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 7 labelled items, carried by 7 declarations: 2 proved here and 5 stated without proof (3 of them exercises).

## Proposition 11.10.1 / Exercise 11.10.1

`Chapter11.integ_of_mul_deriv` (theorem, [line 26](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_10.lean#L26)). An exercise, stated without proof.

> Proposition 11.10.1 (Integration by parts formula) / Exercise 11.10.1

```lean
theorem integ_of_mul_deriv {a b:ℝ} (hab: a ≤ b) {F G: ℝ → ℝ}
  (hF: DifferentiableOn ℝ F (Icc a b)) (hG : DifferentiableOn ℝ G (Icc a b))
  (hF': IntegrableOn (derivWithin F (Icc a b)) (Icc a b))
  (hG': IntegrableOn (derivWithin G (Icc a b)) (Icc a b)) :
  integ (F * derivWithin G (Icc a b)) (Icc a b) = F b * G b - F a * G a -
    integ (G * derivWithin F (Icc a b)) (Icc a b)
```

## Theorem 11.10.2

`Chapter11.PiecewiseConstantOn.RS_integ_eq_integ_of_mul_deriv` (theorem, [line 35](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_10.lean#L35)). Proved here.

> Theorem 11.10.2.  Need to add continuity of α due to our conventions on `α_length`

```lean
theorem PiecewiseConstantOn.RS_integ_eq_integ_of_mul_deriv
  {a b:ℝ} {α f:ℝ → ℝ}
  (hα_diff: DifferentiableOn ℝ α (Icc a b)) (hαcont: Continuous α)
  (hα': IntegrableOn (derivWithin α (Icc a b)) (Icc a b))
  (hf: PiecewiseConstantOn f (Icc a b)) :
  IntegrableOn (f * derivWithin α (Icc a b)) (Icc a b) ∧
  Chapter11.integ (f * derivWithin α (Icc a b)) (Icc a b) = RS_integ f (Icc a b) α
```

## Corollary 11.10.3

`Chapter11.RS_integ_eq_integ_of_mul_deriv` (theorem, [line 79](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_10.lean#L79)). Stated without proof.

> Corollary 11.10.3

```lean
theorem RS_integ_eq_integ_of_mul_deriv
  {a b:ℝ} (hab: a < b) {α f:ℝ → ℝ} (hα: Monotone α)
  (hα_diff: DifferentiableOn ℝ α (Icc a b)) (hαcont: Continuous α)
  (hα': IntegrableOn (derivWithin α (Icc a b)) (Icc a b))
  (hf: RS_IntegrableOn f (Icc a b) α) :
  IntegrableOn (f * derivWithin α (Icc a b)) (Icc a b) ∧
  integ (f * derivWithin α (Icc a b)) (Icc a b) = RS_integ f (Icc a b) α
```

## Lemma 11.10.5 / Exercise 11.10.2

`Chapter11.PiecewiseConstantOn.RS_integ_of_comp` (theorem, [line 129](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_10.lean#L129)). An exercise, stated without proof.

> Lemma 11.10.5 / Exercise 11.10.2

```lean
theorem PiecewiseConstantOn.RS_integ_of_comp {a b:ℝ} (hab: a < b) {φ f:ℝ → ℝ}
  (hφ_cont: Continuous φ) (hφ_mono: Monotone φ) (hf: PiecewiseConstantOn f (Icc (φ a) (φ b))) :
  PiecewiseConstantOn (f ∘ φ) (Icc a b) ∧ RS_integ (f ∘ φ) (Icc a b) φ =
    integ f (Icc (φ a) (φ b))
```

## Proposition 11.10.6

`Chapter11.RS_integ_of_comp` (theorem, [line 179](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_10.lean#L179)). Stated without proof.

> Proposition 11.10.6 (Change of variables formula II).

```lean
theorem RS_integ_of_comp {a b:ℝ} (hab: a < b) {φ f: ℝ → ℝ}
  (hφ_cont: Continuous φ) (hφ_mono: Monotone φ) (hf: IntegrableOn f (Icc (φ a) (φ b))) :
  RS_IntegrableOn (f ∘ φ) (Icc a b) φ ∧
  RS_integ (f ∘ φ) (Icc a b) φ = integ f (Icc (φ a) (φ b))
```

## Proposition 11.10.7

`Chapter11.integ_of_comp` (theorem, [line 209](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_10.lean#L209)). Proved here.

> Proposition 11.10.7 (Change of variables formula III).

```lean
theorem integ_of_comp {a b:ℝ} (hab: a < b) {φ f: ℝ → ℝ}
  (hφ_diff: DifferentiableOn ℝ φ (Icc a b))
  (hφ_cont: Continuous φ) (hφ_mono: Monotone φ)
  (hφ': IntegrableOn (derivWithin φ (Icc a b)) (Icc a b))
  (hf: IntegrableOn f (Icc (φ a) (φ b))) :
  IntegrableOn (f ∘ φ * derivWithin φ (Icc a b)) (Icc a b) ∧
  integ (f ∘ φ * derivWithin φ (Icc a b)) (Icc a b) =
    integ f (Icc (φ a) (φ b))
```

## Exercise 11.10.3

An `example` ([line 222](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_10.lean#L222)). An exercise, stated without proof.

> Exercise 11.10.3

```lean
example {a b:ℝ} (hab: a < b) {f: ℝ → ℝ} (hf: IntegrableOn f (Icc a b)) :
  IntegrableOn (fun x ↦ f (-x)) (Icc (-b) (-a)) ∧
  integ (fun x ↦ f (-x)) (Icc (-b) (-a)) = integ f (Icc a b)
```

## Depends on

- [Section 9.6: The maximum principle](../chapter-9/section-9-6.md)
- [Section 10.3: Monotone functions and derivatives](../chapter-10/section-10-3.md)
- [Section 11.9: The two fundamental theorems of calculus](section-11-9.md)

## Sources

- [Analysis/Section_11_10.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_11_10.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_11_10/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_11_10.html)
