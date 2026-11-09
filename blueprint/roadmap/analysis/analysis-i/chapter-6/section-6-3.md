---
declaration: abbrev
origin: cited
lean: Chapter6.Sequence.sup, Chapter6.Sequence.inf, Chapter6.Sequence.le_sup, Chapter6.Sequence.sup_le_upper, Chapter6.Sequence.exists_between_lt_sup, Chapter6.Sequence.ge_inf, Chapter6.Sequence.inf_ge_lower, Chapter6.Sequence.exists_between_gt_inf, Chapter6.Sequence.convergent_of_monotone, Chapter6.Sequence.lim_of_monotone, Chapter6.Example_6_3_9, Chapter6.lim_of_exp, Chapter6.lim_of_exp'
statement: formalized
---

# Section 6.3: Suprema and infima of sequences

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Suprema and infima of sequences.

*Quoted from [Analysis/Section_6_3.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 22 labelled items, carried by 23 declarations: 20 stated without proof (8 of them exercises) and 3 definitions. It also has 13 declarations with no label, counted here but not shown.

## Definition 6.3.1

`Chapter6.Sequence.sup` (abbrev, [line 24](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean#L24)). A definition.

> Definition 6.3.1 (supremum of a sequence)

```lean
noncomputable abbrev Sequence.sup (a:Sequence) : EReal
```

`Chapter6.Sequence.inf` (abbrev, [line 27](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean#L27)). A definition.

> Definition 6.3.1 (infimum of a sequence)

```lean
noncomputable abbrev Sequence.inf (a:Sequence) : EReal
```

## Example 6.3.3 (a)

An `example` ([line 30](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean#L30)). Stated without proof.

> Example 6.3.3 (a)

```lean
example : ((fun (n:ℕ) ↦ (-1:ℝ)^(n+1)):Sequence).sup = 1
```

## Example 6.3.3 (b)

An `example` ([line 33](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean#L33)). Stated without proof.

> Example 6.3.3 (b)

```lean
example : ((fun (n:ℕ) ↦ (-1:ℝ)^(n+1)):Sequence).inf = -1
```

## Example 6.3.4 / Exercise 6.3.1 (a)

An `example` ([line 36](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean#L36)). An exercise, stated without proof.

> Example 6.3.4 / Exercise 6.3.1 (a)

```lean
example : ((fun (n:ℕ) ↦ 1/((n:ℝ)+1)):Sequence).sup = 1
```

## Example 6.3.4 / Exercise 6.3.1 (b)

An `example` ([line 39](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean#L39)). An exercise, stated without proof.

> Example 6.3.4 / Exercise 6.3.1 (b)

```lean
example : ((fun (n:ℕ) ↦ 1/((n:ℝ)+1)):Sequence).inf = 0
```

## Example 6.3.5 (a)

An `example` ([line 42](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean#L42)). Stated without proof.

> Example 6.3.5 (a)

```lean
example : ((fun (n:ℕ) ↦ (n+1:ℝ)):Sequence).sup = ⊤
```

## Example 6.3.5 (b)

An `example` ([line 45](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean#L45)). Stated without proof.

> Example 6.3.5 (b)

```lean
example : ((fun (n:ℕ) ↦ (n+1:ℝ)):Sequence).inf = 1
```

## Proposition 6.3.6 (a) / Exercise 6.3.2

`Chapter6.Sequence.le_sup` (theorem, [line 62](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean#L62)). An exercise, stated without proof.

> Proposition 6.3.6 (a) (Least upper bound property) / Exercise 6.3.2

```lean
theorem Sequence.le_sup {a:Sequence} {n:ℤ} (hn: n ≥ a.m) : a n ≤ a.sup
```

## Proposition 6.3.6 (b) / Exercise 6.3.2

`Chapter6.Sequence.sup_le_upper` (theorem, [line 65](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean#L65)). An exercise, stated without proof.

> Proposition 6.3.6 (b) (Least upper bound property) / Exercise 6.3.2

```lean
theorem Sequence.sup_le_upper {a:Sequence} {M:EReal} (h: ∀ n ≥ a.m, a n ≤ M) : a.sup ≤ M
```

## Proposition 6.3.6 (c) / Exercise 6.3.2

`Chapter6.Sequence.exists_between_lt_sup` (theorem, [line 68](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean#L68)). An exercise, stated without proof.

> Proposition 6.3.6 (c) (Least upper bound property) / Exercise 6.3.2

```lean
theorem Sequence.exists_between_lt_sup {a:Sequence} {y:EReal} (h: y < a.sup ) :
    ∃ n ≥ a.m, y < a n ∧ a n ≤ a.sup
```

## Remark 6.3.7 (a)

`Chapter6.Sequence.ge_inf` (theorem, [line 72](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean#L72)). Stated without proof.

> Remark 6.3.7 (a)

```lean
theorem Sequence.ge_inf {a:Sequence} {n:ℤ} (hn: n ≥ a.m) : a n ≥ a.inf
```

## Remark 6.3.7 (b)

`Chapter6.Sequence.inf_ge_lower` (theorem, [line 75](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean#L75)). Stated without proof.

> Remark 6.3.7 (b)

```lean
theorem Sequence.inf_ge_lower {a:Sequence} {M:EReal} (h: ∀ n ≥ a.m, a n ≥ M) : a.inf ≥ M
```

## Remark 6.3.7 (c)

`Chapter6.Sequence.exists_between_gt_inf` (theorem, [line 78](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean#L78)). Stated without proof.

> Remark 6.3.7 (c)

```lean
theorem Sequence.exists_between_gt_inf {a:Sequence} {y:EReal} (h: y > a.inf ) :
    ∃ n ≥ a.m, y > a n ∧ a n ≥ a.inf
```

## Proposition 6.3.8 (a) / Exercise 6.3.3

`Chapter6.Sequence.convergent_of_monotone` (theorem, [line 86](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean#L86)). An exercise, stated without proof.

> Proposition 6.3.8 (a) / Exercise 6.3.3

```lean
theorem Sequence.convergent_of_monotone {a:Sequence} (hbound: a.BddAbove) (hmono: a.IsMonotone) :
    a.Convergent
```

## Proposition 6.3.8 (b) / Exercise 6.3.3

`Chapter6.Sequence.lim_of_monotone` (theorem, [line 90](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean#L90)). An exercise, stated without proof.

> Proposition 6.3.8 (b) / Exercise 6.3.3

```lean
theorem Sequence.lim_of_monotone {a:Sequence} (hbound: a.BddAbove) (hmono: a.IsMonotone) :
    lim a = a.sup
```

## Example 6.3.9 (a)

`Chapter6.Example_6_3_9` (abbrev, [line 106](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean#L106)). A definition.

> Example 6.3.9 (a)

```lean
noncomputable abbrev Example_6_3_9 (n:ℕ)
```

## Example 6.3.9 (b)

An `example` ([line 109](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean#L109)). Stated without proof.

> Example 6.3.9 (b)

```lean
example : (Example_6_3_9:Sequence).IsMonotone
```

## Example 6.3.9 (c)

An `example` ([line 112](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean#L112)). Stated without proof.

> Example 6.3.9 (c)

```lean
example : (Example_6_3_9:Sequence).BddAboveBy 4
```

## Example 6.3.9 (d)

An `example` ([line 115](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean#L115)). Stated without proof.

> Example 6.3.9 (d)

```lean
example : (Example_6_3_9:Sequence).Convergent
```

## Example 6.3.9 (e)

An `example` ([line 118](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean#L118)). Stated without proof.

> Example 6.3.9 (e)

```lean
example : lim (Example_6_3_9:Sequence) ≤ 4
```

## Proposition 6.3.1

`Chapter6.lim_of_exp` (theorem, [line 121](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean#L121)). Stated without proof.

> Proposition 6.3.1

```lean
theorem lim_of_exp {x:ℝ} (hpos: 0 < x) (hbound: x < 1) :
    ((fun (n:ℕ) ↦ x^n):Sequence).Convergent ∧ lim ((fun (n:ℕ) ↦ x^n):Sequence) = 0
```

## Exercise 6.3.4

`Chapter6.lim_of_exp'` (theorem, [line 139](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean#L139)). An exercise, stated without proof.

> Exercise 6.3.4

```lean
theorem lim_of_exp' {x:ℝ} (hbound: x > 1) : ¬((fun (n:ℕ) ↦ x^n):Sequence).Convergent
```

## Depends on

- [Section 6.1: Convergence and limit laws](section-6-1.md)
- [Section 6.2: The extended real number system](section-6-2.md)

## Sources

- [Analysis/Section_6_3.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_3.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_6_3/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_6_3.html)
