---
declaration: corollary
origin: cited
lean: edist_chainingSeq_pow_two_le
statement: formalized
proof: formalized
---

# dist_chainingSequence_pow_two_le

For $\varepsilon_n = \varepsilon_0 2^{-n}$, with the hypothesis of Lemma [dist_chainingSequence_le](lem-dist-chainingsequence-le.md), we have

$$
\begin{aligned}
d_E(\bar{x}_m, \bar{y}_m)
&\le d_E(x, y) + \varepsilon_0 2^{-m+2}
\: .
\end{aligned}
$$

## Depends on

- [Chaining sequence](def-chainingsequence.md)

## Proof depends on

- [dist_chainingSequence_le](lem-dist-chainingsequence-le.md)

## Lean

Formalized as [`edist_chainingSeq_pow_two_le`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/edist_chainingSeq_pow_two_le).

## Sources

- [Brownian motion blueprint: chapters/kolmogorov_chentsov.tex, line 458](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/kolmogorov_chentsov.tex#L458)
