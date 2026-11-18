---
declaration: def
origin: cited
lean: TauCeti.LaurentSeries.Level.algEquivOfFinrankEq
statement: formalized
---

# Finite extensions of `K⸨X⸩`

If `K` is algebraically closed of characteristic zero, then
every extension `L` of `K⸨X⸩` of degree `e` is isomorphic over `K⸨X⸩` to the ramified level
`K⸨u⸩`, `u ^ e = X`. The isomorphism is a chosen one: it is built from a chosen embedding of `L`
into the Puiseux field, whose image is the level-`e` subfield.

```lean
TauCeti.LaurentSeries.Level.algEquivOfFinrankEq.{u_1, u_2} {K : Type u_1} [Field K] [IsAlgClosed K]
  [CharZero K] {L : Type u_2} [Field L] [Algebra (LaurentSeries K) L] {e : ℕ+}
  (h : Module.finrank (LaurentSeries K) L = ↑e) :
  L ≃ₐ[LaurentSeries K] TauCeti.LaurentSeries.Level K e
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Newton–Puiseux theorem](../../part-02/other-results/part-02/newton-puiseux-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LaurentSeries.Level.algEquivOfFinrankEq`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Puiseux/FiniteExtension.html#TauCeti.LaurentSeries.Level.algEquivOfFinrankEq).

## Sources

- [Tau Ceti documentation: `TauCeti.LaurentSeries.Level.algEquivOfFinrankEq`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Puiseux/FiniteExtension.html#TauCeti.LaurentSeries.Level.algEquivOfFinrankEq)
- [Source of `TauCeti.LaurentSeries.Level.algEquivOfFinrankEq` in TauCeti/RingTheory/LaurentSeries/Puiseux/FiniteExtension.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/LaurentSeries/Puiseux/FiniteExtension.lean#L162)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
