---
declaration: definition
origin: cited
---

# Confluent theory

Let $\Gamma$ be a theory. A word $w$ can be *reduced* to another $w'$ if one can get from $w$ to $w'$ by a series of substitutions of laws in $\Gamma$, where no substitution increases the length of the word **this is a working definition, might not be the best one to keep.**. A theory $\Gamma$ is *confluent* if whenever a word $w$ can be reduced to both $w'$ and $w''$, then both $w'$ and $w''$ can be reduced further to a common reduction $\tilde w$. As such, each word $w \in M_X$ should have a *unique simplification* to a reduced word $w_\Gamma$ in some normal form, for instance the shortest reduction that is minimal with respect to some suitable ordering such as lexicographical ordering.

## Depends on

- [Free Magma](../../basic-theory-of-magmas/free-magma-def.md)

## Sources

- [Equational Theories blueprint: chapter/abstract_nonsense.tex, line 100](https://github.com/teorth/equational_theories/blob/2ddb16c4c4c036242ad3e18167579b57cac2a006/blueprint/src/chapter/abstract_nonsense.tex#L100)
