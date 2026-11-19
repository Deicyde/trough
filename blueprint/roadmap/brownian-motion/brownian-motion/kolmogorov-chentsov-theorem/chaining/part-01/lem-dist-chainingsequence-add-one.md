---
declaration: lemma
origin: cited
lean: edist_chainingSeq_add_one
statement: formalized
proof: formalized
---

# dist_chainingSequence_add_one

Let $(\varepsilon_n)_{n \in \mathbb{N}}$ be a sequence of positive numbers, $C_n$ a finite $\varepsilon_n$-cover of $A \subseteq E$ with $C_n \subseteq A$ and $x \in C_k$ for some $k \in \mathbb{N}$. Then for all $i < k$, $d_E(\bar{x}_i, \bar{x}_{i+1}) \le \varepsilon_i$.

## Depends on

- [Chaining sequence](def-chainingsequence.md)

## Proof depends on

- [dist_nearestPt_of_isCover](lem-dist-nearestpt-of-iscover.md)
- [chainingSequence_mem](lem-chainingsequence-mem.md)

## Proof

Apply Lemma [dist_nearestPt_of_isCover](lem-dist-nearestpt-of-iscover.md) with $S = C_i$ and $x = \bar{x}_{i+1}$.

## Lean

Formalized as [`edist_chainingSeq_add_one`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/edist_chainingSeq_add_one).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 405](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L405)
