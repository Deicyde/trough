---
declaration: def
origin: cited
lean: MvPolynomial.weightedIndex
statement: formalized
---

# MvPolynomial.weightedIndex

The weighted index is the least reciprocal-weighted order of a nonzero Hasse jet;
the infimum of the empty set is `⊤`.

```lean
MvPolynomial.weightedIndex.{u_1, u_2} {σ : Type u_1} {R : Type u_2} [CommSemiring R] (r : σ → ℕ)
  (a : σ → R) (P : MvPolynomial σ R) : ENNReal
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`MvPolynomial.weightedIndex`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/WeightedIndex.html#MvPolynomial.weightedIndex).

## Sources

- [Tau Ceti documentation: `MvPolynomial.weightedIndex`](https://taucetiproject.org/docs/TauCeti/RingTheory/MvPolynomial/WeightedIndex.html#MvPolynomial.weightedIndex)
- [Source of `MvPolynomial.weightedIndex` in TauCeti/RingTheory/MvPolynomial/WeightedIndex.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/MvPolynomial/WeightedIndex.lean#L81)
- [Tau Ceti roadmap status: Diophantine approximation and transcendence](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/DiophantineApproximationAndTranscendence/STATUS.md)
