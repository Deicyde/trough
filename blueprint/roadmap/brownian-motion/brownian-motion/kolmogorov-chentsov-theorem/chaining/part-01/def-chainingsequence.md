---
declaration: definition
origin: cited
lean: chainingSeq
statement: formalized
---

# Chaining sequence

Let $(\varepsilon_n)_{n \in \mathbb{N}}$ be a sequence of positive numbers, $C_n$ a finite $\varepsilon_n$-cover of $A \subseteq E$ with $C_n \subseteq A$ and $x \in C_k$ for some $k \in \mathbb{N}$. We define the chaining sequence of $x$, denoted $(\bar{x}_i)_{i \le k}$, recursively as follows: $\bar{x}_k = x$ and for $i < k$, $\bar{x}_i = \pi(\bar{x}_{i+1}, C_i)$.

## Depends on

- [nearestPt](def-nearestpt.md)
- [$\varepsilon$-cover](../../covers-and-covering-numbers/part-01/def-iscover.md)

## Lean

Formalized as [`chainingSeq`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/chainingSeq).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 383](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L383)
