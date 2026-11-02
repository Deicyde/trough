---
declaration: lemma
origin: cited
lean: first_fourier
statement: formalized
proof: formalized
---

# first-fourier

If $\psi: \mathbb{R} \to \mathbb{C}$ is integrable and $x > 0$, then for any $\sigma>1$

$$
\sum_{n=1}^\infty \frac{f(n)}{n^\sigma} \hat \psi( \frac{1}{2\pi} \log \frac{n}{x} ) =
\int_\mathbb{R} F(\sigma + it) \psi(t) x^{it}\ dt.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

By the definition of the Fourier transform, the left-hand side expands as

$$
\sum_{n=1}^\infty \int_\mathbb{R} \frac{f(n)}{n^\sigma} \psi(t) e( - \frac{1}{2\pi} t \log
\frac{n}{x})\ dt
$$

while the right-hand side expands as

$$
\int_\mathbb{R} \sum_{n=1}^\infty \frac{f(n)}{n^{\sigma+it}} \psi(t) x^{it}\ dt.
$$

Since

$$
\frac{f(n)}{n^\sigma} \psi(t) e( - \frac{1}{2\pi} t \log \frac{n}{x}) =
\frac{f(n)}{n^{\sigma+it}} \psi(t) x^{it}
$$

the claim then follows from Fubini's theorem.

## Lean

Formalized as [`first_fourier`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/first_fourier).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
