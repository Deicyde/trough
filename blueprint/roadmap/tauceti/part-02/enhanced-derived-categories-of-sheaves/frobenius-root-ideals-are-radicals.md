---
declaration: theorem
origin: cited
lean: TauCeti.frobeniusRootIdeal_eq_radical
statement: formalized
proof: formalized
---

# Frobenius-root ideals are radicals

In a perfect ring, the Frobenius-root ideal of `f`
is the radical of the principal ideal `(f)`.

```lean
TauCeti.frobeniusRootIdeal_eq_radical.{u_1} {R : Type u_1} [CommSemiring R] {p : ℕ} [ExpChar R p]
  [PerfectRing R p] [hp : Fact (Nat.Prime p)] (f : R) :
  TauCeti.frobeniusRootIdeal R p f = (Ideal.span {f}).radical
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.frobeniusRootIdeal_eq_radical`](https://taucetiproject.org/docs/TauCeti/RingTheory/Perfect/FrobeniusRootIdeal.html#TauCeti.frobeniusRootIdeal_eq_radical).

## Sources

- [Tau Ceti documentation: `TauCeti.frobeniusRootIdeal_eq_radical`](https://taucetiproject.org/docs/TauCeti/RingTheory/Perfect/FrobeniusRootIdeal.html#TauCeti.frobeniusRootIdeal_eq_radical)
- [Source of `TauCeti.frobeniusRootIdeal_eq_radical` in TauCeti/RingTheory/Perfect/FrobeniusRootIdeal.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Perfect/FrobeniusRootIdeal.lean#L200)
- [Tau Ceti roadmap status: Enhanced derived categories of sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EnhancedDerivedSheaves/STATUS.md)
