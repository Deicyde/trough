---
declaration: theorem
origin: cited
lean: TauCeti.TerminalCut.min_pairMinimumValue_le
statement: formalized
proof: formalized
---

# Ultrametric inequality for minimum cut values

every cut separating `s` from `t`
separates `s` from `v` or `v` from `t`. The intermediate vertex `v` is arbitrary.

```lean
TauCeti.TerminalCut.min_pairMinimumValue_le.{u_1, u_3} {V : Type u_1} {K : Type u_3} [Finite V]
  [Zero K] [LinearOrder K] (f : Finset V → K) {s t : V} (hst : s ≠ t) (v : V) :
  min (TauCeti.TerminalCut.pairMinimumValue f s v) (TauCeti.TerminalCut.pairMinimumValue f v t) ≤
    TauCeti.TerminalCut.pairMinimumValue f s t
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.TerminalCut.min_pairMinimumValue_le`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/MinimumCut/Basic.html#TauCeti.TerminalCut.min_pairMinimumValue_le).

## Sources

- [Tau Ceti documentation: `TauCeti.TerminalCut.min_pairMinimumValue_le`](https://taucetiproject.org/docs/TauCeti/Combinatorics/Network/MinimumCut/Basic.html#TauCeti.TerminalCut.min_pairMinimumValue_le)
- [Source of `TauCeti.TerminalCut.min_pairMinimumValue_le` in TauCeti/Combinatorics/Network/MinimumCut/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/Combinatorics/Network/MinimumCut/Basic.lean#L499)
- [Tau Ceti roadmap status: Finite graph connectivity and network flows](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/GraphConnectivityAndFlows/STATUS.md)
