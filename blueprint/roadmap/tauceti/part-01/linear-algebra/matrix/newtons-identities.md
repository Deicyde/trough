---
declaration: theorem
origin: cited
lean: LinearMap.mul_coeff_reverse_charpoly_eq_neg_sum, Matrix.mul_coeff_charpolyRev_eq_neg_sum
statement: formalized
proof: formalized
---

# Newton's identities

**Newton's identities** for the traces of the powers of an endomorphism `f` of a finite free
module: the coefficients `c_r` of `det (1 - X f)`, the reverse of the characteristic polynomial,
and the traces `p_j = tr (f ^ j)` satisfy `r c_r = -(c_(r-1) p_1 + c_(r-2) p_2 + ⋯ + c_0 p_r)`.

```lean
LinearMap.mul_coeff_reverse_charpoly_eq_neg_sum.{u_1, u_2} {R : Type u_1} {M : Type u_2}
  [CommRing R] [AddCommGroup M] [_root_.Module R M] [Module.Free R M] [Module.Finite R M]
  (f : Module.End R M) (r : ℕ) :
  ↑r * (LinearMap.charpoly f).reverse.coeff r =
    -∑ j ∈ Finset.range r,
        (LinearMap.charpoly f).reverse.coeff (r - (j + 1)) * (LinearMap.trace R M) (f ^ (j + 1))
```

## Depends on

Its statement uses no other declaration mapped here.

## Proof depends on

- [Newton's identities for a multiset](../../ring-theory/part-01/multivariate-polynomials/newtons-identities-for-a-multiset.md)
- [Vieta's formula for `det (1 - X A)`](vietas-formula-for-det-1-x-a.md)

## Lean

Formalized in Tau Ceti as [`LinearMap.mul_coeff_reverse_charpoly_eq_neg_sum`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Charpoly/Newton.html#LinearMap.mul_coeff_reverse_charpoly_eq_neg_sum).

## Other forms

**Newton's identities for the traces of the powers of a matrix.** Formalized in Tau Ceti as [`Matrix.mul_coeff_charpolyRev_eq_neg_sum`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Charpoly/Newton.html#Matrix.mul_coeff_charpolyRev_eq_neg_sum).

```lean
Matrix.mul_coeff_charpolyRev_eq_neg_sum.{u_1, u_3} {n : Type u_1} {R : Type u_3} [Fintype n]
  [DecidableEq n] [CommRing R] (A : Matrix n n R) (r : ℕ) :
  ↑r * A.charpolyRev.coeff r =
    -∑ j ∈ Finset.range r, A.charpolyRev.coeff (r - (j + 1)) * (A ^ (j + 1)).trace
```

## Sources

- [Tau Ceti documentation: `LinearMap.mul_coeff_reverse_charpoly_eq_neg_sum`](https://taucetiproject.org/docs/TauCeti/LinearAlgebra/Matrix/Charpoly/Newton.html#LinearMap.mul_coeff_reverse_charpoly_eq_neg_sum)
- [Source of `LinearMap.mul_coeff_reverse_charpoly_eq_neg_sum` in TauCeti/LinearAlgebra/Matrix/Charpoly/Newton.lean](https://github.com/TauCetiProject/TauCeti/blob/a6027b1d24fcb935c53bd5b50d11b40991cda418/TauCeti/LinearAlgebra/Matrix/Charpoly/Newton.lean#L193)
