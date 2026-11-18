---
catalog: module
lean: Relation.RelatesInSteps, Relation.RelatesInSteps.reflTransGen, Relation.ReflTransGen.relatesInSteps, Relation.RelatesInSteps.single, Relation.RelatesInSteps.head, Relation.RelatesInSteps.head_induction_on, Relation.RelatesInSteps.zero, Relation.RelatesInSteps.zero_iff, Relation.RelatesInSteps.trans, Relation.RelatesInSteps.succ, Relation.RelatesInSteps.succ_iff, Relation.RelatesInSteps.succ', Relation.RelatesInSteps.succ'_iff, Relation.RelatesInSteps.apply_le_apply_add, Relation.RelatesInSteps.map, Relation.RelatesInSteps.exists_isChainFromTo, List.IsChain.relatesInSteps_getElem, List.IsChainFromTo.relatesInSteps, Relation.relatesInSteps_iff_exists_isChainFromTo, Relation.RelatesWithinSteps, Relation.RelatesWithinSteps.of_relatesInSteps, Relation.RelatesWithinSteps.refl, Relation.RelatesWithinSteps.single, Relation.RelatesWithinSteps.zero, Relation.RelatesWithinSteps.zero_iff, Relation.RelatesWithinSteps.trans, Relation.RelatesWithinSteps.mono, Relation.RelatesWithinSteps.apply_le_apply_add, Relation.RelatesWithinSteps.map, Relation.ReflTransGen.relatesInSteps_lt_encard
statement: formalized
proof: formalized
---

# Relations Across Steps

`Cslib.Foundations.Relation.RelatesInSteps`, in [Cslib/Foundations/Relation/RelatesInSteps.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean), by Bolton Bailey.

> This file defines `Relation.RelatesInSteps` (and `Relation.RelatesWithinSteps`).
> These are inductively defined propositions that communicate whether a relation forms a
> chain of length `n` (or at most `n`) between two elements.
>
> The lemma `RelatesInSteps.exists_isChainFromTo` allows to obtain a chain
> (`List.IsChainFromTo`) of related elements that witness the reachability, and
> `List.IsChainFromTo.relatesInSteps` is the converse direction.
> `Relation.relatesInSteps_iff_exists_isChainFromTo` combines both.
>
> Another result is `Relation.ReflTransGen.relatesInSteps_lt_encard`, which states that any element
> reachable from `a` is reachable in fewer steps than there are elements reachable from `a`.

`Relation.RelatesInSteps` (inductive type, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L40))

> A relation `r` relates two elements of `α` in `n` steps
> if there is a chain of `n` pairs `(t_i, t_{i+1})` such that `r t_i t_{i+1}` for each `i`,
> starting from the first element and ending at the second.

```lean
inductive RelatesInSteps (r : α → α → Prop) : α → α → ℕ → Prop
  | refl (a : α) : RelatesInSteps r a a 0
  | tail (t t' t'' : α) (n : ℕ) (h₁ : RelatesInSteps r t t' n) (h₂ : r t' t'') :
      RelatesInSteps r t t'' (n + 1)
```

`Relation.RelatesInSteps.reflTransGen` (theorem, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L45))

```lean
theorem RelatesInSteps.reflTransGen (h : RelatesInSteps r a b n) : ReflTransGen r a b
```

`Relation.ReflTransGen.relatesInSteps` (theorem, [line 52](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L52))

> If `b` is reachable from `a` via `r`, then they relate to each other for some number
> of steps.

```lean
theorem ReflTransGen.relatesInSteps (h : ReflTransGen r a b) : ∃ n, RelatesInSteps r a b n
```

`Relation.RelatesInSteps.single` (lemma, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L59))

```lean
lemma RelatesInSteps.single {a b : α} (h : r a b) : RelatesInSteps r a b 1
```

`Relation.RelatesInSteps.head` (theorem, [line 62](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L62))

```lean
theorem RelatesInSteps.head (t t' t'' : α) (n : ℕ) (h₁ : r t t')
    (h₂ : RelatesInSteps r t' t'' n) : RelatesInSteps r t t'' (n+1)
```

`Relation.RelatesInSteps.head_induction_on` (theorem, [line 71](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L71))

```lean
theorem RelatesInSteps.head_induction_on {motive : ∀ (a : α) (n : ℕ), RelatesInSteps r a b n → Prop}
    {a : α} {n : ℕ} (h : RelatesInSteps r a b n) (hrefl : motive b 0 (.refl b))
    (hhead : ∀ {a c n} (h' : r a c) (h : RelatesInSteps r c b n),
      motive c n h → motive a (n + 1) (h.head a c b n h')) :
    motive a n h
```

`Relation.RelatesInSteps.zero` (lemma, [line 83](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L83))

```lean
lemma RelatesInSteps.zero {a b : α} (h : RelatesInSteps r a b 0) : a = b
```

`Relation.RelatesInSteps.zero_iff` (lemma, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L88))

```lean
lemma RelatesInSteps.zero_iff {a b : α} : RelatesInSteps r a b 0 ↔ a = b
```

`Relation.RelatesInSteps.trans` (lemma, [line 94](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L94))

```lean
lemma RelatesInSteps.trans {a b c : α} {n m : ℕ}
    (h₁ : RelatesInSteps r a b n) (h₂ : RelatesInSteps r b c m) :
    RelatesInSteps r a c (n + m)
```

`Relation.RelatesInSteps.succ` (lemma, [line 103](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L103))

```lean
lemma RelatesInSteps.succ {n : ℕ} (h : RelatesInSteps r a b (n + 1)) :
    ∃ t', RelatesInSteps r a t' n ∧ r t' b
```

`Relation.RelatesInSteps.succ_iff` (lemma, [line 108](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L108))

```lean
lemma RelatesInSteps.succ_iff {a b : α} {n : ℕ} :
    RelatesInSteps r a b (n + 1) ↔ ∃ t', RelatesInSteps r a t' n ∧ r t' b
```

`Relation.RelatesInSteps.succ'` (lemma, [line 115](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L115))

```lean
lemma RelatesInSteps.succ' {a b : α} {n : ℕ} (h : RelatesInSteps r a b (n + 1)) :
    ∃ t', r a t' ∧ RelatesInSteps r t' b n
```

`Relation.RelatesInSteps.succ'_iff` (lemma, [line 127](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L127))

```lean
lemma RelatesInSteps.succ'_iff {a b : α} {n : ℕ} :
    RelatesInSteps r a b (n + 1) ↔ ∃ t', r a t' ∧ RelatesInSteps r t' b n
```

`Relation.RelatesInSteps.apply_le_apply_add` (lemma, [line 138](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L138))

> If `h : α → ℕ` increases by at most 1 on each step of `r`,
> then the value of `h` at the output is at most `h` at the input plus the number of steps.

```lean
lemma RelatesInSteps.apply_le_apply_add {a b : α} {m : ℕ} (hevals : RelatesInSteps r a b m)
    (h : α → ℕ) (h_step : ∀ a b, r a b → h b ≤ h a + 1) :
    h b ≤ h a + m
```

`Relation.RelatesInSteps.map` (lemma, [line 151](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L151))

> If `g` is a homomorphism from `r` to `r'` (i.e., it preserves the reduction relation),
> then `RelatesInSteps` is preserved under `g`.

```lean
lemma RelatesInSteps.map {α α' : Type*}
    {r : α → α → Prop} {r' : α' → α' → Prop}
    (g : α → α') (hg : ∀ a b, r a b → r' (g a) (g b))
    {a b : α} {n : ℕ} (h : RelatesInSteps r a b n) :
    RelatesInSteps r' (g a) (g b) n
```

> ## Translating between `RelatesInSteps` and chains (`List.IsChainFromTo`)

`Relation.RelatesInSteps.exists_isChainFromTo` (lemma, [line 167](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L167))

> If `b` is related to `a` via `r` in `n` steps, then there is an `r`-chain of `n + 1` elements
> starting at `a` and ending at `b`.
> This is similar to `List.exists_isChain_ne_nil_of_relationReflTransGen`, but also provides
> a length guarantee.

```lean
lemma RelatesInSteps.exists_isChainFromTo {a b : α} {n : ℕ} (h : RelatesInSteps r a b n) :
    ∃ chain : List α, chain.IsChainFromTo r a b ∧ chain.length = n + 1
```

`List.IsChain.relatesInSteps_getElem` (lemma, [line 178](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L178))

> Any two elements along an `r`-chain are related in as many steps as their distance in the
> chain.

```lean
lemma _root_.List.IsChain.relatesInSteps_getElem {chain : List α} (hc : chain.IsChain r)
    (i k : ℕ) (hik : i + k < chain.length) :
    RelatesInSteps r chain[i] chain[i + k] k
```

`List.IsChainFromTo.relatesInSteps` (lemma, [line 189](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L189))

> If there is an `r`-chain of `n + 1` elements from `a` to `b`, then `a` and `b` are related
> to each other in `n` steps.

```lean
lemma _root_.List.IsChainFromTo.relatesInSteps {chain : List α} {n : ℕ}
    (hc : chain.IsChainFromTo r a b) (hlen : chain.length = n + 1) :
    RelatesInSteps r a b n
```

`Relation.relatesInSteps_iff_exists_isChainFromTo` (lemma, [line 198](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L198))

> `a` and `b` are related in `n` steps exactly when there is an `r`-chain of `n + 1` elements
> from `a` to `b`.

```lean
lemma relatesInSteps_iff_exists_isChainFromTo :
    RelatesInSteps r a b n ↔ ∃ chain : List α, chain.IsChainFromTo r a b ∧ chain.length = n + 1
```

> ## RelatesWithinSteps - only requires an upper bound on the number of steps

`Relation.RelatesWithinSteps` (definition, [line 208](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L208))

> `RelatesWithinSteps` is a variant of `RelatesInSteps` that allows for a loose bound.
> It states that `a` relates to `b` in *at most* `n` steps.

```lean
def RelatesWithinSteps (r : α → α → Prop) (a b : α) (n : ℕ) : Prop
```

`Relation.RelatesWithinSteps.of_relatesInSteps` (lemma, [line 212](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L212))

> `RelatesInSteps` implies `RelatesWithinSteps` with the same bound.

```lean
lemma RelatesWithinSteps.of_relatesInSteps {a b : α} {n : ℕ} (h : RelatesInSteps r a b n) :
    RelatesWithinSteps r a b n
```

`Relation.RelatesWithinSteps.refl` (lemma, [line 216](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L216))

```lean
lemma RelatesWithinSteps.refl (a : α) : RelatesWithinSteps r a a 0
```

`Relation.RelatesWithinSteps.single` (lemma, [line 219](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L219))

```lean
lemma RelatesWithinSteps.single {a b : α} (h : r a b) : RelatesWithinSteps r a b 1
```

`Relation.RelatesWithinSteps.zero` (lemma, [line 222](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L222))

```lean
lemma RelatesWithinSteps.zero {a b : α} (h : RelatesWithinSteps r a b 0) : a = b
```

`Relation.RelatesWithinSteps.zero_iff` (lemma, [line 227](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L227))

```lean
lemma RelatesWithinSteps.zero_iff {a b : α} : RelatesWithinSteps r a b 0 ↔ a = b
```

`Relation.RelatesWithinSteps.trans` (lemma, [line 235](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L235))

> Transitivity of `RelatesWithinSteps` in the sum of the step bounds.

```lean
lemma RelatesWithinSteps.trans {a b c : α} {n₁ n₂ : ℕ}
    (h₁ : RelatesWithinSteps r a b n₁) (h₂ : RelatesWithinSteps r b c n₂) :
    RelatesWithinSteps r a c (n₁ + n₂)
```

`Relation.RelatesWithinSteps.mono` (lemma, [line 244](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L244))

> If two elements `a` and `b` are related in at most `n₁` steps in the relation `r` and
> `n₁ ≤ n₂`, then they are also related in at most `n₂` steps.

```lean
lemma RelatesWithinSteps.mono {a b : α} : Monotone (RelatesWithinSteps r a b ·)
```

`Relation.RelatesWithinSteps.apply_le_apply_add` (lemma, [line 250](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L250))

> If `h : α → ℕ` increases by at most 1 on each step of `r`,
> then the value of `h` at the output is at most `h` at the input plus the step bound.

```lean
lemma RelatesWithinSteps.apply_le_apply_add {a b : α} {m : ℕ}
    (hevals : RelatesWithinSteps r a b m)
    (h : α → ℕ)
    (h_step : ∀ a b, r a b → h b ≤ h a + 1) :
    h b ≤ h a + m
```

`Relation.RelatesWithinSteps.map` (lemma, [line 263](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L263))

> If `g` is a homomorphism from `r` to `r'` (i.e., it preserves the reduction relation),
> then `RelatesWithinSteps` is preserved under `g`.

```lean
lemma RelatesWithinSteps.map {α α' : Type*} {r : α → α → Prop} {r' : α' → α' → Prop}
    (g : α → α') (hg : ∀ a b, r a b → r' (g a) (g b))
    {a b : α} {n : ℕ} (h : RelatesWithinSteps r a b n) :
    RelatesWithinSteps r' (g a) (g b) n
```

> ## Reachability under a bound on the number of reachable elements

`Relation.ReflTransGen.relatesInSteps_lt_encard` (theorem, [line 276](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean#L276))

> A more precise version of `ReflTransGen.relatesInSteps`: if `b` is reachable from `a`, then it
> is related to `a` in fewer steps than there are elements reachable from `a`.
> Note that this cardinality is an `ℕ∞`, and if it is infinite, no bound on the number of steps
> is stated.

```lean
theorem ReflTransGen.relatesInSteps_lt_encard {b : α} (h : ReflTransGen r a b) :
    ∃ n, RelatesInSteps r a b n ∧ (n : ℕ∞) < {x | ReflTransGen r a x}.encard
```

## Depends on

- [Chains with a designated start and end](../data/list/ischainfromto.md)

## Sources

- [Cslib/Foundations/Relation/RelatesInSteps.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Relation/RelatesInSteps.lean)
