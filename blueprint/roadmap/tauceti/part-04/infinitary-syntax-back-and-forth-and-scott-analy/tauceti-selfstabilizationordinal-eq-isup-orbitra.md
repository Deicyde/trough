---
declaration: theorem
origin: cited
lean: TauCeti.selfStabilizationOrdinal_eq_iSup_orbitRank
statement: formalized
proof: formalized
---

# TauCeti.selfStabilizationOrdinal\_eq\_iSup\_orbitRank

The least simultaneous stabilization level is the supremum of the orbit ranks
of all finite tuples. This holds for arbitrary structures.

```lean
TauCeti.selfStabilizationOrdinal_eq_iSup_orbitRank.{u, v, w} {L : FirstOrder.Language}
  [L.IsRelational] {M : Type w} [L.Structure M] :
  TauCeti.selfStabilizationOrdinal M = ⨆ p, TauCeti.orbitRank p.snd
```

## Depends on

- [TauCeti.BFEquiv](tauceti-bfequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.selfStabilizationOrdinal_eq_iSup_orbitRank`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Scott/Rank.html#TauCeti.selfStabilizationOrdinal_eq_iSup_orbitRank).

## Sources

- [Tau Ceti documentation: `TauCeti.selfStabilizationOrdinal_eq_iSup_orbitRank`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Scott/Rank.html#TauCeti.selfStabilizationOrdinal_eq_iSup_orbitRank)
- [Source of `TauCeti.selfStabilizationOrdinal_eq_iSup_orbitRank` in TauCeti/ModelTheory/Scott/Rank.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/ModelTheory/Scott/Rank.lean#L141)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/InfinitaryLogic/STATUS.md)
