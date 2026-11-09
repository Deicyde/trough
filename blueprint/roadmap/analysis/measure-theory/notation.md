---
declaration: theorem
origin: cited
lean: ENNReal.tsum_of_tsum, ENNReal.tsum_of_tsum', Set.choose, Countable.choose
statement: formalized
proof: formalized
---

# Chapter 0: Notation

> A companion to Chapter 0 of the book "An introduction to Measure Theory".
>
> We use existing Mathlib constructions, such as `Set.indicator`, `EuclideanSpace`, `ENNReal`,
> and `tsum` to describe the concepts defined in Chapter 0.

*Quoted from [Analysis/MeasureTheory/Notation.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Notation.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 5 labelled items, carried by 6 declarations: 4 proved here and 2 definitions. It also has 18 declarations and 2 examples with no label, counted here but not shown.

## Exercise 0.0.1

An `example` ([line 189](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Notation.lean#L189)). Proved here.

> Exercise 0.0.1

```lean
example {A:Type} {x : A → ENNReal} (hx: ∑' α, x α < ⊤) :
  ∃ E: Set A, Countable E ∧ ∀ α ∉ E, x α = 0
```

## Theorem 0.0.2

`ENNReal.tsum_of_tsum` (theorem, [line 197](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Notation.lean#L197)). Proved here.

> Theorem 0.0.2 (Tonelli's theorem for series)

```lean
theorem ENNReal.tsum_of_tsum (x: ℕ → ℕ → ENNReal) : ∑' p:ℕ × ℕ, x p.1 p.2 = ∑' n, ∑' m, x n m
```

`ENNReal.tsum_of_tsum'` (theorem, [line 228](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Notation.lean#L228)). Proved here.

> Theorem 0.0.2

```lean
theorem ENNReal.tsum_of_tsum' (x: ℕ → ℕ → ENNReal) : ∑' p:ℕ × ℕ, x p.1 p.2 = ∑' m, ∑' n, x n m
```

## Exercise 0.0.2

An `example` ([line 236](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Notation.lean#L236)). Proved here.

> Exercise 0.0.2 (Tonelli's theorem for series over arbitrary sets).

```lean
example {A B:Type*} (x: A → B → ENNReal) : ∑' p:A × B, x p.1 p.2 = ∑' a, ∑' b, x a b
```

## Axiom 0.0.4

`Set.choose` (def, [line 251](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Notation.lean#L251)). A definition.

> Axiom 0.0.4 (Axiom of choice).

```lean
noncomputable def Set.choose {A: Type*} {E: A → Type*} (hE: ∀ n, Nonempty (E n)) :
∀ n, E n
```

## Corollary 0.0.5

`Countable.choose` (def, [line 255](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Notation.lean#L255)). A definition.

> Corollary 0.0.5 (Axiom of countable choice)

```lean
noncomputable def Countable.choose {E: ℕ → Type*} (hE: ∀ n, Nonempty (E n)) :
∀ n, E n
```

## Depends on

Its Lean file imports no other section's file.

## Sources

- [Analysis/MeasureTheory/Notation.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/MeasureTheory/Notation.lean)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/MeasureTheory/Notation.html)
