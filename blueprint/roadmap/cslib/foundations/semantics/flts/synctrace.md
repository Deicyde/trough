---
catalog: module
lean: Cslib.FLTS.IsSyncTrace, Cslib.FLTS.HasSyncTrace, Cslib.FLTS.PairwiseHasSyncTrace, Cslib.FLTS.hasSyncTrace_iff_pairwiseHasSyncTrace
statement: formalized
proof: formalized
---

# Synchronising traces

`Cslib.Foundations.Semantics.FLTS.SyncTrace`, in [Cslib/Foundations/Semantics/FLTS/SyncTrace.lean](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Semantics/FLTS/SyncTrace.lean), by Fabrizio Montesi.

> This module defines synchronising traces for `FLTS`.
>
> For finite state spaces, `hasSyncTrace_iff_pairwiseHasSyncTrace` characterises synchronisation by
> the ability to merge each pair of states, possibly using a different trace for each pair.
> The label type need not be finite.
>
> ## References
>
> * [M. V. Volkov, *Synchronization of finite automata*][Volkov2022], Proposition 2.1.

`Cslib.FLTS.IsSyncTrace` (definition, [line 32](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Semantics/FLTS/SyncTrace.lean#L32))

> A trace `μs` is synchronising if following it from any two states leads to the same state.

```lean
def IsSyncTrace (flts : FLTS State Label) (μs : List Label) : Prop
```

`Cslib.FLTS.HasSyncTrace` (definition, [line 36](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Semantics/FLTS/SyncTrace.lean#L36))

> `flts` is synchronising, i.e., it has at least one synchronising trace.

```lean
def HasSyncTrace (flts : FLTS State Label) : Prop
```

`Cslib.FLTS.PairwiseHasSyncTrace` (definition, [line 40](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Semantics/FLTS/SyncTrace.lean#L40))

> Every pair of states can be merged by some trace, which may depend on the pair.

```lean
def PairwiseHasSyncTrace (flts : FLTS State Label) : Prop
```

`Cslib.FLTS.hasSyncTrace_iff_pairwiseHasSyncTrace` (theorem, [line 61](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Semantics/FLTS/SyncTrace.lean#L61))

> A finite-state `FLTS` has a synchronising trace iff every pair of states can be merged
> by some trace. This is the pairwise synchronisation criterion of Liu and Černý;
> see [Volkov2022], Proposition 2.1.

```lean
theorem hasSyncTrace_iff_pairwiseHasSyncTrace [Finite State] (flts : FLTS State Label) :
    flts.HasSyncTrace ↔ flts.PairwiseHasSyncTrace
```

## Depends on

- [Functional Labelled Transition System (FLTS)](basic.md)

## Sources

- [Cslib/Foundations/Semantics/FLTS/SyncTrace.lean at 8b510d01](https://github.com/leanprover/cslib/blob/8b510d014295ed2c2334a379a7c96561a1603dc4/Cslib/Foundations/Semantics/FLTS/SyncTrace.lean)
- [Declaration ledger](../../../../../sources/cslib/Cslib.Foundations.Semantics.FLTS.SyncTrace.json)
