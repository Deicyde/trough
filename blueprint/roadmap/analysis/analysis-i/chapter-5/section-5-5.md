---
declaration: theorem
origin: cited
lean: Chapter5.Real.upperBound_def, Chapter5.Real.isLUB_def, Chapter5.Real.LUB_unique, Chapter5.Real.upperBound_between, Chapter5.Real.upperBound_discrete_unique, Chapter5.Real.LIM_of_Cauchy, Chapter5.Real.LUB_exist, Chapter5.ExtendedReal.sup, Chapter5.ExtendedReal.sup_of_empty, Chapter5.ExtendedReal.sup_of_unbounded, Chapter5.ExtendedReal.sup_of_bounded, Chapter5.Real.exist_sqrt_two, Chapter5.Real.exist_irrational, Chapter5.Real.inf_neg, Chapter5.Real.irrat_between
statement: formalized
---

# Section 5.5: The least upper bound property

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text.  When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter.  In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Upper bound and least upper bound on the real line
>
> ## Tips from past users
>
> Users of the companion who have completed the exercises in this section are welcome to send their tips for future users in this section as PRs.
>
> - (Add tip here)

*Quoted from [Analysis/Section_5_5.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_5.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 17 labelled items, carried by 20 declarations: 7 proved here, 12 stated without proof (5 of them exercises) and 1 definition. It also has 33 declarations with no label, counted here but not shown.

## Definition 5.5.1

`Chapter5.Real.upperBound_def` (theorem, [line 29](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_5.lean#L29)). Proved here.

> Definition 5.5.1 (upper bounds). Here we use the `upperBounds` set defined in Mathlib.

```lean
theorem Real.upperBound_def (E: Set Real) (M: Real) : M ∈ upperBounds E ↔ ∀ x ∈ E, x ≤ M
```

## Example 5.5.2

An `example` ([line 42](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_5.lean#L42)). Stated without proof.

> Example 5.5.2

```lean
example (M: Real) : M ∈ upperBounds (.Icc 0 1) ↔ M ≥ 1
```

## Example 5.5.3

An `example` ([line 48](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_5.lean#L48)). Stated without proof.

> Example 5.5.3

```lean
example : ¬ ∃ M : Real, M ∈ upperBounds (.Ioi 0)
```

## Example 5.5.4

An `example` ([line 51](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_5.lean#L51)). Stated without proof.

> Example 5.5.4

```lean
example : ∀ M, M ∈ upperBounds (∅ : Set Real)
```

## Definition 5.5.5

`Chapter5.Real.isLUB_def` (theorem, [line 57](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_5.lean#L57)). Proved here.

> Definition 5.5.5 (least upper bound).  Here we use the `IsLUB` predicate defined in Mathlib.

```lean
theorem Real.isLUB_def (E: Set Real) (M: Real) :
    IsLUB E M ↔ M ∈ upperBounds E ∧ ∀ M' ∈ upperBounds E, M' ≥ M
```

## Example 5.5.6

An `example` ([line 64](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_5.lean#L64)). Stated without proof.

> Example 5.5.6

```lean
example : IsLUB (.Icc 0 1) (1 : Real)
```

## Example 5.5.7

An `example` ([line 67](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_5.lean#L67)). Stated without proof.

> Example 5.5.7

```lean
example : ¬∃ M, IsLUB (∅: Set Real) M
```

## Proposition 5.5.8

`Chapter5.Real.LUB_unique` (theorem, [line 70](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_5.lean#L70)). Proved here.

> Proposition 5.5.8 (Uniqueness of least upper bound).

```lean
theorem Real.LUB_unique {E: Set Real} {M M': Real} (h1: IsLUB E M) (h2: IsLUB E M') : M = M'
```

## Exercise 5.5.2

`Chapter5.Real.upperBound_between` (theorem, [line 79](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_5.lean#L79)). An exercise, stated without proof.

> Exercise 5.5.2

```lean
theorem Real.upperBound_between {E: Set Real} {n:ℕ} {L K:ℤ} (hLK: L < K)
  (hK: K*((1/(n+1):ℚ):Real) ∈ upperBounds E) (hL: L*((1/(n+1):ℚ):Real) ∉ upperBounds E) :
    ∃ m, L < m
    ∧ m ≤ K
    ∧ m*((1/(n+1):ℚ):Real) ∈ upperBounds E
    ∧ (m-1)*((1/(n+1):ℚ):Real) ∉ upperBounds E
```

## Exercise 5.5.3

`Chapter5.Real.upperBound_discrete_unique` (theorem, [line 87](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_5.lean#L87)). An exercise, stated without proof.

> Exercise 5.5.3

```lean
theorem Real.upperBound_discrete_unique {E: Set Real} {n:ℕ} {m m':ℤ}
  (hm1: (((m:ℚ) / (n+1):ℚ):Real) ∈ upperBounds E)
  (hm2: (((m:ℚ) / (n+1) - 1 / (n+1):ℚ):Real) ∉ upperBounds E)
  (hm'1: (((m':ℚ) / (n+1):ℚ):Real) ∈ upperBounds E)
  (hm'2: (((m':ℚ) / (n+1) - 1 / (n+1):ℚ):Real) ∉ upperBounds E) :
    m = m'
```

## Exercise 5.5.4

`Chapter5.Real.LIM_of_Cauchy` (theorem, [line 110](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_5.lean#L110)). An exercise, stated without proof.

> Exercise 5.5.4

```lean
theorem Real.LIM_of_Cauchy {q:ℕ → ℚ} (hq: ∀ M, ∀ n ≥ M, ∀ n' ≥ M, |q n - q n'| ≤ 1 / (M+1)) :
    (q:Sequence).IsCauchy ∧ ∀ M, |q M - LIM q| ≤ 1 / (M+1)
```

## Theorem 5.5.9

`Chapter5.Real.LUB_exist` (theorem, [line 166](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_5.lean#L166)). Proved here.

> Theorem 5.5.9 (Existence of least upper bound).

```lean
theorem Real.LUB_exist {E: Set Real} (hE: Set.Nonempty E) (hbound: BddAbove E): ∃ S, IsLUB E S
```

## Definition 5.5.10

`Chapter5.ExtendedReal.sup` (abbrev, [line 226](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_5.lean#L226)). A definition.

> Definition 5.5.10 (Supremum).

```lean
noncomputable abbrev ExtendedReal.sup (E: Set Real) : ExtendedReal
```

`Chapter5.ExtendedReal.sup_of_empty` (theorem, [line 230](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_5.lean#L230)). Proved here.

> Definition 5.5.10 (Supremum of empty set).

```lean
theorem ExtendedReal.sup_of_empty : sup ∅ = ⊥
```

`Chapter5.ExtendedReal.sup_of_unbounded` (theorem, [line 233](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_5.lean#L233)). Proved here.

> Definition 5.5.10 (Supremum of unbounded set).

```lean
theorem ExtendedReal.sup_of_unbounded {E: Set Real} (hb: ¬ BddAbove E) : sup E = ⊤
```

`Chapter5.ExtendedReal.sup_of_bounded` (theorem, [line 238](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_5.lean#L238)). Proved here.

> Definition 5.5.10 (Supremum of bounded set).

```lean
theorem ExtendedReal.sup_of_bounded {E: Set Real} (hnon: E.Nonempty) (hb: BddAbove E) :
    IsLUB E (sup E)
```

## Proposition 5.5.12

`Chapter5.Real.exist_sqrt_two` (theorem, [line 246](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_5.lean#L246)). Stated without proof.

> Proposition 5.5.12

```lean
theorem Real.exist_sqrt_two : ∃ x:Real, x^2 = 2
```

## Remark 5.5.13

`Chapter5.Real.exist_irrational` (theorem, [line 302](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_5.lean#L302)). Stated without proof.

> Remark 5.5.13

```lean
theorem Real.exist_irrational : ∃ x:Real, ¬ ∃ q:ℚ, x = (q:Real)
```

## Exercise 5.5.1

`Chapter5.Real.inf_neg` (theorem, [line 308](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_5.lean#L308)). An exercise, stated without proof.

> Exercise 5.5.1

```lean
theorem Real.inf_neg {E: Set Real} {M:Real} (h: IsLUB E M) : IsGLB (-E) (-M)
```

## Exercise 5.5.5

`Chapter5.Real.irrat_between` (theorem, [line 330](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_5.lean#L330)). An exercise, stated without proof.

> Exercise 5.5.5

```lean
theorem Real.irrat_between {x y:Real} (hxy: x < y) :
    ∃ z, x < z ∧ z < y ∧ ¬ ∃ q:ℚ, z = (q:Real)
```

## Depends on

- [Section 5.4: Ordering the reals](section-5-4.md)

## Sources

- [Analysis/Section_5_5.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_5_5.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_5_5/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_5_5.html)
