---
declaration: theorem
origin: cited
lean: TauCeti.internalScottRank_lt_omega_one
statement: formalized
proof: formalized
---

# TauCeti.internalScottRank_lt_omega_one

Every countable structure has internal Scott rank below the first uncountable ordinal.
The relational language need not be countable.

```lean
TauCeti.internalScottRank_lt_omega_one.{u, v, w} {L : FirstOrder.Language} [L.IsRelational]
  {M : Type w} [L.Structure M] [Countable M] : TauCeti.internalScottRank M < Ordinal.omega 1
```

## Depends on

- [TauCeti.BFEquiv](tauceti-bfequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.internalScottRank_lt_omega_one`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Scott/Rank.html#TauCeti.internalScottRank_lt_omega_one).

## Sources

- [Tau Ceti documentation: `TauCeti.internalScottRank_lt_omega_one`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Scott/Rank.html#TauCeti.internalScottRank_lt_omega_one)
- [Source of `TauCeti.internalScottRank_lt_omega_one` in TauCeti/ModelTheory/Scott/Rank.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/Scott/Rank.lean#L216)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/Completed/InfinitaryLogic/STATUS.md)
