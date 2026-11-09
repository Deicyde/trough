---
declaration: theorem
origin: cited
lean: Chapter8.Nat.exists_unique_min, Chapter8.Nat.monotone_enum_of_infinite, Chapter8.Nat.atMostCountable_subset, Chapter8.AtMostCountable.subset, Chapter8.AtMostCountable.image_nat, Chapter8.AtMostCountable.image, Chapter8.CountablyInfinite.union, Chapter8.Int.countablyInfinite, Chapter8.CountablyInfinite.lower_diag, Chapter8.CountablyInfinite.prod_nat, Chapter8.CountablyInfinite.prod, Chapter8.Rat.countablyInfinite, Chapter8.explicit_bijection
statement: formalized
---

# Section 8.1: Countability

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Custom notions for "equal cardinality", "countable", and "at most countable".  Note that Mathlib's
> `Countable` typeclass corresponds to what we call "at most countable" in this text.
> - Countability of the integers and rationals.
>
> Note that as the Chapter 3 set theory has been deprecated, we will not re-use relevant constructions from that theory here, replacing them with Mathlib counterparts instead.

*Quoted from [Analysis/Section_8_1.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_1.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 17 labelled items, carried by 17 declarations: 3 proved here, 13 stated without proof (8 of them exercises) and 1 definition (1 with a value left as `sorry`). It also has 30 declarations and 3 examples with no label, counted here but not shown.

## Examples 8.1.3

An `example` ([line 105](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_1.lean#L105)). Stated without proof.

> Examples 8.1.3

```lean
example : CountablyInfinite ℕ
```

## Proposition 8.1.4 / Exercise 8.1.2

`Chapter8.Nat.exists_unique_min` (theorem, [line 113](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_1.lean#L113)). An exercise, stated without proof.

> Proposition 8.1.4 (Well ordering principle) / Exercise 8.1.2

```lean
theorem Nat.exists_unique_min {X : Set ℕ} (hX : X.Nonempty) :
  ∃! m ∈ X, ∀ n ∈ X, m ≤ n
```

## Proposition 8.1.5

`Chapter8.Nat.monotone_enum_of_infinite` (theorem, [line 149](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_1.lean#L149)). Stated without proof.

> Proposition 8.1.5

```lean
theorem Nat.monotone_enum_of_infinite (X : Set ℕ) [Infinite X] : ∃! f : ℕ → X, Function.Bijective f ∧ StrictMono f
```

## Corollary 8.1.6

`Chapter8.Nat.atMostCountable_subset` (theorem, [line 192](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_1.lean#L192)). Proved here.

> Corollary 8.1.6

```lean
theorem Nat.atMostCountable_subset (X: Set ℕ) : AtMostCountable X
```

## Corollary 8.1.7

`Chapter8.AtMostCountable.subset` (theorem, [line 198](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_1.lean#L198)). Stated without proof.

> Corollary 8.1.7

```lean
theorem AtMostCountable.subset {X: Type} (hX : AtMostCountable X) (Y: Set X) : AtMostCountable Y
```

## Proposition 8.1.8 / Exercise 8.1.4

`Chapter8.AtMostCountable.image_nat` (theorem, [line 213](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_1.lean#L213)). An exercise, stated without proof.

> Proposition 8.1.8 / Exercise 8.1.4

```lean
theorem AtMostCountable.image_nat (Y: Type) (f: ℕ → Y) : AtMostCountable (f '' .univ)
```

## Corollary 8.1.9 / Exercise 8.1.5

`Chapter8.AtMostCountable.image` (theorem, [line 217](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_1.lean#L217)). An exercise, stated without proof.

> Corollary 8.1.9 / Exercise 8.1.5

```lean
theorem AtMostCountable.image {X:Type} (hX: CountablyInfinite X) {Y: Type} (f: X → Y) : AtMostCountable (f '' .univ)
```

## Proposition 8.1.10 / Exercise 8.1.7

`Chapter8.CountablyInfinite.union` (theorem, [line 221](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_1.lean#L221)). An exercise, stated without proof.

> Proposition 8.1.10 / Exercise 8.1.7

```lean
theorem CountablyInfinite.union {A:Type} {X Y: Set A} (hX: CountablyInfinite X) (hY: CountablyInfinite Y) :
  CountablyInfinite (X ∪ Y: Set A)
```

## Corollary 8.1.11

`Chapter8.Int.countablyInfinite` (theorem, [line 226](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_1.lean#L226)). Proved here.

> Corollary 8.1.11

```lean
theorem Int.countablyInfinite : CountablyInfinite ℤ
```

## Lemma 8.1.12

`Chapter8.CountablyInfinite.lower_diag` (theorem, [line 243](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_1.lean#L243)). Stated without proof.

> Lemma 8.1.12

```lean
theorem CountablyInfinite.lower_diag : CountablyInfinite { n : ℕ × ℕ | n.2 ≤ n.1 }
```

## Corollary 8.1.13

`Chapter8.CountablyInfinite.prod_nat` (theorem, [line 279](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_1.lean#L279)). Proved here.

> Corollary 8.1.13

```lean
theorem CountablyInfinite.prod_nat : CountablyInfinite (ℕ × ℕ)
```

## Corollary 8.1.14 / Exercise 8.1.8

`Chapter8.CountablyInfinite.prod` (theorem, [line 289](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_1.lean#L289)). An exercise, stated without proof.

> Corollary 8.1.14 / Exercise 8.1.8

```lean
theorem CountablyInfinite.prod {X Y:Type} (hX: CountablyInfinite X) (hY: CountablyInfinite Y) :
  CountablyInfinite (X × Y)
```

## Corollary 8.1.15

`Chapter8.Rat.countablyInfinite` (theorem, [line 294](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_1.lean#L294)). Stated without proof.

> Corollary 8.1.15

```lean
theorem Rat.countablyInfinite : CountablyInfinite ℚ
```

## Exercise 8.1.1

An `example` ([line 311](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_1.lean#L311)). An exercise, stated without proof.

> Exercise 8.1.1

```lean
example (X: Type) : Infinite X ↔ ∃ Y : Set X, Y ≠ .univ ∧ EqualCard Y X
```

## Exercise 8.1.6

An `example` ([line 315](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_1.lean#L315)). An exercise, stated without proof.

> Exercise 8.1.6

```lean
example (A: Type) : AtMostCountable A ↔ ∃ f : A → ℕ, Function.Injective f
```

## Exercise 8.1.9

An `example` ([line 319](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_1.lean#L319)). An exercise, stated without proof.

> Exercise 8.1.9

```lean
example {I X:Type} (hI: AtMostCountable I) (A: I → Set X) (hA: ∀ i, AtMostCountable (A i)) :
  AtMostCountable (⋃ i, A i)
```

## Exercise 8.1.10

`Chapter8.explicit_bijection` (abbrev, [line 323](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_1.lean#L323)). A definition whose value is left as `sorry`.

> Exercise 8.1.10.  Note the lack of the `noncomputable` keyword in the `abbrev`.

```lean
abbrev explicit_bijection : ℕ → ℚ
```

## Depends on

Its Lean file imports no other section's file.

## Sources

- [Analysis/Section_8_1.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_1.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_8_1/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_8_1.html)
