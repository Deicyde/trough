---
declaration: theorem
origin: cited
lean: TauCeti.isZero_Tor_succ_of_perfectRing
statement: formalized
proof: formalized
---

# Tor independence of perfect rings

For perfect algebras `B` and `C` over a perfect ring `A`
of prime characteristic `p`, `Tor_{n+1}^A(B, C) = 0`.

```lean
TauCeti.isZero_Tor_succ_of_perfectRing.{u} {A : Type u} [CommRing A] {p : ℕ} [ExpChar A p]
  [PerfectRing A p] [Fact (Nat.Prime p)] (B C : Type u) [CommRing B] [CommRing C] [Algebra A B]
  [Algebra A C] [ExpChar B p] [PerfectRing B p] [ExpChar C p] [PerfectRing C p] (n : ℕ) :
  CategoryTheory.Limits.IsZero (((CategoryTheory.Tor (ModuleCat A) (n + 1)).obj ↧B).obj ↧C)
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.isZero_Tor_succ_of_perfectRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Perfect/Tor.html#TauCeti.isZero_Tor_succ_of_perfectRing).

## Sources

- [Tau Ceti documentation: `TauCeti.isZero_Tor_succ_of_perfectRing`](https://taucetiproject.org/docs/TauCeti/RingTheory/Perfect/Tor.html#TauCeti.isZero_Tor_succ_of_perfectRing)
- [Source of `TauCeti.isZero_Tor_succ_of_perfectRing` in TauCeti/RingTheory/Perfect/Tor.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/RingTheory/Perfect/Tor.lean#L157)
- [Tau Ceti roadmap status: Enhanced derived categories of sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/EnhancedDerivedSheaves/STATUS.md)
