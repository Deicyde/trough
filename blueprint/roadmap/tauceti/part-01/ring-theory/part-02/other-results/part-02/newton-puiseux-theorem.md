---
declaration: theorem
origin: cited
lean: TauCeti.LaurentSeries.exists_isRoot_map_expand, TauCeti.puiseuxField.exists_isRoot_levelEmbedding
statement: formalized
proof: formalized
---

# Newton–Puiseux theorem

Over an algebraically closed field `K` of characteristic zero,
every nonconstant polynomial `P` over `K⸨X⸩` has a root after a finite ramification: for some
`n > 0`, the polynomial `P(X ^ n)` obtained by substituting `X ↦ X ^ n` in its coefficients has a
root in `K⸨X⸩`.

```lean
TauCeti.LaurentSeries.exists_isRoot_map_expand.{u_1} {K : Type u_1} [Field K] [IsAlgClosed K]
  [CharZero K] {P : Polynomial (LaurentSeries K)} (hP : P.degree ≠ 0) :
  ∃ n y, (Polynomial.map (↑(LaurentSeries.expand K n)) P).IsRoot y
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.LaurentSeries.exists_isRoot_map_expand`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/NewtonPuiseux.html#TauCeti.LaurentSeries.exists_isRoot_map_expand).

## Other forms

**Newton–Puiseux theorem.** Formalized in Tau Ceti as [`TauCeti.puiseuxField.exists_isRoot_levelEmbedding`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/Puiseux/AlgClosure.html#TauCeti.puiseuxField.exists_isRoot_levelEmbedding).

```lean
TauCeti.puiseuxField.exists_isRoot_levelEmbedding.{u_1} {K : Type u_1} [Field K] [IsAlgClosed K]
  [CharZero K] {P : Polynomial ↥(TauCeti.puiseuxField K)} (hP : P.degree ≠ 0) :
  ∃ n y, P.IsRoot ((TauCeti.puiseuxField.levelEmbedding K n) y)
```

## Sources

- [Tau Ceti documentation: `TauCeti.LaurentSeries.exists_isRoot_map_expand`](https://taucetiproject.org/docs/TauCeti/RingTheory/LaurentSeries/NewtonPuiseux.html#TauCeti.LaurentSeries.exists_isRoot_map_expand)
- [Source of `TauCeti.LaurentSeries.exists_isRoot_map_expand` in TauCeti/RingTheory/LaurentSeries/NewtonPuiseux.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/LaurentSeries/NewtonPuiseux.lean#L126)
