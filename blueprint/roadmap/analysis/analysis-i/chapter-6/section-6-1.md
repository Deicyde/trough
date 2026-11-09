---
declaration: theorem
origin: cited
lean: Real.close_def, Chapter6.Sequence, Real.Steady, Real.steady_def, Real.EventuallySteady, Real.eventuallySteady_def, Chapter6.Sequence.IsCauchy, Chapter6.Sequence.isCauchy_def, Chapter6.Sequence.isCauchy_of_rat, Real.CloseSeq, Real.closeSeq_def, Real.EventuallyClose, Real.eventuallyClose_def, Chapter6.Sequence.tendsTo_iff, Chapter6.Sequence.tendsTo_unique, Chapter6.Sequence.Convergent, Chapter6.Sequence.convergent_def, Chapter6.Sequence.Divergent, Chapter6.Sequence.divergent_def, Chapter6.lim, Chapter6.Sequence.lim_def, Chapter6.Sequence.lim_eq, Chapter6.Sequence.lim_harmonic, Chapter6.Sequence.IsCauchy.convergent, Chapter6.Sequence.lim_eq_LIM, Chapter6.Sequence.BoundedBy, Chapter6.Sequence.boundedBy_def, Chapter6.Sequence.IsBounded, Chapter6.Sequence.isBounded_def, Chapter6.Sequence.bounded_of_convergent, Chapter6.Sequence.tendsTo_add, Chapter6.Sequence.tendsTo_mul, Chapter6.Sequence.tendsTo_smul, Chapter6.Sequence.tendsTo_sub, Chapter6.Sequence.tendsTo_inv, Chapter6.Sequence.tendsTo_div, Chapter6.Sequence.tendsTo_max, Chapter6.Sequence.tendsTo_min, Chapter6.Sequence.mono_if, Chapter6.Sequence.tendsTo_of_from, Chapter6.Sequence.tendsTo_of_shift, Chapter6.Sequence.isBounded_of_rat, Chapter6.Sequence.lim_div_fail, Chapter6.Chapter5.Sequence.equiv_rat
statement: formalized
---

# Section 6.1: Convergence and limit laws

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Definition of $ε$-closeness, $ε$-steadiness, and their eventual counterparts.
> - Notion of a Cauchy sequence, convergent sequence, and bounded sequence of reals.

*Quoted from [Analysis/Section_6_1.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 29 labelled items, carried by 53 declarations: 17 proved here, 25 stated without proof (9 of them exercises) and 11 definitions. It also has 61 declarations with no label, counted here but not shown.

## Definition 6.1.2

`Real.close_def` (theorem, [line 32](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L32)). Proved here.

> Definition 6.1.2 (ε-close). This is similar to the previous notion of ε-closeness, but where
> all quantities are real instead of rational.

```lean
theorem Real.close_def (ε x y : ℝ) : ε.Close x y ↔ dist x y ≤ ε
```

## Definition 6.1.3

`Chapter6.Sequence` (structure, [line 41](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L41)). A definition.

> Definition 6.1.3 (Sequence). This is similar to the Chapter 5 sequence, except that now the
> sequence is real-valued. As with Chapter 5, we start sequences from 0 by default.

```lean
structure Sequence
```

`Real.Steady` (abbrev, [line 87](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L87)). A definition.

> Definition 6.1.3 (ε-steady)

```lean
abbrev Real.Steady (ε: ℝ) (a: Chapter6.Sequence) : Prop
```

`Real.steady_def` (lemma, [line 91](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L91)). Proved here.

> Definition 6.1.3 (ε-steady, def)

```lean
lemma Real.steady_def (ε: ℝ) (a: Chapter6.Sequence) :
  ε.Steady a ↔ ∀ n ≥ a.m, ∀ m ≥ a.m, ε.Close (a n) (a m)
```

`Real.EventuallySteady` (abbrev, [line 95](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L95)). A definition.

> Definition 6.1.3 (Eventually ε-steady)

```lean
abbrev Real.EventuallySteady (ε: ℝ) (a: Chapter6.Sequence) : Prop
```

`Real.eventuallySteady_def` (lemma, [line 99](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L99)). Proved here.

> Definition 6.1.3 (Eventually ε-steady, def)

```lean
lemma Real.eventuallySteady_def (ε: ℝ) (a: Chapter6.Sequence) :
  ε.EventuallySteady a ↔ ∃ N, (N ≥ a.m) ∧ ε.Steady (a.from N)
```

`Chapter6.Sequence.IsCauchy` (abbrev, [line 114](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L114)). A definition.

> Definition 6.1.3 (Cauchy sequence)

```lean
abbrev Sequence.IsCauchy (a:Sequence) : Prop
```

`Chapter6.Sequence.isCauchy_def` (lemma, [line 117](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L117)). Proved here.

> Definition 6.1.3 (Cauchy sequence, def)

```lean
lemma Sequence.isCauchy_def (a:Sequence) :
  a.IsCauchy ↔ ∀ ε > (0:ℝ), ε.EventuallySteady a
```

## Proposition 6.1.4

`Chapter6.Sequence.isCauchy_of_rat` (theorem, [line 174](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L174)). Proved here.

> Proposition 6.1.4

```lean
theorem Sequence.isCauchy_of_rat (a: Chapter5.Sequence) : a.IsCauchy ↔ (a:Sequence).IsCauchy
```

## Definition 6.1.5

`Real.CloseSeq` (abbrev, [line 195](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L195)). A definition.

> Definition 6.1.5 (CloseSeq)

```lean
abbrev Real.CloseSeq (ε: ℝ) (a: Chapter6.Sequence) (L:ℝ) : Prop
```

`Real.closeSeq_def` (theorem, [line 198](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L198)). Proved here.

> Definition 6.1.5 (CloseSeq, def)

```lean
theorem Real.closeSeq_def (ε: ℝ) (a: Chapter6.Sequence) (L:ℝ) :
  ε.CloseSeq a L ↔ ∀ n ≥ a.m, dist (a n) L ≤ ε
```

`Real.EventuallyClose` (abbrev, [line 202](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L202)). A definition.

> Definition 6.1.5 (EventuallyClose)

```lean
abbrev Real.EventuallyClose (ε: ℝ) (a: Chapter6.Sequence) (L:ℝ) : Prop
```

`Real.eventuallyClose_def` (theorem, [line 206](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L206)). Proved here.

> Definition 6.1.5 (EventuallyClose, def)

```lean
theorem Real.eventuallyClose_def (ε: ℝ) (a: Chapter6.Sequence) (L:ℝ) :
  ε.EventuallyClose a L ↔ ∃ N, (N ≥ a.m) ∧ ε.CloseSeq (a.from N) L
```

## Exercise 6.1.2

`Chapter6.Sequence.tendsTo_iff` (theorem, [line 231](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L231)). An exercise, stated without proof.

> Exercise 6.1.2

```lean
theorem Sequence.tendsTo_iff (a:Sequence) (L:ℝ) :
  a.TendsTo L ↔ ∀ ε > 0, ∃ N, ∀ n ≥ N, |a n - L| ≤ ε
```

## Examples 6.1.6

An `example` ([line 237](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L237)). Proved here.

> Examples 6.1.6 (0.1 close)

```lean
example : (0.1:ℝ).CloseSeq seq_6_1_6 1
```

An `example` ([line 250](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L250)). Proved here.

> Examples 6.1.6 (0.01 not close)

```lean
example : ¬ (0.01:ℝ).CloseSeq seq_6_1_6 1
```

An `example` ([line 254](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L254)). Stated without proof.

> Examples 6.1.6 (0.01 eventually close)

```lean
example : (0.01:ℝ).EventuallyClose seq_6_1_6 1
```

An `example` ([line 257](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L257)). Stated without proof.

> Examples 6.1.6 (tends to 1)

```lean
example : seq_6_1_6.TendsTo 1
```

## Proposition 6.1.7

`Chapter6.Sequence.tendsTo_unique` (theorem, [line 260](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L260)). Proved here.

> Proposition 6.1.7 (Uniqueness of limits)

```lean
theorem Sequence.tendsTo_unique (a:Sequence) {L L':ℝ} (h:L ≠ L') :
    ¬ (a.TendsTo L ∧ a.TendsTo L')
```

## Definition 6.1.8

`Chapter6.Sequence.Convergent` (abbrev, [line 283](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L283)). A definition.

> Definition 6.1.8 (Convergent)

```lean
abbrev Sequence.Convergent (a:Sequence) : Prop
```

`Chapter6.Sequence.convergent_def` (theorem, [line 286](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L286)). Proved here.

> Definition 6.1.8 (Convergent, def)

```lean
theorem Sequence.convergent_def (a:Sequence) : a.Convergent ↔ ∃ L, a.TendsTo L
```

`Chapter6.Sequence.Divergent` (abbrev, [line 289](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L289)). A definition.

> Definition 6.1.8 (Divergent)

```lean
abbrev Sequence.Divergent (a:Sequence) : Prop
```

`Chapter6.Sequence.divergent_def` (theorem, [line 292](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L292)). Proved here.

> Definition 6.1.8 (Divergent, def)

```lean
theorem Sequence.divergent_def (a:Sequence) : a.Divergent ↔ ¬ a.Convergent
```

`Chapter6.lim` (abbrev, [line 298](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L298)). A definition.

> Definition 6.1.8.  We give the limit of a sequence the junk value of `0` if it is not convergent.

```lean
noncomputable abbrev lim (a:Sequence) : ℝ
```

`Chapter6.Sequence.lim_def` (theorem, [line 301](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L301)). Proved here.

> Definition 6.1.8 (lim, def)

```lean
theorem Sequence.lim_def {a:Sequence} (h: a.Convergent) : a.TendsTo (lim a)
```

`Chapter6.Sequence.lim_eq` (theorem, [line 305](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L305)). Proved here.

> Definition 6.1.8 (lim, characterization)

```lean
theorem Sequence.lim_eq {a:Sequence} {L:ℝ} :
a.TendsTo L ↔ a.Convergent ∧ lim a = L
```

## Proposition 6.1.11

`Chapter6.Sequence.lim_harmonic` (theorem, [line 316](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L316)). Proved here.

> Proposition 6.1.11

```lean
theorem Sequence.lim_harmonic :
    ((fun (n:ℕ) ↦ (n+1:ℝ)⁻¹):Sequence).Convergent ∧ lim ((fun (n:ℕ) ↦ (n+1:ℝ)⁻¹):Sequence) = 0
```

## Proposition 6.1.12 / Exercise 6.1.5

`Chapter6.Sequence.IsCauchy.convergent` (theorem, [line 340](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L340)). An exercise, stated without proof.

> Proposition 6.1.12 / Exercise 6.1.5

```lean
theorem Sequence.IsCauchy.convergent {a:Sequence} (h:a.Convergent) : a.IsCauchy
```

## Example 6.1.13

An `example` ([line 344](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L344)). Stated without proof.

> Example 6.1.13 (not eventually steady)

```lean
example : ¬ (0.1:ℝ).EventuallySteady ((fun n ↦ (-1:ℝ)^n):Sequence)
```

An `example` ([line 347](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L347)). Stated without proof.

> Example 6.1.13 (not Cauchy)

```lean
example : ¬ ((fun n ↦ (-1:ℝ)^n):Sequence).IsCauchy
```

An `example` ([line 350](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L350)). Stated without proof.

> Example 6.1.13 (not convergent)

```lean
example : ¬ ((fun n ↦ (-1:ℝ)^n):Sequence).Convergent
```

## Proposition 6.1.15 / Exercise 6.1.6

`Chapter6.Sequence.lim_eq_LIM` (theorem, [line 353](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L353)). An exercise, stated without proof.

> Proposition 6.1.15 / Exercise 6.1.6 (Formal limits are genuine limits)

```lean
theorem Sequence.lim_eq_LIM {a:ℕ → ℚ} (h: (a:Chapter5.Sequence).IsCauchy) :
    ((a:Chapter5.Sequence):Sequence).TendsTo (Chapter5.Real.equivR (Chapter5.LIM a))
```

## Definition 6.1.16

`Chapter6.Sequence.BoundedBy` (abbrev, [line 357](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L357)). A definition.

> Definition 6.1.16 (BoundedBy)

```lean
abbrev Sequence.BoundedBy (a:Sequence) (M:ℝ) : Prop
```

`Chapter6.Sequence.boundedBy_def` (lemma, [line 361](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L361)). Proved here.

> Definition 6.1.16 (BoundedBy, def)

```lean
lemma Sequence.boundedBy_def (a:Sequence) (M:ℝ) :
  a.BoundedBy M ↔ ∀ n, |a n| ≤ M
```

`Chapter6.Sequence.IsBounded` (abbrev, [line 365](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L365)). A definition.

> Definition 6.1.16 (IsBounded)

```lean
abbrev Sequence.IsBounded (a:Sequence) : Prop
```

`Chapter6.Sequence.isBounded_def` (lemma, [line 368](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L368)). Proved here.

> Definition 6.1.16 (IsBounded, def)

```lean
lemma Sequence.isBounded_def (a:Sequence) :
  a.IsBounded ↔ ∃ M ≥ 0, a.BoundedBy M
```

## Corollary 6.1.17

`Chapter6.Sequence.bounded_of_convergent` (theorem, [line 375](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L375)). Stated without proof.

> Corollary 6.1.17

```lean
theorem Sequence.bounded_of_convergent {a:Sequence} (h: a.Convergent) : a.IsBounded
```

## Example 6.1.18

An `example` ([line 379](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L379)). Stated without proof.

> Example 6.1.18 (not bounded)

```lean
example : ¬ ((fun (n:ℕ) ↦ (n+1:ℝ)):Sequence).IsBounded
```

An `example` ([line 382](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L382)). Stated without proof.

> Example 6.1.18 (not convergent)

```lean
example : ¬ ((fun (n:ℕ) ↦ (n+1:ℝ)):Sequence).Convergent
```

## Theorem 6.1.19(a)

`Chapter6.Sequence.tendsTo_add` (theorem, [line 400](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L400)). Stated without proof.

> Theorem 6.1.19(a) (limit laws).  The `Sequence.TendsTo` version is more usable than the `lim` version
> in applications.

```lean
theorem Sequence.tendsTo_add {a b:Sequence} {L M:ℝ} (ha: a.TendsTo L) (hb: b.TendsTo M) :
  (a+b).TendsTo (L+M)
```

## Theorem 6.1.19(b)

`Chapter6.Sequence.tendsTo_mul` (theorem, [line 424](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L424)). Stated without proof.

> Theorem 6.1.19(b) (limit laws).  The `Sequence.TendsTo` version is more usable than the `lim` version
> in applications.

```lean
theorem Sequence.tendsTo_mul {a b:Sequence} {L M:ℝ} (ha: a.TendsTo L) (hb: b.TendsTo M) :
    (a * b).TendsTo (L * M)
```

## Theorem 6.1.19(c)

`Chapter6.Sequence.tendsTo_smul` (theorem, [line 449](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L449)). Stated without proof.

> Theorem 6.1.19(c) (limit laws).  The `Sequence.TendsTo` version is more usable than the `lim` version
> in applications.

```lean
theorem Sequence.tendsTo_smul (c:ℝ) {a:Sequence} {L:ℝ} (ha: a.TendsTo L) :
    (c • a).TendsTo (c * L)
```

## Theorem 6.1.19(d)

`Chapter6.Sequence.tendsTo_sub` (theorem, [line 473](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L473)). Stated without proof.

> Theorem 6.1.19(d) (limit laws).  The `Sequence.TendsTo` version is more usable than the `lim` version
> in applications.

```lean
theorem Sequence.tendsTo_sub {a b:Sequence} {L M:ℝ} (ha: a.TendsTo L) (hb: b.TendsTo M) :
    (a - b).TendsTo (L - M)
```

## Theorem 6.1.19(e)

`Chapter6.Sequence.tendsTo_inv` (theorem, [line 497](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L497)). Stated without proof.

> Theorem 6.1.19(e) (limit laws).  The `Sequence.TendsTo` version is more usable than the `lim` version
> in applications.

```lean
theorem Sequence.tendsTo_inv {a:Sequence} {L:ℝ} (ha: a.TendsTo L) (hnon: L ≠ 0) :
    (a⁻¹).TendsTo (L⁻¹)
```

## Theorem 6.1.19(f)

`Chapter6.Sequence.tendsTo_div` (theorem, [line 521](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L521)). Stated without proof.

> Theorem 6.1.19(f) (limit laws).  The `Sequence.TendsTo` version is more usable than the `lim` version
> in applications.

```lean
theorem Sequence.tendsTo_div {a b:Sequence} {L M:ℝ} (ha: a.TendsTo L) (hb: b.TendsTo M) (hnon: M ≠ 0) :
    (a / b).TendsTo (L / M)
```

## Theorem 6.1.19(g)

`Chapter6.Sequence.tendsTo_max` (theorem, [line 545](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L545)). Stated without proof.

> Theorem 6.1.19(g) (limit laws).  The `Sequence.TendsTo` version is more usable than the `lim` version
> in applications.

```lean
theorem Sequence.tendsTo_max {a b:Sequence} {L M:ℝ} (ha: a.TendsTo L) (hb: b.TendsTo M) :
    (max a b).TendsTo (max L M)
```

## Theorem 6.1.19(h)

`Chapter6.Sequence.tendsTo_min` (theorem, [line 568](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L568)). Stated without proof.

> Theorem 6.1.19(h) (limit laws)

```lean
theorem Sequence.tendsTo_min {a b:Sequence} {L M:ℝ} (ha: a.TendsTo L) (hb: b.TendsTo M) :
    (min a b).TendsTo (min L M)
```

## Exercise 6.1.1

`Chapter6.Sequence.mono_if` (theorem, [line 577](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L577)). An exercise, stated without proof.

> Exercise 6.1.1

```lean
theorem Sequence.mono_if {a: ℕ → ℝ} (ha: ∀ n, a (n+1) > a n) {n m:ℕ} (hnm: m > n) : a m > a n
```

## Exercise 6.1.3

`Chapter6.Sequence.tendsTo_of_from` (theorem, [line 581](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L581)). An exercise, stated without proof.

> Exercise 6.1.3

```lean
theorem Sequence.tendsTo_of_from {a: Sequence} {c:ℝ} (m:ℤ) :
    a.TendsTo c ↔ (a.from m).TendsTo c
```

## Exercise 6.1.4

`Chapter6.Sequence.tendsTo_of_shift` (theorem, [line 586](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L586)). An exercise, stated without proof.

> Exercise 6.1.4

```lean
theorem Sequence.tendsTo_of_shift {a: Sequence} {c:ℝ} (k:ℕ) :
    a.TendsTo c ↔ (Sequence.mk' a.m (fun n : {n // n ≥ a.m} ↦ a (n+k))).TendsTo c
```

## Exercise 6.1.7

`Chapter6.Sequence.isBounded_of_rat` (theorem, [line 591](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L591)). An exercise, stated without proof.

> Exercise 6.1.7

```lean
theorem Sequence.isBounded_of_rat (a: Chapter5.Sequence) :
    a.IsBounded ↔ (a:Sequence).IsBounded
```

## Exercise 6.1.9

`Chapter6.Sequence.lim_div_fail` (theorem, [line 596](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L596)). An exercise, stated without proof.

> Exercise 6.1.9

```lean
theorem Sequence.lim_div_fail :
    ∃ a b, a.Convergent
    ∧ b.Convergent
    ∧ lim b = 0
    ∧ ¬ ((a / b).Convergent ∧ lim (a / b) = lim a / lim b)
```

## Exercise 6.1.10

`Chapter6.Chapter5.Sequence.equiv_rat` (theorem, [line 621](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean#L621)). An exercise, stated without proof.

> Exercise 6.1.10

```lean
theorem Chapter5.Sequence.equiv_rat (a b: ℕ → ℚ) :
  Chapter5.Sequence.Equiv a b ↔ Chapter5.Sequence.RatEquiv a b
```

## Depends on

- [Section 5.1: Cauchy sequences](../chapter-5/section-5-1.md)
- [Section 5.3: The construction of the real numbers](../chapter-5/section-5-3.md)
- [Chapter 5 epilogue: Isomorphism with the Mathlib real numbers](../chapter-5/section-5-epilogue.md)

## Sources

- [Analysis/Section_6_1.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_6_1.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_6_1/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_6_1.html)
