---
declaration: theorem
origin: cited
lean: TauCeti.selfStabilizationOrdinal_eq_iSup_orbitRank
statement: formalized
proof: formalized
---

# TauCeti.selfStabilizationOrdinal_eq_iSup_orbitRank

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
- [Source of `TauCeti.selfStabilizationOrdinal_eq_iSup_orbitRank` in TauCeti/ModelTheory/Scott/Rank.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/ModelTheory/Scott/Rank.lean#L139)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/InfinitaryLogic/STATUS.md)
