---
catalog: module
lean: Cslib.LTS.union, Cslib.LTS.unionSubtype, Cslib.LTS.inl, Cslib.LTS.inr, Cslib.LTS.unionSum, Cslib.LTS.unionSum_tr_inl_inl, Cslib.LTS.unionSum_tr_inr_inr, Cslib.LTS.unionSum_not_tr_inl_inr, Cslib.LTS.unionSum_not_tr_inr_inl, Cslib.LTS.unionSum_mTr_inl, Cslib.LTS.unionSum_mTr_inr, Cslib.LTS.unionSum_mTr_inl_iff, Cslib.LTS.unionSum_mTr_inr_iff
statement: formalized
proof: formalized
---

# Union of LTSs

`Cslib.Foundations.Semantics.LTS.Union`, in [Cslib/Foundations/Semantics/LTS/Union.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Union.lean), by Fabrizio Montesi.

> Note: there is a nontrivial balance between ergonomics and generality here. These definitions might
> change in the future.

`Cslib.LTS.union` (definition, [line 27](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Union.lean#L27))

> The union of two LTSs defined on the same types.

```lean
def union (lts1 lts2 : LTS State Label) : LTS State Label
```

`Cslib.LTS.unionSubtype` (definition, [line 31](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Union.lean#L31))

> The union of two LTSs that have common supertypes for states and labels.

```lean
def unionSubtype
{S1 : State → Prop} {L1 : Label → Prop} {S2 : State → Prop} {L2 : Label → Prop}
(lts1 : LTS (@Subtype State S1) (@Subtype Label L1))
(lts2 : LTS (@Subtype State S2) (@Subtype Label L2)) :
  LTS State Label
```

`Cslib.LTS.inl` (definition, [line 41](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Union.lean#L41))

> Lifting of an `LTS State Label` to `LTS (State ⊕ State') Label`.

```lean
def inl (lts : LTS State Label) :
    LTS { x : State ⊕ State' // x.isLeft } { _label : Label // True }
```

`Cslib.LTS.inr` (definition, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Union.lean#L49))

> Lifting of an `LTS State Label` to `LTS (State' ⊕ State) Label`.

```lean
def inr (lts : LTS State Label) :
    LTS { x : State' ⊕ State // x.isRight } { _label : Label // True }
```

`Cslib.LTS.unionSum` (definition, [line 58](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Union.lean#L58))

> Union of two LTSs with the same `Label` type. The result combines the original respective
> state types `State1` and `State2` into `(State1 ⊕ State2)`.

```lean
def unionSum (lts1 : LTS State1 Label) (lts2 : LTS State2 Label) :
    LTS (State1 ⊕ State2) Label
```

`Cslib.LTS.unionSum_tr_inl_inl` (theorem, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Union.lean#L67))

```lean
theorem unionSum_tr_inl_inl {s s' : State1} {μ : Label} :
    (unionSum lts1 lts2).Tr (.inl s) μ (.inl s') ↔ lts1.Tr s μ s'
```

`Cslib.LTS.unionSum_tr_inr_inr` (theorem, [line 72](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Union.lean#L72))

```lean
theorem unionSum_tr_inr_inr {s s' : State2} {μ : Label} :
    (unionSum lts1 lts2).Tr (.inr s) μ (.inr s') ↔ lts2.Tr s μ s'
```

`Cslib.LTS.unionSum_not_tr_inl_inr` (theorem, [line 77](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Union.lean#L77))

```lean
theorem unionSum_not_tr_inl_inr {s : State1} {s' : State2} {μ : Label} :
    ¬(unionSum lts1 lts2).Tr (.inl s) μ (.inr s')
```

`Cslib.LTS.unionSum_not_tr_inr_inl` (theorem, [line 82](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Union.lean#L82))

```lean
theorem unionSum_not_tr_inr_inl {s : State2} {s' : State1} {μ : Label} :
    ¬(unionSum lts1 lts2).Tr (.inr s) μ (.inl s')
```

`Cslib.LTS.unionSum_mTr_inl` (theorem, [line 88](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Union.lean#L88))

> A run of `unionSum lts1 lts2` from a state of `lts1` stays among the states of `lts1`, where it
> is a run of `lts1`.

```lean
theorem unionSum_mTr_inl {s : State1} {μs : List Label} {y : State1 ⊕ State2}
    (h : (unionSum lts1 lts2).MTr (.inl s) μs y) : ∃ t, y = .inl t ∧ lts1.MTr s μs t
```

`Cslib.LTS.unionSum_mTr_inr` (theorem, [line 103](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Union.lean#L103))

> A run of `unionSum lts1 lts2` from a state of `lts2` stays among the states of `lts2`, where it
> is a run of `lts2`.

```lean
theorem unionSum_mTr_inr {s : State2} {μs : List Label} {y : State1 ⊕ State2}
    (h : (unionSum lts1 lts2).MTr (.inr s) μs y) : ∃ t, y = .inr t ∧ lts2.MTr s μs t
```

`Cslib.LTS.unionSum_mTr_inl_iff` (theorem, [line 117](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Union.lean#L117))

> The runs of `unionSum lts1 lts2` between states of `lts1` are the runs of `lts1`.

```lean
theorem unionSum_mTr_inl_iff {s t : State1} {μs : List Label} :
    (unionSum lts1 lts2).MTr (.inl s) μs (.inl t) ↔ lts1.MTr s μs t
```

`Cslib.LTS.unionSum_mTr_inr_iff` (theorem, [line 128](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Union.lean#L128))

> The runs of `unionSum lts1 lts2` between states of `lts2` are the runs of `lts2`.

```lean
theorem unionSum_mTr_inr_iff {s t : State2} {μs : List Label} :
    (unionSum lts1 lts2).MTr (.inr s) μs (.inr t) ↔ lts2.MTr s μs t
```

## Depends on

- [Labelled Transition System (LTS)](basic.md)

## Sources

- [Cslib/Foundations/Semantics/LTS/Union.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/LTS/Union.lean)
