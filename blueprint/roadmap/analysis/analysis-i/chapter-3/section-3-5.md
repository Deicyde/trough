---
declaration: structure
origin: cited
lean: Chapter3.OrderedPair, Chapter3.OrderedPair.eq, Chapter3.OrderedPair.toObject, Chapter3.OrderedPair.toObject', Chapter3.SetTheory.Set.cartesian, Chapter3.SetTheory.Set.curry_equiv, Chapter3.SetTheory.Set.prod_commutator, Chapter3.SetTheory.Set.tuple, Chapter3.SetTheory.Set.iProd, Chapter3.SetTheory.Set.mem_iProd, Chapter3.SetTheory.Set.prod_associator, Chapter3.SetTheory.Set.singleton_iProd_equiv, Chapter3.SetTheory.Set.empty_iProd_equiv, Chapter3.SetTheory.Set.iProd_of_const_equiv, Chapter3.SetTheory.Set.iProd_equiv_prod, Chapter3.SetTheory.Set.iProd_equiv_prod_triple, Chapter3.SetTheory.Set.finite_choice, Chapter3.SetTheory.Set.Tuple.eq, Chapter3.OrderedPair.refl, Chapter3.SetTheory.Set.prod_union, Chapter3.SetTheory.Set.prod_inter, Chapter3.SetTheory.Set.prod_diff, Chapter3.SetTheory.Set.union_prod, Chapter3.SetTheory.Set.inter_prod, Chapter3.SetTheory.Set.diff_prod, Chapter3.SetTheory.Set.inter_of_prod, Chapter3.SetTheory.Set.union_of_prod, Chapter3.SetTheory.Set.diff_of_prod, Chapter3.SetTheory.Set.prod_subset_prod, Chapter3.SetTheory.Set.direct_sum, Chapter3.SetTheory.Set.iProd_empty_iff, Chapter3.SetTheory.Set.iUnion_inter_iUnion, Chapter3.SetTheory.Set.graph_inj, Chapter3.SetTheory.Set.powerset_axiom', Chapter3.SetTheory.Set.recursion, Chapter3.SetTheory.Set.nat_unique
statement: formalized
---

# Section 3.5: Cartesian products

> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - Ordered pairs and n-tuples.
> - Cartesian products and n-fold products.
> - Finite choice.
> - Connections with Mathlib counterparts such as `Set.pi` and `Set.prod`.
>
> ## Tips from past users
>
> Users of the companion who have completed the exercises in this section are welcome to send their tips for future users in this section as PRs.
>
> - (Add tip here)

*Quoted from [Analysis/Section_3_5.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 32 labelled items, carried by 37 declarations: 4 proved here, 17 stated without proof (17 of them exercises) and 16 definitions (10 with a value left as `sorry`). It also has 43 declarations and 1 example with no label, counted here but not shown.

## Definition 3.5.1

`Chapter3.OrderedPair` (structure, [line 41](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L41)). A definition.

> Definition 3.5.1 (Ordered pair).  One could also have used `Object × Object` to
> define `OrderedPair` here.

```lean
structure OrderedPair
```

`Chapter3.OrderedPair.eq` (theorem, [line 49](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L49)). Proved here.

> Definition 3.5.1 (Ordered pair)

```lean
theorem OrderedPair.eq (x y x' y' : Object) :
    (⟨ x, y ⟩ : OrderedPair) = (⟨ x', y' ⟩ : OrderedPair) ↔ x = x' ∧ y = y'
```

## Exercise 3.5.1

`Chapter3.OrderedPair.toObject` (def, [line 58](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L58)). A definition whose value is left as `sorry`.

> Exercise 3.5.1, first part

```lean
def OrderedPair.toObject : OrderedPair ↪ Object
```

`Chapter3.OrderedPair.toObject'` (abbrev, [line 367](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L367)). A definition whose value is left as `sorry`.

> Exercise 3.5.1, second part (requires axiom of regularity)

```lean
abbrev OrderedPair.toObject' : OrderedPair ↪ Object
```

## Definition 3.5.4

`Chapter3.SetTheory.Set.cartesian` (abbrev, [line 77](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L77)). A definition.

> Definition 3.5.4 (Cartesian product)

```lean
abbrev SetTheory.Set.cartesian (X Y:Set) : Set
```

## Example 3.5.5

An `example` ([line 145](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L145)). Proved here.

> Example 3.5.5

```lean
example : ({1, 2}: Set) ×ˢ ({3, 4, 5}: Set) = ({
  ((mk_cartesian (1: Nat) (3: Nat)): Object),
  ((mk_cartesian (1: Nat) (4: Nat)): Object),
  ((mk_cartesian (1: Nat) (5: Nat)): Object),
  ((mk_cartesian (2: Nat) (3: Nat)): Object),
  ((mk_cartesian (2: Nat) (4: Nat)): Object),
  ((mk_cartesian (2: Nat) (5: Nat)): Object)
}: Set)
```

`Chapter3.SetTheory.Set.curry_equiv` (abbrev, [line 162](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L162)). A definition.

> Example 3.5.5. A function of two variables can be thought of as a function of a pair.

```lean
noncomputable abbrev SetTheory.Set.curry_equiv {X Y Z:Set} : (X → Y → Z) ≃ (X ×ˢ Y → Z)
```

## Example 3.5.5 / Exercise 3.6.5

`Chapter3.SetTheory.Set.prod_commutator` (abbrev, [line 155](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L155)). A definition whose value is left as `sorry`.

> Example 3.5.5 / Exercise 3.6.5. There is a bijection between `X ×ˢ Y` and `Y ×ˢ X`.

```lean
noncomputable abbrev SetTheory.Set.prod_commutator (X Y:Set) : X ×ˢ Y ≃ Y ×ˢ X
```

## Definition 3.5.6

`Chapter3.SetTheory.Set.tuple` (abbrev, [line 171](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L171)). A definition.

> Definition 3.5.6.  The indexing set `I` plays the role of ${ i : 1 ≤ i ≤ n }$ in the text.
> See Exercise 3.5.10 below for some connections between this concept and the preceding notion
> of Cartesian product and ordered pair.

```lean
abbrev SetTheory.Set.tuple {I:Set} {X: I → Set} (x: ∀ i, X i) : Object
```

`Chapter3.SetTheory.Set.iProd` (abbrev, [line 175](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L175)). A definition.

> Definition 3.5.6 (indexed product)

```lean
abbrev SetTheory.Set.iProd {I: Set} (X: I → Set) : Set
```

`Chapter3.SetTheory.Set.mem_iProd` (theorem, [line 179](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L179)). Proved here.

> Definition 3.5.6 (membership in an indexed product)

```lean
theorem SetTheory.Set.mem_iProd {I: Set} {X: I → Set} (t:Object) :
    t ∈ iProd X ↔ ∃ x: ∀ i, X i, t = tuple x
```

## Example 3.5.8

`Chapter3.SetTheory.Set.prod_associator` (abbrev, [line 195](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L195)). A definition.

> Example 3.5.8. There is a bijection between `(X ×ˢ Y) ×ˢ Z` and `X ×ˢ (Y ×ˢ Z)`.

```lean
noncomputable abbrev SetTheory.Set.prod_associator (X Y Z:Set) : (X ×ˢ Y) ×ˢ Z ≃ X ×ˢ (Y ×ˢ Z)
```

## Example 3.5.10 (a)

`Chapter3.SetTheory.Set.singleton_iProd_equiv` (abbrev, [line 205](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L205)). A definition whose value is left as `sorry`.

> Example 3.5.10 (a). I suspect most of the equivalences will require classical reasoning and only be
> defined non-computably, but would be happy to learn of counterexamples.

```lean
noncomputable abbrev SetTheory.Set.singleton_iProd_equiv (i:Object) (X:Set) :
    iProd (fun _:({i}:Set) ↦ X) ≃ X
```

## Example 3.5.10 (b)

`Chapter3.SetTheory.Set.empty_iProd_equiv` (abbrev, [line 213](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L213)). A definition whose value is left as `sorry`.

> Example 3.5.10 (b)

```lean
abbrev SetTheory.Set.empty_iProd_equiv (X: (∅:Set) → Set) : iProd X ≃ Unit
```

## Example 3.5.10 (c)

`Chapter3.SetTheory.Set.iProd_of_const_equiv` (abbrev, [line 220](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L220)). A definition whose value is left as `sorry`.

> Example 3.5.10 (c)

```lean
noncomputable abbrev SetTheory.Set.iProd_of_const_equiv (I:Set) (X: Set) :
    iProd (fun _:I ↦ X) ≃ (I → X)
```

## Example 3.5.10 (d)

`Chapter3.SetTheory.Set.iProd_equiv_prod` (abbrev, [line 228](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L228)). A definition whose value is left as `sorry`.

> Example 3.5.10 (d)

```lean
noncomputable abbrev SetTheory.Set.iProd_equiv_prod (X: ({0,1}:Set) → Set) :
    iProd X ≃ (X ⟨ 0, by simp ⟩) ×ˢ (X ⟨ 1, by simp ⟩)
```

## Example 3.5.10 (e)

`Chapter3.SetTheory.Set.iProd_equiv_prod_triple` (abbrev, [line 236](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L236)). A definition whose value is left as `sorry`.

> Example 3.5.10 (e)

```lean
noncomputable abbrev SetTheory.Set.iProd_equiv_prod_triple (X: ({0,1,2}:Set) → Set) :
    iProd X ≃ (X ⟨ 0, by simp ⟩) ×ˢ (X ⟨ 1, by simp ⟩) ×ˢ (X ⟨ 2, by simp ⟩)
```

## Lemma 3.5.11

`Chapter3.SetTheory.Set.finite_choice` (theorem, [line 340](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L340)). Proved here.

> Lemma 3.5.11 (finite choice)

```lean
theorem SetTheory.Set.finite_choice {n:ℕ} {X: Fin n → Set} (h: ∀ i, X i ≠ ∅) : iProd X ≠ ∅
```

## Exercise 3.5.2

`Chapter3.SetTheory.Set.Tuple.eq` (theorem, [line 390](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L390)). An exercise, stated without proof.

> Exercise 3.5.2

```lean
theorem SetTheory.Set.Tuple.eq {n:ℕ} (t t':Tuple n) :
    t = t' ↔ ∀ n : Fin n, ((t.x n):Object) = ((t'.x n):Object)
```

## Exercise 3.5.3

`Chapter3.OrderedPair.refl` (theorem, [line 404](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L404)). An exercise, stated without proof.

> Exercise 3.5.3. The spirit here is to avoid direct rewrites (which make all of these claims
> trivial), and instead use `OrderedPair.eq` or `SetTheory.Set.tuple_inj`

```lean
theorem OrderedPair.refl (p: OrderedPair) : p = p
```

## Exercise 3.5.4 (a)

`Chapter3.SetTheory.Set.prod_union` (theorem, [line 421](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L421)). An exercise, stated without proof.

> Exercise 3.5.4 (a)

```lean
theorem SetTheory.Set.prod_union (A B C:Set) : A ×ˢ (B ∪ C) = (A ×ˢ B) ∪ (A ×ˢ C)
```

## Exercise 3.5.4 (b)

`Chapter3.SetTheory.Set.prod_inter` (theorem, [line 424](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L424)). An exercise, stated without proof.

> Exercise 3.5.4 (b)

```lean
theorem SetTheory.Set.prod_inter (A B C:Set) : A ×ˢ (B ∩ C) = (A ×ˢ B) ∩ (A ×ˢ C)
```

## Exercise 3.5.4 (c)

`Chapter3.SetTheory.Set.prod_diff` (theorem, [line 427](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L427)). An exercise, stated without proof.

> Exercise 3.5.4 (c)

```lean
theorem SetTheory.Set.prod_diff (A B C:Set) : A ×ˢ (B \ C) = (A ×ˢ B) \ (A ×ˢ C)
```

## Exercise 3.5.4 (d)

`Chapter3.SetTheory.Set.union_prod` (theorem, [line 430](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L430)). An exercise, stated without proof.

> Exercise 3.5.4 (d)

```lean
theorem SetTheory.Set.union_prod (A B C:Set) : (A ∪ B) ×ˢ C = (A ×ˢ C) ∪ (B ×ˢ C)
```

## Exercise 3.5.4 (e)

`Chapter3.SetTheory.Set.inter_prod` (theorem, [line 433](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L433)). An exercise, stated without proof.

> Exercise 3.5.4 (e)

```lean
theorem SetTheory.Set.inter_prod (A B C:Set) : (A ∩ B) ×ˢ C = (A ×ˢ C) ∩ (B ×ˢ C)
```

## Exercise 3.5.4 (f)

`Chapter3.SetTheory.Set.diff_prod` (theorem, [line 436](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L436)). An exercise, stated without proof.

> Exercise 3.5.4 (f)

```lean
theorem SetTheory.Set.diff_prod (A B C:Set) : (A \ B) ×ˢ C = (A ×ˢ C) \ (B ×ˢ C)
```

## Exercise 3.5.5 (a)

`Chapter3.SetTheory.Set.inter_of_prod` (theorem, [line 439](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L439)). An exercise, stated without proof.

> Exercise 3.5.5 (a)

```lean
theorem SetTheory.Set.inter_of_prod (A B C D:Set) :
    (A ×ˢ B) ∩ (C ×ˢ D) = (A ∩ C) ×ˢ (B ∩ D)
```

## Exercise 3.5.5 (b)

`Chapter3.SetTheory.Set.union_of_prod` (def, [line 443](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L443)). A definition whose value is left as `sorry`.

> Exercise 3.5.5 (b)

```lean
def SetTheory.Set.union_of_prod :
  Decidable (∀ (A B C D:Set), (A ×ˢ B) ∪ (C ×ˢ D) = (A ∪ C) ×ˢ (B ∪ D))
```

## Exercise 3.5.5 (c)

`Chapter3.SetTheory.Set.diff_of_prod` (def, [line 449](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L449)). A definition whose value is left as `sorry`.

> Exercise 3.5.5 (c)

```lean
def SetTheory.Set.diff_of_prod :
  Decidable (∀ (A B C D:Set), (A ×ˢ B) \ (C ×ˢ D) = (A \ C) ×ˢ (B \ D))
```

## Exercise 3.5.6

`Chapter3.SetTheory.Set.prod_subset_prod` (theorem, [line 457](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L457)). An exercise, stated without proof.

> Exercise 3.5.6.

```lean
theorem SetTheory.Set.prod_subset_prod {A B C D:Set}
  (hA: A ≠ ∅) (hB: B ≠ ∅) (hC: C ≠ ∅) (hD: D ≠ ∅) :
    A ×ˢ B ⊆ C ×ˢ D ↔ A ⊆ C ∧ B ⊆ D
```

## Exercise 3.5.7

`Chapter3.SetTheory.Set.direct_sum` (theorem, [line 467](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L467)). An exercise, stated without proof.

> Exercise 3.5.7

```lean
theorem SetTheory.Set.direct_sum {X Y Z:Set} (f: Z → X) (g: Z → Y) :
    ∃! h: Z → X ×ˢ Y, fst ∘ h = f ∧ snd ∘ h = g
```

## Exercise 3.5.8

`Chapter3.SetTheory.Set.iProd_empty_iff` (theorem, [line 472](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L472)). An exercise, stated without proof.

> Exercise 3.5.8

```lean
theorem SetTheory.Set.iProd_empty_iff {n:ℕ} {X: Fin n → Set} :
    iProd X = ∅ ↔ ∃ i, X i = ∅
```

## Exercise 3.5.9

`Chapter3.SetTheory.Set.iUnion_inter_iUnion` (theorem, [line 476](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L476)). An exercise, stated without proof.

> Exercise 3.5.9

```lean
theorem SetTheory.Set.iUnion_inter_iUnion {I J: Set} (A: I → Set) (B: J → Set) :
    (iUnion I A) ∩ (iUnion J B) = iUnion (I ×ˢ J) (fun p ↦ (A (fst p)) ∩ (B (snd p)))
```

## Exercise 3.5.10

`Chapter3.SetTheory.Set.graph_inj` (theorem, [line 483](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L483)). An exercise, stated without proof.

> Exercise 3.5.10

```lean
theorem SetTheory.Set.graph_inj {X Y:Set} (f f': X → Y) :
    graph f = graph f' ↔ f = f'
```

## Exercise 3.5.11

`Chapter3.SetTheory.Set.powerset_axiom'` (theorem, [line 494](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L494)). An exercise, stated without proof.

> Exercise 3.5.11. This trivially follows from `SetTheory.Set.powerset_axiom`, but the
> exercise is to derive it from `SetTheory.Set.exists_powerset` instead.

```lean
theorem SetTheory.Set.powerset_axiom' (X Y:Set) :
    ∃! S:Set, ∀(F:Object), F ∈ S ↔ ∃ f: Y → X, f = F
```

## Exercise 3.5.12

`Chapter3.SetTheory.Set.recursion` (theorem, [line 498](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L498)). An exercise, stated without proof.

> Exercise 3.5.12, with errata from web site incorporated

```lean
theorem SetTheory.Set.recursion (X: Set) (f: nat → X → X) (c:X) :
    ∃! a: nat → X, a 0 = c ∧ ∀ n, a (n + 1:ℕ) = f n (a n)
```

## Exercise 3.5.13

`Chapter3.SetTheory.Set.nat_unique` (theorem, [line 502](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean#L502)). An exercise, stated without proof.

> Exercise 3.5.13

```lean
theorem SetTheory.Set.nat_unique (nat':Set) (zero:nat') (succ:nat' → nat')
  (succ_ne: ∀ n:nat', succ n ≠ zero) (succ_of_ne: ∀ n m:nat', n ≠ m → succ n ≠ succ m)
  (ind: ∀ P: nat' → Prop, P zero → (∀ n, P n → P (succ n)) → ∀ n, P n) :
    ∃! f : nat → nat', Function.Bijective f ∧ f 0 = zero
    ∧ ∀ (n:nat) (n':nat'), f n = n' ↔ f (n+1:ℕ) = succ n'
```

## Depends on

- [Section 3.1: Fundamentals (of set theory)](section-3-1.md)
- [Section 3.2: Russell's paradox](section-3-2.md)
- [Section 3.4: Images and inverse images](section-3-4.md)

## Sources

- [Analysis/Section_3_5.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_5.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_3_5/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_3_5.html)
