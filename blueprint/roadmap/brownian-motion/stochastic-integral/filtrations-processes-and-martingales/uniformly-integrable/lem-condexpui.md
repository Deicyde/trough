---
declaration: lemma
origin: cited
lean: MeasureTheory.UniformIntegrable.condExp'
statement: formalized
proof: formalized
---

# condExpUI

If $(X_i)_{i \in \iota}$ is a family of (probabilistically) uniformly integrable functions and $(\mathcal{F}_j)_{j \in \kappa}$ is a family of $\sigma$-algebras, then the family $(P[X_i \mid \mathcal{F}_j])_{i \in \iota, j \in \kappa}$ is uniformly integrable.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Since $(X_i)_{i \in \iota}$ is uniformly integrable, it is uniformly bounded in $L^1$, thus so is $(P[X_i \mid \mathcal{F}_j])_{i \in \iota, j \in \kappa}$. Moreover, for any $\epsilon > 0$, there exists some $\delta > 0$ such that for any measurable set $A$ with $P(A) < \delta$, we have that $\sup_{i \in \iota} P[|X_i| \mathbb{I}_A] < \epsilon$.

On the other hand, by Markov's inequality, for any $\lambda > 0$, $i \in \iota$ and $j \in \kappa$ we have that

$$
P(|P[X_i \mid \mathcal{F}_j]| \ge \lambda) \le \lambda^{-1}P[|P[X_i \mid \mathcal{F}_j]|] \le \lambda^{-1}P[|X_i|].
$$

Now set $\lambda := \delta^{-1} \sup_{i \in \iota} P[|X_i|] + 1$. Then for any $i \in \iota$ and $j \in \kappa$ we have that

$$
P(|P[X_i \mid \mathcal{F}_j]| \ge \lambda) \le \frac{P[|X_i|]}{\delta^{-1} \sup_{k \in \iota} P[|X_k|] + 1} < \delta,
$$

and so,

$$
\begin{aligned}
P[|P[X_i \mid \mathcal{F}_j]| \mathbb{I}_{|P[X_i \mid \mathcal{F}_i]| \ge \lambda}]
& = P[|P[X_i \mid \mathcal{F}_j] \mathbb{I}_{|P[X_i \mid \mathcal{F}_i]| \ge \lambda}|] \\
& = P[|P[X_i \mathbb{I}_{|P[X_i \mid \mathcal{F}_i]| \ge \lambda} \mid \mathcal{F}_j]|] \\
& \le P[P[|X_i|\mathbb{I}_{|P[X_i \mid \mathcal{F}_j]| \ge \lambda} \mid \mathcal{F}_j]] \\
& = P[|X_i|\mathbb{I}_{|P[X_i \mid \mathcal{F}_j]| \ge \lambda}] < \epsilon,
\end{aligned}
$$

showing that $(P[X_i \mid \mathcal{F}_j])_{i \in \iota, j \in \kappa}$ is uniformly integrable.

## Lean

Formalized as [`MeasureTheory.UniformIntegrable.condExp'`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.UniformIntegrable.condExp').

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 713](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L713)
