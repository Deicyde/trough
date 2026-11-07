---
declaration: theorem
origin: cited
lean: TauCeti.internalScottRank_lt_omega_one
statement: formalized
proof: formalized
---

# TauCeti.internalScottRank\_lt\_omega\_one

Every countable structure has internal Scott rank below the first uncountable ordinal.
The relational language need not be countable.

```lean
TauCeti.internalScottRank_lt_omega_one.{u, v, w} {L : FirstOrder.Language} [L.IsRelational]
  {M : Type w} [L.Structure M] [Countable M] : TauCeti.internalScottRank M < Ordinal.omega 1
```

## Depends on

- [TauCeti.BFEquiv](tauceti-bfequiv.md)

## Proof depends on

- [TauCeti.exists\_complete\_self\_stabilization](tauceti-exists-complete-self-stabilization.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.internalScottRank_lt_omega_one`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Scott/Rank.html#TauCeti.internalScottRank_lt_omega_one).

## Sources

- [Tau Ceti documentation: `TauCeti.internalScottRank_lt_omega_one`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Scott/Rank.html#TauCeti.internalScottRank_lt_omega_one)
- [Source of `TauCeti.internalScottRank_lt_omega_one` in TauCeti/ModelTheory/Scott/Rank.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/ModelTheory/Scott/Rank.lean#L216)
- [Tau Ceti roadmap status: Infinitary syntax, back-and-forth, and Scott analysis](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/Completed/InfinitaryLogic/STATUS.md)
