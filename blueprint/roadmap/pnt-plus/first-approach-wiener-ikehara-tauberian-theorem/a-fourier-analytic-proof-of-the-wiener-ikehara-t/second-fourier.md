---
declaration: lemma
origin: cited
lean: second_fourier
statement: formalized
proof: formalized
---

# second-fourier

If $\psi: \mathbb{R} \to \mathbb{C}$ is absolutely integrable and $x > 0$, then for any $\sigma>1$

$$
\int_{-\log x}^\infty e^{-u(\sigma-1)} \hat \psi(\frac{u}{2\pi})\ du =
x^{\sigma - 1} \int_\mathbb{R} \frac{1}{\sigma+it-1} \psi(t) x^{it}\ dt.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof

The left-hand side expands as

$$
\int_{-\log x}^\infty \int_\mathbb{R} e^{-u(\sigma-1)} \psi(t) e(-\frac{tu}{2\pi})\ dt\ du
$$

so by Fubini's theorem it suffices to verify the identity

$$
\begin{aligned}
\int_{-\log x}^\infty e^{-u(\sigma-1)} e(-\frac{tu}{2\pi})\ du
&= \int_{-\log x}^\infty e^{(it - \sigma + 1)u}\ du \\
&= \frac{1}{it - \sigma + 1} e^{(it - \sigma + 1)u}\ \Big|_{-\log x}^\infty \\
&= x^{\sigma - 1} \frac{1}{\sigma+it-1} x^{it}
\end{aligned}
$$

## Lean

Formalized as [`second_fourier`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/second_fourier).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
