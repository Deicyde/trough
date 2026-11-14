---
declaration: lemma
origin: cited
lean: MeasureTheory.StronglyAdapted.isStronglyProgressive_of_rightContinuous
statement: formalized
proof: formalized
---

# Adapted.isStronglyProgressive_of_rightContinuous

Suppose $T$ is a linearly ordered set equipped with the order topology. If $T$ is second countable and a stochastic process $(X_t)_{t \in T}$ is right continuous and adapted, then it is progressively measurable.

## Depends on

- [adapted](def-adapted.md)
- [Progressively measurable](def-isstronglyprogressive.md)
- [Right continuous function](def-rightcontinuous.md)

## Proof

Fixing $t \in T$, let $S$ be a union of a dense set of $(-\infty,t]$ and the set of points isolated from right in $(-\infty,t]$. As $T$ is second countable, $S$ can be chosen so that it is countable, which means that there exists a surjective function $u: \mathbb{N} \rightarrow S$. We need to show that $X$ restricted to $(-\infty, t] \times \Omega$ is measurable with respect to $\mathcal{B}((-\infty, t]) \otimes \mathcal{F}_t$. To this end, we rearrange the image of the first $n$ numbers under the map $u$ in nondecreasing order, denoted by $v_0\le v_1\le \cdots\le v_n$, and define a left continuous discrete approximation of $X$ on $(-\infty, t]$ by

$$
X^n_s = \begin{cases}
X_{v_0} & \text{if } s \le v_0 \\
X_{v_i} & \text{if } s \in (- v_{i-1}, v_i]
\end{cases}
$$

As $X$ is right continuous, it is easy to see that $X^n \to X$ pointwise as $n \to \infty$. Thus, as each $X^n$ is measurable, it follows that $X$ is also measurable (by using `stronglyMeasurable_of_tendsto`).

## Lean

Formalized as [`MeasureTheory.StronglyAdapted.isStronglyProgressive_of_rightContinuous`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.StronglyAdapted.isStronglyProgressive_of_rightContinuous).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 46](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L46)
