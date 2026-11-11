---
declaration: theorem
origin: cited
lean: Matrix.coeff_charpolyRev_eq_esymm_roots_charpoly_of_splits
statement: formalized
proof: formalized
---

# Vieta's formula for `det (1 - X A)`

If the characteristic polynomial of `A` splits, the
`r`-th coefficient of `det (1 - X A)` is `(-1) ^ r` times the `r`-th elementary symmetric function
of the characteristic roots of `A`, counted with algebraic multiplicity.

```lean
Matrix.coeff_charpolyRev_eq_esymm_roots_charpoly_of_splits.{u_1, u_2} {n : Type u_1} {K : Type u_2}
  [Fintype n] [DecidableEq n] [CommRing K] [IsDomain K] {A : Matrix n n K} (hA : A.charpoly.Splits)
  (r : ℕ) : A.charpolyRev.coeff r = (-1) ^ r * A.charpoly.roots.esymm r
```

## Depends on

Its statement uses no other declaration mapped here.

## Lean

Formalized in Tau Ceti as [`Matrix.coeff_charpolyRev_eq_esymm_roots_charpoly_of_splits`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Charpoly/Roots.html#Matrix.coeff_charpolyRev_eq_esymm_roots_charpoly_of_splits).

## Sources

- [Tau Ceti documentation: `Matrix.coeff_charpolyRev_eq_esymm_roots_charpoly_of_splits`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Charpoly/Roots.html#Matrix.coeff_charpolyRev_eq_esymm_roots_charpoly_of_splits)
- [Source of `Matrix.coeff_charpolyRev_eq_esymm_roots_charpoly_of_splits` in TauCeti/LinearAlgebra/Matrix/Charpoly/Roots.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/Matrix/Charpoly/Roots.lean#L164)
