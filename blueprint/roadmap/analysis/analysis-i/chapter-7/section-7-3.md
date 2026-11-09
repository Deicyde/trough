---
declaration: theorem
origin: cited
lean: Chapter7.Series.converges_of_nonneg_iff, Chapter7.Series.converges_of_le, Chapter7.Series.converges_geom, Chapter7.Series.cauchy_criterion, Chapter7.Series.converges_qseries, Chapter7.Series.zeta_eq, Chapter7.Series.nonneg_sum_zero
statement: formalized
---

# Section 7.3: Sums of non-negative numbers

> I have attempted to make the translation as faithful a paraphrasing as possible of the original text.  When there is a choice between a more idiomatic Lean solution and a more faithful translation, I have generally chosen the latter.  In particular, there will be places where the Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided doing so.
>
> Main constructions and results of this section:
>
> - Equivalent characterizations of convergence of nonnegative series.
> - Cauchy condensation test.

*Quoted from [Analysis/Section_7_3.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_3.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 7 labelled items, carried by 7 declarations: 4 proved here and 3 stated without proof (3 of them exercises). It also has 11 declarations with no label, counted here but not shown.

## Proposition 7.3.1

`Chapter7.Series.converges_of_nonneg_iff` (theorem, [line 30](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_3.lean#L30)). Proved here.

> Proposition 7.3.1

```lean
theorem Series.converges_of_nonneg_iff {s: Series} (h: s.nonneg) : s.converges ↔ ∃ M, ∀ N, s.partial N ≤ M
```

## Corollary 7.3.2 / Exercise 7.3.1

`Chapter7.Series.converges_of_le` (theorem, [line 68](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_3.lean#L68)). An exercise, stated without proof.

> Corollary 7.3.2 (Comparison test) / Exercise 7.3.1

```lean
theorem Series.converges_of_le {s t: Series} (hm: s.m = t.m) (hcomp: ∀ n ≥ s.m, |s.seq n| ≤ t.seq n) (hconv : t.converges) : s.absConverges ∧ |s.sum| ≤ s.abs.sum ∧ s.abs.sum ≤ t.sum
```

## Lemma 7.3.3 / Exercise 7.3.2

`Chapter7.Series.converges_geom` (theorem, [line 73](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_3.lean#L73)). An exercise, stated without proof.

> Lemma 7.3.3 (Geometric series) / Exercise 7.3.2

```lean
theorem Series.converges_geom {x: ℝ} (hx: |x| < 1) : (fun n ↦ x ^ n : Series).convergesTo (1 / (1 - x))
```

## Proposition 7.3.4

`Chapter7.Series.cauchy_criterion` (theorem, [line 82](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_3.lean#L82)). Proved here.

> Proposition 7.3.4 (Cauchy criterion)

```lean
theorem Series.cauchy_criterion {s:Series} (hm: s.m = 1) (hs:s.nonneg) (hmono: ∀ n ≥ 1, s.seq (n+1) ≤ s.seq n) : s.converges ↔ (fun k ↦ 2^k * s.seq (2^k): Series).converges
```

## Corollary 7.3.7

`Chapter7.Series.converges_qseries` (theorem, [line 145](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_3.lean#L145)). Proved here.

> Corollary 7.3.7

```lean
theorem Series.converges_qseries (q: ℝ) (hq: q > 0) : (mk' (m := 1) fun n ↦ 1 / (n:ℝ) ^ q : Series).converges ↔ (q>1)
```

## Remark 7.3.8

`Chapter7.Series.zeta_eq` (theorem, [line 166](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_3.lean#L166)). Proved here.

> Remark 7.3.8

```lean
theorem Series.zeta_eq {q:ℝ} (hq: q > 1) : (mk' (m := 1) fun n ↦ 1 / (n:ℝ) ^ q : Series).sum = riemannZeta q
```

## Exercise 7.3.3

`Chapter7.Series.nonneg_sum_zero` (theorem, [line 201](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_3.lean#L201)). An exercise, stated without proof.

> Exercise 7.3.3

```lean
theorem Series.nonneg_sum_zero {a:ℕ → ℝ} (ha: (a:Series).nonneg) (hconv: (a:Series).converges) : (a:Series).sum = 0 ↔ ∀ n, a n = 0
```

## Depends on

- [Section 6.1: Convergence and limit laws](../chapter-6/section-6-1.md)
- [Chapter 6 epilogue: Connections with Mathlib limits](../chapter-6/section-6-epilogue.md)
- [Section 7.2: Infinite series](section-7-2.md)

## Sources

- [Analysis/Section_7_3.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_3.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_7_3/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_7_3.html)
