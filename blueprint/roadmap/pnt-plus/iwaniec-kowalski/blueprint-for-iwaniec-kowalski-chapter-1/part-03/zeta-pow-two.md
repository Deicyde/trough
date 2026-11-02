---
declaration: theorem
origin: cited
lean: ArithmeticFunction.zeta_pow_two
statement: formalized
proof: formalized
---

# zeta pow two

$$
\zeta(s)^2 =\zeta(2s) \sum_{n=1}^{\infty} 2^{\omega(n)} n^{-s}
$$

for $\Re(s) > 1$.

```
An expression for `ζ^2`, in IK (1.31).
```

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [two-pow-omega-LSeries-eulerProduct-tprod](two-pow-omega-lseries-eulerproduct-tprod.md)
- [two-pow-omega-LSeries-eulerProduct-hasProd](two-pow-omega-lseries-eulerproduct-hasprod.md)
- [Complex.one-add-prime-cpow-ne-zero](complex-one-add-prime-cpow-ne-zero.md)

## Proof

Note that

$$
\zeta(s)^2=\prod_p\frac{1}{(1-p^{-s})^2}.
$$

Similarly

$$
\zeta(2s)=\prod_p\frac{1}{(1-p^{-2s})}.
$$

Applying Theorems two-pow-omega-LSeries-eulerProduct-tprod and two-pow-omega-LSeries-eulerProduct-hasProd we have

$$
\sum_{1\leq n}2^{\omega(n)}n^{-s}=\prod_p\frac{1+p^{-s}}{1-p^{-s}}.
$$

Thus

$$
\zeta(2s)\left(\sum_{1\leq n}2^{\omega(n)}n^{-s}\right)=\prod_p\frac{1+p^{-s}}{(1-p^{-s})(1-p^{-2s})}=\prod_p\frac{1}{(1-p^{-s})^2}
$$

by the difference of squares. This is exactly the Euler product for $\zeta(s)^2$ mentioned earlier.

## Lean

Formalized as [`ArithmeticFunction.zeta_pow_two`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ArithmeticFunction.zeta_pow_two).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/IwaniecKowalskiCh1.lean)
