---
declaration: lemma
origin: cited
lean: ZetaUpperBnd
statement: formalized
proof: formalized
---

# ZetaUpperBnd

For any $s = \sigma + tI \in \mathbb{C}$, $1/2 \le \sigma\le 2, 3 < |t|$ and any $0 < A < 1$ sufficiently small, and $1-A/\log |t| \le \sigma$, we have

$$
|\zeta(s)| \ll \log t.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [ZetaBnd-aux2](zetabnd-aux2.md)
- [riemannZeta0](../part-01/riemannzeta0.md)
- [ZetaBnd-aux1](../part-01/zetabnd-aux1.md)
- [Zeta0EqZeta](zeta0eqzeta.md)

## Proof

First replace $\zeta(s)$ by $\zeta_0(N,s)$ for $N = \lfloor |t| \rfloor$. We estimate:

$$
|\zeta_0(N,s)| \ll
\sum_{1\le n \le |t|} |n^{-s}|
+
\frac{- |t|^{1-\sigma}}{|1-s|} + \frac{-|t|^{-\sigma}}{2} +
|t| \cdot |t| ^ {-σ} / σ
$$

$$
\ll
e^A \sum_{1\le n < |t|} n^{-1}
+|t|^{1-\sigma},
$$

where we used Lemma [ZetaBnd-aux2](zetabnd-aux2.md) and Lemma [ZetaBnd-aux1](../part-01/zetabnd-aux1.md). The first term is $\ll \log |t|$. For the second term, estimate

$$
|t|^{1-\sigma}
\le |t|^{1-(1-A/\log |t|)}
= |t|^{A/\log |t|} \ll 1.
$$

## Lean

Formalized as [`ZetaUpperBnd`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZetaUpperBnd).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaBounds.lean)
