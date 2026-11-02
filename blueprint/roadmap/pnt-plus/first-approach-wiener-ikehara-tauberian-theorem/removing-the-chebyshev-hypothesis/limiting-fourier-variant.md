---
declaration: lemma
origin: cited
lean: limiting_fourier_variant
statement: formalized
proof: formalized
---

# limiting-fourier-variant

If $\psi: \mathbb{R} \to \mathbb{C}$ is $C^2$ and compactly supported with $f$ and $\hat \psi$ non-negative, and $0 < x$, then

$$
\sum_{n=1}^\infty \frac{f(n)}{n} \hat \psi( \frac{1}{2\pi} \log \frac{n}{x} ) - A \int_{-\log x}^\infty \hat \psi(\frac{u}{2\pi})\ du =  \int_\mathbb{R} G(1+it) \psi(t) x^{it}\ dt.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [second-fourier](../a-fourier-analytic-proof-of-the-wiener-ikehara-t/second-fourier.md)
- [first-fourier](../a-fourier-analytic-proof-of-the-wiener-ikehara-t/first-fourier.md)
- [Decay bounds](../a-fourier-analytic-proof-of-the-wiener-ikehara-t/decay.md)

## Proof

Repeat the proof of Lemma limiting-fourier-variant, but use monotone convergence instead of dominated convergence. (The proof should be simpler, as one no longer needs to establish domination for the sum.)

## Lean

Formalized as [`limiting_fourier_variant`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/limiting_fourier_variant).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
