---
declaration: lemma
origin: cited
lean: ZetaDerivUpperBnd
statement: formalized
proof: formalized
---

# ZetaDerivUpperBnd

For any $s = \sigma + tI \in \mathbb{C}$, $1/2 \le \sigma\le 2, 3 < |t|$, there is an $A>0$ so that for $1-A/\log t \le \sigma$, we have

$$
|\zeta'(s)| \ll \log^2 t.
$$

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [ZetaBnd-aux2](zetabnd-aux2.md)
- [ZetaUpperBnd](zetaupperbnd.md)
- [DerivUpperBnd-aux7](derivupperbnd-aux7.md)
- [riemannZeta0](../part-01/riemannzeta0.md)
- [ZetaBnd-aux1](../part-01/zetabnd-aux1.md)
- [Zeta0EqZeta](zeta0eqzeta.md)

## Proof

First replace $\zeta(s)$ by $\zeta_0(N,s)$ for $N = \lfloor |t| \rfloor$. Differentiating term by term, we get:

$$
\zeta'(s) = -\sum_{1\le n < N} n^{-s} \log n
+ \frac{N^{1 - s}}{(1 - s)^2} + \frac{N^{1 - s} \log N} {1 - s}
+ \frac{N^{-s}\log N}{2} +
\int_N^\infty \frac{\lfloor x\rfloor + 1/2 - x}{x^{s+1}} \, dx
-s \int_N^\infty \log x \frac{\lfloor x\rfloor + 1/2 - x}{x^{s+1}} \, dx
.
$$

Estimate as before, with an extra factor of $\log |t|$.

## Lean

Formalized as [`ZetaDerivUpperBnd`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/ZetaDerivUpperBnd).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaBounds.lean)
