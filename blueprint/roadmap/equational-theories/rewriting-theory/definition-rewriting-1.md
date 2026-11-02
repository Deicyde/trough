---
declaration: definition
origin: cited
---

# definition-rewriting-1

We write $a \rightarrow b$ if $a\ R\ b$ holds in $A$, and say that $a$ *rewrites to* (or *reduces to*) $b$. We further define

- $\rightarrow^+$ as the transitive closure of $R$.
- $\rightarrow^*$ as the reflexive transitive closure of $R$.
- $\leftrightarrow^*$ as the reflexive transitive and symmetric closure of $R$.

We sometimes write $b\leftarrow a$, (resp. $b\ {}^*\leftarrow a$ etc) to mean $a\rightarrow b$ (resp. $a\rightarrow^*b$ etc), and chain notations, e.g. $b_1\leftarrow a\rightarrow b_2$.

## Depends on

Its statement uses no other node of the blueprint.

## Sources

- [Equational Theories blueprint: chapter/rewriting.tex, line 6](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/rewriting.tex#L6)
