---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: isBounded_image_of_isCadlag_of_isCompact
---

# isBounded_image_of_isCadlag_of_isCompact

Assume $T$ is a linear order endowed with a topology making it first countable and $E$ is a pseudo-metric space. If $X$ is a càdlàg process then it maps compact sets of $T$ to bounded sets.

## Depends on

- [Cadlag function](../../../filtrations-processes-and-martingales/basic-definitions/part-01/def-iscadlag.md)

## Proof

Let $K \subseteq T$ be a compact set and $\omega \in \Omega$. Assume that $X(\omega)(K)$ is not bounded. Then there exists a sequence $(t_n)$ in $K$ such that for all $n \in N$, $d(X_{t_n}(\omega), x) \ge n$, for some arbitrary $x \in E$. Because $K$ is compact, there is a subsequence $(t_{\phi(n)})$ that converges. Then one can extract a subsequence $(t_{\phi(\psi(n))})$ which either converges from below or from above. In both cases the sequence $(X_{t_{\phi(\psi(n))}})$ will converge, contradicting the hypotheses.

## Lean

Formalized as [`isBounded_image_of_isCadlag_of_isCompact`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/isBounded_image_of_isCadlag_of_isCompact).

## Sources

- [Brownian motion blueprint: chapters/local_martingales.tex, line 716](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/local_martingales.tex#L716)
