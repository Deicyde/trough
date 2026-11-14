---
catalog: module
lean: List.IsChainFromTo, List.IsChainFromTo.length_pos, List.IsChainFromTo.getElem_zero, List.IsChainFromTo.getElem_length_sub_one, List.IsChainFromTo.reflTransGen, List.IsChain.isChainFromTo_of_ne_nil, List.isChainFromTo_singleton, List.IsChainFromTo.cons, List.isChainFromTo_pair_iff, List.IsChainFromTo.of_cons_cons, List.IsChainFromTo.append_tail, List.IsChainFromTo.snoc, List.IsChainFromTo.append_dropLast, List.IsChainFromTo.take, List.IsChainFromTo.drop, List.IsChainFromTo.head_induction_on, List.IsChainFromTo.reflTransGen_of_mem, List.IsChainFromTo.reflTransGen_of_mem', List.IsChainFromTo.exists_length_lt_of_not_nodup, List.IsChainFromTo.exists_nodup
statement: formalized
proof: formalized
---

# Chains with a designated start and end

`Cslib.Foundations.Data.List.IsChainFromTo`, in [Cslib/Foundations/Data/List/IsChainFromTo.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/List/IsChainFromTo.lean), by Christian Reitwiessner, Thomas Waring.

> This file defines `List.IsChainFromTo`, a variant of `List.IsChain` that also fixes the first and
> last element of the chain. Such a chain is an explicit witness for the fact that its end point is
> reachable from its start point, and its length bounds the number of steps that are needed.
>
> ## Main definitions
>
> * `List.IsChainFromTo r chain a b`: `chain` is a non-empty list whose adjacent elements are related
>   by `r`, whose first element is `a` and whose last element is `b`.
>
> ## Main results
>
> * `List.IsChainFromTo.reflTransGen`: the start and the end of a chain are related by
>   `Relation.ReflTransGen`.
> * `List.IsChainFromTo.head_induction_on`: induction on a chain, peeling off elements at the start.
> * `List.IsChainFromTo.exists_length_lt_of_not_nodup`: a chain with duplicates can always be
>   shortened.
> * `List.IsChainFromTo.exists_nodup`: iterating the above yields a chain without duplicates.

`List.IsChainFromTo` (structure, [line 43](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/List/IsChainFromTo.lean#L43))

> A "chain from to" is a list of elements where adjacent elements relate to each other
> (cf. `List.IsChain`) and start and end with specific elements.

```lean
structure IsChainFromTo {α : Type*} (r : α → α → Prop) (chain : List α) (a b : α) : Prop where
  isChain : chain.IsChain r
  ne_nil : chain ≠ []
  head_eq : chain.head ne_nil = a
  getLast_eq : chain.getLast ne_nil = b
```

`List.IsChainFromTo.length_pos` (lemma, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/List/IsChainFromTo.lean#L53))

> A chain has at least one element.

```lean
lemma IsChainFromTo.length_pos (hc : chain.IsChainFromTo r a b) : 0 < chain.length
```

`List.IsChainFromTo.getElem_zero` (lemma, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/List/IsChainFromTo.lean#L58))

> The first element of an `r`-chain from `a` to `b` is `a`.

```lean
lemma IsChainFromTo.getElem_zero (hc : chain.IsChainFromTo r a b) :
    chain[0]'hc.length_pos = a
```

`List.IsChainFromTo.getElem_length_sub_one` (lemma, [line 65](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/List/IsChainFromTo.lean#L65))

> The last element of an `r`-chain from `a` to `b` is `b`.

```lean
lemma IsChainFromTo.getElem_length_sub_one (hc : chain.IsChainFromTo r a b) :
    chain[chain.length - 1]'(by have := hc.length_pos; lia) = b
```

`List.IsChainFromTo.reflTransGen` (theorem, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/List/IsChainFromTo.lean#L71))

> The start and the end of an `r`-chain are reflexively-transitively related by `r`.

```lean
theorem IsChainFromTo.reflTransGen (hc : chain.IsChainFromTo r a b) :
    Relation.ReflTransGen r a b
```

`List.IsChain.isChainFromTo_of_ne_nil` (theorem, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/List/IsChainFromTo.lean#L77))

> Create a `List.IsChainFromTo` from a non-empty `List.IsChain`.

```lean
theorem IsChain.isChainFromTo_of_ne_nil
    {chain : List α} (hc : chain.IsChain r) (h_ne_nil : chain ≠ []) :
    List.IsChainFromTo r chain (chain.head h_ne_nil) (chain.getLast h_ne_nil)
```

`List.isChainFromTo_singleton` (lemma, [line 84](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/List/IsChainFromTo.lean#L84))

> A one-element list is an `r`-chain from that element to itself.

```lean
lemma isChainFromTo_singleton : List.IsChainFromTo r [a] a a
```

`List.IsChainFromTo.cons` (lemma, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/List/IsChainFromTo.lean#L88))

> Prepend an `r`-related element to the start of the chain.

```lean
lemma IsChainFromTo.cons (h : r a b) (hc : chain.IsChainFromTo r b c) :
    (a :: chain).IsChainFromTo r a c
```

`List.isChainFromTo_pair_iff` (lemma, [line 96](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/List/IsChainFromTo.lean#L96))

```lean
lemma isChainFromTo_pair_iff {a a' b b' : α} :
    List.IsChainFromTo r [a, b] a' b' ↔ r a b ∧ a = a' ∧ b = b'
```

`List.IsChainFromTo.of_cons_cons` (lemma, [line 105](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/List/IsChainFromTo.lean#L105))

> Removing the head yields a valid chain.

```lean
lemma IsChainFromTo.of_cons_cons {x y : α} (hc : (x :: y :: chain).IsChainFromTo r a b) :
    (y :: chain).IsChainFromTo r y b
```

`List.IsChainFromTo.append_tail` (lemma, [line 111](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/List/IsChainFromTo.lean#L111))

> Appending a chain and the tail of a second one whose start point equals the end point of the
> first yields a valid chain.

```lean
lemma IsChainFromTo.append_tail (hc : chain.IsChainFromTo r a b) {chain' : List α}
    (hc' : chain'.IsChainFromTo r b c) : (chain ++ chain'.tail).IsChainFromTo r a c
```

`List.IsChainFromTo.snoc` (lemma, [line 124](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/List/IsChainFromTo.lean#L124))

> Add an `r`-related element to the end of the chain.

```lean
lemma IsChainFromTo.snoc (hc : chain.IsChainFromTo r a b) (h : r b c) :
    (chain ++ [c]).IsChainFromTo r a c
```

`List.IsChainFromTo.append_dropLast` (lemma, [line 130](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/List/IsChainFromTo.lean#L130))

> Appending a chain, dropping its last element and another chain whose start point equals
> the end point of the first chain yields a valid chain.

```lean
lemma IsChainFromTo.append_dropLast (hc : chain.IsChainFromTo r a b) {chain' : List α}
    (hc' : chain'.IsChainFromTo r b c) : (chain.dropLast ++ chain').IsChainFromTo r a c
```

`List.IsChainFromTo.take` (lemma, [line 138](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/List/IsChainFromTo.lean#L138))

> Taking the first `i + 1` elements of a chain yields a chain from the same start point to
> `chain[i]`.

```lean
lemma IsChainFromTo.take (hc : chain.IsChainFromTo r a b) {i : ℕ} (hi : i < chain.length) :
    (chain.take (i + 1)).IsChainFromTo r a chain[i]
```

`List.IsChainFromTo.drop` (lemma, [line 145](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/List/IsChainFromTo.lean#L145))

> Dropping the first `i` elements of a chain yields a chain from `chain[i]` to the same end
> point.

```lean
lemma IsChainFromTo.drop (hc : chain.IsChainFromTo r a b) {i : ℕ} (hi : i < chain.length) :
    (chain.drop i).IsChainFromTo r chain[i] b
```

`List.IsChainFromTo.head_induction_on` (lemma, [line 151](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/List/IsChainFromTo.lean#L151))

```lean
lemma IsChainFromTo.head_induction_on
    {motive : ∀ {chain : List α} {a b : α}, chain.IsChainFromTo r a b → Prop}
    (h_refl : ∀ {a : α}, motive (isChainFromTo_singleton (r := r) (a := a)))
    (h_head : ∀ {a b c : α} {chain : List α} (hab : r a b) (hc : chain.IsChainFromTo r b c),
      motive hc → motive (hc.cons hab))
    {chain : List α} {a b : α} (hc : chain.IsChainFromTo r a b) : motive hc
```

`List.IsChainFromTo.reflTransGen_of_mem` (lemma, [line 166](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/List/IsChainFromTo.lean#L166))

> Any element of an `r`-chain from `a` to `b` is reflexively-transitively related from `a`.

```lean
lemma IsChainFromTo.reflTransGen_of_mem (hc : chain.IsChainFromTo r a b) {x : α} (mem : x ∈ chain) :
    Relation.ReflTransGen r a x
```

`List.IsChainFromTo.reflTransGen_of_mem'` (lemma, [line 172](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/List/IsChainFromTo.lean#L172))

> Any element of an `r`-chain from `a` to `b` is reflexively-transitively related to `b`.

```lean
lemma IsChainFromTo.reflTransGen_of_mem' (hc : chain.IsChainFromTo r a b) {x : α}
    (mem : x ∈ chain) :
    Relation.ReflTransGen r x b
```

`List.IsChainFromTo.exists_length_lt_of_not_nodup` (lemma, [line 180](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/List/IsChainFromTo.lean#L180))

> If there is an `r`-chain from `a` to `b` with duplicates, then there is a shorter `r`-chain
> from `a` to `b` (the one that skips the part between the duplicates).

```lean
lemma IsChainFromTo.exists_length_lt_of_not_nodup
    (hc : chain.IsChainFromTo r a b)
    (h_dup : ¬ chain.Nodup) :
    ∃ chain' : List α, chain'.IsChainFromTo r a b ∧ chain'.length < chain.length
```

`List.IsChainFromTo.exists_nodup` (lemma, [line 197](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/List/IsChainFromTo.lean#L197))

> For any `r`-chain from `a` to `b` there is one without duplicates.

```lean
lemma IsChainFromTo.exists_nodup (hc : chain.IsChainFromTo r a b) :
    ∃ chain' : List α, chain'.IsChainFromTo r a b ∧ chain'.Nodup
```

## Depends on

Its statements use no other CSLib module's declarations.

## Sources

- [Cslib/Foundations/Data/List/IsChainFromTo.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Data/List/IsChainFromTo.lean)
