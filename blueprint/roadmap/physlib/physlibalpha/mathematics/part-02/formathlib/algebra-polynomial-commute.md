---
declaration: module
origin: cited
lean: Polynomial.commute_of_commute_coeff, Polynomial.mul_eq_neg_mul_of_coeff
statement: formalized
proof: formalized
---

# Commuting and anticommuting polynomials

The module `PhyslibAlpha.Mathematics.ForMathlib.Algebra.Polynomial.Commute`, [PhyslibAlpha/Mathematics/ForMathlib/Algebra/Polynomial/Commute.lean](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Algebra/Polynomial/Commute.lean): 2 declarations, 2 with a docstring.

> Polynomials over a noncommutative ring commute, or anticommute, when their coefficients do.

## i. Overview

> Over a noncommutative ring the polynomials are themselves noncommutative. The coefficient of
> `X ^ n` in `p * q` is the sum over the antidiagonal of `p.coeff a * q.coeff b`, and in `q * p` it
> is the same sum with the factors in the opposite order. So two polynomials commute as soon as
> each coefficient of the one commutes with each coefficient of the other, and they anticommute as
> soon as the coefficients pairwise anticommute.

## ii. Key results

> - `Polynomial.commute_of_commute_coeff` : polynomials with pairwise commuting coefficients
>   commute.
> - `Polynomial.mul_eq_neg_mul_of_coeff` : polynomials with pairwise anticommuting coefficients
>   anticommute.

## iv. References

> * None.

## A. Commuting and anticommuting coefficients

**`Polynomial.commute_of_commute_coeff`**, a lemma, [line 52](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Algebra/Polynomial/Commute.lean#L52).

> Two polynomials commute as soon as each coefficient of the one commutes with each
> coefficient of the other. The coefficients of the two products are the same sums over the
> antidiagonal, read in opposite orders.

```lean
lemma commute_of_commute_coeff {R : Type*} [Semiring R]
    {p q : Polynomial R} (h : ∀ a b, Commute (p.coeff a) (q.coeff b)) : Commute p q
```

**`Polynomial.mul_eq_neg_mul_of_coeff`**, a lemma, [line 62](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Algebra/Polynomial/Commute.lean#L62).

> Two polynomials anticommute as soon as each coefficient of the one anticommutes with
> each coefficient of the other.

```lean
lemma mul_eq_neg_mul_of_coeff {R : Type*} [Ring R] {p q : Polynomial R}
    (h : ∀ a b, p.coeff a * q.coeff b = -(q.coeff b * p.coeff a)) : p * q = -(q * p)
```

## Depends on

Its declarations' statements use no declaration of another module with an article here.

## Sources

- [PhyslibAlpha/Mathematics/ForMathlib/Algebra/Polynomial/Commute.lean at d6a3586e](https://github.com/leanprover-community/physlib/blob/d6a3586eb33124da3d6740c9e609d8adbf87e651/PhyslibAlpha/Mathematics/ForMathlib/Algebra/Polynomial/Commute.lean)
