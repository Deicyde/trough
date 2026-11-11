---
declaration: def
origin: cited
lean: TauCeti.BFScattered
statement: formalized
---

# TauCeti.BFScattered

A set `K` of configurations on `ℕ` is *back-and-forth scattered* when, at every countable
level `α`, the restriction of `bfEquivSetoid L ℕ α` to `K` has countably many classes. The set
`K` itself may be uncountable.

```lean
TauCeti.BFScattered.{u, v} {L : FirstOrder.Language} [L.IsRelational]
  (K : Set (TauCeti.RelationalConfiguration L ℕ)) : Prop
```

## Depends on

- [TauCeti.BFEquiv](../infinitary-syntax-back-and-forth-and-scott-analy/tauceti-bfequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.BFScattered`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Scattered/Basic.html#TauCeti.BFScattered).

## Sources

- [Tau Ceti documentation: `TauCeti.BFScattered`](https://taucetiproject.org/docs/TauCeti/ModelTheory/Counting/Scattered/Basic.html#TauCeti.BFScattered)
- [Source of `TauCeti.BFScattered` in TauCeti/ModelTheory/Counting/Scattered/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/Counting/Scattered/Basic.lean#L88)
- [Tau Ceti roadmap status: Counting countable models: Morley's theorem and the Vaught toolkit](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CountableModelCounting/STATUS.md)
