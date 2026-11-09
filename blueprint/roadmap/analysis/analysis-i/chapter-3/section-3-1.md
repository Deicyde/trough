---
declaration: instance
origin: cited
lean: Chapter3.SetTheory.objects_mem_sets, Chapter3.SetTheory.sets_are_objects, Chapter3.SetTheory.Set.coe_eq, Chapter3.SetTheory.Set.coe_eq_iff, Chapter3.SetTheory.Set.ext, Chapter3.SetTheory.Set.not_mem_empty, Chapter3.SetTheory.Set.nonempty_def, Chapter3.SetTheory.Set.mem_singleton, Chapter3.SetTheory.Set.mem_union, Chapter3.SetTheory.Set.pair_eq, Chapter3.SetTheory.Set.mem_pair, Chapter3.SetTheory.Set.singleton_uniq, Chapter3.SetTheory.Set.pair_uniq, Chapter3.SetTheory.Set.pair_comm, Chapter3.SetTheory.Set.pair_self, Chapter3.SetTheory.Set.pair_eq_pair, Chapter3.SetTheory.Set.emptyset_neq_singleton, Chapter3.SetTheory.Set.emptyset_neq_pair, Chapter3.SetTheory.Set.singleton_empty_neq_pair, Chapter3.SetTheory.Set.union_congr_left, Chapter3.SetTheory.Set.union_congr_right, Chapter3.SetTheory.Set.singleton_union_singleton, Chapter3.SetTheory.Set.union_comm, Chapter3.SetTheory.Set.union_assoc, Chapter3.SetTheory.Set.union_self, Chapter3.SetTheory.Set.inter_self, Chapter3.SetTheory.Set.union_empty, Chapter3.SetTheory.Set.empty_union, Chapter3.SetTheory.Set.pair_union_pair, Chapter3.SetTheory.Set.instSubset, Chapter3.SetTheory.Set.instSSubset, Chapter3.SetTheory.Set.subset_congr_left, Chapter3.SetTheory.Set.subset_self, Chapter3.SetTheory.Set.empty_subset, Chapter3.SetTheory.Set.subset_trans, Chapter3.SetTheory.Set.subset_antisymm, Chapter3.SetTheory.Set.ssubset_trans, Chapter3.SetTheory.Set.specification_axiom, Chapter3.SetTheory.Set.specification_axiom', Chapter3.SetTheory.Set.specification_axiom'', Chapter3.SetTheory.Set.mem_inter, Chapter3.SetTheory.Set.mem_sdiff, Chapter3.SetTheory.Set.inter_comm, Chapter3.SetTheory.Set.subset_union, Chapter3.SetTheory.Set.union_subset, Chapter3.SetTheory.Set.inter_assoc, Chapter3.SetTheory.Set.inter_union_distrib_left, Chapter3.SetTheory.Set.union_inter_distrib_left, Chapter3.SetTheory.Set.union_compl, Chapter3.SetTheory.Set.inter_compl, Chapter3.SetTheory.Set.compl_union, Chapter3.SetTheory.Set.compl_inter, Chapter3.SetTheory.Set.replacement_axiom, Chapter3.SetTheory.Set.nat_equiv, Chapter3.SetTheory.Set.subset_tfae, Chapter3.SetTheory.Set.inter_subset_left, Chapter3.SetTheory.Set.inter_subset_right, Chapter3.SetTheory.Set.subset_inter_iff, Chapter3.SetTheory.Set.subset_union_left, Chapter3.SetTheory.Set.subset_union_right, Chapter3.SetTheory.Set.union_subset_iff, Chapter3.SetTheory.Set.inter_union_cancel, Chapter3.SetTheory.Set.union_inter_cancel, Chapter3.SetTheory.Set.partition_left, Chapter3.SetTheory.Set.partition_right, Chapter3.SetTheory.Set.pairwise_disjoint, Chapter3.SetTheory.Set.union_eq_partition, Chapter3.SetTheory.Set.specification_from_replacement, Chapter3.SetTheory.Set.subset_union_subset, Chapter3.SetTheory.Set.subset_inter_subset, Chapter3.SetTheory.Set.subset_diff_subset_counter, Chapter3.SetTheory.Set.singleton_iff
statement: formalized
---

# Section 3.1: Fundamentals (of set theory)

> In this section we set up a version of Zermelo-Frankel set theory (with atoms) that tries to be
> as faithful as possible to the original text of Analysis I, Section 3.1. All numbering refers to
> the original text.
>
> I have attempted to make the translation as faithful a paraphrasing as possible of the original
> text. When there is a choice between a more idiomatic Lean solution and a more faithful
> translation, I have generally chosen the latter. In particular, there will be places where the
> Lean code could be "golfed" to be more elegant and idiomatic, but I have consciously avoided
> doing so.
>
> Main constructions and results of this section:
>
> - A type `Chapter3.SetTheory.Set` of sets
> - A type `Chapter3.SetTheory.Object` of objects
> - An axiom that every set is (or can be coerced into) an object
> - The empty set `∅`, singletons `{y}`, and pairs `{y,z}` (and more general finite tuples), with
>   their attendant axioms
> - Pairwise union `X ∪ Y`, and their attendant axioms
> - Coercion of a set `A` to its associated type `A.toSubtype`, which is a subtype of `Object`, and
>   basic API.  (This is a technical construction needed to make the Zermelo-Frankel set theory
>   compatible with the dependent type theory of Lean.)
> - The specification `A.specify P` of a set `A` and a predicate `P: A.toSubtype → Prop` to the
>   subset of elements of `A` obeying `P`, and the axiom of specification.
>   TODO: somehow implement set builder elaboration for this.
> - The replacement `A.replace hP` of a set `A` via a predicate
>   `P: A.toSubtype → Object → Prop` obeying a uniqueness condition
>   `∀ x y y', P x y ∧ P x y' → y = y'`, and the axiom of replacement.
> - A bijective correspondence between the Mathlib natural numbers `ℕ` and a set
>   `Chapter3.Nat : Chapter3.Set` (the axiom of infinity).
> - Axioms of regularity, power set, and union (used in later sections of this chapter, but not
>   required here)
> - Connections with Mathlib's notion of a `Set`
>
> The other axioms of Zermelo-Frankel set theory are discussed in later sections.
>
> Some technical notes:
> - Mathlib of course has its own notion of a `Set` (or more precisely, a type `Set X` associated to
>   each type `X`), which is not compatible with the notion `Chapter3.Set` defined here,
>   though we will try to make the notations match as much as possible.  This causes some notational
>   conflict: for instance, one may need to explicitly specify `(∅:Chapter3.Set)` instead of just `∅`
>   to indicate that one is using the `Chapter3.Set` version of the empty set, rather than the
>   Mathlib version of the empty set, and similarly for other notation defined here.
> - In Analysis I, we chose to work with an "impure" set theory, in which there could be more
>   `Object`s than just `Set`s.  In the type theory of Lean, this requires treating `Chapter3.Set`
>   and `Chapter3.Object` as distinct types. Occasionally this means we have to use a coercion
>   `(X: Chapter3.Object)` of a `Chapter3.Set` `X` to make into a `Chapter3.Object`: this is
>   mostly needed when manipulating sets of sets.
> - Strictly speaking, a set `X:Set` is not a type; however, we will coerce sets to types, and
>   specifically to a subtype of `Object`.  A similar coercion is in place for Mathlib's
>   formalization of sets.
> - After this chapter is concluded, the notion of a `Chapter3.SetTheory.Set` will be deprecated in
>   favor of the standard Mathlib notion of a `Set` (or more precisely of the type `Set X` of a set
>   in a given type `X`).  However, due to various technical incompatibilities between set theory
>   and type theory, we will not attempt to create a full equivalence between these two
>   notions of sets. (As such, this makes this entire chapter optional from the point of view of
>   the rest of the book, though we retain it for pedagogical purposes.)
>
>
> ## Tips from past users
>
> Users of the companion who have completed the exercises in this section are welcome to send their tips for future users in this section as PRs.
>
> - (Add tip here)

*Quoted from [Analysis/Section_3_1.lean](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean) in [teorth/analysis](https://github.com/teorth/analysis) at commit [a19a5bfa](https://github.com/teorth/analysis/tree/a19a5bfadc616467562995b75f46035232841943), Apache-2.0, as are the docstrings and Lean statements below.*

The file has 52 labelled items, carried by 79 declarations: 23 proved here, 51 stated without proof (26 of them exercises) and 5 definitions. It also has 65 declarations and 39 examples with no label, counted here but not shown.

## Definition 3.1.1

`Chapter3.SetTheory.objects_mem_sets` (instance, [line 119](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L119)). A definition.

> Definition 3.1.1 (objects can be elements of sets)

```lean
instance SetTheory.objects_mem_sets : Membership Object Set
```

## Axiom 3.1

`Chapter3.SetTheory.sets_are_objects` (instance, [line 126](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L126)). A definition.

> Axiom 3.1 (Sets are objects, coercion).

```lean
instance SetTheory.sets_are_objects : Coe Set Object
```

`Chapter3.SetTheory.Set.coe_eq` (theorem, [line 133](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L133)). Proved here.

> Axiom 3.1 (Sets are objects, injectivity).

```lean
theorem SetTheory.Set.coe_eq {X Y:Set} (h: (X: Object) = (Y: Object)) : X = Y
```

`Chapter3.SetTheory.Set.coe_eq_iff` (theorem, [line 138](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L138)). Proved here.

> Axiom 3.1 (Sets are objects, iff lemma).

```lean
theorem SetTheory.Set.coe_eq_iff (X Y:Set) : (X: Object) = (Y: Object) ↔  X = Y
```

## Axiom 3.2

`Chapter3.SetTheory.Set.ext` (theorem, [line 143](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L143)). Proved here.

> Axiom 3.2 (Equality of sets).  The `@[ext]` tag allows the `ext` tactic to work for sets.

```lean
theorem SetTheory.Set.ext {X Y:Set} (h: ∀ x, x ∈ X ↔ x ∈ Y) : X = Y
```

## Axiom 3.3

`Chapter3.SetTheory.Set.not_mem_empty` (theorem, [line 163](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L163)). Proved here.

> Axiom 3.3 (empty set).
> Note: in some applications one may have to explicitly cast `(∅ : Set)` to `Set` due to
> Mathlib's existing set theory notation.

```lean
theorem SetTheory.Set.not_mem_empty : ∀ x, x ∉ (∅:Set)
```

## Lemma 3.1.5

`Chapter3.SetTheory.Set.nonempty_def` (lemma, [line 174](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L174)). Proved here.

> Lemma 3.1.5 (Single choice)

```lean
lemma SetTheory.Set.nonempty_def {X:Set} (h: X ≠ ∅) : ∃ x, x ∈ X
```

## Axiom 3.3(a)

`Chapter3.SetTheory.Set.mem_singleton` (theorem, [line 198](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L198)). Proved here.

> Axiom 3.3(a) (singleton).
> Note: in some applications one may have to explicitly cast `{a}` to `Set` due to Mathlib's
> existing set theory notation.

```lean
theorem SetTheory.Set.mem_singleton (x a:Object) : x ∈ ({a}:Set) ↔ x = a
```

## Axiom 3.4

`Chapter3.SetTheory.Set.mem_union` (theorem, [line 209](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L209)). Proved here.

> Axiom 3.4 (Pairwise union).

```lean
theorem SetTheory.Set.mem_union (x:Object) (X Y:Set) : x ∈ (X ∪ Y) ↔ (x ∈ X ∨ x ∈ Y)
```

## Axiom 3.3(b)

`Chapter3.SetTheory.Set.pair_eq` (theorem, [line 221](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L221)). Proved here.

> Axiom 3.3(b) (pair).  Note: in some applications one may have to cast `{a,b}`
> to `Set`.

```lean
theorem SetTheory.Set.pair_eq (a b:Object) : ({a,b}:Set) = {a} ∪ {b}
```

`Chapter3.SetTheory.Set.mem_pair` (theorem, [line 226](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L226)). Proved here.

> Axiom 3.3(b) (pair).  Note: in some applications one may have to cast `{a,b}`
> to `Set`.

```lean
theorem SetTheory.Set.mem_pair (x a b:Object) : x ∈ ({a,b}:Set) ↔ (x = a ∨ x = b)
```

## Remark 3.1.9

`Chapter3.SetTheory.Set.singleton_uniq` (theorem, [line 234](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L234)). Stated without proof.

> Remark 3.1.9

```lean
theorem SetTheory.Set.singleton_uniq (a:Object) : ∃! (X:Set), ∀ x, x ∈ X ↔ x = a
```

`Chapter3.SetTheory.Set.pair_uniq` (theorem, [line 237](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L237)). Stated without proof.

> Remark 3.1.9

```lean
theorem SetTheory.Set.pair_uniq (a b:Object) : ∃! (X:Set), ∀ x, x ∈ X ↔ x = a ∨ x = b
```

`Chapter3.SetTheory.Set.pair_comm` (theorem, [line 240](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L240)). Stated without proof.

> Remark 3.1.9

```lean
theorem SetTheory.Set.pair_comm (a b:Object) : ({a,b}:Set) = {b,a}
```

`Chapter3.SetTheory.Set.pair_self` (theorem, [line 244](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L244)). Stated without proof.

> Remark 3.1.9

```lean
theorem SetTheory.Set.pair_self (a:Object) : ({a,a}:Set) = {a}
```

## Exercise 3.1.1

`Chapter3.SetTheory.Set.pair_eq_pair` (theorem, [line 248](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L248)). An exercise, stated without proof.

> Exercise 3.1.1

```lean
theorem SetTheory.Set.pair_eq_pair {a b c d:Object} (h: ({a,b}:Set) = {c,d}) :
    a = c ∧ b = d ∨ a = d ∧ b = c
```

## Exercise 3.1.2

`Chapter3.SetTheory.Set.emptyset_neq_singleton` (theorem, [line 257](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L257)). An exercise, stated without proof.

> Exercise 3.1.2 (empty set is not a singleton)

```lean
theorem SetTheory.Set.emptyset_neq_singleton : empty ≠ singleton_empty
```

`Chapter3.SetTheory.Set.emptyset_neq_pair` (theorem, [line 261](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L261)). An exercise, stated without proof.

> Exercise 3.1.2 (empty set is not a pair)

```lean
theorem SetTheory.Set.emptyset_neq_pair : empty ≠ pair_empty
```

`Chapter3.SetTheory.Set.singleton_empty_neq_pair` (theorem, [line 264](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L264)). An exercise, stated without proof.

> Exercise 3.1.2 (singleton is not a pair)

```lean
theorem SetTheory.Set.singleton_empty_neq_pair : singleton_empty ≠ pair_empty
```

## Remark 3.1.11

`Chapter3.SetTheory.Set.union_congr_left` (theorem, [line 271](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L271)). Stated without proof.

> Remark 3.1.11.
> (These results can be proven either by a direct rewrite, or by using extensionality.)

```lean
theorem SetTheory.Set.union_congr_left (A A' B:Set) (h: A = A') : A ∪ B = A' ∪ B
```

`Chapter3.SetTheory.Set.union_congr_right` (theorem, [line 277](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L277)). Stated without proof.

> Remark 3.1.11.
> (These results can be proven either by a direct rewrite, or by using extensionality.)

```lean
theorem SetTheory.Set.union_congr_right (A B B':Set) (h: B = B') : A ∪ B = A ∪ B'
```

## Lemma 3.1.12 / Exercise 3.1.3

`Chapter3.SetTheory.Set.singleton_union_singleton` (theorem, [line 280](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L280)). An exercise, stated without proof.

> Lemma 3.1.12 (Basic properties of unions, singletons) / Exercise 3.1.3

```lean
theorem SetTheory.Set.singleton_union_singleton (a b:Object) :
    ({a}:Set) ∪ ({b}:Set) = {a,b}
```

`Chapter3.SetTheory.Set.union_comm` (theorem, [line 285](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L285)). An exercise, stated without proof.

> Lemma 3.1.12 (Basic properties of unions, commutativity) / Exercise 3.1.3

```lean
theorem SetTheory.Set.union_comm (A B:Set) : A ∪ B = B ∪ A
```

`Chapter3.SetTheory.Set.union_assoc` (theorem, [line 288](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L288)). An exercise, stated without proof.

> Lemma 3.1.12 (Basic properties of unions, associativity) / Exercise 3.1.3

```lean
theorem SetTheory.Set.union_assoc (A B C:Set) : (A ∪ B) ∪ C = A ∪ (B ∪ C)
```

## Proposition 3.1.27(c)

`Chapter3.SetTheory.Set.union_self` (theorem, [line 305](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L305)). Stated without proof.

> Proposition 3.1.27(c) (Union idempotent).

```lean
theorem SetTheory.Set.union_self (A:Set) : A ∪ A = A
```

`Chapter3.SetTheory.Set.inter_self` (theorem, [line 494](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L494)). Stated without proof.

> Proposition 3.1.27(c) (Intersection idempotent).

```lean
theorem SetTheory.Set.inter_self (A:Set) : A ∩ A = A
```

## Proposition 3.1.27(a)

`Chapter3.SetTheory.Set.union_empty` (theorem, [line 310](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L310)). Stated without proof.

> Proposition 3.1.27(a) (Union with empty).

```lean
theorem SetTheory.Set.union_empty (A:Set) : A ∪ ∅ = A
```

`Chapter3.SetTheory.Set.empty_union` (theorem, [line 315](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L315)). Stated without proof.

> Proposition 3.1.27(a) (Empty with union).

```lean
theorem SetTheory.Set.empty_union (A:Set) : ∅ ∪ A = A
```

## Example 3.1.10

`Chapter3.SetTheory.Set.pair_union_pair` (theorem, [line 322](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L322)). Proved here.

> Example 3.1.10

```lean
theorem SetTheory.Set.pair_union_pair (a b c:Object) :
    ({a,b}:Set) ∪ {b,c} = {a,b,c}
```

## Definition 3.1.14

`Chapter3.SetTheory.Set.instSubset` (instance, [line 327](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L327)). A definition.

> Definition 3.1.14 (Subset).

```lean
instance SetTheory.Set.instSubset : HasSubset Set
```

`Chapter3.SetTheory.Set.instSSubset` (instance, [line 337](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L337)). A definition.

> Definition 3.1.14 (Strict subset).
> Note that the strict subset operation in Mathlib is denoted `⊂` rather than `⊊`.

```lean
instance SetTheory.Set.instSSubset : HasSSubset Set
```

## Remark 3.1.15

`Chapter3.SetTheory.Set.subset_congr_left` (theorem, [line 348](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L348)). Stated without proof.

> Remark 3.1.15

```lean
theorem SetTheory.Set.subset_congr_left {A A' B:Set} (hAA':A = A') (hAB: A ⊆ B) : A' ⊆ B
```

## Examples 3.1.16

`Chapter3.SetTheory.Set.subset_self` (theorem, [line 352](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L352)). Stated without proof.

> Examples 3.1.16 (reflexivity)

```lean
theorem SetTheory.Set.subset_self (A:Set) : A ⊆ A
```

`Chapter3.SetTheory.Set.empty_subset` (theorem, [line 356](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L356)). Stated without proof.

> Examples 3.1.16 (the empty set is a subset)

```lean
theorem SetTheory.Set.empty_subset (A:Set) : ∅ ⊆ A
```

## Proposition 3.1.17

`Chapter3.SetTheory.Set.subset_trans` (theorem, [line 359](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L359)). Proved here.

> Proposition 3.1.17 (Partial ordering by set inclusion, transitivity)

```lean
theorem SetTheory.Set.subset_trans {A B C:Set} (hAB:A ⊆ B) (hBC:B ⊆ C) : A ⊆ C
```

`Chapter3.SetTheory.Set.subset_antisymm` (theorem, [line 369](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L369)). Stated without proof.

> Proposition 3.1.17 (Partial ordering by set inclusion, antisymmetry)

```lean
theorem SetTheory.Set.subset_antisymm (A B:Set) (hAB:A ⊆ B) (hBA:B ⊆ A) : A = B
```

`Chapter3.SetTheory.Set.ssubset_trans` (theorem, [line 373](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L373)). Stated without proof.

> Proposition 3.1.17 (Partial ordering by set inclusion, strict transitivity)

```lean
theorem SetTheory.Set.ssubset_trans (A B C:Set) (hAB:A ⊂ B) (hBC:B ⊂ C) : A ⊂ C
```

## Axiom 3.6

`Chapter3.SetTheory.Set.specification_axiom` (theorem, [line 429](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L429)). Proved here.

> Axiom 3.6 (axiom of specification, membership)

```lean
theorem SetTheory.Set.specification_axiom {A:Set} {P: A → Prop} {x:Object} (h: x ∈ A.specify P) :
    x ∈ A
```

`Chapter3.SetTheory.Set.specification_axiom'` (theorem, [line 434](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L434)). Proved here.

> Axiom 3.6 (axiom of specification, the property holds)

```lean
theorem SetTheory.Set.specification_axiom' {A:Set} (P: A → Prop) (x:A) :
    x.val ∈ A.specify P ↔ P x
```

`Chapter3.SetTheory.Set.specification_axiom''` (theorem, [line 440](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L440)). Proved here.

> Axiom 3.6 (axiom of specification, the specified set is a subset)

```lean
theorem SetTheory.Set.specification_axiom'' {A:Set} (P: A → Prop) (x:Object) :
    x ∈ A.specify P ↔ ∃ h:x ∈ A, P ⟨ x, h ⟩
```

## Definition 3.1.22

`Chapter3.SetTheory.Set.mem_inter` (theorem, [line 463](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L463)). Proved here.

> Definition 3.1.22 (Intersections)

```lean
theorem SetTheory.Set.mem_inter (x:Object) (X Y:Set) : x ∈ (X ∩ Y) ↔ (x ∈ X ∧ x ∈ Y)
```

## Definition 3.1.26

`Chapter3.SetTheory.Set.mem_sdiff` (theorem, [line 477](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L477)). Proved here.

> Definition 3.1.26 (Difference sets)

```lean
theorem SetTheory.Set.mem_sdiff (x:Object) (X Y:Set) : x ∈ (X \ Y) ↔ (x ∈ X ∧ x ∉ Y)
```

## Proposition 3.1.27(d) / Exercise 3.1.6

`Chapter3.SetTheory.Set.inter_comm` (theorem, [line 484](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L484)). An exercise, stated without proof.

> Proposition 3.1.27(d) / Exercise 3.1.6

```lean
theorem SetTheory.Set.inter_comm (A B:Set) : A ∩ B = B ∩ A
```

## Proposition 3.1.27(b)

`Chapter3.SetTheory.Set.subset_union` (theorem, [line 487](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L487)). Stated without proof.

> Proposition 3.1.27(b) (Subset absorption).

```lean
theorem SetTheory.Set.subset_union {A X: Set} (hAX: A ⊆ X) : A ∪ X = X
```

`Chapter3.SetTheory.Set.union_subset` (theorem, [line 490](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L490)). Stated without proof.

> Proposition 3.1.27(b) (Union absorption).

```lean
theorem SetTheory.Set.union_subset {A X: Set} (hAX: A ⊆ X) : X ∪ A = X
```

## Proposition 3.1.27(e)

`Chapter3.SetTheory.Set.inter_assoc` (theorem, [line 498](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L498)). Stated without proof.

> Proposition 3.1.27(e)

```lean
theorem SetTheory.Set.inter_assoc (A B C:Set) : (A ∩ B) ∩ C = A ∩ (B ∩ C)
```

## Proposition 3.1.27(f)

`Chapter3.SetTheory.Set.inter_union_distrib_left` (theorem, [line 501](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L501)). Stated without proof.

> Proposition 3.1.27(f) (Intersection distributes over union).

```lean
theorem  SetTheory.Set.inter_union_distrib_left (A B C:Set) :
    A ∩ (B ∪ C) = (A ∩ B) ∪ (A ∩ C)
```

`Chapter3.SetTheory.Set.union_inter_distrib_left` (theorem, [line 506](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L506)). Stated without proof.

> Proposition 3.1.27(f) (Union distributes over intersection).

```lean
theorem  SetTheory.Set.union_inter_distrib_left (A B C:Set) :
    A ∪ (B ∩ C) = (A ∪ B) ∩ (A ∪ C)
```

`Chapter3.SetTheory.Set.union_compl` (theorem, [line 511](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L511)). Stated without proof.

> Proposition 3.1.27(f) (Partition of a superset).

```lean
theorem SetTheory.Set.union_compl {A X:Set} (hAX: A ⊆ X) : A ∪ (X \ A) = X
```

`Chapter3.SetTheory.Set.inter_compl` (theorem, [line 514](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L514)). Stated without proof.

> Proposition 3.1.27(f) (Disjoint intersection with complement).

```lean
theorem SetTheory.Set.inter_compl {A X:Set} : A ∩ (X \ A) = ∅
```

## Proposition 3.1.27(g)

`Chapter3.SetTheory.Set.compl_union` (theorem, [line 517](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L517)). Stated without proof.

> Proposition 3.1.27(g) (Complement of a union).

```lean
theorem SetTheory.Set.compl_union {A B X:Set} : X \ (A ∪ B) = (X \ A) ∩ (X \ B)
```

`Chapter3.SetTheory.Set.compl_inter` (theorem, [line 520](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L520)). Stated without proof.

> Proposition 3.1.27(g) (Complement of an intersection).

```lean
theorem SetTheory.Set.compl_inter {A B X:Set} : X \ (A ∩ B) = (X \ A) ∪ (X \ B)
```

## Axiom 3.7

`Chapter3.SetTheory.Set.replacement_axiom` (theorem, [line 560](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L560)). Proved here.

> Axiom 3.7 (Axiom of replacement)

```lean
theorem SetTheory.Set.replacement_axiom {A:Set} {P: A → Object → Prop}
  (hP: ∀ x y y', P x y ∧ P x y' → y = y') (y:Object) :
    y ∈ A.replace hP ↔ ∃ x, P x y
```

## Axiom 3.8

`Chapter3.SetTheory.Set.nat_equiv` (def, [line 577](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L577)). A definition.

> Axiom 3.8 (Axiom of infinity)

```lean
def SetTheory.Set.nat_equiv : ℕ ≃ Nat
```

## Example 3.1.16

An `example` ([line 684](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L684)). Proved here.

> Example 3.1.16 (simplified).

```lean
example : ({3, 5}:Set) ⊆ {1, 3, 5}
```

## Example 3.1.17

An `example` ([line 689](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L689)). Proved here.

> Example 3.1.17 (simplified).

```lean
example : ({3, 5}:Set).specify (fun x ↦ x.val ≠ 3) = ({5}:Set)
```

## Example 3.1.24

An `example` ([line 697](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L697)). Proved here.

> Example 3.1.24

```lean
example : ({1, 2, 4}:Set) ∩ {2,3,4} = {2, 4}
```

## Example 3.1.25

An `example` ([line 705](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L705)). Proved here.

> Example 3.1.25

```lean
example : ({1, 2}:Set) ∩ {3,4} = ∅
```

## Example 3.1.28

An `example` ([line 720](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L720)). Proved here.

> Example 3.1.28 (Difference sets).

```lean
example : ({1, 2, 3, 4}:Set) \ {2,4,6} = {1, 3}
```

## Example 3.1.30

An `example` ([line 724](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L724)). Stated without proof.

> Example 3.1.30

```lean
example : ({3,5,9}:Set).replace (P := fun x y ↦ ∃ (n:ℕ), x.val = n ∧ y = (n+1:ℕ)) (by aesop)
  = {4,6,10}
```

## Example 3.1.31

An `example` ([line 728](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L728)). Proved here.

> Example 3.1.31

```lean
example : ({3,5,9}:Set).replace (P := fun _ y ↦ y=1) (by aesop) = {1}
```

## Exercise 3.1.5

`Chapter3.SetTheory.Set.subset_tfae` (theorem, [line 732](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L732)). An exercise, stated without proof.

> Exercise 3.1.5.  One can use the `tfae_have` and `tfae_finish` tactics here.

```lean
theorem SetTheory.Set.subset_tfae (A B:Set) : [A ⊆ B, A ∪ B = B, A ∩ B = A].TFAE
```

## Exercise 3.1.7 (a)

`Chapter3.SetTheory.Set.inter_subset_left` (theorem, [line 735](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L735)). An exercise, stated without proof.

> Exercise 3.1.7 (a)

```lean
theorem SetTheory.Set.inter_subset_left (A B:Set) : A ∩ B ⊆ A
```

## Exercise 3.1.7 (b)

`Chapter3.SetTheory.Set.inter_subset_right` (theorem, [line 739](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L739)). An exercise, stated without proof.

> Exercise 3.1.7 (b)

```lean
theorem SetTheory.Set.inter_subset_right (A B:Set) : A ∩ B ⊆ B
```

## Exercise 3.1.7 (c)

`Chapter3.SetTheory.Set.subset_inter_iff` (theorem, [line 744](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L744)). An exercise, stated without proof.

> Exercise 3.1.7 (c)

```lean
theorem SetTheory.Set.subset_inter_iff (A B C:Set) : C ⊆ A ∩ B ↔ C ⊆ A ∧ C ⊆ B
```

## Exercise 3.1.7 (d)

`Chapter3.SetTheory.Set.subset_union_left` (theorem, [line 748](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L748)). An exercise, stated without proof.

> Exercise 3.1.7 (d)

```lean
theorem SetTheory.Set.subset_union_left (A B:Set) : A ⊆ A ∪ B
```

## Exercise 3.1.7 (e)

`Chapter3.SetTheory.Set.subset_union_right` (theorem, [line 752](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L752)). An exercise, stated without proof.

> Exercise 3.1.7 (e)

```lean
theorem SetTheory.Set.subset_union_right (A B:Set) : B ⊆ A ∪ B
```

## Exercise 3.1.7 (f)

`Chapter3.SetTheory.Set.union_subset_iff` (theorem, [line 757](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L757)). An exercise, stated without proof.

> Exercise 3.1.7 (f)

```lean
theorem SetTheory.Set.union_subset_iff (A B C:Set) : A ∪ B ⊆ C ↔ A ⊆ C ∧ B ⊆ C
```

## Exercise 3.1.8 (a)

`Chapter3.SetTheory.Set.inter_union_cancel` (theorem, [line 762](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L762)). An exercise, stated without proof.

> Exercise 3.1.8 (a)

```lean
theorem SetTheory.Set.inter_union_cancel (A B:Set) : A ∩ (A ∪ B) = A
```

## Exercise 3.1.8 (b)

`Chapter3.SetTheory.Set.union_inter_cancel` (theorem, [line 766](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L766)). An exercise, stated without proof.

> Exercise 3.1.8 (b)

```lean
theorem SetTheory.Set.union_inter_cancel (A B:Set) : A ∪ (A ∩ B) = A
```

## Exercise 3.1.9 (a)

`Chapter3.SetTheory.Set.partition_left` (theorem, [line 769](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L769)). An exercise, stated without proof.

> Exercise 3.1.9 (a)

```lean
theorem SetTheory.Set.partition_left {A B X:Set} (h_union: A ∪ B = X) (h_inter: A ∩ B = ∅) :
    A = X \ B
```

## Exercise 3.1.9 (b)

`Chapter3.SetTheory.Set.partition_right` (theorem, [line 773](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L773)). An exercise, stated without proof.

> Exercise 3.1.9 (b)

```lean
theorem SetTheory.Set.partition_right {A B X:Set} (h_union: A ∪ B = X) (h_inter: A ∩ B = ∅) :
    B = X \ A
```

## Exercise 3.1.10

`Chapter3.SetTheory.Set.pairwise_disjoint` (theorem, [line 781](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L781)). An exercise, stated without proof.

> Exercise 3.1.10.
> You may find `Function.onFun_apply` and the `fin_cases` tactic useful.

```lean
theorem SetTheory.Set.pairwise_disjoint (A B:Set) :
    Pairwise (Function.onFun Disjoint ![A \ B, A ∩ B, B \ A])
```

`Chapter3.SetTheory.Set.union_eq_partition` (theorem, [line 785](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L785)). An exercise, stated without proof.

> Exercise 3.1.10

```lean
theorem SetTheory.Set.union_eq_partition (A B:Set) : A ∪ B = (A \ B) ∪ (A ∩ B) ∪ (B \ A)
```

## Exercise 3.1.11

`Chapter3.SetTheory.Set.specification_from_replacement` (theorem, [line 793](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L793)). An exercise, stated without proof.

> Exercise 3.1.11.
> The challenge is to prove this without using `Set.specify`, `Set.specification_axiom`,
> `Set.specification_axiom'`, or anything built from them (like differences and intersections).

```lean
theorem SetTheory.Set.specification_from_replacement {A:Set} {P: A → Prop} :
    ∃ B, B ⊆ A ∧ ∀ x, x.val ∈ B ↔ P x
```

## Exercise 3.1.12

`Chapter3.SetTheory.Set.subset_union_subset` (theorem, [line 797](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L797)). An exercise, stated without proof.

> Exercise 3.1.12 (unions)

```lean
theorem SetTheory.Set.subset_union_subset {A B A' B':Set} (hA'A: A' ⊆ A) (hB'B: B' ⊆ B) :
    A' ∪ B' ⊆ A ∪ B
```

`Chapter3.SetTheory.Set.subset_inter_subset` (theorem, [line 801](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L801)). An exercise, stated without proof.

> Exercise 3.1.12 (intersections)

```lean
theorem SetTheory.Set.subset_inter_subset {A B A' B':Set} (hA'A: A' ⊆ A) (hB'B: B' ⊆ B) :
    A' ∩ B' ⊆ A ∩ B
```

`Chapter3.SetTheory.Set.subset_diff_subset_counter` (theorem, [line 805](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L805)). An exercise, stated without proof.

> Exercise 3.1.12 (differences: a counterexample)

```lean
theorem SetTheory.Set.subset_diff_subset_counter :
    ∃ (A B A' B':Set), (A' ⊆ A) ∧ (B' ⊆ B) ∧ ¬ (A' \ B') ⊆ (A \ B)
```

## Exercise 3.1.13

`Chapter3.SetTheory.Set.singleton_iff` (theorem, [line 814](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean#L814)). An exercise, stated without proof.

> Exercise 3.1.13

```lean
theorem SetTheory.Set.singleton_iff (A:Set) (hA: A ≠ ∅) : (¬∃ B ⊂ A, B ≠ ∅) ↔ ∃ x, A = {x}
```

## Depends on

Its Lean file imports no other section's file.

## Sources

- [Analysis/Section_3_1.lean at a19a5bfa](https://github.com/teorth/analysis/blob/a19a5bfadc616467562995b75f46035232841943/Analysis/Section_3_1.lean)
- [Verso page](https://teorth.github.io/analysis/Analysis/Section_3_1/)
- [Documentation](https://teorth.github.io/analysis/docs/Analysis/Section_3_1.html)
