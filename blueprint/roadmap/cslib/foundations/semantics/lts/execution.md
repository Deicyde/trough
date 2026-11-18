---
catalog: module
lean: Cslib.LTS.Execution, Cslib.LTS.Execution.of_tr, Cslib.LTS.Execution.length, Cslib.LTS.Execution.length', Cslib.LTS.Execution.length_ss_pos, Cslib.LTS.Execution.ss_ne_nil, Cslib.LTS.Execution.nonEmpty_states, Cslib.LTS.Execution.head, Cslib.LTS.Execution.start, Cslib.LTS.Execution.getLast, Cslib.LTS.Execution.last, Cslib.LTS.Execution.last', Cslib.LTS.Execution.trans, Cslib.LTS.Execution.mk, Cslib.LTS.execution_iff_index, Cslib.LTS.Execution.cons_invert, Cslib.LTS.Execution.cons_cons_invert, Cslib.LTS.Execution.tail_of_length_pos, Cslib.LTS.Execution.of_mTr, Cslib.LTS.Execution.to_mTr, Cslib.LTS.Execution.isChainFromTo, Cslib.LTS.Execution.isChain, Cslib.LTS.mTr_iff_execution, Cslib.LTS.Execution.comp, Cslib.LTS.Execution.take, Cslib.LTS.Execution.drop, Cslib.LTS.Execution.split
statement: formalized
proof: formalized
---

# Finite executions of LTS

`Cslib.Foundations.Semantics.LTS.Execution`, in [Cslib/Foundations/Semantics/LTS/Execution.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean), by Fabrizio Montesi, Ching-Tsun Chou, Thomas Waring.

> A finite execution of `lts : LTS State Label`, a proposition `lts.Execution s μs t ss`, which says
> that `lts` can transition from `s` to `t` through `ss` using the transition labels `μ`. That is,
> the lists have the form `μs = [μ₀, μ₁, ..., μₙ]` and `ss = [s, s₁, s₂, ..., sₙ, t]`, and there are
> transitions `lts.Tr s μ₀ s₁`, `lts.Tr s₁ μ₁ s₂`, ..., `lts.Tr sₙ μₙ t`.
>
> We define `Cslib.LTS.Execution` as an inductive proposition, which is equivalent to the definition
> in terms of indicies: see `Cslib.LTS.Execution.mk` and `Cslib.LTS.execution_iff_index`.

`Cslib.LTS.Execution` (inductive type, [line 42](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L42))

> `Execution` extends `MTr` by providing the intermediate states of a multistep transition:
> `lts.Execution s₁ μs s₂ ss` means that `lts` can transition from `s₁` to `s₂` through `ss` using
> the transition labels `μ`. This is equivalent to the proposition:
> ```lean
> ∃ _ : ss.length = μs.length + 1, ss[0] = s₁ ∧ ss[ss.length - 1] = s₂ ∧
>   ∀ k < μs.length, lts.Tr ss[k] μ[k] ss[k + 1].
> ```
> Access that formulation as a constructor using `Cslib.LTS.Execution.mk`, and its projections as
> `Cslib.LTS.Execution.length`, `Cslib.LTS.Execution.start`, `Cslib.LTS.Execution.last` and
> `Cslib.LTS.Execution.trans`.

```lean
inductive Execution (lts : LTS State Label) :
    (s : State) → (μs : List Label) → (t : State) → (ss : List State) → Prop where
  /-- Every state has an execution of zero steps terminating in itself. -/
  | refl (s : State) : lts.Execution s [] s [s]
  /-- Equivalent of `MTr.stepL` for executions. -/
  | stepL {r s t : State} {μ : Label} {μs : List Label} {ss : List State}
      (htr : lts.Tr r μ s) (hex : lts.Execution s μs t ss) :
      lts.Execution r (μ :: μs) t (r :: ss)
```

`Cslib.LTS.Execution.of_tr` (theorem, [line 53](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L53))

```lean
theorem of_tr (h : lts.Tr s μ t) : lts.Execution s [μ] t [s, t]
```

`Cslib.LTS.Execution.length` (theorem, [line 59](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L59))

> The lengths of `μs` and `ss` are constrained by the fact that each label `μ ∈ μs` represents
> a transition between two states in `ss`.

```lean
theorem length (h : lts.Execution s μs t ss) : ss.length = μs.length + 1
```

`Cslib.LTS.Execution.length'` (theorem, [line 62](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L62))

```lean
theorem length' (h : lts.Execution s μs t ss) :
  μs.length = ss.length - 1
```

`Cslib.LTS.Execution.length_ss_pos` (theorem, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L67))

> Transitions have positive length.

```lean
theorem length_ss_pos (h : lts.Execution s μs t ss) : 0 < ss.length
```

`Cslib.LTS.Execution.ss_ne_nil` (theorem, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L72))

> Every execution has at least one intermediate state.

```lean
theorem ss_ne_nil (h : lts.Execution s μs t ss) : ss ≠ []
```

`Cslib.LTS.Execution.nonEmpty_states` (alias, [line 75](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L75))

```lean
alias nonEmpty_states
```

`Cslib.LTS.Execution.head` (theorem, [line 78](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L78))

> `s` is the first state of the execution.

```lean
theorem head (h : lts.Execution s μs t ss) : ss.head h.ss_ne_nil = s
```

`Cslib.LTS.Execution.start` (theorem, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L82))

> Alternative accessor for `Cslib.LTS.Execution.head`.

```lean
theorem start (h : lts.Execution s μs t ss) : ss[0]'(h.length_ss_pos) = s
```

`Cslib.LTS.Execution.getLast` (theorem, [line 87](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L87))

> `t` is the last state of the execution.

```lean
theorem getLast (h : lts.Execution s μs t ss) :
    ss.getLast h.ss_ne_nil = t
```

`Cslib.LTS.Execution.last` (theorem, [line 95](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L95))

> Alternative accessor for `Cslib.LTS.Execution.getLast`.

```lean
theorem last (h : lts.Execution s μs t ss) :
    ss[ss.length - 1]'(by lia [h.length_ss_pos]) = t
```

`Cslib.LTS.Execution.last'` (theorem, [line 101](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L101))

> Alternative accessor for `Cslib.LTS.Execution.getLast`.

```lean
theorem last' (h : lts.Execution s μs t ss) :
  ss[μs.length]'(by grind) = t
```

`Cslib.LTS.Execution.trans` (theorem, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L107))

> `lts` transitions along the `k`th label in `μs` between the `k`th and `(k + 1)`th states in
> `ss`.

```lean
theorem trans (h : lts.Execution s μs t ss) (k : ℕ) (hk : k < μs.length) :
    lts.Tr (ss[k]'(by lia [h.length])) μs[k] (ss[k + 1]'(by lia [h.length]))
```

`Cslib.LTS.Execution.mk` (theorem, [line 122](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L122))

> Alternative constructor for `Cslib.LTS.Execution`, in terms of the indexed collections of
> states and labels.

```lean
protected theorem mk {s t : State} {μs : List Label} {ss : List State}
    (length : ss.length = μs.length + 1) (start : ss[0] = s) (last : ss[ss.length - 1] = t)
    (trans : ∀ k (hk : k < μs.length), lts.Tr ss[k] μs[k] ss[k + 1]) :
    lts.Execution s μs t ss
```

`Cslib.LTS.execution_iff_index` (theorem, [line 141](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L141))

> The inductive definition of `Cslib.LTS.Execution` is equivalent to that in terms of indices.

```lean
theorem _root_.Cslib.LTS.execution_iff_index :
    lts.Execution s μs t ss ↔
      ∃ (_ : ss.length = μs.length + 1), ss[0] = s ∧ ss[ss.length - 1] = t ∧
        ∀ k (_ : k < μs.length), lts.Tr ss[k] μs[k] ss[k + 1]
```

`Cslib.LTS.Execution.cons_invert` (theorem, [line 148](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L148))

> Deconstruction of executions with `List.cons`.

```lean
theorem cons_invert (h : lts.Execution s (μ :: μs) t (s :: ss)) :
    lts.Execution (ss[0]'(by grind)) μs t ss
```

`Cslib.LTS.Execution.cons_cons_invert` (theorem, [line 155](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L155))

> Deconstruct a positive-length execution, with a specific value for the second state in the
> sequence.

```lean
theorem cons_cons_invert (h : lts.Execution r (μ :: μs) t (r' :: s :: ss)) :
    lts.Execution s μs t (s :: ss)
```

`Cslib.LTS.Execution.tail_of_length_pos` (theorem, [line 161](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L161))

> Trim the first state from a positive-length execution.

```lean
theorem tail_of_length_pos (he : lts.Execution s μs t ss) (hlen : 0 < μs.length) :
    lts.Execution (ss[1]'(by grind)) μs.tail t ss.tail
```

`Cslib.LTS.Execution.of_mTr` (theorem, [line 169](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L169))

> A multistep transition implies the existence of an execution.

```lean
theorem of_mTr {lts : LTS State Label} {s : State} {μs : List Label} {t : State}
    (h : lts.MTr s μs t) : ∃ ss : List State, lts.Execution s μs t ss
```

`Cslib.LTS.Execution.to_mTr` (theorem, [line 180](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L180))

> Converts an execution into a multistep transition.

```lean
theorem to_mTr (hex : lts.Execution s μs t ss) :
    lts.MTr s μs t
```

`Cslib.LTS.Execution.isChainFromTo` (theorem, [line 188](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L188))

> The states visited by an execution form a chain from the initial to the final state
> in the underlying unlabelled relation.

```lean
theorem isChainFromTo (hex : lts.Execution s μs t ss) :
    ss.IsChainFromTo lts.UnlabelledTr s t
```

`Cslib.LTS.Execution.isChain` (theorem, [line 195](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L195))

> The states visited by an execution form a chain in the underlying unlabelled relation.

```lean
theorem isChain (hex : lts.Execution s μs t ss) :
    ss.IsChain lts.UnlabelledTr
```

`Cslib.LTS.mTr_iff_execution` (theorem, [line 201](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L201))

> Correspondence of multistep transitions and executions.

```lean
theorem _root_.Cslib.LTS.mTr_iff_execution :
    lts.MTr s μs t ↔ ∃ ss : List State, lts.Execution s μs t ss
```

`Cslib.LTS.Execution.comp` (theorem, [line 206](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L206))

> The composition of two executions is an execution.

```lean
theorem comp {lts : LTS State Label} {s r t : State} {μs₁ μs₂ : List Label} {ss₁ ss₂ : List State}
    (h₁ : lts.Execution s μs₁ r ss₁) (h₂ : lts.Execution r μs₂ t ss₂) :
    lts.Execution s (μs₁ ++ μs₂) t (ss₁ ++ ss₂.tail)
```

`Cslib.LTS.Execution.take` (theorem, [line 214](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L214))

> The states up to `ss[n]` form an execution.

```lean
theorem take (he : lts.Execution s μs t ss) (n : ℕ) (hn : n < ss.length) :
    lts.Execution s (μs.take n) ss[n] (ss.take (n + 1))
```

`Cslib.LTS.Execution.drop` (theorem, [line 224](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L224))

> The states from `ss[n]` onward form an execution.

```lean
theorem drop (he : lts.Execution s μs t ss) (n : ℕ) (hn : n < ss.length) :
    lts.Execution ss[n] (μs.drop n) t (ss.drop n)
```

`Cslib.LTS.Execution.split` (theorem, [line 237](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean#L237))

> Split an execution at an intermediate state `ss[n]`.

```lean
theorem split (he : lts.Execution s μs t ss) {n : ℕ} (hn : n < ss.length) :
    lts.Execution s (μs.take n) ss[n] (ss.take (n + 1)) ∧
      lts.Execution ss[n] (μs.drop n) t (ss.drop n)
```

## Depends on

- [Chains with a designated start and end](../../data/list/ischainfromto.md)
- [Labelled Transition System (LTS)](basic.md)

## Sources

- [Cslib/Foundations/Semantics/LTS/Execution.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Execution.lean)
