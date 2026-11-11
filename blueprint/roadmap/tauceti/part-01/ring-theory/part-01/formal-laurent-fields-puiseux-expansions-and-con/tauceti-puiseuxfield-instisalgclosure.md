---
declaration: theorem
origin: cited
lean: TauCeti.puiseuxField.instIsAlgClosure
statement: formalized
proof: formalized
---

# TauCeti.puiseuxField.instIsAlgClosure

Over an algebraically closed field `K` of characteristic zero, the Puiseux field is an
algebraic closure of the Laurent-series field `K⸨X⸩`.

```lean
TauCeti.puiseuxField.instIsAlgClosure.{u_1} {K : Type u_1} [Field K] [IsAlgClosed K] [CharZero K] :
  IsAlgClosure (LaurentSeries K) ↥(TauCeti.puiseuxField K)
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Newton–Puiseux theorem](../../part-02/other-results/part-02/newton-puiseux-theorem.md)

## Lean

Formalized in Tau Ceti as [`TauCeti.puiseuxField.instIsAlgClosure`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Puiseux/AlgClosure.html#TauCeti.puiseuxField.instIsAlgClosure).

## Sources

- [Tau Ceti documentation: `TauCeti.puiseuxField.instIsAlgClosure`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Puiseux/AlgClosure.html#TauCeti.puiseuxField.instIsAlgClosure)
- [Source of `TauCeti.puiseuxField.instIsAlgClosure` in TauCeti/RingTheory/LaurentSeries/Puiseux/AlgClosure.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/LaurentSeries/Puiseux/AlgClosure.lean#L68)
- [Tau Ceti roadmap status: Formal Laurent fields, Puiseux expansions and continuous differential calculus](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/FormalLaurentPuiseux/STATUS.md)
