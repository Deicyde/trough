---
declaration: def
origin: cited
lean: TauCeti.Finance.IsSelfFinancing
statement: formalized
---

# TauCeti.Finance.IsSelfFinancing

A simple strategy holding `a j` shares of stock and `b j` shares of bond on
`(τ j, τ (j + 1)]` is **self-financing** for the prices `S` and `β` if every rebalancing is paid
for by the old position: at each date `τ (j + 1)` with `j + 1 < n`, the new portfolio costs what
the old one is worth.

```lean
TauCeti.Finance.IsSelfFinancing.{u_1, u_2} {Ω : Type u_1} {ι : Type u_2} (τ : ℕ → ι) (n : ℕ)
  (a b : ℕ → Ω → ℝ) (S β : ι → Ω → ℝ) : Prop
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.Finance.IsSelfFinancing`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/SimpleStrategy/Basic.html#TauCeti.Finance.IsSelfFinancing).

## Sources

- [Tau Ceti documentation: `TauCeti.Finance.IsSelfFinancing`](https://taucetiproject.org/docs/TauCeti/Probability/Finance/SimpleStrategy/Basic.html#TauCeti.Finance.IsSelfFinancing)
- [Source of `TauCeti.Finance.IsSelfFinancing` in TauCeti/Probability/Finance/SimpleStrategy/Basic.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/Probability/Finance/SimpleStrategy/Basic.lean#L443)
- [Tau Ceti roadmap status: Financial mathematics: one-factor markets and replication](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FinancialMathematics/STATUS.md)
