---
declaration: theorem
origin: cited
lean: Finset.sum_of_empty, Finset.sum_of_nonempty, Finset.concat_finite_series, Finset.shift_finite_series, Finset.finite_series_add, Finset.finite_series_const_mul, Finset.abs_finite_series_le, Finset.finite_series_of_le, Finset.finite_series_of_rearrange, Finset.finite_series_eq, Finset.finite_series_of_empty, Finset.finite_series_of_singleton, Finset.map_finite_series, Finset.finite_series_of_disjoint_union, Finset.finite_series_of_add, Finset.finite_series_of_const_mul, Finset.finite_series_of_le', Finset.abs_finite_series_le', Finset.finite_series_of_finite_series, Finset.finite_series_refl, Finset.binomial_theorem, Finset.lim_of_finite_series, Finset.sum_union_disjoint, Finset.sum_finite_col_row_counts
statement: formalized
---

# Section 7.1: Finite series

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Technical note: it is convenient in Lean to extend finite sequences (usually by zero) to be
> functions on the entire integers.
>
> Main constructions and results of this section:

*Quoted from [Analysis/Section_7_1.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 24 labelled items, carried by 25 declarations: 5 proved here and 20 stated without proof (18 of them exercises). It also has 3 declarations and 5 examples with no label, counted here but not shown.

## Definition 7.1.1

`Finset.sum_of_empty` (theorem, [line 44](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L44)). Proved here.

> Definition 7.1.1

```lean
theorem sum_of_empty {n m:ℤ} (h: n < m) (a: ℤ → ℝ) : ∑ i ∈ Icc m n, a i = 0
```

`Finset.sum_of_nonempty` (theorem, [line 51](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L51)). Proved here.

> Definition 7.1.1. This is similar to Mathlib's `Finset.sum_Icc_succ_top` except that the
> latter involves summation over the natural numbers rather than integers.

```lean
theorem sum_of_nonempty {n m:ℤ} (h: n ≥ m-1) (a: ℤ → ℝ) :
    ∑ i ∈ Icc m (n+1), a i = ∑ i ∈ Icc m n, a i + a (n+1)
```

## Remark 7.1.3

An `example` ([line 70](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L70)). Proved here.

> Remark 7.1.3

```lean
example (a: ℤ → ℝ) (m n:ℤ) : ∑ i ∈ Icc m n, a i = ∑ j ∈ Icc m n, a j
```

## Lemma 7.1.4(a) / Exercise 7.1.1

`Finset.concat_finite_series` (theorem, [line 73](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L73)). An exercise, stated without proof.

> Lemma 7.1.4(a) / Exercise 7.1.1

```lean
theorem concat_finite_series {m n p:ℤ} (hmn: m ≤ n+1) (hpn : n ≤ p) (a: ℤ → ℝ) :
  ∑ i ∈ Icc m n, a i + ∑ i ∈ Icc (n+1) p, a i = ∑ i ∈ Icc m p, a i
```

## Lemma 7.1.4(b) / Exercise 7.1.1

`Finset.shift_finite_series` (theorem, [line 77](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L77)). An exercise, stated without proof.

> Lemma 7.1.4(b) / Exercise 7.1.1

```lean
theorem shift_finite_series {m n k:ℤ} (a: ℤ → ℝ) :
  ∑ i ∈ Icc m n, a i = ∑ i ∈ Icc (m+k) (n+k), a (i-k)
```

## Lemma 7.1.4(c) / Exercise 7.1.1

`Finset.finite_series_add` (theorem, [line 81](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L81)). An exercise, stated without proof.

> Lemma 7.1.4(c) / Exercise 7.1.1

```lean
theorem finite_series_add {m n:ℤ} (a b: ℤ → ℝ) :
  ∑ i ∈ Icc m n, (a i + b i) = ∑ i ∈ Icc m n, a i + ∑ i ∈ Icc m n, b i
```

## Lemma 7.1.4(d) / Exercise 7.1.1

`Finset.finite_series_const_mul` (theorem, [line 85](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L85)). An exercise, stated without proof.

> Lemma 7.1.4(d) / Exercise 7.1.1

```lean
theorem finite_series_const_mul {m n:ℤ} (a: ℤ → ℝ) (c:ℝ) :
  ∑ i ∈ Icc m n, c * a i = c * ∑ i ∈ Icc m n, a i
```

## Lemma 7.1.4(e) / Exercise 7.1.1

`Finset.abs_finite_series_le` (theorem, [line 89](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L89)). An exercise, stated without proof.

> Lemma 7.1.4(e) / Exercise 7.1.1

```lean
theorem abs_finite_series_le {m n:ℤ} (a: ℤ → ℝ) :
  |∑ i ∈ Icc m n, a i| ≤ ∑ i ∈ Icc m n, |a i|
```

## Lemma 7.1.4(f) / Exercise 7.1.1

`Finset.finite_series_of_le` (theorem, [line 93](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L93)). An exercise, stated without proof.

> Lemma 7.1.4(f) / Exercise 7.1.1

```lean
theorem finite_series_of_le {m n:ℤ}  {a b: ℤ → ℝ} (h: ∀ i, m ≤ i → i ≤ n → a i ≤ b i) :
  ∑ i ∈ Icc m n, a i ≤ ∑ i ∈ Icc m n, b i
```

## Proposition 7.1.8

`Finset.finite_series_of_rearrange` (theorem, [line 102](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L102)). Stated without proof.

> Proposition 7.1.8.

```lean
theorem finite_series_of_rearrange {n:ℕ} {X':Type*} (X: Finset X') (hcard: X.card = n)
  (f: X' → ℝ) (g h: Icc (1:ℤ) n → X) (hg: Function.Bijective g) (hh: Function.Bijective h) :
    ∑ i ∈ Icc (1:ℤ) n, (if hi:i ∈ Icc (1:ℤ) n then f (g ⟨ i, hi ⟩) else 0)
    = ∑ i ∈ Icc (1:ℤ) n, (if hi: i ∈ Icc (1:ℤ) n then f (h ⟨ i, hi ⟩) else 0)
```

## Definition 7.1.6

`Finset.finite_series_eq` (theorem, [line 182](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L182)). Proved here.

> Definition 7.1.6

```lean
theorem finite_series_eq {n:ℕ} {Y:Type*} (X: Finset Y) (f: Y → ℝ) (g: Icc (1:ℤ) n → X)
  (hg: Function.Bijective g) :
    ∑ i ∈ X, f i = ∑ i ∈ Icc (1:ℤ) n, (if hi:i ∈ Icc (1:ℤ) n then f (g ⟨ i, hi ⟩) else 0)
```

## Proposition 7.1.11(a) / Exercise 7.1.2

`Finset.finite_series_of_empty` (theorem, [line 193](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L193)). An exercise, stated without proof.

> Proposition 7.1.11(a) / Exercise 7.1.2

```lean
theorem finite_series_of_empty {X':Type*} (f: X' → ℝ) : ∑ i ∈ ∅, f i = 0
```

## Proposition 7.1.11(b) / Exercise 7.1.2

`Finset.finite_series_of_singleton` (theorem, [line 196](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L196)). An exercise, stated without proof.

> Proposition 7.1.11(b) / Exercise 7.1.2

```lean
theorem finite_series_of_singleton {X':Type*} (f: X' → ℝ) (x₀:X') : ∑ i ∈ {x₀}, f i = f x₀
```

## Proposition 7.1.11(c) / Exercise 7.1.2

`Finset.map_finite_series` (theorem, [line 207](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L207)). An exercise, stated without proof.

> Proposition 7.1.11(c) / Exercise 7.1.2

```lean
theorem map_finite_series {X:Type*} [Fintype X] [Fintype Y] (f: X → ℝ) {g:Y → X}
  (hg: Function.Bijective g) :
    ∑ x, f x = ∑ y, f (g y)
```

## Proposition 7.1.11(e) / Exercise 7.1.2

`Finset.finite_series_of_disjoint_union` (theorem, [line 214](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L214)). An exercise, stated without proof.

> Proposition 7.1.11(e) / Exercise 7.1.2

```lean
theorem finite_series_of_disjoint_union {Z:Type*} {X Y: Finset Z} (hdisj: Disjoint X Y) (f: Z → ℝ) :
    ∑ z ∈ X ∪ Y, f z = ∑ z ∈ X, f z + ∑ z ∈ Y, f z
```

## Proposition 7.1.11(f) / Exercise 7.1.2

`Finset.finite_series_of_add` (theorem, [line 218](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L218)). An exercise, stated without proof.

> Proposition 7.1.11(f) / Exercise 7.1.2

```lean
theorem finite_series_of_add {X':Type*} (f g: X' → ℝ) (X: Finset X') :
    ∑ x ∈ X, (f + g) x = ∑ x ∈ X, f x + ∑ x ∈ X, g x
```

## Proposition 7.1.11(g) / Exercise 7.1.2

`Finset.finite_series_of_const_mul` (theorem, [line 222](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L222)). An exercise, stated without proof.

> Proposition 7.1.11(g) / Exercise 7.1.2

```lean
theorem finite_series_of_const_mul {X':Type*} (f: X' → ℝ) (X: Finset X') (c:ℝ) :
    ∑ x ∈ X, c * f x = c * ∑ x ∈ X, f x
```

## Proposition 7.1.11(h) / Exercise 7.1.2

`Finset.finite_series_of_le'` (theorem, [line 226](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L226)). An exercise, stated without proof.

> Proposition 7.1.11(h) / Exercise 7.1.2

```lean
theorem finite_series_of_le' {X':Type*} (f g: X' → ℝ) (X: Finset X') (h: ∀ x ∈ X, f x ≤ g x) :
    ∑ x ∈ X, f x ≤ ∑ x ∈ X, g x
```

## Proposition 7.1.11(i) / Exercise 7.1.2

`Finset.abs_finite_series_le'` (theorem, [line 230](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L230)). An exercise, stated without proof.

> Proposition 7.1.11(i) / Exercise 7.1.2

```lean
theorem abs_finite_series_le' {X':Type*} (f: X' → ℝ) (X: Finset X') :
    |∑ x ∈ X, f x| ≤ ∑ x ∈ X, |f x|
```

## Lemma 7.1.13

`Finset.finite_series_of_finite_series` (theorem, [line 234](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L234)). Stated without proof.

> Lemma 7.1.13

```lean
theorem finite_series_of_finite_series {XX YY:Type*} (X: Finset XX) (Y: Finset YY)
  (f: XX × YY → ℝ) :
    ∑ x ∈ X, ∑ y ∈ Y, f (x, y) = ∑ z ∈ X.product Y, f z
```

## Corollary 7.1.14

`Finset.finite_series_refl` (theorem, [line 271](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L271)). Proved here.

> Corollary 7.1.14 (Fubini's theorem for finite series).

```lean
theorem finite_series_refl {XX YY:Type*} (X: Finset XX) (Y: Finset YY) (f: XX × YY → ℝ) :
    ∑ z ∈ X.product Y, f z = ∑ z ∈ Y.product X, f (z.2, z.1)
```

## Exercise 7.1.4

`Finset.binomial_theorem` (theorem, [line 301](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L301)). An exercise, stated without proof.

> Exercise 7.1.4. Note: there may be some technicalities passing back and forth between natural
> numbers and integers. Look into the tactics `zify`, `norm_cast`, and `omega`

```lean
theorem binomial_theorem (x y:ℝ) (n:ℕ) :
    (x + y)^n
    = ∑ j ∈ Icc (0:ℤ) n,
    n.factorial / (j.toNat.factorial * (n-j).toNat.factorial) * x^j * y^(n - j)
```

## Exercise 7.1.5

`Finset.lim_of_finite_series` (theorem, [line 308](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L308)). An exercise, stated without proof.

> Exercise 7.1.5

```lean
theorem lim_of_finite_series {X:Type*} [Fintype X] (a: X → ℕ → ℝ) (L : X → ℝ)
  (h: ∀ x, Filter.atTop.Tendsto (a x) (nhds (L x))) :
    Filter.atTop.Tendsto (fun n ↦ ∑ x, a x n) (nhds (∑ x, L x))
```

## Exercise 7.1.6

`Finset.sum_union_disjoint` (theorem, [line 314](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L314)). An exercise, stated without proof.

> Exercise 7.1.6

```lean
theorem sum_union_disjoint {n : ℕ} {S : Type*} [Fintype S]
    (E : Fin n → Finset S)
    (disj : ∀ i j : Fin n, i ≠ j → Disjoint (E i) (E j))
    (cover : ∀ s : S, ∃ i, s ∈ E i)
    (f : S → ℝ) :
    ∑ s, f s = ∑ i, ∑ s ∈ E i, f s
```

## Exercise 7.1.7

`Finset.sum_finite_col_row_counts` (theorem, [line 324](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean#L324)). An exercise, stated without proof.

> `aᵢ` Exercise 7.1.7. Uses `Fin m` (so `aᵢ < m`) instead of the book's `aᵢ ≤ m`;
> the bound is baked into the type, and `<` replaces `≤` to match the 0-indexed shift.

```lean
theorem sum_finite_col_row_counts {n m : ℕ} (a : Fin n → Fin m) :
    ∑ i, (a i : ℕ) = ∑ j : Fin m, {i : Fin n | j < a i}.toFinset.card
```

## Depends on

Its Lean file imports no other section's file.

## Sources

- [Analysis/Section_7_1.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_7_1.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_7_1/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_7_1.html)
