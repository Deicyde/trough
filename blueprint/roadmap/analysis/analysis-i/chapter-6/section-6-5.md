---
declaration: theorem
origin: cited
lean: Chapter6.Sequence.lim_of_power_decay, Chapter6.Sequence.lim_of_geometric, Chapter6.Sequence.lim_of_geometric', Chapter6.Sequence.lim_of_geometric'', Chapter6.Sequence.lim_of_roots, Chapter6.Sequence.lim_of_rat_power_decay, Chapter6.Sequence.lim_of_rat_power_growth
statement: formalized
---

# Section 6.5: Some standard limits

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Some standard limits, including limits of sequences of the form 1/n^α, x^n, and x^(1/n).

*Quoted from [Analysis/Section_6_5.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_5.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 5 labelled items, carried by 7 declarations: 1 proved here and 6 stated without proof (6 of them exercises). It also has 5 declarations with no label, counted here but not shown.

## Corollary 6.5.1

`Chapter6.Sequence.lim_of_power_decay` (theorem, [line 50](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_5.lean#L50)). Proved here.

> Corollary 6.5.1

```lean
theorem Sequence.lim_of_power_decay {k:ℕ} :
    ((fun (n:ℕ) ↦ 1/((n:ℝ)+1)^(1/(k+1:ℝ))):Sequence).TendsTo 0
```

## Lemma 6.5.2 / Exercise 6.5.2

`Chapter6.Sequence.lim_of_geometric` (theorem, [line 74](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_5.lean#L74)). An exercise, stated without proof.

> Lemma 6.5.2 (ratio of absolute value less than one) / Exercise 6.5.2

```lean
theorem Sequence.lim_of_geometric {x:ℝ} (hx: |x| < 1) : ((fun (n:ℕ) ↦ x^n):Sequence).TendsTo 0
```

`Chapter6.Sequence.lim_of_geometric'` (theorem, [line 78](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_5.lean#L78)). An exercise, stated without proof.

> Lemma 6.5.2 (ratio one) / Exercise 6.5.2

```lean
theorem Sequence.lim_of_geometric' {x:ℝ} (hx: x = 1) : ((fun (n:ℕ) ↦ x^n):Sequence).TendsTo 1
```

`Chapter6.Sequence.lim_of_geometric''` (theorem, [line 82](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_5.lean#L82)). An exercise, stated without proof.

> Lemma 6.5.2 (ratio minus one or of absolute value greater than one) / Exercise 6.5.2

```lean
theorem Sequence.lim_of_geometric'' {x:ℝ} (hx: x = -1 ∨ |x| > 1) :
    ((fun (n:ℕ) ↦ x^n):Sequence).Divergent
```

## Lemma 6.5.3 / Exercise 6.5.3

`Chapter6.Sequence.lim_of_roots` (theorem, [line 87](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_5.lean#L87)). An exercise, stated without proof.

> Lemma 6.5.3 / Exercise 6.5.3

```lean
theorem Sequence.lim_of_roots {x:ℝ} (hx: x > 0) :
    ((fun (n:ℕ) ↦ x^(1/(n+1:ℝ))):Sequence).TendsTo 1
```

## Exercise 6.5.1 (i)

`Chapter6.Sequence.lim_of_rat_power_decay` (theorem, [line 92](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_5.lean#L92)). An exercise, stated without proof.

> Exercise 6.5.1 (i)

```lean
theorem Sequence.lim_of_rat_power_decay {q:ℚ} (hq: q > 0) :
    (fun (n:ℕ) ↦ 1/((n+1:ℝ)^(q:ℝ)):Sequence).TendsTo 0
```

## Exercise 6.5.1 (ii)

`Chapter6.Sequence.lim_of_rat_power_growth` (theorem, [line 97](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_5.lean#L97)). An exercise, stated without proof.

> Exercise 6.5.1 (ii)

```lean
theorem Sequence.lim_of_rat_power_growth {q:ℚ} (hq: q > 0) :
    (fun (n:ℕ) ↦ ((n+1:ℝ)^(q:ℝ)):Sequence).Divergent
```

## Depends on

- [Section 6.4: Limsup, liminf, and limit points](section-6-4.md)

## Sources

- [Analysis/Section_6_5.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_5.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_6_5/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_6_5.html)
