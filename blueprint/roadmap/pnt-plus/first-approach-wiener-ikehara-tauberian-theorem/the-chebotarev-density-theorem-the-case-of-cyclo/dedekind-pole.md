---
declaration: lemma
origin: cited
---

# Simple pole

The Dedekind zeta function $\zeta_L$ admits a meromorphic continuation to a neighbourhood of the line $\Re(s)=1$ with a single simple pole at $s=1$ (and is otherwise holomorphic and nonvanishing on that line after removing the pole). In particular $\log \zeta_L(s) \sim \log(s-1)^{-1}$ as $s \to 1^+$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

This is the standard analytic continuation of Dedekind zeta (Theorem 7.1.12 of <https://www.math.ucla.edu/~sharifi/algnum.pdf>): absolute convergence of the ideal Dirichlet series and Euler product for $\Re(s)>1$, meromorphic continuation across $\Re(s)>1-[L:\mathbb{Q}]^{-1}$, and a simple pole at $s=1$. The logarithmic asymptotic is immediate from the simple pole.

## Sources

- [PNT+ blueprint: PrimeNumberTheoremAnd/Wiener.lean](https://github.com/AlexKontorovich/PrimeNumberTheoremAnd/blob/127b50e33f6033e2147921167a117af96d9ba4ea/PrimeNumberTheoremAnd/Wiener.lean)
