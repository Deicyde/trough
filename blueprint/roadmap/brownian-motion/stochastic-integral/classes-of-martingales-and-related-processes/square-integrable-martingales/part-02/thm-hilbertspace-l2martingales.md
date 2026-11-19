---
declaration: theorem
origin: cited
lean: ProbabilityTheory.instCompleteSpaceSquareIntegrable
statement: formalized
---

# hilbertSpace_L2Martingales

If $T$ is separable then the space $\mathcal{M}^2$ is a Hilbert space.

## Depends on

- [L2Martingales.inner](def-l2martingales-inner.md)
- [L2Martingales.norm_eq_zero](lem-l2martingales-norm-eq-zero.md)

## Proof depends on

- [L2Martingales.module](../part-01/lem-l2martingales-module.md)

## Proof

We show that the map

$$
\begin{aligned}
\phi : \mathcal{M}^2 & \to \left\{f \in L^2(E, P) | f \text{ is } \left(\bigsqcup_t, \mathcal{F}_t\right)\text{-strongly measurable}\right\} \\
M & \mapsto M_\infty
\end{aligned}
$$

is a bijective isometry. It is an isometry by Definition [L2Martingales.norm](def-l2martingales-norm.md). We define the inverse $\psi$ as the map which to $f$ associates a càdlàg martingale that is a modification of $t \mapsto P[f | \mathcal{F}_t]$, given by Lemma [exists_cadlag_mod_of_local_mg](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/cadlag.tex#L519).

Let $M$ be a square integrable martingale. Then for any $t$, $M_t$ is a.e. equal to $P[M_\infty | \mathcal{F}_t]$ by Lemma [condExp_limitProcess](../part-01/lem-condexp-limitprocess.md), thus $M$ is a càdlàg modification of $t \mapsto P[f | \mathcal{F}_t]$, thus it is indistinguishable from $\psi(M_\infty)$.

Let $f \in L^2(E, P)$ be a.e. strongly measurable with respect to $\bigsqcup_t \mathcal{F}_t$. Then by Lemma [tendsto_ae_condExp](../part-01/lem-tendsto-ae-condexp.md) we know that almost surely $P[f | \mathcal{F}_t]$ converges to $f$. Because $T$ is separable we can consider $(t_n)$ a sequence of points that tends to infinity. Because $\psi(f)$ and $P[f | \mathcal{F}_t]$ are modifications of each other, we have that almost surely, for all $n \in \mathcal{N}$, $\psi(f)_{t_n} = P[f | \mathcal{F}_{t_n}]$. But we also know that $\psi(f)_{t_n}$ converges to $\psi(f)_\infty$ so we conclude that $\psi(f)_\infty$ is a.e. equal to f.

## Lean

Stated as [`ProbabilityTheory.instCompleteSpaceSquareIntegrable`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/ProbabilityTheory.instCompleteSpaceSquareIntegrable); the blueprint marks no proof of it as formalized.

## Sources

- [Brownian motion blueprint: chapters/martingale_classes.tex, line 502](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/martingale_classes.tex#L502)
