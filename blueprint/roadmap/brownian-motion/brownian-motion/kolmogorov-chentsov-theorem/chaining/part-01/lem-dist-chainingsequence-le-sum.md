---
declaration: lemma
origin: cited
lean: edist_chainingSeq_le_sum
statement: formalized
proof: formalized
---

# dist_chainingSequence_le_sum

Let $(\varepsilon_n)_{n \in \mathbb{N}}$ be a sequence of positive numbers, $C_n$ a finite $\varepsilon_n$-cover of $A \subseteq E$ with $C_n \subseteq A$ and $x \in C_k$ for some $k \in \mathbb{N}$. Then for $m \le k$, $d_E(\bar{x}_m, x) \le \sum_{i=m}^{k-1} \varepsilon_i$.

## Depends on

- [Chaining sequence](def-chainingsequence.md)

## Proof depends on

- [dist_chainingSequence_add_one](lem-dist-chainingsequence-add-one.md)

## Proof

By the triangle inequality and Lemma [dist_chainingSequence_add_one](lem-dist-chainingsequence-add-one.md),

$$
\begin{aligned}
d_E(\bar{x}_m, x)
\le \sum_{i=m}^{k-1} d_E(\bar{x}_i, \bar{x}_{i+1})
\le \sum_{i=m}^{k-1} \varepsilon_i
\: .
\end{aligned}
$$

## Lean

Formalized as [`edist_chainingSeq_le_sum`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/edist_chainingSeq_le_sum).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 419](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L419)
