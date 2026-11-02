---
declaration: lemma
origin: cited
lean: Zeta0EqZeta
statement: formalized
proof: formalized
---

# Zeta0EqZeta

For $\Re(s)>0$, $s\ne1$, and for any $N$,

$$
\zeta_0(N,s) = \zeta(s).
$$

## Depends on

- [riemannZeta0](../part-01/riemannzeta0.md)

## Proof depends on

- [isPathConnected-aux](../part-01/ispathconnected-aux.md)
- [ZetaSum-aux2](../part-01/zetasum-aux2.md)
- [HolomorphicOn-riemannZeta0](../part-01/holomorphicon-riemannzeta0.md)

## Proof

Use Lemma [ZetaSum-aux2](../part-01/zetasum-aux2.md) and the Definition [riemannZeta0](../part-01/riemannzeta0.md).

## Lean

Formalized as [`Zeta0EqZeta`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/Zeta0EqZeta).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/ZetaBounds.lean)
