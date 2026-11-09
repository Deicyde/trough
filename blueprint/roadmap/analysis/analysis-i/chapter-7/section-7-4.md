---
declaration: theorem
origin: cited
lean: Chapter7.Series.converges_of_permute_nonneg, Chapter7.Series.zeta_2_converges, Chapter7.Series.absConverges_of_permute, Chapter7.Series.a_7_4_4, Chapter7.Series.absConverges_of_subseries, Chapter7.Series.absConverges_of_permute'
statement: formalized
---

# Section 7.4: Rearrangement of series

> I have attempted to make the translation as faithful a paraphrasing as possible of the original text.  When there is a choice between a more idiomatic Lean solution and a more faithful translation, I have generally chosen the latter.  In particular, there will be places where the Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided doing so.
>
> Main constructions and results of this section:
>
> - Rearrangement of non-negative or absolutely convergent series.

*Quoted from [Analysis/Section_7_4.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_4.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 6 labelled items, carried by 6 declarations: 1 proved here, 4 stated without proof (2 of them exercises) and 1 definition. It also has 9 declarations with no label, counted here but not shown.

## Proposition 7.4.1

`Chapter7.Series.converges_of_permute_nonneg` (theorem, [line 22](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_4.lean#L22)). Proved here.

> Proposition 7.4.1

```lean
theorem Series.converges_of_permute_nonneg {a:ℕ → ℝ} (ha: (a:Series).nonneg) (hconv: (a:Series).converges)
  {f: ℕ → ℕ} (hf: Function.Bijective f) :
    (fun n ↦ a (f n) : Series).converges ∧ (a:Series).sum = (fun n ↦ a (f n) : Series).sum
```

## Example 7.4.2

`Chapter7.Series.zeta_2_converges` (theorem, [line 110](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_4.lean#L110)). Stated without proof.

> Example 7.4.2

```lean
theorem Series.zeta_2_converges : (fun n:ℕ ↦ 1/(n+1:ℝ)^2 : Series).converges
```

## Proposition 7.4.3

`Chapter7.Series.absConverges_of_permute` (theorem, [line 121](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_4.lean#L121)). Stated without proof.

> Proposition 7.4.3 (Rearrangement of series)

```lean
theorem Series.absConverges_of_permute {a:ℕ → ℝ} (ha : (a:Series).absConverges)
  {f: ℕ → ℕ} (hf: Function.Bijective f) :
    (fun n ↦ a (f n):Series).absConverges  ∧ (a:Series).sum = (fun n ↦ a (f n) : Series).sum
```

## Example 7.4.4

`Chapter7.Series.a_7_4_4` (abbrev, [line 191](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_4.lean#L191)). A definition.

> Example 7.4.4

```lean
noncomputable abbrev Series.a_7_4_4 : ℕ → ℝ
```

## Exercise 7.4.1

`Chapter7.Series.absConverges_of_subseries` (theorem, [line 206](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_4.lean#L206)). An exercise, stated without proof.

> Exercise 7.4.1

```lean
theorem Series.absConverges_of_subseries {a:ℕ → ℝ} (ha: (a:Series).absConverges) {f: ℕ → ℕ} (hf: StrictMono f) :
  (fun n ↦ a (f n):Series).absConverges
```

## Exercise 7.4.2

`Chapter7.Series.absConverges_of_permute'` (theorem, [line 214](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_4.lean#L214)). An exercise, stated without proof.

> Exercise 7.4.2 : reprove Proposition 7.4.3 using Proposition 7.4.1, Proposition 7.2.14,
> and expressing `a n` as the difference of `a n + |a n|` and `|a n|`.

```lean
theorem Series.absConverges_of_permute' {a:ℕ → ℝ} (ha : (a:Series).absConverges)
  {f: ℕ → ℕ} (hf: Function.Bijective f) :
    (fun n ↦ a (f n):Series).absConverges  ∧ (a:Series).sum = (fun n ↦ a (f n):Series).sum
```

## Depends on

- [Section 7.3: Sums of non-negative numbers](section-7-3.md)

## Sources

- [Analysis/Section_7_4.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_4.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_7_4/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_7_4.html)
