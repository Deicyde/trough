---
declaration: abbrev
origin: cited
lean: Chapter3.SetTheory.Set.EqualCard, Chapter3.SetTheory.Set.Example_3_6_2, Chapter3.SetTheory.Set.Example_3_6_3, Chapter3.SetTheory.Set.EqualCard.inst_setoid, Chapter3.SetTheory.Set.has_card, Chapter3.SetTheory.Set.Remark_3_6_6, Chapter3.SetTheory.Set.Example_3_6_7a, Chapter3.SetTheory.Set.pos_card_nonempty, Chapter3.SetTheory.Set.card_erase, Chapter3.SetTheory.Set.has_card_zero, Chapter3.SetTheory.Set.card_uniq, Chapter3.SetTheory.Set.bounded_on_finite, Chapter3.SetTheory.Set.nat_infinite, Chapter3.SetTheory.Set.empty_iff_card_eq_zero, Chapter3.SetTheory.Set.card_insert, Chapter3.SetTheory.Set.card_union, Chapter3.SetTheory.Set.card_union_disjoint, Chapter3.SetTheory.Set.card_subset, Chapter3.SetTheory.Set.card_ssubset, Chapter3.SetTheory.Set.card_image, Chapter3.SetTheory.Set.card_image_inj, Chapter3.SetTheory.Set.card_prod, Chapter3.SetTheory.Set.card_pow, Chapter3.SetTheory.Set.prod_EqualCard_prod, Chapter3.SetTheory.Set.pow_pow_EqualCard_pow_prod, Chapter3.SetTheory.Set.injection_iff_card_le, Chapter3.SetTheory.Set.surjection_from_injection, Chapter3.SetTheory.Set.card_union_add_card_inter, Chapter3.SetTheory.Set.pigeonhole_principle, Chapter3.SetTheory.Set.two_to_two_iff, Chapter3.SetTheory.Set.Permutations, Chapter3.SetTheory.Set.Permutations_finite, Chapter3.SetTheory.Set.Permutations_ih, Chapter3.SetTheory.Set.Permutations_card
statement: formalized
---

# Section 3.6: Cardinality of sets

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
>
> Main constructions and results of this section:
>
> - Cardinality of a set
> - Finite and infinite sets
> - Connections with Mathlib equivalents
>
> After this section, these notions will be deprecated in favor of their Mathlib equivalents.
>
> ## Tips from past users
>
> Users of the companion who have completed the exercises in this section are welcome to send their tips for future users in this section as PRs.
>
> - (Add tip here)

*Quoted from [Analysis/Section_3_6.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 32 labelled items, carried by 34 declarations: 4 proved here, 26 stated without proof (22 of them exercises) and 4 definitions. It also has 51 declarations with no label, counted here but not shown.

## Definition 3.6.1

`Chapter3.SetTheory.Set.EqualCard` (abbrev, [line 38](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L38)). A definition.

> Definition 3.6.1 (Equal cardinality)

```lean
abbrev SetTheory.Set.EqualCard (X Y:Set) : Prop
```

## Example 3.6.2

`Chapter3.SetTheory.Set.Example_3_6_2` (theorem, [line 41](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L41)). Proved here.

> Example 3.6.2

```lean
theorem SetTheory.Set.Example_3_6_2 : EqualCard {0,1,2} {3,4,5}
```

## Example 3.6.3

`Chapter3.SetTheory.Set.Example_3_6_3` (theorem, [line 56](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L56)). Stated without proof.

> Example 3.6.3

```lean
theorem SetTheory.Set.Example_3_6_3 : EqualCard nat (nat.specify (fun x ↦ Even (x:ℕ)))
```

## Proposition 3.6.4 / Exercise 3.6.1

`Chapter3.SetTheory.Set.EqualCard.inst_setoid` (instance, [line 71](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L71)). A definition.

> Proposition 3.6.4 / Exercise 3.6.1

```lean
instance SetTheory.Set.EqualCard.inst_setoid : Setoid SetTheory.Set
```

## Definition 3.6.5

`Chapter3.SetTheory.Set.has_card` (abbrev, [line 74](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L74)). A definition.

> Definition 3.6.5

```lean
abbrev SetTheory.Set.has_card (X:Set) (n:ℕ) : Prop
```

## Remark 3.6.6

`Chapter3.SetTheory.Set.Remark_3_6_6` (theorem, [line 81](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L81)). Stated without proof.

> Remark 3.6.6

```lean
theorem SetTheory.Set.Remark_3_6_6 (n:ℕ) :
    (nat.specify (fun x ↦ 1 ≤ (x:ℕ) ∧ (x:ℕ) ≤ n)).has_card n
```

## Example 3.6.7

`Chapter3.SetTheory.Set.Example_3_6_7a` (theorem, [line 85](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L85)). Proved here.

> Example 3.6.7

```lean
theorem SetTheory.Set.Example_3_6_7a (a:Object) : ({a}:Set).has_card 1
```

## Lemma 3.6.9

`Chapter3.SetTheory.Set.pos_card_nonempty` (theorem, [line 114](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L114)). Stated without proof.

> Lemma 3.6.9

```lean
theorem SetTheory.Set.pos_card_nonempty {n:ℕ} (h: n ≥ 1) {X:Set} (hX: X.has_card n) : X ≠ ∅
```

`Chapter3.SetTheory.Set.card_erase` (theorem, [line 129](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L129)). Stated without proof.

> Lemma 3.6.9

```lean
theorem SetTheory.Set.card_erase {n:ℕ} (h: n ≥ 1) {X:Set} (hX: X.has_card n) (x:X) :
    (X \ {x.val}).has_card (n-1)
```

## Exercise 3.6.2a

`Chapter3.SetTheory.Set.has_card_zero` (theorem, [line 126](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L126)). An exercise, stated without proof.

> Exercise 3.6.2a

```lean
theorem SetTheory.Set.has_card_zero {X:Set} : X.has_card 0 ↔ X = ∅
```

## Proposition 3.6.8

`Chapter3.SetTheory.Set.card_uniq` (theorem, [line 151](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L151)). Proved here.

> Proposition 3.6.8 (Uniqueness of cardinality)

```lean
theorem SetTheory.Set.card_uniq {X:Set} {n m:ℕ} (h1: X.has_card n) (h2: X.has_card m) : n = m
```

## Exercise 3.6.3

`Chapter3.SetTheory.Set.bounded_on_finite` (theorem, [line 199](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L199)). An exercise, stated without proof.

> Exercise 3.6.3, phrased using Mathlib natural numbers

```lean
theorem SetTheory.Set.bounded_on_finite {n:ℕ} (f: Fin n → nat) : ∃ M, ∀ i, (f i:ℕ) ≤ M
```

## Theorem 3.6.12

`Chapter3.SetTheory.Set.nat_infinite` (theorem, [line 202](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L202)). Proved here.

> Theorem 3.6.12

```lean
theorem SetTheory.Set.nat_infinite : infinite nat
```

## Exercise 3.6.2

`Chapter3.SetTheory.Set.empty_iff_card_eq_zero` (theorem, [line 246](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L246)). An exercise, stated without proof.

> Exercise 3.6.2

```lean
theorem SetTheory.Set.empty_iff_card_eq_zero {X:Set} : X = ∅ ↔ X.finite ∧ X.card = 0
```

## Proposition 3.6.14 (a) / Exercise 3.6.4

`Chapter3.SetTheory.Set.card_insert` (theorem, [line 271](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L271)). An exercise, stated without proof.

> Proposition 3.6.14 (a) / Exercise 3.6.4

```lean
theorem SetTheory.Set.card_insert {X:Set} (hX: X.finite) {x:Object} (hx: x ∉ X) :
    (X ∪ {x}).finite ∧ (X ∪ {x}).card = X.card + 1
```

## Proposition 3.6.14 (b) / Exercise 3.6.4

`Chapter3.SetTheory.Set.card_union` (theorem, [line 275](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L275)). An exercise, stated without proof.

> Proposition 3.6.14 (b) / Exercise 3.6.4

```lean
theorem SetTheory.Set.card_union {X Y:Set} (hX: X.finite) (hY: Y.finite) :
    (X ∪ Y).finite ∧ (X ∪ Y).card ≤ X.card + Y.card
```

## Proposition 3.6.14 (b') / Exercise 3.6.4

`Chapter3.SetTheory.Set.card_union_disjoint` (theorem, [line 279](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L279)). An exercise, stated without proof.

> Proposition 3.6.14 (b') / Exercise 3.6.4

```lean
theorem SetTheory.Set.card_union_disjoint {X Y:Set} (hX: X.finite) (hY: Y.finite)
  (hdisj: Disjoint X Y) : (X ∪ Y).card = X.card + Y.card
```

## Proposition 3.6.14 (c) / Exercise 3.6.4

`Chapter3.SetTheory.Set.card_subset` (theorem, [line 283](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L283)). An exercise, stated without proof.

> Proposition 3.6.14 (c) / Exercise 3.6.4

```lean
theorem SetTheory.Set.card_subset {X Y:Set} (hX: X.finite) (hY: Y ⊆ X) :
    Y.finite ∧ Y.card ≤ X.card
```

## Proposition 3.6.14 (c') / Exercise 3.6.4

`Chapter3.SetTheory.Set.card_ssubset` (theorem, [line 287](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L287)). An exercise, stated without proof.

> Proposition 3.6.14 (c') / Exercise 3.6.4

```lean
theorem SetTheory.Set.card_ssubset {X Y:Set} (hX: X.finite) (hY: Y ⊂ X) :
    Y.card < X.card
```

## Proposition 3.6.14 (d) / Exercise 3.6.4

`Chapter3.SetTheory.Set.card_image` (theorem, [line 291](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L291)). An exercise, stated without proof.

> Proposition 3.6.14 (d) / Exercise 3.6.4

```lean
theorem SetTheory.Set.card_image {X Y:Set} (hX: X.finite) (f: X → Y) :
    (image f X).finite ∧ (image f X).card ≤ X.card
```

## Proposition 3.6.14 (d') / Exercise 3.6.4

`Chapter3.SetTheory.Set.card_image_inj` (theorem, [line 295](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L295)). An exercise, stated without proof.

> Proposition 3.6.14 (d') / Exercise 3.6.4

```lean
theorem SetTheory.Set.card_image_inj {X Y:Set} (hX: X.finite) {f: X → Y}
  (hf: Function.Injective f) : (image f X).card = X.card
```

## Proposition 3.6.14 (e) / Exercise 3.6.4

`Chapter3.SetTheory.Set.card_prod` (theorem, [line 299](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L299)). An exercise, stated without proof.

> Proposition 3.6.14 (e) / Exercise 3.6.4

```lean
theorem SetTheory.Set.card_prod {X Y:Set} (hX: X.finite) (hY: Y.finite) :
    (X ×ˢ Y).finite ∧ (X ×ˢ Y).card = X.card * Y.card
```

## Proposition 3.6.14 (f) / Exercise 3.6.4

`Chapter3.SetTheory.Set.card_pow` (theorem, [line 312](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L312)). An exercise, stated without proof.

> Proposition 3.6.14 (f) / Exercise 3.6.4

```lean
theorem SetTheory.Set.card_pow {X Y:Set} (hY: Y.finite) (hX: X.finite) :
    (Y ^ X).finite ∧ (Y ^ X).card = Y.card ^ X.card
```

## Exercise 3.6.5

`Chapter3.SetTheory.Set.prod_EqualCard_prod` (theorem, [line 316](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L316)). An exercise, stated without proof.

> Exercise 3.6.5. You might find `SetTheory.Set.prod_commutator` useful.

```lean
theorem SetTheory.Set.prod_EqualCard_prod (A B:Set) :
    EqualCard (A ×ˢ B) (B ×ˢ A)
```

## Exercise 3.6.6

`Chapter3.SetTheory.Set.pow_pow_EqualCard_pow_prod` (theorem, [line 323](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L323)). An exercise, stated without proof.

> Exercise 3.6.6. You may find `SetTheory.Set.curry_equiv` useful.

```lean
theorem SetTheory.Set.pow_pow_EqualCard_pow_prod (A B C:Set) :
    EqualCard ((A ^ B) ^ C) (A ^ (B ×ˢ C))
```

## Exercise 3.6.7

`Chapter3.SetTheory.Set.injection_iff_card_le` (theorem, [line 334](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L334)). An exercise, stated without proof.

> Exercise 3.6.7

```lean
theorem SetTheory.Set.injection_iff_card_le {A B:Set} (hA: A.finite) (hB: B.finite) :
    (∃ f:A → B, Function.Injective f) ↔ A.card ≤ B.card
```

## Exercise 3.6.8

`Chapter3.SetTheory.Set.surjection_from_injection` (theorem, [line 338](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L338)). An exercise, stated without proof.

> Exercise 3.6.8

```lean
theorem SetTheory.Set.surjection_from_injection {A B:Set} (hA: A ≠ ∅) (f: A → B)
  (hf: Function.Injective f) : ∃ g:B → A, Function.Surjective g
```

## Exercise 3.6.9

`Chapter3.SetTheory.Set.card_union_add_card_inter` (theorem, [line 342](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L342)). An exercise, stated without proof.

> Exercise 3.6.9

```lean
theorem SetTheory.Set.card_union_add_card_inter {A B:Set} (hA: A.finite) (hB: B.finite) :
    A.card + B.card = (A ∪ B).card + (A ∩ B).card
```

## Exercise 3.6.10

`Chapter3.SetTheory.Set.pigeonhole_principle` (theorem, [line 346](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L346)). An exercise, stated without proof.

> Exercise 3.6.10

```lean
theorem SetTheory.Set.pigeonhole_principle {n:ℕ} {A: Fin n → Set}
  (hA: ∀ i, (A i).finite) (hAcard: (iUnion _ A).card > n) : ∃ i, (A i).card ≥ 2
```

## Exercise 3.6.11

`Chapter3.SetTheory.Set.two_to_two_iff` (theorem, [line 350](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L350)). An exercise, stated without proof.

> Exercise 3.6.11

```lean
theorem SetTheory.Set.two_to_two_iff {X Y:Set} (f: X → Y): Function.Injective f ↔
    ∀ S ⊆ X, S.card = 2 → (image f S).card = 2
```

## Exercise 3.6.12

`Chapter3.SetTheory.Set.Permutations` (def, [line 354](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L354)). A definition.

> Exercise 3.6.12

```lean
def SetTheory.Set.Permutations (n: ℕ): Set
```

## Exercise 3.6.12 (i)

`Chapter3.SetTheory.Set.Permutations_finite` (theorem, [line 358](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L358)). An exercise, stated without proof.

> Exercise 3.6.12 (i), first part

```lean
theorem SetTheory.Set.Permutations_finite (n: ℕ): (Permutations n).finite
```

`Chapter3.SetTheory.Set.Permutations_ih` (theorem, [line 449](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L449)). An exercise, stated without proof.

> Exercise 3.6.12 (i), second part

```lean
theorem SetTheory.Set.Permutations_ih (n: ℕ):
    (Permutations (n + 1)).card = (n + 1) * (Permutations n).card
```

## Exercise 3.6.12 (ii)

`Chapter3.SetTheory.Set.Permutations_card` (theorem, [line 463](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean#L463)). An exercise, stated without proof.

> Exercise 3.6.12 (ii)

```lean
theorem SetTheory.Set.Permutations_card (n: ℕ):
    (Permutations n).card = n.factorial
```

## Depends on

- [Section 3.3: Functions](section-3-3.md)
- [Section 3.5: Cartesian products](section-3-5.md)

## Sources

- [Analysis/Section_3_6.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_6.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_3_6/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_3_6.html)
