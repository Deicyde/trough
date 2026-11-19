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
- [Source of `TauCeti.internalScottRank_lt_omega_one` in TauCeti/ModelTheory/Scott/Rank.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/ModelTheory/Scott/Rank.lean#L214)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/Completed/InfinitaryLogic/STATUS.md)
