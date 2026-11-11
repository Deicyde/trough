---
declaration: theorem
origin: cited
lean: TauCeti.sq_eq_two_mul_mul_pow_three_add_one_iff
statement: formalized
proof: formalized
---

# The integer points of the Heegner quartic

The integer solutions of `y² = 2u(u³ + 1)` are
exactly `(u, y) = (-1, 0), (0, 0), (1, ±2), (2, ±6)`.

```lean
TauCeti.sq_eq_two_mul_mul_pow_three_add_one_iff {u y : ℤ} :
  y ^ 2 = 2 * u * (u ^ 3 + 1) ↔ (u, y) ∈ {(-1, 0), (0, 0), (1, 2), (1, -2), (2, 6), (2, -6)}
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`TauCeti.sq_eq_two_mul_mul_pow_three_add_one_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassNumberOne/HeegnerQuartic.html#TauCeti.sq_eq_two_mul_mul_pow_three_add_one_iff).

## Sources

- [Tau Ceti documentation: `TauCeti.sq_eq_two_mul_mul_pow_three_add_one_iff`](https://taucetiproject.org/docs/TauCeti/NumberTheory/ClassNumberOne/HeegnerQuartic.html#TauCeti.sq_eq_two_mul_mul_pow_three_add_one_iff)
- [Source of `TauCeti.sq_eq_two_mul_mul_pow_three_add_one_iff` in TauCeti/NumberTheory/ClassNumberOne/HeegnerQuartic.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/NumberTheory/ClassNumberOne/HeegnerQuartic.lean#L264)
- [Tau Ceti roadmap status: Imaginary quadratic fields: class numbers, finiteness and class number one](https://github.com/TauCetiProject/TauCetiRoadmap/blob/9f7c032adaf1b838e8183d63ff3cfa886d061cb3/TauCetiRoadmap/ImaginaryQuadraticClassNumber/STATUS.md)
