---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.UniformIntegrable.memLp_of_tendstoInMeasure
---

# memLp_of_tendstoInMeasure

Let $(X_n)_{n \in \mathbb{N}}$ be a sequence of $p$-uniformly integrable stochastic processes and suppose $X_n \to X$ in probability as $n \to \infty$. Then, $X$ is $L^p$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Since $X_n \to X$ in probability, it has a subsequence $(X_{n_k}) \subseteq (X_n)$ which converges to $X$ almost surely. Thus, we have by Fatou's lemma that

$$
P[|X|^p] = P[\liminf_{k \to \infty} |X_{n_k}|^p] \le \liminf_{k \to \infty} P[|X_{n_k}|^p] < \infty
$$

where the last inequality follows as uniform integrability implies that $(X_n)$ is uniform bounded in $L^p$.

## Lean

Formalized as [`MeasureTheory.UniformIntegrable.memLp_of_tendstoInMeasure`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.UniformIntegrable.memLp_of_tendstoInMeasure).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 870](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L870)
