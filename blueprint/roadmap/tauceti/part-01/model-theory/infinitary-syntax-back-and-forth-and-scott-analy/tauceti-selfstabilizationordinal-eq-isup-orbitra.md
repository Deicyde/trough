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
- [Source of `TauCeti.selfStabilizationOrdinal_eq_iSup_orbitRank` in TauCeti/ModelTheory/Scott/Rank.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/Scott/Rank.lean#L141)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/InfinitaryLogic/STATUS.md)
