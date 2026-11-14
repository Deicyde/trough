# Kolmogorov-Chentsov Theorem

We follow the proof of the Kolmogorov-Chentsov theorem from (kratschmer2023kolmogorov). That proof notably uses the chaining technique developed by Talagrand (talagrand2022upper).

That theorem is about stochastic processes $X : T \to \Omega \to E$, where $\Omega$ is a measurable space with a probability measure $\mathbb{P}$, the index set $T$ is a metric space with distance $d_T$, and $E$ is also a metric space with distance $d_E$, on which we put the Borel $\sigma$-algebra.

The main result is Theorem [countable_set_bound](kolmogorov-chentsov-theorem/thm-countable-set-bound.md). Under an assumption on the covering number of $T$, for a process $X$ that satisfies the Kolmogorov condition $\mathbb{E}[d_E(X_s, X_t)^p] \le M d_T(s, t)^q$ (see Definition [Kolmogorov condition](chaining-for-stochastic-processes-under-kolmogor/part-01/def-iskolmogorovprocess.md)),the theorem gives a finite bound on the expectation of the supremum of the ratio

$$
\begin{aligned}
\mathbb{E}\left[ \sup_{s, t \in T'} \frac{d_E(X_s, X_t)^p}{d_T(s, t)^{\beta p}} \right]
\: ,
\end{aligned}
$$

for $T'$ a countable subset of $T$. As a corollary, we obtain that there exists a modification of $X$ with Hölder continuous paths.

In Lean, we will use the typeclass `PseudoEMetricSpace` for both $T$ and $E$ as long as possible, and then specialize to `EMetricSpace` (or perhaps even `MetricSpace`) when we need the stronger properties of a metric space. For example, to prove the existence of a modification of a stochastic process, we will eventually use the fact that $d_E(x, y) = 0$ implies $x = y$, which does not hold in a pseudo-metric space. All distances will be expressed with `edist`, which takes values in `ENNReal`, and the integrals refer to Lebesgue integrals.

- [Covers and covering numbers](covers-and-covering-numbers/README.md)
- [Chaining](chaining/README.md)
- [Chaining for stochastic processes under Kolmogorov conditions](chaining-for-stochastic-processes-under-kolmogor/README.md)
- [Kolmogorov-Chentsov Theorem](kolmogorov-chentsov-theorem/README.md)
