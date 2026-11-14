---
catalog: module
lean: Cslib.FLTS.IsSyncTrace, Cslib.FLTS.HasSyncTrace
statement: formalized
proof: formalized
---

# Synchronising traces

`Cslib.Foundations.Semantics.FLTS.SyncTrace`, in [Cslib/Foundations/Semantics/FLTS/SyncTrace.lean](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/SyncTrace.lean), by Fabrizio Montesi.

> This module defines synchronising traces for `FLTS`.

`Cslib.FLTS.IsSyncTrace` (definition, [line 24](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/SyncTrace.lean#L24))

> A trace `μs` is synchronising if following it from any two states leads to the same state.

```lean
def IsSyncTrace (flts : FLTS State Label) (μs : List Label) : Prop
```

`Cslib.FLTS.HasSyncTrace` (definition, [line 28](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/SyncTrace.lean#L28))

> `flts` is synchronising, i.e., it has at least one synchronising trace.

```lean
def HasSyncTrace (flts : FLTS State Label) : Prop
```

## Depends on

- [Functional Labelled Transition System (FLTS)](basic.md)

## Sources

- [Cslib/Foundations/Semantics/FLTS/SyncTrace.lean at 86d560b6](https://github.com/leanprover/cslib/blob/86d560b6cbb379bd82512424cbcd2a915a1565e7/Cslib/Foundations/Semantics/FLTS/SyncTrace.lean)
