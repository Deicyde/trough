---
declaration: lemma
origin: cited
lean: limiting_cor_schwartz
statement: formalized
proof: formalized
---

# Limiting identity for Schwartz functions

The previous corollary also holds for functions $\psi$ that are assumed to be in the Schwartz class, as opposed to being $C^2$ and compactly supported.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Corollary of limiting identity](limiting-cor.md)
- [Smooth Urysohn lemma](smooth-ury.md)

## Proof

For any $R>1$, one can use a smooth cutoff function (provided by Lemma [Smooth Urysohn lemma](smooth-ury.md) to write $\psi = \psi_{\leq R} + \psi_{>R}$, where $\psi_{\leq R}$ is $C^2$ (in fact smooth) and compactly supported (on $[-R,R]$), and $\psi_{>R}$ obeys bounds of the form

$$
|\psi_{>R}(t)|, |\psi''_{>R}(t)| \ll R^{-1} / (1 + |t|^2)
$$

where the implied constants depend on $\psi$. By Lemma [Decay bounds](decay.md) we then have

$$
\hat \psi_{>R}(u) \ll R^{-1} / (1+|u|^2).
$$

Using this and [(1)](README.md) one can show that

$$
\sum_{n=1}^\infty \frac{f(n)}{n} \hat \psi_{>R}( \frac{1}{2\pi} \log \frac{n}{x} ),
A \int_{-\infty}^\infty \hat \psi_{>R} (\frac{u}{2\pi})\ du \ll R^{-1}
$$

(with implied constants also depending on $A$), while from Lemma [Corollary of limiting identity](limiting-cor.md) one has

$$
\sum_{n=1}^\infty \frac{f(n)}{n} \hat \psi_{\leq R}( \frac{1}{2\pi} \log \frac{n}{x} )
= A \int_{-\infty}^\infty \hat \psi_{\leq R} (\frac{u}{2\pi})\ du + o(1).
$$

Combining the two estimates and letting $R$ be large, we obtain the claim.

## Lean

Formalized as [`limiting_cor_schwartz`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/limiting_cor_schwartz).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
