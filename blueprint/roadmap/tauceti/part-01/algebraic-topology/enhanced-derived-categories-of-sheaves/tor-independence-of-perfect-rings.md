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
- [Source of `TauCeti.isZero_Tor_succ_of_perfectRing` in TauCeti/RingTheory/Perfect/Tor.lean](https://github.com/TauCetiProject/TauCeti/blob/cd41bffcb343151b3e58c89392e206b11fe78c1c/TauCeti/RingTheory/Perfect/Tor.lean#L157)
- [Tau Ceti roadmap status: Enhanced derived categories of sheaves](https://github.com/TauCetiProject/TauCetiRoadmap/blob/612845ab80fb9c2b9bee724a156756ee78031591/TauCetiRoadmap/EnhancedDerivedSheaves/STATUS.md)
