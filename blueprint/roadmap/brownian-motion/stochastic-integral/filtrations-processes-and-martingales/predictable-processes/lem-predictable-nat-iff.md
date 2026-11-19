---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.IsStronglyPredictable.iff_measurable_add_one
---

# predictable_nat_iff

Let $X : \mathbb{N} \to \Omega \to E$ be a stochastic process and let $\mathcal{F}$ be a filtration indexed by $\mathbb{N}$. Then $X$ is predictable if and only if $X_0$ is $\mathcal{F}_0$-measurable and for all $n \in \mathbb{N}$, $X_{n+1}$ is $\mathcal{F}_n$-measurable.

## Depends on

- [Predictable process](def-predictable.md)

## Proof depends on

- [predictable_Ioc_prod](lem-predictable-ioc-prod.md)

## Proof

Suppose first that $X$ is predictable. Straightaway, $X_0$ is $\mathcal{F}_0$-measurable as predictable implies progressively measurable which in turn implies adapted.

Fixing $n$, we observe that for any $S \in \mathcal{B}(E)$,

$$
X_{n + 1}^{-1}(S) = \{\omega \mid (n + 1, \omega) \in X^{-1}(S)\} = \pi^{-1}(\iota^{-1}(X^{-1}(S)))
$$

where

$$
\pi : \Omega \to \{n + 1\} \times \Omega : \omega \mapsto (n + 1, \omega)
$$

and

$$
\iota : \{n + 1\} \times \Omega \to T \times \Omega : (n + 1, \omega) \mapsto (n + 1, \omega).
$$

As $X^{-1}(S) \in \Sigma_{\mathcal{F}}$ – the predictable $\sigma$-algebra, it suffices to show that $\pi^{-1}(\iota^{-1}(\Sigma_{\mathcal{F}})) \in \mathcal{F}_n$. To this end, we again only need to show these for the generating sets of $\Sigma_{\mathcal{F}}$:

- For $A \in \mathcal{F}_0$, measurability is clear as $\iota^{-1}(\{0\} \times A) = \varnothing$.
- Similarly, for $m > n$ and $A \in \mathcal{F}_m$, $\iota^{-1}((m, \infty) \times A) = \varnothing$.
- For $m \le n$ and $A \in \mathcal{F}_m \le \mathcal{F}_n$ we have that $\pi^{-1}(\iota^{-1}((m, \infty) \times A)) = A$ which is $\mathcal{F}_n$ measurable by the monotonicity of the filtration.

Now, supposing $X_0$ is $\mathcal{F}_0$-measurable and $X_{n + 1}$ is $\mathcal{F}_n$-measurable, we will show that $X$ is predictable. Indeed, fixing $S \in \mathcal{B}(E)$, we have

$$
X^{-1}(S) = \bigcup_{n \in \mathbb{N}} \{n\} \times X_n^{-1}(S) = {0} \times X_0^{-1}(S) \cup \bigcup_{n \in \mathbb{N}} \{n + 1\} \times X_{n + 1}^{-1}(S).
$$

Thus, as $\{0\} \times X_0^{-1}(S) \in \Sigma_{\mathcal{F}}$ by construction and $\{n + 1\} \times X_{n + 1}^{-1}(S) = (n, n + 1] \times X_{n + 1}^{-1}(S) \in \Sigma_{\mathcal{F}}$ by Lemma [predictable_Ioc_prod](lem-predictable-ioc-prod.md) and the fact that $X_{n + 1}^{-1}(S) \in \mathcal{F}_n$, we have that $X^{-1}(S) \in \Sigma_{\mathcal{F}}$ as required.

## Lean

Formalized as [`MeasureTheory.IsStronglyPredictable.iff_measurable_add_one`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.IsStronglyPredictable.iff_measurable_add_one).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 668](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L668)
