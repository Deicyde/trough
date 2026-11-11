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
- [Source of `TauCeti.LaurentSeries.Level.algEquivOfFinrankEq` in TauCeti/RingTheory/LaurentSeries/Puiseux/FiniteExtension.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/LaurentSeries/Puiseux/FiniteExtension.lean#L123)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
