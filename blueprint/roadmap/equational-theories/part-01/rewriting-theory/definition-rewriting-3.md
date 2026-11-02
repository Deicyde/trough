---
declaration: definition
origin: cited
---

# Definition: Given a rewrite system $R$ and two rules…

Given a rewrite system $R$ and two rules $\rho_1: l_1\rightarrow r_1$ and $\rho_2: l_2\rightarrow r_2$ in $R$, we say that $(t, u)$ is a *critical pair* for $\rho_1$ and $\rho_2$ if there is some non-variable position $p$ in $l_1$ such that $l_2$ unifies with the term at that position. We denote by $\sigma$ the most general unifier thus obtained and have $t = r_1\sigma$ and $u = l_1\sigma[r_2\sigma]_p$

## Depends on

Its statement uses no other node of the blueprint.

## Sources

- [Equational Theories blueprint: chapter/rewriting.tex, line 84](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/rewriting.tex#L84)
