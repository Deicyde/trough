---
declaration: theorem
origin: cited
lean: Chapter7.Series.root_test_pos, Chapter7.Series.root_test_neg, Chapter7.Series.root_test_inconclusive, Chapter7.Series.root_test_inconclusive', Chapter7.Series.ratio_ineq, Chapter7.Series.ratio_test_pos, Chapter7.Series.ratio_test_neg, Chapter7.Series.ratio_test_inconclusive, Chapter7.Series.ratio_test_inconclusive', Chapter7.Series.root_self_converges, Chapter7.Series.poly_mul_geom_converges
statement: formalized
---

# Section 7.5: The root and ratio tests

> I have attempted to make the translation as faithful a paraphrasing as possible of the original text.  When there is a choice between a more idiomatic Lean solution and a more faithful translation, I have generally chosen the latter.  In particular, there will be places where the Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided doing so.
>
> Main constructions and results of this section:
>
> - The root and ratio tests/
>
> A point that is only implicitly stated in the text is that for the root and ratio tests, the lim inf and lim sup should be interpreted within the extended reals.  The Lean formalizations below make this point more explicit.

*Quoted from [Analysis/Section_7_5.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_5.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 10 labelled items, carried by 11 declarations: 4 proved here and 7 stated without proof (6 of them exercises).

## Theorem 7.5.1(a)

`Chapter7.Series.root_test_pos` (theorem, [line 25](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_5.lean#L25)). Proved here.

> Theorem 7.5.1(a) (Root test).  A technical condition is needed to ensure the limsup is finite.

```lean
theorem Series.root_test_pos {s : Series}
  (h : atTop.limsup (fun n ↦ ((|s.seq n|^(1/(n:ℝ)):ℝ):EReal)) < 1) : s.absConverges
```

## Theorem 7.5.1(b)

`Chapter7.Series.root_test_neg` (theorem, [line 78](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_5.lean#L78)). Proved here.

> Theorem 7.5.1(b) (Root test)

```lean
theorem Series.root_test_neg {s : Series}
  (h : atTop.limsup (fun n ↦ ((|s.seq n|^(1/(n:ℝ)):ℝ):EReal)) > 1) : s.diverges
```

## Theorem 7.5.1(c) / Exercise 7.5.3

`Chapter7.Series.root_test_inconclusive` (theorem, [line 90](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_5.lean#L90)). An exercise, stated without proof.

> Theorem 7.5.1(c) (Root test) / Exercise 7.5.3

```lean
theorem Series.root_test_inconclusive: ∃ s:Series,
  atTop.Tendsto (fun n ↦ |s.seq n|^(1/(n:ℝ))) (nhds 1) ∧ s.diverges
```

## Theorem 7.5.1 / Exercise 7.5.3

`Chapter7.Series.root_test_inconclusive'` (theorem, [line 95](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_5.lean#L95)). An exercise, stated without proof.

> Theorem 7.5.1 (Root test) / Exercise 7.5.3

```lean
theorem Series.root_test_inconclusive' : ∃ s:Series,
  atTop.Tendsto (fun n ↦ |s.seq n|^(1/(n:ℝ))) (nhds 1) ∧ s.absConverges
```

## Lemma 7.5.2 / Exercise 7.5.1

`Chapter7.Series.ratio_ineq` (theorem, [line 100](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_5.lean#L100)). An exercise, stated without proof.

> Lemma 7.5.2 / Exercise 7.5.1

```lean
theorem Series.ratio_ineq {c:ℤ → ℝ} (m:ℤ) (hpos: ∀ n ≥ m, c n > 0) :
  atTop.liminf (fun n ↦ ((c (n+1) / c n:ℝ):EReal)) ≤
    atTop.liminf (fun n ↦ ↑((c n)^(1/(n:ℝ)):ℝ))
  ∧ atTop.liminf (fun n ↦ (((c n)^(1/(n:ℝ)):ℝ):EReal)) ≤
    atTop.limsup (fun n ↦ ↑((c n)^(1/(n:ℝ)):ℝ))
  ∧ atTop.limsup (fun n ↦ (((c n)^(1/(n:ℝ)):ℝ):EReal)) ≤
    atTop.limsup (fun n ↦ ↑(c (n+1) / c n:ℝ))
```

## Corollary 7.5.3

`Chapter7.Series.ratio_test_pos` (theorem, [line 179](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_5.lean#L179)). Proved here.

> Corollary 7.5.3 (Ratio test, convergence).

```lean
theorem Series.ratio_test_pos {s : Series} (hnon: ∀ n ≥ s.m, s.seq n ≠ 0)
  (h : atTop.limsup (fun n ↦ ((|s.seq (n+1)| / |s.seq n|:ℝ):EReal)) < 1) : s.absConverges
```

`Chapter7.Series.ratio_test_neg` (theorem, [line 187](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_5.lean#L187)). Proved here.

> Corollary 7.5.3 (Ratio test, divergence).

```lean
theorem Series.ratio_test_neg {s : Series} (hnon: ∀ n ≥ s.m, s.seq n ≠ 0)
  (h : atTop.liminf (fun n ↦ ((|s.seq (n+1)| / |s.seq n|:ℝ):EReal)) > 1) : s.diverges
```

## Corollary 7.5.3(i) / Exercise 7.5.3

`Chapter7.Series.ratio_test_inconclusive` (theorem, [line 194](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_5.lean#L194)). An exercise, stated without proof.

> Corollary 7.5.3(i) (Ratio test inconclusive, diverges) / Exercise 7.5.3

```lean
theorem Series.ratio_test_inconclusive: ∃ s:Series, (∀ n ≥ s.m, s.seq n ≠ 0) ∧
  atTop.Tendsto (fun n ↦ |s.seq (n+1)| / |s.seq n|) (nhds 1) ∧ s.diverges
```

## Corollary 7.5.3(ii) / Exercise 7.5.3

`Chapter7.Series.ratio_test_inconclusive'` (theorem, [line 199](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_5.lean#L199)). An exercise, stated without proof.

> Corollary 7.5.3(ii) (Ratio test inconclusive, absConverges) / Exercise 7.5.3

```lean
theorem Series.ratio_test_inconclusive' : ∃ s:Series, (∀ n ≥ s.m, s.seq n ≠ 0) ∧
  atTop.Tendsto (fun n ↦ |s.seq (n+1)| / |s.seq n|) (nhds 1) ∧ s.absConverges
```

## Proposition 7.5.4

`Chapter7.Series.root_self_converges` (theorem, [line 204](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_5.lean#L204)). Stated without proof.

> Proposition 7.5.4

```lean
theorem Series.root_self_converges : atTop.Tendsto (fun (n:ℕ) ↦ (n:ℝ)^(1 / (n:ℝ))) (nhds 1)
```

## Exercise 7.5.2

`Chapter7.Series.poly_mul_geom_converges` (theorem, [line 208](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_5.lean#L208)). An exercise, stated without proof.

> Exercise 7.5.2

```lean
theorem Series.poly_mul_geom_converges {x:ℝ} (hx: |x|<1) (q:ℝ) : (fun n:ℕ ↦ (n:ℝ)^q * x^n : Series).converges
  ∧ atTop.Tendsto (fun n:ℕ ↦ (n:ℝ)^q * x^n) (nhds 0)
```

## Depends on

- [Section 6.4: Limsup, liminf, and limit points](../chapter-6/section-6-4.md)
- [Section 7.4: Rearrangement of series](section-7-4.md)

## Sources

- [Analysis/Section_7_5.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_5.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_7_5/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_7_5.html)
