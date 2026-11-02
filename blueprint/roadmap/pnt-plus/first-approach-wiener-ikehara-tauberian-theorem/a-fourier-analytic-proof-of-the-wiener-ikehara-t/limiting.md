---
declaration: lemma
origin: cited
lean: limiting_fourier
statement: formalized
proof: formalized
---

# Limiting Fourier identity

If $\psi: \mathbb{R} \to \mathbb{C}$ is $C^2$ and compactly supported and $x \geq 1$, then

$$
\sum_{n=1}^\infty \frac{f(n)}{n} \hat \psi( \frac{1}{2\pi} \log \frac{n}{x} )
- A \int_{-\log x}^\infty \hat \psi(\frac{u}{2\pi})\ du
= \int_\mathbb{R} G(1+it) \psi(t) x^{it}\ dt.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [second-fourier](second-fourier.md)
- [first-fourier](first-fourier.md)

## Proof

By Lemma [first-fourier](first-fourier.md) and Lemma [second-fourier](second-fourier.md), we know that for any $\sigma>1$, we have

$$
\sum_{n=1}^\infty \frac{f(n)}{n^\sigma} \hat \psi( \frac{1}{2\pi} \log \frac{n}{x} )
- A x^{1-\sigma} \int_{-\log x}^\infty e^{-u(\sigma-1)} \hat \psi(\frac{u}{2\pi})\ du
= \int_\mathbb{R} G(\sigma+it) \psi(t) x^{it}\ dt.
$$

Now take limits as $\sigma \to 1$ using dominated convergence together with [(1)](README.md) and Lemma [Decay bounds](decay.md) to obtain the result.

## Lean

Formalized as [`limiting_fourier`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/limiting_fourier).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
