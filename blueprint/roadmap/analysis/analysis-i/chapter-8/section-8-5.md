---
declaration: theorem
origin: cited
lean: Chapter8.IsMax.iff, Chapter8.WellFoundedLT.iff, Chapter8.IsMax.ofFinite, Chapter8.IsMin.ofFinite, Chapter8.WellFoundedLT.ofFinite, Chapter8.WellFoundedLT.strong_induction, Chapter8.IsUpperBound, Chapter8.WellFoundedLT.partialOrder, Chapter8.Zorns_lemma, Chapter8.empty_set_partial_order, Chapter8.PNat.divOrder, Chapter8.OrderIdeals, Chapter8.Lex', Chapter8.inj_trichotomy, Chapter8.PartialOrder.coarserOrder, Chapter8.exists_set_singleton_intersect', Chapter8.hausdorff_of_zorns_lemma, Chapter8.WellOrderedSubset, Chapter8.maximal_disjoint_subcollection
statement: formalized
---

# Section 8.5: Ordered sets

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Review of `PartialOrder`, `LinearOrder`, and `WellFoundedLT`, with some API.
> - Strong induction.
> - Zorn's lemma.

*Quoted from [Analysis/Section_8_5.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 31 labelled items, carried by 31 declarations: 5 proved here, 19 stated without proof (16 of them exercises) and 7 definitions (2 with a value left as `sorry`). It also has 41 declarations and 23 examples with no label, counted here but not shown.

## Definition 8.5.1

An `example` ([line 27](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L27)). Proved here.

> Definition 8.5.1 - Here we just review the Mathlib `PartialOrder` class.

```lean
example {X:Type} [PartialOrder X] (x:X) : x ≤ x
```

## Definition 8.5.3

An `example` ([line 47](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L47)). Proved here.

> Definition 8.5.3.  Here we just review the Mathlib `LinearOrder` class.

```lean
example {X:Type} [LinearOrder X] : PartialOrder X
```

## Definition 8.5.5

`Chapter8.IsMax.iff` (theorem, [line 83](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L83)). Proved here.

> Definition 8.5.5 (Maximal and minimal elements).  Here we use Mathlib's `IsMax` and `IsMin`.

```lean
theorem IsMax.iff {X:Type} [PartialOrder X] (x:X) :
  IsMax x ↔ ¬ ∃ y, x < y
```

## Examples 8.5.6

An `example` ([line 90](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L90)). Stated without proof.

> Examples 8.5.6

```lean
example : IsMin (⟨ {2}, by aesop ⟩ : X_8_5_4)
```

## Example 8.5.7

An `example` ([line 97](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L97)). Stated without proof.

> Example 8.5.7

```lean
example : IsMin (0:ℕ)
```

## Definition 8.5.8

`Chapter8.WellFoundedLT.iff` (theorem, [line 102](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L102)). Proved here.

> Definition 8.5.8.  We use `[LinearOrder X] [WellFoundedLT X]` to describe well-ordered sets.

```lean
theorem WellFoundedLT.iff (X:Type) [LinearOrder X] :
  WellFoundedLT X ↔ ∀ A:Set X, A.Nonempty → ∃ x:A, IsMin x
```

## Example 8.5.9

An `example` ([line 116](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L116)). Proved here.

> Example 8.5.9

```lean
example : WellFoundedLT ℕ
```

## Exercise 8.1.2

An `example` ([line 122](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L122)). An exercise, stated without proof.

> Exercise 8.1.2

```lean
example : ¬ WellFoundedLT ℤ
```

## Exercise 8.5.8 (i)

`Chapter8.IsMax.ofFinite` (theorem, [line 127](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L127)). An exercise, stated without proof.

> Exercise 8.5.8 (i)

```lean
theorem IsMax.ofFinite {X:Type} [LinearOrder X] [Finite X] [Nonempty X] : ∃ x:X, IsMax x
```

## Exercise 8.5.8 (ii)

`Chapter8.IsMin.ofFinite` (theorem, [line 130](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L130)). An exercise, stated without proof.

> Exercise 8.5.8 (ii)

```lean
theorem IsMin.ofFinite {X:Type} [LinearOrder X] [Finite X] [Nonempty X] : ∃ x:X, IsMin x
```

## Exercise 8.5.8 (iii)

`Chapter8.WellFoundedLT.ofFinite` (theorem, [line 133](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L133)). An exercise, stated without proof.

> Exercise 8.5.8 (iii)

```lean
theorem WellFoundedLT.ofFinite {X:Type} [LinearOrder X] [Finite X] : WellFoundedLT X
```

## Proposition 8.5.10 / Exercise 8.5.10

`Chapter8.WellFoundedLT.strong_induction` (theorem, [line 148](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L148)). An exercise, stated without proof.

> Proposition 8.5.10 / Exercise 8.5.10

```lean
theorem WellFoundedLT.strong_induction {X:Type} [LinearOrder X] [WellFoundedLT X] {P:X → Prop}
  (h: ∀ n, (∀ m < n, P m) → P n) : ∀ n, P n
```

## Definition 8.5.12

`Chapter8.IsUpperBound` (abbrev, [line 153](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L153)). A definition.

> Definition 8.5.12 (Upper bounds and strict upper bounds)

```lean
abbrev IsUpperBound {X:Type} [PartialOrder X] (A:Set X) (x:X) : Prop
```

## Exercise 8.5.11

An `example` ([line 191](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L191)). An exercise, stated without proof.

> Exercise 8.5.11

```lean
example {X:Type} [PartialOrder X] {Y Y':Set X} (hY: IsTotal Y) (hY': IsTotal Y') (hY_well: WellFoundedLT Y) (hY'_well: WellFoundedLT Y') (hYY': IsTotal (Y ∪ Y': Set X)) : WellFoundedLT (Y ∪ Y': Set X)
```

## Lemma 8.5.14

`Chapter8.WellFoundedLT.partialOrder` (theorem, [line 194](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L194)). Stated without proof.

> Lemma 8.5.14

```lean
theorem WellFoundedLT.partialOrder {X:Type} [PartialOrder X] (x₀ : X) : ∃ Y : Set X, IsTotal Y ∧ WellFoundedLT Y ∧ (∃ hx₀ : x₀ ∈ Y, IsMin (⟨ x₀, hx₀ ⟩: Y)) ∧ ¬ ∃ x, IsStrictUpperBound Y x
```

## Lemma 8.5.15 / Exercise 8.5.14

`Chapter8.Zorns_lemma` (theorem, [line 311](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L311)). An exercise, stated without proof.

> Lemma 8.5.15 (Zorn's lemma) / Exercise 8.5.14

```lean
theorem Zorns_lemma {X:Type} [PartialOrder X] [Nonempty X]
  (hchain: ∀ Y:Set X, IsTotal Y ∧ Y.Nonempty → ∃ x, IsUpperBound Y x) : ∃ x:X, IsMax x
```

## Exercise 8.5.1

`Chapter8.empty_set_partial_order` (def, [line 316](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L316)). A definition whose value is left as `sorry`.

> Exercise 8.5.1

```lean
def empty_set_partial_order [h₀: LE Empty] : Decidable (∃ h : PartialOrder Empty, h.le = h₀.le)
```

## Exercise 8.5.2

An `example` ([line 326](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L326)). An exercise, stated without proof.

> Exercise 8.5.2

```lean
example : ∃ (X:Type) (h₀: LE X), (∀ x:X, x ≤ x) ∧ (∀ x y:X, x ≤ y → y ≤ x → x = y) ∧ ¬ (∀ x y z:X, x ≤ y → y ≤ z → x ≤ z)
```

## Exercise 8.5.3

`Chapter8.PNat.divOrder` (def, [line 333](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L333)). A definition whose value is left as `sorry`.

> Exercise 8.5.3: The divisibility ordering on PNat.

```lean
def PNat.divOrder : PartialOrder PNat
```

## Exercise 8.5.4

An `example` ([line 350](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L350)). An exercise, stated without proof.

> Exercise 8.5.4

```lean
example : ¬ ∃ x : {x:ℝ| x > 0}, IsMin x
```

## Exercise 8.5.5

An `example` ([line 353](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L353)). An exercise, stated without proof.

> Exercise 8.5.5

```lean
example {X Y:Type} [PartialOrder Y] (f:X → Y) : ∃ h₀: PartialOrder X, h₀.le = (fun x y ↦ f x < f y ∨ x = y)
```

## Exercise 8.5.6

`Chapter8.OrderIdeals` (abbrev, [line 361](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L361)). A definition.

> Exercise 8.5.6

```lean
abbrev OrderIdeals (X: Type) [PartialOrder X] : Set (Set X)
```

## Exercise 8.5.7

An `example` ([line 372](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L372)). An exercise, stated without proof.

> Exercise 8.5.7

```lean
example {Y:Type} [LinearOrder Y] {x y:Y} (hx: IsMin x) (hy: IsMin y) : x = y
```

## Exercise 8.5.9

An `example` ([line 379](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L379)). An exercise, stated without proof.

> Exercise 8.5.9

```lean
example {X:Type} [LinearOrder X] (hmin: ∀ Y: Set X, Y.Nonempty → ∃ x:Y, IsMin x) (hmax: ∀ Y: Set X, Y.Nonempty → ∃ x:Y, IsMax x) : Finite X
```

## Exercise 8.5.12

`Chapter8.Lex'` (def, [line 385](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L385)). A definition.

> Exercise 8.5.12.  Here we make a copy of Mathlib's `Lex` wrapper for lexicographical orderings.  This wrapper is needed
> because products `X × Y` of ordered sets are given the default instance of the product partial order instead of
> the lexicographical one.

```lean
def Lex' (α : Type)
```

## Exercise 8.5.15

`Chapter8.inj_trichotomy` (theorem, [line 401](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L401)). An exercise, stated without proof.

> Exercise 8.5.15

```lean
theorem inj_trichotomy {X Y : Type}
    (h : ¬∃ f : X → Y, Function.Injective f) :
    ∃ g : Y → X, Function.Injective g
```

## Exercise 8.5.16

`Chapter8.PartialOrder.coarserOrder` (instance, [line 407](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L407)). A definition.

> Exercise 8.5.16: The set of partial orderings on X, ordered by "coarser than",
> is itself a partial order.

```lean
instance PartialOrder.coarserOrder (X : Type) : PartialOrder (PartialOrder X)
```

## Exercise 8.5.17

`Chapter8.exists_set_singleton_intersect'` (theorem, [line 448](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L448)). An exercise, stated without proof.

> Exercise 8.5.17: Use Zorn's lemma to reprove Exercise 8.4.2

```lean
theorem exists_set_singleton_intersect' {I U : Type} {X : I → Set U}
    (h : Set.PairwiseDisjoint .univ X) (hne : ∀ α, Nonempty (X α)) :
    ∃ Y : Set U, ∀ α, Nat.card (Y ∩ X α : Set U) = 1
```

## Exercise 8.5.18

`Chapter8.hausdorff_of_zorns_lemma` (theorem, [line 453](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L453)). An exercise, stated without proof.

> Exercise 8.5.18

```lean
theorem hausdorff_of_zorns_lemma {X : Type} [PartialOrder X] :
    ∃ M : Set X, Maximal (fun (S : Set X) => IsTotal S) M
```

## Exercise 8.5.19

`Chapter8.WellOrderedSubset` (structure, [line 463](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L463)). A definition.

> Exercise 8.5.19: A well-ordered subset of X: a subset with a linear order and
> well-foundedness.

```lean
structure WellOrderedSubset (X : Type)
```

## Exercise 8.5.20

`Chapter8.maximal_disjoint_subcollection` (theorem, [line 524](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean#L524)). An exercise, stated without proof.

> Exercise 8.5.20

```lean
theorem maximal_disjoint_subcollection {X : Type} (Ω : Set (Set X)) (hne : ∅ ∉ Ω) :
    ∃ Ω' ⊆ Ω, Ω'.Pairwise Disjoint ∧
      (∀ C ∈ Ω, ∃ A ∈ Ω', (C ∩ A).Nonempty)
```

## Depends on

- [Section 8.4: The axiom of choice](section-8-4.md)

## Sources

- [Analysis/Section_8_5.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_5.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_8_5/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_8_5.html)
