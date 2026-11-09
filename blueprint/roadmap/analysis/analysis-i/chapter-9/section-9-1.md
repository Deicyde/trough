---
declaration: abbrev
origin: cited
lean: Real.adherent', Chapter9.AdherentPt, Chapter9.closure_def, Chapter9.subset_closure, Chapter9.closure_union, Chapter9.closure_inter, Chapter9.closure_subset, Chapter9.closure_of_subset_closure, Chapter9.closure_of_Ioo, Chapter9.closure_of_N, Chapter9.closure_of_Z, Chapter9.closure_of_Q, Chapter9.limit_of_AdherentPt, Chapter9.isClosed_def, Chapter9.Icc_closed, Chapter9.Ici_closed, Chapter9.Iic_closed, Chapter9.R_closed, Chapter9.Ico_not_closed, Chapter9.Ioc_not_closed, Chapter9.Ioo_not_closed, Chapter9.Ioi_not_closed, Chapter9.Iio_not_closed, Chapter9.N_closed, Chapter9.Z_closed, Chapter9.Q_not_closed, Chapter9.isClosed_iff_limits_mem, Chapter9.LimitPt, Chapter9.IsolatedPt, Chapter9.LimitPt.iff_limit, Chapter9.mem_Icc_isLimit, Chapter9.isBounded_def, Chapter9.Icc_bounded, Chapter9.Ici_unbounded, Chapter9.N_unbounded, Chapter9.Z_unbounded, Chapter9.Q_unbounded, Chapter9.R_unbounded, Chapter9.Heine_Borel
statement: formalized
---

# Section 9.1: Subsets of the real line

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text.  When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter.  In particular, there will be places where
> the Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Review of Mathlib intervals.
> - Adherent points, limit points, isolated points.
> - Closed sets and closure.
> - The Heine-Borel theorem for the real line.

*Quoted from [Analysis/Section_9_1.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 32 labelled items, carried by 54 declarations: 5 proved here, 45 stated without proof (22 of them exercises) and 4 definitions. It also has 21 declarations and 10 examples with no label, counted here but not shown.

## Example 9.1.4

An `example` ([line 44](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L44)). Stated without proof.

> Example 9.1.4

```lean
example {a b: EReal} (h: a > b) : Set.Icc a b = ∅
```

## Definition 9.1.5

`Real.adherent'` (abbrev, [line 63](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L63)). A definition.

> Definition 9.1.5.  Note that a slightly different `Real.Adherent` was defined in
> Chapter 6.4

```lean
abbrev Real.adherent' (ε:ℝ) (x:ℝ) (X: Set ℝ)
```

## Example 9.1.7

An `example` ([line 66](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L66)). Stated without proof.

> Example 9.1.7

```lean
example : (0.5:ℝ).adherent' 1.1 (.Ioo 0 1)
```

## Definition 9.1.8

`Chapter9.AdherentPt` (abbrev, [line 76](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L76)). A definition.

> Definition 9.1.8 (Adherent points).

```lean
abbrev AdherentPt (x:ℝ) (X:Set ℝ)
```

## Definition 9.1.10

`Chapter9.closure_def` (theorem, [line 83](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L83)). Proved here.

> Definition 9.1.10 (Closure).  Here we identify this definition with the Mathlib version.

```lean
theorem closure_def (X:Set ℝ) : closure X = { x | AdherentPt x X }
```

## Lemma 9.1.11 / Exercise 9.1.1

`Chapter9.subset_closure` (theorem, [line 96](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L96)). An exercise, stated without proof.

> Lemma 9.1.11 / Exercise 9.1.1 (subset)

```lean
theorem subset_closure (X:Set ℝ): X ⊆ closure X
```

`Chapter9.closure_union` (theorem, [line 99](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L99)). An exercise, stated without proof.

> Lemma 9.1.11 / Exercise 9.1.1 (union)

```lean
theorem closure_union (X Y:Set ℝ): closure (X ∪ Y) = closure X ∪ closure Y
```

`Chapter9.closure_inter` (theorem, [line 102](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L102)). An exercise, stated without proof.

> Lemma 9.1.11 / Exercise 9.1.1 (inter)

```lean
theorem closure_inter (X Y:Set ℝ): closure (X ∩ Y) ⊆ closure X ∩ closure Y
```

`Chapter9.closure_subset` (theorem, [line 105](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L105)). An exercise, stated without proof.

> Lemma 9.1.11 / Exercise 9.1.1 (monotonicity)

```lean
theorem closure_subset {X Y:Set ℝ} (h: X ⊆ Y): closure X ⊆ closure Y
```

`Chapter9.closure_of_subset_closure` (theorem, [line 108](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L108)). An exercise, stated without proof.

> Lemma 9.1.11 / Exercise 9.1.1 (sandwich)

```lean
theorem closure_of_subset_closure {X Y:Set ℝ} (h: X ⊆ Y) (h' : Y ⊆ closure X): closure Y = closure X
```

## Lemma 9.1.12

`Chapter9.closure_of_Ioo` (theorem, [line 111](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L111)). Stated without proof.

> Lemma 9.1.12

```lean
theorem closure_of_Ioo {a b:ℝ} (h:a < b) : closure (.Ioo a b) = .Icc a b
```

## Lemma 9.1.13 / Exercise 9.1.2

`Chapter9.closure_of_N` (theorem, [line 153](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L153)). An exercise, stated without proof.

> Lemma 9.1.13 / Exercise 9.1.2 (N)

```lean
theorem closure_of_N :
  closure ((fun n:ℕ ↦ (n:ℝ)) '' .univ) = ((fun n:ℕ ↦ (n:ℝ)) '' .univ)
```

`Chapter9.closure_of_Z` (theorem, [line 158](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L158)). An exercise, stated without proof.

> Lemma 9.1.13 / Exercise 9.1.2 (Z)

```lean
theorem closure_of_Z :
  closure ((fun n:ℤ ↦ (n:ℝ)) '' .univ) = ((fun n:ℤ ↦ (n:ℝ)) '' .univ)
```

`Chapter9.closure_of_Q` (theorem, [line 163](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L163)). An exercise, stated without proof.

> Lemma 9.1.13 / Exercise 9.1.2 (Q)

```lean
theorem closure_of_Q :
  closure ((fun n:ℚ ↦ (n:ℝ)) '' .univ) = .univ
```

## Lemma 9.1.14 / Exercise 9.1.4

`Chapter9.limit_of_AdherentPt` (theorem, [line 168](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L168)). An exercise, stated without proof.

> Lemma 9.1.14 / Exercise 9.1.4

```lean
theorem limit_of_AdherentPt (X: Set ℝ) (x:ℝ) :
  AdherentPt x X ↔ ∃ a : ℕ → ℝ, (∀ n, a n ∈ X) ∧ Filter.atTop.Tendsto a (nhds x)
```

## Definition 9.1.15

`Chapter9.isClosed_def` (theorem, [line 176](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L176)). Proved here.

> Definition 9.1.15.  Here we use the Mathlib definition.

```lean
theorem isClosed_def (X:Set ℝ): IsClosed X ↔ closure X = X
```

## Examples 9.1.16

`Chapter9.Icc_closed` (theorem, [line 183](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L183)). Stated without proof.

> Examples 9.1.16 (Icc)

```lean
theorem Icc_closed {a b:ℝ} : IsClosed (.Icc a b)
```

`Chapter9.Ici_closed` (theorem, [line 186](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L186)). Stated without proof.

> Examples 9.1.16 (Ici)

```lean
theorem Ici_closed (a:ℝ) : IsClosed (.Ici a)
```

`Chapter9.Iic_closed` (theorem, [line 189](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L189)). Stated without proof.

> Examples 9.1.16 (Iic)

```lean
theorem Iic_closed (a:ℝ) : IsClosed (.Iic a)
```

`Chapter9.R_closed` (theorem, [line 192](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L192)). Stated without proof.

> Examples 9.1.16 (R)

```lean
theorem R_closed : IsClosed (.univ : Set ℝ)
```

`Chapter9.Ico_not_closed` (theorem, [line 195](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L195)). Stated without proof.

> Examples 9.1.16 (Ico)

```lean
theorem Ico_not_closed {a b:ℝ} (h: a < b) : ¬ IsClosed (.Ico a b)
```

`Chapter9.Ioc_not_closed` (theorem, [line 198](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L198)). Stated without proof.

> Examples 9.1.16 (Ioc)

```lean
theorem Ioc_not_closed {a b:ℝ} (h: a < b) : ¬ IsClosed (.Ioc a b)
```

`Chapter9.Ioo_not_closed` (theorem, [line 201](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L201)). Stated without proof.

> Examples 9.1.16 (Ioo)

```lean
theorem Ioo_not_closed {a b:ℝ} (h: a < b) : ¬ IsClosed (.Ioo a b)
```

`Chapter9.Ioi_not_closed` (theorem, [line 204](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L204)). Stated without proof.

> Examples 9.1.16 (Ioi)

```lean
theorem Ioi_not_closed (a:ℝ) : ¬ IsClosed (.Ioi a)
```

`Chapter9.Iio_not_closed` (theorem, [line 207](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L207)). Stated without proof.

> Examples 9.1.16 (Iio)

```lean
theorem Iio_not_closed (a:ℝ) : ¬ IsClosed (.Iio a)
```

`Chapter9.N_closed` (theorem, [line 210](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L210)). Stated without proof.

> Examples 9.1.16 (N)

```lean
theorem N_closed : IsClosed ((fun n:ℕ ↦ (n:ℝ)) '' .univ)
```

`Chapter9.Z_closed` (theorem, [line 213](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L213)). Stated without proof.

> Examples 9.1.16 (Z)

```lean
theorem Z_closed : IsClosed ((fun n:ℤ ↦ (n:ℝ)) '' .univ)
```

`Chapter9.Q_not_closed` (theorem, [line 216](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L216)). Stated without proof.

> Examples 9.1.16 (Q)

```lean
theorem Q_not_closed : ¬ IsClosed ((fun n:ℚ ↦ (n:ℝ)) '' .univ)
```

## Corollary 9.1.17

`Chapter9.isClosed_iff_limits_mem` (theorem, [line 219](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L219)). Proved here.

> Corollary 9.1.17

```lean
theorem isClosed_iff_limits_mem (X: Set ℝ) :
  IsClosed X ↔ ∀ (a:ℕ → ℝ) (L:ℝ), (∀ n, a n ∈ X) → Filter.atTop.Tendsto a (nhds L) → L ∈ X
```

## Definition 9.1.18

`Chapter9.LimitPt` (abbrev, [line 227](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L227)). A definition.

> Definition 9.1.18 (Limit points)

```lean
abbrev LimitPt (x:ℝ) (X: Set ℝ)
```

## Definition 9.1.19

`Chapter9.IsolatedPt` (abbrev, [line 234](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L234)). A definition.

> Definition 9.1.19 (Isolated points).

```lean
abbrev IsolatedPt (x:ℝ) (X: Set ℝ)
```

## Example 9.1.19

An `example` ([line 237](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L237)). Stated without proof.

> Example 9.1.19

```lean
example : AdherentPt 3 ((.Ioo 1 2) ∪ {3})
```

## Remark 9.1.20

`Chapter9.LimitPt.iff_limit` (theorem, [line 244](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L244)). Proved here.

> Remark 9.1.20

```lean
theorem LimitPt.iff_limit (x:ℝ) (X: Set ℝ) :
  LimitPt x X ↔ ∃ a : ℕ → ℝ, (∀ n, a n ∈ X \ {x}) ∧ Filter.atTop.Tendsto a (nhds x)
```

## Lemma 9.1.21

`Chapter9.mem_Icc_isLimit` (theorem, [line 249](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L249)). Stated without proof.

> Lemma 9.1.21

```lean
theorem mem_Icc_isLimit {a b x:ℝ} (h: a < b) (hx: x ∈ Set.Icc a b) : LimitPt x (.Icc a b)
```

## Definition 9.1.22

`Chapter9.isBounded_def` (theorem, [line 295](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L295)). Proved here.

> Definition 9.1.22.  We use here Mathlib's `Bornology.IsBounded`

```lean
theorem isBounded_def (X: Set ℝ) : Bornology.IsBounded X ↔ ∃ M > 0, X ⊆ .Icc (-M) M
```

## Example 9.1.23

`Chapter9.Icc_bounded` (theorem, [line 304](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L304)). Stated without proof.

> Example 9.1.23 (Icc)

```lean
theorem Icc_bounded (a b:ℝ) : Bornology.IsBounded (.Icc a b)
```

`Chapter9.Ici_unbounded` (theorem, [line 307](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L307)). Stated without proof.

> Example 9.1.23 (Ici)

```lean
theorem Ici_unbounded (a: ℝ) : ¬ Bornology.IsBounded (.Ici a)
```

`Chapter9.N_unbounded` (theorem, [line 310](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L310)). Stated without proof.

> Example 9.1.23 (N)

```lean
theorem N_unbounded : ¬ Bornology.IsBounded ((fun n:ℕ ↦ (n:ℝ)) '' .univ)
```

`Chapter9.Z_unbounded` (theorem, [line 313](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L313)). Stated without proof.

> Example 9.1.23 (Z)

```lean
theorem Z_unbounded : ¬ Bornology.IsBounded ((fun n:ℤ ↦ (n:ℝ)) '' .univ)
```

`Chapter9.Q_unbounded` (theorem, [line 316](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L316)). Stated without proof.

> Example 9.1.23 (Q)

```lean
theorem Q_unbounded : ¬ Bornology.IsBounded ((fun n:ℚ ↦ (n:ℝ)) '' .univ)
```

`Chapter9.R_unbounded` (theorem, [line 319](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L319)). Stated without proof.

> Example 9.1.23 (R)

```lean
theorem R_unbounded : ¬ Bornology.IsBounded (.univ: Set ℝ)
```

## Theorem 9.1.24 / Exercise 9.1.13

`Chapter9.Heine_Borel` (theorem, [line 322](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L322)). An exercise, stated without proof.

> Theorem 9.1.24 / Exercise 9.1.13 (Heine-Borel theorem for the line).

```lean
theorem Heine_Borel (X: Set ℝ) :
  IsClosed X ∧ Bornology.IsBounded X ↔ ∀ a : ℕ → ℝ, (∀ n, a n ∈ X) →
  (∃ n : ℕ → ℕ, StrictMono n
    ∧ ∃ L ∈ X, Filter.atTop.Tendsto (fun j ↦ a (n j)) (nhds L))
```

## Exercise 9.1.3

An `example` ([line 329](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L329)). An exercise, stated without proof.

> Exercise 9.1.3

```lean
example : ∃ (X Y:Set ℝ), closure (X ∩ Y) ≠ closure X ∩ closure Y
```

## Exercise 9.1.5

An `example` ([line 333](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L333)). An exercise, stated without proof.

> Exercise 9.1.5

```lean
example (X:Set ℝ) : IsClosed (closure X)
```

## Exercise 9.1.6

An `example` ([line 337](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L337)). An exercise, stated without proof.

> Exercise 9.1.6

```lean
example {X Y:Set ℝ} (hY: IsClosed Y) (hXY: X ⊆ Y) : closure X ⊆ Y
```

## Exercise 9.1.7

An `example` ([line 341](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L341)). An exercise, stated without proof.

> Exercise 9.1.7

```lean
example {n:ℕ} (X: Fin n → Set ℝ) (hX: ∀ i, IsClosed (X i)) :
  IsClosed (⋃ i, X i)
```

## Exercise 9.1.8

An `example` ([line 346](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L346)). An exercise, stated without proof.

> Exercise 9.1.8

```lean
example {I:Type} (X: I → Set ℝ) (hX: ∀ i, IsClosed (X i)) :
  IsClosed (⋂ i, X i)
```

## Exercise 9.1.9 (i)

An `example` ([line 351](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L351)). An exercise, stated without proof.

> Exercise 9.1.9 (i)

```lean
example {X:Set ℝ} {x:ℝ} (hx: AdherentPt x X) : LimitPt x X ∨ IsolatedPt x X
```

## Exercise 9.1.9 (ii)

An `example` ([line 355](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L355)). An exercise, stated without proof.

> Exercise 9.1.9 (ii)

```lean
example {X:Set ℝ} {x:ℝ} : ¬ (LimitPt x X ∧ IsolatedPt x X)
```

## Exercise 9.1.10

An `example` ([line 359](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L359)). An exercise, stated without proof.

> Exercise 9.1.10

```lean
example {X:Set ℝ} (hX: X ≠ ∅) : Bornology.IsBounded X ↔
  sSup ((fun x:ℝ ↦ (x:EReal)) '' X) < ⊤ ∧
  sInf ((fun x:ℝ ↦ (x:EReal)) '' X) > ⊥
```

## Exercise 9.1.11

An `example` ([line 365](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L365)). An exercise, stated without proof.

> Exercise 9.1.11

```lean
example {X:Set ℝ} (hX: Bornology.IsBounded X) : Bornology.IsBounded (closure X)
```

## Exercise 9.1.12

An `example` ([line 369](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L369)). An exercise, stated without proof.

> Exercise 9.1.12.  As a followup: prove or disprove this exercise with `[Fintype I]` removed.

```lean
example {I:Type} [Fintype I] (X: I → Set ℝ) (hX: ∀ i, Bornology.IsBounded (X i)) :
  Bornology.IsBounded (⋃ i, X i)
```

## Exercise 9.1.14

An `example` ([line 374](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L374)). An exercise, stated without proof.

> Exercise 9.1.14

```lean
example (I: Finset ℝ) : IsClosed (I:Set ℝ) ∧ Bornology.IsBounded (I:Set ℝ)
```

## Exercise 9.1.15

An `example` ([line 378](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean#L378)). An exercise, stated without proof.

> Exercise 9.1.15

```lean
example {E:Set ℝ} (hE: Bornology.IsBounded E) (hnon: E.Nonempty): AdherentPt (sSup E) E ∧ AdherentPt (sSup E) Eᶜ
```

## Depends on

- [Section 6.4: Limsup, liminf, and limit points](../chapter-6/section-6-4.md)

## Sources

- [Analysis/Section_9_1.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_9_1.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_9_1/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_9_1.html)
