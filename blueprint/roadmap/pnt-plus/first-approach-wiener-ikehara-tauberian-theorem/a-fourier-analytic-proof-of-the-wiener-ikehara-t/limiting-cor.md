---
declaration: corollary
origin: cited
lean: limiting_cor
statement: formalized
proof: formalized
---

# Corollary of limiting identity

With the hypotheses as above, we have

$$
\sum_{n=1}^\infty \frac{f(n)}{n} \hat \psi( \frac{1}{2\pi} \log \frac{n}{x} )
= A \int_{-\infty}^\infty \hat \psi(\frac{u}{2\pi})\ du + o(1)
$$

as $x \to \infty$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Limiting Fourier identity](limiting.md)

## Proof

Immediate from the Riemann-Lebesgue lemma, and also noting that $\int_{-\infty}^{-\log x} \hat \psi(\frac{u}{2\pi})\ du = o(1)$.

## Lean

Formalized as [`limiting_cor`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/limiting_cor).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
