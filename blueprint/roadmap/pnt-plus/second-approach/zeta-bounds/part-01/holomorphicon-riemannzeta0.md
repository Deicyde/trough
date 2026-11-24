---
declaration: theorem
origin: cited
lean: HolomorphicOn_riemannZeta0
statement: formalized
proof: formalized
---

# HolomorphicOn-riemannZeta0

For any $N\ge1$, the function $\zeta_0(N,s)$ is holomorphic on $\{s\in \mathbb{C}\mid \Re(s)>0 ∧ s \ne 1\}$.

## Depends on

- [riemannZeta0](riemannzeta0.md)

## Proof

The function $\zeta_0(N,s)$ is a finite sum of entire functions, plus an integral that's absolutely convergent on $\{s\in \mathbb{C}\mid \Re(s)>0 ∧ s \ne 1\}$ by Lemma [ZetaBnd-aux1b](zetabnd-aux1b.md).

## Lean

Formalized as [`HolomorphicOn_riemannZeta0`](https://AlexKontorovich.github.io/PrimeNumberTheoremAnd/docs/find/#doc/HolomorphicOn_riemannZeta0).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/ZetaBounds.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/b47896b36cc6e36559189281330930ecf25fae7a/PrimeNumberTheoremAnd/ZetaBounds.lean)
