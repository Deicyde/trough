---
declaration: abbrev
origin: cited
lean: Chapter8.CartesianProduct, Chapter8.Function.equiv, Chapter8.axiom_of_choice, Chapter8.exist_tendsTo_sup, Chapter8.exist_tendsTo_sup_of_closed, Chapter8.exists_function, Chapter8.axiom_of_choice_from_exists_function, Chapter8.exists_set_singleton_intersect, Chapter8.axiom_of_choice_from_exists_set_singleton_intersect, Chapter8.Function.Injective.inv_surjective, Chapter8.axiom_of_choice_from_function_injective_inv_surjective
statement: formalized
---

# Section 8.4: The axiom of choice

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Review of Mathlib's dependent product type `∀ α, X α`.
> - The axiom of choice in various equivalent forms, as well as the countable axiom of choice.
>
> As the Chapter 3 set theory has been deprecated for many chapters at this point, we will not insert the axiom of choice directly into that theory in this text; but this could be accomplished if desired
> (e.g., by extending the `Chapter3.SetTheory` class to a `Chapter3.SetTheoryWithChoice` class), and
> students are welcome to attempt this separately.  Instead, we will use Mathlib's native
> `Classical.choice` axiom.  Technically, this axiom has already been used quite frequently in the
> text already, in large part because Mathlib uses `Classical.choice` to derive many weaker statements,
> such as the law of the excluded middle.  So the distinctions made in the original text regarding
> whether a given statement or not uses the axiom of choice are somewhat blurred in this formalization.
> It is theoretically possible to restore this distinction by removing the reliance on Mathlib and
> working throughout with custom structures such as `Chapter3.SetTheory` and
> `Chapter3.SetTheoryWithChoice`, but this would be extremely tedious and not attempted here.

*Quoted from [Analysis/Section_8_4.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_4.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 9 labelled items, carried by 11 declarations: 3 proved here, 6 stated without proof (6 of them exercises) and 2 definitions. It also has 6 declarations with no label, counted here but not shown.

## Definition 8.4.1

`Chapter8.CartesianProduct` (abbrev, [line 43](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_4.lean#L43)). A definition.

> Definition 8.4.1 (Infinite Cartesian products).  We will avoid using this definition in favor
> of the Mathlib form `∀ α, X α` which we will shortly show is equivalent to (or more precisely,
> generalizes) this one.
>
>
> Because Lean does not allow unrestricted unions of types, we cheat slightly here by assuming all the
> `X α` are sets in a common universe `U`.  Note that the Mathlib definition does not have this
> restriction.

```lean
abbrev CartesianProduct {I U: Type} (X : I → Set U)
```

## Example 8.4.2

`Chapter8.Function.equiv` (def, [line 55](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_4.lean#L55)). A definition.

> Example 8.4.2.

```lean
def Function.equiv {I X:Type} : (∀ _:I, X) ≃ (I → X)
```

## Axiom 8.1

`Chapter8.axiom_of_choice` (theorem, [line 96](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_4.lean#L96)). Proved here.

> Axiom 8.1 (Choice)

```lean
theorem axiom_of_choice {I: Type} {X: I → Type} (h : ∀ i, Nonempty (X i)) :
  Nonempty (∀ i, X i)
```

## Lemma 8.4.5

`Chapter8.exist_tendsTo_sup` (theorem, [line 103](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_4.lean#L103)). Proved here.

> Lemma 8.4.5

```lean
theorem exist_tendsTo_sup {E: Set ℝ} (hnon: E.Nonempty) (hbound: BddAbove E) :
  ∃ a : ℕ → ℝ, (∀ n, a n ∈ E) ∧ Filter.atTop.Tendsto a (nhds (sSup E))
```

## Remark 8.4.6

`Chapter8.exist_tendsTo_sup_of_closed` (theorem, [line 122](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_4.lean#L122)). Proved here.

> Remark 8.4.6.  This special case of Lemma 8.4.5 avoids (countable) choice.

```lean
theorem exist_tendsTo_sup_of_closed {E: Set ℝ} (hnon: E.Nonempty) (hbound: BddAbove E) (hclosed: IsClosed E) :
  ∃ a : ℕ → ℝ, (∀ n, a n ∈ E) ∧ Filter.atTop.Tendsto a (nhds (sSup E))
```

## Proposition 8.4.7 / Exercise 8.4.1

`Chapter8.exists_function` (theorem, [line 145](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_4.lean#L145)). An exercise, stated without proof.

> Proposition 8.4.7 / Exercise 8.4.1

```lean
theorem exists_function {X Y : Type} {P : X → Y → Prop} (h: ∀ x, ∃ y, P x y) :
  ∃ f : X → Y, ∀ x, P x (f x)
```

## Exercise 8.4.1

`Chapter8.axiom_of_choice_from_exists_function` (theorem, [line 152](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_4.lean#L152)). An exercise, stated without proof.

> Exercise 8.4.1.  The spirit of the question here is to establish this result directly
> from `exists_function`, avoiding previous results that relied more explicitly
> on the axiom of choice.

```lean
theorem axiom_of_choice_from_exists_function {I: Type} {X: I → Type} (h : ∀ i, Nonempty (X i)) :
  Nonempty (∀ i, X i)
```

## Exercise 8.4.2

`Chapter8.exists_set_singleton_intersect` (theorem, [line 157](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_4.lean#L157)). An exercise, stated without proof.

> Exercise 8.4.2

```lean
theorem exists_set_singleton_intersect {I U:Type} {X: I → Set U} (h: Set.PairwiseDisjoint .univ X)
  (hnon: ∀ α, Nonempty (X α)) :
  ∃ Y : Set U, ∀ α, Nat.card (Y ∩ X α : Set U) = 1
```

`Chapter8.axiom_of_choice_from_exists_set_singleton_intersect` (theorem, [line 165](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_4.lean#L165)). An exercise, stated without proof.

> Exercise 8.4.2.  The spirit of the question here is to establish this result directly
> from `exists_set_singleton_intersect`, avoiding previous results that relied more explicitly
> on the axiom of choice.

```lean
theorem axiom_of_choice_from_exists_set_singleton_intersect {I: Type} {X: I → Type} (h : ∀ i, Nonempty (X i)) :
  Nonempty (∀ i, X i)
```

## Exercise 8.4.3

`Chapter8.Function.Injective.inv_surjective` (theorem, [line 170](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_4.lean#L170)). An exercise, stated without proof.

> Exercise 8.4.3

```lean
theorem Function.Injective.inv_surjective {A B:Type} {g: B → A} (hg: Function.Surjective g) :
  ∃ f : A → B, Function.Injective f ∧ Function.RightInverse f g
```

`Chapter8.axiom_of_choice_from_function_injective_inv_surjective` (theorem, [line 177](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_4.lean#L177)). An exercise, stated without proof.

> Exercise 8.4.3.  The spirit of the question here is to establish this result directly
> from `Function.Injective.inv_surjective`, avoiding previous results that relied more explicitly
> on the axiom of choice.

```lean
theorem axiom_of_choice_from_function_injective_inv_surjective {I: Type} {X: I → Type} (h : ∀ i, Nonempty (X i)) :
  Nonempty (∀ i, X i)
```

## Depends on

- [Section 8.1: Countability](section-8-1.md)
- [Section 8.2: Summation on infinite sets](section-8-2.md)

## Sources

- [Analysis/Section_8_4.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_8_4.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_8_4/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_8_4.html)
