---
declaration: theorem
origin: cited
lean: TauCeti.puiseuxField.exists_isRoot_levelEmbedding, TauCeti.LaurentSeries.exists_isRoot_map_expand
statement: formalized
proof: formalized
---

# Newton–Puiseux theorem

Over an algebraically closed field `K` of characteristic zero,
every nonconstant polynomial over the Puiseux field has a root lying in a single ramified level.

```lean
TauCeti.puiseuxField.exists_isRoot_levelEmbedding.{u_1} {K : Type u_1} [Field K] [IsAlgClosed K]
  [CharZero K] {P : Polynomial ↥(TauCeti.puiseuxField K)} (hP : P.degree ≠ 0) :
  ∃ n y, P.IsRoot ((TauCeti.puiseuxField.levelEmbedding K n) y)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.puiseuxField.exists_isRoot_levelEmbedding`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Puiseux/AlgClosure.html#TauCeti.puiseuxField.exists_isRoot_levelEmbedding).

## Other forms

**Newton–Puiseux theorem.** Formalized in Tau Ceti as [`TauCeti.LaurentSeries.exists_isRoot_map_expand`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/NewtonPuiseux.html#TauCeti.LaurentSeries.exists_isRoot_map_expand).

```lean
TauCeti.LaurentSeries.exists_isRoot_map_expand.{u_1} {K : Type u_1} [Field K] [IsAlgClosed K]
  [CharZero K] {P : Polynomial (LaurentSeries K)} (hP : P.degree ≠ 0) :
  ∃ n y, (Polynomial.map (↑(LaurentSeries.expand K n)) P).IsRoot y
```

## Sources

- [Tau Ceti documentation: `TauCeti.puiseuxField.exists_isRoot_levelEmbedding`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Puiseux/AlgClosure.html#TauCeti.puiseuxField.exists_isRoot_levelEmbedding)
- [Source of `TauCeti.puiseuxField.exists_isRoot_levelEmbedding` in TauCeti/RingTheory/LaurentSeries/Puiseux/AlgClosure.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/LaurentSeries/Puiseux/AlgClosure.lean#L52)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
