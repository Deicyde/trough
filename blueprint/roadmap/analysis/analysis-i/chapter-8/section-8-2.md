---
declaration: abbrev
origin: cited
lean: Chapter8.AbsConvergent, Chapter8.sum_of_sum_of_AbsConvergent_nonneg, Chapter8.sum_of_sum_of_AbsConvergent, Chapter8.sum_of_sum_of_AbsConvergent', Chapter8.sum_comm, Chapter8.AbsConvergent.iff, Chapter8.AbsConvergent'.countable_supp, Chapter8.Sum'.add, Chapter8.Sum'.smul, Chapter8.Sum'.of_disjoint_union, Chapter8.divergent_parts_of_divergent, Chapter8.permute_convergesTo_of_divergent, Chapter8.permute_diverges_of_divergent
statement: formalized
---

# Section 8.2: Summation on infinite sets

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Absolute convergence and summation on countably infinite or general sets.
> - Connections with Mathlib's `Summable` and `tsum`.
> - The Riemann rearrangement theorem.
>
> Some non-trivial API is provided beyond what is given in the textbook in order connect these
> notions with existing summation notions.
>
> After this section, the summation notation developed here will be deprecated in favor of Mathlib's API for `Summable` and `tsum`.

*Quoted from [Analysis/Section_8_2.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_2.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 10 labelled items, carried by 13 declarations: 2 proved here, 10 stated without proof (8 of them exercises) and 1 definition. It also has 23 declarations with no label, counted here but not shown.

## Definition 8.2.1

`Chapter8.AbsConvergent` (abbrev, [line 35](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_2.lean#L35)). A definition.

> Definition 8.2.1 (Series on countable sets).  Note that with this definition, functions defined
> on finite sets will not be absolutely convergent; one should use `AbsConvergent'` instead for such
> cases.

```lean
abbrev AbsConvergent {X:Type} (f: X → ℝ) : Prop
```

## Theorem 8.2.2

`Chapter8.sum_of_sum_of_AbsConvergent_nonneg` (theorem, [line 89](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_2.lean#L89)). Stated without proof.

> Theorem 8.2.2, preliminary version.  The arguments here are rearranged slightly from the text.

```lean
theorem sum_of_sum_of_AbsConvergent_nonneg {f:ℕ × ℕ → ℝ} (hf:AbsConvergent f) (hpos: ∀ n m, 0 ≤ f (n, m)) :
  (∀ n, ((fun m ↦ f (n, m)):Series).converges) ∧
  (fun n ↦ ((fun m ↦ f (n, m)):Series).sum:Series).convergesTo (Sum f)
```

`Chapter8.sum_of_sum_of_AbsConvergent` (theorem, [line 154](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_2.lean#L154)). Stated without proof.

> Theorem 8.2.2, second version

```lean
theorem sum_of_sum_of_AbsConvergent {f:ℕ × ℕ → ℝ} (hf:AbsConvergent f) :
  (∀ n, ((fun m ↦ f (n, m)):Series).absConverges) ∧
  (fun n ↦ ((fun m ↦ f (n, m)):Series).sum:Series).convergesTo (Sum f)
```

`Chapter8.sum_of_sum_of_AbsConvergent'` (theorem, [line 192](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_2.lean#L192)). Proved here.

> Theorem 8.2.2, third version

```lean
theorem sum_of_sum_of_AbsConvergent' {f:ℕ × ℕ → ℝ} (hf:AbsConvergent f) :
  (∀ m, ((fun n ↦ f (n, m)):Series).absConverges) ∧
  (fun m ↦ ((fun n ↦ f (n, m)):Series).sum:Series).convergesTo (Sum f)
```

`Chapter8.sum_comm` (theorem, [line 204](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_2.lean#L204)). Proved here.

> Theorem 8.2.2, fourth version

```lean
theorem sum_comm {f:ℕ × ℕ → ℝ} (hf:AbsConvergent f) :
  (fun n ↦ ((fun m ↦ f (n, m)):Series).sum:Series).sum = (fun m ↦ ((fun n ↦ f (n, m)):Series).sum:Series).sum
```

## Lemma 8.2.3 / Exercise 8.2.1

`Chapter8.AbsConvergent.iff` (theorem, [line 210](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_2.lean#L210)). An exercise, stated without proof.

> Lemma 8.2.3 / Exercise 8.2.1

```lean
theorem AbsConvergent.iff {X:Type} (hX:CountablyInfinite X) (f : X → ℝ) :
  AbsConvergent f ↔ BddAbove ( (fun A ↦ ∑ x ∈ A, |f x|) '' .univ )
```

## Lemma 8.2.5 / Exercise 8.2.2

`Chapter8.AbsConvergent'.countable_supp` (theorem, [line 239](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_2.lean#L239)). An exercise, stated without proof.

> Lemma 8.2.5 / Exercise 8.2.2

```lean
theorem AbsConvergent'.countable_supp {X:Type} {f:X → ℝ} (hf: AbsConvergent' f) :
  AtMostCountable { x | f x ≠ 0 }
```

## Proposition 8.2.6 (a) / Exercise 8.2.3

`Chapter8.Sum'.add` (theorem, [line 413](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_2.lean#L413)). An exercise, stated without proof.

> Proposition 8.2.6 (a) (Absolutely convergent series laws) / Exercise 8.2.3

```lean
theorem Sum'.add {X:Type} {f g:X → ℝ} (hf: AbsConvergent' f) (hg: AbsConvergent' g) :
  AbsConvergent' (f+g) ∧ Sum' (f + g) = Sum' f + Sum' g
```

## Proposition 8.2.6 (b) / Exercise 8.2.3

`Chapter8.Sum'.smul` (theorem, [line 418](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_2.lean#L418)). An exercise, stated without proof.

> Proposition 8.2.6 (b) (Absolutely convergent series laws) / Exercise 8.2.3

```lean
theorem Sum'.smul {X:Type} {f:X → ℝ} (hf: AbsConvergent' f) (c: ℝ) :
  AbsConvergent' (c • f) ∧ Sum' (c • f) = c * Sum' f
```

## Proposition 8.2.6 (c) / Exercise 8.2.3

`Chapter8.Sum'.of_disjoint_union` (theorem, [line 432](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_2.lean#L432)). An exercise, stated without proof.

> Proposition 8.2.6 (c) (Absolutely convergent series laws) / Exercise 8.2.3.  The first
> part of this proposition has been moved to `AbsConvergent'.subtype`.

```lean
theorem Sum'.of_disjoint_union {X:Type} {f:X → ℝ} (hf: AbsConvergent' f) {X₁ X₂ : Set X} (hdisj: Disjoint X₁ X₂):
  Sum' (fun x: (X₁ ∪ X₂: Set X) ↦ f x) = Sum' (fun x : X₁ ↦ f x) + Sum' (fun x : X₂ ↦ f x)
```

## Lemma 8.2.7 / Exercise 8.2.4

`Chapter8.divergent_parts_of_divergent` (theorem, [line 448](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_2.lean#L448)). An exercise, stated without proof.

> Lemma 8.2.7 / Exercise 8.2.4

```lean
theorem divergent_parts_of_divergent {a: ℕ → ℝ} (ha: (a:Series).converges)
  (ha': ¬ (a:Series).absConverges) :
  ¬ AbsConvergent (fun n : {n | a n ≥ 0} ↦ a n) ∧ ¬ AbsConvergent (fun n : {n | a n < 0} ↦ a n)
```

## Theorem 8.2.8 / Exercise 8.2.5

`Chapter8.permute_convergesTo_of_divergent` (theorem, [line 455](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_2.lean#L455)). An exercise, stated without proof.

> Theorem 8.2.8 (Riemann rearrangement theorem) / Exercise 8.2.5

```lean
theorem permute_convergesTo_of_divergent {a: ℕ → ℝ} (ha: (a:Series).converges)
  (ha': ¬ (a:Series).absConverges) (L:ℝ) :
  ∃ f : ℕ → ℕ, Bijective f ∧ (a ∘ f:Series).convergesTo L
```

## Exercise 8.2.6

`Chapter8.permute_diverges_of_divergent` (theorem, [line 494](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_2.lean#L494)). An exercise, stated without proof.

> Exercise 8.2.6

```lean
theorem permute_diverges_of_divergent {a: ℕ → ℝ} (ha: (a:Series).converges)
  (ha': ¬ (a:Series).absConverges)  :
  ∃ f : ℕ → ℕ,  Bijective f ∧ atTop.Tendsto (fun N ↦ ((a ∘ f:Series).partial N : EReal)) (nhds ⊤)
```

## Depends on

- [Section 7.2: Infinite series](../chapter-7/section-7-2.md)
- [Section 7.3: Sums of non-negative numbers](../chapter-7/section-7-3.md)
- [Section 7.4: Rearrangement of series](../chapter-7/section-7-4.md)
- [Section 8.1: Countability](section-8-1.md)

## Sources

- [Analysis/Section_8_2.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_2.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_8_2/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_8_2.html)
