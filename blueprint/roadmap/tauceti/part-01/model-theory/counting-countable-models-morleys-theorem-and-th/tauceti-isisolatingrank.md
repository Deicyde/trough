---
declaration: structure
origin: cited
lean: TauCeti.IsIsolatingRank
statement: formalized
---

# TauCeti.IsIsolatingRank

A countable, isomorphism-invariant rank that isolates each configuration's isomorphism
class at its own back-and-forth level. It need not be the least such level.

```lean
TauCeti.IsIsolatingRank.{u, v} {L : FirstOrder.Language} [L.IsRelational]
  (ρ : TauCeti.RelationalConfiguration L ℕ → Ordinal.{0}) : Prop
```

## Depends on

- [TauCeti.BFEquiv](../infinitary-syntax-back-and-forth-and-scott-analy/tauceti-bfequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.IsIsolatingRank`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Stratification.html#TauCeti.IsIsolatingRank).

## Sources

- [Tau Ceti documentation: `TauCeti.IsIsolatingRank`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Stratification.html#TauCeti.IsIsolatingRank)
- [Source of `TauCeti.IsIsolatingRank` in TauCeti/ModelTheory/Counting/Stratification.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/Counting/Stratification.lean#L76)
- [Tau Ceti roadmap status: Counting countable models: Morley's theorem and the Vaught toolkit](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CountableModelCounting/STATUS.md)
