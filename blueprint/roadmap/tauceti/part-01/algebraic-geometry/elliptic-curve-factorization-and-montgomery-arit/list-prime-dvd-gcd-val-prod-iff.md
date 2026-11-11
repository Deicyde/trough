---
declaration: theorem
origin: cited
lean: List.prime_dvd_gcd_val_prod_iff
statement: formalized
proof: formalized
---

# List.prime_dvd_gcd_val_prod_iff

A prime divides the product gcd exactly when it divides some leaf gcd, without requiring
that it divide the modulus. In particular, the empty product has no prime divisor.

```lean
List.prime_dvd_gcd_val_prod_iff {n : ℕ} (L : List (ZMod n)) {p : ℕ} (hp : Nat.Prime p) :
  p ∣ L.prod.val.gcd n ↔ ∃ t ∈ L, p ∣ t.val.gcd n
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`List.prime_dvd_gcd_val_prod_iff`](https://taucetiproject.org/docs/TauCeti/Data/ZMod/ProductGCD.html#List.prime_dvd_gcd_val_prod_iff).

## Sources

- [Tau Ceti documentation: `List.prime_dvd_gcd_val_prod_iff`](https://taucetiproject.org/docs/TauCeti/Data/ZMod/ProductGCD.html#List.prime_dvd_gcd_val_prod_iff)
- [Source of `List.prime_dvd_gcd_val_prod_iff` in TauCeti/Data/ZMod/ProductGCD.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/Data/ZMod/ProductGCD.lean#L43)
- [Tau Ceti roadmap status: Elliptic-curve factorization and Montgomery arithmetic](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ECM/STATUS.md)
