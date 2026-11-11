---
declaration: theorem
origin: cited
lean: TauCeti.RelationalConfiguration.exists_limit_of_bfEquiv_chain
statement: formalized
proof: formalized
---

# The limit of a back-and-forth chain of configurations

If `α` is monotone and
`bfEquivSetoid (α i + ω)` relates `c i` and `c (i + 1)` for every `i`, then some configuration on
`ℕ` is related to every `c i` by `bfEquivSetoid (α i)`.

```lean
TauCeti.RelationalConfiguration.exists_limit_of_bfEquiv_chain.{u, v, o} {L : FirstOrder.Language}
  [L.IsRelational] {c : ℕ → TauCeti.RelationalConfiguration L ℕ} {α : ℕ → Ordinal.{o}}
  (hα : Monotone α)
  (h :
    ∀ (i : ℕ),
      (TauCeti.RelationalConfiguration.bfEquivSetoid L ℕ (α i + Ordinal.omega0)) (c i)
        (c (i + 1))) :
  ∃ d, ∀ (i : ℕ), (TauCeti.RelationalConfiguration.bfEquivSetoid L ℕ (α i)) d (c i)
```

## Depends on

- [TauCeti.BFEquiv](../infinitary-syntax-back-and-forth-and-scott-analy/tauceti-bfequiv.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.RelationalConfiguration.exists_limit_of_bfEquiv_chain`](https://taucetiproject.org/docs/TauCeti/ModelTheory/RelationalConfiguration/BackAndForth.html#TauCeti.RelationalConfiguration.exists_limit_of_bfEquiv_chain).

## Sources

- [Tau Ceti documentation: `TauCeti.RelationalConfiguration.exists_limit_of_bfEquiv_chain`](https://taucetiproject.org/docs/TauCeti/ModelTheory/RelationalConfiguration/BackAndForth.html#TauCeti.RelationalConfiguration.exists_limit_of_bfEquiv_chain)
- [Source of `TauCeti.RelationalConfiguration.exists_limit_of_bfEquiv_chain` in TauCeti/ModelTheory/RelationalConfiguration/BackAndForth.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/ModelTheory/RelationalConfiguration/BackAndForth.lean#L182)
- [Tau Ceti roadmap status: Counting countable models: Morley's theorem and the Vaught toolkit](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/CountableModelCounting/STATUS.md)
