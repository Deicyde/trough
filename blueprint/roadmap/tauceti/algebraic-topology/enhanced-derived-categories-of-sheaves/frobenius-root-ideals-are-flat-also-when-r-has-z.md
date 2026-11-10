---
declaration: theorem
origin: cited
lean: TauCeti.flat_frobeniusRootIdeal
statement: formalized
proof: formalized
---

# Frobenius-root ideals are flat, also when `R` has zero divisors

```lean
TauCeti.flat_frobeniusRootIdeal.{u_1} {R : Type u_1} [CommRing R] {p : ℕ} [ExpChar R p]
  [PerfectRing R p] [hp : Fact (Nat.Prime p)] (f : R) :
  Module.Flat R ↥(TauCeti.frobeniusRootIdeal R p f)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.flat_frobeniusRootIdeal`](https://taucetiproject.org/docs/TauCeti/RingTheory/Perfect/FrobeniusRootIdeal.html#TauCeti.flat_frobeniusRootIdeal).

## Sources

- [Tau Ceti documentation: `TauCeti.flat_frobeniusRootIdeal`](https://taucetiproject.org/docs/TauCeti/RingTheory/Perfect/FrobeniusRootIdeal.html#TauCeti.flat_frobeniusRootIdeal)
- [Source of `TauCeti.flat_frobeniusRootIdeal` in TauCeti/RingTheory/Perfect/FrobeniusRootIdeal.lean](https://github.com/TauCetiProject/TauCeti/blob/ace60277c4c5ba2166795686bca1af4052290145/TauCeti/RingTheory/Perfect/FrobeniusRootIdeal.lean#L233)
- [Tau Ceti roadmap status: Enhanced derived categories of sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/eaf17b10d9267c0e3cdd3b62dd5e8983e47c690d/TauCetiRoadmap/EnhancedDerivedSheaves/STATUS.md)
