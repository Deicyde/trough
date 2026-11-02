---
declaration: lemma
origin: cited
---

# Dedekind-nonvanishing

For any nontrivial character $\chi$ of $G = \mathrm{Gal}(L/K)$, one has $L(\chi,1) \neq 0$. Moreover $L(\chi,s)$ does not vanish for $\Re(s)=1$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof depends on

- [Dedekind-factor](dedekind-factor.md)
- [Simple pole](dedekind-pole.md)
- [Continuation of nontrivial Artin $L$-functions](artin-l-continuation.md)

## Proof

For the value at $s=1$: write $\log\zeta_L(t) = \sum_\chi \log L(\chi,t)$ for real $t>1$. As $t\to 1^+$, the left side is $\sim \log(t-1)^{-1}$ by Lemma [Simple pole](dedekind-pole.md). If some nontrivial $L(\chi,\cdot)$ had a zero of order $m_\chi \geq 1$ at $s=1$, the right side would behave like $\bigl(1 - \sum_\chi m_\chi\bigr)\log(t-1)^{-1}$ up to a bounded error (the trivial character contributes the pole of $\zeta_K$, absorbed into the factorisation), forcing $1-\sum m_\chi \leq 0$, a contradiction. Hence $L(\chi,1)\neq 0$ for all nontrivial $\chi$ (Sharifi, Proposition 7.1.19).

For the rest of the line $\Re(s)=1$, $s\neq 1$: adapt the classical nonvanishing argument for Dirichlet $L$-functions (comparison of $\zeta_L(s)$, $\zeta_L(s)^3\,|L(\chi,s)|^4$, or the $3+4\operatorname{Re}$ inequality) using the Euler product of Lemma [Artin $L$-function as Euler product](artin-l-euler.md) and the absence of poles of nontrivial $L(\chi,\cdot)$ on $\Re(s)=1$ from Lemma [Continuation of nontrivial Artin $L$-functions](artin-l-continuation.md).

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
