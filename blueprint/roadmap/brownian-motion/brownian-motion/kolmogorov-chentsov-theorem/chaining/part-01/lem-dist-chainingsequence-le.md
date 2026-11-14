---
declaration: lemma
origin: cited
lean: edist_chainingSeq_le
statement: formalized
proof: formalized
---

# dist_chainingSequence_le

Let $(\varepsilon_n)_{n \in \mathbb{N}}$ be a sequence of positive numbers, $C_n$ a finite $\varepsilon_n$-cover of $A \subseteq E$ with $C_n \subseteq A$. Let $m, k, \ell \in \mathbb{N}$ with $m \le k$ and $m \le \ell$ and let $x \in C_k$ and $y \in C_\ell$. Then

$$
\begin{aligned}
d_E(\bar{x}_m, \bar{y}_m)
&\le d_E(x, y) + \sum_{i=m}^{k-1} \varepsilon_i + \sum_{j=m}^{\ell-1} \varepsilon_j
\end{aligned}
$$

## Depends on

- [Chaining sequence](def-chainingsequence.md)

## Proof depends on

- [dist_chainingSequence_le_sum](lem-dist-chainingsequence-le-sum.md)

## Proof

Triangle inequality and Lemma [dist_chainingSequence_le_sum](lem-dist-chainingsequence-le-sum.md).

## Lean

Formalized as [`edist_chainingSeq_le`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/edist_chainingSeq_le).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 439](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L439)
