---
declaration: lemma
origin: cited
lean: log_pow_over_xsq_integral_bounded
statement: formalized
proof: formalized
---

# log-pow-over-xsq-integral-bounded

For every $0\lt n$ there exists a constant $C>0$ (depending on $n$) such that

$$
\int_3^T\frac{(\log x)^n}{x^2}dx < C
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Real.log-le-const-mul-rpow](real-log-le-const-mul-rpow.md)

## Proof

Using the previous lemma, we know for all $0\lt c$ and $0\lt x$ that

$$
(\log x)^n\leq (cx^{1/c})^n=c^nx^{n/c}.
$$

Now if we choose $c=2n$ then

$$
\frac{(\log x)^n}{x^2}\leq (2n)^nx^{-3/2}.
$$

This function is dominates the integrand and is integrable in $x$ by the $p$-test.

## Lean

Formalized as [`log_pow_over_xsq_integral_bounded`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/log_pow_over_xsq_integral_bounded).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/MediumPNT.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/MediumPNT.lean)
