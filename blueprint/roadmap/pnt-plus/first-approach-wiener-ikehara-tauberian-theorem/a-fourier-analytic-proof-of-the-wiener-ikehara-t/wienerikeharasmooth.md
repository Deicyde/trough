---
declaration: corollary
origin: cited
lean: wiener_ikehara_smooth
statement: formalized
proof: formalized
---

# Smoothed Wiener-Ikehara

If $\Psi: (0,\infty) \to \mathbb{C}$ is smooth and compactly supported away from the origin, then,

$$
\sum_{n=1}^\infty f(n) \Psi( \frac{n}{x} ) = A x \int_0^\infty \Psi(y)\ dy + o(x)
$$

as $x \to \infty$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Limiting identity for Schwartz functions](schwarz-id.md)
- [Bijectivity of Fourier transform](bij.md)

## Proof

By Lemma [Bijectivity of Fourier transform](bij.md), we can write

$$
y \Psi(y) = \hat \psi( \frac{1}{2\pi} \log y )
$$

for all $y>0$ and some Schwartz function $\psi$. Making this substitution, the claim is then equivalent after standard manipulations to

$$
\sum_{n=1}^\infty \frac{f(n)}{n} \hat \psi( \frac{1}{2\pi} \log \frac{n}{x} )
= A \int_{-\infty}^\infty \hat \psi(\frac{u}{2\pi})\ du + o(1)
$$

and the claim follows from Lemma [Limiting identity for Schwartz functions](schwarz-id.md).

## Lean

Formalized as [`wiener_ikehara_smooth`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/wiener_ikehara_smooth).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
