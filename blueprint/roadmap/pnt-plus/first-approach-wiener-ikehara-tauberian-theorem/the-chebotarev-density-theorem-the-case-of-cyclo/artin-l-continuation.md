---
declaration: lemma
origin: cited
---

# Continuation of nontrivial Artin $L$-functions

Let $\chi : G \to \mathbb{C}^\times$ be a nontrivial character. Then $L(\chi,s)$ extends to an analytic function on the half-plane $\Re(s) > 1 - [K:\mathbb{Q}]^{-1}$, and in particular is holomorphic at $s=1$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Following Proposition 7.1.19 of <https://www.math.ucla.edu/~sharifi/algnum.pdf>: let $n$ be the order of $\chi$. Geometry of numbers supplies the estimate that, for each $n$th root of unity $\zeta$, the number of ideals $\mathfrak{a}$ with $N\mathfrak{a} \leq N$ and $\chi(\mathfrak{a})=\zeta$ is $CN + O\bigl(N^{1-[K:\mathbb{Q}]^{-1}}\bigr)$ with $C$ independent of $\zeta$. Summing against $\zeta$ cancels the main terms, so $\sum_{N\mathfrak{a}\leq N} \chi(\mathfrak{a}) = O\bigl(N^{1-[K:\mathbb{Q}]^{-1}}\bigr)$. Lemma 7.1.5 of Sharifi then yields absolute uniform convergence of $\sum_{\mathfrak{a}} \chi(\mathfrak{a})\, N\mathfrak{a}^{-s}$ on compact subsets of $\Re(s) > 1 - [K:\mathbb{Q}]^{-1}$.

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
