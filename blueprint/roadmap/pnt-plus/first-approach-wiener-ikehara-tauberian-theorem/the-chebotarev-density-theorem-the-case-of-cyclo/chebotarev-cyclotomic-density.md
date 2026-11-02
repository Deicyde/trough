---
declaration: proposition
origin: cited
---

# Cyclotomic Chebotarev density

For every $\sigma \in G$, the set of prime ideals $\mathfrak{p}$ of $K$ unramified in $L$ with Frobenius $\varphi_{\mathfrak{p}} = \sigma$ has Dirichlet density $1/|G|$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Dedekind-factor](dedekind-factor.md)
- [Simple pole](dedekind-pole.md)
- [Dedekind-nonvanishing](dedekind-nonvanishing.md)
- [Artin $L$-function as Euler product](artin-l-euler.md)
- [Orthogonality for Frobenius classes](chebotarev-orthogonality.md)

## Proof

This is Proposition 7.2.1 of <https://www.math.ucla.edu/~sharifi/algnum.pdf>. For $\Re(s)>1$ one has $\log L(\chi,s) \sim \sum_{\mathfrak{p}} \chi(\mathfrak{p})\, N\mathfrak{p}^{-s}$. Summing against $\chi(\sigma)^{-1}$ and applying Lemma [Orthogonality for Frobenius classes](chebotarev-orthogonality.md) yields

$$
\sum_{\chi} \chi(\sigma)^{-1} \log L(\chi,s)
\;\sim\;
|G| \sum_{\varphi_{\mathfrak{p}}=\sigma} N\mathfrak{p}^{-s}.
$$

On the other hand, by Lemmas [Dedekind-factor](dedekind-factor.md) and [Dedekind-nonvanishing](dedekind-nonvanishing.md) the left side is $\sim \log\zeta_K(s) \sim \log(s-1)^{-1}$ as $s\to 1^+$ (only the trivial character contributes a pole). Comparing the two asymptotics gives the asserted Dirichlet density.

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
