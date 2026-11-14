---
declaration: lemma
origin: cited
lean: ProbabilityTheory.exists_subsequence_ae_tendsto_uniformly
statement: formalized
proof: formalized
---

# exists_subsequence_ae_tendsto_uniformly

Let $(M^{(n)})$ be a sequence of square integrable martingales and $N$ be a square integrable martingale such that $\|M^{(n)}_\infty - N_\infty\|_2 \longrightarrow_{n \to +\infty} 0$. Then there exists $\phi : \mathbb{N} \to \mathbb{N}$ increasing such that, almost surely, $M^{(\phi(n))}_\cdot(\omega)$ converges uniformly to $N_\cdot(\omega)$ as $n$ goes to infinity.

## Depends on

- [Square integrable martingales](../part-01/def-issquareintegrable.md)

## Proof depends on

- [IsSquareIntegrable.integral_iSup_norm_rpow_rpow_inv_le_limitProcess](../part-01/lem-issquareintegrable-integral-isup-norm-rpow-r.md)

## Proof

We can find $\phi$ increasing such that $\|M^{(\phi(n))}_\infty - N_\infty\|_2 \le 1/2^n$. Then,

$$
\begin{aligned}
P[\sum_n \sup_t \|M^{(\phi(n))}_t -  N_t\|] & = \sum_n P[\sup_t \|M^{(\phi(n))}_t -  N_t\|] \\
& \le \sqrt{P(\Omega)} \sum_n P[(\sup_t \|M^{(\phi(n))}_t -  N_t\|)^2]^{1/2} \\
& \le 2 \sqrt{P(\Omega)} \|M^{(\phi(n))}_\infty - N_\infty\|_2 < \infty,
\end{aligned}
$$

Where the second inequality is Lemma [IsSquareIntegrable.integral_iSup_norm_rpow_rpow_inv_le_limitProcess](../part-01/lem-issquareintegrable-integral-isup-norm-rpow-r.md). In particular, almost surely, $\sum_n \sup_t \|M^{(\phi(n))}_t - N_t\| < \infty$ and thus $\sup_t \|M^{(\phi(n))}_t - N_t\| \longrightarrow_{n \to +\infty} 0$, which concludes the proof.

## Lean

Formalized as [`ProbabilityTheory.exists_subsequence_ae_tendsto_uniformly`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.exists_subsequence_ae_tendsto_uniformly).

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 588](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L588)
