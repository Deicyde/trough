---
declaration: structure
origin: cited
lean: Chapter7.Series, Chapter7.Series.partial, Chapter7.Series.sum_of_converges, Chapter7.Series.example_7_2_4, Chapter7.Series.converges_iff_tail_decay, Chapter7.Series.decay_of_converges, Chapter7.Series.example_7_2_7, Chapter7.Series.abs, Chapter7.Series.converges_of_absConverges, Chapter7.Series.converges_of_alternating, Chapter7.Series.example_7_2_13, Chapter7.Series.convergesTo.add, Chapter7.Series.convergesTo.smul, Chapter7.Series.converges_from, Chapter7.Series.shift, Chapter7.Series.telescope, Chapter7.Series.exercise_7_2_1_convergent
statement: formalized
---

# Section 7.2: Infinite series

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Formal series and their limits.
> - Absolute convergence; basic series laws.

*Quoted from [Analysis/Section_7_2.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_2.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 17 labelled items, carried by 17 declarations: 1 proved here, 10 stated without proof (8 of them exercises) and 6 definitions (1 with a value left as `sorry`). It also has 39 declarations with no label, counted here but not shown.

## Definition 7.2.1

`Chapter7.Series` (structure, [line 29](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_2.lean#L29)). A definition.

> Definition 7.2.1 (Formal infinite series). This is similar to Chapter 6 sequence, but is
> manipulated differently. As with Chapter 5, we will start series from 0 by default.

```lean
structure Series
```

## Definition 7.2.2

`Chapter7.Series.partial` (abbrev, [line 54](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_2.lean#L54)). A definition.

> Definition 7.2.2 (Convergence of series)

```lean
noncomputable abbrev Series.partial (s : Series) (N:ℤ) : ℝ
```

## Remark 7.2.3

`Chapter7.Series.sum_of_converges` (theorem, [line 80](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_2.lean#L80)). Proved here.

> Remark 7.2.3

```lean
theorem Series.sum_of_converges {s : Series} {L:ℝ} (h: s.convergesTo L) : s.sum = L
```

## Example 7.2.4

`Chapter7.Series.example_7_2_4` (abbrev, [line 91](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_2.lean#L91)). A definition.

> Example 7.2.4

```lean
noncomputable abbrev Series.example_7_2_4
```

## Proposition 7.2.5 / Exercise 7.2.2

`Chapter7.Series.converges_iff_tail_decay` (theorem, [line 108](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_2.lean#L108)). An exercise, stated without proof.

> Proposition 7.2.5 / Exercise 7.2.2

```lean
theorem Series.converges_iff_tail_decay (s:Series) :
    s.converges ↔ ∀ ε > 0, ∃ N ≥ s.m, ∀ p ≥ N, ∀ q ≥ N, |∑ n ∈ Finset.Icc p q, s.seq n| ≤ ε
```

## Corollary 7.2.6 / Exercise 7.2.3

`Chapter7.Series.decay_of_converges` (theorem, [line 113](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_2.lean#L113)). An exercise, stated without proof.

> Corollary 7.2.6 (Zero test) / Exercise 7.2.3

```lean
theorem Series.decay_of_converges {s:Series} (h: s.converges) :
    Filter.atTop.Tendsto s.seq (nhds 0)
```

## Example 7.2.7

`Chapter7.Series.example_7_2_7` (theorem, [line 122](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_2.lean#L122)). Stated without proof.

> Example 7.2.7

```lean
theorem Series.example_7_2_7 : ((fun _:ℕ ↦ (1:ℝ)):Series).diverges
```

## Definition 7.2.8

`Chapter7.Series.abs` (abbrev, [line 131](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_2.lean#L131)). A definition.

> Definition 7.2.8 (Absolute convergence)

```lean
abbrev Series.abs (s:Series) : Series
```

## Proposition 7.2.9 / Exercise 7.2.4

`Chapter7.Series.converges_of_absConverges` (theorem, [line 138](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_2.lean#L138)). An exercise, stated without proof.

> Proposition 7.2.9 (Absolute convergence test) / Exercise 7.2.4

```lean
theorem Series.converges_of_absConverges {s:Series} (h : s.absConverges) : s.converges
```

## Proposition 7.2.12

`Chapter7.Series.converges_of_alternating` (theorem, [line 145](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_2.lean#L145)). Stated without proof.

> Proposition 7.2.12 (Alternating series test)

```lean
theorem Series.converges_of_alternating {m:ℤ} {a: { n // n ≥ m} → ℝ} (ha: ∀ n, a n ≥ 0)
  (ha': Antitone a) :
    ((mk' (fun n ↦ (-1)^(n:ℤ) * a n)).converges ↔ Filter.atTop.Tendsto a (nhds 0))
```

## Example 7.2.13

`Chapter7.Series.example_7_2_13` (abbrev, [line 186](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_2.lean#L186)). A definition.

> Example 7.2.13

```lean
noncomputable abbrev Series.example_7_2_13 : Series
```

## Proposition 7.2.14 (a) / Exercise 7.2.5

`Chapter7.Series.convergesTo.add` (theorem, [line 210](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_2.lean#L210)). An exercise, stated without proof.

> Proposition 7.2.14 (a) (Series laws) / Exercise 7.2.5.  The `convergesTo` form can be more convenient for applications.

```lean
theorem Series.convergesTo.add {s t:Series} {L M: ℝ} (hs: s.convergesTo L) (ht: t.convergesTo M) :
    (s + t).convergesTo (L + M)
```

## Proposition 7.2.14 (b) / Exercise 7.2.5

`Chapter7.Series.convergesTo.smul` (theorem, [line 229](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_2.lean#L229)). An exercise, stated without proof.

> Proposition 7.2.14 (b) (Series laws) / Exercise 7.2.5.  The `convergesTo` form can be more convenient for applications.

```lean
theorem Series.convergesTo.smul {s:Series} {L c: ℝ} (hs: s.convergesTo L) :
    (c • s).convergesTo (c * L)
```

## Proposition 7.2.14 (c) / Exercise 7.2.5

`Chapter7.Series.converges_from` (theorem, [line 259](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_2.lean#L259)). An exercise, stated without proof.

> Proposition 7.2.14 (c) (Series laws) / Exercise 7.2.5

```lean
theorem Series.converges_from (s:Series) (k:ℕ) : s.converges ↔ (s.from (s.m+k)).converges
```

## Proposition 7.2.14 (d) / Exercise 7.2.5

`Chapter7.Series.shift` (theorem, [line 267](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_2.lean#L267)). An exercise, stated without proof.

> Proposition 7.2.14 (d) (Series laws) / Exercise 7.2.5

```lean
theorem Series.shift {s:Series} {x:ℝ} (h: s.convergesTo x) (L:ℤ) :
    (mk' (m := s.m + L) (fun n ↦ s.seq (n - L))).convergesTo x
```

## Lemma 7.2.15 / Exercise 7.2.6

`Chapter7.Series.telescope` (theorem, [line 272](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_2.lean#L272)). An exercise, stated without proof.

> Lemma 7.2.15 (telescoping series) / Exercise 7.2.6

```lean
theorem Series.telescope {a:ℕ → ℝ} (ha: Filter.atTop.Tendsto a (nhds 0)) :
    ((fun n:ℕ ↦ a n - a (n+1)):Series).convergesTo (a 0)
```

## Exercise 7.2.1

`Chapter7.Series.exercise_7_2_1_convergent` (def, [line 277](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_2.lean#L277)). A definition whose value is left as `sorry`.

> Exercise 7.2.1

```lean
def Series.exercise_7_2_1_convergent :
  Decidable ( (mk' (m := 1) (fun n ↦ (-1:ℝ)^(n:ℤ))).converges )
```

## Depends on

Its Lean file imports no other section's file.

## Sources

- [Analysis/Section_7_2.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_2.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_7_2/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_7_2.html)
