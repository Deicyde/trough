---
declaration: lemma
origin: cited
lean: MeasureTheory.uniformIntegrable_of_eLpNorm_le
statement: formalized
proof: formalized
---

# uniformIntegrable_of_bounded

Let $(X_i)_{i \in \iota}$ be a family of random variables that is bounded in $\mathrm L^p$, for $p > q \ge 1$. Then $(X_i)_{i \in \iota}$ is uniformly integrable in $\mathrm L^q$.

## Depends on

Its statement uses no other node of the blueprint.

## Proof

For any measurable set $s$ we have by Hölder inequality that

$$
\|X_t \mathbb{I}_s\|_q \le \|X_t\|_p P(s)^{1/q - 1/p},
$$

which goes to $0$ as $P(s)$ goes to zero. Moreover,

$$
\|X_t\|_q \le P(\Omega)^{1/q - 1/p} \|X_t\|_p,
$$

so $(X_i)_{i \in \iota}$ is bounded in $\mathrm L^q$.

## Lean

Formalized as [`MeasureTheory.uniformIntegrable_of_eLpNorm_le`](https://RemyDegenne.github.io/brownian-motion/docs/find/#doc/MeasureTheory.uniformIntegrable_of_eLpNorm_le).

## Sources

- [Brownian motion blueprint: chapters/filtration_martingale.tex, line 741](https://github.com/RemyDegenne/brownian-motion/blob/8fd8dc52830cdd07cf9cc8eadd533e284425fa6f/blueprint/src/chapters/filtration_martingale.tex#L741)
