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

- [Newton–Puiseux theorem](newton-puiseux-theorem.md)
- [TauCeti.puiseuxField.levelGalEquivRootsOfUnity](tauceti-puiseuxfield-levelgalequivrootsofunity.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.LaurentSeries.Level.algEquivOfFinrankEq`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Puiseux/FiniteExtension.html#TauCeti.LaurentSeries.Level.algEquivOfFinrankEq).

## Sources

- [Tau Ceti documentation: `TauCeti.LaurentSeries.Level.algEquivOfFinrankEq`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Puiseux/FiniteExtension.html#TauCeti.LaurentSeries.Level.algEquivOfFinrankEq)
- [Source of `TauCeti.LaurentSeries.Level.algEquivOfFinrankEq` in TauCeti/RingTheory/LaurentSeries/Puiseux/FiniteExtension.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/LaurentSeries/Puiseux/FiniteExtension.lean#L129)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
