---
declaration: lemma
origin: cited
mathlib: true
mathlib_declaration: MeasureTheory.UniformIntegrable.uniformIntegrable_of_ae_tendsto
---

# uniformIntegrable_of_tendsto_ae

Let $(X_t)_{t \in T}$ be a family of $p$-uniformly integrable stochastic processes. Then the family of limits in almost everywhere convergence of sequences of $X$ is $p$-uniformly integrable.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

Let $\epsilon > 0$. There exists $\delta > 0$ such that for all $t\in T$ and all measurable set $S$ such that $P(S)\lt \delta$,

$$
P[\|X_t\|^p\mathbb{I}_S]^{1/p}\le \varepsilon.
$$

Let $(t_n)_{n \in \mathbb{N}}$ be a sequence in $T$ such that $X_{t_n}$ converges almost everywhere to $Y$. We have by Fatou's lemma that

$$
P[\|Y\|^p \mathbb{I}_{S}]^{1/p} = P[\liminf_{n \to \infty} \|X_{t_{n}}\|^p \mathbb{I}_{S}]^{1/p} \le \liminf_{n \to \infty} P[\|X_{t_{n}}\|^p \mathbb{I}_{S}]^{1/p} \le \epsilon.
$$

This proves that the family of limits in a.e convergence of sequences of $X$ is $p$-uniformly integrable in the measure theory sense. One can prove uniform boundedness of this family by using Fatou's lemma in a similar way.

## Lean

Formalized as [`MeasureTheory.UniformIntegrable.uniformIntegrable_of_ae_tendsto`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.UniformIntegrable.uniformIntegrable_of_ae_tendsto).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 885](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L885)
