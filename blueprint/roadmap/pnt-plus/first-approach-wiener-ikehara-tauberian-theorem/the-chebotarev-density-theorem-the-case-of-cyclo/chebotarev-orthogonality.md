---
declaration: lemma
origin: cited
---

# Orthogonality for Frobenius classes

Fix $\sigma \in G$. For every prime ideal $\mathfrak{p}$ of $\mathcal{O}_K$ unramified in $L$,

$$
\sum_{\chi : G \to \mathbb{C}^\times} \chi(\sigma)^{-1}\,\chi(\varphi_{\mathfrak{p}})
\;=\;
\begin{cases}
|G| & \text{if }\varphi_{\mathfrak{p}} = \sigma,\\
0 & \text{otherwise.}
\end{cases}
$$

Equivalently, if $\sigma(\zeta_m) = \zeta_m^a$ with $\gcd(a,m)=1$, the sum equals $|G|$ precisely when $N\mathfrak{p} \equiv a \pmod{m}$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Standard character orthogonality on the finite abelian group $G$. The reformulation in terms of $N\mathfrak{p} \bmod m$ uses that $\varphi_{\mathfrak{p}}(\zeta_m) = \zeta_m^{N\mathfrak{p}}$ for the cyclotomic character.

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
