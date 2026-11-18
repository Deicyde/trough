---
catalog: module
lean: Cslib.DistributedConsistency.isTrans_ar, Cslib.DistributedConsistency.so_iff_se_rb, Cslib.DistributedConsistency.so_le_rb, Cslib.DistributedConsistency.se_rval_eq_none, Cslib.DistributedConsistency.singleOrder_vis_ar_rval_ne_none, Cslib.DistributedConsistency.singleOrder_realTime_imp_readMyWrites, Cslib.DistributedConsistency.linearizability_imp_sequentialConsistency, Cslib.DistributedConsistency.readMyWrites_imp_hb_le_trans_vis, Cslib.DistributedConsistency.singleOrder_readMyWrites_imp_causalArbitration, Cslib.DistributedConsistency.causalVisibility_imp_readMyWrites, Cslib.DistributedConsistency.causalVisibility_imp_monotonicReads, Cslib.DistributedConsistency.causalVisibility_imp_noCircularCausality, Cslib.DistributedConsistency.singleOrder_readMyWrites_imp_causalVisibility, Cslib.DistributedConsistency.singleOrder_imp_eventualVisibility, Cslib.DistributedConsistency.sequentialConsistency_imp_causalConsistency, Cslib.DistributedConsistency.causalConsistency_imp_basicEventualConsistency
statement: formalized
proof: formalized
---

# Consistency hierarchy

`Cslib.Computability.Distributed.Consistency.Hierarchy`, in [Cslib/Computability/Distributed/Consistency/Hierarchy.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Hierarchy.lean), by Ching-Tsun Chou.

> We prove a number of results about the various notions of consistency for replicated data types.
> In paricular, we prove that:
>
>   Linearizability → SequentialConsistency → CausalConsistency → BasicEventualConsistency
>
> Our proofs follow closely the proofs of Lemma 5.1 and Proposition 5.1 of [Burckhardt2014].
>
> ## References
>
> * [*Principles of Eventual Consistency*][Burckhardt2014]

`Cslib.DistributedConsistency.isTrans_ar` (instance, [line 37](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Hierarchy.lean#L37))

```lean
instance isTrans_ar : IsTrans Event a.ar
```

`Cslib.DistributedConsistency.so_iff_se_rb` (lemma, [line 40](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Hierarchy.lean#L40))

```lean
lemma so_iff_se_rb (s : Session) (x y : Event) :
    a.so s x y ↔ a.se x = s ∧ a.se y = s ∧ a.rb x y
```

`Cslib.DistributedConsistency.so_le_rb` (lemma, [line 45](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Hierarchy.lean#L45))

```lean
lemma so_le_rb (s : Session) : a.so s ≤ a.rb
```

`Cslib.DistributedConsistency.se_rval_eq_none` (lemma, [line 49](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Hierarchy.lean#L49))

```lean
lemma se_rval_eq_none {s : Session} {x : Event} (h1 : a.se x = s) (h2 : a.rval x = none) :
    {y | a.se y = s} = {y | a.se y = s ∧ a.rb y x } ∪ {x}
```

`Cslib.DistributedConsistency.singleOrder_vis_ar_rval_ne_none` (lemma, [line 62](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Hierarchy.lean#L62))

```lean
lemma singleOrder_vis_ar_rval_ne_none (h : a.SingleOrder) (x y : Event) :
    (a.vis x y → a.ar x y) ∧ (a.ar x y → a.rval x ≠ none → a.vis x y)
```

`Cslib.DistributedConsistency.singleOrder_realTime_imp_readMyWrites` (lemma, [line 67](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Hierarchy.lean#L67))

```lean
lemma singleOrder_realTime_imp_readMyWrites
    (h1 : a.SingleOrder) (h2 : a.RealTime) : a.ReadMyWrites
```

`Cslib.DistributedConsistency.linearizability_imp_sequentialConsistency` (theorem, [line 74](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Hierarchy.lean#L74))

```lean
theorem linearizability_imp_sequentialConsistency
    (h : a.Linearizability d) : a.SequentialConsistency d
```

`Cslib.DistributedConsistency.readMyWrites_imp_hb_le_trans_vis` (lemma, [line 78](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Hierarchy.lean#L78))

```lean
lemma readMyWrites_imp_hb_le_trans_vis
    (h : a.ReadMyWrites) : a.hb ≤ TransGen a.vis
```

`Cslib.DistributedConsistency.singleOrder_readMyWrites_imp_causalArbitration` (lemma, [line 86](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Hierarchy.lean#L86))

```lean
lemma singleOrder_readMyWrites_imp_causalArbitration
    (h1 : a.SingleOrder) (h2 : a.ReadMyWrites) : a.CausalArbitration
```

`Cslib.DistributedConsistency.causalVisibility_imp_readMyWrites` (lemma, [line 97](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Hierarchy.lean#L97))

```lean
lemma causalVisibility_imp_readMyWrites
    (h : a.CausalVisibility) : a.ReadMyWrites
```

`Cslib.DistributedConsistency.causalVisibility_imp_monotonicReads` (lemma, [line 102](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Hierarchy.lean#L102))

```lean
lemma causalVisibility_imp_monotonicReads
    (h : a.CausalVisibility) : a.MonotonicReads
```

`Cslib.DistributedConsistency.causalVisibility_imp_noCircularCausality` (lemma, [line 107](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Hierarchy.lean#L107))

```lean
lemma causalVisibility_imp_noCircularCausality
    (h : a.CausalVisibility) : a.NoCircularCausality
```

`Cslib.DistributedConsistency.singleOrder_readMyWrites_imp_causalVisibility` (lemma, [line 111](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Hierarchy.lean#L111))

```lean
lemma singleOrder_readMyWrites_imp_causalVisibility
    (h1 : a.SingleOrder) (h2 : a.ReadMyWrites) : a.CausalVisibility
```

`Cslib.DistributedConsistency.singleOrder_imp_eventualVisibility` (lemma, [line 118](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Hierarchy.lean#L118))

```lean
lemma singleOrder_imp_eventualVisibility
    (h : a.SingleOrder) : a.EventualVisibility
```

`Cslib.DistributedConsistency.sequentialConsistency_imp_causalConsistency` (theorem, [line 140](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Hierarchy.lean#L140))

```lean
theorem sequentialConsistency_imp_causalConsistency
    (h : a.SequentialConsistency d) : a.CausalConsistency d
```

`Cslib.DistributedConsistency.causalConsistency_imp_basicEventualConsistency` (theorem, [line 145](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Hierarchy.lean#L145))

```lean
theorem causalConsistency_imp_basicEventualConsistency
    (h : a.CausalConsistency d) : a.BasicEventualConsistency d
```

## Depends on

- [Consistency specifications](specification.md)

## Proof depends on

- [Basic properties of relations](../../../foundations/relation/basic.md)

## Sources

- [Cslib/Computability/Distributed/Consistency/Hierarchy.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Computability/Distributed/Consistency/Hierarchy.lean)
