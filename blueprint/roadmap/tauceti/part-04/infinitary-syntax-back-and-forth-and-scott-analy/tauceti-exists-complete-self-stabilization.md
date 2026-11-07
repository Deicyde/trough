---
declaration: theorem
origin: cited
lean: TauCeti.exists_complete_self_stabilization
statement: formalized
proof: formalized
---

# TauCeti.exists\_complete\_self\_stabilization

A countable structure stabilizes below `ω₁`. Only its tuples are counted; the language
may be uncountable.

```lean
TauCeti.exists_complete_self_stabilization.{u, v, w} {L : FirstOrder.Language} [L.IsRelational]
  (M : Type w) [L.Structure M] [Countable M] :
  ∃ α < Ordinal.omega 1, TauCeti.SelfStabilizesCompletely M α
```

## Depends on

- [TauCeti.BFEquiv](tauceti-bfequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.exists_complete_self_stabilization`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Scott/Stabilization.html#TauCeti.exists_complete_self_stabilization).

## Sources

- [Tau Ceti documentation: `TauCeti.exists_complete_self_stabilization`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Scott/Stabilization.html#TauCeti.exists_complete_self_stabilization)
- [Source of `TauCeti.exists_complete_self_stabilization` in TauCeti/ModelTheory/Scott/Stabilization.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/ModelTheory/Scott/Stabilization.lean#L178)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/InfinitaryLogic/STATUS.md)
