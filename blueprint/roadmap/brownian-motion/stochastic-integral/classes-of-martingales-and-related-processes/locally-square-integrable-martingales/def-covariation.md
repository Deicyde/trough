---
declaration: definition
origin: cited
lean: ProbabilityTheory.predQuadCovariation
statement: formalized
---

# Predictable covariation

For $M, N \in \mathcal{M}^2_{\mathrm{loc}}$, the predictable covariation $\langle M, N \rangle$ is a stochastic process defined by polarization of the predictable quadratic variation:

$$
\begin{aligned}
\langle M, N \rangle_t = \frac{1}{2}\left(\langle M+N \rangle_t - \langle M \rangle_t - \langle N \rangle_t \right)
\: .
\end{aligned}
$$

## Depends on

- [Locally square-integrable martingales](def-islocallysquareintegrable.md)
- [Predictable quadratic variation](def-quadraticvariation.md)

## Lean

Formalized as [`ProbabilityTheory.predQuadCovariation`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.predQuadCovariation).

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 918](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L918)
